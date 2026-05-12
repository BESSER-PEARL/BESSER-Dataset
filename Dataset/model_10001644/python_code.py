from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Discription:

    pass


class Payment:

    pass


class User:

    pass


class Delivery:

    pass


class Order:

    def __init__(self, ID_: int, Type_: str, Size_: int, Quantity: int, myClass0: "Delivery" = None, myClass22: "User" = None, myClass34: "Payment" = None, myClass48: "Discription" = None):
        self.ID_ = ID_
        self.Type_ = Type_
        self.Size_ = Size_
        self.Quantity = Quantity
        self.myClass0 = myClass0
        self.myClass22 = myClass22
        self.myClass34 = myClass34
        self.myClass48 = myClass48
        
        pass
    @property
    def Size_(self):
        return self.__Size_
    @Size_.setter
    def Size_(self, Size_: int):
        self.__Size_ = Size_

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity

    @property
    def Type_(self):
        return self.__Type_
    @Type_.setter
    def Type_(self, Type_: str):
        self.__Type_ = Type_

    @property
    def ID_(self):
        return self.__ID_
    @ID_.setter
    def ID_(self, ID_: int):
        self.__ID_ = ID_

    @property
    def myClass22(self):
        return self.__myClass22
    @myClass22.setter
    def myClass22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__myClass22", None)
        self.__myClass22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order3"):
                opp_val = getattr(old_value, "order3", None)
                if opp_val == self:
                    setattr(old_value, "order3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order3"):
                opp_val = getattr(value, "order3", None)
                setattr(value, "order3", self)

    @property
    def myClass48(self):
        return self.__myClass48
    @myClass48.setter
    def myClass48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__myClass48", None)
        self.__myClass48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order9"):
                opp_val = getattr(old_value, "order9", None)
                if opp_val == self:
                    setattr(old_value, "order9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order9"):
                opp_val = getattr(value, "order9", None)
                setattr(value, "order9", self)

    @property
    def myClass34(self):
        return self.__myClass34
    @myClass34.setter
    def myClass34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__myClass34", None)
        self.__myClass34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order5"):
                opp_val = getattr(old_value, "order5", None)
                if opp_val == self:
                    setattr(old_value, "order5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order5"):
                opp_val = getattr(value, "order5", None)
                setattr(value, "order5", self)

    @property
    def myClass0(self):
        return self.__myClass0
    @myClass0.setter
    def myClass0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__myClass0", None)
        self.__myClass0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order1"):
                opp_val = getattr(old_value, "order1", None)
                if opp_val == self:
                    setattr(old_value, "order1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order1"):
                opp_val = getattr(value, "order1", None)
                setattr(value, "order1", self)

