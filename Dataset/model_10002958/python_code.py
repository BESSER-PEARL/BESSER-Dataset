from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Analyzing_UseCase:

    pass


class Comment_UseCase:

    pass


class Admin_Actor:

    pass


class Key_generate_UseCase:

    pass


class Buy_product_UseCase:

    pass


class Update_product_UseCase:

    pass


class Password_UseCase:

    pass


class View_product_UseCase:

    pass


class Login_UseCase:

    pass


class User_Actor:

    pass


class user_name_UseCase:

    pass





class order:

    def __init__(self, no_of_items_: int, amount__: int, order_status_: str, cart19: "Cart" = None, account21: "Account" = None):
        self.no_of_items_ = no_of_items_
        self.amount__ = amount__
        self.order_status_ = order_status_
        self.cart19 = cart19
        self.account21 = account21
        
        pass
    @property
    def no_of_items_(self):
        return self.__no_of_items_
    @no_of_items_.setter
    def no_of_items_(self, no_of_items_: int):
        self.__no_of_items_ = no_of_items_

    @property
    def order_status_(self):
        return self.__order_status_
    @order_status_.setter
    def order_status_(self, order_status_: str):
        self.__order_status_ = order_status_

    @property
    def amount__(self):
        return self.__amount__
    @amount__.setter
    def amount__(self, amount__: int):
        self.__amount__ = amount__

    @property
    def cart19(self):
        return self.__cart19
    @cart19.setter
    def cart19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_order__cart19", None)
        self.__cart19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order18"):
                opp_val = getattr(old_value, "order18", None)
                if opp_val == self:
                    setattr(old_value, "order18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order18"):
                opp_val = getattr(value, "order18", None)
                setattr(value, "order18", self)

    @property
    def account21(self):
        return self.__account21
    @account21.setter
    def account21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_order__account21", None)
        self.__account21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "order20"):
                opp_val = getattr(old_value, "order20", None)
                if opp_val == self:
                    setattr(old_value, "order20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "order20"):
                opp_val = getattr(value, "order20", None)
                setattr(value, "order20", self)



class Cart:

    def __init__(self, Buy_: int, No_of_items_: int, Delete_: str, order18: "order" = None):
        self.Buy_ = Buy_
        self.No_of_items_ = No_of_items_
        self.Delete_ = Delete_
        self.order18 = order18
        
        pass
    @property
    def Buy_(self):
        return self.__Buy_
    @Buy_.setter
    def Buy_(self, Buy_: int):
        self.__Buy_ = Buy_

    @property
    def Delete_(self):
        return self.__Delete_
    @Delete_.setter
    def Delete_(self, Delete_: str):
        self.__Delete_ = Delete_

    @property
    def No_of_items_(self):
        return self.__No_of_items_
    @No_of_items_.setter
    def No_of_items_(self, No_of_items_: int):
        self.__No_of_items_ = No_of_items_

    @property
    def order18(self):
        return self.__order18
    @order18.setter
    def order18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cart__order18", None)
        self.__order18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cart19"):
                opp_val = getattr(old_value, "cart19", None)
                if opp_val == self:
                    setattr(old_value, "cart19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cart19"):
                opp_val = getattr(value, "cart19", None)
                setattr(value, "cart19", self)



class Login:

    def __init__(self, login_id_: str, password_: str, customer16: "Customer" = None):
        self.login_id_ = login_id_
        self.password_ = password_
        self.customer16 = customer16
        
        pass
    @property
    def password_(self):
        return self.__password_
    @password_.setter
    def password_(self, password_: str):
        self.__password_ = password_

    @property
    def login_id_(self):
        return self.__login_id_
    @login_id_.setter
    def login_id_(self, login_id_: str):
        self.__login_id_ = login_id_

    @property
    def customer16(self):
        return self.__customer16
    @customer16.setter
    def customer16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__customer16", None)
        self.__customer16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login17"):
                opp_val = getattr(old_value, "login17", None)
                if opp_val == self:
                    setattr(old_value, "login17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login17"):
                opp_val = getattr(value, "login17", None)
                setattr(value, "login17", self)



class Payment:

    def __init__(self, Transaction_id_: int, Amount_paid_: int, Acc_No_: int):
        self.Transaction_id_ = Transaction_id_
        self.Amount_paid_ = Amount_paid_
        self.Acc_No_ = Acc_No_
        
        pass
    @property
    def Acc_No_(self):
        return self.__Acc_No_
    @Acc_No_.setter
    def Acc_No_(self, Acc_No_: int):
        self.__Acc_No_ = Acc_No_

    @property
    def Amount_paid_(self):
        return self.__Amount_paid_
    @Amount_paid_.setter
    def Amount_paid_(self, Amount_paid_: int):
        self.__Amount_paid_ = Amount_paid_

    @property
    def Transaction_id_(self):
        return self.__Transaction_id_
    @Transaction_id_.setter
    def Transaction_id_(self, Transaction_id_: int):
        self.__Transaction_id_ = Transaction_id_



class Account:

    def __init__(self, Branch_: str, Phone_no_: int, Acc_no_: int, order20: "order" = None):
        self.Branch_ = Branch_
        self.Phone_no_ = Phone_no_
        self.Acc_no_ = Acc_no_
        self.order20 = order20
        
        pass
    @property
    def Phone_no_(self):
        return self.__Phone_no_
    @Phone_no_.setter
    def Phone_no_(self, Phone_no_: int):
        self.__Phone_no_ = Phone_no_

    @property
    def Acc_no_(self):
        return self.__Acc_no_
    @Acc_no_.setter
    def Acc_no_(self, Acc_no_: int):
        self.__Acc_no_ = Acc_no_

    @property
    def Branch_(self):
        return self.__Branch_
    @Branch_.setter
    def Branch_(self, Branch_: str):
        self.__Branch_ = Branch_

    @property
    def order20(self):
        return self.__order20
    @order20.setter
    def order20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__order20", None)
        self.__order20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account21"):
                opp_val = getattr(old_value, "account21", None)
                if opp_val == self:
                    setattr(old_value, "account21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account21"):
                opp_val = getattr(value, "account21", None)
                setattr(value, "account21", self)



class Customer:

    def __init__(self, login_id_: str, Address_: str, Phone_: int, login17: "Login" = None):
        self.login_id_ = login_id_
        self.Address_ = Address_
        self.Phone_ = Phone_
        self.login17 = login17
        
        pass
    @property
    def Address_(self):
        return self.__Address_
    @Address_.setter
    def Address_(self, Address_: str):
        self.__Address_ = Address_

    @property
    def Phone_(self):
        return self.__Phone_
    @Phone_.setter
    def Phone_(self, Phone_: int):
        self.__Phone_ = Phone_

    @property
    def login_id_(self):
        return self.__login_id_
    @login_id_.setter
    def login_id_(self, login_id_: str):
        self.__login_id_ = login_id_

    @property
    def login17(self):
        return self.__login17
    @login17.setter
    def login17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__login17", None)
        self.__login17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer16"):
                opp_val = getattr(old_value, "customer16", None)
                if opp_val == self:
                    setattr(old_value, "customer16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer16"):
                opp_val = getattr(value, "customer16", None)
                setattr(value, "customer16", self)

