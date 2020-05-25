def bar(n, ch="-"):
    """A horizontal bar of length n."""
    return ch * n
def separator(html=False):
    """A horizontal line, either in plain text or HTML."""
    if html:
        print "<hr />"
    else:
        print bar(40)
def box(txt):
    """Put txt inside a box."""
    print "+-" + bar(len(txt)) + "-+"
    print "| " + txt           + " |"
    print "+-" + bar(len(txt)) + "-+"
box("Hello")
