from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TransactionType(Enum):
    pass

############################################
# Definition of Classes
############################################










class Setting:

    pass


class Transaction:

    def __init__(self, TranId: int, Acc_num: int, date: str, type: TransactionType, amount: int, prevBalance: int, currentBalance: int, status: str, account11: "Account" = None):
        self.TranId = TranId
        self.Acc_num = Acc_num
        self.date = date
        self.type = type
        self.amount = amount
        self.prevBalance = prevBalance
        self.currentBalance = currentBalance
        self.status = status
        self.account11 = account11
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: TransactionType):
        self.__type = type

    @property
    def currentBalance(self):
        return self.__currentBalance
    @currentBalance.setter
    def currentBalance(self, currentBalance: int):
        self.__currentBalance = currentBalance

    @property
    def prevBalance(self):
        return self.__prevBalance
    @prevBalance.setter
    def prevBalance(self, prevBalance: int):
        self.__prevBalance = prevBalance

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def TranId(self):
        return self.__TranId
    @TranId.setter
    def TranId(self, TranId: int):
        self.__TranId = TranId

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount

    @property
    def Acc_num(self):
        return self.__Acc_num
    @Acc_num.setter
    def Acc_num(self, Acc_num: int):
        self.__Acc_num = Acc_num

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def account11(self):
        return self.__account11
    @account11.setter
    def account11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Transaction__account11", None)
        self.__account11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transaction10"):
                opp_val = getattr(old_value, "transaction10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transaction10"):
                opp_val = getattr(value, "transaction10", None)
                if opp_val is None:
                    setattr(value, "transaction10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Manager:

    pass


class Employee:

    def __init__(self, Eid: int, Mid: int, manager8: "Manager" = None):
        self.Eid = Eid
        self.Mid = Mid
        self.manager8 = manager8
        
        pass
    @property
    def Eid(self):
        return self.__Eid
    @Eid.setter
    def Eid(self, Eid: int):
        self.__Eid = Eid

    @property
    def Mid(self):
        return self.__Mid
    @Mid.setter
    def Mid(self, Mid: int):
        self.__Mid = Mid

    @property
    def manager8(self):
        return self.__manager8
    @manager8.setter
    def manager8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__manager8", None)
        self.__manager8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee9"):
                opp_val = getattr(old_value, "employee9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee9"):
                opp_val = getattr(value, "employee9", None)
                if opp_val is None:
                    setattr(value, "employee9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class User:

    def __init__(self, uid: int, name: str, family: str, userName: str, password: str):
        self.uid = uid
        self.name = name
        self.family = family
        self.userName = userName
        self.password = password
        
        pass
    @property
    def userName(self):
        return self.__userName
    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def family(self):
        return self.__family
    @family.setter
    def family(self, family: str):
        self.__family = family

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def uid(self):
        return self.__uid
    @uid.setter
    def uid(self, uid: int):
        self.__uid = uid



class Customer:

    def __init__(self, Cust_id: str, name: str, address: str, phone: str, saving_Account5: "Saving_Account" = None, current_Account7: "Current_Account" = None):
        self.Cust_id = Cust_id
        self.name = name
        self.address = address
        self.phone = phone
        self.saving_Account5 = saving_Account5
        self.current_Account7 = current_Account7
        
        pass
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def Cust_id(self):
        return self.__Cust_id
    @Cust_id.setter
    def Cust_id(self, Cust_id: str):
        self.__Cust_id = Cust_id

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def saving_Account5(self):
        return self.__saving_Account5
    @saving_Account5.setter
    def saving_Account5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__saving_Account5", None)
        self.__saving_Account5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer4"):
                opp_val = getattr(old_value, "customer4", None)
                if opp_val == self:
                    setattr(old_value, "customer4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer4"):
                opp_val = getattr(value, "customer4", None)
                setattr(value, "customer4", self)

    @property
    def current_Account7(self):
        return self.__current_Account7
    @current_Account7.setter
    def current_Account7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__current_Account7", None)
        self.__current_Account7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer6"):
                opp_val = getattr(old_value, "customer6", None)
                if opp_val == self:
                    setattr(old_value, "customer6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer6"):
                opp_val = getattr(value, "customer6", None)
                setattr(value, "customer6", self)



class Current_Account:

    pass


class Saving_Account:

    def __init__(self, interest_Rate: int, customer4: "Customer" = None):
        self.interest_Rate = interest_Rate
        self.customer4 = customer4
        
        pass
    @property
    def interest_Rate(self):
        return self.__interest_Rate
    @interest_Rate.setter
    def interest_Rate(self, interest_Rate: int):
        self.__interest_Rate = interest_Rate

    @property
    def customer4(self):
        return self.__customer4
    @customer4.setter
    def customer4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Saving_Account__customer4", None)
        self.__customer4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "saving_Account5"):
                opp_val = getattr(old_value, "saving_Account5", None)
                if opp_val == self:
                    setattr(old_value, "saving_Account5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "saving_Account5"):
                opp_val = getattr(value, "saving_Account5", None)
                setattr(value, "saving_Account5", self)



class Account:

    def __init__(self, Acc_no: int, Balance: int, date_Of_Opening: str, min_Balance: int, branch3: "Branch" = None, transaction10: set["Transaction"] = None):
        self.Acc_no = Acc_no
        self.Balance = Balance
        self.date_Of_Opening = date_Of_Opening
        self.min_Balance = min_Balance
        self.branch3 = branch3
        self.transaction10 = transaction10 if transaction10 is not None else set()
        
        pass
    @property
    def min_Balance(self):
        return self.__min_Balance
    @min_Balance.setter
    def min_Balance(self, min_Balance: int):
        self.__min_Balance = min_Balance

    @property
    def Acc_no(self):
        return self.__Acc_no
    @Acc_no.setter
    def Acc_no(self, Acc_no: int):
        self.__Acc_no = Acc_no

    @property
    def Balance(self):
        return self.__Balance
    @Balance.setter
    def Balance(self, Balance: int):
        self.__Balance = Balance

    @property
    def date_Of_Opening(self):
        return self.__date_Of_Opening
    @date_Of_Opening.setter
    def date_Of_Opening(self, date_Of_Opening: str):
        self.__date_Of_Opening = date_Of_Opening

    @property
    def branch3(self):
        return self.__branch3
    @branch3.setter
    def branch3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__branch3", None)
        self.__branch3 = value
        
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
    def transaction10(self):
        return self.__transaction10
    @transaction10.setter
    def transaction10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__transaction10", None)
        self.__transaction10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account11"):
                    opp_val = getattr(item, "account11", None)
                    
                    if opp_val == self:
                        setattr(item, "account11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account11"):
                    opp_val = getattr(item, "account11", None)
                    
                    setattr(item, "account11", self)
                    



class Branch:

    def __init__(self, Branch_code: str, City: str, bank1: "Bank" = None, account2: set["Account"] = None):
        self.Branch_code = Branch_code
        self.City = City
        self.bank1 = bank1
        self.account2 = account2 if account2 is not None else set()
        
        pass
    @property
    def City(self):
        return self.__City
    @City.setter
    def City(self, City: str):
        self.__City = City

    @property
    def Branch_code(self):
        return self.__Branch_code
    @Branch_code.setter
    def Branch_code(self, Branch_code: str):
        self.__Branch_code = Branch_code

    @property
    def bank1(self):
        return self.__bank1
    @bank1.setter
    def bank1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Branch__bank1", None)
        self.__bank1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "branch0"):
                opp_val = getattr(old_value, "branch0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "branch0"):
                opp_val = getattr(value, "branch0", None)
                if opp_val is None:
                    setattr(value, "branch0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def account2(self):
        return self.__account2
    @account2.setter
    def account2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Branch__account2", None)
        self.__account2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "branch3"):
                    opp_val = getattr(item, "branch3", None)
                    
                    if opp_val == self:
                        setattr(item, "branch3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "branch3"):
                    opp_val = getattr(item, "branch3", None)
                    
                    setattr(item, "branch3", self)
                    



class Bank:

    def __init__(self, Name: str, Code: str, branch0: set["Branch"] = None):
        self.Name = Name
        self.Code = Code
        self.branch0 = branch0 if branch0 is not None else set()
        
        pass
    @property
    def Code(self):
        return self.__Code
    @Code.setter
    def Code(self, Code: str):
        self.__Code = Code

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def branch0(self):
        return self.__branch0
    @branch0.setter
    def branch0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bank__branch0", None)
        self.__branch0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bank1"):
                    opp_val = getattr(item, "bank1", None)
                    
                    if opp_val == self:
                        setattr(item, "bank1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bank1"):
                    opp_val = getattr(item, "bank1", None)
                    
                    setattr(item, "bank1", self)
                    

