from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class CheckBalance:

    def __init__(self, Query: str):
        self.Query = Query
        
        pass
    @property
    def Query(self):
        return self.__Query
    @Query.setter
    def Query(self, Query: str):
        self.__Query = Query



class Transfer_Money:

    def __init__(self, amount: int, ACC_NO: str):
        self.amount = amount
        self.ACC_NO = ACC_NO
        
        pass
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount

    @property
    def ACC_NO(self):
        return self.__ACC_NO
    @ACC_NO.setter
    def ACC_NO(self, ACC_NO: str):
        self.__ACC_NO = ACC_NO



class Withdraw_Transaction:

    def __init__(self, amount: int):
        self.amount = amount
        
        pass
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount



class Savings_Account:

    def __init__(self, Acc_no: str, Balance: str):
        self.Acc_no = Acc_no
        self.Balance = Balance
        
        pass
    @property
    def Balance(self):
        return self.__Balance
    @Balance.setter
    def Balance(self, Balance: str):
        self.__Balance = Balance

    @property
    def Acc_no(self):
        return self.__Acc_no
    @Acc_no.setter
    def Acc_no(self, Acc_no: str):
        self.__Acc_no = Acc_no



class Current_Account:

    def __init__(self, Acc_no: str, Balance: str):
        self.Acc_no = Acc_no
        self.Balance = Balance
        
        pass
    @property
    def Balance(self):
        return self.__Balance
    @Balance.setter
    def Balance(self, Balance: str):
        self.__Balance = Balance

    @property
    def Acc_no(self):
        return self.__Acc_no
    @Acc_no.setter
    def Acc_no(self, Acc_no: str):
        self.__Acc_no = Acc_no



class ATM_Transaction:

    def __init__(self, TransactionId: str, Date: str, Amount: int, aTM_INFO13: "ATM_INFO" = None):
        self.TransactionId = TransactionId
        self.Date = Date
        self.Amount = Amount
        self.aTM_INFO13 = aTM_INFO13
        
        pass
    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: int):
        self.__Amount = Amount

    @property
    def TransactionId(self):
        return self.__TransactionId
    @TransactionId.setter
    def TransactionId(self, TransactionId: str):
        self.__TransactionId = TransactionId

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def aTM_INFO13(self):
        return self.__aTM_INFO13
    @aTM_INFO13.setter
    def aTM_INFO13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATM_Transaction__aTM_INFO13", None)
        self.__aTM_INFO13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aTM_Transaction12"):
                opp_val = getattr(old_value, "aTM_Transaction12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aTM_Transaction12"):
                opp_val = getattr(value, "aTM_Transaction12", None)
                if opp_val is None:
                    setattr(value, "aTM_Transaction12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class ATM_INFO:

    def __init__(self, Location: str, aTM_Transaction12: set["ATM_Transaction"] = None, myClass7: "Bank" = None):
        self.Location = Location
        self.aTM_Transaction12 = aTM_Transaction12 if aTM_Transaction12 is not None else set()
        self.myClass7 = myClass7
        
        pass
    @property
    def Location(self):
        return self.__Location
    @Location.setter
    def Location(self, Location: str):
        self.__Location = Location

    @property
    def aTM_Transaction12(self):
        return self.__aTM_Transaction12
    @aTM_Transaction12.setter
    def aTM_Transaction12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATM_INFO__aTM_Transaction12", None)
        self.__aTM_Transaction12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aTM_INFO13"):
                    opp_val = getattr(item, "aTM_INFO13", None)
                    
                    if opp_val == self:
                        setattr(item, "aTM_INFO13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aTM_INFO13"):
                    opp_val = getattr(item, "aTM_INFO13", None)
                    
                    setattr(item, "aTM_INFO13", self)
                    

    @property
    def myClass7(self):
        return self.__myClass7
    @myClass7.setter
    def myClass7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATM_INFO__myClass7", None)
        self.__myClass7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aTM_INFO6"):
                opp_val = getattr(old_value, "aTM_INFO6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aTM_INFO6"):
                opp_val = getattr(value, "aTM_INFO6", None)
                if opp_val is None:
                    setattr(value, "aTM_INFO6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Account:

    def __init__(self, Type: str, Owned_by: str, BranchLocation: str, debit_Card11: "Debit_Card" = None):
        self.Type = Type
        self.Owned_by = Owned_by
        self.BranchLocation = BranchLocation
        self.debit_Card11 = debit_Card11
        
        pass
    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Owned_by(self):
        return self.__Owned_by
    @Owned_by.setter
    def Owned_by(self, Owned_by: str):
        self.__Owned_by = Owned_by

    @property
    def BranchLocation(self):
        return self.__BranchLocation
    @BranchLocation.setter
    def BranchLocation(self, BranchLocation: str):
        self.__BranchLocation = BranchLocation

    @property
    def debit_Card11(self):
        return self.__debit_Card11
    @debit_Card11.setter
    def debit_Card11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Account__debit_Card11", None)
        self.__debit_Card11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account10"):
                opp_val = getattr(old_value, "account10", None)
                if opp_val == self:
                    setattr(old_value, "account10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account10"):
                opp_val = getattr(value, "account10", None)
                setattr(value, "account10", self)



class Debit_Card:

    def __init__(self, Card_No: str, Owned_By: str, debit_Card8: "Debit_Card" = None, debit_Card9: "Debit_Card" = None, account10: "Account" = None, myClass0: "Bank" = None, customer2: "Customer" = None):
        self.Card_No = Card_No
        self.Owned_By = Owned_By
        self.debit_Card8 = debit_Card8
        self.debit_Card9 = debit_Card9
        self.account10 = account10
        self.myClass0 = myClass0
        self.customer2 = customer2
        
        pass
    @property
    def Owned_By(self):
        return self.__Owned_By
    @Owned_By.setter
    def Owned_By(self, Owned_By: str):
        self.__Owned_By = Owned_By

    @property
    def Card_No(self):
        return self.__Card_No
    @Card_No.setter
    def Card_No(self, Card_No: str):
        self.__Card_No = Card_No

    @property
    def customer2(self):
        return self.__customer2
    @customer2.setter
    def customer2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Debit_Card__customer2", None)
        self.__customer2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debit_Card3"):
                opp_val = getattr(old_value, "debit_Card3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debit_Card3"):
                opp_val = getattr(value, "debit_Card3", None)
                if opp_val is None:
                    setattr(value, "debit_Card3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def account10(self):
        return self.__account10
    @account10.setter
    def account10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Debit_Card__account10", None)
        self.__account10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debit_Card11"):
                opp_val = getattr(old_value, "debit_Card11", None)
                if opp_val == self:
                    setattr(old_value, "debit_Card11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debit_Card11"):
                opp_val = getattr(value, "debit_Card11", None)
                setattr(value, "debit_Card11", self)

    @property
    def debit_Card8(self):
        return self.__debit_Card8
    @debit_Card8.setter
    def debit_Card8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Debit_Card__debit_Card8", None)
        self.__debit_Card8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debit_Card9"):
                opp_val = getattr(old_value, "debit_Card9", None)
                if opp_val == self:
                    setattr(old_value, "debit_Card9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debit_Card9"):
                opp_val = getattr(value, "debit_Card9", None)
                setattr(value, "debit_Card9", self)

    @property
    def myClass0(self):
        return self.__myClass0
    @myClass0.setter
    def myClass0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Debit_Card__myClass0", None)
        self.__myClass0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debit_Card1"):
                opp_val = getattr(old_value, "debit_Card1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debit_Card1"):
                opp_val = getattr(value, "debit_Card1", None)
                if opp_val is None:
                    setattr(value, "debit_Card1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def debit_Card9(self):
        return self.__debit_Card9
    @debit_Card9.setter
    def debit_Card9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Debit_Card__debit_Card9", None)
        self.__debit_Card9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debit_Card8"):
                opp_val = getattr(old_value, "debit_Card8", None)
                if opp_val == self:
                    setattr(old_value, "debit_Card8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debit_Card8"):
                opp_val = getattr(value, "debit_Card8", None)
                setattr(value, "debit_Card8", self)



class Customer:

    def __init__(self, Id: str, Name: str, Address: str, debit_Card3: set["Debit_Card"] = None, myClass5: "Bank" = None):
        self.Id = Id
        self.Name = Name
        self.Address = Address
        self.debit_Card3 = debit_Card3 if debit_Card3 is not None else set()
        self.myClass5 = myClass5
        
        pass
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
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: str):
        self.__Id = Id

    @property
    def debit_Card3(self):
        return self.__debit_Card3
    @debit_Card3.setter
    def debit_Card3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__debit_Card3", None)
        self.__debit_Card3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer2"):
                    opp_val = getattr(item, "customer2", None)
                    
                    if opp_val == self:
                        setattr(item, "customer2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer2"):
                    opp_val = getattr(item, "customer2", None)
                    
                    setattr(item, "customer2", self)
                    

    @property
    def myClass5(self):
        return self.__myClass5
    @myClass5.setter
    def myClass5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__myClass5", None)
        self.__myClass5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer4"):
                opp_val = getattr(old_value, "customer4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer4"):
                opp_val = getattr(value, "customer4", None)
                if opp_val is None:
                    setattr(value, "customer4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Bank:

    def __init__(self, BankId: str, location: str, debit_Card1: set["Debit_Card"] = None, customer4: set["Customer"] = None, aTM_INFO6: set["ATM_INFO"] = None):
        self.BankId = BankId
        self.location = location
        self.debit_Card1 = debit_Card1 if debit_Card1 is not None else set()
        self.customer4 = customer4 if customer4 is not None else set()
        self.aTM_INFO6 = aTM_INFO6 if aTM_INFO6 is not None else set()
        
        pass
    @property
    def BankId(self):
        return self.__BankId
    @BankId.setter
    def BankId(self, BankId: str):
        self.__BankId = BankId

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def customer4(self):
        return self.__customer4
    @customer4.setter
    def customer4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bank__customer4", None)
        self.__customer4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myClass5"):
                    opp_val = getattr(item, "myClass5", None)
                    
                    if opp_val == self:
                        setattr(item, "myClass5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myClass5"):
                    opp_val = getattr(item, "myClass5", None)
                    
                    setattr(item, "myClass5", self)
                    

    @property
    def debit_Card1(self):
        return self.__debit_Card1
    @debit_Card1.setter
    def debit_Card1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bank__debit_Card1", None)
        self.__debit_Card1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myClass0"):
                    opp_val = getattr(item, "myClass0", None)
                    
                    if opp_val == self:
                        setattr(item, "myClass0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myClass0"):
                    opp_val = getattr(item, "myClass0", None)
                    
                    setattr(item, "myClass0", self)
                    

    @property
    def aTM_INFO6(self):
        return self.__aTM_INFO6
    @aTM_INFO6.setter
    def aTM_INFO6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bank__aTM_INFO6", None)
        self.__aTM_INFO6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myClass7"):
                    opp_val = getattr(item, "myClass7", None)
                    
                    if opp_val == self:
                        setattr(item, "myClass7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myClass7"):
                    opp_val = getattr(item, "myClass7", None)
                    
                    setattr(item, "myClass7", self)
                    

