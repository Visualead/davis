#!/usr/bin/env python

# ----------------------------------------------------------------------------
# A Benchmark Dataset and Evaluation Methodology for Video Object Segmentation
# -----------------------------------------------------------------------------
# Copyright (c) 2016 Federico Perazzi
# Licensed under the BSD License [see LICENSE for details]
# Written by Federico Perazzi
# ----------------------------------------------------------------------------

"""
Evaluate a technique and store results in HDF5 file.

EXAMPLE:
	python tools/eval.py ../data/Results/Segmentations/480p/fcp ./

"""

import os
import time
import argparse
import sys

import numpy   as np
import os.path as osp

from prettytable import PrettyTable

# To make it work from within pycharm
# sys.path.insert(0,'/Users/eddie/Documents/Projects/Repositories/davis/python/lib')
from davis.dataset import db_eval, db_save_eval
from davis import cfg, log


def parse_args():
    """Parse input arguments."""

    parser = argparse.ArgumentParser(
        description="""Evaluate a technique and store results.
			""")

    parser.add_argument(
        dest='input', default=None, type=str,
        help='Path to the technique to be evaluated')

    parser.add_argument(
        dest='output', default=None, type=str,
        help='Output folder')

    parser.add_argument(
        '--metrics', default=None, nargs='+', type=str, choices=['J', 'F', 'T'])

    args = parser.parse_args()

    return args


def find_sequences(input_dir):
    """
    Find relevant sequence folders

    """
    lowest_dirs = []
    for root, dirs, files in os.walk(input_dir):
        if not dirs:
            lowest_dirs.append(root[len(input_dir) + 1:])

    return lowest_dirs


if __name__ == '__main__':
    args = parse_args()
    args.input = osp.abspath(args.input)
    sequences = find_sequences(os.path.abspath(args.input))

    db_eval_dict = db_eval(osp.basename(args.input),
                           sequences, osp.dirname(args.input),
                           args.metrics)

    log.info("Saving results in: %s" % osp.join(
        args.output, osp.basename(args.input)) + ".h5")

    db_save_eval(db_eval_dict, outputdir=args.output)
