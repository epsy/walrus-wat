def function():
    list((x := i) for i in range(5))
    print(x)

function()
