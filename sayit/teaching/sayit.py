#!/usr/local/bin/python3
import argparse
import logging
import sys

logger = logging.getLogger(__name__)

cow_top = '''  ___________'''
cow_bottom = '''  =========== /
                \ /
                 \ /
                   ^__^
                   (oo)\_______
                   (__)\       )\/\
                       ||----w |
                       ||     ||'''

def main(args):
    '''sayit.py explores creating a python cli app with argparse and unittest'''
    init_logs(args)
    logger.info('Starting Sayit...')
    logger.debug(f'Initialized with args:{args}')

    #TODO: (1) add arg to print n-number of times
    say(args.blurb)
    
    #TODO: (2) implement some unit tests!
    
    #TODO: (3) implement sayCow with arg

def say(blurb):
    if blurb is None: sys.exit(1)
    print(blurb)

def get_parser():
    '''Populate parser with args'''
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description="sayit says the darndest things!")
    parser.add_argument('-b', '--blurb', type=str, help='What to say?')
    parser.add_argument('-c', '--cowsay', type=str, help='What to say?') #TODO: implement
    parser.add_argument('-C', '--Cap', default=False, action='store_true', help='Caps?')
    parser.add_argument('-l', '--log_level', default='INFO', type=str, help='log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL')
    #TODO: Add number of times arg here
    return parser

def init_logs(args):
    logging.basicConfig(level=args.log_level)
    
if __name__ == '__main__':
    main(args=get_parser().parse_args())
