###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################
import wx
import wx.grid
import wx.xrc
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
import os
import gettext

from M2 import run_template

_ = gettext.gettext

# Function to load CSV data
def load_csv_file():
    try:
        # Try to load the file if it's in the current directory
        file_path = 'Food_Nutrition_Dataset.csv'
        if not os.path.exists(file_path):
            raise FileNotFoundError
        return pd.read_csv(file_path)
    except FileNotFoundError:
        return None

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="Dashboard", pos=wx.DefaultPosition, size=(500, 300),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        # Professional dark background color
        self.SetBackgroundColour(wx.Colour(45, 45, 48))  # Dark grey background

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        wSizer1 = wx.WrapSizer(wx.VERTICAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        # Buttons with a modern style
        self.m_button1 = wx.Button(self, wx.ID_ANY, "Diet Plan", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button1.SetForegroundColour(wx.Colour(255, 255, 255))  # White text
        self.m_button1.SetBackgroundColour(wx.Colour(0, 122, 204))  # Blue background
        self.m_button1.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        wSizer1.Add(self.m_button1, 0, wx.ALL, 5)

        self.m_button2 = wx.Button(self, wx.ID_ANY, "Calorie Count", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button2.SetForegroundColour(wx.Colour(255, 255, 255))  # White text
        self.m_button2.SetBackgroundColour(wx.Colour(0, 122, 204))  # Blue background
        self.m_button2.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        wSizer1.Add(self.m_button2, 0, wx.ALL, 5)

        self.m_button3 = wx.Button(self, wx.ID_ANY, "Nutrition Range Filter", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button3.SetForegroundColour(wx.Colour(255, 255, 255))  # White text
        self.m_button3.SetBackgroundColour(wx.Colour(0, 122, 204))  # Blue background
        self.m_button3.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        wSizer1.Add(self.m_button3, 0, wx.ALL, 5)

        self.m_button10 = wx.Button(self, wx.ID_ANY, "Nutrition Level Filter", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button10.SetForegroundColour(wx.Colour(255, 255, 255))  # White text
        self.m_button10.SetBackgroundColour(wx.Colour(0, 122, 204))  # Blue background
        self.m_button10.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        wSizer1.Add(self.m_button10, 0, wx.ALL, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, "View Progress", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button11.SetForegroundColour(wx.Colour(255, 255, 255))  # White text
        self.m_button11.SetBackgroundColour(wx.Colour(0, 122, 204))  # Blue background
        self.m_button11.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        wSizer1.Add(self.m_button11, 0, wx.ALL, 5)

        bSizer1.Add(wSizer1, 1, wx.EXPAND, 5)
        self.SetSizer(bSizer1)
        self.Layout()
        self.Centre(wx.BOTH)

        # Bind events to button clicks
        self.m_button1.Bind(wx.EVT_BUTTON, self.on_diet_plan)
        self.m_button2.Bind(wx.EVT_BUTTON, self.on_calorie_count)
        self.m_button3.Bind(wx.EVT_BUTTON, self.on_nutrition_range_filter)  # Bind Nutrition Range Filter button
        self.m_button10.Bind(wx.EVT_BUTTON, self.on_nutrition_level_filter)  # Bind Nutrition Level Filter button
        self.m_button11.Bind(wx.EVT_BUTTON, self.on_view_progress)  # Bind View Progress button

    def on_diet_plan(self, event):
        frame = MyFrame3(self)
        frame.Show()

    def on_calorie_count(self, event):
        frame = MyFrame2(self)
        frame.Show()

    def on_nutrition_range_filter(self, event):
        frame = MyFrame4(self)
        frame.Show()

    def on_nutrition_level_filter(self, event):
        frame = MyFrame5(self)
        frame.Show()

    def on_view_progress(self, event):
        frame = MyFrame6(self)
        frame.Show()


    def __del__(self):
        pass



###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="Calorie Count", pos=wx.DefaultPosition, size=wx.Size(600, 400),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(45, 45, 48))  # Dark grey background


        bSizer2 = wx.BoxSizer(wx.VERTICAL)


        gSizer1 = wx.GridSizer(0, 2, 0, 0)


        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, _(u"Total Fat"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.SetForegroundColour(wx.Colour(255, 255, 255))  # White text
        gSizer1.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, _(u"Total Protein"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.SetForegroundColour(wx.Colour(255, 255, 255))  # White text
        gSizer1.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, _(u"Total Calories"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.SetForegroundColour(wx.Colour(255, 255, 255))  # White text
        gSizer1.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, _(u"Total Sugars"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.SetForegroundColour(wx.Colour(255, 255, 255))  # White text
        gSizer1.Add(self.m_staticText4, 0, wx.ALL, 5)


        self.search_ctrl = wx.TextCtrl(self, wx.ID_ANY, "", wx.DefaultPosition, wx.Size(200, 30), style=wx.BORDER_SIMPLE)
        self.search_ctrl.SetBackgroundColour(wx.Colour(70, 70, 75))  # Darker text field
        self.search_ctrl.SetForegroundColour(wx.Colour(255, 255, 255))  # Light text in search box
        gSizer1.Add(self.search_ctrl, 0, wx.ALL, 5)


        self.m_button4 = wx.Button(self, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button4.SetForegroundColour(wx.Colour(255, 255, 255))  # White text
        self.m_button4.SetBackgroundColour(wx.Colour(0, 122, 204))  # Blue button
        self.m_button4.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        gSizer1.Add(self.m_button4, 0, wx.ALL, 5)


        bSizer2.Add(gSizer1, 1, wx.EXPAND, 5)


        self.chart_panel = wx.Panel(self, size=(400, 200))
        self.chart_panel.SetBackgroundColour(wx.Colour(60, 60, 65))
        self.chart_sizer = wx.BoxSizer(wx.VERTICAL)
        self.chart_panel.SetSizer(self.chart_sizer)
        bSizer2.Add(self.chart_panel, 1, wx.EXPAND | wx.ALL, 5)


        self.SetSizer(bSizer2)
        self.Layout()
        self.Centre(wx.BOTH)


        self.m_button4.Bind(wx.EVT_BUTTON, self.on_search)

        # Bind search button to on_search method
        self.m_button4.Bind(wx.EVT_BUTTON, self.on_search)

        # Load CSV file when initializing the frame
        self.data = self.load_csv_file()
        if self.data is None:
            self.select_file_dialog()  # Ask user to select the file if not found

    def load_csv_file(self):
        """Attempt to load the CSV file."""
        try:
            return pd.read_csv('Food_Nutrition_Dataset.csv')
        except FileNotFoundError:
            wx.MessageBox('CSV file not found!', 'Error', wx.OK | wx.ICON_ERROR)
            return None

    def select_file_dialog(self):
        """Prompts the user to select a CSV file if not found."""
        with wx.FileDialog(self, "Open CSV file", wildcard="CSV files (*.csv)|*.csv",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # The user canceled the file selection

            file_path = fileDialog.GetPath()

            try:
                self.data = pd.read_csv(file_path)
            except Exception as e:
                wx.LogError(f"Cannot open file '{file_path}': {e}")

    def on_search(self, event):
        """Trigger search function in the run_template module."""
        run_template.on_search(self)



    def __del__(self):
        pass

###########################################################################
## Class MyFrame3
###########################################################################
class MyFrame3(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="Diet Plan Progress", pos=wx.DefaultPosition,
                          size=wx.Size(600, 400),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)


        bSizer13 = wx.BoxSizer(wx.HORIZONTAL)


        self.m_button9 = wx.Button(self, wx.ID_ANY, _(u"View Meals"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer13.Add(self.m_button9, 0, wx.ALL, 5)


        self.SetSizer(bSizer13)
        self.Layout()
        self.Centre(wx.BOTH)


        self.m_button9.Bind(wx.EVT_BUTTON, self.onViewProgress)


        self.data = self.load_csv_file()


        self.chart_panel = wx.Panel(self, size=(500, 300))
        self.chart_panel.SetBackgroundColour(wx.Colour(60, 60, 65))  # Dark grey chart background
        self.chart_sizer = wx.BoxSizer(wx.VERTICAL)
        self.chart_panel.SetSizer(self.chart_sizer)
        bSizer13.Add(self.chart_panel, 1, wx.EXPAND | wx.ALL, 5)

    def load_csv_file(self):
        """Load the CSV data for the progress chart."""
        return run_template.load_csv_file(self)

    def onViewProgress(self, event):
        """Displays a progress chart when the 'View Meals' button is clicked."""
        run_template.onViewProgress(self)

    def __del__(self):
        pass


###########################################################################
## Class MyFrame4
###########################################################################

class MyFrame4 ( wx.Frame ):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="Nutritional Level Filter", pos=wx.DefaultPosition,
                          size=wx.Size(644, 308),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, _(u"Nutrition Check"), wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)

        bSizer5.Add(self.m_staticText7, 0, wx.ALL, 5)

        # Define choices for nutrients (for example, these are columns in your dataset)
        m_choice1Choices = ['Fat', 'Protein', 'Carbohydrates', 'Sugars', 'Saturated Fats']
        self.m_choice1 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0)
        self.m_choice1.SetSelection(0)
        bSizer5.Add(self.m_choice1, 0, wx.ALL, 5)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, _(u"Maximum"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)

        bSizer5.Add(self.m_staticText8, 0, wx.ALL, 5)

        self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(240,25), 0)
        bSizer5.Add(self.m_textCtrl1, 0, wx.ALL, 5)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, _(u"Minimum"), wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)

        bSizer5.Add(self.m_staticText9, 0, wx.ALL, 5)

        self.m_textCtrl3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(240,25), 0)
        bSizer5.Add(self.m_textCtrl3, 0, wx.ALL, 5)

        self.m_button5 = wx.Button(self, wx.ID_ANY, _(u"Search"), wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_button5, 0, wx.ALL, 5)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)
        bSizer5.Add(bSizer6, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer5, 1, wx.EXPAND, 5)

        # Create a grid to display filtered data
        self.m_grid1 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Initial grid setup
        self.m_grid1.CreateGrid(5, 5)  # Default size
        self.m_grid1.EnableEditing(True)
        self.m_grid1.EnableGridLines(True)
        self.m_grid1.EnableDragGridSize(False)
        self.m_grid1.SetMargins(0, 0)

        # Columns
        self.m_grid1.EnableDragColMove(False)
        self.m_grid1.EnableDragColSize(True)
        self.m_grid1.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.m_grid1.EnableDragRowSize(True)
        self.m_grid1.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Set grid label names
        self.m_grid1.SetColLabelValue(0, "Food")
        self.m_grid1.SetColLabelValue(1, "Fat")
        self.m_grid1.SetColLabelValue(2, "Protein")
        self.m_grid1.SetColLabelValue(3, "Carbs")
        self.m_grid1.SetColLabelValue(4, "Sugars")

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer1.Add(self.m_grid1, 0, wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        self.Centre(wx.BOTH)

        # Bind search button to the event handler
        self.m_button5.Bind(wx.EVT_BUTTON, self.onSearchFilter)

        # Load data into a DataFrame (replace with your actual dataset)
        self.data = self.load_data()

    def load_data(self):
        """Loads the dataset from a CSV file."""
        return run_template.load_data(self)

    def onSearchFilter(self, event):
        run_template.onSearchFilter(self)

    def update_grid(self, filtered_data):
        run_template.update_grid1(self, filtered_data)

    def __del__(self):
        pass


###########################################################################n
## Class MyFrame5
###########################################################################

class MyFrame5(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="Nutrition Level Filter", pos=wx.DefaultPosition,
                          size=(737, 274), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)
        bSizer8 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText10 = wx.StaticText(self, wx.ID_ANY, "Nutrient Type:-", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText10.Wrap(-1)
        bSizer8.Add(self.m_staticText10, 0, wx.ALL, 5)

        m_choice2Choices = ['Fat', 'Protein', 'Carbohydrates', 'Sugars', 'Nutrition Density']
        self.m_choice2 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0)
        self.m_choice2.SetSelection(0)
        bSizer8.Add(self.m_choice2, 0, wx.ALL, 5)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, "Nutrient Level", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        bSizer8.Add(self.m_staticText11, 0, wx.ALL, 5)

        m_choice3Choices = ['Low', 'Mid', 'High']
        self.m_choice3 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0)
        self.m_choice3.SetSelection(0)
        bSizer8.Add(self.m_choice3, 0, wx.ALL, 5)

        self.m_button7 = wx.Button(self, wx.ID_ANY, "Search", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button7.Bind(wx.EVT_BUTTON, self.on_search)
        bSizer8.Add(self.m_button7, 0, wx.ALL, 5)

        self.m_button8 = wx.Button(self, wx.ID_ANY, "Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button8.Bind(wx.EVT_BUTTON, self.on_cancel)
        bSizer8.Add(self.m_button8, 0, wx.ALL, 5)

        bSizer7.Add(bSizer8, 1, wx.EXPAND, 5)

        self.m_grid2 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_grid2.CreateGrid(5, 5)
        self.m_grid2.EnableEditing(True)
        self.m_grid2.EnableGridLines(True)
        self.m_grid2.SetMargins(0, 0)

        self.m_grid2.EnableDragColMove(False)
        self.m_grid2.EnableDragColSize(True)
        self.m_grid2.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        self.m_grid2.EnableDragRowSize(True)
        self.m_grid2.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        self.m_grid2.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)

        bSizer7.Add(self.m_grid2, 0, wx.ALL, 5)

        self.SetSizer(bSizer7)
        self.Layout()
        self.Centre(wx.BOTH)

    def on_search(self, event):
        """Handles the search button click event."""
        global filtered_data
        nutrient_type = self.m_choice2.GetString(self.m_choice2.GetSelection())
        level = self.m_choice3.GetString(self.m_choice3.GetSelection())

        # Load your data
        data = self.load_data()

        # Calculate the maximum values for nutrients to define levels
        max_values = {
            'Fat': data['Fat'].max(),
            'Protein': data['Protein'].max(),
            'Carbohydrates': data['Carbohydrates'].max(),
            'Sugars': data['Sugars'].max(),
            'Nutrition Density': data['Nutrition Density'].max()
        }

        # Define thresholds
        low_thresholds = {key: value * 0.33 for key, value in max_values.items()}
        mid_thresholds = {key: value * 0.66 for key, value in max_values.items()}

        # Filter based on selected nutrient type and level
        if level == 'Low':
            filtered_data = data[data[nutrient_type] < low_thresholds[nutrient_type]]
        elif level == 'Mid':
            filtered_data = data[
                (data[nutrient_type] >= low_thresholds[nutrient_type]) &
                (data[nutrient_type] <= mid_thresholds[nutrient_type])
                ]
        elif level == 'High':
            filtered_data = data[data[nutrient_type] > mid_thresholds[nutrient_type]]

        # Print filtered data shape for debugging
        print(f"Filtered data shape: {filtered_data.shape}")

        # Update grid with filtered data
        self.update_grid(filtered_data)

    def on_cancel(self, event):
        """Handles the cancel button click event."""
        self.Close()

    def load_data(self):
        """Loads data from a CSV file. Modify this method to load your actual data."""
        return pd.read_csv('Food_Nutrition_Dataset.csv')

    def update_grid(self, filtered_data):
        """Updates the grid with filtered data."""
        self.m_grid2.ClearGrid()  # Clear existing data

        # Ensure the filtered data contains only the desired columns
        filtered_data = filtered_data[['food', 'Fat', 'Protein', 'Carbohydrates', 'Sugars', 'Nutrition Density']]

        # Get the number of rows and columns
        num_rows = len(filtered_data)
        num_cols = len(filtered_data.columns)

        # Adjust the grid size based on the filtered data
        current_rows = self.m_grid2.GetNumberRows()
        current_cols = self.m_grid2.GetNumberCols()

        # Adjust the number of columns if necessary
        if num_cols > current_cols:
            self.m_grid2.AppendCols(num_cols - current_cols)
        elif num_cols < current_cols:
            self.m_grid2.DeleteCols(0, current_cols - num_cols)

        # Adjust the number of rows if necessary
        if num_rows > current_rows:
            self.m_grid2.AppendRows(num_rows - current_rows)
        elif num_rows < current_rows:
            self.m_grid2.DeleteRows(0, current_rows - num_rows)

        # Set the column labels (only needs to be done once, typically after creation)
        column_labels = list(filtered_data.columns)
        for col_idx in range(num_cols):
            self.m_grid2.SetColLabelValue(col_idx, column_labels[col_idx])

        # Populate the grid with filtered data
        for row_idx in range(num_rows):
            row = filtered_data.iloc[row_idx]  # Use iloc to get the row by integer index
            for col_idx in range(num_cols):
                self.m_grid2.SetCellValue(row_idx, col_idx, str(row[col_idx]))

        # Optional: Resize the grid after populating
        self.m_grid2.AutoSize()

    def __del__(self):
        pass


###########################################################################
## Class MyFrame6
###########################################################################

class MyFrame6 ( wx.Frame ):


    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title="DataFeed",
                          pos=wx.DefaultPosition, size=wx.Size(600, 400),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        # Layout components
        bSizer14 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText13 = wx.StaticText(self, wx.ID_ANY, "My Top Meals", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText13.Wrap(-1)
        bSizer14.Add(self.m_staticText13, 0, wx.ALL, 5)

        # Add a button to trigger view progress
        self.m_button9 = wx.Button(self, wx.ID_ANY, "View Progress", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button9.Bind(wx.EVT_BUTTON, self.on_view_progress)
        bSizer14.Add(self.m_button9, 0, wx.ALL, 5)

        # Create a placeholder for the plot
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self, -1, self.figure)
        bSizer14.Add(self.canvas, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer14)
        self.Layout()
        self.Centre(wx.BOTH)

    def on_view_progress(self, event):
        """Handles the View Progress button click."""
        # Simulate loading of the dataset
        data = self.load_data()

        # Plot the nutrient intake over time
        self.plot_nutritional_progress(data)

    def load_data(self):
        """Simulate loading top meal data."""
        # Simulating some sample data for demonstration. Replace with actual data loading.
        data = {
            'Meal': ['Meal 1', 'Meal 2', 'Meal 3', 'Meal 4'],
            'Date': ['2024-10-01', '2024-10-02', '2024-10-03', '2024-10-04'],
            'Fat': [20, 15, 25, 10],
            'Protein': [30, 40, 35, 25],
            'Carbohydrates': [100, 90, 120, 80],
            'Sugars': [50, 40, 60, 30],
        }
        return pd.DataFrame(data)

    def plot_nutritional_progress(self, data):
        """Generates a plot to visualize nutritional progress."""
        # Clear the existing plot
        self.figure.clear()

        # Create a new axis
        ax = self.figure.add_subplot(111)

        # Convert 'Date' to datetime for better plotting
        data['Date'] = pd.to_datetime(data['Date'])

        # Plot each nutrient over time
        ax.plot(data['Date'], data['Fat'], label='Fat', marker='o')
        ax.plot(data['Date'], data['Protein'], label='Protein', marker='o')
        ax.plot(data['Date'], data['Carbohydrates'], label='Carbohydrates', marker='o')
        ax.plot(data['Date'], data['Sugars'], label='Sugars', marker='o')

        # Customize the plot
        ax.set_title('Nutrient Intake Over Time')
        ax.set_xlabel('Date')
        ax.set_ylabel('Amount (grams)')
        ax.legend()

        # Refresh the canvas to show the new plot
        self.canvas.draw()

    def __del__( self ):
        pass





if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame1(None)
    frame.Show()
    app.MainLoop()
