print("hello")


def jishu(start,end):
    global i
    for i in range(start,end):
        if i % 2 == 1:
            print(i)





def oushu(start,end):
    global i
    for i in range(start,end):
        if i % 2 == 0:
            print(i)

jishu(1,101)
oushu(1,101)