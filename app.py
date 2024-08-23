from flask import Flask
from inspect_data import *
from eda import *
from correlation import *
from continent_analysis import *

app = Flask(__name__)

inspect_data()
inspect_cleaned_data()
identify_variable_distribution()
variables_correlation()
variables_correlation_with_life_ladder()
variables_correlation_with_gdp()
life_ladder_and_gdp_correlation()
continent_by_life_ladder()

if __name__ == '__main__':
    app.run()
