import usrcheck
import hashlib
def test_auth():
    usrcheck.save_users([['testusr',hashlib.sha256('testPSWD'.encode()).hexdigest()]],True)
    assert usrcheck.load_users() == [['testusr',hashlib.sha256('testPSWD'.encode()).hexdigest()]], "Userlist loading failed"
    assert usrcheck.usr_check('testusr', 'testPSWD',[['testusr',hashlib.sha256('testPSWD'.encode()).hexdigest()]]) == (True,True), "User check failed"
    #Wrong username
    assert usrcheck.usr_check('wrongusr', 'testPSWD',[['testusr',hashlib.sha256('testPSWD'.encode()).hexdigest()]]) == (False,False), "User check failed"
    #Wrong password
    assert usrcheck.usr_check('testusr', 'wrongPSWD',[['testusr',hashlib.sha256('testPSWD'.encode()).hexdigest()]]) == (True,False), "User check failed"
test_auth()