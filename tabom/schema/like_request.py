from ninja import Schema


class LikeRequest(Schema):
    user_id: int
    article_id: int
