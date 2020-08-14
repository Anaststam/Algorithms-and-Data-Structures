"""
# Created by Anastasia on 12/8/20
"""
def test(i:int):

    for i in range (1,51):

        if i % 3 == 0:
            #print("The number is:", i, "and is multiple of 3")

            print("Fizz")
        elif i % 5 == 0:
            #print("The number is:", i, "and is multiple of 5")
            print("Buzz")
        elif(i%5==0 and i%3==0):
           # print("The number is:", i, "and is multiple for 5 and 3")
            print("FizzBuzz")
        else:
            print(i)

test(i=10)

