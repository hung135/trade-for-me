# -*- coding: utf-8 -*-
import argparse
import sys
import logging
import time

from trade_for_me import __version__
import cbpro
import pprint

from coin import Coin


__author__ = "Hung Nguyen"
__copyright__ = "Hung Nguyen"
__license__ = "mit"

_logger = logging.getLogger(__name__)
 
def alt_watcher(altcoin,basecoin='BTC'):
    """Watch an Alcoin to BTC (base coin) or USD

    Args:
 
      altcoin (string): string

    Returns:
      string: Sucess status string and time
    """
    
    altCoin=Coin(altcoin)
    altCoin.get_positions()
    # Get the order book at the default level.
     
    while True  :
       
      altCoin.pull_data()
      altCoin.print_table()
      #print(f'{basecoin}: ${btc[0][0]} {altcoin}->USD: ${usd_alt} {altcoin}-{basecoin}: {btc_alt} {altcoin}->{basecoin}->USD: ${dollar}')
      time.sleep(1)
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
