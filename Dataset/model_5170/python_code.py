from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class b_Y:

    def __init__(self, label: str, info: str, b_Y: "b_Model" = None):
        self.label = label
        self.info = info
        self.b_Y = b_Y
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def info(self) -> str:
        return self.__info

    @info.setter
    def info(self, info: str):
        self.__info = info

    @property
    def b_Y(self):
        return self.__b_Y

    @b_Y.setter
    def b_Y(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_Y__b_Y", None)
        self.__b_Y = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Model2"):
                opp_val = getattr(old_value, "b_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Model2"):
                opp_val = getattr(value, "b_Model2", None)
                if opp_val is None:
                    setattr(value, "b_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class b_B:

    def __init__(self, id: str, b_B: "b_Model" = None):
        self.id = id
        self.b_B = b_B
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def b_B(self):
        return self.__b_B

    @b_B.setter
    def b_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_b_B__b_B", None)
        self.__b_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "b_Model"):
                opp_val = getattr(old_value, "b_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "b_Model"):
                opp_val = getattr(value, "b_Model", None)
                if opp_val is None:
                    setattr(value, "b_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class b_Model:

    pass