import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def draw_cat_plot():
    # 1. Import the data from medical_examination.csv
    df = pd.read_csv("medical_examination.csv")

    # 2. Add an overweight column based on BMI (> 25).
    height_m = df["height"] / 100
    bmi = df["weight"] / (height_m ** 2)
    df["overweight"] = (bmi > 25).astype(int)

    # 3. Normalize cholesterol and glucose: 0 = good, 1 = bad.
    df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
    df["gluc"] = (df["gluc"] > 1).astype(int)

    # 4. Draw the categorical plot.
    # 5. Convert selected columns to long format.
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"],
    )

    # 6. Group by cardio and feature value, then count observations.
    df_cat = (
        df_cat.groupby(["cardio", "variable", "value"])
        .size()
        .reset_index(name="total")
    )

    # 7. Plot categorical feature counts split by cardiovascular disease status.
    fig = sns.catplot(
        data=df_cat,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar",
    ).fig

    # 8. Get the figure for the output.
    fig = fig

    # 9. Do not modify the next two lines.
    fig.savefig("catplot.png")
    return fig


def draw_heat_map():
    # 10. Import the data.
    df = pd.read_csv("medical_examination.csv")

    # 11. Clean incorrect/outlier records.
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    ].copy()

    # 12. Calculate the correlation matrix.
    corr = df_heat.corr(numeric_only=True)

    # 13. Mask the upper triangle.
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14. Set up the matplotlib figure.
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15. Plot the correlation matrix.
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
        center=0,
        ax=ax,
    )

    # 16. Do not modify the next two lines.
    fig.savefig("heatmap.png")
    return fig
