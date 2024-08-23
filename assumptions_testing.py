from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from scipy.stats import shapiro, anderson
import statsmodels.api as sm
import numpy as np
from scipy.stats import boxcox
from sklearn.preprocessing import StandardScaler

from statsmodels.stats.stattools import durbin_watson
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.diagnostic import het_goldfeldquandt
from statsmodels.stats.diagnostic import het_white
from statsmodels.stats.diagnostic import acorr_ljungbox

from data.data_preprocessing import data_preprocessing

df = data_preprocessing()

X = df[['gdp', 'social_support', 'healthy_life', 'life_choices_freedom', 'generosity',
        'corruption', 'positive_affect', 'negative_affect', 'population', 'area']]
y = df['life_ladder']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

residuals = y_test - y_pred

# Find outliers
threshold = 3 * np.std(residuals)
outliers = np.where(np.abs(residuals) > threshold)[0]
outlier_data = df.iloc[outliers]
print('Outliers:\n', outlier_data)


# Testing if errors (residuals) are independent.
# The Durbin-Watson test is a common test for detecting the presence of autocorrelation
# (a situation where residuals are correlated with each other). The test statistic ranges
# from 0 to 4:
# A value of 2 indicates no autocorrelation.
# A value closer to 0 suggests positive autocorrelation.
# A value closer to 4 suggests negative autocorrelation.
dw_stat = durbin_watson(residuals)
print(f'Durbin-Watson statistic: {dw_stat}')

# Detecting autocorrelation at multiple lags. It checks whether any of a group of
# autocorrelations of the residuals are different from zero.
# A p-value > 0.05 suggests that there is no significant autocorrelation, implying that
# residuals are independent.
ljung_box_result = acorr_ljungbox(residuals, lags=[10], return_df=True)
print(f'Ljung-Box test: {ljung_box_result}')

plt.plot(residuals)
plt.title('Testing Independence of Residuals\nResiduals Over Time')
plt.xlabel('Observation Order')
plt.ylabel('Residuals')
plt.show()

# An ACF plot shows the autocorrelation of residuals with themselves at different lags.
# If residuals are independent, the autocorrelations should be close to zero for all lags.
sm.graphics.tsa.plot_acf(residuals, lags=40)
plt.title('Testing Independence of Residuals')
plt.show()

# Testing normality of residuals.

sns.histplot(residuals, kde=True)
plt.title('Residuals Histogram')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.show()

stats.probplot(residuals, dist="norm", plot=plt)
plt.title('Testing Normality of Residuals\nQ-Q Plot of Residuals')
plt.show()

shapiro_test = shapiro(residuals)
# normal if p value > 0.05
print('Shapiro-Wilki test statistic:', shapiro_test.statistic)
print('Shapiro-Wilki test p-value:', shapiro_test.pvalue)

anderson_test = anderson(residuals)
# normal if test statistic is below critical value
print('Anderson-Darling test statistic:', anderson_test.statistic)
print('Critical values:', anderson_test.critical_values)

# Testing homoscedasticity.

fitted_values = y_pred

plt.scatter(fitted_values, residuals)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')
plt.title('Testing Homoscedasticity.\nResiduals vs Fitted Values')
plt.show()


# homoscedastic if p-value > 0.05
bp_test = het_breuschpagan(residuals, sm.add_constant(X_test))
print('p-value:', bp_test[1])

gq_test = het_goldfeldquandt(residuals, sm.add_constant(X_test))
print('p-value:', gq_test[1])


# Logarithmic transformation.
df['log_life_ladder'] = np.log(df['life_ladder'])

X = df[['gdp', 'social_support', 'healthy_life', 'life_choices_freedom',
        'generosity', 'corruption', 'positive_affect', 'negative_affect']]
y = df['log_life_ladder']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
y_transformed, _ = boxcox(y + 1)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_transformed, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

residuals = y_test - y_pred

y_pred_original = np.exp(y_pred)
y_test_original = np.exp(y_test)


mse = mean_squared_error(y_test_original, y_pred_original)
print(f"Mean Squared Error: {mse}")

shapiro_test = shapiro(residuals)
# normal if p value > 0.05
print('Shapiro-Wilki test p-value for log data:', shapiro_test.pvalue)

white_test = het_white(residuals, sm.add_constant(X_test))
print('white test p-value:', white_test[1])
