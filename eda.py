import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm

from data.clean_data import clean_data

df = clean_data()


def identify_life_ladder_distribution():
    data = df['life_ladder']

    data_mean = data.mean()
    data_std = data.std()

    one_std_upper_limit = data_mean + 1 * data_std
    one_std_lower_limit = data_mean - 1 * data_std

    # How many values of total falls within one std of the mean.
    share_of_values_in_one_std_interval = (((data >= one_std_lower_limit) & (data <= one_std_upper_limit)).mean()) * 100

    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=25, color='#5D7CE6', edgecolor='w', alpha=0.95)
    plt.ylabel('Count')
    plt.title('Distribution of Life Ladder Values')

    plt.savefig('static/graphs/01_life_ladder_histogram.png')
    plt.close()

    # Calculate Z-score for every Life Ladder value.
    df['Z_score'] = stats.zscore(df['life_ladder'])

    # Find outlier with value less than -3 or more than 3.
    outliers = df[(df['Z_score'] < -3) | (df['Z_score'] > 3)]

    with open('results/01_life_ladder_distribution.txt', 'w') as f:
        f.write('\nDetermine Life Ladder distribution\n\n')
        f.write(f'- Mean: {data_mean:.2f}\n')
        f.write(f'- Standard Deviation: {data_std:.2f}\n')
        f.write(f'- Lower limit of one standard error: {one_std_lower_limit:.2f}\n')
        f.write(f'- Upper limit of one standard error: {one_std_upper_limit:.2f}\n')
        f.write(f'- Share of values within one std of the mean: {share_of_values_in_one_std_interval:.2f}%\n')


def find_confidence_interval_for_life_ladder_mean():
    data = df['life_ladder']

    data_mean = data.mean()
    data_std = data.std()

    estimated_standard_error = data_std / np.sqrt(data.shape[0])

    confidence_interval_95 = stats.norm.interval(0.95, loc=data_mean, scale=estimated_standard_error)

    confidence_interval_99 = stats.norm.interval(0.99, loc=data_mean, scale=estimated_standard_error)

    with open('results/02_life_ladder_mean_ci.txt', 'w') as f:
        f.write('\nLife Ladder confidence interval for mean\n\n')
        f.write(f'- Mean: {data_mean:.2f}\n')
        f.write(f'- CI 95% level: lower {confidence_interval_95[0]:.2f} - upper {confidence_interval_95[1]:.2f}\n')
        f.write(f'- CI 99% level: lower {confidence_interval_99[0]:.2f} - upper {confidence_interval_99[1]:.2f}\n')
