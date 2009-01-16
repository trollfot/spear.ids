# -*- coding: utf-8 -*-

from five import grok
from zope.interface import Interface
from zope.component import getUtility
from zope.app.intid.interfaces import IIntIds
from persistent.interfaces import IPersistent
from zope.cachedescriptors.property import CachedProperty
from interfaces import IObjectIdResolver, IUniqueObjectId


class IntIdResolver(grok.Adapter):
    """Object id manager using intid.
    """
    grok.context(Interface)
    grok.implements(IObjectIdResolver)

    @CachedProperty
    def _intid(self):
        return getUtility(IIntIds)

    def getObjectFromId(self, id):
        return self._intid.getObject(int(id))

    def getIdFromObject(self, obj):
        return str(self._intid.register(obj))


class IntIdAdapter(grok.Adapter):
    """Object id manager using intid.
    """
    grok.context(IPersistent)
    grok.implements(IUniqueObjectId)

    def UID(self):
        resolver = getUtility(IIntIds).register
        return str(resolver(self.context))
