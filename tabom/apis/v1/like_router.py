from typing import Tuple

from django.http import HttpRequest
from ninja import Router

from tabom.models import Like
from tabom.schema.like_request import LikeRequest
from tabom.schema.like_response import LikeResponse
from tabom.services.like_service import do_like, undo_like

router = Router()


@router.post("/", response={201: LikeResponse})
def post_like(request: HttpRequest, like_request: LikeRequest) -> tuple[int, LikeResponse]:
    like = do_like(like_request.user_id, like_request.article_id)
    return 201, LikeResponse(id=like.id, user_id=like.user_id, article_id=like.article_id)


@router.delete("/", response={204: None})
def delete_like(request: HttpRequest, user_id: int, article_id: int) -> tuple[int, None]:
    undo_like(user_id, article_id)
    return 204, None
