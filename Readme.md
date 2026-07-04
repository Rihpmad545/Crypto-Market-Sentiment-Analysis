# Crypto Market Sentiment vs Trader Performance Analysis

## Project Overview

This project analyzes the relationship between market sentiment and cryptocurrency trader performance. The analysis combines the Fear & Greed Index with historical trading data to determine how different market sentiments influence profitability, win rates, trading behavior, and overall performance.

The objective is to identify patterns that can help traders understand which market conditions are associated with better trading outcomes.

---

## Dataset Description

### 1. Fear & Greed Index Dataset

Contains daily market sentiment classifications:

* Extreme Fear
* Fear
* Neutral
* Greed
* Extreme Greed

The dataset provides sentiment labels that represent the overall emotional state of the cryptocurrency market.

### 2. Historical Trading Dataset

Contains trader activity information including:

* Account
* Coin
* Direction
* Closed PnL
* Fees
* Trade Size
* Timestamp

This dataset is used to evaluate trader performance under different market conditions.

---

## Dataset Availability

The original Hyperliquid historical trading dataset contains a large number of records and exceeds practical GitHub upload limits.

To keep the repository lightweight and easily accessible, a sample dataset containing the first 1000 records has been included:

* `historical_data_sample.csv`
* `fear_greed_index.csv`

The complete historical dataset was provided as part of the assignment and can be accessed through the original dataset links shared by the hiring team.

This repository contains all source code, analysis scripts, visualizations, and reports required to reproduce the project workflow.


## Project Objectives

The project aims to answer the following questions:

1. Does market sentiment affect trader profitability?
2. Which sentiment generates the highest average returns?
3. Which cryptocurrencies perform best during specific sentiment conditions?
4. How do elite traders behave compared to normal traders?
5. Are profitability differences across sentiment categories statistically significant?

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy

---

## Project Structure

```text
Intern Project/
│
├── data/
│   ├── historical_data.csv
│   └── fear_greed_index.csv
│
├── outputs/
│   ├── sentiment_performance.png
│   ├── sentiment_winrate.png
│   ├── top_coins.png
│   ├── top_traders.png
│   ├── direction_analysis.png
│   ├── risk_adjusted_returns.png
│   ├── strategy_ranking.png
│   └── coin_frequency.png
│
├── src/
│   ├── data_loading.py
│   ├── preprocessing.py
│   ├── analysis.py
│   └── visualization.py
│
├── report.md
├── README.md
└── requirements.txt
```

---

## Data Preprocessing

The preprocessing pipeline performs:

* Date formatting and alignment
* Dataset merging
* Missing value handling
* Feature engineering
* Win/Loss classification
* Profit efficiency calculation
* Fee efficiency calculation

Generated Features:

### Winning Trade

```python
Winning_Trade = Closed PnL > 0
```

### Profit Efficiency

```python
Profit_Efficiency = Closed PnL / Size USD
```

### Fee Efficiency

```python
Fee_Efficiency = Closed PnL / Fee
```

---

## Analysis Performed

### 1. Sentiment Performance Analysis

Metrics:

* Total Trades
* Total Profit
* Average Profit
* Median Profit
* Win Rate
* Profit Efficiency
* Fee Efficiency

---

### 2. Coin Performance Analysis

Evaluates:

* Most profitable coins
* Most traded coins
* Coin profitability rankings

---

### 3. Top Trader Analysis

Identifies:

* Highest earning traders
* Average trader profitability
* Win rate rankings

---

### 4. Elite Trader Analysis

Elite traders are defined as the top 10% of traders based on total profitability.

Comparison metrics:

* Average PnL
* Win Rate
* Trading behavior

---

### 5. Elite Sentiment Behavior

Compares sentiment exposure between:

* Elite Traders
* Normal Traders

This helps identify whether successful traders prefer certain market conditions.

---

### 6. Direction Analysis

Performance evaluation based on:

* Close Long
* Close Short
* Sell
* Buy
* Other trade directions

Metrics:

* Total Profit
* Average Profit
* Win Rate

---

### 7. Risk Adjusted Return Analysis

Formula:

```python
Risk Adjusted Return =
Average PnL / Standard Deviation of PnL
```

This measures return relative to volatility.

---

### 8. Sentiment Strategy Ranking

Ranks sentiment categories using:

* Average Profitability
* Win Rate
* Trade Count

---

### 9. Coin × Sentiment Analysis

Identifies:

* Best coins during Extreme Fear
* Best coins during Fear
* Best coins during Neutral
* Best coins during Greed
* Best coins during Extreme Greed

---

### 10. Statistical Validation

Kruskal-Wallis Test is used to determine whether profitability differs significantly across sentiment categories.

Hypothesis:

H0:
All sentiment groups have similar profitability distributions.

H1:
At least one sentiment group differs significantly.

---

## Key Findings

### Most Profitable Sentiment

Extreme Greed generated the highest average profitability.

Average PnL:

67.89

Win Rate:

46.49%

---

### Best Overall Coin

@107 was the most profitable coin overall.

Total Profit:

2.78 Million+

---

### Elite Trader Insights

Elite Traders:

* Average PnL: 106.28
* Win Rate: 40.70%

Normal Traders:

* Average PnL: 29.97
* Win Rate: 41.26%

Elite traders generate significantly larger profits despite similar win rates.

---

### Risk Adjusted Performance Ranking

1. Extreme Greed
2. Neutral
3. Fear
4. Greed
5. Extreme Fear

Extreme Greed provides the best reward relative to risk.

---

### Statistical Results

Kruskal-Wallis Statistic:

1226.9956

P-value:

< 0.000001

Result:

There is a statistically significant difference in trader profitability across sentiment groups.

---

## Generated Visualizations

The project automatically generates:

1. Average Profitability by Sentiment
2. Win Rate by Sentiment
3. Top 10 Coins by Profit
4. Top 10 Traders by Profit
5. Trade Direction Analysis
6. Risk Adjusted Returns
7. Sentiment Strategy Ranking
8. Coin Frequency Analysis

All visualizations are stored inside the outputs folder.

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run analysis:

```bash
python src/analysis.py
```

The program will:

* Load datasets
* Perform preprocessing
* Execute all analyses
* Generate visualizations
* Save graphs to the outputs folder

---

## Conclusion

The analysis demonstrates that cryptocurrency trader performance varies significantly across market sentiment conditions. Extreme Greed consistently produced the strongest profitability and risk-adjusted returns, while elite traders displayed distinct trading behaviors compared to the broader market.

These findings suggest that incorporating market sentiment into trading strategies can provide valuable insights for improving decision-making and portfolio performance.
