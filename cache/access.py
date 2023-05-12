import os
import random
import hashlib

files = os.listdir("./secrets")
random_file = random.choice(files)
#print(random_file)
hash = hashlib.sha256(random_file.encode()).hexdigest()
#print(hash)


while True:
  f = open("./secrets/" + str(random_file))
  f.read()
  s = input("enter your song:")
  if hashlib.sha256(s.encode()).hexdigest() == hash:
    print("nice...😎")
    break
  else:
    print("oh...🤓")
  f.close()
