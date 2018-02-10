from ..database import db_session
from ..models.lyric import *


def lyric(lyric_id):
    return Lyric.query.get(lyric_id)


def lyrics():
    return db_session.query(Lyric).filter_by(deleted=False).order_by(Lyric.datetime.asc()).all()
