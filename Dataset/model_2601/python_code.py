from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class model_Person:

    def __init__(self, firstName: str, model_Person: "model_PersonList" = None, model_Person2: "model_Root" = None):
        self.firstName = firstName
        self.model_Person = model_Person
        self.model_Person2 = model_Person2
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def model_Person(self):
        return self.__model_Person

    @model_Person.setter
    def model_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Person__model_Person", None)
        self.__model_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PersonList"):
                opp_val = getattr(old_value, "model_PersonList", None)
                if opp_val == self:
                    setattr(old_value, "model_PersonList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PersonList"):
                opp_val = getattr(value, "model_PersonList", None)
                setattr(value, "model_PersonList", self)

    @property
    def model_Person2(self):
        return self.__model_Person2

    @model_Person2.setter
    def model_Person2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Person__model_Person2", None)
        self.__model_Person2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Root"):
                opp_val = getattr(old_value, "model_Root", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Root"):
                opp_val = getattr(value, "model_Root", None)
                if opp_val is None:
                    setattr(value, "model_Root", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_Root:

    pass
class model_PersonList:

    pass