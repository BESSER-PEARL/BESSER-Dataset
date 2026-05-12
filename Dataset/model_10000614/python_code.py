from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Component32322_Component:

    pass


class Component3232_Component:

    pass


class Component323_Component:

    pass


class Component322_Component:

    pass


class Component32_Component:

    pass


class Component3_Component:

    pass


class ATM_Machine__Component:

    pass


class T:

    pass


class Component_Component:

    pass


class ATM__Transactions:

    def __init__(self, Transaction_id: str, Date: str, Type: str, Amount: str, Post_balance: str, account7: "Account" = None):
        self.Transaction_id = Transaction_id
        self.Date = Date
        self.Type = Type
        self.Amount = Amount
        self.Post_balance = Post_balance
        self.account7 = account7
        
        pass
    @property
    def Post_balance(self):
        return self.__Post_balance
    @Post_balance.setter
    def Post_balance(self, Post_balance: str):
        self.__Post_balance = Post_balance

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: str):
        self.__Amount = Amount

    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Transaction_id(self):
        return self.__Transaction_id
    @Transaction_id.setter
    def Transaction_id(self, Transaction_id: str):
        self.__Transaction_id = Transaction_id

    @property
    def account7(self):
        return self.__account7
    @account7.setter
    def account7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATM__Transactions__account7", None)
        self.__account7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATM__Transactions6"):
                opp_val = getattr(old_value, "ATM__Transactions6", None)
                if opp_val == self:
                    setattr(old_value, "ATM__Transactions6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATM__Transactions6"):
                opp_val = getattr(value, "ATM__Transactions6", None)
                setattr(value, "ATM__Transactions6", self)



class ATM:

    def __init__(self, location: str, ManagedBy: str, BANK1: "BANK" = None):
        self.location = location
        self.ManagedBy = ManagedBy
        self.BANK1 = BANK1
        
        pass
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def ManagedBy(self):
        return self.__ManagedBy
    @ManagedBy.setter
    def ManagedBy(self, ManagedBy: str):
        self.__ManagedBy = ManagedBy

    @property
    def BANK1(self):
        return self.__BANK1
    @BANK1.setter
    def BANK1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATM__BANK1", None)
        self.__BANK1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ATM0"):
                opp_val = getattr(old_value, "ATM0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ATM0"):
                opp_val = getattr(value, "ATM0", None)
                if opp_val is None:
                    setattr(value, "ATM0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Account:

    def __init__(self, AccountNumber: str, Balance: str, BANK3: "BANK" = None, customer5: "Customer" = None, ATM__Transactions6: "ATM__Transactions" = None):
        self.AccountNumber = AccountNumber
        self.Balance = Balance
        self.BANK3 = BANK3
        self.customer5 = customer5
        self.ATM__Transactions6 = ATM__Transactions6
        
        pass
    @property
    def AccountNumber(self):
        return self.__AccountNumber
    @AccountNumber.setter
    def AccountNumber(self, AccountNumber: str):
        self.__AccountNumber = AccountNumber

    @property
    def Balance(self):
        return self.__Balance
    @Balance.setter
    def Balance(self, Balance: str):
        self.__Balance = Balance

    @property
    def BANK3(self):
        return self.__BANK3
    @BANK3.setter
    def BANK3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__BANK3", None)
        self.__BANK3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account2"):
                opp_val = getattr(old_value, "account2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account2"):
                opp_val = getattr(value, "account2", None)
                if opp_val is None:
                    setattr(value, "account2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def customer5(self):
        return self.__customer5
    @customer5.setter
    def customer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__customer5", None)
        self.__customer5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account4"):
                opp_val = getattr(old_value, "account4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account4"):
                opp_val = getattr(value, "account4", None)
                if opp_val is None:
                    setattr(value, "account4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ATM__Transactions6(self):
        return self.__ATM__Transactions6
    @ATM__Transactions6.setter
    def ATM__Transactions6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__ATM__Transactions6", None)
        self.__ATM__Transactions6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account7"):
                opp_val = getattr(old_value, "account7", None)
                if opp_val == self:
                    setattr(old_value, "account7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account7"):
                opp_val = getattr(value, "account7", None)
                setattr(value, "account7", self)



class Customer:

    def __init__(self, Name: str, DOB: str, Pin: int, Card_num: int, account4: set["Account"] = None):
        self.Name = Name
        self.DOB = DOB
        self.Pin = Pin
        self.Card_num = Card_num
        self.account4 = account4 if account4 is not None else set()
        
        pass
    @property
    def DOB(self):
        return self.__DOB
    @DOB.setter
    def DOB(self, DOB: str):
        self.__DOB = DOB

    @property
    def Pin(self):
        return self.__Pin
    @Pin.setter
    def Pin(self, Pin: int):
        self.__Pin = Pin

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Card_num(self):
        return self.__Card_num
    @Card_num.setter
    def Card_num(self, Card_num: int):
        self.__Card_num = Card_num

    @property
    def account4(self):
        return self.__account4
    @account4.setter
    def account4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__account4", None)
        self.__account4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer5"):
                    opp_val = getattr(item, "customer5", None)
                    
                    if opp_val == self:
                        setattr(item, "customer5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer5"):
                    opp_val = getattr(item, "customer5", None)
                    
                    setattr(item, "customer5", self)
                    



class BANK:

    def __init__(self, Code: str, Address: str, ATM0: set["ATM"] = None, account2: set["Account"] = None):
        self.Code = Code
        self.Address = Address
        self.ATM0 = ATM0 if ATM0 is not None else set()
        self.account2 = account2 if account2 is not None else set()
        
        pass
    @property
    def Code(self):
        return self.__Code
    @Code.setter
    def Code(self, Code: str):
        self.__Code = Code

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def ATM0(self):
        return self.__ATM0
    @ATM0.setter
    def ATM0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BANK__ATM0", None)
        self.__ATM0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BANK1"):
                    opp_val = getattr(item, "BANK1", None)
                    
                    if opp_val == self:
                        setattr(item, "BANK1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BANK1"):
                    opp_val = getattr(item, "BANK1", None)
                    
                    setattr(item, "BANK1", self)
                    

    @property
    def account2(self):
        return self.__account2
    @account2.setter
    def account2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BANK__account2", None)
        self.__account2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BANK3"):
                    opp_val = getattr(item, "BANK3", None)
                    
                    if opp_val == self:
                        setattr(item, "BANK3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BANK3"):
                    opp_val = getattr(item, "BANK3", None)
                    
                    setattr(item, "BANK3", self)
                    

