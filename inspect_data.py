from data.read_data import read_data
from data.clean_data import clean_data


def inspect_data():
    data = read_data()
    file = open('insight/basic_insight.txt', 'w')

    read_to_file(data, file)


def inspect_cleaned_data():
    data = clean_data()
    file = open('insight/basic_insight_clean_data.txt', 'w')

    read_to_file(data, file)


def read_to_file(data, file):
    file.write(f'Number of rows and columns: \n{data.shape}\n' + '\n')
    file.write(f'Column types: \n{data.dtypes}\n' + '\n')

    file.write(f'Number of duplicates: {data.duplicated().sum()}\n' + '\n')

    file.write(f'Summary:' + '\n')
    summary = data.describe()
    summary = summary.iloc[:, 1:]
    for column in summary:
        file.write(f'Column: {column} \n{summary[column]}\n' + '\n')

    file.write(f'Total missing values: \n{data.isnull().sum().sum()}\n' + '\n')
    file.write(f'Missing values per variable: \n{data.isnull().sum()}\n' + '\n')
    file.close()
