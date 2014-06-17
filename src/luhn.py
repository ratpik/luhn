from random import randint


class Luhn:
    # n includes the checksum as the last digit
    #http://en.wikipedia.org/wiki/Luhn_algorithm
    def is_valid_mod_10(self, n):

        if n == 0:
            return False

        digits = self._get_digits(n)

        if len(digits) < 2:
            return False

        #Exclude the checksum digit
        checksum = digits[0]
        digits = digits[1:]

        #Double every second digit
        #Remember digits are in reverse order

        for pos, value in enumerate(digits):
            if pos % 2 == 0:
                digits[pos] = sum(self._get_digits(2 * digits[pos]))

        #Reduce to single digit by summation
        #checksum

        sum_total = sum(digits)
        sum_total_times_9 = sum_total * 9

        sum_digits = self._get_digits(sum_total_times_9)

        return sum_digits[0] == checksum


    @staticmethod
    def _get_digits(n):
        digits = []
        while n != 0:
            digits.append(n % 10)
            n /= 10

        return digits


    def generate(self, num_of_digits=16, do_random_initialization=False):
        low = 10 ** (num_of_digits - 1)
        high = 10 ** num_of_digits - 1

        if do_random_initialization:
            n = randint(low, high)
        else:
            n = low

        while n <= high:
            if self.is_valid_mod_10(n):
                yield n
            n += 1


if __name__ == '__main__':
    l = Luhn()
    print l.is_valid_mod_10(26)

    x = l.generate(num_of_digits=14, do_random_initialization=False)

    print [x.next() for i in range(10)]