# StockSentimentAnalysis

Stock Price Sentiment Analysis classified by **Random Forest**.  


## Sample of Dataset
| Date      | Label | Top1 | ... | Top25|
| --------- | ----- | ---- | --- | ---- |
2008-08-08	| 0 | b"Georgia 'downs two Russian warplanes' as countries move to brink of war" | ... | b'Indian shoe manufactory  - And again in a series of "you do not like your work?"'|
2008-08-11  | 1 | b'Why wont America and Nato help us? If they wont help us now, why did we help them in Iraq?' | ... | b'Russia is so much better at war'|  

More information about dataset can be accessed by https://www.kaggle.com/aaron7sun/stocknews.

## Result
|   | precision  |  recall | f1-score |  support|
| - | ---------- | ------- | -------- | ------- | 
| 0 | 0.80       |0.01     |0.03      |299      |
| 1 |0.53        |1.00     |0.69      |331      |

_Accuracy = 0.53_ 


## Acknowledgements
Sun, J. (2016, August). Daily News for Stock Market Prediction, Version 1. Retrieved 01/09/21 from https://www.kaggle.com/aaron7sun/stocknews.


