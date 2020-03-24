from django  import templates

register=templates.Library()

def cut(value,arg):
    return value.replace(arg,' ')

register.filter('cut',cut)
