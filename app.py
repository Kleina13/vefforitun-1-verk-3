# APP

from flask import Flask, render_template as rend

app = Flask(__name__)

articles = [{'id': 1, 'author': 'Guðrún', 'title': 'epic', 'content': 'LOREM IPSUM'},
			{'id': 2, 'author': 'Arnór', 'title': 'car', 'content': 'LOREM IPSUM'},
			{'id': 3, 'author': 'Erik', 'title': 'battle', 'content': 'LOREM IPSUM'}]
author = ''
title = ''
content = ''

@app.route('/')
def index():
	return rend('layout.html')

@app.route('/article/<ID>')
def article(ID):
	for x in range(len(articles)):
		if int(ID) == articles[x]['id']:
			author = articles[x]['author']
			title = articles[x]['title']
			content = articles[x]['content']
	return rend('layout.html', author=author, title=title, content=content)


if __name__ == "__main__":
	app.run(debug=True)