from abc import ABCMeta, abstractmethod

class AbstractTeamFactory(metaclass=ABCMeta):
    """Абстрактная фабрика для создания футбольных команд."""

    @abstractmethod
    def create_barcelona(self):
        pass

    @abstractmethod
    def create_real_madrid(self):
        pass

class FirstTeamFactory(AbstractTeamFactory):
    """Фабрика для создания основных составов футбольных команд"""

    def create_barcelona(self):
        return FirstTeamBarcelona()

    def create_real_madrid(self):
        return FirstTeamRealMadrid()

class YouthTeamFactory(AbstractTeamFactory):
    """Фабрика для создания молодежных составов футбольных команд"""

    def create_barcelona(self):
        return YouthTeamBarcelona()

    def create_real_madrid(self):
        return YouthTeamRealMadrid()

class AbstractTeamRealMadrid(metaclass=ABCMeta):
    """Абстрактная команда Реал Мадрид"""

    @abstractmethod
    def training(self, times_of_day):
        pass

    @abstractmethod
    def match(self, match_place, enemy_team):
        pass

class FirstTeamRealMadrid(AbstractTeamRealMadrid):
    """Основной состав Реал Мадрида"""

    def training(self, times_of_day="утренняя"):
        return ('{} тренировка у основного состава Реал Мадрид'.format(times_of_day))

    def match(self, match_place, enemy_team):
        return ('{} матч основного состава Реал Мадрид с {}'.format(match_place, enemy_team))

class YouthTeamRealMadrid(AbstractTeamRealMadrid):
    """Молодежный состав Реал Мадрида"""

    def training(self, times_of_day="утренняя"):
        return ('{} тренировка у молодежного состава Реал Мадрид'.format(times_of_day))

    def match(self, match_place, enemy_team):
        return ('{} матч молодежного состава Реал Мадрида с '
              'молодежной командой {}'.format(match_place, enemy_team))

class AbstractTeamBarcelona(metaclass=ABCMeta):
    """Абстрактная команда Барселоны"""

    @abstractmethod
    def training(self, times_of_day):
        pass

    @abstractmethod
    def match_with_RM(self, match_place, enemy_team, collaborator: AbstractTeamRealMadrid):
        pass

class FirstTeamBarcelona(metaclass=ABCMeta):
    """Основная команда Барселоны"""

    def training(self, times_of_day="утренняя"):
        return ('{} тренировка у основного состава Барселоны'.format(times_of_day))

    def match_with_RM(self, collaborator: AbstractTeamRealMadrid):
        result = collaborator.match(match_place='Домашний', enemy_team='Барселоной')
        return f'{result}'

class YouthTeamBarcelona(metaclass=ABCMeta):
    """Молодежная команда Барселоны"""

    def training(self, times_of_day="утренняя"):
        return ('{} тренировка у молодежного состава Барселоны'.format(times_of_day))

    def match_with_RM(self, collaborator: AbstractTeamRealMadrid):
        result = collaborator.match(match_place='Домашний', enemy_team='молодежный Барселоны')
        return f'{result}'

barca = FirstTeamFactory().create_barcelona()
print(barca.match_with_RM(FirstTeamRealMadrid()))