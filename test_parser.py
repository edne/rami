def test_parser():
    import parser
    code = '''
a:
    b: 1
    c: 2
d:
    e: 3
    '''
    tree = parser.parse(code)
    assert tree == [['a', [['b', '1'],
                           ['c', '2']]],
                    ['d', [['e', '3']]]]
