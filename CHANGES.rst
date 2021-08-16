Version 0.1.1
-------------

Unreleased

-   Replace ``posixemulation`` from Werkzeug 1.0.1 with ``os.rename``. :issue:`12`


Version 0.1.0
-------------

Released 2020-02-26

-   Extracted from Werkzeug 0.15.
-   Dropped support for Python 3.4.
-   ``SessionMiddleware`` sets ``secure_cookie.session`` in the environ
    instead of ``werkzeug.session``.
-   ``FilesystemSessionStore`` uses the filename template
    ``secure_cookie_%s.session`` instead of ``werkzeug_%s.sess``.
-   ``SecureCookie.serialization_method`` is ``json`` instead of
    ``pickle``. To upgrade existing tokens, override ``unquote`` to try
    ``pickle`` if ``json`` fails.
