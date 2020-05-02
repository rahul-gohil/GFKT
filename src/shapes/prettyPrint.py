import json

def prettify(d):
    return json.dumps(
        d,
        sort_keys = False,
        indent = 4,
        separators = (
        ',',
        ': '
        )
    )
