from django import template
#from django.template import resolve_variable

register=template.Library()

def get_url_not_endwithslash(url):
    return url[:-1]
def show_keyword(body, keywords):
    return body.replace(keywords, '<span class="showkey">'+keywords+'</span>')
register.filter('show_keyword', show_keyword)
register.filter('get_url_not_endwithslash', get_url_not_endwithslash)


