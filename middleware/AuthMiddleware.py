import falcon
import jwt

from config import cfg


class AuthMiddleware(object):
    def __init__(self, exclude_routes=[]):
        self.exclude_routes = exclude_routes

    def process_request(self, req, resp):
        for route in self.exclude_routes:
            if route in req.path:
                return

        token = req.get_header('Authorization')

        challenges = ['Token type="Bearer"']

        if token is None:
            description = ('Please provide an auth token '
                           'as part of the request.')
            raise falcon.HTTPUnauthorized('Auth token required',
                                          description,
                                          challenges,
                                          href='https://auth0.com/docs/jwt')
        token = token.split(' ')[1]

        if not self._is_token_valid(token):
            description = ('The provided auth token is not valid. '
                           'Please request a new token and try again.')
            raise falcon.HTTPUnauthorized('Authentication required',
                                          description,
                                          challenges,
                                          href='https://auth0.com/docs/jwt')

    def _is_token_valid(self, token):
        try:
            jwt.decode(bytes(token, encoding='UTF-8'), cfg('app', 'secret'), algorithm='HS256', verify=True)
        except (jwt.InvalidTokenError, jwt.DecodeError) as e:
            print(">>> TOKEN ERROR", e)
            return False
        return True
