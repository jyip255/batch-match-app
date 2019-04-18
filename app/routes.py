from app import app
from checkFolder import checkFolder
import os
from flask import url_for

@app.route('/')
@app.route('/index')
def index():
	return "Welcome to the batch match app!<p><a href='/status'>Check the status</a></p><p><a href='/check'>Are there files to scan?</a></p>"

@app.route('/check')
def check():
	return str(checkFolder("../shared/check/","../shared/temp/","../shared/error/","../shared/scanned/","../shared/nomatch"))

@app.route('/status')
def status():
	errorList =[file for file in os.listdir("../shared/error/") if file[0] != "."]
	scannedList = [file for file in os.listdir("../shared/scanned/") if file[0] != "."]
	noMatchList = [file for file in os.listdir("../shared/nomatch/") if file[0] != "."]
	error = "<br/>".join(errorList)
	scanned = "<br/>".join(scannedList)
	nomatch = "<br/>".join(noMatchList)
	return str(len(scannedList))+" successfully attached files, "\
	+str(len(errorList))+" files that could not be scanned, "\
	+str(len(noMatchList))+" files that could not be matched."+\
	"<br/><br/>Files in scanned directory:<br/>"+scanned+\
	"<br/><br/>Files in error directory:<br/>"+error+\
	"<br/><br/>Files in nomatch directory:<br/>"+nomatch
