#!/usr/bin/env python3
"""Helper function for calculating pagination index ranges."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return start and end indexes for a page.

    Page numbers are 1-indexed. The end index is exclusive,
    so it can be used directly as a list slice bound.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
