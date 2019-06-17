import json


def test_write_post(app, token):
    new_post = {
        'title': 'test_title',
        'content': 'test_content',
        'category': 'test_category'
    }

    res = app.post(
        '/post/write',
        data=json.dumps(new_post),
        content_type='application/json',
        headers={
            'Authorization': f"Bearer {token}"
        }
    )

    assert res.status_code == 201


def test_read_category_post(app, token):
    res = app.get(
        '/post/test_category',
        content_type='application/json',
        headers={
            'Authorization': f"Bearer {token}"
        }
    )

    assert res.status_code == 200


def test_read_one_category_post(app, token):
    res = app.get(
        '/post/test_category/1',
        content_type='application/json',
        headers={
            'Authorization': f"Bearer {token}"
        }
    )

    assert res.status_code == 200

    data = json.loads(res.data.decode('utf-8'))

    assert data[0]['title'] == 'test_title'
    assert data[0]['content'] == 'test_content'


def test_modified_one_category_post(app, token):
    post = {
        'title': 'Modified title',
        'content': 'Modified content',
        'category': 'test_category'
    }

    res = app.put(
        '/post/test_category/1',
        data=json.dumps(post),
        content_type='application/json',
        headers={
            'Authorization': f"Bearer {token}"
        }
    )

    assert res.status_code == 201

    res = app.get(
        '/post/test_category/1',
        headers={
            'Authorization': f"Bearer {token}"
        }
    )

    data = json.loads(res.data.decode('utf-8'))

    assert data[0]['title'] == post['title']
    assert data[0]['content'] == post['content']


def test_delete_one_category_post(app, token):
    res = app.delete(
        '/post/test_category/1',
        headers={
            'Authorization': f"Bearer {token}"
        }
    )

    assert res.status_code == 201

    res = app.get(
        '/post/test_category/1',
        headers={
            'Authorization': f"Bearer {token}"
        }
    )

    assert res.status_code == 406
