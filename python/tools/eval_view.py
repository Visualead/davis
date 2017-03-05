#!/usr/bin/env python

# ----------------------------------------------------------------------------
# A Benchmark Dataset and Evaluation Methodology for Video Object Segmentation
#-----------------------------------------------------------------------------
# Copyright (c) 2016 Federico Perazzi
# Licensed under the BSD License [see LICENSE for details]
# Written by Federico Perazzi
# ----------------------------------------------------------------------------

""" Read and display evaluation from HDF5.

EXAMPLE:
	python tools/eval_view.py method.h5

"""


import os
import time
import argparse

import numpy   as np
import os.path as osp

from prettytable import PrettyTable as ptable

# To make it work from within pycharm
# import sys
# sys.path.insert(0, '/Users/eddie/Documents/Projects/Repositories/davis/python/lib')
from davis.dataset import *
from davis import log

def parse_args():
	"""Parse input arguments."""

	parser = argparse.ArgumentParser(
			description='Read and display evaluation from HDF5.')

	parser.add_argument(dest='input',default=None,type=str,
			help='Path to the HDF5 evaluation file to be displayed.')

	parser.add_argument('--eval_set',default='all',type=str,
			choices=['training','test','gygo-test','gygo-training','all'],help='Select set of videos to evaluate.')

	parser.add_argument('--summary',action='store_true',
			help='Print dataset average instead of per-sequence results.')

	parser.add_argument('--output_dir', default='', type=str,
			help='Visualead: Path to the directory where outputs will be written.')


	# Parse command-line arguments
	args       = parser.parse_args()
	args.input = osp.abspath(args.input)

	return args

if __name__ == '__main__':

	args = parse_args()

	technique = osp.splitext(osp.basename(args.input))[0]

	db_eval_dict = db_read_eval(technique,raw_eval=False,
			inputdir=osp.dirname(args.input), eval_set=args.eval_set)

	log.info("Displaying evaluation of: %s"%osp.basename(args.input))

	import os
	if not os.path.exists(args.output_dir):
		os.makedirs(args.output_dir)

	db_eval_view(db_eval_dict, technique,
				 args.summary, args.eval_set,
				 output_path_prefix=os.path.join(args.output_dir,
											   'davis-benchmark'))
