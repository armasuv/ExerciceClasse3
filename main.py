import random

def nombre():
    random1 = random.randint(1, 6)
    random2 = random.randint(1, 6)
    random3 = random.randint(1, 6)
    random4 = random.randint(1, 6)

    list = [random1, random2, random3, random4]
    list.sort()
    list.pop(0)
    return list[0] + list[1] + list[2]

class NPC:
    def __init__(self, nom, race, espece, profession):
       self.Force = nombre()
       self.Agilitie = nombre()
       self.Constitution = nombre()
       self.Intelligence = nombre()
       self.Sagesse = nombre()
       self.Charisme = nombre()
       self.classe_armure = random.randint(1,2)
       self.nom = nom
       self.race = race
       self.espece = espece
       self.points_vie = random.randint(1, 20)
       self.profession = profession

    def caracteristique(self):
        print("\nNom:", self.nom)
        print("Force:", self.Force)
        print("Agilite:", self.Agilite)
        print("Constitution:", self.Constitution)
        print("Intelligence:", self.Intelligence)
        print("Sagesse:", self.Sagesse)
        print("Charisme:", self.Charisme)
        print("Race:", self.race)
        print("Espece:", self.espece)
        print("Points de vie:", self.points_vie)
        print("Profession:", self.profession)

class Hero(NPC):
    def attaquer(self, cible):
        attaque = random.randint(1.20)
        if attaque == 20:
            dommages_taken = random.randint(1, 8)
            cible.encasser_dommages(dommages_taken)
        elif attaque == 1:
            print("Votre attaque n'as pas marché.")
        else:
            if attaque > cible.classe_armure:
                dommages_taken = random.randint(1.6)
                cible.encasser_dommages(dommages_taken)

    def encasser_dommages(self, dommages):
        self.points_vie -= (dommages - self.classe_armure)
class Kobold(NPC):
    def attaquer(self, cible):
        attaque = random.randint(1, 20)
        if attaque == 20:
            dommages_taken = random.randint(1, 8)
            cible.encasser_dommages(dommages_taken)
        elif attaque == 1:
            print("Votre attaque n'a aucun effet")
        else:
            if attaque > cible.classe_armure:
                dommages_taken = random.randint(1, 6)
                cible.encasser_dommages(dommages_taken)

    def encasser_dommages(self, dommages):
        self.points_vie -= (dommages - self.classe_armure)
