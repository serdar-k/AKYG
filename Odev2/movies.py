from flask import Flask, render_template, request, redirect, url_for
from flask_restful import Api, Resource, reqparse
import requests

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		input = request.form.get('title')
		return redirect(url_for("movie", title=input))		
	else:
		return render_template('home.html')

@app.route('/<title>')
def movie(title):
	url = f"http://www.omdbapi.com/?t={title}&apikey=1e387f75"
	response = requests.get(url).json()
	# return response.json()
	title = response["Title"]
	year = response["Year"]
	genre = response["Genre"]
	plot = response["Plot"]
	poster = response["Poster"]

	return render_template('movie.html', title=title, year=year, genre=genre, plot=plot, poster=poster)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=6767)
	app.run()