from flask import Flask
from config import Config
from checkFolder import checkFolder
from apscheduler.schedulers.background import BackgroundScheduler
import logging

app = Flask(__name__)

def printFolderCheck():
	logging.getLogger().setLevel(logging.DEBUG)
	app.logger.info(str(checkFolder("../shared")))

app.config.from_object(Config)
sched = BackgroundScheduler()
sched.add_job(printFolderCheck,"interval",minutes=app.config['TIME_INTERVAL_MINS'])
sched.start()