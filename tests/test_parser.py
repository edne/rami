import rami.parser
from rami.parser import Leaf, Branch

code = '''
a:
    b: 1
    c: 2
d:
    e: 3
'''


def test_parser():
    tree = rami.parser.parse(code)
    assert tree == [Branch('a', [Leaf('b', '1'),
                                 Leaf('c', '2')]),
                    Branch('d', [Leaf('e', '3')])]
