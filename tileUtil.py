#!/usr/local/bin/python3
#coding: utf-8

import argparse
import os
import tilemap.image2Map
import tilemap.tilesetSplit
import tilemap.mapWriter

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='sub-command help')

########################################
# list to map
########################################

list2map_parser = subparsers.add_parser('list2map', help=tilemap.image2Map.__doc__)
tilemap.image2Map.add_arguments_to_parser(list2map_parser)

########################################
# tileset split
########################################

tileset_split_parser = subparsers.add_parser('tileset_split', help=tilemap.tilesetSplit.__doc__)
tilemap.tilesetSplit.add_arguments_to_parser(tileset_split_parser,True)

########################################
# map writer
########################################

map_writer_parser = subparsers.add_parser('map_writer', help=tilemap.mapWriter.__doc__)
tilemap.mapWriter.add_arguments_to_parser(map_writer_parser, True)

args = parser.parse_args()
args.func(args)