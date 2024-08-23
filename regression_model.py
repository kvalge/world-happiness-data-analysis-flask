import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
import pandas as pd

from data.data_preprocessing import data_preprocessing

df = data_preprocessing()


def linear_regression_model():
    X = df[['gdp', 'social_support', 'healthy_life', 'life_choices_freedom', 'generosity',
            'corruption', 'positive_affect', 'negative_affect', 'population', 'area']]
    y = df['life_ladder']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns, index=X.index)
    X_scaled_with_const = sm.add_constant(X_scaled_df)

    model = sm.OLS(y, X_scaled_with_const).fit()

    print(model.summary())


def linear_regression_model_2():
    X = df[['gdp', 'social_support', 'healthy_life', 'life_choices_freedom', 'generosity',
            'corruption', 'positive_affect', 'area']]
    y = df['life_ladder']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    X_scaled_df = pd.DataFrame(X_scaled, columns=X.columns, index=X.index)
    X_scaled_with_const = sm.add_constant(X_scaled_df)

    model = sm.OLS(y, X_scaled_with_const).fit()

    print(model.summary())


linear_regression_model()
linear_regression_model_2()
