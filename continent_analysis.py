import matplotlib.pyplot as plt
import seaborn as sns

from data.data_preprocessing import data_preprocessing

data = data_preprocessing()


def continent_by_life_ladder():
    continent_order = data.groupby('continent')['life_ladder'].mean().sort_values().index

    plt.figure(figsize=(10, 8))
    sns.boxplot(x=data['continent'], y=data["life_ladder"], color='#5D7CE6', order=continent_order)
    plt.title('\nLife Ladder by Continent\n', fontsize=20)
    plt.xlabel('')
    plt.ylabel('Life Ladder', fontsize=7)

    plt.savefig('static/graphs/continent_by_life_ladder_boxplot.png')
