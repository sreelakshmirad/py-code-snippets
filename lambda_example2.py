def trigger_action(f, val):
    return f(val)

func = lambda x : x* 3

print(trigger_action(func,5))