# -*- coding: utf-8 -*-

from arrow import utcnow
from sqlalchemy_utils import ArrowType
from sqlalchemy import Column, Integer
from chadevmonster import db
from chadevmonster.models import ModelMixin


class Article(db.Model, ModelMixin):
    id = Column(Integer, primary_key=True)
    created_on = Column(ArrowType, default=utcnow)
    article_title = Column(db.Unicode, nullable=False)
    article_url = Column(db.Unicode, nullable=False)

    def __init__(self, article_title, article_url):
        self.article_title = article_title
        self.article_url = article_url

    def __repr__(self):
        return self.article_title
