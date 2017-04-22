import unittest

import ast
import gast
import glob
import os


class SelfTestCase(unittest.TestCase):

    def testParse(self):
        srcs = glob.glob(os.path.join(gast.__path__[0], '*.py'))
        for src_py in srcs:
            with open(src_py) as f:
                content = f.read()
            gast.parse(content)

    def testCompile(self):
        srcs = glob.glob(os.path.join(gast.__path__[0], '*.py'))
        for src_py in srcs:
            with open(src_py) as f:
                content = f.read()
            gnode = gast.parse(content)
            compile(gast.gast_to_ast(gnode), src_py, 'exec')


if __name__ == '__main__':
    unittest.main()
