def dekorator(uskor):
    def obertka(v0,v1,t):
        a=uskor(v0,v1,t)
        print(v0*t+(a*t*t)/2)
        print(uskor(v0,v1,t))
    return obertka

try:
    @dekorator
    def uskor(v0,v1,t):
        a=(v1-v0)/t
        return(a)
except ZeroDivisionError:
    print("Нельзя делить на ноль")
except ValueError:
    print("Вводить строки нельзя")


uskor(3,4,5)

