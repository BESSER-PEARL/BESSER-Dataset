from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Loan_Account:

    def __init__(self, HolderName: str, Acc_No: int, Loan_No: int, Type: str):
        self.HolderName = HolderName
        self.Acc_No = Acc_No
        self.Loan_No = Loan_No
        self.Type = Type
        
        pass
    @property
    def HolderName(self):
        return self.__HolderName
    @HolderName.setter
    def HolderName(self, HolderName: str):
        self.__HolderName = HolderName

    @property
    def Acc_No(self):
        return self.__Acc_No
    @Acc_No.setter
    def Acc_No(self, Acc_No: int):
        self.__Acc_No = Acc_No

    @property
    def Loan_No(self):
        return self.__Loan_No
    @Loan_No.setter
    def Loan_No(self, Loan_No: int):
        self.__Loan_No = Loan_No

    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type



class Savings_Account:

    def __init__(self, Holder_Name: str, AccNo: int, PIn: Savings_Account):
        self.Holder_Name = Holder_Name
        self.AccNo = AccNo
        self.PIn = PIn
        
        pass
    @property
    def Holder_Name(self):
        return self.__Holder_Name
    @Holder_Name.setter
    def Holder_Name(self, Holder_Name: str):
        self.__Holder_Name = Holder_Name

    @property
    def PIn(self):
        return self.__PIn
    @PIn.setter
    def PIn(self, PIn: Savings_Account):
        self.__PIn = PIn

    @property
    def AccNo(self):
        return self.__AccNo
    @AccNo.setter
    def AccNo(self, AccNo: int):
        self.__AccNo = AccNo



class CurrentAccount:

    def __init__(self, HolderName: str, AccNo: int, PIn: int):
        self.HolderName = HolderName
        self.AccNo = AccNo
        self.PIn = PIn
        
        pass
    @property
    def PIn(self):
        return self.__PIn
    @PIn.setter
    def PIn(self, PIn: int):
        self.__PIn = PIn

    @property
    def HolderName(self):
        return self.__HolderName
    @HolderName.setter
    def HolderName(self, HolderName: str):
        self.__HolderName = HolderName

    @property
    def AccNo(self):
        return self.__AccNo
    @AccNo.setter
    def AccNo(self, AccNo: int):
        self.__AccNo = AccNo



class ATM_s:

    def __init__(self, PIN: int, OperatorName: str, Withdrawn: int, bank1: "Bank" = None):
        self.PIN = PIN
        self.OperatorName = OperatorName
        self.Withdrawn = Withdrawn
        self.bank1 = bank1
        
        pass
    @property
    def Withdrawn(self):
        return self.__Withdrawn
    @Withdrawn.setter
    def Withdrawn(self, Withdrawn: int):
        self.__Withdrawn = Withdrawn

    @property
    def OperatorName(self):
        return self.__OperatorName
    @OperatorName.setter
    def OperatorName(self, OperatorName: str):
        self.__OperatorName = OperatorName

    @property
    def PIN(self):
        return self.__PIN
    @PIN.setter
    def PIN(self, PIN: int):
        self.__PIN = PIN

    @property
    def bank1(self):
        return self.__bank1
    @bank1.setter
    def bank1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ATM_s__bank1", None)
        self.__bank1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aTM_s0"):
                opp_val = getattr(old_value, "aTM_s0", None)
                if opp_val == self:
                    setattr(old_value, "aTM_s0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aTM_s0"):
                opp_val = getattr(value, "aTM_s0", None)
                setattr(value, "aTM_s0", self)



class AccountHolder:

    def __init__(self, Name: str, AccNo: int, Address: str, accounts7: "Accounts" = None):
        self.Name = Name
        self.AccNo = AccNo
        self.Address = Address
        self.accounts7 = accounts7
        
        pass
    @property
    def AccNo(self):
        return self.__AccNo
    @AccNo.setter
    def AccNo(self, AccNo: int):
        self.__AccNo = AccNo

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def accounts7(self):
        return self.__accounts7
    @accounts7.setter
    def accounts7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AccountHolder__accounts7", None)
        self.__accounts7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accountHolder6"):
                opp_val = getattr(old_value, "accountHolder6", None)
                if opp_val == self:
                    setattr(old_value, "accountHolder6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accountHolder6"):
                opp_val = getattr(value, "accountHolder6", None)
                setattr(value, "accountHolder6", self)



class BankEmployee:

    def __init__(self, Name: str, EmployeeID: int, EmpAdd: str, Salary: int, bank3: "Bank" = None):
        self.Name = Name
        self.EmployeeID = EmployeeID
        self.EmpAdd = EmpAdd
        self.Salary = Salary
        self.bank3 = bank3
        
        pass
    @property
    def EmployeeID(self):
        return self.__EmployeeID
    @EmployeeID.setter
    def EmployeeID(self, EmployeeID: int):
        self.__EmployeeID = EmployeeID

    @property
    def EmpAdd(self):
        return self.__EmpAdd
    @EmpAdd.setter
    def EmpAdd(self, EmpAdd: str):
        self.__EmpAdd = EmpAdd

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Salary(self):
        return self.__Salary
    @Salary.setter
    def Salary(self, Salary: int):
        self.__Salary = Salary

    @property
    def bank3(self):
        return self.__bank3
    @bank3.setter
    def bank3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankEmployee__bank3", None)
        self.__bank3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bankEmployee2"):
                opp_val = getattr(old_value, "bankEmployee2", None)
                if opp_val == self:
                    setattr(old_value, "bankEmployee2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bankEmployee2"):
                opp_val = getattr(value, "bankEmployee2", None)
                setattr(value, "bankEmployee2", self)



class Accounts:

    def __init__(self, AccountNo: int, branchCode: str, bank4: "Bank" = None, accountHolder6: "AccountHolder" = None):
        self.AccountNo = AccountNo
        self.branchCode = branchCode
        self.bank4 = bank4
        self.accountHolder6 = accountHolder6
        
        pass
    @property
    def AccountNo(self):
        return self.__AccountNo
    @AccountNo.setter
    def AccountNo(self, AccountNo: int):
        self.__AccountNo = AccountNo

    @property
    def branchCode(self):
        return self.__branchCode
    @branchCode.setter
    def branchCode(self, branchCode: str):
        self.__branchCode = branchCode

    @property
    def bank4(self):
        return self.__bank4
    @bank4.setter
    def bank4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Accounts__bank4", None)
        self.__bank4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounts5"):
                opp_val = getattr(old_value, "accounts5", None)
                if opp_val == self:
                    setattr(old_value, "accounts5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounts5"):
                opp_val = getattr(value, "accounts5", None)
                setattr(value, "accounts5", self)

    @property
    def accountHolder6(self):
        return self.__accountHolder6
    @accountHolder6.setter
    def accountHolder6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Accounts__accountHolder6", None)
        self.__accountHolder6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounts7"):
                opp_val = getattr(old_value, "accounts7", None)
                if opp_val == self:
                    setattr(old_value, "accounts7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounts7"):
                opp_val = getattr(value, "accounts7", None)
                setattr(value, "accounts7", self)



class Bank:

    def __init__(self, Name_string: str, Name: str, ID: int, locality: str, aTM_s0: "ATM_s" = None, bankEmployee2: "BankEmployee" = None, accounts5: "Accounts" = None):
        self.Name_string = Name_string
        self.Name = Name
        self.ID = ID
        self.locality = locality
        self.aTM_s0 = aTM_s0
        self.bankEmployee2 = bankEmployee2
        self.accounts5 = accounts5
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def locality(self):
        return self.__locality
    @locality.setter
    def locality(self, locality: str):
        self.__locality = locality

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Name_string(self):
        return self.__Name_string
    @Name_string.setter
    def Name_string(self, Name_string: str):
        self.__Name_string = Name_string

    @property
    def bankEmployee2(self):
        return self.__bankEmployee2
    @bankEmployee2.setter
    def bankEmployee2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bank__bankEmployee2", None)
        self.__bankEmployee2 = value
        
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
    def aTM_s0(self):
        return self.__aTM_s0
    @aTM_s0.setter
    def aTM_s0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bank__aTM_s0", None)
        self.__aTM_s0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank1"):
                opp_val = getattr(old_value, "bank1", None)
                if opp_val == self:
                    setattr(old_value, "bank1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank1"):
                opp_val = getattr(value, "bank1", None)
                setattr(value, "bank1", self)

    @property
    def accounts5(self):
        return self.__accounts5
    @accounts5.setter
    def accounts5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bank__accounts5", None)
        self.__accounts5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank4"):
                opp_val = getattr(old_value, "bank4", None)
                if opp_val == self:
                    setattr(old_value, "bank4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank4"):
                opp_val = getattr(value, "bank4", None)
                setattr(value, "bank4", self)

