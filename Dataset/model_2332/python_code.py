from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Persons_Person:

    def __init__(self, name: str, ID: int, Persons_Person: "Persons_PersonContainer" = None):
        self.name = name
        self.ID = ID
        self.Persons_Person = Persons_Person
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ID(self) -> int:
        return self.__ID

    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def Persons_Person(self):
        return self.__Persons_Person

    @Persons_Person.setter
    def Persons_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Persons_Person__Persons_Person", None)
        self.__Persons_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Persons_PersonContainer"):
                opp_val = getattr(old_value, "Persons_PersonContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Persons_PersonContainer"):
                opp_val = getattr(value, "Persons_PersonContainer", None)
                if opp_val is None:
                    setattr(value, "Persons_PersonContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Persons_PersonContainer:

    pass