import random
import os

# Тот же самый путь к файлу на диске C
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

print("--- ДОБРО ПОЖАЛОВАТЬ В РЕЖИМ CASINO ---")
print("Здесь нужно выбрать 2 числа от 0 до 10.")
print("Ставка: 5 Niko-Коинов.")
print("(Введи 'q' для трусливого побега)")

while True:
    current_balance = load_balance()
    print(f"\nТвой текущий баланс: {current_balance} Niko-Коинов")
    
    user_input = input("\nВведи ДВА числа через пробел (или 'q' для выхода): ").strip()
    
    if user_input.lower() == 'q':
        print("\nКазино закрыто, все свободны.")
        input("\nНажми Enter, чтобы закрыть окно...")
        break
        
    parts = user_input.split()
    if len(parts) != 2:
        if random.random() < 0.1:
            print("\nНевероятно! Ты тупее обезьяны раз не можешь ввести ДВА числа через пробел!")
        else:
            print("\nУ воды IQ больше чем у тебя. Нужно ввести ровно ДВА числа.")
        print("-------------------------------------------")
        continue
        
    try:
        guess1 = int(parts[0])
        guess2 = int(parts[1])
        
        if not (0 <= guess1 <= 10) or not (0 <= guess2 <= 10):
            print("\nЧисла должны быть от 0 до 10, гений.")
            continue
            
        if current_balance < 5:
            print("\n🚨 БАНКРОТ! У тебя нет 5 коинов для ставки. Иди майни в second.py!")
            print("-------------------------------------------")
            input("Нажми Enter...")
            continue
            
        # Списываем ставку
        current_balance -= 5
        save_balance(current_balance)
        
        win1 = random.randint(0, 10)
        win2 = random.randint(0, 10)
        print(f"Казино загадало: {win1} и {win2}")
        
        if {guess1, guess2} == {win1, win2}:
            print("\n🎉 Фантастика! Ты угадал оба числа!")
            current_balance += 100
            save_balance(current_balance)
            print("Награда: +100 Niko-Коинов!")
        else:
            print("\nМимо! Ты проиграл 5 Niko-Коинов.")
            print("Попробуй еще раз, лудоман.")
            
    except ValueError:
        if random.random() < 0.1:
            print("\nНевероятно! Ты тупее обезьяны раз словил это! Поздравляю!")
        else:
            print("\nУ воды IQ больше чем у тебя. Буквы в казино не принимаются.")
            
    print("\n-------------------------------------------")
    input("Нажми Enter, чтобы продолжить...")
