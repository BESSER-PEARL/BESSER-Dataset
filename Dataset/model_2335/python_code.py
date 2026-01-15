from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class PersonsRegister_Person:

    def __init__(self, lastName: str, identity: str, firstName: str, PersonsRegister_Person: "PersonsRegister_PersonsRegister" = None):
        self.lastName = lastName
        self.identity = identity
        self.firstName = firstName
        self.PersonsRegister_Person = PersonsRegister_Person
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def identity(self) -> str:
        return self.__identity

    @identity.setter
    def identity(self, identity: str):
        self.__identity = identity

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def PersonsRegister_Person(self):
        return self.__PersonsRegister_Person

    @PersonsRegister_Person.setter
    def PersonsRegister_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonsRegister_Person__PersonsRegister_Person", None)
        self.__PersonsRegister_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PersonsRegister_PersonsRegister"):
                opp_val = getattr(old_value, "PersonsRegister_PersonsRegister", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PersonsRegister_PersonsRegister"):
                opp_val = getattr(value, "PersonsRegister_PersonsRegister", None)
                if opp_val is None:
                    setattr(value, "PersonsRegister_PersonsRegister", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PersonsRegister_PersonsRegister:

    pass