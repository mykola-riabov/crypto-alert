# crypto-alert
The functionality of the script is to get data from the Binance exchange and send it to messengers. In this case, the script gets the aggregated volume of the LUNC cryptocurrency and sends the information to Telegram if certain values are met.

Here is more detailed information on how the script works:
1. The script first connects to the Binance exchange API.
2. Then the script requests the aggregated volume of the LUNC cryptocurrency.
3. The script analyzes the received volume and determines if it is above or below the set threshold value.
4. If the volume is above the threshold value, the script sends the information about it to Telegram.

The script can be used to monitor the trading volume of cryptocurrencies and receive notifications when the volume reaches certain values. This can be useful for traders who want to track market volatility and make informed decisions on buying or selling cryptocurrencies.

To run the script, you need to install `pip3 install unicorn_binance_websocket_api

![1.png](screen%2F1.png)

![2.png](screen%2F2.png)

To automatically start and use the script, you can use an example service unit
