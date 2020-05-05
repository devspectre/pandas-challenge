import csv
import os
import sys
import pandas as pd
import numpy as np

files = []
data = []
path = ''

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

def merge_all(dir_path):
	"""merge all csv files in the dir_path into a single csv file
	Args:
		dir_path(str): absolute path to the source directory
	Returns:
		output_file_name(str), list of rows
	"""

	# get list of all csv files in the directory
	list_of_csv(dir_path)

	print(f'There are {len(files)} csv files in total!')

	print(f'Reading csv files({len(files)}) ...')

	for index, file in enumerate(files):
		df = pd.read_csv(file)
		df = df.replace(np.nan, '', regex=True)
		data.append(df)
		# print(df)
		pbar.update(index + 1)

	df_data = pd.concat(data)
	df_data['ts'] = pd.to_datetime(df_data['ts'])
	df_data.sort_values(by='ts', inplace=True)

	# get first & last reading date
	start_date = df_data.iloc[0]['ts']
	end_date = df_data.iloc[len(df_data.index) - 1]['ts']
	timeline = pd.date_range(start_date, end_date, freq='15T')

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