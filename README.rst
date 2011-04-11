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

Using papyrus_ogcproxy to set an OGC proxy in a Pyramid application is easy.

Edit the application's main file, ``__init__.py``, and register
papyrus_ogcproxy using the ``Configurator.include`` method::

    def main(global_config, **settings):

        config = Configurator(settings=settings)

        import papyrus_ogcproxy
        config.include(papyrus_ogcproxy)

That's it! The OGC proxy is available at ``/ogcproxy``.

Here is a test URL:
http://localhost:5643/ogcproxy?url=http://wms.jpl.nasa.gov/wms.cgi?SERVICE=WMS&REQUEST=GetCapabilities

Run the tests
-------------

To run the tests install the ``nose``, ``mock`` and ``coverage`` packages in
the Python environment, and execute::

    $ nosetests --with-coverage
