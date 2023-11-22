# Towards Zero Hunger: A Cross-Country Analysis of Factors Affecting Food Insecurity

Exploratory Data Analysis on Global food security indicators: A comprehensive study using Multiple Linear Regression on "Prevalence of Moderate and Severe Food Insecurity", against numerous socio-economic factors of influence. 

# Problem Statement
> :blue_book: “How might we identify the key factors of influence for food insecurity index across countries, to facilitate informed and targeted governmental policy interventions?”

# Quantitative Indicators
1. Gross Domestic Product (GDP)
2. Population
3. Infant Mortality Rates
4. Minimum Wage (Log-Transformed)
5. Income inequality Index (Gini Index)

# Qualitative Indicators
1. Geopolitical Analysis
2. Policy Interventions
3. Foreign Aid

# Dataset Providers
1. [World Bank](https://data.worldbank.org/)
2. [Food and Agriculture Organisation](https://www.fao.org/faostat/en/)
3. [Kaggle](https://www.kaggle.com/datasets)

# Install guide for online Web Application
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