# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
[options.entry_points] section in setup.cfg:

    console_scripts =
         fibonacci = trade_for_me.skeleton:run

Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""

import argparse
import sys
import logging
import time

from trade_for_me import __version__
import cbpro
import pprint

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

def get_asking(market,trans_type,level=1):
  cur_price=public_client.get_product_order_book(market,level=level)[trans_type]
  return  cur_price
def alt_watcher(altcoin):
    """Watch an Alcoin to BTC or USD

    Args:
 
      altcoin (string): string

    Returns:
      string: Sucess status string and time
    """
    
 
    # Get the order book at the default level.
    while True:
      btc=get_asking('BTC-USD','asks')
      alt_usd=get_asking(f'{altcoin}-USD','asks')
      alt_btc=get_asking(f'{altcoin}-BTC','asks')
      
      print(btc,alt_usd,alt_btc)
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
    alt_watcher(args.c)
    #print("The {}-th Fibonacci number is {}".format(args.n, trade_for_(args.n)))
    _logger.info("Script ends here")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
