from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class model_IPersonList:

    pass
class model_IPerson:

    def __init__(self, firstName: str, model_IPerson: "model_IPersonList" = None):
        self.firstName = firstName
        self.model_IPerson = model_IPerson
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def model_IPerson(self):
        return self.__model_IPerson

    @model_IPerson.setter
    def model_IPerson(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_IPerson__model_IPerson", None)
        self.__model_IPerson = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_IPersonList"):
                opp_val = getattr(old_value, "model_IPersonList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_IPersonList"):
                opp_val = getattr(value, "model_IPersonList", None)
                if opp_val is None:
                    setattr(value, "model_IPersonList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
