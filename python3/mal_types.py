def is_list(ast):
    return isinstance(ast, list)


def is_symbol(ast, env):
    return env.find(ast)


def is_int(s):
    try:
        val = int(s)
    except ValueError:
        return False
    return True


def is_float(s):
    try:
        val = float(s)
    except ValueError:
        return False
    return True


def is_number(s):
    return is_float(s) or is_int(s)
