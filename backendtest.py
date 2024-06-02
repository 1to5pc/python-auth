import usrcheck
import hash
def test_auth():
    # Updated test to support new implementation
    for hash_method in hash.SUPPORTED_HASHES:
        # Overwrite test
        hasher = hash.Hasher(hash_method, ('testPSWD' + '1QgF35ws').encode())
        usr_list = [['testusr', hasher.hexdigest(), '1QgF35ws']]
        hasher = hash.Hasher(hash_method, ('testPSWD2' + '9DgF37sx').encode())
        usr_list.append(['testusr2', hasher.hexdigest(),'9DgF37sx'])
        usrcheck.save_users(usr_list, True)
        assert usrcheck.load_users() == usr_list, "UserList loading N1 failed"
        # Append test
        hasher = hash.Hasher(hash_method, ('testPSWD3' + '90I2iX9qS').encode())
        usr_list.append(['testusr 03', hasher.hexdigest(), '90I2iX9qS'])
        usr_list2 = [['testusr 03', hasher.hexdigest(), '90I2iX9qS']]
        hasher = hash.Hasher(hash_method, ('testPSWD!4' + 'wSDzyhfW92').encode())
        usr_list.append(['test USR !4', hasher.hexdigest(),'wSDzyhfW92'])
        usr_list2.append(['test USR !4', hasher.hexdigest(),'wSDzyhfW92'])
        hasher.clear_hasher()
        usrcheck.save_users(usr_list2, False)
        assert usrcheck.load_users() == usr_list, "UserList loading N2 failed"
        # Correct credentials
        assert usrcheck.usr_check('testusr', 'testPSWD', usr_list, test_hasher=hasher) == (True,True), "User check failed"
        # Wrong username
        assert usrcheck.usr_check('wrongusr', 'testPSWD', usr_list, test_hasher=hasher) == (False,False), "Username check failed"
        # Wrong password
        assert usrcheck.usr_check('testusr', 'wrongPSWD', usr_list, test_hasher=hasher) == (True,False), "User password check failed"
test_auth()