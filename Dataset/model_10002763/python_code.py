from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










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
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: str):
        self.__Amount = Amount

    @property
    def Post_balance(self):
        return self.__Post_balance
    @Post_balance.setter
    def Post_balance(self, Post_balance: str):
        self.__Post_balance = Post_balance

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
            if hasattr(old_value, "atm__Transactions6"):
                opp_val = getattr(old_value, "atm__Transactions6", None)
                if opp_val == self:
                    setattr(old_value, "atm__Transactions6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atm__Transactions6"):
                opp_val = getattr(value, "atm__Transactions6", None)
                setattr(value, "atm__Transactions6", self)



class ATM:

    def __init__(self, location: str, ManagedBy: str, bANK1: "BANK" = None):
        self.location = location
        self.ManagedBy = ManagedBy
        self.bANK1 = bANK1
        
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
    def bANK1(self):
        return self.__bANK1
    @bANK1.setter
    def bANK1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATM__bANK1", None)
        self.__bANK1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "atm0"):
                opp_val = getattr(old_value, "atm0", None)
                if opp_val == self:
                    setattr(old_value, "atm0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "atm0"):
                opp_val = getattr(value, "atm0", None)
                setattr(value, "atm0", self)



class Account:

    def __init__(self, AccountNumber: str, Balance: str, bank3: "BANK" = None, customer5: "Customer" = None, atm__Transactions6: "ATM__Transactions" = None):
        self.AccountNumber = AccountNumber
        self.Balance = Balance
        self.bank3 = bank3
        self.customer5 = customer5
        self.atm__Transactions6 = atm__Transactions6
        
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
    def bank3(self):
        return self.__bank3
    @bank3.setter
    def bank3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__bank3", None)
        self.__bank3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account2"):
                opp_val = getattr(old_value, "account2", None)
                if opp_val == self:
                    setattr(old_value, "account2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account2"):
                opp_val = getattr(value, "account2", None)
                setattr(value, "account2", self)

    @property
    def atm__Transactions6(self):
        return self.__atm__Transactions6
    @atm__Transactions6.setter
    def atm__Transactions6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__atm__Transactions6", None)
        self.__atm__Transactions6 = value
        
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
                if opp_val == self:
                    setattr(old_value, "account4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account4"):
                opp_val = getattr(value, "account4", None)
                setattr(value, "account4", self)



class Customer:

    def __init__(self, Name: str, DOB: str, Pin: int, Card_num: int, account4: "Account" = None):
        self.Name = Name
        self.DOB = DOB
        self.Pin = Pin
        self.Card_num = Card_num
        self.account4 = account4
        
        pass
    @property
    def Pin(self):
        return self.__Pin
    @Pin.setter
    def Pin(self, Pin: int):
        self.__Pin = Pin

    @property
    def Card_num(self):
        return self.__Card_num
    @Card_num.setter
    def Card_num(self, Card_num: int):
        self.__Card_num = Card_num

    @property
    def DOB(self):
        return self.__DOB
    @DOB.setter
    def DOB(self, DOB: str):
        self.__DOB = DOB

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def account4(self):
        return self.__account4
    @account4.setter
    def account4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__account4", None)
        self.__account4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer5"):
                opp_val = getattr(old_value, "customer5", None)
                if opp_val == self:
                    setattr(old_value, "customer5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer5"):
                opp_val = getattr(value, "customer5", None)
                setattr(value, "customer5", self)



class BANK:

    def __init__(self, Code: str, Address: str, atm0: "ATM" = None, account2: "Account" = None):
        self.Code = Code
        self.Address = Address
        self.atm0 = atm0
        self.account2 = account2
        
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
    def account2(self):
        return self.__account2
    @account2.setter
    def account2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BANK__account2", None)
        self.__account2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank3"):
                opp_val = getattr(old_value, "bank3", None)
                if opp_val == self:
                    setattr(old_value, "bank3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank3"):
                opp_val = getattr(value, "bank3", None)
                setattr(value, "bank3", self)

    @property
    def atm0(self):
        return self.__atm0
    @atm0.setter
    def atm0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BANK__atm0", None)
        self.__atm0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bANK1"):
                opp_val = getattr(old_value, "bANK1", None)
                if opp_val == self:
                    setattr(old_value, "bANK1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bANK1"):
                opp_val = getattr(value, "bANK1", None)
                setattr(value, "bANK1", self)

