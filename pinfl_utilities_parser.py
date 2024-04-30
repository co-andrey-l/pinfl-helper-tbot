"""Utilities for parsing PINFL (Personal Identification Number for Individual Taxpayer)"""

from collections import namedtuple
from datetime import date


class PinflUtilitiesParser:
    """Class for parsing PINFL"""

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
        """Initialize PinflUtilitiesParser with PINFL value."""
        self.value = "".join(filter(str.isdigit, str(value)))

    @property
    def century_and_gender(self):
        """Extract century and gender from the PINFL."""
        return int(self.value[0])

    @property
    def gender(self):
        """Determine gender based on PINFL."""
        return "male" if self.century_and_gender % 2 == 1 else "female"

    @property
    def century(self):
        """Calculate century from PINFL."""
        return (((self.century_and_gender + 1) // 2) + self.BEGINNING_CENTURY) * 100

    @property
    def decade(self):
        """Extract decade from PINFL."""
        return int(self.value[5:7])

    @property
    def year(self):
        """Calculate year from PINFL."""
        return self.century + self.decade

    @property
    def month(self):
        """Extract month from PINFL."""
        return int(self.value[3:5])

    @property
    def day(self):
        """Extract day from PINFL."""
        return int(self.value[1:3])

    @property
    def birth_date(self):
        """Calculate birth date from PINFL."""
        return date(self.year, self.month, self.day) if self.is_valid_date() else None

    @property
    def area_code(self):
        """Extract area code from PINFL."""
        return self.value[7:10]

    @property
    def citizen_serial_number(self):
        """Extract citizen serial number from PINFL."""
        return self.value[10:13]

    @property
    def check_digit(self):
        """Extract check digit from PINFL."""
        return int(self.value[13])

    @property
    def parts(self):
        """Get the parts of the PINFL."""
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
        """Check if the PINFL is valid."""
        return len(self.value) == 14 and (
            self.is_valid_date()
            and self.validate_check_digit()
            and self.validate_area_code()
            and self.validate_citizen_serial_number()
        )

    def is_valid_date(self):
        """Check if the birth date in the PINFL is valid."""
        try:
            date(self.year, self.month, self.day)
            return True
        except ValueError:
            return False

    def validate_check_digit(self):
        """Validate the check digit of the PINFL."""
        return self.check_digit == self.calculate_check_digit()

    def validate_area_code(self):
        """Validate the area code of the PINFL."""
        return int(self.area_code) != 0

    def validate_citizen_serial_number(self):
        """Validate the citizen serial number of the PINFL."""
        return int(self.citizen_serial_number) != 0

    def calculate_check_digit(self):
        """Calculate the check digit of the PINFL."""
        pinfl_numbers = list(map(int, self.value))
        return (
            sum(
                num * weight
                for num, weight in zip(pinfl_numbers[:-1], self.WEIGHT_FUNC)
            )
            % 10
        )
