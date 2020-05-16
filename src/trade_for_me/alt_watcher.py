# -*- coding: utf-8 -*-
import argparse
import sys
import logging
import time

from trade_for_me import __version__
import cbpro
import pprint
from tabulate import tabulate


__author__ = "Hung Nguyen"
__copyright__ = "Hung Nguyen"
__license__ = "mit"

_logger = logging.getLogger(__name__)

public_client = cbpro.PublicClient()
def auth_cbp():
 
  auth_client = cbpro.AuthenticatedClient(key, b64secret, passphrase)
  # Use the sandbox API (requires a different set of API access credentials)
  auth_client = cbpro.AuthenticatedClient(key, b64secret, passphrase,
                                    api_url="https://api-public.sandbox.pro.coinbase.com")
def get_ratio(coin1,coin2):
  print(coin1[0][0],coin2[0][0])
  ratio=float(coin1[0][0])/float(coin2[0][0])
  ratio2=float(coin2[0][0])/float(coin1[0][0])
  return ratio,ratio2
def print_table(basecoin,altcoin,btc,btc_alt,dollar):
  header=['Market', 'Price']
  data=[[basecoin, f'${btc[0][0]}']
        , [f'{altcoin}', f'${dollar}']
        , [f'{altcoin}-{basecoin}', f'{btc_alt}']
        ]

  print(tabulate(data, headers=header))
  print('\n')
   #print(f'{basecoin}: ${btc[0][0]} {altcoin}->USD: ${usd_alt} {altcoin}-{basecoin}: {btc_alt} {altcoin}->{basecoin}->USD: ${dollar}')
def get_asking(market,trans_type,level=1):
   
  try:
    x=public_client.get_product_order_book(market,level=level)
    cur_price=x[trans_type]
  except Exception as e:
    print("Error Getting ",e)
    return [[0,0,0]]
  return  cur_price 
def alt_watcher(altcoin,basecoin='BTC'):
    """Watch an Alcoin to BTC (base coin) or USD

    Args:
 
      altcoin (string): string

    Returns:
      string: Sucess status string and time
    """
    
 
    # Get the order book at the default level.
    while True:
      btc=get_asking(f'{basecoin}-USD','asks')
      alt_usd=get_asking(f'{altcoin}-USD','asks')
      alt_btc=get_asking(f'{altcoin}-{basecoin}','asks')
      
      usd_alt=alt_usd[0][0]
      btc_alt=alt_btc[0][0]
      dollar=round(float(btc_alt)*float(btc[0][0]),4)
      print_table(basecoin,altcoin,btc,btc_alt,dollar)
      #print(f'{basecoin}: ${btc[0][0]} {altcoin}->USD: ${usd_alt} {altcoin}-{basecoin}: {btc_alt} {altcoin}->{basecoin}->USD: ${dollar}')
      time.sleep(3)
    return 'abc'


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Just a Fibonacci demonstration")
    parser.add_argument(
        "--version",
        action="version",
        version="trade-for-me {ver}".format(ver=__version__))
 
    parser.add_argument(
        dest="c",
        help="altcoin short Name (ETH, ADA, REP etc..)",
        type=str,
        metavar="STRING")
    parser.add_argument(
    
        dest="bc",
        help="base coin to watch default (BTC))",
        type=str,
        default='BTC',
        metavar="STRING")
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO)
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG)
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(level=loglevel, stream=sys.stdout,
                        format=logformat, datefmt="%Y-%m-%d %H:%M:%S")


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    _logger.debug("Starting crazy calculations...")
    alt_watcher(args.c,args.bc)
    #print("The {}-th Fibonacci number is {}".format(args.n, trade_for_(args.n)))
    _logger.info("Script ends here")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
