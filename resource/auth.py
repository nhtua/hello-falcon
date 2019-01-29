import falcon
import bcrypt
import jwt
from datetime import datetime, timedelta
from model import User
from resource import BaseResource
from form.login import LoginSchema
from hook import validator
from config import cfg


class Auth(BaseResource):

    @falcon.before(validator, LoginSchema(strict=True))
    def on_post(self, req, resp):
        username = req.get_json('username')
        password = req.get_json('password')
        dbsession = self.db.session
        user = dbsession.query(User).filter(User.username == username).first()
        if user is None or not bcrypt.checkpw(
                bytes(password, encoding='UTF-8'),
                bytes(user.password, encoding='UTF-8')
        ):
            raise falcon.HTTPUnauthorized(title='Unauthorized', description='Authentication failed!!!')
        token = jwt.encode(dict(
            user_id=user.id,
            exp=datetime.utcnow() + timedelta(seconds=cfg('app', 'expired_after'))
        ), cfg('app', 'secret'), algorithm='HS256')

        resp.json = dict(
            id=user.id,
            username=user.username,
            token=token.decode('UTF-8')
        )
