def function():
    list((i := i) for i in range(5))
    print(i)

function()
