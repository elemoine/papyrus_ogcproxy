from pyramid.config import Configurator

def add_route(config):
    """ Add a route to the ogcproxy view callable. The proxy
    service is made available at ``/ogcproxy``.

    Arguments:

    * ``config``: the ``pyramid.config.Configurator`` object.
    """
    route = config.add_route('ogcproxy', '/ogcproxy')
    config.add_view('papyrus_ogcproxy.views:ogcproxy', route_name='ogcproxy')
    return route

def includeme(config):
    """ The callable making it possible to include papyrus_ogcproxy
    in a Pyramid application.

    Calling ``config.include(papyrus_ogcproxy)`` will result in this
    callable being called.

    Arguments:

    * ``config``: the ``pyramid.config.Configurator`` object.
    """
    add_route(config)

def main(global_config, **settings):
    """ Return the Pyramid application.
    """
    config = Configurator(settings=settings)
    config.include(includeme)
    return config.make_wsgi_app()
