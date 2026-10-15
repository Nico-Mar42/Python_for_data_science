import pandas as pd


def load(path: str) -> pd.DataFrame:
    """Load a CSV file from a given path and return it as a pandas DataFrame"""

    try:
        assert isinstance(path, str), "Path must be a String"
        assert path.lower().endswith(".csv"), "File must be in .csv format"

        DataFrame = pd.read_csv(path)

    except AssertionError as e:
        print(f"Assertion Error: {e}")
        return None

    except (FileNotFoundError, pd.errors.ParserError, OSError) as error:
        print(f"Error: {error}")
        return None

    print(f"Loading dataset of dimensions ({DataFrame.shape})")

    return DataFrame
