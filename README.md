# :united_nations: Towards Zero Hunger: A Cross-Country Analysis of Factors Affecting Food Insecurity

Exploratory Data Analysis on Global food security indicators: A comprehensive study using Multiple Linear Regression on "Prevalence of Moderate and Severe Food Insecurity", against numerous socio-economic factors of influence. 

# :memo: Problem Statement
> :blue_book: “How might we identify the key factors of influence for food insecurity index across countries, to facilitate informed and targeted governmental policy interventions?”

# :chart_with_upwards_trend: Quantitative Indicators
1. Gross Domestic Product (GDP)
2. Population
3. Infant Mortality Rates
4. Minimum Wage (Log-Transformed)
5. Income inequality Index (Gini Index)

# :clipboard: Qualitative Indicators
1. Geopolitical Analysis
2. Policy Interventions
3. Foreign Aid

# :bar_chart: Dataset Providers
1. [World Bank](https://data.worldbank.org/)
2. [Food and Agriculture Organisation](https://www.fao.org/faostat/en/)
3. [Kaggle](https://www.kaggle.com/datasets)

# Install guide for Online Web Application
Aside from our Jupyter Notebook, we have also developed a user-friendly web-application for all governmental organisations around the world to use, and to determine the most significant factors of influence for Food Insecurity Index for their country. 

Our application is built on Flask with Jinja Templating.

## Requirements
- cloned repo
- `python3`

## Steps for Linux/MacOS Users
1. Downloading requirements
```sh
./setup.sh
```
2. Running webapp
```sh
./startup.sh
```

## Steps for Windows Users

1. Downloading requirements
```sh
python -m venv .venv
python -m pip install -r requirements.txt
```

2. Running webapp
```sh
. .venv/Scripts/activate
flask run
```

## Steps to use Web Application
1. Enter the relevant quantitative factors for your country
2. Press 'Compute'
3. The Website will now predict the value for your country's 'Prevalence of Moderate to Severe Food Insecurity' value. A higher value signifies higher risk of food insecurity in your country, vice versa.