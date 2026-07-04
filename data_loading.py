import pandas as pd


def load_fear_greed_data(file_path):
    """
    Load Fear & Greed Index dataset.
    """
    df = pd.read_csv(file_path)

    # Convert date column to datetime
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'])

    return df


def load_trader_data(file_path):
    """
    Load Hyperliquid trader dataset.
    """
    df = pd.read_csv(file_path)

    # Convert timestamp column to datetime
    if 'Timestamp IST' in df.columns:
        df['Timestamp IST'] = pd.to_datetime(
    df['Timestamp IST'],
    format='%d-%m-%Y %H:%M'
)

    return df


def dataset_summary(df, dataset_name):
    """
    Print dataset summary statistics.
    """
    print(f"\n{'=' * 50}")
    print(f"Dataset: {dataset_name}")
    print(f"{'=' * 50}")

    print(f"\nShape: {df.shape}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())


if __name__ == "__main__":

    fear_greed_df = load_fear_greed_data(
        "data/fear_greed_index.csv"
    )

    trader_df = load_trader_data(
        "data/historical_data.csv"
    )

    dataset_summary(
        fear_greed_df,
        "Fear & Greed Index"
    )

    dataset_summary(
        trader_df,
        "Hyperliquid Historical Data"
    )