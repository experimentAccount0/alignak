"""This package is a subclasse of bottle available in Bottle class
to avoid code duplication

"""
from .bottlecore import *


class Bottle(Bottle):
    """Bottle subclass Botlle in bottlecore so that we don't duplicate files

    """

    def wsgi(self, environ, start_response):
        """Get wsgi. Add HTTP_X_FORWARDED_PROTO variable to env

        :param environ: bottle env
        :param start_response:
        :return:
        """
        if 'HTTP_X_FORWARDED_PROTO' in environ:
            environ['wsgi.url_scheme'] = environ['HTTP_X_FORWARDED_PROTO']
        return super(Bottle, self).wsgi(environ, start_response)


class BaseRequest(BaseRequest):
    """Used to change MEMFILE_MAX to 102400

    """
    MEMFILE_MAX = 102400