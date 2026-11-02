import random
import os

# Путь к файлу сохранения на диске C в папке пользователя
SAVE_PATH = os.path.join(os.path.expanduser("~"), ".sapg_save.txt")

def load_balance():
    if os.path.exists(SAVE_PATH):
        try:
            with open(SAVE_PATH, "r") as f:
                return int(f.read().strip())
        except:
            return 0
    return 0

def save_balance(val):
    try:
        with open(SAVE_PATH, "w") as f:
            f.write(str(val))
    except:
        pass

coins = load_balance()
clicks = 0

print("--- ДОБРО ПОЖАЛОВАТЬ В КЛИКЕР СИЗИФА ---")
print("Нажимай ENTER, чтобы майнить Niko-Коины.")
print(f"Сохранение привязано к диску C: ({SAVE_PATH})")
print("(Введи 'q' для выхода)")

while True:
    user_input = input(f"\nБаланс: {coins} Niko-Коинов | Нажми ENTER, чтобы кликнуть: ").strip()

    if user_input.lower() == 'q':
        save_balance(coins)
        print(f"\nИгра окончена! Твой баланс сохранен: {coins} Niko-Коинов.")
        input("\nНажми Enter для закрытия окна...")
        break

    clicks += 1
    
    if random.random() < 0.05 and coins > 0:
        coins = 0
        save_balance(coins)
        print("\n🚨 КРИЗИС! Камень Сизифа покатился вниз. Твой баланс сгорел.")
        print("У воды всё еще больше IQ, раз ты надеялся сохранить эти коины.")
        print("-------------------------------------------")
        continue

    coins += 1
    save_balance(coins)
    print(f"+1 Niko-Коин! Всего кликов: {clicks}")
