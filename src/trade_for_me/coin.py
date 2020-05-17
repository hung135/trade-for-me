import cbpro
import os, sys
from tabulate import tabulate
public_client = cbpro.PublicClient()

class Coin:
    def __init__(self,coin,basecoin='BTC'):
        self.coin=coin.upper()
        self.basecoin=basecoin.upper()
        self.market=str(f'{coin}-{basecoin}').upper()
        self.marketusd=str(f'{coin}-USD').upper()
        self.price_asks={}
        self.price_bids={}
        self.positions={}
        self.auth_cbp()
    def get_positions(self):
        print("Getting account")
        x=self.auth_client.get_accounts()
        print(x)
    def auth_cbp(self):
        key=os.environ.get('CBPRO_KEY',None)
        b64secret=os.environ.get('CBPRO_SECRET_KEY',None)
        passphrase=os.environ.get('CBPRO_PASSPHRASE',None)
        if (key is None or b64secret is None or passphrase is None):
            print('KEY INFO REQUIRED')
            print(f'\texport CBPRO_KEY={key}')
            print(f'\texport CBPRO_SECRET_KEY={b64secret}')
            print(f'\texport CBPRO_PASSPHRASE={passphrase}')

            sys.exit('Set your Keys in Environment Variables')
        else:
            self.auth_client = cbpro.AuthenticatedClient(key, b64secret, passphrase)
        # Use the sandbox API (requires a different set of API access credentials)
            #self.auth_client = cbpro.AuthenticatedClient(key, b64secret, passphrase,
            #                            api_url="https://api-public.sandbox.pro.coinbase.com")

    def get_ratio(coin1,coin2):
        print(coin1[0][0],coin2[0][0])
        ratio=float(coin1[0][0])/float(coin2[0][0])
        ratio2=float(coin2[0][0])/float(coin1[0][0])
        return ratio,ratio2
    def get_asking(self,market,trans_type,level=1):
        cur_price=public_client.get_product_order_book(market,level=level)[trans_type]
        return  cur_price
    def get_asks(self):
        self.price_asks[self.marketusd]=self.get_asking(self.marketusd,'asks')
    def get_bids(self):
        self.price_bids[self.marketusd]=self.get_asking(self.marketusd,'bids')
 
    def pull_data(self):
        self.get_asks()
        self.get_bids()
    def print(self):
        btc=get_asking('BTC-USD','asks')
        alt_usd=get_asking(f'{self.coin}-USD','asks')
        alt_btc=get_asking(f'{self.coin}-BTC','asks') 
        print(btc,alt_usd,alt_btc)
    
    def print_table(self):
        header=['type','Market', 'Price','QTY','MYQTY']
        data=[  ]
        for k in self.price_asks.keys():
            p=self.price_asks[k][0][0]
            qty=self.price_asks[k][0][1]
            myqty=self.positions.get(k,0)
            data.append(['asks',k,p,qty,myqty])
            p=self.price_bids[k][0][0]
            qty=self.price_bids[k][0][1]
            data.append(['bids',k,p,qty,myqty])
            
        print(tabulate(data, headers=header))
        print('\n')