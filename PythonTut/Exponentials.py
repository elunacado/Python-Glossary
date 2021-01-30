print(2**3)

def RaiseToPower (base, pow):
    result = 1
    for index in range(pow):
        result = result * base
    return result

print(RaiseToPower(10,10))