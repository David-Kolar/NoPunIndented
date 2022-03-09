from random import *
seed(42)
print(100)
for i in range(100):
    try:
        s = "".join(choice("abc") for i in range(10))
    finally:
        if random()<0.4:
            print(s+":")
        else:
            print(s)