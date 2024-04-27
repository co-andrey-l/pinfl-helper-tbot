import random
import datetime


class PinflUtilitiesGenerator:
    def generate_pinfl(self, gender, birth_date):
        century = str(self.gender_date_index(gender, birth_date))
        month = str(birth_date.month).zfill(2)
        day = str(birth_date.day).zfill(2)
        decade = str(birth_date.year % 100)
        area_code = str(random.randint(1, 999)).zfill(3)
        serial_number = str(random.randint(1, 999)).zfill(3)
        pinfl_digits = [
            str(digit)
            for digit in century + day + month + decade + area_code + serial_number
        ]
        check_digit = self._calculate_check_digit(pinfl_digits)
        return "".join(pinfl_digits) + str(check_digit)

    def gender_date_index(self, gender, birth_date):
        gender_shift_number = 1 if gender == "female" else 0
        return (birth_date.year // 100) - 17 + gender_shift_number

    def _calculate_check_digit(self, pinfl_digits):
        weight_func = [7, 3, 1, 7, 3, 1, 7, 3, 1, 7, 3, 1, 7]
        sum_digits = sum(
            int(digit) * weight for digit, weight in zip(pinfl_digits, weight_func)
        )
        return sum_digits % 10
