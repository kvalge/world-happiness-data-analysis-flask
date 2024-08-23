import statsmodels.api as sm

from data.data_preprocessing import data_preprocessing

df = data_preprocessing()


def linear_regression_model():
    X = df[['gdp', 'social_support', 'healthy_life', 'life_choices_freedom',
            'generosity', 'corruption', 'positive_affect', 'negative_affect']]
    y = df['life_ladder']

    X = sm.add_constant(X)

    model = sm.OLS(y, X).fit()

    print(model.summary())


def linear_regression_model_2():
    X = df[['gdp', 'social_support', 'healthy_life', 'life_choices_freedom',
            'generosity', 'corruption', 'positive_affect']]
    y = df['life_ladder']

    X = sm.add_constant(X)

    model = sm.OLS(y, X).fit()

    print(model.summary())


linear_regression_model()
linear_regression_model_2()
