#!/usr/bin/env python3

"""
Polystock
Author: Ashar Latif
Date: 2021-06-09
Description: A ticker displayer for polybar.
Contact: ashar.k.latif@gmail.com
"""

from datetime import datetime
from datetime import time
from datetime import timedelta
import argparse

from yahoo_fin import stock_info as si

import symbols

DEBUG: bool = False

# How many decimal place to show in stock price.
ROUND_NUMBER: int = 2

# Color definitions
TICKER_NAME_COLOR: str = '#fa83aa'
POSITIVE_PERCENTAGE_COLOR: str = '#05fc15'
NEGATIVE_PERCENTAGE_COLOR: str = '#fc0511'

# Market Times
PREMARKET_OPEN = time(4,0)
MARKET_OPEN = time(9,30)
MARKET_CLOSE = time(16,0)
POSTMARKET_CLOSE = time(20,0)

def ticker_value(ticker: str) -> str:
    """Get ticker price

    Retrieves price of ticker

    Args:
        ticker: The ticker to get a stock price on and to display.

    Returns:
        output: Stock price and ticker of a stock with format 'TICKER': 'PRICE'.
    """
    ticker_price = si.get_live_price(ticker)
    percentage = gain_loss(ticker, ticker_price)
    output = ticker + ': ' + str(round(ticker_price, ROUND_NUMBER)) + percentage
    if DEBUG:
        print(str(output))
    return output

def gain_loss(ticker: str, today) -> str:
    """Calculate percent change

    Calculates percent price change from previous close and formats colorized string

    Args:
        ticker: The ticker to calculate percent change on.
        today:  Current price of the cicker.

    Returns:
        output: Colorized directional percentage movement of the ticker
    """
    if DEBUG:
        print("Starting gain_loss function")
    start = last_trading_day()
    yesterday = si.get_data(ticker, start_date = start).iloc[0]['close']
    if DEBUG:
        print("Last close: " + str(yesterday))
    percentage = round(((100 * today) / yesterday) - 100, 2)
    if DEBUG:
        print("Percentage move:" + str(percentage))
    if percentage >= 0:
        color = POSITIVE_PERCENTAGE_COLOR
    elif percentage < 0:
        color = NEGATIVE_PERCENTAGE_COLOR
    output = str('%{F' + color + '}' + str(percentage) + '%\%{F-}')
    return output
