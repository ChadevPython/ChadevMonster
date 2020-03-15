import unittest

from chadevmonster import app, db
from chadevmonster.models.article import Article


class ApiTests(unittest.TestCase):

    def setUp(self):
        app.config['SQLALECHEMY_DATABASE_URI'] = 'sqlite.//'
        app.testing = True
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_article_get_returns_all_articles(self):
        Article(article_title='Test1', article_url='/url/url').save()
        Article(article_title='Test2', article_url='/url/url').save()
        response = self.client.get('/api/articles')
        self.assertEqual(response.status_code,  200)
        expected = [
            {'title': 'Test1', 'url': '/url/url'},
            {'title': 'Test2', 'url': '/url/url'}
        ]
        self.assertEqual(response.json, expected)
