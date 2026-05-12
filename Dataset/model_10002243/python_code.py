from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Login_UseCase:

    pass


class Sign_Up_UseCase:

    pass


class Make_Payment_UseCase:

    pass


class Track_Order_UseCase:

    pass


class View_Order_Details_UseCase:

    pass


class Rating_UseCase:

    pass


class Place_Order_UseCase:

    pass


class Add_To_Cart_UseCase:

    pass


class Customer_Actor:

    pass





class Cash_On_Delivery:

    pass


class Wallet:

    pass


class Payment:

    def __init__(self, Amount: int, System_Order_Payment_117: "System_Order" = None):
        self.Amount = Amount
        self.System_Order_Payment_117 = System_Order_Payment_117
        
        pass
    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: int):
        self.__Amount = Amount

    @property
    def System_Order_Payment_117(self):
        return self.__System_Order_Payment_117
    @System_Order_Payment_117.setter
    def System_Order_Payment_117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__System_Order_Payment_117", None)
        self.__System_Order_Payment_117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "System_Order_Payment_016"):
                opp_val = getattr(old_value, "System_Order_Payment_016", None)
                if opp_val == self:
                    setattr(old_value, "System_Order_Payment_016", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "System_Order_Payment_016"):
                opp_val = getattr(value, "System_Order_Payment_016", None)
                setattr(value, "System_Order_Payment_016", self)



class System_Order:

    pass


class Cutomer:

    pass
