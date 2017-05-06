import rami.parser

code = '''
a:
    b: 1
    c: 2
d:
    e: 3
'''


def test_parser():
    tree = rami.parser.parse(code)
    assert tree == [['a', [['b', '1'],
                           ['c', '2']]],
                    ['d', [['e', '3']]]]
