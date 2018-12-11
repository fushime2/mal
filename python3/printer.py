from mal_types import *


def pr_list(ls):
    s = "("
    for i, elem in enumerate(ls):
        if is_list(elem):
            s += pr_list(elem)
        else:
            s += pr_str(elem)
            if i != len(ls) - 1:
                s += " "
    s += ")"
    return s


def pr_str(ast):
    if is_list(ast):
        return pr_list(ast)
    elif ast is True:
        return "true"
    elif ast is False:
        return "false"
    elif ast is None:
        return "nil"
    else:  # synbol
        return str(ast)
