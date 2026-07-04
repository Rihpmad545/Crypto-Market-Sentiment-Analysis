# Trader Behavior Analysis Using Fear & Greed Index

## Project Overview

This project analyzes the relationship between cryptocurrency market sentiment and trader performance. The study combines historical trader transaction data with the Crypto Fear & Greed Index to investigate how different market sentiment conditions influence profitability, win rates, and trading behavior.

The objective is to identify profitable market conditions, analyze elite trader strategies, and discover sentiment-driven trading opportunities.

---

# Dataset Description

## 1. Fear & Greed Index Dataset

The Fear & Greed Index measures market sentiment and classifies market conditions into:

* Extreme Fear
* Fear
* Neutral
* Greed
* Extreme Greed

The dataset contains:

| Column         | Description                   |
| -------------- | ----------------------------- |
| timestamp      | Date of sentiment observation |
| classification | Sentiment category            |
| value          | Fear & Greed score            |

---

## 2. Historical Trading Dataset

The trader dataset contains detailed transaction records.

Important fields used:

| Column     | Description           |
| ---------- | --------------------- |
| Account    | Trader wallet/account |
| Coin       | Cryptocurrency traded |
| Direction  | Trade direction       |
| Closed PnL | Profit or Loss        |
| Fee        | Trading fee           |

---

# Data Preprocessing

The following preprocessing steps were performed:

1. Converted timestamps into datetime format.
2. Matched each trade with the corresponding Fear & Greed sentiment.
3. Removed invalid records.
4. Handled missing values.
5. Created engineered features:

   * Winning_Trade
   * Profit_Efficiency
   * Fee_Efficiency

Preprocessing completed successfully with only six unmatched sentiment records.

---

# Methodology

The analysis was divided into multiple sections:

## Sentiment Performance Analysis

Evaluated:

* Total Trades
* Total Profit
* Average Profit
* Median Profit
* Win Rate
* Profit Efficiency
* Fee Efficiency

---

## Coin Analysis

Studied:

* Most profitable coins
* Most frequently traded coins
* Coin profitability across different sentiment regimes

---

## Trader Analysis

Investigated:

* Top performing traders
* Elite trader behavior
* Differences between elite and normal traders

---

## Statistical Validation

Applied the Kruskal-Wallis statistical test to determine whether profitability differs significantly across sentiment categories.

---

# Results

## Sentiment Performance

| Sentiment     | Average PnL |
| ------------- | ----------: |
| Extreme Greed |       67.89 |
| Fear          |       54.29 |
| Greed         |       42.74 |
| Extreme Fear  |       34.54 |
| Neutral       |       34.31 |

### Observation

Extreme Greed produced the highest average profitability.

---

## Win Rate Analysis

| Sentiment     | Win Rate (%) |
| ------------- | -----------: |
| Extreme Greed |        46.49 |
| Fear          |        42.08 |
| Neutral       |        39.70 |
| Greed         |        38.48 |
| Extreme Fear  |        37.06 |

### Observation

Traders achieved the highest win rate during Extreme Greed periods.

---

## Most Profitable Coins

| Coin | Total PnL |
| ---- | --------: |
| @107 |     2.78M |
| HYPE |     1.95M |
| SOL  |     1.64M |
| ETH  |     1.32M |
| BTC  |      868K |

### Observation

The coin @107 generated the highest cumulative profit among all traded assets.

---

## Most Frequently Traded Coins

| Coin | Trades |
| ---- | -----: |
| HYPE | 68,005 |
| @107 | 29,992 |
| BTC  | 26,064 |
| ETH  | 11,158 |
| SOL  | 10,691 |

### Observation

HYPE was the most actively traded cryptocurrency.

---

# Elite Trader Analysis

Elite traders were defined as traders belonging to the top 10% based on cumulative profitability.

## Comparison

| Metric      | Elite Traders | Normal Traders |
| ----------- | ------------: | -------------: |
| Average PnL |        106.28 |          29.97 |
| Win Rate    |        40.70% |         41.26% |

### Observation

Elite traders generated significantly higher profits despite having similar win rates. This suggests superior position sizing and risk management rather than simply winning more trades.

---

# Elite Trader Sentiment Behavior

## Elite Traders

* Fear: 44.64%
* Neutral: 20.52%
* Greed: 18.54%
* Extreme Fear: 10.90%
* Extreme Greed: 5.41%

## Normal Traders

* Greed: 25.54%
* Fear: 24.26%
* Extreme Greed: 23.35%
* Neutral: 16.97%
* Extreme Fear: 9.88%

### Observation

Elite traders disproportionately traded during Fear conditions, indicating contrarian behavior.

---

# Risk-Adjusted Sentiment Analysis

| Sentiment     | Risk Adjusted Return |
| ------------- | -------------------: |
| Extreme Greed |               0.0885 |
| Neutral       |               0.0663 |
| Fear          |               0.0580 |
| Greed         |               0.0383 |
| Extreme Fear  |               0.0304 |

### Observation

Extreme Greed generated the highest return per unit of risk.

---

# Sentiment Strategy Ranking

| Rank | Sentiment     | Average PnL |
| ---- | ------------- | ----------: |
| 1    | Extreme Greed |       67.89 |
| 2    | Fear          |       54.29 |
| 3    | Greed         |       42.74 |
| 4    | Extreme Fear  |       34.54 |
| 5    | Neutral       |       34.31 |

### Observation

Extreme Greed consistently outperformed all other sentiment categories.

---

# Direction Analysis

Top profitable trade directions:

| Direction         | Average PnL |
| ----------------- | ----------: |
| Auto-Deleveraging |     7184.81 |
| Short > Long      |      154.19 |
| Sell              |      146.05 |
| Close Short       |      103.01 |
| Close Long        |       74.43 |

### Observation

Trade-closing actions generated the majority of realized profits.

---

# Statistical Testing

## Kruskal-Wallis Test

Statistic: 1226.9956

P-value: < 0.000001

### Result

A statistically significant difference exists between sentiment groups.

Therefore, market sentiment has a measurable impact on trading profitability.

---

# Visualizations Generated

The project generated the following visualizations:

1. Average Profitability by Market Sentiment
2. Win Rate by Sentiment
3. Top 10 Coins by Profitability
4. Top 10 Traders by Profitability
5. Direction Analysis
6. Risk Adjusted Returns
7. Strategy Ranking
8. Coin Trading Frequency

These visualizations are stored in the outputs folder.

---

# Key Insights

1. Extreme Greed delivered the highest average profitability and win rate.
2. Fear conditions were heavily favored by elite traders.
3. Elite traders achieved more than 3× the average profitability of normal traders.
4. Coin @107 was the most profitable asset.
5. HYPE was the most actively traded coin.
6. Statistical testing confirmed significant profitability differences across sentiment regimes.
7. Risk-adjusted returns were strongest during Extreme Greed conditions.

---

# Conclusion

This analysis demonstrates a strong relationship between market sentiment and trading performance. Traders operating during Extreme Greed conditions achieved the highest profitability, while elite traders exhibited contrarian tendencies by participating more heavily during Fear periods.

The findings suggest that sentiment indicators can be valuable signals for identifying favorable trading environments and designing sentiment-aware trading strategies.

Future work could include predictive machine learning models, real-time sentiment monitoring, and automated strategy generation based on market sentiment dynamics.
