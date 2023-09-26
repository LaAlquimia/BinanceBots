import pandas as pd

async def processKline(client, _symbol, interval : int):
    kline =  pd.DataFrame(client.futures_klines(symbol= _symbol, interval =  client.KLINE_INTERVAL_5MINUTE, limit = interval) ,
                          columns=[
    "time_open",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "time_close",
    "quote_aset_volume",
    "trades",
    "",
    "",
    "",] )
    kline.close = pd.to_numeric(kline.close)
    kline.high = pd.to_numeric(kline.high)
    kline.low = pd.to_numeric(kline.low)
    kline.open = pd.to_numeric(kline.open)    
    kline.volume = pd.to_numeric(kline.volume)    
    return (kline) 



async def volumeSignal(client, _symbol):
    kline =client.futures_klines(symbol= _symbol, interval =  client.KLINE_INTERVAL_5MINUTE, limit = 20)
    df = pd.DataFrame(pd.to_numeric([x[5] for x in kline]))
    prev = df.tail(3).iloc[1] 
    mean_volume = df.mean() 
    value = ((prev- mean_volume)/ mean_volume).values[0]
    if value> 1:
        print(_symbol , value) 
    return 

async def filtrarVol():
    return ()


async def get_available_tokens(client):
    return ([x['symbol'] for x  in     client.futures_exchange_info()['symbols'] if x[ 'status'] == 'TRADING' ])
