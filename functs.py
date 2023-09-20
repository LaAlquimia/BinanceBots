import pandas as pd



async def processKlines(client, _symbol):
    kline =client.futures_klines(symbol= _symbol, interval =  client.KLINE_INTERVAL_5MINUTE, limit = 288)
    df = pd.DataFrame(pd.to_numeric([x[5] for x in kline]))
    prev = df.tail(3).iloc[1] 
    mean_volume = df.mean() 
    value = ((prev- mean_volume)/ prev).values[0]
    if value > 1:
        print("Alert in :" , _symbol) 
    return 

async def filtrarVol():
    return ()


async def get_available_tokens(client):
    return ([x['symbol'] for x  in     client.futures_exchange_info()['symbols'] if x[ 'status'] == 'TRADING' ])