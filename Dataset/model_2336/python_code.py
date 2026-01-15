from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class persons_Person:

    def __init__(self, name: str, persons_Person: "persons_PersonGroup" = None):
        self.name = name
        self.persons_Person = persons_Person
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def persons_Person(self):
        return self.__persons_Person

    @persons_Person.setter
    def persons_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persons_Person__persons_Person", None)
        self.__persons_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persons_PersonGroup"):
                opp_val = getattr(old_value, "persons_PersonGroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persons_PersonGroup"):
                opp_val = getattr(value, "persons_PersonGroup", None)
                if opp_val is None:
                    setattr(value, "persons_PersonGroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class persons_PersonGroup:

    pass