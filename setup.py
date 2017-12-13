from IPython.display import HTML, display

def style():
    with open('style.css') as f:
        display(HTML('<style>%s</style>' % f.read()))

