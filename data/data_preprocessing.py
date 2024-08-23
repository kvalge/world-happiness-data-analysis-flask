import pandas as pd

from data.read_data import read_data


def data_preprocessing():
    source_data = read_data()

    source_data['year'] = pd.to_datetime(source_data['year'], format='%Y')

    data = source_data.dropna().copy()
    data = data[data['Country name'] != 'Haiti']

    data.rename(columns={'Country name': 'country',
                         'Life Ladder': 'life_ladder',
                         'Log GDP per capita': 'gdp',
                         'Social support': 'social_support',
                         'Healthy life expectancy at birth': 'healthy_life',
                         'Freedom to make life choices': 'life_choices_freedom',
                         'Generosity': 'generosity',
                         'Perceptions of corruption': 'corruption',
                         'Positive affect': 'positive_affect',
                         'Negative affect': 'negative_affect',
                         },
                inplace=True)

    return data
