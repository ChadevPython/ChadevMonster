# -*- coding: utf-8 -*-

from flask import jsonify, request
from flask_classy import FlaskView, route

from chadevmonster.models.article import Article

__all__ = "ApiView"


class ArticlesView(FlaskView):

    def get(self):
        """Get all article records."""
        articles = Article.query.all()
        return jsonify([
            {
                'id': article.id,
                'title': article.article_title,
                'url': article.article_url,
            }
            for article in articles
        ])

    def post(self):
        Article(**request.json).save()
        return jsonify('Good Job!')
