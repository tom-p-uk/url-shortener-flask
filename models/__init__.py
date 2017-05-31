from db import db


class UrlModel(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(50))
    short_url = db.Column(db.String(50))

    def __init__(self, long_url, short_url):
        self.long_url = long_url
        self.short_url = short_url

    def save_to_db(self):
        db.session.add(self)
        db.session.commit(self)

    @classmethod
    def find_by_long_url(cls, long_url):
        return cls.query.filter_by(long_url=long_url).first()

    @classmethod
    def find_by_short_url(cls, short_url):
        return cls.query.filter_by(short_url=short_url).first()
