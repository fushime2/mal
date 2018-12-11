import reader
import printer
from env import Env
from mal_types import *

repl_env = Env()
repl_env.set("+", lambda a, b: a + b)
repl_env.set("-", lambda a, b: a - b)
repl_env.set("*", lambda a, b: a * b)
repl_env.set("/", lambda a, b: a // b)


def READ(s):
    return reader.read_str(s)


def eval_ast(ast, env):
    if is_list(ast):
        return list(map(lambda a: EVAL(a, env), ast))
    elif is_symbol(ast, env):
        try:
            return env.get(ast)
        except BaseException:
            raise Exception("error: symbol is not found.")
    else:
        return ast


def EVAL(ast, env=repl_env):
    if not is_list(ast):
        return eval_ast(ast, env)
    elif len(ast) == 0:
        return ast
    else:
        a0, a1, a2 = ast[0], ast[1], ast[2]
        if a0 == "def!":
            return env.set(a1, EVAL(a2, env))
        elif a0 == "let*":
            let_env = Env(env)
            for i in range(0, len(a1), 2):
                let_env.set(a1[i], EVAL(a1[i + 1], let_env))
            return EVAL(a2, let_env)
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
        except BaseException as err:
            print(err)


if __name__ == "__main__":
    main()
