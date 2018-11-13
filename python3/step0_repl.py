def READ(s):
    return s

def EVAL(s):
    return s

def PRINT(s):
    return s

def rep(s):
    return PRINT(EVAL(READ(s)))

def main():
    while True:
        try:
            line = input("user> ")
        except EOFError:
            break
        print(rep(line))

if __name__ == "__main__":
    main()
