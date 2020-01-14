from abc import ABCMeta, abstractmethod

class Brewery(metaclass=ABCMeta):
    """Суперкласс пивоваренного завода"""
    def __init__(self, grade):
        self.grade = grade

    @abstractmethod
    def factory_method(self):
        pass

    def brewing_beer(self):
        self.beer = self.factory_method()
        print('Пиво сорта {} сделано из {}, имеет {} цвет, способ брожения - {}'.format(self.beer['grade'],
                                                                                        self.beer['raw_material'],
                                                                                        self.beer['color'],
                                                                                        self.beer['fermentation_method']))
        return self.beer

    def sale_beer(self):
        pass

class Baltica(Brewery):
    """Пивоваренный завод Балтика, производящий светлый лагер"""
    def factory_method(self):
        lager = Lager()
        return lager.parameters_brewing(grade = 'лагер', raw_material = 'ячмень', color = 'светлое',
                                        fermentation_method = 'низовое брожение')

class Paulaner(Brewery):
    """Пивоваренный завод Пауланер, производящий пшеничное пиво"""
    def factory_method(self):
        wheat_beer = WheatBeer()
        return wheat_beer.parameters_brewing(grade = 'пшеничное пиво', raw_material = 'пшеница', color = 'светлое',
                                        fermentation_method = 'верховое брожение')

class Beer(metaclass=ABCMeta):
    """Суперкласс пиво"""
    @abstractmethod
    def parameters_brewing(self, **kwargs):
        pass

class Lager(Beer):
    """Сорт лагер"""
    def parameters_brewing(self, **kwargs):
        self.params = kwargs
        return self.params

class WheatBeer(Beer):
    """Сорт пшеничное пиво"""
    def parameters_brewing(self, **kwargs):
        self.params = kwargs
        return self.params


paulaner = Paulaner("wheat beer")
paulaner.brewing_beer()