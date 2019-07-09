try:
    x = int(input("Please provide an int value : "))
    if x%2==0 and x%5==0:
        print("Hurray it is what I am looking for")
    else:
        print("Wrong input")
except:
    print("Please proide an int value")
