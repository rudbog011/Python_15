def update_user_word(secret_word, user_word, char):
    new_user_word = ''
    for i in range(len(secret_word)):
        if secret_word[i] == char:
            new_user_word += char
        else:
            new_user_word += user_word[i]
    return new_user_word
def game():
    count = 0
    secret_word = 'академия'
    user_word = '********'
    letters = ''
    print(user_word)
    while user_word != secret_word:
        print('Введите букву:')
        user_char = input()
        
        if len(user_char) != 1:
            continue
        elif ord(user_char) < 1040 or ord(user_char) > 1103:
            continue
        elif user_char in letters:
            print('Такая буква уже была')
            continue

        count += 1
        letters += user_char
        new_user_word = update_user_word(secret_word, user_word, user_char)
        if user_word == new_user_word:
            print('К сожалению, такой буквы нет в слове')
        else:
            print('Поздравляем, такая буква есть в слове')
        user_word = new_user_word
        print(user_word)

        
    print('Ура, вы угадали загаданное слово, за', count, 'попыток.')
    print('Вы хотите ещё поиграть? (Да/Нет)')
    query = input()
    if query == 'Да':
        game()
game()
