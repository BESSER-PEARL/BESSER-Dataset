from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class personDsl_Person:

    def __init__(self, ID: int, name: str, personDsl_Person: "personDsl_PersonContainer" = None):
        self.ID = ID
        self.name = name
        self.personDsl_Person = personDsl_Person
        
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
    def personDsl_Person(self):
        return self.__personDsl_Person

    @personDsl_Person.setter
    def personDsl_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_personDsl_Person__personDsl_Person", None)
        self.__personDsl_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "personDsl_PersonContainer"):
                opp_val = getattr(old_value, "personDsl_PersonContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "personDsl_PersonContainer"):
                opp_val = getattr(value, "personDsl_PersonContainer", None)
                if opp_val is None:
                    setattr(value, "personDsl_PersonContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class personDsl_PersonContainer:

    pass