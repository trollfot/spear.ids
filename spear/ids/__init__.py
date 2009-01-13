try:
    __import__('pkg_resources').declare_namespace(__name__)
except ImportError:
    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)


from interfaces import IObjectIdResolver, IUniqueObjectId
from resolvers import IntIdResolver, IntIdAdapter
