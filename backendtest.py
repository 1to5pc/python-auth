import usrcheck
import hash

def test_auth():
    # Assuming usr_list and hasher are set up correctly in your test environment
    usr_list = [['testusr', 'hashedPSWD', 'salt']]
    hasher = hash.Hasher('sha256')
    
    assert usrcheck.user_check('testusr', 'testPSWD', usr_list, test_hasher=hasher) == (True, True), "User check failed"

if __name__ == "__main__":
    test_auth()
