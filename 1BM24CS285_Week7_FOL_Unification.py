def is_variable(x):
    return isinstance(x, str) and x.islower() and len(x) == 1

def parse_expr(expr):
    pred, args_str = expr.split("(")
    args = [a.strip() for a in args_str[:-1].split(",")]
    return pred.strip(), args

def apply_subs(arg, subs):
    while arg in subs:
        arg = subs[arg]
    return arg

def unify(expr1, expr2):
    pred1, args1 = parse_expr(expr1)
    pred2, args2 = parse_expr(expr2)

    if pred1 != pred2 or len(args1) != len(args2):
        return "Unification Failed"

    subs = {}

    for i in range(len(args1)):
        a1 = apply_subs(args1[i], subs)
        a2 = apply_subs(args2[i], subs)

        if a1 == a2:
            continue
        elif is_variable(a1):
            if a1 in a2:
                return "Unification Failed"
            subs[a1] = a2
        elif is_variable(a2):
            if a2 in a1:
                return "Unification Failed"
            subs[a2] = a1
        else:
            if "(" in a1 and "(" in a2:
                res = unify(a1, a2)
                if res == "Unification Failed":
                    return "Unification Failed"
                subs.update(res)
            else:
                return "Unification Failed"

    return subs

e1 = "Eats(x, Apple)"
e2 = "Eats(Riya, y)"
print("Substitutions:", unify(e1, e2))

e3 = "Knows(John, x)"
e4 = "Knows(x, Elisabeth)"
print("Substitutions:", unify(e3, e4))