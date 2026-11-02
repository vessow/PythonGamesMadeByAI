import random

# Запускаем бесконечный цикл игры
while True:
    print("\n--- ДОБРО ПОЖАЛОВАТЬ В РЕЖИМ NORMAL ---")
    print("Угадай число от 0 до 10 и получи... абсолютно НИЧЕГО.")
    print("(Введи 'q' для выхода из игры)")

    secret_number = random.randint(0, 10)

    user_input = input("\nВведи свою цифру: ").strip()

    # Проверяем, не хочет ли игрок выйти
    if user_input.lower() == 'q':
        print("\nПока, лудоман! Возвращайся за своим НИЧЕГО.")
        input("\nНажми Enter, чтобы закрыть окно...")
        break

    try:
        user_guess = int(user_input)
        
        if user_guess == secret_number:
            print("\nНе удивительно.")
            print("Награда: 0 рублей 00 копеек. Чистый кайф.")
        else:
            print(f"\nМимо! Правильно было {secret_number}.")
            print("Попробуй еще раз, лудоман.")
            
    except ValueError:
        if random.random() < 0.1:
            print("\nНевероятно! Ты тупее обезьяны раз словил это! Поздравляю!")
        else:
            print("\nУ воды IQ больше чем у тебя.")

    # Небольшая пауза между раундами, чтобы экран не засорялся мгновенно
    print("\n-------------------------------------------")
    input("Нажми Enter, чтобы начать следующий раунд...")