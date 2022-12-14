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
    res = session.post('http://127.0.0.1:5000/summary?date=2018-05-15')
    assert res.json() == {
        'active_minutes': 27, 
        'calories': 2050, 
        'distance': 6.93, 
        'steps': 10011
    }
    assert res.status_code == 200

def test_rank():
    res = session.post('http://127.0.0.1:5000/rank')
    assert res.json() == ['phangjiekie', 'epg002', 'etp014', 'etp022', 'jimmya', 'epg005', 'etp001', 'epg010', 'etp013', 'etp002', 'epg011', 'etp018', 'etp021', 'etp009', 'etp008', 'epg006', 'etp007', 'epg009', 'etp010ah', 'epg001', 'epg019', 'epg015', 'etp011', 'ebd003', 'etp016', 'etp026', 'epg022', 'etp024', 'epg003', 'epg012', 'ebd006', 'max', 'etp025', 'epg023', 'etp003', 'epg021', 'epg007', 'ebd009', 'epg004', 'etp034', 'epg016', 'ebd010', 'epg017', 'etp019', 'etp033', 'etp030', 'etp015', 'epg018', 'etp032', 'ebd001', 'epg024', 'epg013', 'etp027', 'epg025', 'epg008', 'ebd007', 'etp017', 'etp006', 'ebd008', 'etp012', 'epg029', 'ebd004', 'epg014', 'ebd013', 'etp031', 'ebd012', 'epg020', 'etp020', 'ebd014', 'etp028', 'epg027', 'epg026', 'etp023', 'epg028', 'etp029', 'abc', 'ebd011', 'ebd002', 'etp004']
    assert res.status_code == 200

def test_rank_wrong_return():
    res = session.post('http://127.0.0.1:5000/rank')
    assert res.json() != ['epg002', 'phangjiekie', 'etp014', 'etp022', 'jimmya', 'epg005', 'etp001', 'epg010', 'etp013', 'etp002', 'epg011', 'etp018', 'etp021', 'etp009', 'etp008', 'epg006', 'etp007', 'epg009', 'etp010ah', 'epg001', 'epg019', 'epg015', 'etp011', 'ebd003', 'etp016', 'etp026', 'epg022', 'etp024', 'epg003', 'epg012', 'ebd006', 'max', 'etp025', 'epg023', 'etp003', 'epg021', 'epg007', 'ebd009', 'epg004', 'etp034', 'epg016', 'ebd010', 'epg017', 'etp019', 'etp033', 'etp030', 'etp015', 'epg018', 'etp032', 'ebd001', 'epg024', 'epg013', 'etp027', 'epg025', 'epg008', 'ebd007', 'etp017', 'etp006', 'ebd008', 'etp012', 'epg029', 'ebd004', 'epg014', 'ebd013', 'etp031', 'ebd012', 'epg020', 'etp020', 'ebd014', 'etp028', 'epg027', 'epg026', 'etp023', 'epg028', 'etp029', 'abc', 'ebd011', 'ebd002', 'etp004']
    assert res.status_code == 200