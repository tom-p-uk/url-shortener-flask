from db import db


class UrlModel(db.Model):
    __tablename__ = 'shortened_urls'

    id = db.Column(db.Integer, primary_key=True)
    short_url = db.Column(db.String(80))
    long_url = db.Column(db.String(80))

    def __init__(self, long_url, short_url):
        self.long_url = long_url
        self.short_url = short_url

    def json(self):
        return {'long_url': self.long_url, 'short_url': 'https://url-shortener-flask.herokuapp.com/api/' + self.short_url}

    @classmethod
    def find_by_short_url(cls, short_url):
        return cls.query.filter_by(short_url=short_url).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
