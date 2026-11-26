def makeCharacter(name, hp, min_damage, max_damage):
    return {
        "name": name,
        "hp": hp,
        "max_hp": hp,
        "min_damage": min_damage,
        "max_damage": max_damage,
    }

def main():
    print("Heroes Battlefield")
    print("------------------")

    username = input("masukkan nama karakter: ") or "Kevin"

    player = makeCharacter(username, hp=100, min_damage=5, max_damage=14)
    enemy = makeCharacter(name="abyss", hp=100, min_damage=4, max_damage=12)

if __name__ == "__main__":
    main()