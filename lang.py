from parser import parse


class Lang:
    def __init__(self):
        self.leaves = {}
        self.branches = {}

    def eval(self, code):
        parsed = parse(code)
        return self._eval_parsed(parsed)

    def _eval_parsed(self, parsed):
        for branch in parsed:
            name, content = branch

            if isinstance(content, str):
                if name in self.leaves:
                    f = self.leaves[name]
                    value = eval(content)
                    yield f(value)
                else:
                    raise Exception('Undefined leaf {}'.format(name))

            elif isinstance(content, list):
                if name in self.branches:
                    f = self.branches[name]
                    branches = self._eval_parsed(content)
                    yield f(branches)
                else:
                    raise Exception('Undefined branch {}'.format(name))

            else:
                raise Exception('Error in parsing')

    def leaf(self, f):
        name = f.__name__
        self.leaves[name] = f
        return f

    def branch(self, f):
        name = f.__name__
        self.branches[name] = f
        return f
