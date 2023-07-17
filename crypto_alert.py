from unicorn_binance_websocket_api.manager import BinanceWebSocketApiManager
import os

# import class to process stream data
from process import BinanceWebSocketApiProcessStreams

# create instance of BinanceWebSocketApiManager and provide the function for stream processing
binance_websocket_api_manager = BinanceWebSocketApiManager(BinanceWebSocketApiProcessStreams.process_stream_data)

# define channels
channels = {'aggTrade'}

# define markets
markets = {'luncusdt'}

# create stream
trade_stream_id = binance_websocket_api_manager.create_stream(channels, markets)
