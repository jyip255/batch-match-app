from app import app

@app.route('/')
@app.route('/index')
def index():
	return "Welcome to the admin site for Batch Match! ~More coming soon~"
