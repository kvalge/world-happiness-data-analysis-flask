import statsmodels.api as sm

from data.data_preprocessing import data_preprocessing

df = data_preprocessing()

X = df[['gdp', 'social_support', 'healthy_life', 'life_choices_freedom',
        'generosity', 'corruption', 'positive_affect', 'negative_affect']]
y = df['life_ladder']

X = sm.add_constant(X)

model = sm.OLS(y, X).fit()

print(model.summary())