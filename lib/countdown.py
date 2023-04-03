# your code goes here!
import time
import ipdb

def countdown():
    i = 10
    while i > 0:
        print(f"{i} SECOND(S)!")
        i -= 1
    print('HAPPY NEW YEAR!')

    #or
#         if i == 0:
#             print('HAPPY NEW YEAR!')
#         else:
#             print(f"{i} SECOND(S)")
#         i -= 1
# ipdb.set_trace()
        # time.sleep(1)
        # print("HAPPY NEW YEAR!")

# def countdown_with_sleep(n):
#     for i in range(n, -1, -1):
#         print(i)
#         time.sleep(1)

def countdown_with_sleep(i):
    while i > 0:
        print(f"{i} SECOND(S)!")
        i -= 1
    time.sleep()
    print('HAPPY NEW YEAR!')

