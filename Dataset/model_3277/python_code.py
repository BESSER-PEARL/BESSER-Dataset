from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class data_Variable:

    def __init__(self, id: str, data_Variable: "data_Variables" = None):
        self.id = id
        self.data_Variable = data_Variable
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def data_Variable(self):
        return self.__data_Variable

    @data_Variable.setter
    def data_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_data_Variable__data_Variable", None)
        self.__data_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "data_Variables"):
                opp_val = getattr(old_value, "data_Variables", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data_Variables"):
                opp_val = getattr(value, "data_Variables", None)
                if opp_val is None:
                    setattr(value, "data_Variables", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class data_Variables:

    pass