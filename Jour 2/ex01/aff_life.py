from load_csv import load
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


def main():
    """Main function to test the load functionality."""

    matplotlib.use("TkAgg")
    try:
        df = load("life_expectancy_years.csv")
        assert df is not None, "DataFrame is None"
        assert isinstance(df, pd.DataFrame), "Loaded object is not a DataFrame"
        assert not df.empty, "DataFrame is empty"

    except AssertionError as e:
        print(f"AssertionError : {e}")
        return

    france = df[df["country"] == "France"].iloc[0]

    x = df.columns[1:]
    y = france.iloc[1:]

    plt.plot(x, y)
    plt.xticks(x[::40])
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")
    plt.title("France Life Expectancy Projection")
    plt.show()

    return


if __name__ == "__main__":
    main()
