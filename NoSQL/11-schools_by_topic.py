#!/usr/bin/env python3
"""Find schools that cover a given topic."""


def schools_by_topic(mongo_collection, topic):
    """Return the list of schools that have the given topic."""
    return list(mongo_collection.find({"topics": topic}))
