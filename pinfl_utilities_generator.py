"""Random PINFL generation module."""

import random


class PinflUtilitiesGenerator:
    """Random PINFL generation."""

    def generate(self, gender, birth_date):
        """PINFL generation function."""

        century = str(self._gender_date_index(gender, birth_date))

        month = str(birth_date.month).zfill(2)
        day = str(birth_date.day).zfill(2)
        decade = str(birth_date.year % 100)

        area_code = str(random.randint(1, 999)).zfill(3)
        serial_number = str(random.randint(1, 999)).zfill(3)

        digits = [
            str(digit)
            for digit in century + day + month + decade + area_code + serial_number
        ]

        check_digit = self._calculate_check_digit(digits)
        return "".join(digits) + str(check_digit)

    def generate_pinfl(self, gender, birth_date):
        """Generate PINFL."""

        return self.generate(gender, birth_date)

    def _gender_date_index(self, gender, birth_date):
        gender_shift_number = 1 if gender == "female" else 0
        return (birth_date.year // 100) - 17 + gender_shift_number

    def _calculate_check_digit(self, digits):
        weight_func = [7, 3, 1, 7, 3, 1, 7, 3, 1, 7, 3, 1, 7]
        sum_digits = sum(
            int(digit) * weight for digit, weight in zip(digits, weight_func)
        )
        return sum_digits % 10
