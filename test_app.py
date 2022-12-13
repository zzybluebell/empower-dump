import pytest
import requests

session = requests.session()

@pytest.fixture(scope='class')
def login():
    res = session.post(' http://localhost:5000',data={
        'username' : 'phangjiekie',
        'password' : 'pumpkin'
    })
    return res.status_code == 200

def test_login_fail():
    res = requests.post('http://localhost:5000/login', data ={
        'username': 'phangjiekie',
        'password': 'xxx'
    })
    assert res.json() == 'fail'
    assert res.status_code == 300
    res = requests.post('http://127.0.0.1:5000/login', data ={
        'username': 'xxx',
        'password': 'pumpkin'
    })
    assert res.json() == 'fail'
    assert res.status_code == 300

def test_login_successful():
    res = requests.post('http://127.0.0.1:5000/login', data ={
        'username': 'phangjiekie',
        'password': 'pumpkin'
    })
    assert res.json() == 'successful'
    assert res.status_code == 200