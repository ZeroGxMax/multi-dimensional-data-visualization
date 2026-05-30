"""
Script to generate multi‑dimensional data visualizations for the
CMP_SC‑8630 data visualization assignment.  The script loads three
real‑world datasets related to climate and hydrology and produces
visualizations that explore patterns across multiple variables and
dimensions.  The resulting figures are saved to the ``output``
directory.  The datasets used here include:

* ``weather_data.csv`` – daily weather observations for multiple
  cities in New Zealand (2016–2017) containing temperature,
  humidity, wind, pressure and precipitation variables.  Source:
  mosaicData package within the Rdatasets collection.
* ``global_temp.csv`` – NASA Goddard Institute for Space Studies
  (GISTEMP) global land–ocean temperature anomalies from 1880 to
  2025.  Monthly anomalies relative to the 1951–1980 baseline are
  provided.  Source: NASA GISS via data.giss.nasa.gov.
* ``minnesota_weather.csv`` – monthly weather summary for six
  Minnesota agricultural sites (1927–1936) including cooling and
  heating degree days, precipitation and temperature extremes.
  Source: agridat package within Rdatasets.

The visualizations include heatmaps, scatter plots and line charts
to illustrate how variables such as temperature, humidity and
precipitation vary over time and across different locations.
"""

import os
from typing import List

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def ensure_output_dir(path: str) -> None:
    """Ensure that the output directory exists."""
    os.makedirs(path, exist_ok=True)


def plot_weather_heatmap(df: pd.DataFrame, outdir: str) -> str:
    """Create a heatmap of average temperature by city and month.

    Parameters
    ----------
    df : pandas.DataFrame
        Weather data with columns ``city``, ``month`` and ``avg_temp``.
    outdir : str
        Directory to write the output image.

    Returns
    -------
    str
        Path to the saved figure.
    """
    # 1. Compute the average monthly temperature for each city (group by 'city' and 'month', calculate mean of 'avg_temp').
    grouped = df.groupby(['city', 'month'])['avg_temp'].mean().reset_index()
    # 2. Pivot the result to create a matrix with 'city' as index, 'month' as columns, and average temperature as values.
    pivot_df = grouped.pivot(index='city', columns='month', values='avg_temp')
    # 3. Ensure the columns (months) are sorted in calendar order.
    pivot_df = pivot_df.sort_index(axis=1)
    # 4. Create a heatmap using seaborn.heatmap():
    plt.figure(figsize=(10, 4))
    sns.heatmap(pivot_df, cmap='coolwarm', annot=True, fmt='.1f', cbar_kws={'label': 'Average temperature'})
    # 5. Set title "Average monthly temperature by city", xlabel "Month", and ylabel "City".
    plt.title("Average monthly temperature by city")
    plt.xlabel("Month")
    plt.ylabel("City")
    # 6. Save the figure as "weather_heatmap.png" in outdir (using 300 dpi and tight layout) and return the saved file path.
    outpath = os.path.join(outdir, "new_weather_heatmap.png")
    plt.tight_layout()
    plt.savefig(outpath, dpi=300)
    plt.close()
    return outpath


def plot_weather_scatter(df: pd.DataFrame, outdir: str) -> str:
    """Create a scatter plot exploring relationships between humidity,
    temperature and precipitation.

    Each point represents a daily observation.  The x‑axis shows
    average humidity, the y‑axis shows average temperature in Fahrenheit,
    the marker size encodes precipitation and colour encodes the city.
    Separate legends are provided for city and precipitation to avoid
    overlap.

    Parameters
    ----------
    df : pandas.DataFrame
        Weather data with columns ``avg_humidity``, ``avg_temp``,
        ``precip`` and ``city``.
    outdir : str
        Directory to write the output image.

    Returns
    -------
    str
        Path to the saved figure.
    """
    import matplotlib.lines as mlines
    # 1. Clean the 'precip' column
    df = df.copy()
    df['precip'] = pd.to_numeric(df['precip'], errors='coerce').fillna(0.0)
    # 2. Set up the figure
    fig, ax = plt.subplots(figsize=(9, 6))
    # 3. Set a marker size range
    size_range = (20, 300)
    # 4. Generate a scatter plot
    sns.scatterplot(
        data=df,
        x="avg_humidity",
        y="avg_temp",
        hue="city",
        size="precip",
        sizes=size_range,
        alpha=0.65,
        legend=False,
        ax=ax
    )
    ax.set_xlabel("Average relative humidity (%)")
    ax.set_ylabel("Average temperature (°F)")
    
    # 5. Create a custom legend for the cities (hue)
    cities_sorted = sorted(df['city'].unique())
    palette = sns.color_palette(n_colors=len(cities_sorted))
    city_handles = [
        mlines.Line2D([], [], color=palette[i], marker='o', linestyle='None',
                      markersize=8, label=city)
        for i, city in enumerate(cities_sorted)
    ]
    leg1 = ax.legend(handles=city_handles, loc="upper left", bbox_to_anchor=(1.02, 1.0), title="City")
    ax.add_artist(leg1)
    
    # 6. Create a custom legend for precipitation sizes (size)
    min_p, max_p = df['precip'].min(), df['precip'].max()
    p_values = np.linspace(min_p, max_p, 4)
    if max_p == min_p:
        mapped_sizes = [size_range[0]] * 4
    else:
        mapped_sizes = np.interp(p_values, (min_p, max_p), size_range)
    precip_handles = [
        plt.scatter([], [], s=sz, color='gray', alpha=0.65, label=f"{v:.2f}")
        for v, sz in zip(p_values, mapped_sizes)
    ]
    ax.legend(handles=precip_handles, loc="lower left", bbox_to_anchor=(1.02, 0.0), title="Precipitation")
    
    # 7. Add title
    plt.title("Daily weather: temperature vs humidity with precipitation (size)")
    
    # 8. Save the figure
    outpath = os.path.join(outdir, "new_weather_scatter.png")
    plt.tight_layout()
    plt.savefig(outpath, dpi=300)
    plt.close()
    return outpath


def plot_global_temp_heatmap(df: pd.DataFrame, outdir: str) -> str:
    """Create a heatmap of global temperature anomalies by year and month.

    Parameters
    ----------
    df : pandas.DataFrame
        Global temperature anomalies where rows correspond to years and
        columns to months (Jan–Dec).  The DataFrame should include
        numeric values for anomalies.  Missing values are allowed and
        will appear as blank cells.
    outdir : str
        Directory to write the output image.

    Returns
    -------
    str
        Path to the saved figure.
    """
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # 1. Reshape the dataframe from wide to long format
    long_df = df.melt(id_vars=['Year'], value_vars=months, var_name='Month', value_name='Anomaly')
    # 2. Map Month abbreviations to month numbers
    month_map = {m: i + 1 for i, m in enumerate(months)}
    long_df['MonthNum'] = long_df['Month'].map(month_map)
    # 3. Pivot the long dataframe back to a matrix
    pivot_df = long_df.pivot(index='Year', columns='MonthNum', values='Anomaly')
    # 4. Ensure the matrix is sorted by year index in ascending order
    pivot_df = pivot_df.sort_index(ascending=True)
    # 5. Set up the figure
    plt.figure(figsize=(10, 8))
    # 6. Draw a heatmap
    sns.heatmap(
        pivot_df,
        cmap='coolwarm',
        vmin=-1.5, vmax=1.5,
        cbar_kws={'label': 'Temperature anomaly (°C relative to 1951–1980)'},
        linewidths=0,
        linecolor="white"
    )
    # 7. Customize x-ticks
    plt.xticks(np.arange(12) + 0.5, months, rotation=45)
    # 8. Set title and labels
    plt.title("Global land–ocean temperature anomalies (1880–2025)")
    plt.xlabel("Month")
    plt.ylabel("Year")
    # 9. Save the figure
    outpath = os.path.join(outdir, "new_global_temp_heatmap.png")
    plt.tight_layout()
    plt.savefig(outpath, dpi=300)
    plt.close()
    return outpath


def plot_minnesota_precip_line(df: pd.DataFrame, outdir: str) -> str:
    """Create a line chart of monthly precipitation by site over time.

    This figure shows how precipitation varies across the six Minnesota
    sites from 1927 to 1936.  Each line corresponds to a site and
    month; values are aggregated by year and month.

    Parameters
    ----------
    df : pandas.DataFrame
        Minnesota weather data with columns ``site``, ``year``, ``mo`` (month) and
        ``precip``.
    outdir : str
        Directory to write the output image.

    Returns
    -------
    str
        Path to the saved figure.
    """
    df = df.copy()
    # 1. Create a datetime column named 'date'
    df['date'] = pd.to_datetime(df[['year', 'mo']].assign(day=1).rename(columns={'mo': 'month'}))
    # 2. Set up the figure
    fig, ax = plt.subplots(figsize=(10, 6))
    # 3. Create a line plot
    sns.lineplot(
        data=df,
        x='date',
        y='precip',
        hue='site',
        ax=ax
    )
    ax.set_xlabel("Year")
    ax.set_ylabel("Precipitation (inches)")
    # 4. Set title
    plt.title("Monthly precipitation by Minnesota site (1927–1936)")
    # 5. Place the legend outside the plot box
    ax.legend(bbox_to_anchor=(1.05, 1), loc="upper left", title="Site")
    # 6. Save the figure
    outpath = os.path.join(outdir, "new_minnesota_precip_line.png")
    plt.tight_layout()
    plt.savefig(outpath, dpi=300)
    plt.close()
    return outpath


def main() -> List[str]:
    """Run all visualizations and return a list of generated file paths."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    out_dir = os.path.join(base_dir, "output")
    ensure_output_dir(out_dir)
    figures: List[str] = []

    # Load and plot weather data
    weather_path = os.path.join(data_dir, "weather_data.csv")
    weather_df = pd.read_csv(weather_path)
    # Plot heatmap and scatter
    figures.append(plot_weather_heatmap(weather_df, out_dir))
    figures.append(plot_weather_scatter(weather_df, out_dir))

    # Load and plot global temperature anomalies
    global_path = os.path.join(data_dir, "global_temp.csv")
    global_df = pd.read_csv(global_path, skiprows=1)
    # Replace *** with NA and convert to numeric
    global_df = global_df.replace("***", pd.NA)
    for col in global_df.columns[1:]:
        global_df[col] = pd.to_numeric(global_df[col], errors="coerce")
    figures.append(plot_global_temp_heatmap(global_df, out_dir))

    # Load and plot Minnesota weather data
    minn_path = os.path.join(data_dir, "minnesota_weather.csv")
    minn_df = pd.read_csv(minn_path)
    figures.append(plot_minnesota_precip_line(minn_df, out_dir))
    return figures


if __name__ == "__main__":
    generated = main()
    print("Generated figures:")
    for path in generated:
        print(path)