import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import random

def generate_pastel_color(palette='spring', num_colors=12, brightness=0.8, max_palette_size=20):
    """
    Generate a list of pastel colors based on the input color palette and brightness.

    Parameters:
    palette (str): Color palette to use = ['spring', 'summer', 'autumn', 'winter']
    num_colors (int): Number of colors to generate (default=12). Maximum 20.
    brightness (float): Brightness level of the colors, between 0 and 1 (default=0.8).
    max_palette_size (int): Maximum length of the palette list (default=20).

    Returns:
    List of pastel colors in hex format.
    """
    print(palette)
    if num_colors > max_palette_size:
        num_colors = max_palette_size
    if palette == 'spring':
        base_colors = ['#ffb3ba', '#ffdfba', '#ffffba', '#baffc9', '#bae1ff', '#e2baff']
    elif palette == 'summer':
        base_colors = ['#ff9f80', '#ffb088', '#ffd180', '#d8de87', '#80deea', '#82b1ff']
    elif palette == 'autumn':
        base_colors = ['#ff6f69', '#ffcc5c', '#a0da8f', '#ff9e9d', '#d8a9f3', '#8bc8f2']
    elif palette == 'winter':
        base_colors = ['#e1e5f2', '#c4d0ef', '#9eb9f4', '#72a1d1', '#417bb0', '#215587']
    else:
        raise ValueError('Invalid palette name. Choose from "spring", "summer", "autumn", or "winter".')

    color_list = []
    for i in range(num_colors):
        base_color = mpl.colors.ColorConverter().to_rgb(base_colors[i % len(base_colors)])
        new_color = [x + (random.random() / 5.0 - 0.1) for x in base_color]
        new_color = [min(1, max(0, x)) for x in new_color]
        new_color_hex = mpl.colors.rgb2hex(new_color)
        color_list.append(new_color_hex)

    color_list.sort()
    return color_list





def make_chart(data, x_col, y_col, size=6, colors=0, orientation='vertical', chart_type='bar'):
    """
    Make a bar chart.

    Parameters:
    data (DataFrame): DataFrame containing the data.
    x_col (str): Name of the column to be plotted on the x-axis.
    y_col (str): Name of the column to be plotted on the y-axis.
    size (float): Size of the chart (default=6).
    colors (str or list): Color or list of colors for the bars (default=random_color).
    orientation (str): Orientation of the bars, 'vertical' or 'horizontal' (default='vertical').
    chart_type (str): Type of the chart, 'bar', 'barh', or 'pie' (default='bar').

    Returns:
    None.
    """
    fig, ax = plt.subplots(figsize=(size, size))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    if type(colors) == int: 
        colors = {c: plt.cm.tab10(i) for i, c in enumerate(data[x_col].unique())}

    elif type(colors) == str:
        #colors = [colors] * len(data[x_col])
        colors = {c: [colors] for i, c in enumerate(data[x_col].unique())}
    else:
        if len(colors) < len(data[x_col].unique()):
            raise ValueError("The number of colors should be greater than or equal to the number of unique values in x_col")
        colors = {c: [colors[i]] for i, c in enumerate(data[x_col].unique())}
    
    if chart_type == 'bar':
        for i, row in data.iterrows():
            ax.bar(row[x_col], row[y_col], color=colors[row[x_col]])
    elif chart_type == 'barh':
        for i, row in data.iterrows():
            ax.bar(row[x_col], row[y_col], color=colors[row[x_col]])    
    elif chart_type == 'pie':
        colors = [colors[c][0] for c in data[x_col].unique()]
        ax.pie(data[y_col], labels=data[x_col], colors=colors, autopct='%1.1f%%')
    
    if chart_type != 'pie':
        ax.set_xlabel(x_col.capitalize())
        ax.set_ylabel(y_col.capitalize())

        if orientation == 'horizontal':
            plt.xticks(rotation=90)
            plt.gca().invert_yaxis()
        else:
            plt.xticks(rotation=45)
    
    plt.show()
