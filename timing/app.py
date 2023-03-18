from flask import Flask, request
import hashlib
import time
import random
from itertools import zip_longest

app = Flask(__name__)

def checker(password):
    if(len(password) == 0):
        return False
    for cand, flag in zip_longest(password, 'Choo-Choo Gatagoto'):
        time.sleep(random.randint(0, 5) / 1000) # for brute force
        if(cand != flag):
            return False
    return True

@app.route('/login', methods = ['GET', 'POST'])
def login():
    username = request.form.get('username')
    username_hs = hashlib.sha256(username.encode()).hexdigest()
    password = request.form.get('password')

    # username = request.args.get('username')
    # password = request.args.get('password')

    if username_hs == '3a798c7c6b1706ee6762783cba4bb5a8e10db6649c8381407e8bd6d9e017f820':
        if checker(password):
            return {
                    "success": True,
                    "message": "nice ..."
            }
        else:
            return {
            "success": False,
            "message": "Invalid username or password"
        }

    else:
        return {
            "success": False,
            "message": "Invalid username or password"
        }


if __name__ == '__main__':
    # app.debug = True
    app.run(host='127.0.0.1', port=80)