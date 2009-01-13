#!/usr/bin/python
# -*- coding: utf-8 -*-

from zope.interface import Interface


class IObjectIdResolver(Interface):
    """Manage object id queries.
    """
    def getObjectFromId(id):
        """With the given id, return object.
        """

    def getIdFromObject(obj):
        """With the object, return id.
        """

        
class IUniqueObjectId(Interface):
    """Unique identifier for persistent object.
    """
    def UID():
        """Returns the unique identifier for the object.
        """
