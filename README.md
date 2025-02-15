# Telegram Bot for PINFL Analysis

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

This project is a Telegram bot that analyzes the PINFL (Personal Identification Number for Individual Taxpayer) entered by the user and reports its validity, as well as its birth date, region code, and other parameters.

## Why is this project needed?

PINFL (PINFL) is a unique identification number used in several countries to identify citizens. This project is intended for processing and analyzing PINFL to ensure its correctness and provide information about the birth date and other data contained in this number.

## How to use?

1. Navigate to the project directory.

2. Copy ```.env.example ``` to ```.env ```:
```shell
$ cp .env.example .env
```

3. Update all values in ```.env ```:
```shell
$ vim .env
```

4. Run ```docker-compose up -d```

## Additional features

1. The bot pre-checks the entered text for the presence of only digits and a length of at least 14 characters. If the entered text does not meet these criteria, the bot will send a message with the corresponding warning.

