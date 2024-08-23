import pandas as pd


def read_data():
    try:
        countries_data = pd.read_excel('data/world_happiness.xls')
        continents_data = pd.read_excel('data/continents.xlsx')
        data = pd.merge(countries_data, continents_data, left_on='Country name', right_on='Country', how='left')

        return data

    except Exception as e:
        message = f"Error reading file: {e}"
        return message
