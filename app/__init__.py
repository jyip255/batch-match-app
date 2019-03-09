from flask import Flask
from config import Config
from checkFolder import checkFolder
from apscheduler.schedulers.background import BackgroundScheduler
import logging

app = Flask(__name__)
from app import routes

def printFolderCheck():
	logging.getLogger().setLevel(logging.DEBUG)
	app.logger.info(str(checkFolder("../shared/check/","../shared/temp/","../shared/error/","../shared/scanned/")))

app.config.from_object(Config)
sched = BackgroundScheduler()
sched.add_job(printFolderCheck,"interval",minutes=app.config['TIME_INTERVAL_MINS'])
sched.start()