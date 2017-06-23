import os
import subprocess
import sys
import glob
import re


def change_and_create_dir(output_directory):
	os.chdir(os.path.abspath(os.path.dirname(__file__)))
	try:
		os.makedirs(output_directory)
	except OSError:
		pass

def get_file_list(input_derectory):
	files = glob.glob(os.path.join(input_derectory, "*.jpg"))
	return files

def converter_program():
	input_derectory = 'Source'
	output_directory = 'Result'
	change_and_create_dir(output_directory)
	#list_of_files =  os.listdir('Source')
	for file in get_file_list(input_derectory):
		args_for_convert =  'convert ' + file + ' -resize 200 ' + re.sub(input_derectory, output_directory, file)
		process = subprocess.run(args_for_convert)
	print('Done!')

converter_program()


