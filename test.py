import random
import time

a = random.randint(0,100)
b = random.randint(0,100)

op = random.choice(["add","sustract","divide","mult"])
if op =="add":
    print("{}+{} ".format(a,b))
    _init = time.time()
    input("...")
    print("took {}s". format (round(time.time()-_init,1)))
    result = int(input("="))
    print("correct") if result == a+b else print("result was {}".format(a+b))
elif op =="sustract": 
    print("{}-{} ".format(a,b))
    _init = time.time()
    input("...")
    print("took {}s". format (round(time.time()-_init,1)))
    result = int(input("="))
    print("correct") if result == a-b else print("result was {}".format(a-b))

a = random.randint(0,10)
b = random.randint(0,15)

if op =="divide":
    print("{}/{} ".format(a,b))
    _init = time.time()
    input("...")
    print("took {}s". format (round(time.time()-_init,1)))
    result = int(input("="))
    print("correct") if round(result,1) == a/b else print("result was {}".format(round(a/b,1)))

elif op =="mult":
    print("{}*{} ".format(a,b))
    _init = time.time()
    input("...")
    print("took {}s". format (round(time.time()-_init,1)))
    result = int(input("="))
    print("correct") if result == a*b else print("result was {}".format(a*b))

time.sleep(5)