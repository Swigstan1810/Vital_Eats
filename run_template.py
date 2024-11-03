import wx
import wx.grid
import wx.xrc
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import os
import gettext

from nutrition_dashboard import MyFrame1, MyFrame2, MyFrame3, MyFrame4, MyFrame5, MyFrame6

_ = gettext.gettext


def on_search(frame):
    """Handles food search and updates the nutritional information."""
    if frame.data is None:
        wx.MessageBox('No CSV file loaded!', 'Error', wx.OK | wx.ICON_ERROR)
        return

    search_query = frame.search_ctrl.GetValue().strip()  # Get input from the search field

    if not search_query:
        wx.MessageBox('Please enter a food item to search.', 'Warning', wx.OK | wx.ICON_WARNING)
        return

    result = frame.data[frame.data['food'].str.contains(search_query, case=False, na=False)]  # Search for the food item

    if not result.empty:
        # Update static text labels with nutritional data
        frame.m_staticText1.SetLabel(f"Total Fat: {result['Fat'].values[0]} g")
        frame.m_staticText2.SetLabel(f"Total Protein: {result['Protein'].values[0]} g")
        frame.m_staticText3.SetLabel(f"Total Calories: {result['Caloric Value'].values[0]}")
        frame.m_staticText4.SetLabel(f"Total Sugars: {result['Sugars'].values[0]} g")

        # Update chart with new data
        show_pie_chart(frame, result)
    else:
        wx.MessageBox('Food not found!', 'Info', wx.OK | wx.ICON_INFORMATION)


def show_pie_chart(frame, result):
    """Displays a pie chart representing the nutritional breakdown."""
    fig, ax = plt.subplots()

    labels = ['Fat', 'Carbohydrates', 'Protein', 'Sugars']
    sizes = [
        result['Fat'].values[0],
        result['Carbohydrates'].values[0],
        result['Protein'].values[0],
        result['Sugars'].values[0]
    ]

    colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']

    filtered_labels = [label for label, size in zip(labels, sizes) if size > 0]
    filtered_sizes = [size for size in sizes if size > 0]

    if not filtered_sizes:
        wx.MessageBox('All values are 0.0g, no chart to display.', 'Info', wx.OK | wx.ICON_INFORMATION)
        return

    explode = [0.1 if size == max(filtered_sizes) else 0 for size in filtered_sizes]
    ax.pie(filtered_sizes, labels=filtered_labels, colors=colors, autopct='%1.1f%%', startangle=90, explode=explode,
           shadow=True)

    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    frame.chart_sizer.Clear(True)
    canvas = FigureCanvas(frame.chart_panel, -1, fig)
    frame.chart_sizer.Add(canvas, 1, wx.EXPAND | wx.ALL, 5)
    frame.chart_panel.Layout()


def load_csv_file(frame):
    """Load the CSV data for the progress chart."""
    try:
        # Example: Load a sample CSV file with food nutrient data (replace with the actual file path)
        return pd.read_csv('Food_Nutrition_Dataset.csv')
    except FileNotFoundError:
        wx.MessageBox('CSV file not found!', 'Error', wx.OK | wx.ICON_ERROR)
        return None


def onViewProgress(frame):
    """Displays a progress chart when the 'View Meals' button is clicked."""
    show_diet_plan_graph(frame)


def show_diet_plan_graph(frame):
    """Generates a bar chart for healthier food choices based on nutrients."""
    fig, ax = plt.subplots()

    # Define healthy food criteria
    healthy_foods = frame.data[
        (frame.data['Saturated Fats'] < 3) &
        (frame.data['Sugars'] < 5) &
        (frame.data['Protein'] > 5)
        ]

    if healthy_foods.empty:
        wx.MessageBox('No healthy foods found in the dataset.', 'Info', wx.OK | wx.ICON_INFORMATION)
        return

    # Randomly select 10 healthy foods
    if len(healthy_foods) > 10:
        healthy_foods = healthy_foods.sample(n=10, random_state=42)  # Randomly pick 10 foods

    # Get the food names and nutrients for plotting
    food_names = healthy_foods['food']
    fat_values = healthy_foods['Fat']
    protein_values = healthy_foods['Protein']
    carb_values = healthy_foods['Carbohydrates']
    sugar_values = healthy_foods['Sugars']

    # Create a bar chart to show fat, protein, carbohydrates, and sugars for each healthy food
    bar_width = 0.2  # Width of each bar
    index = range(len(food_names))  # X-axis positions

    # Plot each macronutrient with a shift in the index for side-by-side bars
    ax.bar(index, fat_values, bar_width, label='Fat')
    ax.bar([i + bar_width for i in index], protein_values, bar_width, label='Protein')
    ax.bar([i + 2 * bar_width for i in index], carb_values, bar_width, label='Carbohydrates')
    ax.bar([i + 3 * bar_width for i in index], sugar_values, bar_width, label='Sugars')

    # Set labels and title
    ax.set_xlabel('Healthy Foods')
    ax.set_ylabel('Nutrient Content (grams)')
    ax.set_title('Nutrient Content of Healthier Foods')
    ax.set_xticks([i + 1.5 * bar_width for i in index])
    ax.set_xticklabels(food_names, rotation=90)  # Rotate food names for readability
    ax.legend()

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Clear previous chart and draw the new one
    frame.chart_sizer.Clear(True)
    canvas = FigureCanvas(frame.chart_panel, -1, fig)
    frame.chart_sizer.Add(canvas, 1, wx.EXPAND | wx.ALL, 5)
    frame.chart_panel.Layout()


def load_data(frame):
    """Loads the dataset from a CSV file."""
    try:
        # Update the path to your CSV file
        frame.data = pd.read_csv('Food_Nutrition_Dataset.csv')
        return frame.data
    except FileNotFoundError:
        wx.MessageBox('CSV file not found!', 'Error', wx.OK | wx.ICON_ERROR)
        return None


def onSearchFilter(frame):
    """Handles the search button click to filter the data."""
    # Get the selected nutrient, minimum, and maximum values
    nutrient = frame.m_choice1.GetString(frame.m_choice1.GetSelection())
    max_val = frame.m_textCtrl1.GetValue()
    min_val = frame.m_textCtrl3.GetValue()

    try:
        # Convert input to floats for comparison
        max_val = float(max_val)
        min_val = float(min_val)
    except ValueError:
        wx.MessageBox('Please enter valid numeric values for minimum and maximum.', 'Error',
                      wx.OK | wx.ICON_ERROR)
        return

    # Apply the filter to the dataset
    filtered_data = frame.data[(frame.data[nutrient] >= min_val) & (frame.data[nutrient] <= max_val)]

    if filtered_data.empty:
        wx.MessageBox('No foods found for the given range.', 'Info', wx.OK | wx.ICON_INFORMATION)
    else:
        # Update grid to display the filtered results
        update_grid1(frame, filtered_data)


def update_grid(frame, filtered_data):
    """Updates the grid with filtered data."""
    # Keep only the columns you want to display
    columns_to_display = ['food', 'Fat', 'Protein', 'Carbohydrates', 'Sugars']
    filtered_data = filtered_data[columns_to_display]

    required_rows = len(filtered_data)
    required_cols = len(columns_to_display)

    # Resize the grid columns if necessary
    current_cols = frame.m_grid1.GetNumberCols()
    if current_cols < required_cols:
        frame.m_grid1.AppendCols(required_cols - current_cols)
    elif current_cols > required_cols:
        frame.m_grid1.DeleteCols(0, current_cols - required_cols)

    # Resize the grid rows if necessary
    current_rows = frame.m_grid1.GetNumberRows()
    if current_rows < required_rows:
        frame.m_grid1.AppendRows(required_rows - current_rows)
    elif current_rows > required_rows:
        frame.m_grid1.DeleteRows(0, current_rows - required_rows)

    # Clear the grid contents
    frame.m_grid1.ClearGrid()

    # Set column labels
    frame.m_grid1.SetColLabelValue(0, "Food")
    frame.m_grid1.SetColLabelValue(1, "Fat")
    frame.m_grid1.SetColLabelValue(2, "Protein")
    frame.m_grid1.SetColLabelValue(3, "Carbs")
    frame.m_grid1.SetColLabelValue(4, "Sugars")

    # Populate the grid with filtered data
    for row_idx in range(required_rows):
        for col_idx in range(required_cols):
            value = filtered_data.iloc[row_idx, col_idx]  # Access the DataFrame by row/col
            frame.m_grid1.SetCellValue(row_idx, col_idx, str(value))





