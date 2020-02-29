

global_variable = 123 # not the same global as in PHP

def function():
    print(global_variable)
    print(other_global)
    print(another_gloal)
    another_gloal = 456


function()

other_global = 123
another_gloal = 123

function()
