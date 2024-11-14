from random import randint, choice

class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.health} damage: {self.damage}'


class Witcher(GameEntity):
    def __init__(self, name, health, damage, revive_ability):
        super().__init__(name, health, damage)
        self.__revive_ability = revive_ability

    @property
    def revive_ability(self):
        return self.__revive_ability

    @revive_ability.setter
    def revive_ability(self, value):
        self.__revive_ability = value

    def revive_first_dead_hero(self, heroes):
        for hero in heroes:
            if hero != self and hero.health <= 0:  # Проверяем на погибшего героя
                hero.health = 100  # Воскрешаем героя
                print(f"{self.name} оживил {hero.name}, но погиб сам!")
                self.health = 0  # Witcher погибает после воскрешения
                return

    def __str__(self):
        return f"{self.__name}, health: {self.__health}, damage: {self.__damage}, revive: {self.__revive_ability}"

class Magic(GameEntity):
    def __init__(self, name, health, damage, increase_attack):
        super().__init__(name, health, damage, "INCREASE")
        self.__increase_attack = increase_attack

    def apply_super_power(self, boss, heroes):
        pass
        # TODO Here will be implementation of INCREASING
    def increase_attack(self, heroes):
        for hero in heroes:
            hero.damage += self.increase_attack
            return f"урон {hero.name} увеличен на {self.increase_attack}, новый урон: {hero.damage}"