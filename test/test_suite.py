import unittest
from test import test_qgraph


def create_suite(module):
    suite = unittest.TestSuite()
    suite = unittest.defaultTestLoader.loadTestsFromModule(module)
    return suite


def create_suite_pack():
    suite_list = []
    suite_list.append(create_suite(test_qgraph))

    return suite_list


if __name__ == '__main__':
    suite_pack = unittest.TestSuite(create_suite_pack())

    runner = unittest.TextTestRunner(descriptions=True, verbosity=3)
    runner.run(suite_pack)
