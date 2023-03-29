from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username="basheer", password="11110000")
        test_user.save()

        test_post = Post.objects.create(
            title="a coffee cup",
            author=test_user,
            body="How to prepare a cup of coffee..............",
        )
        test_post.save()

    def test_blog(self):
        post = Post.objects.get(id=1)
        author = str(post.author)
        title = str(post.title)
        body = str(post.body)
        self.assertEqual(author, "basheer")
        self.assertEqual(title, "a coffee cup")
        self.assertEqual(body, "How to prepare a cup of coffee..............")
