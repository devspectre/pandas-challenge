import csv
import os
import sys
import pandas as pd
import numpy as np

def list_of_directories(dir_path):
	"""get list of sub folders inside directory
	Args:
		dir_path(str): absolute path to the source directory
	Returns:
		list: a list of absolute paths of sub folders(top level only)
	"""

	return [os.path.join(dir_path, name) for name in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, name))]

if __name__ == '__main__':

	try:
		dir_path = sys.argv[1]
	except IndexError:
		raise SystemExit(f"Usage: {sys.argv[0]} <source_directory>")