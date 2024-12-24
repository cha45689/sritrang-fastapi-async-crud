"""
This file is use to store mock data use to test Pagination model validation rule
"""

valid_pagination = [
    {"current_page": 1, "next_page": 1, "last_page": 2, "total": 2, "size": 1},
    {"current_page": 1, "next_page": None, "last_page": 1, "total": 1, "size": 1},
]

invalid_pagination = [
    {
        "current_page": 1.5,
        "next_page": 1.5,
        "last_page": 2.5,
        "total": 2.5,
        "size": 1.5,
    },
    {
        "current_page": "1",
        "next_page": "1",
        "last_page": "None",
        "total": "1",
        "size": "1",
    },
    {
        "current_page": [1],
        "next_page": [1],
        "last_page": [2],
        "total": [2],
        "size": [1],
    },
    {
        "current_page": {1},
        "next_page": {1},
        "last_page": {None},
        "total": {1},
        "size": {1},
    },
    {
        "current_page": {"1": "1"},
        "next_page": {"1": "1"},
        "last_page": {"1": "1"},
        "total": {"1": "1"},
        "size": {"1": "1"},
    },
    {
        "current_page": None,
        "next_page": None,
        "last_page": None,
        "total": None,
        "size": None,
    },
]
