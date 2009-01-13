# -*- coding: utf-8 -*-

from five import grok
from zope.interface import implements
from zope.component import getUtility
from zope.app.intid.interfaces import IIntIds
from persistent.interfaces import IPersistent
from interfaces import IObjectIdManager


class IntIdResolver(grok.GlobalUtility):
    """Object id manager using intid.
    """
    grok.implements(IObjectIdResolver)

    def __init__(self):
        self._intidResolver = getUtility(IIntIds).register
        self._objectResolver = getUtility(IIntIds).getObject

    def getObjectFromId(self, id):
        return self._objectResolver(int(id))

    def getIdFromObject(self, obj):
        return str(self._intidResolver(obj))


class IntIdAdapter(grok.Adapter):
    """Object id manager using intid.
    """
    grok.adapts(IPersistent)
    grok.implements(IUniqueObjectId)

    def UID(self):
        resolver = getUtility(IIntIds).register
        return str(resolver(self.context))
