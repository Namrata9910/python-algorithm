#write a function to swap a number in place



def swap(a,b):
    b = a+b
    a = b-a
    b = b-a

    return(str(a)+' '+str(b))


if __name__ == "__main__":
    a,b = map(int,input().split())
    print(swap(a,b))
