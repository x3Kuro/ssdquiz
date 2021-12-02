from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
	data = request.form('search')
	p = '[^!@#$%^&\*\(\)\'\"\:]*'
	if re.match(p, data):
		return render_template('result.html', result=data)
		
	else:
		return redirect(url_for('home'))
	
	
if __name__ == '__main__':
	app.run()
