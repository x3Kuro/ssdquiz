from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
	p = 
	
if __name__ == '__main__':
	app.run()
