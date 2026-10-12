from load_csv import load
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


def convert_population(value):
    """Convert population values from strings with suffixes to float."""
    if value.endswith("M"):
        return float(value[:-1]) * 1_000_000
    if value.endswith("k"):
        return float(value[:-1]) * 1_000
    return float(value)


def format_thousands(value, pos):
    """Format the y-axis labels in thousands."""
    return f"{value / 1_000:.0f}K"


def main():
    """Main function to test the load functionality."""

    matplotlib.use("TkAgg")
    try:
        df_life = load("life_expectancy_years.csv")
        assert df_life is not None, "DataFrame is None"
        assert isinstance(df_life, pd.DataFrame), \
            "Loaded object is not a DataFrame"
        assert not df_life.empty, "DataFrame is empty"

        df_GDP = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        assert df_GDP is not None, "DataFrame is None"
        assert isinstance(df_GDP, pd.DataFrame), \
            "Loaded object is not a DataFrame"
        assert not df_GDP.empty, "DataFrame is empty"

    except AssertionError as e:
        print(f"AssertionError : {e}")
        return

    Life = df_life["1900"]
    GDP = df_GDP["1900"]

    plt.scatter(GDP, Life, label="Countries")

    plt.xscale("log")
    plt.xlim(300, 10_000)
    plt.xticks(
        [300, 1_000, 10_000],
        ["300", "1k", "10k"]
    )

    plt.xlabel("GDP per capita in 1900")
    plt.ylabel("Life expectancy in 1900")
    plt.title("Life expectancy vs GDP per capita in 1900")
    plt.show()

    return


if __name__ == "__main__":
    main()
