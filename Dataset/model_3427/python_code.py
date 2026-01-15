from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class people_Person:

    def __init__(self, name: str, people_Person: "people_Model" = None):
        self.name = name
        self.people_Person = people_Person
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def people_Person(self):
        return self.__people_Person

    @people_Person.setter
    def people_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_people_Person__people_Person", None)
        self.__people_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "people_Model"):
                opp_val = getattr(old_value, "people_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "people_Model"):
                opp_val = getattr(value, "people_Model", None)
                if opp_val is None:
                    setattr(value, "people_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class people_Model:

    pass