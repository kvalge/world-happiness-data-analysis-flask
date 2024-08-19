from flask import Flask
from inspect_data import *
from eda import *
from correlation import *

app = Flask(__name__)

inspect_data()
inspect_cleaned_data()
identify_life_ladder_distribution()
find_confidence_interval_for_life_ladder_mean()
variables_correlation()
variables_correlation_with_life_ladder()
life_ladder_and_gdp_correlation()


if __name__ == '__main__':
    app.run()
