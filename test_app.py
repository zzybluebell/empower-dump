import pytest
import requests

session = requests.session()

@pytest.fixture(scope='class')
def login():
    res = session.post('http://127.0.0.1:5000/login',  data = {
        'username': 'phangjiekie', 
        'password': 'pumpkin'
    })
    return res.status_code == 200
    

def test_login_fail():
    res = requests.post('http://127.0.0.1:5000/login', data ={
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

def test_summary_logout():
    res = requests.post('http://127.0.0.1:5000/summary')
    assert res.json() == 'logout'
    assert res.status_code == 300

def test_summary_no_date(login):
    res = session.post('http://127.0.0.1:5000/summary')
    assert res.json() == 'Missing date parameter'
    assert res.status_code == 300

def test_summary_invalid_date(login):
    res = session.post('http://127.0.0.1:5000/summary?date=2001-35-35')
    assert res.json() == 'invalid date format, please enter date format as YY-MM-D'
    assert res.status_code == 300

def test_summary_invalid_date(login):
    res = session.post('http://127.0.0.1:5000/summary?date=2001-35-35')
    assert res.json() == 'invalid date format, please enter date format as YY-MM-D'
    assert res.status_code == 300

def test_summary_no_result(login):
    res = session.post('http://127.0.0.1:5000/summary?date=2025-01-01')
    assert res.json() == ''
    assert res.status_code == 200

def test_summary_one_result(login):
    response = session.post('http://127.0.0.1:5000/summary?date=2018-05-15')
    assert response.json() == {
        'active_minutes': 27, 
        'calories': 2050, 
        'distance': 6.93, 
        'steps': 10011
    }
    assert response.status_code == 200

