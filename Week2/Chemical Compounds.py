import unittest
import re
with open('elements.txt') as f:
    ELEMENTS = set(i.split(',')[1] for i in f)


def check_parens(compound):
    return compound.count('(') == compound.count(')')


def validate(compound):
    return False


class TestValidate(unittest.TestCase):
    def test_check_parens(self):
        self.assertTrue(check_parens("CH3CH2OH"))
        self.assertTrue(check_parens("H2O"))
        self.assertTrue(check_parens("Uut(HLr2)20Th"))
        self.assertTrue(check_parens("C8H10N4O2"))
        self.assertTrue(check_parens("Rb"))

    def test_validate(self):
        self.assertTrue(validate("CH3CH2OH"))
        self.assertTrue(validate("H2O"))
        self.assertTrue(validate("Uut(HLr2)20Th"))
        self.assertTrue(validate("C8H10N4O2"))
        self.assertTrue(validate("Rb"))
        self.assertTrue(validate("(NaO)2"))
        self.assertTrue(validate("H(H)1(H)1"))

        self.assertFalse(validate("C2C3C4CX(C5C6C7C100)2"))
        self.assertFalse(validate("chicken"))
        self.assertFalse(validate("Ba(C(H2O)4C)2Ba"))
        self.assertFalse(validate("H2O(H2O2)"))


def main():
    line = input('Line: ')
    while line:
        if validate(line):
            print('Valid.')
        else:
            print('Invalid.')
        line = input('Line: ')

if __name__ == '__main__':
    unittest.main(verbosity=2)
    # main()
