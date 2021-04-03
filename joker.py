def password (func):
    def wrong (arg):
        if len(arg) >=8:
            func(arg)
            print("password ok")
        else:
            func(arg)
            print("password invalid")
    return wrong

@password
def vopros (a):
    print(a)


vopros("gggggg gggggg")