# StocksAggregateDashboard
Stocks Aggregate Data Dashboard

Here is a frontend for the Django site that displays financial indicators for publicly traded companies. It contains the data of ~3600 tickers of the Vanguard Total Stock Market ETF (VTI). 

You can see the site in action at http://stocks.pp.ua/. It allows to select the stocks and sectors for long and short positions in the investment portfolio using the following indicators:

1. Forward P/E.
2. Leverage.
3. Margin.
4. Liquidity.
5. Cash flow.
6. CEO payment.

The [Piotroski F-score](https://www.aaii.com/journal/article/simple-methods-to-improve-the-piotroski-f-score) system inspired me to create this resource. The data is aggregated by business sectors and industries. See, for example, http://stocks.pp.ua/sector/financial-services/ and http://stocks.pp.ua/industry/banks-diversified/. As far as I know, aggregated data in such a form is not freely available anywhere else. 

However, I have not yet been able to derive any practical benefit from the processed data. The site makes it easy to see which companies in the sectors and industries are the best and the worst. However, the stock market is quite efficient. Good companies tend to have a high price (high P/E ratio). Also, cheap companies are cheap for a reason, due to their low-quality management or absence of moan against the competition.
