import os
import time

# membuat karakter
def makeCharacter(name, hp, min_damage, max_damage):
    return {
        "name": name,
        "hp": hp,
        "max_hp": hp,
        "min_damage": min_damage,
        "max_damage": max_damage,
    }

def makeChoice() :
    while True:
        print("\nPilih Aksi:")
        print("1. Attack")
        print("2. Defend")
        choice = input("> ").strip()
        if choice in ["1", "2"]:
            return choice
        print("Input yang anda masukkan salah!")

# menampilkan hp terkini
def showHP(player, enemy):
    print(f"\n{player['name']}: {player['hp']}/{player['max_hp']} HP")
    print(f"{enemy['name']}: {enemy['hp']}/{enemy['max_hp']} HP")

def main():
    os.system('cls')
    print("Heroes Battlefield")
    print("------------------")

    # opsi untuk input username custom atau memakai default
    username = input("Masukkan nama karakter: ").strip() or "Player"

    # input data player dan enemy
    player = makeCharacter(username, hp=100, min_damage=5, max_damage=14)
    enemy = makeCharacter(name="Abyss", hp=100, min_damage=4, max_damage=12)

    os.system('cls')
    print(f"\n{player['name']} akan menghadapi {enemy['name']}!")
    print("Pertandingan segera dimulai!")
    time.sleep(3)

    # Hitung mundur di bawah teks pertama
    for i in range(5, 0, -1):
        os.system('cls')
        print(f"\nMenghubungkan ke server dalam {i}...", end="\r")
        time.sleep(1)

    # Bersihkan layar setelah hitungan selesai
    os.system('cls')

    while player['hp'] > 0 and enemy['hp'] > 0:
        os.system("cls")
        print("Arena Pertarungan")
        print("=================")
        
        showHP(player, enemy)
        choice = makeChoice()
        time.sleep(3)


if __name__ == "__main__":
    main()