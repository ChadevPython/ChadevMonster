# -*- coding: utf-8 -*-

from flask import jsonify
from flask_classy import FlaskView, route
from chadevmonster import csrf, app
from chadevmonster.models.article import Article

__all__ = "ApiView"


class ApiView(FlaskView):
    route_base = "/api"

    @route("/articles", methods=["GET"])
    def articles(self):
        """Get all article records."""

        articles = Article.query.all()
        return jsonify([
            {
                'title': article_title,
                'url':  article.article_url,
            }
            for article in  articles
        ])        
