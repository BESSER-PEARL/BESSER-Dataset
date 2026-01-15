from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class A_A:

    def __init__(self, name: str, A_A: "A_A1" = None):
        self.name = name
        self.A_A = A_A
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def A_A(self):
        return self.__A_A

    @A_A.setter
    def A_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A_A__A_A", None)
        self.__A_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "A_A1"):
                opp_val = getattr(old_value, "A_A1", None)
                if opp_val == self:
                    setattr(old_value, "A_A1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "A_A1"):
                opp_val = getattr(value, "A_A1", None)
                setattr(value, "A_A1", self)

class A_A2:

    def __init__(self, description: str, A_A2: "A_A1" = None):
        self.description = description
        self.A_A2 = A_A2
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def A_A2(self):
        return self.__A_A2

    @A_A2.setter
    def A_A2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A_A2__A_A2", None)
        self.__A_A2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "A_A12"):
                opp_val = getattr(old_value, "A_A12", None)
                if opp_val == self:
                    setattr(old_value, "A_A12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "A_A12"):
                opp_val = getattr(value, "A_A12", None)
                setattr(value, "A_A12", self)

class A_A1:

    def __init__(self, description: str, A_A1: "A_A" = None, A_A12: "A_A2" = None):
        self.description = description
        self.A_A1 = A_A1
        self.A_A12 = A_A12
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def A_A1(self):
        return self.__A_A1

    @A_A1.setter
    def A_A1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A_A1__A_A1", None)
        self.__A_A1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "A_A"):
                opp_val = getattr(old_value, "A_A", None)
                if opp_val == self:
                    setattr(old_value, "A_A", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "A_A"):
                opp_val = getattr(value, "A_A", None)
                setattr(value, "A_A", self)

    @property
    def A_A12(self):
        return self.__A_A12

    @A_A12.setter
    def A_A12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_A_A1__A_A12", None)
        self.__A_A12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "A_A2"):
                opp_val = getattr(old_value, "A_A2", None)
                if opp_val == self:
                    setattr(old_value, "A_A2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "A_A2"):
                opp_val = getattr(value, "A_A2", None)
                setattr(value, "A_A2", self)
