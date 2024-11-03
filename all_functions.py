import pandas as pd


# Function to read the CSV file
def read_data_file_csv(filepath='Food_Nutrition_Dataset.csv'):
    """
    Reads a CSV file and returns the DataFrame. In case of an error, it returns None.

    Args:
    filepath (str): Path to the CSV file. Defaults to 'Food_Nutrition_Dataset.csv'.

    Returns:
    pd.DataFrame or None: DataFrame containing the CSV data or None if an error occurs.
    """
    try:
        return pd.read_csv(filepath)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None


# Function to get records in the dataframe based on food name
def get_records_in_dataframe(food, df):
    """
    Filters the DataFrame for rows that match the given food name.

    Args:
        food (str): The name of the food to filter by.
        df (pd.DataFrame): The DataFrame containing the food data.

    Returns:
        pd.DataFrame: A DataFrame containing the matching rows or an empty DataFrame if no match.
    """
    # First, validate the inputs
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Invalid input. Expected a pandas DataFrame for 'df'.")

    if not isinstance(food, str) or not food:
        raise TypeError("Invalid input. Expected a non-empty string for 'food'.")

    # Now check if 'food' column exists in the DataFrame
    if 'food' not in df.columns:
        raise KeyError("'food' column is not present in the DataFrame.")

    # Filter for the matching food name
    return df[df['food'] == food].reset_index(drop=True)  # reset_index for a cleaner result


# Function to get the sum of nutritional values for a specific food
def get_sum_value_in_dataframe(food, df):
    """
    Returns the sum of 'nutrition_value' for a given food, or 0 if food is not found.

    Args:
        food (str): The name of the food.
        df (pd.DataFrame): The DataFrame containing food data.

    Returns:
        float: Sum of the 'nutrition_value', or 0 if food is not found or an error occurs.
    """
    # Check if food is a string

    # Check if df is a pandas DataFrame
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Expected a pandas DataFrame.")


    # Sum 'nutrition_value' for the matching food
    return df.loc[df['food'] == food, 'nutrition_value'].sum() if not df.empty else 0


# Function to filter data by a nutrition range
def get_nutrition_range_filter(nutrient, min_value, max_value, df):
    """
    Filters the DataFrame for rows where the value of a specific nutrient falls within the specified range.

    Args:
    nutrient (str): The nutrient to filter by (e.g., 'Fat', 'Protein').
    min_value (float): The minimum value of the range.
    max_value (float): The maximum value of the range.
    df (pd.DataFrame): The DataFrame containing the food data.

    Returns:
    pd.DataFrame: A DataFrame containing the matching rows or an empty DataFrame in case of an error.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Expected a pandas DataFrame.")
    try:
        return df[(df[nutrient] >= min_value) & (df[nutrient] <= max_value)]
    except (KeyError, IndexError, TypeError) as e:
        print(f"Error filtering data by {nutrient}: {e}")
        return pd.DataFrame()


# Function to get the highest and lowest values for a given nutrient
def get_highest_lowest_nutrition_level_filter(nutrient, df):
    """
    Retrieves the minimum and maximum values of a specific nutrient in the DataFrame.

    Args:
    nutrient (str): The nutrient to retrieve the min and max values for.
    df (pd.DataFrame): The DataFrame containing the food data.

    Returns:
    tuple: A tuple containing the minimum and maximum values or (0, 0) in case of an error.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Expected a pandas DataFrame.")
    try:
        return df[nutrient].min(), df[nutrient].max()
    except (KeyError, IndexError, TypeError) as e:
        print(f"Error retrieving highest and lowest values for {nutrient}: {e}")
        return 0, 0


# Function to get the top 5 foods with maximum nutrient value
def get_list_5food_max_nutrition(nutrient, df):
    """
    Retrieves the top 5 foods with the highest values for a specific nutrient.

    Args:
    nutrient (str): The nutrient to sort by.
    df (pd.DataFrame): The DataFrame containing the food data.

    Returns:
    pd.DataFrame: A DataFrame containing the top 5 foods sorted by nutrient value in descending order.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Expected a pandas DataFrame.")
    try:
        return df[['food', nutrient]].sort_values(by=nutrient, ascending=False).head(5)
    except (KeyError, IndexError, TypeError) as e:
        print(f"Error retrieving top 5 foods by {nutrient}: {e}")
        return pd.DataFrame()


# Function to get the top 5 foods with minimum nutrient value
def get_list_5food_min_nutrition(nutrient, df):
    """
    Retrieves the top 5 foods with the lowest values for a specific nutrient.

    Args:
    nutrient (str): The nutrient to sort by.
    df (pd.DataFrame): The DataFrame containing the food data.

    Returns:
    pd.DataFrame: A DataFrame containing the top 5 foods sorted by nutrient value in ascending order.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Expected a pandas DataFrame.")
    try:
        return df[['food', nutrient]].sort_values(by=nutrient, ascending=True).head(5)
    except (KeyError, IndexError, TypeError) as e:
        print(f"Error retrieving bottom 5 foods by {nutrient}: {e}")
        return pd.DataFrame()


# Function to compare nutrition values between two foods
def get_two_foods_with_nutritions(food1, food2, df):
    """
    Retrieves the nutrition records for two foods.

    Args:
        food1 (str): The name of the first food.
        food2 (str): The name of the second food.
        df (pd.DataFrame): The DataFrame containing the food data.

    Returns:
        pd.DataFrame: A DataFrame containing the records for both foods, or an empty DataFrame if not found.
    """
    # Validate inputs
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Expected a pandas DataFrame.")


    # Filter the DataFrame for the two foods
    records = df[df['food'].isin([food1, food2])]

    return records if not records.empty else pd.DataFrame()

