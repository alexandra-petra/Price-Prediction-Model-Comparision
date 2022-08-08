# Price-Prediction-Model-Comparision

![alt text](https://images.unsplash.com/file-1636585210491-f28ca34ea8ecimage)

- performed several ML on the same dataset, for two datasets  scrapped from tsenomer.ru: for Moscow and St. Petersburg.
- First round, with St. Petersburg prices, resulted in poor performance of the models, however, the winning one was XBoost. However, we came to conclusion, that models were overfitted, and continued the experiment.
- For second round we used a bigger dataset for prices in Moscow, and applied another encoding technique to the data.
- Decision Tree is the winner amongst the other models. 
- Feeding with more data definitely helped to increase performance
- So did the changing of the encoding method. For our purposes LabelEncoder() or OrdinarEncoder() is the best fit, since we want to teach the model the corelation between certain grocery shop and the price level in it (how does the shop affect the price). 
