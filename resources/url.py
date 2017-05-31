from flask import redirect
from flask_restful import Resource
import validators
import hashlib
from models.url import UrlModel


class Url(Resource):
    def get(self, url_param):
        url = UrlModel.find_by_short_url(url_param)
        if url:
            return redirect(url.long_url)

        # Prepend an 'http://' to url_param if it doesn't exist for url validation
        if 'http' not in url_param:
            url_param = 'http://' + url_param
        # Return an error if not a valid url
        if not validators.url(url_param):
            return {'error': 'You must provide a valid URL'}

        # Hash the long url and create a new url object
        short_url = hashlib.md5(url_param.encode('utf-8')).hexdigest()[:4]

        url = UrlModel(url_param, short_url)
        url.save_to_db()

        return url.json()
