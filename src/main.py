import os
import time
import random

# membuat karakter
def makeCharacter(name, hp, min_damage, max_damage):
    return {
        "name": name,
        "hp": hp,
        "max_hp": hp,
        "min_damage": min_damage,
        "max_damage": max_damage,
    }

def attack(attacker, target):
    damage = random.randint(attacker['min_damage'], attacker['max_damage'])
    target['hp'] = max(0, target['hp'] - damage)
    return damage

def defend(player):
    recover = random.randint(9, 12)
    new_hp = min(player['max_hp'], player['hp'] + recover)
    selisih = new_hp - player['hp']
    player['hp'] = new_hp
    return selisih

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
    player = makeCharacter(username, hp=100, min_damage=8, max_damage=18)
    enemy = makeCharacter(name="Abyss", hp=100, min_damage=7, max_damage=15)

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

        if choice == "1":
            damage = attack(player, enemy)
            print(f"\n{player['name']} menyerang musuh dengan {damage} Damage")
        elif choice == "2":
            recover = defend(player)
            print(f"\n{player['name']} bertahan memulihkan {recover} HP")
        
        if enemy['hp'] > 0:
            dmg = attack(enemy, player)
            print(f"\n{enemy['name']} membalas serangan dengan {dmg} Damage")

        time.sleep(3)
    
    if player['hp'] > 0 and enemy['hp'] == 0:
        print("\nGAME WIN! Selamat atas kemenangannya!") 
    else:
        print("\nGAME OVER! Silahkan coba lagi!")

if __name__ == "__main__":
    main()