class Spell:
    def __init__(self, heal=0, rage=0):
        self.heal = heal
        self.rage = rage
    
    def deployheal(self, trooparray):
        for troop in trooparray:
            if(troop.alive):
                troop.health = troop.health + troop.maxhealth * 50 / 100
                if troop.health > troop.maxhealth:
                    troop.health = troop.maxhealth

    # def deploy()

    # def rage(self, troop):
    #     troop.rage = troop.rage + troop.maxrage * 50 / 100
    #     if troop.rage > troop.maxrage:
    #         troop.rage = troop.maxrage

    def deployrage(self, time):
        time = time/2
        return time