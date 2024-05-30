import usrcheck
import hashlib
def test_auth():
    usr_list=[['testusr',hashlib.sha256(str('testPSWD'+'1QgF35ws').encode()).hexdigest(),'1QgF35ws']]
    usrcheck.save_users(usr_list,True)
    assert usrcheck.load_users() == usr_list, "Userlist loading failed"
    assert usrcheck.usr_check('testusr', 'testPSWD',usr_list) == (True,True), "User check failed"
    #Wrong username
    assert usrcheck.usr_check('wrongusr', 'testPSWD',usr_list) == (False,False), "User check failed"
    #Wrong password
    assert usrcheck.usr_check('testusr', 'wrongPSWD',usr_list) == (True,False), "User check failed"
test_auth()