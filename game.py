import random
# Lista de palabras posibles
words = ['python', 'programación', 'computadora', 'código', 'desarrollo',
'inteligencia']

# Lista vocales
vocales = ['a','e','i','o','u']

# Elegir una palabra al azar
secret_word = random.choice(words)

# Contador de fallos
cant_fallos = 0

# Lista para almacenar las letras adivinadas
guessed_letters = []

print('¡Bienvenido al juego de adivinanzas!')
# Elige el nivel de dificultad
word_displayed = ''
seguir = False
while not seguir:
    nivel_dificultad = input('¿Qué nivel de dificultad desea elegir? f|m|d: ').lower()
    match nivel_dificultad:
        case 'f':
            for letter in secret_word:
                if letter in vocales:
                    word_displayed += letter
                else:
                    word_displayed += '_'
            seguir = True
        case 'm':
            contador = 0
            for letter in secret_word:
                if contador == 0 or contador == (len(secret_word) - 1):
                    word_displayed += letter
                else:
                    word_displayed += '_'
                contador += 1
            seguir = True
        case 'd':
            word_displayed += '_' * len(secret_word)
            seguir = True
        case _:
            print('El nivel de dificultad que has ingresado no existe, por favor inténtalo de nuevo')

print('Estoy pensando en una palabra. ¿Puedes adivinar cuál es?\n')
# Mostrar la palabra parcialmente adivinada
print(f'Palabra: {word_displayed}')

while cant_fallos < 5:
    # Pedir al jugador que ingrese una letra
    letter = input('Ingresa una letra: ').lower()
    while letter == '':
        print('Valor inválido, por favor ingrese de nuevo')
        letter = input('Ingresa una letra: ').lower()

    # Verificar si la letra ya ha sido adivinada
    if letter in guessed_letters:
        print('Ya has intentado con esa letra. Prueba con otra.')
        continue

    # Agregar la letra a la lista de letras adivinadas
    guessed_letters.append(letter)
    
    # Verificar si la letra está en la palabra secreta
    if letter in secret_word:
        print('¡Bien hecho! La letra está en la palabra.')
    else:
        print('Lo siento, la letra no está en la palabra.')
        cant_fallos += 1
    print(f'Cantidad de fallos: {cant_fallos}\n')

    # Mostrar la palabra parcialmente adivinada
    letters = []
    if nivel_dificultad == 'f':
        for letter in secret_word:
            if letter in guessed_letters or letter in word_displayed:
                letters.append(letter)
            else:
                letters.append('_')
    elif nivel_dificultad == 'm':
        for letter in secret_word:
            if letter in guessed_letters or letter in word_displayed:
                letters.append(letter)
            else:
                letters.append('_')
    else:
        for letter in secret_word:
            if letter in guessed_letters:
                letters.append(letter)
            else:
                letters.append('_')

    word_displayed = ''.join(letters)
    print(f'Palabra: {word_displayed}')

    # Verificar si se ha adivinado la palabra completa
    if word_displayed == secret_word:
        print(f'¡Felicidades! Has adivinado. La palabra secreta era: {secret_word}')
        break
    elif cant_fallos == 5:
        print(f'¡Oh no! Has agotado tus intentos.')
        print(f'La palabra secreta era: {secret_word}')