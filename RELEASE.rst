Release
-------

This file provides the steps for releasing a new version of papyrus_ogcproxy.

Verify that the version number is correct in ``setup.py``.  If not then change
it, then commit and push.

Verify that the tests pass, with 100% coverage::

    $ nosetests --with-coverage
    ..........
    Name                     Stmts   Miss  Cover   Missing
    ------------------------------------------------------
    papyrus_ogcproxy            10      0   100%   
    papyrus_ogcproxy.views      28      0   100%   
    ------------------------------------------------------
    TOTAL                       38      0   100%   
    ----------------------------------------------------------------------
    Ran 10 tests in 14.006s

    OK

Create Git tag and push it::

    $ git tag -a x.y -m 'version x.y'
    $ git push origin x.y

Upload the package to PyPI::

    $ python setup.py sdist upload
