from lang import Lang


lang = Lang()


@lang.leaf
def sides(value):
    return {'sides': value}


@lang.leaf
def color(value):
    return {'color': value}


@lang.branch
def group(branches):
    return {'group': list(branches)}


@lang.branch
def square(branches):
    return {'square': list(branches)}


@lang.branch
def polygon(branches):
    return {'polygon': list(branches)}


code = '''
group:
    square:
        color: [0, 1, 1]

    polygon:
        sides: 6
        color: [1, 1, 0]

polygon:
    sides: 3
    color: [1, 1, 0]
'''


def test_lang():
    g, p = lang.eval(code)

    assert g == {'group': [{'square': [{'color': [0, 1, 1]}]},
                           {'polygon': [{'sides': 6}, {'color': [1, 1, 0]}]}]}

    assert p == {'polygon': [{'sides': 3}, {'color': [1, 1, 0]}]}
