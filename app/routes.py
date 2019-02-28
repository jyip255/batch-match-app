from app import app
from checkFolder import checkFolder

@app.route('/')
@app.route('/index')
def index():
	return "Hello, World!"

@app.route('/check')
def check():
	return str(checkFolder("../shared"))