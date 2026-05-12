from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Savings_Account:

    def __init__(self, AccountNumber: str, Balance: str, current_Account9: "Current_Account" = None):
        self.AccountNumber = AccountNumber
        self.Balance = Balance
        self.current_Account9 = current_Account9
        
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
    def current_Account9(self):
        return self.__current_Account9
    @current_Account9.setter
    def current_Account9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Savings_Account__current_Account9", None)
        self.__current_Account9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "savings_Account8"):
                opp_val = getattr(old_value, "savings_Account8", None)
                if opp_val == self:
                    setattr(old_value, "savings_Account8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "savings_Account8"):
                opp_val = getattr(value, "savings_Account8", None)
                setattr(value, "savings_Account8", self)



class Current_Account:

    def __init__(self, AccountNumber: str, Balance: str, savings_Account8: "Savings_Account" = None):
        self.AccountNumber = AccountNumber
        self.Balance = Balance
        self.savings_Account8 = savings_Account8
        
        pass
    @property
    def Balance(self):
        return self.__Balance
    @Balance.setter
    def Balance(self, Balance: str):
        self.__Balance = Balance

    @property
    def AccountNumber(self):
        return self.__AccountNumber
    @AccountNumber.setter
    def AccountNumber(self, AccountNumber: str):
        self.__AccountNumber = AccountNumber

    @property
    def savings_Account8(self):
        return self.__savings_Account8
    @savings_Account8.setter
    def savings_Account8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Current_Account__savings_Account8", None)
        self.__savings_Account8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "current_Account9"):
                opp_val = getattr(old_value, "current_Account9", None)
                if opp_val == self:
                    setattr(old_value, "current_Account9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "current_Account9"):
                opp_val = getattr(value, "current_Account9", None)
                setattr(value, "current_Account9", self)



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
    def Transaction_id(self):
        return self.__Transaction_id
    @Transaction_id.setter
    def Transaction_id(self, Transaction_id: str):
        self.__Transaction_id = Transaction_id

    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: str):
        self.__Amount = Amount

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def Post_balance(self):
        return self.__Post_balance
    @Post_balance.setter
    def Post_balance(self, Post_balance: str):
        self.__Post_balance = Post_balance

    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

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
            if hasattr(old_value, "aTM__Transactions6"):
                opp_val = getattr(old_value, "aTM__Transactions6", None)
                if opp_val == self:
                    setattr(old_value, "aTM__Transactions6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aTM__Transactions6"):
                opp_val = getattr(value, "aTM__Transactions6", None)
                setattr(value, "aTM__Transactions6", self)



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
            if hasattr(old_value, "aTM0"):
                opp_val = getattr(old_value, "aTM0", None)
                if opp_val == self:
                    setattr(old_value, "aTM0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aTM0"):
                opp_val = getattr(value, "aTM0", None)
                setattr(value, "aTM0", self)



class Account:

    def __init__(self, AccountNumber: str, Balance: str, bANK3: "BANK" = None, customer5: "Customer" = None, aTM__Transactions6: "ATM__Transactions" = None):
        self.AccountNumber = AccountNumber
        self.Balance = Balance
        self.bANK3 = bANK3
        self.customer5 = customer5
        self.aTM__Transactions6 = aTM__Transactions6
        
        pass
    @property
    def Balance(self):
        return self.__Balance
    @Balance.setter
    def Balance(self, Balance: str):
        self.__Balance = Balance

    @property
    def AccountNumber(self):
        return self.__AccountNumber
    @AccountNumber.setter
    def AccountNumber(self, AccountNumber: str):
        self.__AccountNumber = AccountNumber

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

    @property
    def bANK3(self):
        return self.__bANK3
    @bANK3.setter
    def bANK3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__bANK3", None)
        self.__bANK3 = value
        
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
    def aTM__Transactions6(self):
        return self.__aTM__Transactions6
    @aTM__Transactions6.setter
    def aTM__Transactions6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__aTM__Transactions6", None)
        self.__aTM__Transactions6 = value
        
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
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def DOB(self):
        return self.__DOB
    @DOB.setter
    def DOB(self, DOB: str):
        self.__DOB = DOB

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

    def __init__(self, Code: str, Address: str, aTM0: "ATM" = None, account2: "Account" = None):
        self.Code = Code
        self.Address = Address
        self.aTM0 = aTM0
        self.account2 = account2
        
        pass
    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Code(self):
        return self.__Code
    @Code.setter
    def Code(self, Code: str):
        self.__Code = Code

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
            if hasattr(old_value, "bANK3"):
                opp_val = getattr(old_value, "bANK3", None)
                if opp_val == self:
                    setattr(old_value, "bANK3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bANK3"):
                opp_val = getattr(value, "bANK3", None)
                setattr(value, "bANK3", self)

    @property
    def aTM0(self):
        return self.__aTM0
    @aTM0.setter
    def aTM0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BANK__aTM0", None)
        self.__aTM0 = value
        
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

