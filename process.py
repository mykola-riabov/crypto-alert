from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import requests
import sys

found = 'https://api.telegram.org'

token = 'Your Telegram token'
action = '/sendMessage?'

chat_id = 'Your Telegram chat id'
txt = '&text='

try:
    from unicorn_fy.unicorn_fy import UnicornFy
except ImportError:
    print("Please install `unicorn-fy`! https://pypi.org/project/unicorn-fy/")
    sys.exit(1)


class BinanceWebSocketApiProcessStreams(object):
    @staticmethod
    def process_stream_data(received_stream_data_json, stream_buffer_name="False"):
        exchange = "binance.com"
        if exchange == "binance.com" or exchange == "binance.com-testnet":
            unicorn_fied_stream_data = UnicornFy.binance_com_websocket(received_stream_data_json)
        else:
            print("Not a valid exchange: " + str(exchange))

        # Now you can call different methods for different `channels`, here called `event_types`.
        # Its up to you if you call the methods in the bottom of this file or to call other classes which do what
        # ever you want to be done.
        try:
            if unicorn_fied_stream_data['event_type'] == "aggTrade":
                BinanceWebSocketApiProcessStreams.aggtrade(unicorn_fied_stream_data)
            elif unicorn_fied_stream_data['event_type'] == "trade":
                BinanceWebSocketApiProcessStreams.trade(unicorn_fied_stream_data)
            elif unicorn_fied_stream_data['event_type'] == "kline":
                BinanceWebSocketApiProcessStreams.kline(unicorn_fied_stream_data)
            elif unicorn_fied_stream_data['event_type'] == "24hrMiniTicker":
                BinanceWebSocketApiProcessStreams.miniticker(unicorn_fied_stream_data)
            elif unicorn_fied_stream_data['event_type'] == "24hrTicker":
                BinanceWebSocketApiProcessStreams.ticker(unicorn_fied_stream_data)
            elif unicorn_fied_stream_data['event_type'] == "depth":
                BinanceWebSocketApiProcessStreams.miniticker(unicorn_fied_stream_data)
            else:
                BinanceWebSocketApiProcessStreams.anything_else(unicorn_fied_stream_data)
        except KeyError:
            BinanceWebSocketApiProcessStreams.anything_else(unicorn_fied_stream_data)
        except TypeError:
            pass

    @staticmethod
    def aggtrade(stream_data):
        print(stream_data)
        alert = float(5000)
        name = f"{stream_data['symbol']}"
        price = f"{stream_data['price']}"
        volume = f"{stream_data['quantity']}"
        trade_action = f"{stream_data['is_market_maker']}"
        if trade_action == 'True':
            trade_action = 'Sell'
        else:
            trade_action = 'Buy'
        q = float(volume)
        usd = float(price) * q
        print(usd)
        if usd > alert:
            print(name + str(usd))
            message = '_____________________________' + '\n' \
              + '\n' + 'symbol: ' + str(name) \
              + '\n' + 'price: ' + str(price) \
              + '\n' + 'volume: ' + str(volume) \
              + '\n' + 'volume in USD: ' + str(usd) \
              + '\n' + 'action: ' + str(trade_action)
            msg = found + token + action + chat_id + txt + message
            data_t = requests.get(msg)

    @staticmethod
    def trade(stream_data):
        # print `trade` data
        print(stream_data)

    @staticmethod
    def kline(stream_data):
        # print `kline` data
        print(stream_data)

    @staticmethod
    def miniticker(stream_data):
        # print `miniTicker` data
        print(stream_data)

    @staticmethod
    def ticker(stream_data):
        # print `ticker` data
        print(stream_data)

    @staticmethod
    def depth(stream_data):
        # print `depth` data
        print(stream_data)

    @staticmethod
    def outboundAccountInfo(stream_data):
        # print `outboundAccountInfo` data from userData stream
        print(stream_data)

    @staticmethod
    def executionReport(stream_data):
        # print `executionReport` data from userData stream
        print(stream_data)

    @staticmethod
    def anything_else(stream_data):
        print(stream_data)


if __name__ == "__main__":
    print("Dont run this script, its for imports only!")
