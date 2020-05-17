import cbpro
import os, sys
from tabulate import tabulate
from utils import CircularQueQue
from utils import clear
import pprint
public_client = cbpro.PublicClient()

class Coin:
    positions=None
    def __init__(self,coin,basecoin='BTC'):
        self.coin=coin.upper()
        self.basecoin=basecoin.upper()
        self.market=str(f'{coin}-{basecoin}').upper()
        self.marketusd=str(f'{coin}-USD').upper()
        self.price_asks={}
        self.price_bids={}
        self.last_trade_id=0
        self.last_trade_price=0
        self.last_trade_size=0
       
        self.auth_cbp()
        if self.positions is None:
            self.positions={}
        self.session_price=CircularQueQue(length=1*60*60*2) #2 hours 
        self.session_qty=CircularQueQue(length=1*60*60*2) 
    def get_cost(self,position):
        position['cost']=0.385

    def get_positions(self):
        print("Getting account")
        x=self.auth_client.get_accounts()
        for a in x:
            if str(a['currency'])==str(self.coin):
                 
                self.positions[self.coin]=a
                self.get_cost(a)
        #pprint.pprint(self.positions)
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
    def get_last_traded(self):
        
        x=public_client.get_product_trades(product_id=self.marketusd)
        
        if len(self.session_price.list)<1:
            print(x)
            for a in x:
 
                try:
                    self.last_trade_id=int(a['trade_id'])
                    self.last_trade_price=float(a['price'])
                    self.last_trade_size=float(a['size'])
                    #print(self.last_trade_id,int(a['trade_id']))
                    self.session_price.add(self.last_trade_price)
                    self.session_qty.add(self.last_trade_size)
                except:
                    pass
        else:
            for a in x:
                if self.last_trade_id<int(a['trade_id']):
                    self.last_trade_id=int(a['trade_id'])
                    self.last_trade_price=float(a['price'])
                    self.last_trade_size=float(a['size'])
                    self.session_price.add(self.last_trade_price)
                    self.session_qty.add(self.last_trade_size)
                break
        
        
    def pull_data(self):
        self.get_asks()
        self.get_bids()
        self.get_last_traded()
 
        
             
           
   
    
    def print_table(self):
        header=['type','Market', 'Price','QTY','MyQTY','My$','Cost','Prof','SessionAvg','SessTot']
        data=[  ]
        for k in self.price_asks.keys():
            p=self.price_asks[k][0][0]
            qty=self.price_asks[k][0][1]
            print(k)
            myqty=float(self.positions.get(k.split('-')[0],{"balance": 0.0})['balance'])
            cost=float(self.positions.get(k.split('-')[0],{"cost": 0.0})['cost'])
            data.append(['asks',k,p,qty,myqty,'',''])
            p=self.price_bids[k][0][0]
            mydollar=round(myqty*float(p),2)
             
            profit='$0.00'
            if cost*myqty>mydollar:
                profit=f'-${round(cost*myqty-mydollar,2)}'
            else:
                profit=f'+${round(mydollar-cost*myqty,2)}'
            qty=self.price_bids[k][0][1]
            data.append(['bids',k,p,qty,myqty,f'${mydollar}',cost,profit,self.session_price.avg(),sum(self.session_qty.list)])
            
        clear()
        #print(self.session_price.list)
        print(f'Trade History: {(self.session_price.pos)}/{self.session_price.length}',
                f'Highest: {self.session_price.highest}',f'Lowest: {self.session_price.lowest}'
                ,f'LAST: {self.last_trade_price}',f'Size: {self.last_trade_size}'
                ,'\n')
        
        print(tabulate(data, headers=header))
       