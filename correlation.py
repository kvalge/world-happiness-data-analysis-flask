import matplotlib.pyplot as plt
import seaborn as sns

from data.data_preprocessing import data_preprocessing

new_variable_names_dict = {
    'life_ladder': 'life ladder',
    'gdp': 'gdp',
    'social_support': 'social support',
    'healthy_life': 'healthy life',
    'life_choices_freedom': 'life choices freedom',
    'generosity': 'generosity',
    'corruption': 'corruption',
    'positive_affect': 'positive affect',
    'negative_affect': 'negative affect',
}


def variables_correlation():
    data = data_preprocessing()
    corr_data = data.drop(['country', 'year'], axis=1)

    old_labels = corr_data.corr().columns
    new_labels = [new_variable_names_dict.get(label, label) for label in old_labels]

    plt.figure(figsize=(12, 7))
    heatmap = sns.heatmap(corr_data.corr(), cmap='coolwarm', annot=True)
    heatmap.set_xticklabels(new_labels, rotation=45, ha='right')
    heatmap.set_yticklabels(new_labels, rotation=0, ha='right')
    plt.title('\nCorrelation Matrix of Dataset Variables\n', fontsize=20)
    plt.tight_layout()

    plt.savefig('static/graphs/correlation_heatmap.png')


def variables_correlation_with_life_ladder():
    data = data_preprocessing()
    corr_data = data.drop(['country', 'year'], axis=1)

    corr_matrix = corr_data.corr()
    sorted_corr = corr_matrix[['life_ladder']].sort_values('life_ladder', ascending=False)

    old_labels = sorted_corr.index
    new_labels = [new_variable_names_dict.get(label, label) for label in old_labels]

    plt.figure(figsize=(10, 6))
    heatmap = sns.heatmap(sorted_corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    heatmap.set_xticklabels(['life_ladder'])
    heatmap.set_yticklabels(new_labels, ha='right')

    plt.title('\nCorrelations with Life Ladder\n', fontsize=20)
    plt.tight_layout()

    plt.savefig('static/graphs/correlation_heatmap_for_life_ladder.png')


def variables_correlation_with_gdp():
    data = data_preprocessing()
    corr_data = data.drop(['country', 'year', 'life_ladder'], axis=1)

    corr_matrix = corr_data.corr()
    sorted_corr = corr_matrix[['gdp']].sort_values('gdp', ascending=False)

    old_labels = sorted_corr.index
    new_labels = [new_variable_names_dict.get(label, label) for label in old_labels]

    plt.figure(figsize=(10, 6))
    heatmap = sns.heatmap(sorted_corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    heatmap.set_xticklabels(['gdp'])
    heatmap.set_yticklabels(new_labels, ha='right')

    plt.title('\nCorrelations with GDP\n', fontsize=20)
    plt.tight_layout()

    plt.savefig('static/graphs/correlation_heatmap_for_gdp.png')


def life_ladder_and_gdp_correlation():
    data = data_preprocessing()

    plt.figure(figsize=(10, 6))
    plt.scatter(data['life_ladder'], data['gdp'], color='#5D7CE6')
    plt.title('\nLife Ladder and GDP Correlation\n', fontsize=20)
    plt.xlabel('Life Ladder', fontsize=7)
    plt.ylabel('Log GDP per Capita', fontsize=7)

    plt.savefig('static/graphs/correlation_life_ladder&gdp_scatterplot.png')
