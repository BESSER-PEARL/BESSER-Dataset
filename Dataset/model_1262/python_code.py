from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class hutnArticleFamilies_Person:

    def __init__(self, name: str, hutnArticleFamilies_Person: "hutnArticleFamilies_Family" = None):
        self.name = name
        self.hutnArticleFamilies_Person = hutnArticleFamilies_Person
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def hutnArticleFamilies_Person(self):
        return self.__hutnArticleFamilies_Person

    @hutnArticleFamilies_Person.setter
    def hutnArticleFamilies_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hutnArticleFamilies_Person__hutnArticleFamilies_Person", None)
        self.__hutnArticleFamilies_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hutnArticleFamilies_Family"):
                opp_val = getattr(old_value, "hutnArticleFamilies_Family", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hutnArticleFamilies_Family"):
                opp_val = getattr(value, "hutnArticleFamilies_Family", None)
                if opp_val is None:
                    setattr(value, "hutnArticleFamilies_Family", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class hutnArticleFamilies_Family:

    def __init__(self, name: str, nuclear: bool, migrant: bool, lotteryNumbers: int, hutnArticleFamilies_Family: set["hutnArticleFamilies_Person"] = None, hutnArticleFamilies_Family3: "hutnArticleFamilies_Family" = None, hutnArticleFamilies_Family1: set["hutnArticleFamilies_Family"] = None):
        self.name = name
        self.nuclear = nuclear
        self.migrant = migrant
        self.lotteryNumbers = lotteryNumbers
        self.hutnArticleFamilies_Family = hutnArticleFamilies_Family if hutnArticleFamilies_Family is not None else set()
        self.hutnArticleFamilies_Family3 = hutnArticleFamilies_Family3
        self.hutnArticleFamilies_Family1 = hutnArticleFamilies_Family1 if hutnArticleFamilies_Family1 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def migrant(self) -> bool:
        return self.__migrant

    @migrant.setter
    def migrant(self, migrant: bool):
        self.__migrant = migrant

    @property
    def lotteryNumbers(self) -> int:
        return self.__lotteryNumbers

    @lotteryNumbers.setter
    def lotteryNumbers(self, lotteryNumbers: int):
        self.__lotteryNumbers = lotteryNumbers

    @property
    def nuclear(self) -> bool:
        return self.__nuclear

    @nuclear.setter
    def nuclear(self, nuclear: bool):
        self.__nuclear = nuclear

    @property
    def hutnArticleFamilies_Family1(self):
        return self.__hutnArticleFamilies_Family1

    @hutnArticleFamilies_Family1.setter
    def hutnArticleFamilies_Family1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hutnArticleFamilies_Family__hutnArticleFamilies_Family1", None)
        self.__hutnArticleFamilies_Family1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hutnArticleFamilies_Family3"):
                    opp_val = getattr(item, "hutnArticleFamilies_Family3", None)
                    
                    if opp_val == self:
                        setattr(item, "hutnArticleFamilies_Family3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hutnArticleFamilies_Family3"):
                    opp_val = getattr(item, "hutnArticleFamilies_Family3", None)
                    
                    setattr(item, "hutnArticleFamilies_Family3", self)
                    

    @property
    def hutnArticleFamilies_Family(self):
        return self.__hutnArticleFamilies_Family

    @hutnArticleFamilies_Family.setter
    def hutnArticleFamilies_Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hutnArticleFamilies_Family__hutnArticleFamilies_Family", None)
        self.__hutnArticleFamilies_Family = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hutnArticleFamilies_Person"):
                    opp_val = getattr(item, "hutnArticleFamilies_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "hutnArticleFamilies_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hutnArticleFamilies_Person"):
                    opp_val = getattr(item, "hutnArticleFamilies_Person", None)
                    
                    setattr(item, "hutnArticleFamilies_Person", self)
                    

    @property
    def hutnArticleFamilies_Family3(self):
        return self.__hutnArticleFamilies_Family3

    @hutnArticleFamilies_Family3.setter
    def hutnArticleFamilies_Family3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hutnArticleFamilies_Family__hutnArticleFamilies_Family3", None)
        self.__hutnArticleFamilies_Family3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hutnArticleFamilies_Family1"):
                opp_val = getattr(old_value, "hutnArticleFamilies_Family1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hutnArticleFamilies_Family1"):
                opp_val = getattr(value, "hutnArticleFamilies_Family1", None)
                if opp_val is None:
                    setattr(value, "hutnArticleFamilies_Family1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
