import cbpro
import os

public_client = cbpro.PublicClient()

class Coin():
    def init(self,coin,basecoin):
        self.coin=coin.upper()
        self.basecoin=basecoin.upper()
        self.market=str(f'{coin}-{basecoin}').upper()
        self.marketusd=str(f'{coin}-USD').upper()
        self.price_asks={}
        self.price_bids={}
    def auth_cbp():
        key=os.environ.get('CBPRO_KEY',None)
        b64secret=os.environ.get('CBPRO_SCERET_KEY',None)
        passphrase=os.environ.get('CBPRO_PASSPHRASE',None)
        if (key is None or b64secret is None or passphrase is None):
            print('KEY INFO REQUIRED')
            print('\texport CBPRO_KEY=<key>')
            print('\texport CBPRO_SCERET_KEY=<secret_key>',None)
            print('\texport CBPRO_PASSPHRASE=<phrase>')

            sys.exit('1')
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
    def get_asking(market,trans_type,level=1):
        cur_price=public_client.get_product_order_book(market,level=level)[trans_type]
        return  cur_price
    def get_asks(self):
        self.price_asks[self.marketusd]=get_asking(self.marketusd,'asks')
    def get_bids(self):
        self.price_bids[self.marketusd]=get_asking(self.marketusd,'bids')
        
    def pull_data(self):
        self.get_asks()
        self.get_bids()
    def print(self):
        btc=get_asking('BTC-USD','asks')
        alt_usd=get_asking(f'{self.coin}-USD','asks')
        alt_btc=get_asking(f'{self.coin}-BTC','asks') 
        print(btc,alt_usd,alt_btc)