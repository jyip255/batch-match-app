import os

def checkFolder(directory):
	hasFiles = len([file for file in os.listdir(directory) if file[0] != "."]) > 0
	return hasFiles