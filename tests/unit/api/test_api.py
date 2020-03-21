import unittest

from chadevmonster import create_app, db
from chadevmonster.models.article import Article


class ApiTests(unittest.TestCase):

    def setUp(self):
        app = create_app(testing=True)
        app.app_context().push()
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_request_for_articles_returns_all_articles(self):
        Article(article_title='Test1', article_url='/url/url').save()
        Article(article_title='Test2', article_url='/url/url').save()
        response = self.client.get('/api/articles/')
        self.assertEqual(response.status_code,  200)
        expected = [
            {'title': 'Test1', 'url': '/url/url', 'id': 1},
            {'title': 'Test2', 'url': '/url/url', 'id': 2}
        ]
        self.assertEqual(response.json, expected)

    def test_posting_article_creates_articles(self):
        title = 'new article'
        url = '/my/cool/url'
        data = {
            'article_title': title,
            'article_url': url
        }
        response = self.client.post('/api/articles/', json=data)
        self.assertEqual(response.status_code,  200)
        articles = Article.query.all()
        self.assertEqual(len(articles), 1)
        self.assertEqual(articles[0].article_title, title)
        self.assertEqual(articles[0].article_url, url)
