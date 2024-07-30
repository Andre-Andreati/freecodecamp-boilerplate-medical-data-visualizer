import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = ((df['weight'] / ((df['height'] / 100) ** 2)) > 25) * 1

# 3
df['cholesterol'] = (df[['cholesterol']] != 1) * 1
df['gluc'] = (df[['gluc']] != 1) * 1

# 4
def draw_cat_plot():
    # 5
    df_cat = df.drop(columns=['id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo']).melt(id_vars=['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    # 6
    df_cat = df_cat.drop(columns=['variable']).rename(columns={'value': 'cardio'}).melt(id_vars=['cardio'])
  
    # 7
    chart = sns.catplot(data=df_cat, x='variable', col='cardio', hue='value', kind="count")
    chart.set_ylabels('total')

    # 8 Get the figure for the output and store it in the fig variable
    fig = chart.figure

    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # 12 Calculate the correlation matrix and store it in the corr variable
    corr = df_heat.corr()

    # 13 Generate a mask for the upper triangle and store it in the mask variable
    mask = np.triu(np.ones_like(corr))

    # 14 Set up the matplotlib figure
    fig, ax = plt.figure(), plt.axes()
    
    # 15 Plot the correlation matrix using the method provided by the seaborn library import: sns.heatmap()
    sns.heatmap(corr, annot=True, fmt=".1f", linewidths=.5, mask=mask, robust=True)

    # 16
    fig.savefig('heatmap.png')
    return fig