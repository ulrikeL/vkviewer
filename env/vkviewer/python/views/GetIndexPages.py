from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from vkviewer.python.tools import checkIsUser, getCookie
from vkviewer import log

""" basic start site """
@view_config(route_name='home', renderer='index.mako', permission='view',http_cache=0)
def get_index_page(request):  
    log.info('Call view get_index_page.')
    
    # checks if already a user cookie is set and if yes gives back the logged in view
    if checkIsUser(request):
        target_url = request.route_url('home_login')
        return HTTPFound(location = target_url)
    elif getCookie(request, 'welcomepage') == 'off':
        return {'welcomepage':'off'}
    else: 
        return {}

""" basic start site but logged in """
@view_config(route_name='home_login', renderer='indexLoggedIn.mako', permission='edit',http_cache=0)
def get_index_page_loggedIn(request):
    return {'welcomepage':'off'}




    

