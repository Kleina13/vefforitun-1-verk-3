# APP

from flask import Flask, render_template as rend

app = Flask(__name__)

@app.route('/')
def index():
	return rend('layout.html')

@app.route('/article/<article>')
def info(article):
	return rend('layout.html')


if __name__ == "__main__":
	app.run(debug=True)