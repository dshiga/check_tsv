#!/usr/bin/env python

import argparse
import sys

color_codes = {True: 34, False: 31}

def run(input_file):
  i = 0

  with open(input_file) as f:
    line = f.readline()
    parts = line.split('\t')
    num_fields = len(parts) - 1
    print_with_color(parts, i, True)
    num_fields_0 = num_fields
    i += 1

    for line in f:
      parts = line.split('\t')
      num_fields = len(parts) - 1
      valid = num_fields == num_fields_0
      print_with_color(parts, i, valid)
      i += 1

  if valid:
    print('\nSuccess! All rows contain {0} tabs\n'.format(num_fields))
  if not valid:
    print('\nError! Rows do not contain the same number of tabs\n')
    sys.exit(1)

def print_with_color(parts, row_num, valid):
  print('{0}: '.format(row_num + 1) + '\033[{0}m[tab]\033[0m'.format(color_codes[valid]).join(parts).replace('\n', ''))

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('input_file')
  args = parser.parse_args()
  run(args.input_file)

