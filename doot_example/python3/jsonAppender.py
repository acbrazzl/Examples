#! /usr/bin/python3

# A json creater/appender with CLI.  Currently supports one key-value pair per call.  This is reference example code.

import argparse
import json
from pathlib import Path

file_name = "text.json"

def main(args):
    print("Running...")
    #create file if none exist (different than w+)
    f = Path(file_name)
    f.touch(exist_ok=True)
    #load
    infile =  open(file_name,"r+")
    data = {}
    try:
        data = json.load(infile)
    except:
        print("Creating JSON from scratch")
    infile.close()
    print("Read " + file_name +  " as" + str(data))
    #add
    data[args.key] = args.value
    print("Dict is now: " + str(data))

    #save
    with open(file_name,"w+") as outfile:
        json.dump(data, outfile)

    outfile.close()


if __name__ == "__main__":
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('-k','--key',type=str,help="Key to ingest")
    my_parser.add_argument('-v','--value',type=str,help="Value to ingest")
    args = my_parser.parse_args()
    main(args)
