import pandas as pd
import numpy as np


def clean_fear_greed_data(df):
    """
    Clean Fear & Greed dataset.
    """

    df = df.copy()

    df['date'] = pd.to_datetime(df['date'])
    df['date'] = df['date'].dt.date

    df = df[['date', 'classification', 'value']]

    return df


def clean_trader_data(df):
    """
    Clean Hyperliquid trader dataset.
    """

    df = df.copy()

    df['Timestamp IST'] = pd.to_datetime(
        df['Timestamp IST'],
        dayfirst=True,
        errors='coerce'
    )

    df['date'] = df['Timestamp IST'].dt.date

    return df


def create_custom_metrics(df):
    """
    Create custom metrics for deeper analysis.
    """

    df = df.copy()

    # Profit generated per dollar traded
    df['Profit_Efficiency'] = np.where(
        df['Size USD'] != 0,
        df['Closed PnL'] / df['Size USD'],
        0
    )

    # Profit generated per dollar spent on fees
    df['Fee_Efficiency'] = np.where(
        df['Fee'] != 0,
        df['Closed PnL'] / df['Fee'],
        0
    )

    # Winning trade flag
    df['Winning_Trade'] = np.where(
        df['Closed PnL'] > 0,
        1,
        0
    )

    # Losing trade flag
    df['Losing_Trade'] = np.where(
        df['Closed PnL'] < 0,
        1,
        0
    )

    return df


def merge_sentiment_with_trades(
    trader_df,
    sentiment_df
):
    """
    Merge trader data with Fear & Greed sentiment.
    """

    merged_df = trader_df.merge(
        sentiment_df,
        on='date',
        how='left'
    )

    return merged_df


def check_missing_values(df):
    """
    Display missing values.
    """

    missing = (
        df.isnull()
        .sum()
        .sort_values(ascending=False)
    )

    print("\nMissing Values:\n")
    print(missing[missing > 0])


def remove_duplicate_rows(df):
    """
    Remove duplicate records.
    """

    before = len(df)

    df = df.drop_duplicates()

    after = len(df)

    print(
        f"Removed {before - after} duplicate rows."
    )

    return df


def preprocess_pipeline(
    trader_df,
    sentiment_df
):
    """
    Complete preprocessing pipeline.
    """

    sentiment_df = clean_fear_greed_data(
        sentiment_df
    )

    trader_df = clean_trader_data(
        trader_df
    )

    trader_df = remove_duplicate_rows(
        trader_df
    )

    merged_df = merge_sentiment_with_trades(
        trader_df,
        sentiment_df
    )

    merged_df = create_custom_metrics(
        merged_df
    )

    check_missing_values(
        merged_df
    )

    print("\nPreprocessing Completed Successfully.")

    return merged_df


if __name__ == "__main__":

    from data_loading import (
        load_fear_greed_data,
        load_trader_data
    )

    fear_df = load_fear_greed_data(
        "data/fear_greed_index.csv"
    )

    trade_df = load_trader_data(
        "data/historical_data.csv"
    )

    merged_df = preprocess_pipeline(
        trade_df,
        fear_df
    )

    print("\nMerged Dataset Shape:")
    print(merged_df.shape)

    print("\nFirst 5 Rows:")
    print(merged_df.head())