import pandas as pd

from data.read_data import read_data
from data.data_preprocessing import data_preprocessing


def inspect_data():
    data = read_data()
    file = open('insight/basic_insight.txt', 'w')

    read_to_file(data, file)

    file.close()


def inspect_cleaned_data():
    data = data_preprocessing()
    file = open('insight/basic_insight_clean_data.txt', 'w')

    excluded_countries(file)
    read_to_file(data, file)

    file.close()


def read_to_file(data, file):
    file.write(f'Number of rows and columns: \n{data.shape}\n' + '\n')
    file.write(f'Column types: \n{data.dtypes}\n' + '\n')

    country_column = ''
    if 'Country name' in data.columns:
        country_column = 'Country name'
    if 'country' in data.columns:
        country_column = 'country'

    file.write(f'Number of countries: \n{len(pd.unique(data[country_column]))}\n' + '\n')

    file.write(f'Number of duplicates: {data.duplicated().sum()}\n' + '\n')

    file.write(f'Summary:' + '\n')
    summary = data.describe()
    summary = summary.iloc[:, 1:]
    for column in summary:
        file.write(f'Column: {column} \n{summary[column]}\n' + '\n')

    file.write(f'Total missing values: \n{data.isnull().sum().sum()}\n' + '\n')
    file.write(f'Missing values per variable: \n{data.isnull().sum()}\n' + '\n')


def excluded_countries(file):
    countries_source = pd.unique(read_data()['Country name'])
    countries_cleaned = pd.unique(data_preprocessing()['country'])

    file.write(f'Countries excluded due to missing data:\n')
    for c in countries_source:
        if c not in countries_cleaned:
            file.write(f' - {c}\n')
    file.write('\n')

