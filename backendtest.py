import usrcheck
import hash
def test_auth():
    # Updated test to support new implementation
    for hash_method in hash.SUPPORTED_HASHES:
        hasher = hash.Hasher(hash_method, ('testPSWD' + '1QgF35ws').encode())
        usr_list = [['testusr', hasher.hexdigest(), '1QgF35ws']]
        hasher.clear_hasher()
        usrcheck.save_users(usr_list, True)
        assert usrcheck.load_users() == usr_list, "UserList loading failed"
        assert usrcheck.usr_check('testusr', 'testPSWD', usr_list, test_hasher=hasher) == (True,True), "User check failed"
        #Wrong username
        assert usrcheck.usr_check('wrongusr', 'testPSWD', usr_list, test_hasher=hasher) == (False,False), "User check failed"
        #Wrong password
        assert usrcheck.usr_check('testusr', 'wrongPSWD', usr_list, test_hasher=hasher) == (True,False), "User check failed"
test_auth()