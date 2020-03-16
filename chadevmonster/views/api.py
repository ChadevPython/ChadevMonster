# -*- coding: utf-8 -*-

from flask import jsonify, request
from flask_classy import FlaskView, route

from chadevmonster.models.article import Article

__all__ = "ApiView"


class ApiView(FlaskView):
    route_base = "/api"

    @route("/articles", methods=["GET", "POST"])
    def articles(self):
        """Get all article records."""

        if request.method == 'GET':
            articles = Article.query.all()
            return jsonify([
                {
                    'id': article.id,
                    'title': article.article_title,
                    'url': article.article_url,
                }
                for article in articles
            ])
        if request.method == 'POST':
            Article(**request.json).save()
            return jsonify('Good Job!')
