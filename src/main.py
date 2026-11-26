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

# menampilkan hp terkini
def showHP(player, enemy):
    print(f"\n{player['name']}: {player['hp']}/{player['max_hp']} HP")
    print(f"{enemy['name']}: {enemy['hp']}/{enemy['max_hp']} HP")

def main():
    print("Heroes Battlefield")
    print("------------------")

    # opsi untuk input username custom atau memakai default
    username = input("masukkan nama karakter: ") or "Kevin"

    # input data player dan enemy
    player = makeCharacter(username, hp=100, min_damage=5, max_damage=14)
    enemy = makeCharacter(name="abyss", hp=100, min_damage=4, max_damage=12)

    os.system('cls')
    print(f"\n{player['name']} akan menghadapi {enemy['name']}!")
    print("Pertandingan dimulai!")
    time.sleep(3)

    # Hitung mundur di bawah teks pertama
    for i in range(5, 0, -1):
        os.system('cls')
        print(f"\nMenghubungkan ke server dalam {i}...", end="\r")
        time.sleep(1)

    # Bersihkan layar setelah hitungan selesai
    os.system('cls')

    print("Status Game")
    print("===========")
    showHP(player, enemy)

if __name__ == "__main__":
    main()