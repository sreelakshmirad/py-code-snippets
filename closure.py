# text = "Hello Python"


def outerFunction():
    text = "Hello Closures"
    def innerFunction():
        print(text)
    return innerFunction

# text = "Hello Python"
# print(text)
outerFunction()()

