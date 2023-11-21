import seaborn as sns
import pandas as pd

DATA = pd.read_csv('geographical_processed_data.csv')
df = pd.DataFrame(DATA) 
predictors = ['GDP', 'CPI', 'Population: Labor force participation (%)',
              'Agricultural Land( %)', 'Co2-Emissions per ton', 'Minimum wage',
              'Unemployment rate', 'Infant mortality',
              'Population']

print(df.columns)

plot = sns.pairplot(data=df, y_vars = ['Prevalence of moderate or severe food insecurity in the total population (percent) (2022)']) 
fig = plot.fig
fig.savefig('plot.pdf')
