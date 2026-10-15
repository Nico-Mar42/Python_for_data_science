from load_csv import load
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


def convert_population(value):
    """Convert population values from strings with suffixes to float."""
    if value.endswith("M"):
        return float(value[:-1]) * 1_000_000
    if value.endswith("k"):
        return float(value[:-1]) * 1_000
    return float(value)


def format_millions(value, pos):
    """Format the y-axis labels in millions."""
    return f"{value / 1_000_000:.0f}M"


def main():
    """Main function to test the load functionality."""

    matplotlib.use("TkAgg")
    try:
        df = load("population_total.csv")
        assert df is not None, "DataFrame is None"
        assert isinstance(df, pd.DataFrame), "Loaded object is not a DataFrame"
        assert not df.empty, "DataFrame is empty"

    except AssertionError as e:
        print(f"AssertionError : {e}")
        return

    france = df[df["country"] == "France"].iloc[0]
    japan = df[df["country"] == "Japan"].iloc[0]

    x = df.columns[1:]
    y_france = france.iloc[1:].map(convert_population)
    y_japan = japan.iloc[1:].map(convert_population)

    plt.plot(x, y_france, label="France", color="blue")
    plt.plot(x, y_japan, label="Japan", color="red")

    plt.xticks(x[::40])
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.title("Population Projections")
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(format_millions))
    plt.legend()
    plt.show()

    return


if __name__ == "__main__":
    main()
