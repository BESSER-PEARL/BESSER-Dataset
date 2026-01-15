from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Original_Metamodel_D:

    pass
class Original_Metamodel_C:

    def __init__(self, propertyC: str):
        self.propertyC = propertyC
        
    @property
    def propertyC(self) -> str:
        return self.__propertyC

    @propertyC.setter
    def propertyC(self, propertyC: str):
        self.__propertyC = propertyC

class Original_Metamodel_B:

    def __init__(self, propertyB: str, Original_Metamodel_B: "Original_Metamodel_A" = None):
        self.propertyB = propertyB
        self.Original_Metamodel_B = Original_Metamodel_B
        
    @property
    def propertyB(self) -> str:
        return self.__propertyB

    @propertyB.setter
    def propertyB(self, propertyB: str):
        self.__propertyB = propertyB

    @property
    def Original_Metamodel_B(self):
        return self.__Original_Metamodel_B

    @Original_Metamodel_B.setter
    def Original_Metamodel_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Original_Metamodel_B__Original_Metamodel_B", None)
        self.__Original_Metamodel_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Original_Metamodel_A"):
                opp_val = getattr(old_value, "Original_Metamodel_A", None)
                if opp_val == self:
                    setattr(old_value, "Original_Metamodel_A", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Original_Metamodel_A"):
                opp_val = getattr(value, "Original_Metamodel_A", None)
                setattr(value, "Original_Metamodel_A", self)

class Original_Metamodel_A:

    pass