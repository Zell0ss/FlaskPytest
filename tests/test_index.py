import json


def test_index(client):
    res = client.get('/')
    assert res.status_code == 200
    expected = {'hello': 'world'}
    assert expected == json.loads(res.get_data(as_text=True))



def test_health(client):
    res = client.get('/health/')
    assert res.status_code == 200
    expected = {"health": "Good, doctor!"}
    assert expected == json.loads(res.get_data(as_text=True))
