password = input('Введите пароль: ')


def has_digit(password):
    return any(symbol.isdigit() for symbol in password)


def has_letters(password):
    return any(symbol.isalpha() for symbol in password)


def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password)


def has_lower_letters(password):
    return any(symbol.islower() for symbol in password)


def has_symbols(password):
    return any(not symbol.isalnum() for symbol in password)


def is_very_long(password):
    return len(password) > 12


results_of_checks = [
    has_digit(password),
    has_letters(password),
    has_upper_letters(password),
    has_lower_letters(password),
    has_symbols(password),
    is_very_long(password),
]
score = 0

for result in results_of_checks:
    if result:
        score += 2

if password == '':
    score = 0

print(f'Рейтинг пароля: {score}')
