import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")


def plot_sentiment_performance(sentiment_stats):

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=sentiment_stats,
        x='classification',
        y='Average_PnL',
        color='teal'
    )

    plt.title(
        "Average Profitability by Market Sentiment"
    )

    plt.xlabel("Sentiment")
    plt.ylabel("Average Closed PnL")

    plt.tight_layout()
    plt.savefig(
        "outputs/sentiment_performance.png"
    )
    plt.show()
    plt.close()


def plot_sentiment_winrate(sentiment_stats):

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=sentiment_stats,
        x='classification',
        y='Win_Rate',
        color='goldenrod'
    )

    plt.title(
        "Win Rate by Market Sentiment"
    )

    plt.xlabel("Sentiment")
    plt.ylabel("Win Rate (%)")

    plt.tight_layout()
    plt.savefig(
        "outputs/sentiment_winrate.png"
    )
    plt.show()
    plt.close()


def plot_top_coins(coin_stats):

    top10 = coin_stats.head(10)

    plt.figure(figsize=(12, 6))

    sns.barplot(
        x=top10.index,
        y=top10['Total_PnL'],
        color='mediumpurple'
    )

    plt.title(
        "Top 10 Coins by Total Profit"
    )

    plt.xlabel("Coin")
    plt.ylabel("Total PnL")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.savefig(
        "outputs/top_coins.png"
    )
    plt.show()
    plt.close()


def plot_top_traders(top_traders):

    top10 = top_traders.head(10)

    plt.figure(figsize=(12, 6))

    sns.barplot(
        x='Total_PnL',
        y='Account',
        data=top10,
        color='crimson'
    )

    plt.title(
        "Top 10 Traders by Profitability"
    )

    plt.xlabel("Total PnL")
    plt.ylabel("Trader Account")

    plt.tight_layout()
    plt.savefig(
        "outputs/top_traders.png"
    )
    plt.show()
    plt.close()


def plot_direction_analysis(direction_stats):

    plt.figure(figsize=(12, 6))

    sns.barplot(
        data=direction_stats,
        x='Direction',
        y='Average_PnL',
        color='darkorange'
    )

    plt.title(
        "Average Profitability by Trade Direction"
    )

    plt.xlabel("Direction")

    plt.ylabel("Average PnL")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        "outputs/direction_analysis.png"
    )

    plt.show()
    plt.close()


def plot_risk_adjusted_returns(risk_stats):

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=risk_stats,
        x='classification',
        y='Risk_Adjusted_Return',
        color='seagreen'
    )

    plt.title(
        "Risk Adjusted Returns by Sentiment"
    )

    plt.xlabel("Sentiment")

    plt.ylabel("Risk Adjusted Return")

    plt.tight_layout()

    plt.savefig(
        "outputs/risk_adjusted_returns.png"
    )

    plt.show()
    plt.close()


def plot_strategy_ranking(strategy_stats):

    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=strategy_stats,
        x='classification',
        y='Avg_PnL',
        color='royalblue'
    )

    plt.title(
        "Sentiment Strategy Ranking"
    )

    plt.xlabel("Sentiment")

    plt.ylabel("Average PnL")

    plt.tight_layout()

    plt.savefig(
        "outputs/strategy_ranking.png"
    )
    plt.show()
    plt.close()


def plot_coin_frequency(df):

    top20 = (
        df['Coin']
        .value_counts()
        .head(20)
    )

    plt.figure(figsize=(12, 6))

    sns.barplot(
        x=top20.index,
        y=top20.values
    )

    plt.title(
        "Top 20 Most Traded Coins"
    )

    plt.xlabel("Coin")

    plt.ylabel("Trade Count")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(
        "outputs/coin_frequency.png"
    )
    plt.show()
    plt.close()


def create_all_visualizations(
    merged_df,
    sentiment_stats,
    coin_stats,
    top_traders,
    direction_stats,
    risk_stats,
    strategy_stats
):

    plot_sentiment_performance(
        sentiment_stats
    )

    plot_sentiment_winrate(
        sentiment_stats
    )

    plot_top_coins(
        coin_stats
    )

    plot_top_traders(
        top_traders
    )

    plot_direction_analysis(
        direction_stats
    )

    plot_risk_adjusted_returns(
        risk_stats
    )

    plot_strategy_ranking(
        strategy_stats
    )

    plot_coin_frequency(
        merged_df
    )

    print(
        "\nAll visualizations saved in outputs/ folder."
    )

if __name__ == "__main__":

    import os

    os.makedirs("outputs", exist_ok=True)

    from data_loading import (
        load_fear_greed_data,
        load_trader_data
    )

    from preprocessing import (
        preprocess_pipeline
    )

    from analysis import (
        sentiment_performance_analysis,
        coin_analysis,
        top_trader_analysis,
        direction_analysis,
        risk_adjusted_sentiment_analysis,
        sentiment_strategy_ranking
    )

    print("Loading data...")

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

    print("Running analysis...")

    sentiment_stats = sentiment_performance_analysis(merged_df)

    coin_stats = coin_analysis(merged_df)

    top_traders = top_trader_analysis(merged_df)

    direction_stats = direction_analysis(merged_df)

    risk_stats = risk_adjusted_sentiment_analysis(merged_df)

    strategy_stats = sentiment_strategy_ranking(merged_df)

    print("Creating visualizations...")

    create_all_visualizations(
        merged_df,
        sentiment_stats,
        coin_stats,
        top_traders,
        direction_stats,
        risk_stats,
        strategy_stats
    )

    print("Done!")