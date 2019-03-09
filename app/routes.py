from app import app
from checkFolder import checkFolder
import os

@app.route('/')
@app.route('/index')
def index():
	return "Hello, World!"

@app.route('/check')
def check():
	return str(checkFolder("../shared/check/","../shared/temp/","../shared/error/","../shared/scanned/"))

@app.route('/status')
def status():
	errorList =[file for file in os.listdir("../shared/error/") if file[0] != "."]
	scannedList = [file for file in os.listdir("../shared/scanned/") if file[0] != "."]
	error = "<br/>".join(errorList)
	scanned = "<br/>".join(scannedList)
	return str(len(scannedList))+" scanned files, "+str(len(errorList))+" files with errors."\
	"<br/><br/>Files in error directory:<br/>"+error+\
	"<br/><br/>Files in scanned directory:<br/>"+scanned