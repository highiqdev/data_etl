#functions to extract, transform, and load data for automation pipelines.
import pandas

DF = pandas.read_csv("csv_file_location.csv")
CITY = "city_name" #city to filter by

def filter_by_city(df: df, city: str):
    """
    Filters a dataframe by city.
    :param df: The dataframe to filter.
    :param city: The city to filter by, where 'city' is the column name.
    """
    return df[df["city"] == city]


def split_into_csvs(df: df, split_length: int):
    """
    Splits a dataframe into multiple csvs.
    :param df: The dataframe to split.
    :param split_length: The length of each split.
    """
    for i in range(0, len(df), split_length):
        df[i:i + split_length].to_csv(f"split_{i}.csv", index=False)