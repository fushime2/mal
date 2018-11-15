def pr_list(ls):
    s = "("
    for i, elem in enumerate(ls):
        if isinstance(elem, list):
            s += pr_list(elem)
        else:
            s += pr_str(elem)
            if i != len(ls) - 1:
                s += " "
    s += ")"
    return s


def pr_str(ast):
    if isinstance(ast, list):
        return pr_list(ast)
    else:
        return str(ast)
