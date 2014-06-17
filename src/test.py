import unittest
from luhn import Luhn


class TestLuhn(unittest.TestCase):
    # Common test credit cards

    #From http://www.getcreditcardnumbers.com/
    VISA = (
        4929684384290814,
        4485474868225445,
        4716208584129064,
        4485889872783222,
        4024007198905654)

    MASTERCARD = (
        5463163488217055,
        5476421201873710,
        5511566476925517,
        5587010699816731,
        5574292728898055,
    )

    DISCOVER = (
        6011463150469272,
        6011031083493196,
        6011097714997277,
        6011990112944117,
        6011623170795796,
    )

    AMEX = (

        346445629631920,
        344830210102575,
        376426520454987,
        343902345238888,
        375400860116671,
    )

    VALID_14_DIGIT_MOD_10 = [10000000000008, 10000000000016, 10000000000024, 10000000000032, 10000000000040, 10000000000057, 10000000000065, 10000000000073, 10000000000081, 10000000000099]

    def setUp(self):
        pass


    def test_validation(self):
        l = Luhn()
        for num in self.VISA:
            self.assertTrue(l.is_valid_mod_10(num))
        for num in self.MASTERCARD:
            self.assertTrue(l.is_valid_mod_10(num))
        for num in self.DISCOVER:
            self.assertTrue(l.is_valid_mod_10(num))
        for num in self.AMEX:
            self.assertTrue(l.is_valid_mod_10(num))


    def test_generation(self):
        l = Luhn()
        generator = l.generate(14)
        generated_numbers = [generator.next() for i in range(len(self.VALID_14_DIGIT_MOD_10))]
        self.assertItemsEqual(self.VALID_14_DIGIT_MOD_10, generated_numbers)

    def test_invalid(self):
        l = Luhn()

        self.assertFalse(l.is_valid_mod_10(20))
        self.assertFalse(l.is_valid_mod_10(21))
        self.assertFalse(l.is_valid_mod_10(22))
        self.assertFalse(l.is_valid_mod_10(23))
        self.assertFalse(l.is_valid_mod_10(24))
        self.assertFalse(l.is_valid_mod_10(25))

        self.assertTrue(l.is_valid_mod_10(26))

        self.assertFalse(l.is_valid_mod_10(27))
        self.assertFalse(l.is_valid_mod_10(28))
        self.assertFalse(l.is_valid_mod_10(29))
        self.assertFalse(l.is_valid_mod_10(30))

if __name__ == '__main__':
    unittest.main()

    