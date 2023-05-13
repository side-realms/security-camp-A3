import hashlib
import time
import random
from itertools import zip_longest


def checker(password):
    if(len(password) == 0):
        return False
    for cand, flag in zip_longest(password, 'Choo-Choo_Gatagoto'):
        time.sleep(random.randint(0, 5) / 1000) # for brute force
        if(cand != flag):
            flag = False
    if(flag):
        return True
    return False

def login(username, password):
    username_hs = hashlib.sha256(username.encode()).hexdigest()

    # username = request.args.get('username')
    # password = request.args.get('password')

    if (username_hs == '3a798c7c6b1706ee6762783cba4bb5a8e10db6649c8381407e8bd6d9e017f820')or(username_hs == '4495050a37092f6ceab970f3f4544728235f9bb84fe54a759633c25ae04ddc3d'):
        if checker(password):
            print('nice...')
            return True
        else:
            print('Invalid username or password')
            return False

    else:
        print('Invalid username or password')
        return False

def main(username, password):
    return(login(username, password))


if __name__ == '__main__':
    while(True):
        username = input('username:')
        password = input('password:')
        if(main(username, password)):
            break
