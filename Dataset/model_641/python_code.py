from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CustomerType(Enum):
    Youth = "Youth"
    Adult = "Adult"
    Senior = "Senior"


############################################
# Definition of Classes
############################################

class Employee:

    pass
class Account:

    pass
class BankingSystem_Saving(Account):

    def __init__(self, interestRate: float):
        self.interestRate = interestRate
        
    @property
    def interestRate(self) -> float:
        return self.__interestRate

    @interestRate.setter
    def interestRate(self, interestRate: float):
        self.__interestRate = interestRate

class BankingSystem_Chequing(Account):

    pass
class BankingSystem_Financial_Representative(Employee):

    pass
class BankingSystem_Loan:

    def __init__(self, loanNumber: str, amount: float, interestRate: float, duration: int, Loan: "BankingSystem_Customer" = None, loans: "BankingSystem_Customer" = None):
        self.loanNumber = loanNumber
        self.amount = amount
        self.interestRate = interestRate
        self.duration = duration
        self.Loan = Loan
        self.loans = loans
        
    @property
    def loanNumber(self) -> str:
        return self.__loanNumber

    @loanNumber.setter
    def loanNumber(self, loanNumber: str):
        self.__loanNumber = loanNumber

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def interestRate(self) -> float:
        return self.__interestRate

    @interestRate.setter
    def interestRate(self, interestRate: float):
        self.__interestRate = interestRate

    @property
    def amount(self) -> float:
        return self.__amount

    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount

    @property
    def Loan(self):
        return self.__Loan

    @Loan.setter
    def Loan(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankingSystem_Loan__Loan", None)
        self.__Loan = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer9"):
                opp_val = getattr(old_value, "customer9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer9"):
                opp_val = getattr(value, "customer9", None)
                if opp_val is None:
                    setattr(value, "customer9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def loans(self):
        return self.__loans

    @loans.setter
    def loans(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankingSystem_Loan__loans", None)
        self.__loans = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer16"):
                opp_val = getattr(old_value, "Customer16", None)
                if opp_val == self:
                    setattr(old_value, "Customer16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer16"):
                opp_val = getattr(value, "Customer16", None)
                setattr(value, "Customer16", self)

class BankingSystem_Account(ABC):

    def __init__(self, accountNumber: str, balance: float, Account: "BankingSystem_Customer" = None, accounts: "BankingSystem_Customer" = None):
        self.accountNumber = accountNumber
        self.balance = balance
        self.Account = Account
        self.accounts = accounts
        
    @property
    def accountNumber(self) -> str:
        return self.__accountNumber

    @accountNumber.setter
    def accountNumber(self, accountNumber: str):
        self.__accountNumber = accountNumber

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, balance: float):
        self.__balance = balance

    @property
    def Account(self):
        return self.__Account

    @Account.setter
    def Account(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankingSystem_Account__Account", None)
        self.__Account = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer"):
                opp_val = getattr(old_value, "customer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer"):
                opp_val = getattr(value, "customer", None)
                if opp_val is None:
                    setattr(value, "customer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def accounts(self):
        return self.__accounts

    @accounts.setter
    def accounts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankingSystem_Account__accounts", None)
        self.__accounts = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer12"):
                opp_val = getattr(old_value, "Customer12", None)
                if opp_val == self:
                    setattr(old_value, "Customer12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer12"):
                opp_val = getattr(value, "Customer12", None)
                setattr(value, "Customer12", self)

class BankingSystem_Customer:

    def __init__(self, name: str, age: int, address: str, phoneNumber: str, customerType: str, Customer: "BankingSystem_Branch" = None, customers: "BankingSystem_Branch" = None, customer: set["BankingSystem_Account"] = None, customer9: set["BankingSystem_Loan"] = None, a: set["BankingSystem_Financial_Representative"] = None, Customer12: "BankingSystem_Account" = None, Customer16: "BankingSystem_Loan" = None, Customer18: "BankingSystem_Financial_Representative" = None):
        self.name = name
        self.age = age
        self.address = address
        self.phoneNumber = phoneNumber
        self.customerType = customerType
        self.Customer = Customer
        self.customers = customers
        self.customer = customer if customer is not None else set()
        self.customer9 = customer9 if customer9 is not None else set()
        self.a = a if a is not None else set()
        self.Customer12 = Customer12
        self.Customer16 = Customer16
        self.Customer18 = Customer18
        
    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def customerType(self) -> str:
        return self.__customerType

    @customerType.setter
    def customerType(self, customerType: str):
        self.__customerType = customerType

    @property
    def phoneNumber(self) -> str:
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def Customer16(self):
        return self.__Customer16

    @Customer16.setter
    def Customer16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankingSystem_Customer__Customer16", None)
        self.__Customer16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "loans"):
                opp_val = getattr(old_value, "loans", None)
                if opp_val == self:
                    setattr(old_value, "loans", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "loans"):
                opp_val = getattr(value, "loans", None)
                setattr(value, "loans", self)

    @property
    def Customer12(self):
        return self.__Customer12

    @Customer12.setter
    def Customer12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankingSystem_Customer__Customer12", None)
        self.__Customer12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounts"):
                opp_val = getattr(old_value, "accounts", None)
                if opp_val == self:
                    setattr(old_value, "accounts", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounts"):
                opp_val = getattr(value, "accounts", None)
                setattr(value, "accounts", self)

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankingSystem_Customer__a", None)
        self.__a = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Financial_Representative"):
                    opp_val = getattr(item, "Financial_Representative", None)
                    
                    if opp_val == self:
                        setattr(item, "Financial_Representative", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Financial_Representative"):
                    opp_val = getattr(item, "Financial_Representative", None)
                    
                    setattr(item, "Financial_Representative", self)
                    

    @property
    def customer9(self):
        return self.__customer9

    @customer9.setter
    def customer9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankingSystem_Customer__customer9", None)
        self.__customer9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Loan"):
                    opp_val = getattr(item, "Loan", None)
                    
                    if opp_val == self:
                        setattr(item, "Loan", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Loan"):
                    opp_val = getattr(item, "Loan", None)
                    
                    setattr(item, "Loan", self)
                    

    @property
    def Customer18(self):
        return self.__Customer18

    @Customer18.setter
    def Customer18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankingSystem_Customer__Customer18", None)
        self.__Customer18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "representative"):
                opp_val = getattr(old_value, "representative", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "representative"):
                opp_val = getattr(value, "representative", None)
                if opp_val is None:
                    setattr(value, "representative", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankingSystem_Customer__customer", None)
        self.__customer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Account"):
                    opp_val = getattr(item, "Account", None)
                    
                    if opp_val == self:
                        setattr(item, "Account", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Account"):
                    opp_val = getattr(item, "Account", None)
                    
                    setattr(item, "Account", self)
                    

    @property
    def customers(self):
        return self.__customers

    @customers.setter
    def customers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankingSystem_Customer__customers", None)
        self.__customers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Branch6"):
                opp_val = getattr(old_value, "Branch6", None)
                if opp_val == self:
                    setattr(old_value, "Branch6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Branch6"):
                opp_val = getattr(value, "Branch6", None)
                setattr(value, "Branch6", self)

    @property
    def Customer(self):
        return self.__Customer

    @Customer.setter
    def Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankingSystem_Customer__Customer", None)
        self.__Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "branch"):
                opp_val = getattr(old_value, "branch", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "branch"):
                opp_val = getattr(value, "branch", None)
                if opp_val is None:
                    setattr(value, "branch", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BankingSystem_Branch:

    def __init__(self, name: str, branchId: int, location: str, phoneNumber: str, branch3: set["BankingSystem_Employee"] = None, branches: "BankingSystem_Bank" = None, Branch: "BankingSystem_Bank" = None, branch: set["BankingSystem_Customer"] = None, Branch14: "BankingSystem_Employee" = None, Branch6: "BankingSystem_Customer" = None):
        self.name = name
        self.branchId = branchId
        self.location = location
        self.phoneNumber = phoneNumber
        self.branch3 = branch3 if branch3 is not None else set()
        self.branches = branches
        self.Branch = Branch
        self.branch = branch if branch is not None else set()
        self.Branch14 = Branch14
        self.Branch6 = Branch6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def branchId(self) -> int:
        return self.__branchId

    @branchId.setter
    def branchId(self, branchId: int):
        self.__branchId = branchId

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def phoneNumber(self) -> str:
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber

    @property
    def Branch14(self):
        return self.__Branch14

    @Branch14.setter
    def Branch14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankingSystem_Branch__Branch14", None)
        self.__Branch14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employees"):
                opp_val = getattr(old_value, "employees", None)
                if opp_val == self:
                    setattr(old_value, "employees", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employees"):
                opp_val = getattr(value, "employees", None)
                setattr(value, "employees", self)

    @property
    def Branch(self):
        return self.__Branch

    @Branch.setter
    def Branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankingSystem_Branch__Branch", None)
        self.__Branch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank"):
                opp_val = getattr(old_value, "bank", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank"):
                opp_val = getattr(value, "bank", None)
                if opp_val is None:
                    setattr(value, "bank", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def branch3(self):
        return self.__branch3

    @branch3.setter
    def branch3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankingSystem_Branch__branch3", None)
        self.__branch3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee"):
                    opp_val = getattr(item, "Employee", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee"):
                    opp_val = getattr(item, "Employee", None)
                    
                    setattr(item, "Employee", self)
                    

    @property
    def branches(self):
        return self.__branches

    @branches.setter
    def branches(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankingSystem_Branch__branches", None)
        self.__branches = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Bank"):
                opp_val = getattr(old_value, "Bank", None)
                if opp_val == self:
                    setattr(old_value, "Bank", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Bank"):
                opp_val = getattr(value, "Bank", None)
                setattr(value, "Bank", self)

    @property
    def Branch6(self):
        return self.__Branch6

    @Branch6.setter
    def Branch6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankingSystem_Branch__Branch6", None)
        self.__Branch6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customers"):
                opp_val = getattr(old_value, "customers", None)
                if opp_val == self:
                    setattr(old_value, "customers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customers"):
                opp_val = getattr(value, "customers", None)
                setattr(value, "customers", self)

    @property
    def branch(self):
        return self.__branch

    @branch.setter
    def branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankingSystem_Branch__branch", None)
        self.__branch = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Customer"):
                    opp_val = getattr(item, "Customer", None)
                    
                    if opp_val == self:
                        setattr(item, "Customer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Customer"):
                    opp_val = getattr(item, "Customer", None)
                    
                    setattr(item, "Customer", self)
                    

class BankingSystem_Bank:

    def __init__(self, name: str, bankId: int, description: str, Bank: "BankingSystem_Branch" = None, bank: set["BankingSystem_Branch"] = None):
        self.name = name
        self.bankId = bankId
        self.description = description
        self.Bank = Bank
        self.bank = bank if bank is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bankId(self) -> int:
        return self.__bankId

    @bankId.setter
    def bankId(self, bankId: int):
        self.__bankId = bankId

    @property
    def bank(self):
        return self.__bank

    @bank.setter
    def bank(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankingSystem_Bank__bank", None)
        self.__bank = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Branch"):
                    opp_val = getattr(item, "Branch", None)
                    
                    if opp_val == self:
                        setattr(item, "Branch", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Branch"):
                    opp_val = getattr(item, "Branch", None)
                    
                    setattr(item, "Branch", self)
                    

    @property
    def Bank(self):
        return self.__Bank

    @Bank.setter
    def Bank(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankingSystem_Bank__Bank", None)
        self.__Bank = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "branches"):
                opp_val = getattr(old_value, "branches", None)
                if opp_val == self:
                    setattr(old_value, "branches", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "branches"):
                opp_val = getattr(value, "branches", None)
                setattr(value, "branches", self)

class BankingSystem_Employee(ABC):

    def __init__(self, ename: str, isCustomer: bool, eage: int, eaddress: str, ephoneNumber: str, eid: int, Employee: "BankingSystem_Branch" = None, employees: "BankingSystem_Branch" = None):
        self.ename = ename
        self.isCustomer = isCustomer
        self.eage = eage
        self.eaddress = eaddress
        self.ephoneNumber = ephoneNumber
        self.eid = eid
        self.Employee = Employee
        self.employees = employees
        
    @property
    def ename(self) -> str:
        return self.__ename

    @ename.setter
    def ename(self, ename: str):
        self.__ename = ename

    @property
    def eid(self) -> int:
        return self.__eid

    @eid.setter
    def eid(self, eid: int):
        self.__eid = eid

    @property
    def isCustomer(self) -> bool:
        return self.__isCustomer

    @isCustomer.setter
    def isCustomer(self, isCustomer: bool):
        self.__isCustomer = isCustomer

    @property
    def eaddress(self) -> str:
        return self.__eaddress

    @eaddress.setter
    def eaddress(self, eaddress: str):
        self.__eaddress = eaddress

    @property
    def eage(self) -> int:
        return self.__eage

    @eage.setter
    def eage(self, eage: int):
        self.__eage = eage

    @property
    def ephoneNumber(self) -> str:
        return self.__ephoneNumber

    @ephoneNumber.setter
    def ephoneNumber(self, ephoneNumber: str):
        self.__ephoneNumber = ephoneNumber

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankingSystem_Employee__employees", None)
        self.__employees = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Branch14"):
                opp_val = getattr(old_value, "Branch14", None)
                if opp_val == self:
                    setattr(old_value, "Branch14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Branch14"):
                opp_val = getattr(value, "Branch14", None)
                setattr(value, "Branch14", self)

    @property
    def Employee(self):
        return self.__Employee

    @Employee.setter
    def Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BankingSystem_Employee__Employee", None)
        self.__Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "branch3"):
                opp_val = getattr(old_value, "branch3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "branch3"):
                opp_val = getattr(value, "branch3", None)
                if opp_val is None:
                    setattr(value, "branch3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
