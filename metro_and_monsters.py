from faker import Faker
import file_operations
import random
import os


RUNIC_ALPHABET = {
    'а': 'а͠',
    'б': 'б̋',
    'в': 'в͒͠',
    'г': 'г͒͠',
    'д': 'д̋',
    'е': 'е͠',
    'ё': 'ё͒͠',
    'ж': 'ж͒',
    'з': 'з̋̋͠',
    'и': 'и',
    'й': 'й͒͠',
    'к': 'к̋̋',
    'л': 'л̋͠',
    'м': 'м͒͠',
    'н': 'н͒',
    'о': 'о̋',
    'п': 'п̋͠',
    'р': 'р̋͠',
    'с': 'с͒',
    'т': 'т͒',
    'у': 'у͒͠',
    'ф': 'ф̋̋͠',
    'х': 'х͒͠',
    'ц': 'ц̋',
    'ч': 'ч̋͠',
    'ш': 'ш͒͠',
    'щ': 'щ̋',
    'ъ': 'ъ̋͠',
    'ы': 'ы̋͠',
    'ь': 'ь̋',
    'э': 'э͒͠͠',
    'ю': 'ю̋͠',
    'я': 'я̋',
    'А': 'А͠',
    'Б': 'Б̋',
    'В': 'В͒͠',
    'Г': 'Г͒͠',
    'Д': 'Д̋',
    'Е': 'Е',
    'Ё': 'Ё͒͠',
    'Ж': 'Ж͒',
    'З': 'З̋̋͠',
    'И': 'И',
    'Й': 'Й͒͠',
    'К': 'К̋̋',
    'Л': 'Л̋͠',
    'М': 'М͒͠',
    'Н': 'Н͒',
    'О': 'О̋',
    'П': 'П̋͠',
    'Р': 'Р̋͠',
    'С': 'С͒',
    'Т': 'Т͒',
    'У': 'У͒͠',
    'Ф': 'Ф̋̋͠',
    'Х': 'Х͒͠',
    'Ц': 'Ц̋',
    'Ч': 'Ч̋͠',
    'Ш': 'Ш͒͠',
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠',
    'Ы': 'Ы̋͠',
    'Ь': 'Ь̋',
    'Э': 'Э͒͠͠',
    'Ю': 'Ю̋͠',
    'Я': 'Я̋',
    ' ': ' ',
}


def main():
    folder = 'output/svg/'
    os.makedirs(folder, exist_ok=True)
    faker = Faker('ru-RU')

    for card in range(1, 11):
        card_number = card
        skills = ['Стремительный прыжок',
                  'Электрический выстрел',
                  'Ледяной удар',
                  'Стремительный удар',
                  'Кислотный взгляд',
                  'Тайный побег',
                  'Ледяной выстрел',
                  'Огненный заряд',
        ]
        random_skills = random.sample(skills, 3)
        runic_skills = []
        for element in random_skills:
            skill = ''
            for symbol in element:
                skill += symbol.replace(symbol, RUNIC_ALPHABET[symbol])
            runic_skills.append(skill)

        context = {
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "town": faker.city(),
            "job": faker.job(),

            "strength": random.randint(3, 18),
            "agility": random.randint(3, 18),
            "endurance": random.randint(3, 18),
            "intelligence": random.randint(3, 18),
            "luck": random.randint(3, 18),

            "skill_1": runic_skills[0],
            "skill_2": runic_skills[1],
            "skill_3": runic_skills[2],
        }

        file_operations.render_template("src/charsheet.svg",
                            "{folder}/form-{card_number}.svg".format(folder=folder, card_number=card_number), context)


if __name__ == '__main__':
    main()
