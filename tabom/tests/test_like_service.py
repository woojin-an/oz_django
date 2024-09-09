from django.db import IntegrityError
from django.test import TestCase

from tabom.models import Article, User
from tabom.services.like_service import do_like


class TestLikeService(TestCase):
    def test_a_user_can_like_an_article(self) -> None:
        # Given -> 무슨 상황에서? 테스트 대상
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # When -> 테스트 상황, 함수
        like = do_like(user.id, article.id)

        # Then -> 테스트 결과 검증
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        self.assertEqual(article.id, like.article_id)

    def test_a_user_can_like_an_article_only_once(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # Expect (when then을 나누기 애매할 때)
        do_like(user.id, article.id)
        with self.assertRaises(IntegrityError):
            do_like(user.id, article.id)
