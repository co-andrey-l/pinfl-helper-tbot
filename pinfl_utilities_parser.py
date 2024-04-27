from collections import namedtuple
from datetime import date


class PinflUtilitiesParser:
    WEIGHT_FUNC = [7, 3, 1, 7, 3, 1, 7, 3, 1, 7, 3, 1, 7]
    BEGINNING_CENTURY = 17

    Parts = namedtuple(
        "Parts",
        [
            "area_code",
            "check_digit",
            "century",
            "gender",
            "decade",
            "year",
            "month",
            "day",
            "birth_date",
            "citizen_serial_number",
        ],
    )

    def __init__(self, value):
        self.value = "".join(filter(str.isdigit, str(value)))

    @property
    def century_and_gender(self):
        return int(self.value[0])

    @property
    def gender(self):
        return "male" if self.century_and_gender % 2 == 1 else "female"

    @property
    def century(self):
        return (((self.century_and_gender + 1) // 2) + self.BEGINNING_CENTURY) * 100

    @property
    def decade(self):
        return int(self.value[5:7])

    @property
    def year(self):
        return self.century + self.decade

    @property
    def month(self):
        return int(self.value[3:5])

    @property
    def day(self):
        return int(self.value[1:3])

    @property
    def birth_date(self):
        return date(self.year, self.month, self.day) if self.is_valid_date() else None

    @property
    def area_code(self):
        return self.value[7:10]

    @property
    def citizen_serial_number(self):
        return self.value[10:13]

    @property
    def check_digit(self):
        return int(self.value[13])

    @property
    def parts(self):
        return self.Parts(
            area_code=self.area_code,
            check_digit=self.check_digit,
            century=self.century,
            gender=self.gender,
            decade=self.decade,
            year=self.year,
            month=self.month,
            day=self.day,
            birth_date=self.birth_date,
            citizen_serial_number=self.citizen_serial_number,
        )

    def is_valid(self):
        return len(self.value) == 14 and (
            self.is_valid_date()
            and self.validate_check_digit()
            and self.validate_area_code()
            and self.validate_citizen_serial_number()
        )

    def is_valid_date(self):
        try:
            date(self.year, self.month, self.day)
            return True
        except ValueError:
            return False

    def validate_check_digit(self):
        return self.check_digit == self.calculate_check_digit()

    def validate_area_code(self):
        return int(self.area_code) != 0

    def validate_citizen_serial_number(self):
        return int(self.citizen_serial_number) != 0

    def calculate_check_digit(self):
        pinfl_numbers = list(map(int, self.value))
        return (
            sum(
                num * weight
                for num, weight in zip(pinfl_numbers[:-1], self.WEIGHT_FUNC)
            )
            % 10
        )
