import random

def guess_the_number(range_start, range_end):
    print("Laipni lūdzam spēlē 'Uzmini numuru'!")
    
    target = random.randint(range_start, range_end)
    print(f"Cipars ir paslēpts diapazonā no {range_start} līdz {range_end}. Mēģiniet to uzminēt!")
    
    attempts = 0
    found = False

    while not found:
        try:
            guess = int(input("Ievadiet savu minējumu: "))
            attempts += 1
            if guess > range_end or guess < range_start:
                print("Lūdzu, ievadiet diapazonā derīgu numuru.")
        
            elif guess < target:
                print("Slēptais skaitlis ir lielāks.")
            elif guess > target:
                print("Slēptais skaitlis ir mazāks.")
        
            else:
                found = True
                print(f"Apsveicam! Jūs uzminējāt skaitli {target} {attempts} mēģinājumos.")
        except ValueError:
            print("Lūdzu, ievadiet derīgu skaitli.")

    return attempts


def difficulty_level():
    print("\nIzvēlieties grūtības pakāpi:")
    print("1. Viegli (1-20)")
    print("2. Vidēji (1-50)")
    print("3. Grūti (1-100)")
    
    while True:
        level = input("Ievadiet līmeņa numuru (1, 2 vai 3): ")
        if level == '1':
            return 1, 20
        elif level == '2':
            return 1, 50
        elif level == '3':
            return 1, 100
        else:
            print("Nepareiza izvēle! Mēģiniet vēlreiz.")


def display_statistics(total_games, total_wins, total_attempts):
    print("\n--- Statistika ---")
    print(f"Kopā aizvadītās spēles: {total_games}")
    print(f"Uzvaras: {total_wins}")
    if total_games > 0:
        print(f"Vidējais mēģinājumu skaits vienā spēlē: {total_attempts / total_games:.2f}")
    else:
        print("Nav statistikas datu.")


def main():
    total_games = 0
    total_wins = 0
    total_attempts = 0

    while True:
        print("\n--- Galvenā izvēlne ---")
        print("1. Spēlēt 'Uzmini skaitli'")
        print("2. Apskatīt statistiku")
        print("3. Iziet")
        
        choice = input("Izvēlieties darbību (1-3): ")
        
        if choice == '1':
            range_start, range_end = difficulty_level()
            attempts = guess_the_number(range_start, range_end)
            total_games += 1
            total_wins += 1
            total_attempts += attempts
        elif choice == '2':
            display_statistics(total_games, total_wins, total_attempts)
        elif choice == '3':
            print("Paldies, ka spēlējāt! Uz redzēšanos!")
            break
        else:
            print("Nepareiza izvēle! Mēģiniet vēlreiz.")


if __name__ == "__main__":
    main()