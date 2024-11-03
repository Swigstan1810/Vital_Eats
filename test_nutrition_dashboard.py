import pytest
import pandas as pd
from unittest.mock import patch
from all_functions import (
    read_data_file_csv,
    get_records_in_dataframe,
    get_sum_value_in_dataframe,
    get_nutrition_range_filter,
    get_highest_lowest_nutrition_level_filter,
    get_list_5food_max_nutrition,
    get_list_5food_min_nutrition,
    get_two_foods_with_nutritions
)

# Sample DataFrame for testing
@pytest.fixture
def sample_df():
    data = {
        'food': ['apple', 'banana', 'carrot', 'cream cheese', 'donut'],
        'nutrition_value': [50, 70, 30, 80, 100],
        'Fat': [0.2, 0.1, 0.0, 5.0, 10.0]
    }
    return pd.DataFrame(data)

# Test for read_data_file_csv
def test_read_data_file_csv_success():
    with patch('pandas.read_csv') as mock_read_csv:
        mock_read_csv.return_value = pd.DataFrame({'food': ['apple'], 'nutrition_value': [50]})
        df = read_data_file_csv()
        assert df is not None, "CSV file should be read successfully."
        assert 'food' in df.columns, "DataFrame should have a 'food' column."

def test_read_data_file_csv_failure():
    with patch('pandas.read_csv', side_effect=FileNotFoundError):
        df = read_data_file_csv()
        assert df is None, "Reading a non-existent file should return None."

# Test for get_records_in_dataframe
def test_get_records_in_dataframe():
    df = pd.DataFrame({
        'food': ['apple', 'banana', 'carrot'],
        'nutrition_value': [50, 70, 30]
    })

    result = get_records_in_dataframe('apple', df)
    assert len(result) == 1, "Should return 1 record for apple."
    assert result['food'].iloc[0] == 'apple', "The food name should match."

    result = get_records_in_dataframe('banana', df)
    assert len(result) == 1, "Should return 1 record for banana."

    result = get_records_in_dataframe('orange', df)
    assert len(result) == 0, "Should return 0 records for non-existent food."

@pytest.mark.parametrize("food", ['invalid food', 'another invalid'])
def test_get_records_in_dataframe_invalid_input(sample_df, food):
    result = get_records_in_dataframe(food, sample_df)
    assert result.empty, f"No records should be found for {food}."

def test_get_records_in_dataframe_type_error():
    with pytest.raises(TypeError):
        get_records_in_dataframe('apple', 'Not a DataFrame')

def test_get_records_in_dataframe_empty_dataframe():
    df = pd.DataFrame(columns=['food', 'nutrition_value'])
    result = get_records_in_dataframe('apple', df)
    assert result.empty, "Should return an empty DataFrame for empty input."

def test_get_records_in_dataframe_invalid_df():
    with pytest.raises(TypeError):
        get_records_in_dataframe('apple', 'not_a_dataframe')  # invalid df

# Test for invalid food input (TypeError)
def test_get_records_in_dataframe_invalid_food():
    df = pd.DataFrame({'food': ['apple', 'banana'], 'nutrition_value': [50, 70]})
    with pytest.raises(TypeError):
        get_records_in_dataframe(123, df)  # non-string food input

    with pytest.raises(TypeError):
        get_records_in_dataframe('', df)  # empty string food input

# Test for missing 'food' column (KeyError)
def test_get_records_in_dataframe_missing_food_column():
    df = pd.DataFrame({'nutrition_value': [50, 70]})  # no 'food' column
    with pytest.raises(KeyError):
        get_records_in_dataframe('apple', df)

# Test for get_sum_value_in_dataframe
def test_get_sum_value_in_dataframe(sample_df):
    result = get_sum_value_in_dataframe('banana', sample_df)
    assert result == 70, "Sum for 'banana' should be 70."

def test_get_sum_value_in_dataframe_not_found(sample_df):
    result = get_sum_value_in_dataframe('invalid food', sample_df)
    assert result == 0, "Sum for non-existent food should be 0."

def test_get_sum_value_in_dataframe_type_error():
    with pytest.raises(TypeError):
        get_sum_value_in_dataframe('apple', 'Not a DataFrame')

def test_get_sum_value_in_dataframe_empty_dataframe():
    df = pd.DataFrame(columns=['food', 'nutrition_value'])
    result = get_sum_value_in_dataframe('apple', df)
    assert result == 0, "Sum should be 0 for empty DataFrame."

# Test for get_nutrition_range_filter
def test_get_nutrition_range_filter(sample_df):
    result = get_nutrition_range_filter('nutrition_value', 50, 100, sample_df)
    assert len(result) == 4, "Should return 4 foods within the range of 50 to 100."

def test_get_nutrition_range_filter_key_error(sample_df):
    result = get_nutrition_range_filter('invalid_column', 50, 100, sample_df)
    assert result.empty, "Should return an empty DataFrame if the column is invalid."

def test_get_nutrition_range_filter_type_error():
    with pytest.raises(TypeError):
        get_nutrition_range_filter('nutrition_value', 50, 100, 'Not a DataFrame')

def test_get_nutrition_range_filter_invalid_range(sample_df):
    result = get_nutrition_range_filter('nutrition_value', 100, 50, sample_df)
    assert result.empty, "Should return an empty DataFrame for invalid range."

# Test for get_highest_lowest_nutrition_level_filter
def test_get_highest_lowest_nutrition_level_filter(sample_df):
    min_val, max_val = get_highest_lowest_nutrition_level_filter('nutrition_value', sample_df)
    assert min_val == 30, "Minimum should be 30."
    assert max_val == 100, "Maximum should be 100."

def test_get_highest_lowest_nutrition_level_filter_key_error(sample_df):
    min_val, max_val = get_highest_lowest_nutrition_level_filter('invalid_column', sample_df)
    assert min_val == 0 and max_val == 0, "Should return (0, 0) for invalid column."

def test_get_highest_lowest_nutrition_level_filter_type_error():
    with pytest.raises(TypeError):
        get_highest_lowest_nutrition_level_filter('nutrition_value', 'Not a DataFrame')

# Test for get_list_5food_max_nutrition
def test_get_list_5food_max_nutrition(sample_df):
    result = get_list_5food_max_nutrition('nutrition_value', sample_df)
    assert len(result) == 5, "Should return 5 foods."

def test_get_list_5food_max_nutrition_key_error(sample_df):
    result = get_list_5food_max_nutrition('invalid_column', sample_df)
    assert result.empty, "Should return an empty DataFrame for invalid column."

def test_get_list_5food_max_nutrition_type_error():
    with pytest.raises(TypeError):
        get_list_5food_max_nutrition('nutrition_value', 'Not a DataFrame')

# Test for get_list_5food_min_nutrition
def test_get_list_5food_min_nutrition(sample_df):
    result = get_list_5food_min_nutrition('nutrition_value', sample_df)
    assert len(result) == 5, "Should return 5 foods."

def test_get_list_5food_min_nutrition_key_error(sample_df):
    result = get_list_5food_min_nutrition('invalid_column', sample_df)
    assert result.empty, "Should return an empty DataFrame for invalid column."

def test_get_list_5food_min_nutrition_type_error():
    with pytest.raises(TypeError):
        get_list_5food_min_nutrition('nutrition_value', 'Not a DataFrame')

# Test for get_two_foods_with_nutritions
def test_get_two_foods_with_nutritions(sample_df):
    result = get_two_foods_with_nutritions('apple', 'banana', sample_df)
    assert len(result) == 2, "Should return records for both foods."

def test_get_two_foods_with_nutritions_not_found(sample_df):
    result = get_two_foods_with_nutritions('apple', 'invalid food', sample_df)
    assert len(result) == 1, "Should return record for existing food only."

def test_get_two_foods_with_nutritions_type_error():
    with pytest.raises(TypeError):
        get_two_foods_with_nutritions('apple', 'banana', 'Not a DataFrame')

def test_get_two_foods_with_nutritions_both_invalid(sample_df):
    result = get_two_foods_with_nutritions('invalid1', 'invalid2', sample_df)
    assert result.empty, "Should return an empty DataFrame when both foods are invalid."

def test_get_two_foods_with_nutritions_empty_dataframe(sample_df):
    df = pd.DataFrame(columns=['food', 'nutrition_value'])
    result = get_two_foods_with_nutritions('apple', 'banana', df)
    assert result.empty, "Should return an empty DataFrame for empty input."
