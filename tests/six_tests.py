import unittest


class SixTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_six_import(self):
        from htmldiff.lib import diff_files


if __name__ == '__main__':
    unittest.main()
