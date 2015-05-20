papyrus_ogcproxy
=================

papyrus_ogcproxy provides an easy and convenient method for embeding
an OGC proxy in Pyramid applications.

The source code of papyrus_ogcproxy is straightforward, so if
papyrus_ogcproxy doesn't do what you want, open its source code, get
inspiration, and write your own code.

Install
-------

papyrus_ogcproxy can be installed with ``easy_install``::

    $ easy_install papyrus_ogcproxy

Often you'll want to make papyrus_ogcproxy a dependency of your Pyramid
application, which is done by adding ``papyrus_ogcproxy`` to the
``install_requires`` list defined in the Pyramid application's ``setup.py``
file.

Set up
------

Using papyrus_ogcproxy to set up an OGC proxy in a Pyramid application is easy.

Edit the application's main file, ``__init__.py``, and register
papyrus_ogcproxy using the ``Configurator.include`` method::

    def main(global_config, **settings):

        config = Configurator(settings=settings)

        import papyrus_ogcproxy
        config.include(papyrus_ogcproxy)

That's it! The OGC proxy is available at ``/ogcproxy``.

Here is a test URL:
http://localhost:6543/ogcproxy?url=http%3A%2F%2Fmap1.vis.earthdata.nasa.gov/wmts-geo/wmts.cgi%3FSERVICE%3DWMTS%26REQUEST%3DGetCapabilities

Using a proxy for the proxy
---------------------------

If the requests made by the OGC proxy should be made through a proxy, the additional
package ``pysocks`` is required. After the installation of this package, configure
the proxy::


    from papyrus_ogcproxy import views as ogcproxy_views
    from httplib2 import ProxyInfo
    import socks
    ogcproxy_views.proxy_info = ProxyInfo(socks.SOCKS5, 'localhost', 1080)

With this configuration the OGC proxy will make requests through the proxy
``localhost:1080``. For information please refer to the
documentation of `PySocks <https://github.com/Anorov/PySocks>`_ and
`httplib2 <http://httplib2.googlecode.com/hg/doc/html/libhttplib2.html#httplib2.ProxyInfo>`_.


Set up a development environment
--------------------------------

To set up a development environment with virtualenv, run the following
commands::

    $ virtualenv venv
    $ venv/bin/python setup.py develop
    $ venv/bin/pip install -r requirements-dev.txt

Run the tests
-------------

To run the tests::

    $ venv/bin/nosetests --with-coverage

One test assumes that a proxy server is running at ``localhost:1080``. To start
a proxy run::

    $ ssh -N -D 0.0.0.0:1080 localhost
