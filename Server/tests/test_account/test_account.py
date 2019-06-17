import json


def test_user_register(app):
    new_user = {
        'id': 'test',
        'pw': 'test',
        'name': 'test'
    }

    res = app.post(
        '/account/register',
        data=json.dumps(new_user),
        content_type='application/json'
    )

    assert res.status_code == 201


def test_user_login(app):
    user = {
        'id': 'test',
        'pw': 'test'
    }

    res = app.post(
        '/account/login',
        data=json.dumps(user),
        content_type='application/json'
    )

    assert res.status_code == 200

    token = json.loads(res.data.decode('utf-8'))

    assert token['access_token']
    assert token['refresh_token']
