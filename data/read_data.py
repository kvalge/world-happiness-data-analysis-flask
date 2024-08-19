import pandas as pd


def read_data():
    try:
        data = pd.read_excel('data/world_happiness.xls')
        return data

    except Exception as e:
        message = f"Error reading file: {e}"
        return message
