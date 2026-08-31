#!/usr/bin/env python3
"""List all documents in a MongoDB collection."""


def list_all(mongo_collection):
    """Return a list of all documents in mongo_collection.

    If the collection is empty, an empty list is returned.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
