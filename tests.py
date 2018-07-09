import unittest

from rule import stringify_state, iterate_state, prepare_rule


class TestStringMethods(unittest.TestCase):
    def test_print(self):
        state = [True, False, True]
        printed = stringify_state(state)
        self.assertEqual(printed, 'x.x')
        
    def test_prep_rule(self):
        rule = prepare_rule(110)
        self.assertEqual(rule, '01101110')
        
    def test_iterate_state(self):
        state = [True, False, True]
        rule = prepare_rule(110)
        new_state = iterate_state(state, rule)
        self.assertEqual(new_state, [True, True, True])


if __name__ == '__main__':
    unittest.main()
