# to create fibonacci serries 
def fibonacci(n):
    a=0
    b=1
    series=[]
    for _ in range(n):
        series.append(a)
        a,b=b,a+b
    return series
print(fibonacci(10))