from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Payment:

    def __init__(self, Amount: int, Date_off: str, order5: "Order" = None):
        self.Amount = Amount
        self.Date_off = Date_off
        self.order5 = order5
        
        pass
    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: int):
        self.__Amount = Amount

    @property
    def Date_off(self):
        return self.__Date_off
    @Date_off.setter
    def Date_off(self, Date_off: str):
        self.__Date_off = Date_off

    @property
    def order5(self):
        return self.__order5
    @order5.setter
    def order5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Payment__order5", None)
        self.__order5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payment4"):
                opp_val = getattr(old_value, "payment4", None)
                if opp_val == self:
                    setattr(old_value, "payment4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payment4"):
                opp_val = getattr(value, "payment4", None)
                setattr(value, "payment4", self)



class Discription:

    def __init__(self, Email: str, Discription: str, order7: "Order" = None):
        self.Email = Email
        self.Discription = Discription
        self.order7 = order7
        
        pass
    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Discription(self):
        return self.__Discription
    @Discription.setter
    def Discription(self, Discription: str):
        self.__Discription = Discription

    @property
    def order7(self):
        return self.__order7
    @order7.setter
    def order7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Discription__order7", None)
        self.__order7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "discription6"):
                opp_val = getattr(old_value, "discription6", None)
                if opp_val == self:
                    setattr(old_value, "discription6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "discription6"):
                opp_val = getattr(value, "discription6", None)
                setattr(value, "discription6", self)



class User:

    def __init__(self, Name: str, Phone_num: int, Address: str, Email: str, delivery2: "Delivery" = None, order9: "Order" = None):
        self.Name = Name
        self.Phone_num = Phone_num
        self.Address = Address
        self.Email = Email
        self.delivery2 = delivery2
        self.order9 = order9
        
        pass
    @property
    def Phone_num(self):
        return self.__Phone_num
    @Phone_num.setter
    def Phone_num(self, Phone_num: int):
        self.__Phone_num = Phone_num

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def order9(self):
        return self.__order9
    @order9.setter
    def order9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__order9", None)
        self.__order9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user8"):
                opp_val = getattr(old_value, "user8", None)
                if opp_val == self:
                    setattr(old_value, "user8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user8"):
                opp_val = getattr(value, "user8", None)
                setattr(value, "user8", self)

    @property
    def delivery2(self):
        return self.__delivery2
    @delivery2.setter
    def delivery2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__delivery2", None)
        self.__delivery2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "User_Delivery_13"):
                opp_val = getattr(old_value, "User_Delivery_13", None)
                if opp_val == self:
                    setattr(old_value, "User_Delivery_13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "User_Delivery_13"):
                opp_val = getattr(value, "User_Delivery_13", None)
                setattr(value, "User_Delivery_13", self)



class Delivery:

    def __init__(self, Date: str, Type: str, Name: str, order1: "Order" = None, User_Delivery_13: "User" = None):
        self.Date = Date
        self.Type = Type
        self.Name = Name
        self.order1 = order1
        self.User_Delivery_13 = User_Delivery_13
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def User_Delivery_13(self):
        return self.__User_Delivery_13
    @User_Delivery_13.setter
    def User_Delivery_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Delivery__User_Delivery_13", None)
        self.__User_Delivery_13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delivery2"):
                opp_val = getattr(old_value, "delivery2", None)
                if opp_val == self:
                    setattr(old_value, "delivery2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delivery2"):
                opp_val = getattr(value, "delivery2", None)
                setattr(value, "delivery2", self)

    @property
    def order1(self):
        return self.__order1
    @order1.setter
    def order1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Delivery__order1", None)
        self.__order1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "delivery0"):
                opp_val = getattr(old_value, "delivery0", None)
                if opp_val == self:
                    setattr(old_value, "delivery0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "delivery0"):
                opp_val = getattr(value, "delivery0", None)
                setattr(value, "delivery0", self)



class Order:

    def __init__(self, ID: int, Quantity: int, Type: str, Size: int, delivery0: "Delivery" = None, payment4: "Payment" = None, discription6: "Discription" = None, user8: "User" = None):
        self.ID = ID
        self.Quantity = Quantity
        self.Type = Type
        self.Size = Size
        self.delivery0 = delivery0
        self.payment4 = payment4
        self.discription6 = discription6
        self.user8 = user8
        
        pass
    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Size(self):
        return self.__Size
    @Size.setter
    def Size(self, Size: int):
        self.__Size = Size

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity

    @property
    def discription6(self):
        return self.__discription6
    @discription6.setter
    def discription6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__discription6", None)
        self.__discription6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order7"):
                opp_val = getattr(old_value, "order7", None)
                if opp_val == self:
                    setattr(old_value, "order7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order7"):
                opp_val = getattr(value, "order7", None)
                setattr(value, "order7", self)

    @property
    def payment4(self):
        return self.__payment4
    @payment4.setter
    def payment4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__payment4", None)
        self.__payment4 = value
        
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
    def delivery0(self):
        return self.__delivery0
    @delivery0.setter
    def delivery0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__delivery0", None)
        self.__delivery0 = value
        
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

    @property
    def user8(self):
        return self.__user8
    @user8.setter
    def user8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Order__user8", None)
        self.__user8 = value
        
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

