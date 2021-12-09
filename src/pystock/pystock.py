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
