import os
import shutil
import argparse

def Argument_parser():
	# parsing arguments the command line
	parser = argparse.ArgumentParser()
	parser.add_argument('path', nargs='+')
	return parser

def get_key(d, value):
	# function to get name folder by permit the file
	for k, v in d.items():
		if value in v:
			return k 
		else:
			continue

def move(file,name_folder):
	# function which move files to their folder
    try:
        os.mkdir(name_folder)
        shutil.move(file, name_folder)
    except OSError:
        shutil.move(file, name_folder)


files = {
	'text files': ['.txt', '.doc', '.docm', '.docx', '.dot', '.dotm', '.dotx'],
    'html files': ['.html','htm','.mht','.mhtml'],
	'css files': ['.css'],
    'pdf files': ['.pdf'],
    'table files': ['.csv', '.xml', '.xla', '.xlam', '.xls', '.xlsb', '.xlsm', '.xlsx'],
    'python files': ['.py'],
    'picture files': ['.jpg', '.jpeg', '.tif', '.tiff', '.png', '.gif', '.bmp', '.dib'],
    'archive files': ['.zip', '.rar', '.arj', '.cab', '.tar', '.lzh'],
    'presentation files': ['.pptx'],
    'setup files': ['.exe'],
	'torrent files': ['.torrent'],
	'mark down files': ['.md']
}
parser = Argument_parser()
args = parser.parse_args()

d = args.path[1:]
path = args.path[0]
for x in d:
	path +=  f' {x}'

os.chdir(path)
for file in os.listdir(path=path):
	permit = file.index('.')
	s = []
	for z in files.values():
		s.extend(z)
	if file[permit:] in s:
		move(file, get_key(files, file[permit:]))
	else:
		continue