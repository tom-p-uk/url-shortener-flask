# URL Shortener

A URL shortening microservice built using Python. I originally made this with Node, Express and MongoDB as part of Free Code Camp's backend challenges, but rebuilt it to get some more practice with Python. The original repo can be found [here](https://github.com/tom-p-uk/url-shortener-microservice).

### User Stories:

1. I can pass a URL as a parameter and I will receive a shortened URL in the JSON response.
2. If I pass an invalid URL that doesn't follow the valid http://www.example.com format, the JSON response will contain an error instead.
3. When I visit that shortened URL, it will redirect me to my original link.

### Technology Used:

* Python 3.6
* Flask
* Flask-RESTful
* Flask SQLAlchemy

### Heroku Demo:

Make GET requests to https://tom-p-uk-url-shortener-flask.herokuapp.com/api/<url> to receive a JSON response.
