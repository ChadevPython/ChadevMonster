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

        articles_dict = []
        for article in articles:
            articles_dict.append({"title": article.article_title, "url": article.article_url})

        return jsonify(articles_dict)
