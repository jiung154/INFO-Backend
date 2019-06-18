import json
import os
import pytest

from app import create_app
from app.extension import db
from config import TestConfig


@pytest.fixture(scope='session')
def app():
    app = create_app(TestConfig)
    test_client = app.test_client()

    yield test_client

    db.drop_all(app=app)
    db.create_all(app=app)

    file = __file__+r'\..\..\..\image\test.jpg'

    if os.path.isfile(file):
        os.remove(file)


@pytest.fixture(scope='session')
def token(app):
    res = app.post(
        '/account/login',
        data=json.dumps({'id': 'test', 'pw': 'test'}),
        content_type='application/json'
    )

    token = json.loads(res.data.decode('utf-8'))
    access_token = token['access_token']

    return access_token
