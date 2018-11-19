import reader
import printer
from mal_types import *

repl_env = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b
}


def READ(s):
    return reader.read_str(s)


def eval_ast(ast, env):
    if is_symbol(ast):
        try:
            return env[ast]
        except BaseException:
            raise Exception("error: symbol is not found.")
    elif is_list(ast):
        return list(map(lambda a: EVAL(a, env), ast))
    else:
        return ast


def EVAL(ast, env=repl_env):
    if not is_list(ast):
        return eval_ast(ast, env)
    elif len(ast) == 0:
        return ast
    else:
        elist = eval_ast(ast, env)
        return elist[0](elist[1], elist[2])


def PRINT(expr):
    return printer.pr_str(expr)


def rep(s):
    return PRINT(EVAL(READ(s), repl_env))


def main():
    while True:
        try:
            line = input("user> ")
        except EOFError:
            break

        try:
            print(rep(line))
        except BaseException:
            continue


if __name__ == "__main__":
    main()
