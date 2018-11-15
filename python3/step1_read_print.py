import reader
import printer


def READ(s):
    return reader.read_str(s)


def EVAL(ast):
    return ast


def PRINT(expr):
    return printer.pr_str(expr)


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
