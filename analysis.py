import pandas as pd
import numpy as np
from scipy import stats



def sentiment_performance_analysis(df):

    sentiment_stats = (
        df.groupby('classification')
        .agg(
            Total_Trades=('Closed PnL', 'count'),
            Total_PnL=('Closed PnL', 'sum'),
            Average_PnL=('Closed PnL', 'mean'),
            Median_PnL=('Closed PnL', 'median'),
            Win_Rate=('Winning_Trade', 'mean'),
            Profit_Efficiency=('Profit_Efficiency', 'mean'),
            Fee_Efficiency=('Fee_Efficiency', 'mean')
        )
        .reset_index()
    )

    sentiment_stats['Win_Rate'] *= 100

    print("\n===== SENTIMENT PERFORMANCE =====\n")
    print(sentiment_stats)

    return sentiment_stats


def coin_analysis(df):

    coin_stats = (
        df.groupby('Coin')
        .agg(
            Total_PnL=('Closed PnL', 'sum'),
            Average_PnL=('Closed PnL', 'mean'),
            Total_Trades=('Closed PnL', 'count')
        )
        .sort_values(
            by='Total_PnL',
            ascending=False
        )
    )

    print("\n===== TOP COINS =====\n")
    print(coin_stats.head(10))

    print("\n===== COIN FREQUENCY =====\n")
    print(df['Coin'].value_counts().head(20))

    return coin_stats


def top_trader_analysis(df):

    trader_stats = (
        df.groupby('Account')
        .agg(
            Total_PnL=('Closed PnL', 'sum'),
            Average_PnL=('Closed PnL', 'mean'),
            Total_Trades=('Closed PnL', 'count'),
            Win_Rate=('Winning_Trade', 'mean')
        )
        .reset_index()
    )

    trader_stats['Win_Rate'] *= 100

    top_traders = trader_stats.sort_values(
        by='Total_PnL',
        ascending=False
    )

    print("\n===== TOP 10 TRADERS =====\n")
    print(top_traders.head(10))

    return top_traders


def elite_trader_analysis(df):

    trader_pnl = (
        df.groupby('Account')['Closed PnL']
        .sum()
        .reset_index()
    )

    threshold = trader_pnl['Closed PnL'].quantile(0.90)

    elite_accounts = trader_pnl[
        trader_pnl['Closed PnL'] >= threshold
    ]['Account']

    elite_df = df[
        df['Account'].isin(elite_accounts)
    ]

    normal_df = df[
        ~df['Account'].isin(elite_accounts)
    ]

    results = {
        "Elite Avg PnL":
            elite_df['Closed PnL'].mean(),

        "Normal Avg PnL":
            normal_df['Closed PnL'].mean(),

        "Elite Win Rate":
            elite_df['Winning_Trade'].mean() * 100,

        "Normal Win Rate":
            normal_df['Winning_Trade'].mean() * 100
    }

    print("\n===== ELITE TRADER ANALYSIS =====\n")
    print(results)

    return results


def elite_sentiment_analysis(df):

    trader_pnl = (
        df.groupby('Account')['Closed PnL']
        .sum()
        .reset_index()
    )

    threshold = trader_pnl['Closed PnL'].quantile(0.90)

    elite_accounts = trader_pnl[
        trader_pnl['Closed PnL'] >= threshold
    ]['Account']

    elite_df = df[
        df['Account'].isin(elite_accounts)
    ]

    normal_df = df[
        ~df['Account'].isin(elite_accounts)
    ]

    elite_sentiment = (
        elite_df['classification']
        .value_counts(normalize=True)
        * 100
    )

    normal_sentiment = (
        normal_df['classification']
        .value_counts(normalize=True)
        * 100
    )

    print("\n===== ELITE SENTIMENT BEHAVIOR =====\n")

    print("\nElite Traders:")
    print(elite_sentiment)

    print("\nNormal Traders:")
    print(normal_sentiment)


def direction_analysis(df):

    direction_stats = (
        df.groupby('Direction')
        .agg(
            Total_PnL=('Closed PnL', 'sum'),
            Average_PnL=('Closed PnL', 'mean'),
            Win_Rate=('Winning_Trade', 'mean')
        )
        .reset_index()
    )

    direction_stats['Win_Rate'] *= 100

    print("\n===== DIRECTION ANALYSIS =====\n")
    print(direction_stats)

    return direction_stats


def statistical_test(df):

    groups = []

    for sentiment in df['classification'].dropna().unique():

        pnl_values = df[
            df['classification'] == sentiment
        ]['Closed PnL']

        groups.append(pnl_values)

    statistic, p_value = stats.kruskal(*groups)

    print("\n===== KRUSKAL-WALLIS TEST =====")
    print(f"Statistic : {statistic:.4f}")
    print(f"P-value   : {p_value:.6f}")

    if p_value < 0.05:
        print(
            "Result: Significant difference between sentiment groups."
        )
    else:
        print(
            "Result: No significant difference detected."
        )

    return statistic, p_value


def generate_key_insights(df):

    print("\n===== KEY INSIGHTS =====")

    best_sentiment = (
        df.groupby('classification')['Closed PnL']
        .mean()
        .idxmax()
    )

    print(
        f"Highest average profitability observed during: {best_sentiment}"
    )

    best_coin = (
        df.groupby('Coin')['Closed PnL']
        .sum()
        .idxmax()
    )

    print(
        f"Most profitable coin overall: {best_coin}"
    )

def risk_adjusted_sentiment_analysis(df):

    risk_stats = (
        df.groupby('classification')
        .agg(
            Average_PnL=('Closed PnL', 'mean'),
            PnL_Std=('Closed PnL', 'std')
        )
        .reset_index()
    )

    risk_stats['Risk_Adjusted_Return'] = (
        risk_stats['Average_PnL'] /
        risk_stats['PnL_Std']
    )

    risk_stats = risk_stats.sort_values(
        by='Risk_Adjusted_Return',
        ascending=False
    )

    print("\n===== RISK-ADJUSTED SENTIMENT ANALYSIS =====\n")
    print(risk_stats)

    return risk_stats

def sentiment_strategy_ranking(df):

    strategy_stats = (
        df.groupby('classification')
        .agg(
            Avg_PnL=('Closed PnL', 'mean'),
            Win_Rate=('Winning_Trade', 'mean'),
            Total_Trades=('Closed PnL', 'count')
        )
        .reset_index()
    )

    strategy_stats['Win_Rate'] *= 100

    strategy_stats = strategy_stats.sort_values(
        by='Avg_PnL',
        ascending=False
    )

    print("\n===== SENTIMENT STRATEGY RANKING =====\n")
    print(strategy_stats)

    return strategy_stats

def coin_sentiment_analysis(df):

    coin_sentiment = (
        df.groupby(
            ['classification', 'Coin']
        )
        .agg(
            Avg_PnL=('Closed PnL', 'mean'),
            Total_PnL=('Closed PnL', 'sum'),
            Trades=('Closed PnL', 'count')
        )
        .reset_index()
    )

    print("\n===== COIN × SENTIMENT ANALYSIS =====\n")

    for sentiment in coin_sentiment[
        'classification'
    ].dropna().unique():

        subset = (
    coin_sentiment[
        (coin_sentiment['classification'] == sentiment)
        &
        (coin_sentiment['Trades'] >= 100)
    ]
    .sort_values(
        by='Total_PnL',
        ascending=False
    )
    .head(5)
)

        print(f"\nTop Coins During {sentiment}:\n")
        print(
            subset[
                ['Coin', 'Total_PnL', 'Avg_PnL']
            ]
        )

    return coin_sentiment

if __name__ == "__main__":

    from data_loading import (
        load_fear_greed_data,
        load_trader_data
    )

    from preprocessing import (
        preprocess_pipeline
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

    sentiment_performance_analysis(
    merged_df
)

    coin_analysis(
    merged_df
)

    top_trader_analysis(
    merged_df
)

    elite_trader_analysis(
    merged_df
)

    elite_sentiment_analysis(
    merged_df
)

    risk_adjusted_sentiment_analysis(
    merged_df
)

    sentiment_strategy_ranking(
    merged_df
)

    coin_sentiment_analysis(
    merged_df
)

    direction_analysis(
    merged_df
)

    statistical_test(
    merged_df
)

    generate_key_insights(
    merged_df
)
sentiment_stats = sentiment_performance_analysis(merged_df)

coin_stats = coin_analysis(merged_df)

top_traders = top_trader_analysis(merged_df)

direction_stats = direction_analysis(merged_df)

risk_stats = risk_adjusted_sentiment_analysis(merged_df)

strategy_stats = sentiment_strategy_ranking(merged_df)

from visualization import create_all_visualizations

create_all_visualizations(
    merged_df,
    sentiment_stats,
    coin_stats,
    top_traders,
    direction_stats,
    risk_stats,
    strategy_stats
)