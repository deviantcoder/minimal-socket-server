def render(template):
    with open(template) as template:
        return template.read()


def index():
    return render('templates/index.html')
    

def blog():
    return render('templates/blog.html')