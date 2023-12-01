# import pandas_datareader.data as web
# from datetime import datetime as dt
# from yahoo_finance_api2 import share

# dt_now=dt.now()
# today = dt_now.strftime('%Y-%m-%d')
# start='2023-1-1'
# end=today

# stock_list=['N255','USDJPY']

# df=web.get_data_yahoo(f'{stock_list[0]}=X',start,end)
# print(df)

#ライブラリ参照
# import pandas_datareader.data as pdr
# import datetime

# #現在時刻の取得
# dt_now = datetime.datetime.now()

# #「yyyy-MM-dd」形式に変換
# today = dt_now.strftime('%Y-%m-%d')

# #変数の定義
# currencyCode = 'USDJPY'		#通貨ペア
# startDate = '2022-10-02'	#データ取得期間（開始日）
# endDate = today			#データ取得期間（終了日）

# #データ取得
# tempData = pdr.get_data_yahoo(f'{currencyCode}=X', startDate, endDate)

# #出力
# print(tempData)

import os
import datetime as dt
import pandas_datareader.data as pdr
import yfinance as yf
yf.pdr_override()

symbol = '8306.T'
# data_source = 'yahoo' <= yfinanceをオーバーライドして使用する場合、data_sourceの指定は不要です。
start = dt.date.today()
end = dt.date.today()

df = pdr.DataReader(symbol, start, end)
df.sort_index(ascending=False)[:5] # Yahoo Financeのデータは、古いものから順に並んでいるため、最新データから並べる際は、降順にする必要があります。

print(df)

# 実行結果
#                    Open         High          Low        Close    Adj Close     Volume
# Date
# 2020-01-06   584.799988   585.200012   577.200012   582.099976   489.231445   56430300
# 2020-01-07   581.000000   584.299988   580.599976   584.099976   490.912384   41756400
# 2020-01-08   574.099976   575.799988   570.599976   574.000000   482.423737   67480800
# 2020-01-09   586.000000   586.200012   578.599976   580.000000   487.466431   41613400
# 2020-01-10   580.700012   581.700012   577.700012   578.200012   485.953674   27565200
# ...                 ...          ...          ...          ...          ...        ...
# 2023-11-14  1283.000000  1286.000000  1273.500000  1284.000000  1284.000000   70706100
# 2023-11-15  1304.500000  1304.500000  1252.000000  1259.000000  1259.000000  159360000
# 2023-11-16  1259.000000  1286.000000  1259.000000  1264.000000  1264.000000   84402000
# 2023-11-17  1249.500000  1264.000000  1239.000000  1264.000000  1264.000000   69386000
# 2023-11-20  1262.000000  1284.500000  1262.000000  1276.000000  1276.000000   74423400