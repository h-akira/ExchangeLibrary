#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime

def check_summer_time(now=None):
  if now is None:
    now = datetime.datetime.now()
  if now.month == 3:
    # 第二日曜日以降は夏時間
    if now.day - now.weekday() >= 8:
      return True
    else:
      return False
  elif now.month == 11:
    # 第一日曜日以降は冬時間
    if now.day - now.weekday() <= 1:
      return True
    else:
      return False
  elif 4<= now.month <= 10:
    return True
  else:
    return False
def market_open(now=None, diff_from_utc=0):
  # 年末年始等は非対応
  # ニューヨーク時間にする
  if now is None:
    now = datetime.datetime.utcnow() - datetime.timedelta(hours=5)
  else:
    now = now - datetime.timedelta(hours=diff_from_utc) - datetime.timedelta(hours=5)
  # 夏時間なら1時間進める
  if check_summer_time(now):
    now = now + datetime.timedelta(hours=1)
  # 判定
  if 1 <= now.weekday() <= 4:
    return True
  elif now.weekday() == 0 and now.hour >= 17:  
    return True
  elif now.weekday() == 5 and now.hour < 17:
    return True
  else:
    return False
