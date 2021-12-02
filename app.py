from flask import Flask, render_template, redirect, request, url_for
import re

app = Flask(__name__)

def method(string):
    p ='[^!@#$%\^&\*\(\)\<\>\:]*'
    match = re.match(p, string)
    return match

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
	data = request.form.get('search')
	flag = method(data)
	if flag:
		return render_template('search.html', result=data)
		
	else:
		return redirect(url_for('home'))
	
	
if __name__ == '__main__':
	app.run()
