x=10
y=10
scale=15

def test(x:int, y:int):
    x*=scale
    y*=scale
    return(x,y)



x,y=test(x,y)
print(x,y)
