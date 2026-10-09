from django.contrib.auth.models import User
from django.core.management import call_command
from rest_framework.test import APITestCase

from .models import BlogPost, Category


class JournalApiTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        call_command('seed_within', verbosity=0)
        cls.user = User.objects.create_user('reader', 'r@example.com', 'a-good-pass-123')
        cls.other = User.objects.create_user('other', 'o@example.com', 'a-good-pass-123')
        cls.slug = BlogPost.objects.first().slug

    def login(self, name='reader'):
        r = self.client.post('/api/token/', {'username': name, 'password': 'a-good-pass-123'})
        self.assertEqual(r.status_code, 200)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + r.data['access'])

    def test_seed_counts(self):
        self.assertEqual(Category.objects.count(), 6)
        self.assertGreaterEqual(BlogPost.objects.filter(status='published').count(), 24)

    def test_list_paginates_and_filters(self):
        r = self.client.get('/api/posts/')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.data['results']), 9)
        self.assertIsNotNone(r.data['next'])
        r = self.client.get('/api/posts/?category=rest')
        self.assertTrue(all(p['category']['slug'] == 'rest' for p in r.data['results']))
        self.assertEqual(self.client.get('/api/posts/?page=99').status_code, 404)

    def test_search(self):
        r = self.client.get('/api/posts/?q=walk')
        self.assertGreater(r.data['count'], 0)
        r = self.client.get('/api/posts/?q=zzzzqqq')
        self.assertEqual(r.data['count'], 0)

    def test_detail_related_and_404(self):
        self.assertEqual(self.client.get(f'/api/posts/{self.slug}/').status_code, 200)
        rel = self.client.get(f'/api/posts/{self.slug}/related/')
        self.assertEqual(len(rel.data), 3)
        self.assertEqual(self.client.get('/api/posts/nope/').status_code, 404)

    def test_create_requires_auth_then_validates(self):
        payload = {'title': 'A new story', 'content': 'Body text here.', 'category': Category.objects.first().id, 'status': 'published'}
        self.assertEqual(self.client.post('/api/posts/', payload).status_code, 401)
        self.login()
        self.assertEqual(self.client.post('/api/posts/', {'title': ''}).status_code, 400)
        r = self.client.post('/api/posts/', payload)
        self.assertEqual(r.status_code, 201)
        slug = r.data['slug']
        self.assertEqual(self.client.patch(f'/api/posts/{slug}/', {'excerpt': 'Edited'}).status_code, 200)
        self.login('other')
        self.assertEqual(self.client.delete(f'/api/posts/{slug}/').status_code, 403)
        self.login()
        self.assertEqual(self.client.delete(f'/api/posts/{slug}/').status_code, 204)

    def test_likes(self):
        self.assertEqual(self.client.post(f'/api/posts/{self.slug}/like/').status_code, 401)
        self.login()
        self.assertEqual(self.client.post(f'/api/posts/{self.slug}/like/').status_code, 201)
        self.assertEqual(self.client.post(f'/api/posts/{self.slug}/like/').status_code, 200)
        self.assertEqual(self.client.delete(f'/api/posts/{self.slug}/like/').status_code, 204)

    def test_comments(self):
        url = f'/api/posts/{self.slug}/comments/'
        self.assertEqual(self.client.post(url, {'content': 'Hello there'}).status_code, 401)
        self.login()
        self.assertEqual(self.client.post(url, {'content': 'x'}).status_code, 400)
        r = self.client.post(url, {'content': 'A thoughtful note.'})
        self.assertEqual(r.status_code, 201)
        cid = r.data['id']
        self.login('other')
        self.assertEqual(self.client.delete(f'/api/comments/{cid}/').status_code, 403)
        self.login()
        self.assertEqual(self.client.delete(f'/api/comments/{cid}/').status_code, 204)

    def test_contact(self):
        good = {'name': 'Sam', 'email': 'sam@example.com', 'topic': 'Therapy', 'message': 'I would like to ask a question.'}
        self.assertEqual(self.client.post('/api/contact/', good).status_code, 201)
        self.assertEqual(self.client.post('/api/contact/', {**good, 'email': 'bad'}).status_code, 400)

    def test_register_and_me(self):
        r = self.client.post('/api/auth/register/', {'username': 'newbie', 'email': 'n@example.com', 'password': 'a-good-pass-123'})
        self.assertEqual(r.status_code, 201)
        self.assertEqual(self.client.post('/api/auth/register/', {'username': 'newbie', 'email': 'n@example.com', 'password': 'a-good-pass-123'}).status_code, 400)
        self.assertEqual(self.client.get('/api/auth/me/').status_code, 401)
        self.assertEqual(self.client.post('/api/token/', {'username': 'reader', 'password': 'wrong'}).status_code, 401)

    def test_legacy_endpoints_still_work(self):
        self.assertEqual(self.client.get('/api/categories/').status_code, 200)
        self.assertEqual(self.client.get('/api/all-posts/').status_code, 200)
        self.assertEqual(self.client.get('/api/categories/search/?name=Mind').status_code, 200)
