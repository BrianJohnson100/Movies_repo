#from app import do_it, add_up
# from maths import add_up

import app

def andy():
    print("Hello from lib")
    print(app.add_up(1000, 2000))

    print("Hello from lib")
    print(f' this is do_it {app.do_it()}')

if __name__ == "__main__":
    andy()

