def function(lines):
    if any((comment := line).startswith('#') for line in lines):
        print("First comment:", comment)
    else:
        print("There are no comments")

function("""
a line
another line
# a comment
not a comment
""".split("\n"))
