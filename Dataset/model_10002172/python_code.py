from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Contractor:

    pass





class Indevidual:

    pass


class Business:

    pass


class Permanent:

    pass


class Temporary:

    pass


class CheckingAccount:

    def __init__(self, CustomerId: int, AccountNo: int, AccountType: str, Amount: str, Cust_Name: str, Cust_DOB: str, MobileNo: int, Diposit: str, Withdraw: str, customer7: "Customer" = None):
        self.CustomerId = CustomerId
        self.AccountNo = AccountNo
        self.AccountType = AccountType
        self.Amount = Amount
        self.Cust_Name = Cust_Name
        self.Cust_DOB = Cust_DOB
        self.MobileNo = MobileNo
        self.Diposit = Diposit
        self.Withdraw = Withdraw
        self.customer7 = customer7
        
        pass
    @property
    def AccountNo(self):
        return self.__AccountNo
    @AccountNo.setter
    def AccountNo(self, AccountNo: int):
        self.__AccountNo = AccountNo

    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: str):
        self.__Amount = Amount

    @property
    def Cust_Name(self):
        return self.__Cust_Name
    @Cust_Name.setter
    def Cust_Name(self, Cust_Name: str):
        self.__Cust_Name = Cust_Name

    @property
    def Cust_DOB(self):
        return self.__Cust_DOB
    @Cust_DOB.setter
    def Cust_DOB(self, Cust_DOB: str):
        self.__Cust_DOB = Cust_DOB

    @property
    def CustomerId(self):
        return self.__CustomerId
    @CustomerId.setter
    def CustomerId(self, CustomerId: int):
        self.__CustomerId = CustomerId

    @property
    def Withdraw(self):
        return self.__Withdraw
    @Withdraw.setter
    def Withdraw(self, Withdraw: str):
        self.__Withdraw = Withdraw

    @property
    def AccountType(self):
        return self.__AccountType
    @AccountType.setter
    def AccountType(self, AccountType: str):
        self.__AccountType = AccountType

    @property
    def MobileNo(self):
        return self.__MobileNo
    @MobileNo.setter
    def MobileNo(self, MobileNo: int):
        self.__MobileNo = MobileNo

    @property
    def Diposit(self):
        return self.__Diposit
    @Diposit.setter
    def Diposit(self, Diposit: str):
        self.__Diposit = Diposit

    @property
    def customer7(self):
        return self.__customer7
    @customer7.setter
    def customer7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CheckingAccount__customer7", None)
        self.__customer7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "checking_Account6"):
                opp_val = getattr(old_value, "checking_Account6", None)
                if opp_val == self:
                    setattr(old_value, "checking_Account6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "checking_Account6"):
                opp_val = getattr(value, "checking_Account6", None)
                setattr(value, "checking_Account6", self)



class SavingsAccount:

    def __init__(self, CustomerId: int, AccountNo: int, AccountType: str, Amount: str, Cust_Name: str, Cust_DOB: str, Mobile: int, Withdraw: str, Diposit: str, customer5: "Customer" = None):
        self.CustomerId = CustomerId
        self.AccountNo = AccountNo
        self.AccountType = AccountType
        self.Amount = Amount
        self.Cust_Name = Cust_Name
        self.Cust_DOB = Cust_DOB
        self.Mobile = Mobile
        self.Withdraw = Withdraw
        self.Diposit = Diposit
        self.customer5 = customer5
        
        pass
    @property
    def Mobile(self):
        return self.__Mobile
    @Mobile.setter
    def Mobile(self, Mobile: int):
        self.__Mobile = Mobile

    @property
    def Cust_Name(self):
        return self.__Cust_Name
    @Cust_Name.setter
    def Cust_Name(self, Cust_Name: str):
        self.__Cust_Name = Cust_Name

    @property
    def CustomerId(self):
        return self.__CustomerId
    @CustomerId.setter
    def CustomerId(self, CustomerId: int):
        self.__CustomerId = CustomerId

    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: str):
        self.__Amount = Amount

    @property
    def Cust_DOB(self):
        return self.__Cust_DOB
    @Cust_DOB.setter
    def Cust_DOB(self, Cust_DOB: str):
        self.__Cust_DOB = Cust_DOB

    @property
    def Diposit(self):
        return self.__Diposit
    @Diposit.setter
    def Diposit(self, Diposit: str):
        self.__Diposit = Diposit

    @property
    def Withdraw(self):
        return self.__Withdraw
    @Withdraw.setter
    def Withdraw(self, Withdraw: str):
        self.__Withdraw = Withdraw

    @property
    def AccountType(self):
        return self.__AccountType
    @AccountType.setter
    def AccountType(self, AccountType: str):
        self.__AccountType = AccountType

    @property
    def AccountNo(self):
        return self.__AccountNo
    @AccountNo.setter
    def AccountNo(self, AccountNo: int):
        self.__AccountNo = AccountNo

    @property
    def customer5(self):
        return self.__customer5
    @customer5.setter
    def customer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SavingsAccount__customer5", None)
        self.__customer5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "savings_Account4"):
                opp_val = getattr(old_value, "savings_Account4", None)
                if opp_val == self:
                    setattr(old_value, "savings_Account4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "savings_Account4"):
                opp_val = getattr(value, "savings_Account4", None)
                setattr(value, "savings_Account4", self)



class Customer:

    def __init__(self, CustId: int, FName: str, Lname: str, Gender: str, DOB: str, Address: str, attribute: str, State: str, Zipcode: int, Mobile: int, BMS3: "BMS" = None, savings_Account4: "SavingsAccount" = None, checking_Account6: "CheckingAccount" = None):
        self.CustId = CustId
        self.FName = FName
        self.Lname = Lname
        self.Gender = Gender
        self.DOB = DOB
        self.Address = Address
        self.attribute = attribute
        self.State = State
        self.Zipcode = Zipcode
        self.Mobile = Mobile
        self.BMS3 = BMS3
        self.savings_Account4 = savings_Account4
        self.checking_Account6 = checking_Account6
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def CustId(self):
        return self.__CustId
    @CustId.setter
    def CustId(self, CustId: int):
        self.__CustId = CustId

    @property
    def Lname(self):
        return self.__Lname
    @Lname.setter
    def Lname(self, Lname: str):
        self.__Lname = Lname

    @property
    def Gender(self):
        return self.__Gender
    @Gender.setter
    def Gender(self, Gender: str):
        self.__Gender = Gender

    @property
    def FName(self):
        return self.__FName
    @FName.setter
    def FName(self, FName: str):
        self.__FName = FName

    @property
    def Mobile(self):
        return self.__Mobile
    @Mobile.setter
    def Mobile(self, Mobile: int):
        self.__Mobile = Mobile

    @property
    def DOB(self):
        return self.__DOB
    @DOB.setter
    def DOB(self, DOB: str):
        self.__DOB = DOB

    @property
    def State(self):
        return self.__State
    @State.setter
    def State(self, State: str):
        self.__State = State

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Zipcode(self):
        return self.__Zipcode
    @Zipcode.setter
    def Zipcode(self, Zipcode: int):
        self.__Zipcode = Zipcode

    @property
    def BMS3(self):
        return self.__BMS3
    @BMS3.setter
    def BMS3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__BMS3", None)
        self.__BMS3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer2"):
                opp_val = getattr(old_value, "customer2", None)
                if opp_val == self:
                    setattr(old_value, "customer2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer2"):
                opp_val = getattr(value, "customer2", None)
                setattr(value, "customer2", self)

    @property
    def savings_Account4(self):
        return self.__savings_Account4
    @savings_Account4.setter
    def savings_Account4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__savings_Account4", None)
        self.__savings_Account4 = value
        
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

    @property
    def checking_Account6(self):
        return self.__checking_Account6
    @checking_Account6.setter
    def checking_Account6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__checking_Account6", None)
        self.__checking_Account6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer7"):
                opp_val = getattr(old_value, "customer7", None)
                if opp_val == self:
                    setattr(old_value, "customer7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer7"):
                opp_val = getattr(value, "customer7", None)
                setattr(value, "customer7", self)



class Employee:

    def __init__(self, EmpId: int, EmpFName: str, EmpLName: str, DOB: str, Gender: str, Address: str, City: str, State: str, Zipcode: str, EmpType: str, Department: str, BMS1: "BMS" = None):
        self.EmpId = EmpId
        self.EmpFName = EmpFName
        self.EmpLName = EmpLName
        self.DOB = DOB
        self.Gender = Gender
        self.Address = Address
        self.City = City
        self.State = State
        self.Zipcode = Zipcode
        self.EmpType = EmpType
        self.Department = Department
        self.BMS1 = BMS1
        
        pass
    @property
    def Department(self):
        return self.__Department
    @Department.setter
    def Department(self, Department: str):
        self.__Department = Department

    @property
    def EmpType(self):
        return self.__EmpType
    @EmpType.setter
    def EmpType(self, EmpType: str):
        self.__EmpType = EmpType

    @property
    def DOB(self):
        return self.__DOB
    @DOB.setter
    def DOB(self, DOB: str):
        self.__DOB = DOB

    @property
    def City(self):
        return self.__City
    @City.setter
    def City(self, City: str):
        self.__City = City

    @property
    def EmpFName(self):
        return self.__EmpFName
    @EmpFName.setter
    def EmpFName(self, EmpFName: str):
        self.__EmpFName = EmpFName

    @property
    def EmpId(self):
        return self.__EmpId
    @EmpId.setter
    def EmpId(self, EmpId: int):
        self.__EmpId = EmpId

    @property
    def EmpLName(self):
        return self.__EmpLName
    @EmpLName.setter
    def EmpLName(self, EmpLName: str):
        self.__EmpLName = EmpLName

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def State(self):
        return self.__State
    @State.setter
    def State(self, State: str):
        self.__State = State

    @property
    def Zipcode(self):
        return self.__Zipcode
    @Zipcode.setter
    def Zipcode(self, Zipcode: str):
        self.__Zipcode = Zipcode

    @property
    def Gender(self):
        return self.__Gender
    @Gender.setter
    def Gender(self, Gender: str):
        self.__Gender = Gender

    @property
    def BMS1(self):
        return self.__BMS1
    @BMS1.setter
    def BMS1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__BMS1", None)
        self.__BMS1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee0"):
                opp_val = getattr(old_value, "employee0", None)
                if opp_val == self:
                    setattr(old_value, "employee0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee0"):
                opp_val = getattr(value, "employee0", None)
                setattr(value, "employee0", self)



class BMS:

    pass
