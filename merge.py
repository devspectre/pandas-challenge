import csv
import os
import sys
import pandas as pd
import numpy as np

def list_of_directories(dir_path):
	"""get list of sub folders inside directory
	Args:
		dir_path(str): absolute path to the source directoryc
	Returns:
		list: a list of absolute paths of sub folders(top level only)
	"""

	return [os.path.join(dir_path, name) for name in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, name))]

def list_of_csv(dir_path):
	"""get list of all csv files in given path

	Args:
		dir_path(str): absolute path to the source directory
	Returns:
	"""

	files.clear()
	data.clear()

	try:
		for name in os.listdir(dir_path):
			if '.csv' in name:
				files.append(os.path.join(dir_path, name))
	except OSError:
		raise SystemExit(f'Path does not exist or you need to wrap the path inside quotes.')

if __name__ == '__main__':

	try:
		dir_path = sys.argv[1]
	except IndexError:
		raise SystemExit(f"Usage: {sys.argv[0]} <source_directory>")

	dir_path = dir_path.rstrip('\\')
	directories = list_of_directories(dir_path)

	if len(directories) == 0: # single folder
		merge_all(dir_path)
	else: # batch operation, multiple directories in it
		for index, directory in enumerate(directories):
			if index != 0:
				print()
				print()
			directory_name = os.path.basename(os.path.normpath(directory))
			print(f'Started processing on folder {index + 1} {directory_name}')
			merge_all(directory)
			print(f'Completed processing on folder {index + 1}')