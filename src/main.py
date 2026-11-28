import os
import time
import random

# variasi musuh dan kemampuannya
monsters = [
    {"name":"Guard","hp":80,"min_damage":4,"max_damage":13},
    {"name":"Spectator","hp":95,"min_damage":7,"max_damage":15},
    {"name":"Commander","hp":110,"min_damage":9,"max_damage":17},
]

# membuat karakter
def makeCharacter(name, hp, min_damage, max_damage, potion=0):
    return {
        "name": name,
        "hp": hp,
        "max_hp": hp,
        "min_damage": min_damage,
        "max_damage": max_damage,
        "potion": potion,
    }

# fungsi untuk fitur serangan dan memberikan damage secara acak
def attack(attacker, target):
    damage = random.randint(attacker['min_damage'], attacker['max_damage'])
    target['hp'] = max(0, target['hp'] - damage)
    return damage

# fungsi untuk fitur bertahan dan memulihkan HP secara acak
def defend(player):
    recover = random.randint(9, 12)
    new_hp = min(player['max_hp'], player['hp'] + recover)
    selisih = new_hp - player['hp']
    player['hp'] = new_hp
    return selisih

# fungsi untuk fitur potion, ada batasnya dan memulihkan 30 HP
def drink_potion(player):
    if player['potion'] <= 0:
        return None
    player['potion'] -= 1
    new_hp = min(player['max_hp'], player['hp'] + 30)
    selisih = new_hp - player['hp']
    player['hp'] = new_hp
    return selisih

# fungsi untuk user action choice
def makeChoice() :
    while True:
        print("\nPilih Aksi:")
        print("1. Attack")
        print("2. Defend")
        print("3. Drink Potion (3x) +30 HP")
        choice = input("> ").strip()
        if choice in ["1", "2", "3"]:
            return choice
        print("Input yang anda masukkan salah!")

# menampilkan hp terkini
def showHP(player, enemy):
    print(f"\n{player['name']}: {player['hp']}/{player['max_hp']} HP")
    print(f">> Potion [{player['potion']}/3]")
    print(f"{enemy['name']}: {enemy['hp']}/{enemy['max_hp']} HP")

def main():
    os.system('cls')
    print("Heroes Battlefield")
    print("------------------")

    # opsi untuk input username custom atau memakai default
    username = input("Masukkan nama karakter: ").strip() or "Player"

    # input data player dan enemy
    player = makeCharacter(username, hp=100, min_damage=8, max_damage=18, potion=3)
    # mengacak data enemy dari list
    enemy_list = random.choice(monsters)
    enemy = makeCharacter(
        enemy_list['name'], 
        enemy_list['hp'], 
        enemy_list['min_damage'], 
        enemy_list['max_damage'],
        )

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

    # selama hp player dan enemy lebih dari nol maka game berjalan
    while player['hp'] > 0 and enemy['hp'] > 0:
        os.system("cls")
        print("Arena Pertarungan")
        print("=================")
        
        showHP(player, enemy)
        choice = makeChoice()

        # berdasarkan choice akan ada beberapa kondisi
        if choice == "1":
            damage = attack(player, enemy)
            print(f"\n{player['name']} menyerang musuh dengan {damage} Damage")
        elif choice == "2":
            recover = defend(player)
            print(f"\n{player['name']} bertahan memulihkan {recover} HP")
        elif choice == "3":
            # jika hp penuh tidak bisa pakai potion
            if player['hp'] == player['max_hp']:
                print("\nHP masih penuh, silahkan coba aksi lainnya")
                time.sleep(2)
                continue
            # jika potion lebih dari nol
            if player['potion'] > 0:
                # jika hp lebih dari 70 akan ada warning terkait penggunaan potion
                if player['hp'] > 70:
                    potion_potencial = player['max_hp'] - player['hp']
                    print("\n[Warning]")
                    print(f"Hanya akan memulihkan {potion_potencial}/30 HP")
                    # opsi untuk melanjutkan atau berhenti menggunakan potion
                    potion_decision = input("Ingin pakai potion [y/n]: ")
                    if potion_decision != "y":
                        print("\nPenggunaan potion dibatalkan!")
                        time.sleep(2)
                        continue
            # memanggil fungsi potion
            recover = drink_potion(player)
            # jika potion habis
            if recover == None:
                print("\nPotion Habis! Silahkan coba aksi lainnya!")
                time.sleep(2)
                continue
            # jika potion berhasil digunakan
            print(f"\nMenggunakan 1 potion dan memulihkan {recover} HP")

        # musuh akan terus menyerang selama hp nya lebih dari 0
        if enemy['hp'] > 0:
            dmg = attack(enemy, player)
            print(f"\n{enemy['name']} membalas serangan dengan {dmg} Damage")
            
        time.sleep(3)
    
    # menang jika hp player lebih dari 0 dan hp enemy 0, kalah jika sebaliknya
    if player['hp'] > 0 and enemy['hp'] == 0:
        print(f"\nGAME WIN!\n{player['name']} berhasil menang!") 
    else:
        print(f"\nGAME OVER!\n{player['name']} dikalahkan dan {enemy['name']} menang!")

if __name__ == "__main__":
    main()