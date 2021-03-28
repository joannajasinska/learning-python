def funkcja1():
    print("Cokolwiek")

funkcja1()
funkcja1()

def silnia(n):
    if n!=1:
        return n * silnia(n-1)
    else:
        return 1
    
a= silnia(5)
print(a)