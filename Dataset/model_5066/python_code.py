from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class accounting_Serializable(ABC):

    pass
class accounting_JournalStatement:

    def __init__(self, description: str, date: str, amount: str, accounting_JournalStatement: "accounting_JournalGroup" = None, accounting_JournalStatement18: "accounting_Account" = None, accounting_JournalStatement21: "accounting_Account" = None, accounting_JournalStatement24: "accounting_Vat" = None):
        self.description = description
        self.date = date
        self.amount = amount
        self.accounting_JournalStatement = accounting_JournalStatement
        self.accounting_JournalStatement18 = accounting_JournalStatement18
        self.accounting_JournalStatement21 = accounting_JournalStatement21
        self.accounting_JournalStatement24 = accounting_JournalStatement24
        
    @property
    def amount(self) -> str:
        return self.__amount

    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def date(self) -> str:
        return self.__date

    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def accounting_JournalStatement24(self):
        return self.__accounting_JournalStatement24

    @accounting_JournalStatement24.setter
    def accounting_JournalStatement24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_JournalStatement__accounting_JournalStatement24", None)
        self.__accounting_JournalStatement24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_Vat25"):
                opp_val = getattr(old_value, "accounting_Vat25", None)
                if opp_val == self:
                    setattr(old_value, "accounting_Vat25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_Vat25"):
                opp_val = getattr(value, "accounting_Vat25", None)
                setattr(value, "accounting_Vat25", self)

    @property
    def accounting_JournalStatement21(self):
        return self.__accounting_JournalStatement21

    @accounting_JournalStatement21.setter
    def accounting_JournalStatement21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_JournalStatement__accounting_JournalStatement21", None)
        self.__accounting_JournalStatement21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_Account22"):
                opp_val = getattr(old_value, "accounting_Account22", None)
                if opp_val == self:
                    setattr(old_value, "accounting_Account22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_Account22"):
                opp_val = getattr(value, "accounting_Account22", None)
                setattr(value, "accounting_Account22", self)

    @property
    def accounting_JournalStatement18(self):
        return self.__accounting_JournalStatement18

    @accounting_JournalStatement18.setter
    def accounting_JournalStatement18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_JournalStatement__accounting_JournalStatement18", None)
        self.__accounting_JournalStatement18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_Account19"):
                opp_val = getattr(old_value, "accounting_Account19", None)
                if opp_val == self:
                    setattr(old_value, "accounting_Account19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_Account19"):
                opp_val = getattr(value, "accounting_Account19", None)
                setattr(value, "accounting_Account19", self)

    @property
    def accounting_JournalStatement(self):
        return self.__accounting_JournalStatement

    @accounting_JournalStatement.setter
    def accounting_JournalStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_JournalStatement__accounting_JournalStatement", None)
        self.__accounting_JournalStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_JournalGroup16"):
                opp_val = getattr(old_value, "accounting_JournalGroup16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_JournalGroup16"):
                opp_val = getattr(value, "accounting_JournalGroup16", None)
                if opp_val is None:
                    setattr(value, "accounting_JournalGroup16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class accounting_ReportGroup:

    def __init__(self, name: str, ReportGroup: "accounting_BalanceAccount" = None, accounting_ReportGroup: "accounting_Report" = None, accounting_ReportGroup30: "accounting_Report" = None, accounting_ReportGroup33: "accounting_ReportGroup" = None, accounting_ReportGroup31: set["accounting_ReportGroup"] = None, report: set["accounting_BalanceAccount"] = None):
        self.name = name
        self.ReportGroup = ReportGroup
        self.accounting_ReportGroup = accounting_ReportGroup
        self.accounting_ReportGroup30 = accounting_ReportGroup30
        self.accounting_ReportGroup33 = accounting_ReportGroup33
        self.accounting_ReportGroup31 = accounting_ReportGroup31 if accounting_ReportGroup31 is not None else set()
        self.report = report if report is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def accounting_ReportGroup30(self):
        return self.__accounting_ReportGroup30

    @accounting_ReportGroup30.setter
    def accounting_ReportGroup30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_ReportGroup__accounting_ReportGroup30", None)
        self.__accounting_ReportGroup30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_Report29"):
                opp_val = getattr(old_value, "accounting_Report29", None)
                if opp_val == self:
                    setattr(old_value, "accounting_Report29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_Report29"):
                opp_val = getattr(value, "accounting_Report29", None)
                setattr(value, "accounting_Report29", self)

    @property
    def report(self):
        return self.__report

    @report.setter
    def report(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_ReportGroup__report", None)
        self.__report = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BalanceAccount"):
                    opp_val = getattr(item, "BalanceAccount", None)
                    
                    if opp_val == self:
                        setattr(item, "BalanceAccount", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BalanceAccount"):
                    opp_val = getattr(item, "BalanceAccount", None)
                    
                    setattr(item, "BalanceAccount", self)
                    

    @property
    def accounting_ReportGroup31(self):
        return self.__accounting_ReportGroup31

    @accounting_ReportGroup31.setter
    def accounting_ReportGroup31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_ReportGroup__accounting_ReportGroup31", None)
        self.__accounting_ReportGroup31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "accounting_ReportGroup33"):
                    opp_val = getattr(item, "accounting_ReportGroup33", None)
                    
                    if opp_val == self:
                        setattr(item, "accounting_ReportGroup33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "accounting_ReportGroup33"):
                    opp_val = getattr(item, "accounting_ReportGroup33", None)
                    
                    setattr(item, "accounting_ReportGroup33", self)
                    

    @property
    def accounting_ReportGroup(self):
        return self.__accounting_ReportGroup

    @accounting_ReportGroup.setter
    def accounting_ReportGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_ReportGroup__accounting_ReportGroup", None)
        self.__accounting_ReportGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_Report27"):
                opp_val = getattr(old_value, "accounting_Report27", None)
                if opp_val == self:
                    setattr(old_value, "accounting_Report27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_Report27"):
                opp_val = getattr(value, "accounting_Report27", None)
                setattr(value, "accounting_Report27", self)

    @property
    def ReportGroup(self):
        return self.__ReportGroup

    @ReportGroup.setter
    def ReportGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_ReportGroup__ReportGroup", None)
        self.__ReportGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account"):
                opp_val = getattr(old_value, "account", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account"):
                opp_val = getattr(value, "account", None)
                if opp_val is None:
                    setattr(value, "account", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def accounting_ReportGroup33(self):
        return self.__accounting_ReportGroup33

    @accounting_ReportGroup33.setter
    def accounting_ReportGroup33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_ReportGroup__accounting_ReportGroup33", None)
        self.__accounting_ReportGroup33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_ReportGroup31"):
                opp_val = getattr(old_value, "accounting_ReportGroup31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_ReportGroup31"):
                opp_val = getattr(value, "accounting_ReportGroup31", None)
                if opp_val is None:
                    setattr(value, "accounting_ReportGroup31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Account:

    pass
class accounting_PLAccount(Account):

    pass
class accounting_JournalGroup:

    def __init__(self, name: str, accounting_JournalGroup: "accounting_Accounting" = None, accounting_JournalGroup14: "accounting_JournalGroup" = None, accounting_JournalGroup12: set["accounting_JournalGroup"] = None, accounting_JournalGroup16: set["accounting_JournalStatement"] = None):
        self.name = name
        self.accounting_JournalGroup = accounting_JournalGroup
        self.accounting_JournalGroup14 = accounting_JournalGroup14
        self.accounting_JournalGroup12 = accounting_JournalGroup12 if accounting_JournalGroup12 is not None else set()
        self.accounting_JournalGroup16 = accounting_JournalGroup16 if accounting_JournalGroup16 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def accounting_JournalGroup14(self):
        return self.__accounting_JournalGroup14

    @accounting_JournalGroup14.setter
    def accounting_JournalGroup14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_JournalGroup__accounting_JournalGroup14", None)
        self.__accounting_JournalGroup14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_JournalGroup12"):
                opp_val = getattr(old_value, "accounting_JournalGroup12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_JournalGroup12"):
                opp_val = getattr(value, "accounting_JournalGroup12", None)
                if opp_val is None:
                    setattr(value, "accounting_JournalGroup12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def accounting_JournalGroup(self):
        return self.__accounting_JournalGroup

    @accounting_JournalGroup.setter
    def accounting_JournalGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_JournalGroup__accounting_JournalGroup", None)
        self.__accounting_JournalGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_Accounting10"):
                opp_val = getattr(old_value, "accounting_Accounting10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_Accounting10"):
                opp_val = getattr(value, "accounting_Accounting10", None)
                if opp_val is None:
                    setattr(value, "accounting_Accounting10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def accounting_JournalGroup12(self):
        return self.__accounting_JournalGroup12

    @accounting_JournalGroup12.setter
    def accounting_JournalGroup12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_JournalGroup__accounting_JournalGroup12", None)
        self.__accounting_JournalGroup12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "accounting_JournalGroup14"):
                    opp_val = getattr(item, "accounting_JournalGroup14", None)
                    
                    if opp_val == self:
                        setattr(item, "accounting_JournalGroup14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "accounting_JournalGroup14"):
                    opp_val = getattr(item, "accounting_JournalGroup14", None)
                    
                    setattr(item, "accounting_JournalGroup14", self)
                    

    @property
    def accounting_JournalGroup16(self):
        return self.__accounting_JournalGroup16

    @accounting_JournalGroup16.setter
    def accounting_JournalGroup16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_JournalGroup__accounting_JournalGroup16", None)
        self.__accounting_JournalGroup16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "accounting_JournalStatement"):
                    opp_val = getattr(item, "accounting_JournalStatement", None)
                    
                    if opp_val == self:
                        setattr(item, "accounting_JournalStatement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "accounting_JournalStatement"):
                    opp_val = getattr(item, "accounting_JournalStatement", None)
                    
                    setattr(item, "accounting_JournalStatement", self)
                    

class accounting_Report:

    def __init__(self, name: str, accounting_Report: "accounting_Accounting" = None, accounting_Report27: "accounting_ReportGroup" = None, accounting_Report29: "accounting_ReportGroup" = None):
        self.name = name
        self.accounting_Report = accounting_Report
        self.accounting_Report27 = accounting_Report27
        self.accounting_Report29 = accounting_Report29
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def accounting_Report27(self):
        return self.__accounting_Report27

    @accounting_Report27.setter
    def accounting_Report27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Report__accounting_Report27", None)
        self.__accounting_Report27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_ReportGroup"):
                opp_val = getattr(old_value, "accounting_ReportGroup", None)
                if opp_val == self:
                    setattr(old_value, "accounting_ReportGroup", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_ReportGroup"):
                opp_val = getattr(value, "accounting_ReportGroup", None)
                setattr(value, "accounting_ReportGroup", self)

    @property
    def accounting_Report(self):
        return self.__accounting_Report

    @accounting_Report.setter
    def accounting_Report(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Report__accounting_Report", None)
        self.__accounting_Report = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_Accounting8"):
                opp_val = getattr(old_value, "accounting_Accounting8", None)
                if opp_val == self:
                    setattr(old_value, "accounting_Accounting8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_Accounting8"):
                opp_val = getattr(value, "accounting_Accounting8", None)
                setattr(value, "accounting_Accounting8", self)

    @property
    def accounting_Report29(self):
        return self.__accounting_Report29

    @accounting_Report29.setter
    def accounting_Report29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Report__accounting_Report29", None)
        self.__accounting_Report29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_ReportGroup30"):
                opp_val = getattr(old_value, "accounting_ReportGroup30", None)
                if opp_val == self:
                    setattr(old_value, "accounting_ReportGroup30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_ReportGroup30"):
                opp_val = getattr(value, "accounting_ReportGroup30", None)
                setattr(value, "accounting_ReportGroup30", self)

class accounting_BalanceAccount(Account):

    pass
class accounting_Vat:

    def __init__(self, name: str, rate: str, accounting_Vat: "accounting_Accounting" = None, accounting_Vat25: "accounting_JournalStatement" = None):
        self.name = name
        self.rate = rate
        self.accounting_Vat = accounting_Vat
        self.accounting_Vat25 = accounting_Vat25
        
    @property
    def rate(self) -> str:
        return self.__rate

    @rate.setter
    def rate(self, rate: str):
        self.__rate = rate

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def accounting_Vat(self):
        return self.__accounting_Vat

    @accounting_Vat.setter
    def accounting_Vat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Vat__accounting_Vat", None)
        self.__accounting_Vat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_Accounting4"):
                opp_val = getattr(old_value, "accounting_Accounting4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_Accounting4"):
                opp_val = getattr(value, "accounting_Accounting4", None)
                if opp_val is None:
                    setattr(value, "accounting_Accounting4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def accounting_Vat25(self):
        return self.__accounting_Vat25

    @accounting_Vat25.setter
    def accounting_Vat25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Vat__accounting_Vat25", None)
        self.__accounting_Vat25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_JournalStatement24"):
                opp_val = getattr(old_value, "accounting_JournalStatement24", None)
                if opp_val == self:
                    setattr(old_value, "accounting_JournalStatement24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_JournalStatement24"):
                opp_val = getattr(value, "accounting_JournalStatement24", None)
                setattr(value, "accounting_JournalStatement24", self)

class Serializable:

    pass
class accounting_Accounting(Serializable):

    def __init__(self, name: str, accounting_Accounting: set["accounting_AccountGroup"] = None, accounting_Accounting4: set["accounting_Vat"] = None, accounting_Accounting6: "accounting_BalanceAccount" = None, accounting_Accounting8: "accounting_Report" = None, accounting_Accounting10: set["accounting_JournalGroup"] = None):
        self.name = name
        self.accounting_Accounting = accounting_Accounting if accounting_Accounting is not None else set()
        self.accounting_Accounting4 = accounting_Accounting4 if accounting_Accounting4 is not None else set()
        self.accounting_Accounting6 = accounting_Accounting6
        self.accounting_Accounting8 = accounting_Accounting8
        self.accounting_Accounting10 = accounting_Accounting10 if accounting_Accounting10 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def accounting_Accounting6(self):
        return self.__accounting_Accounting6

    @accounting_Accounting6.setter
    def accounting_Accounting6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Accounting__accounting_Accounting6", None)
        self.__accounting_Accounting6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_BalanceAccount"):
                opp_val = getattr(old_value, "accounting_BalanceAccount", None)
                if opp_val == self:
                    setattr(old_value, "accounting_BalanceAccount", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_BalanceAccount"):
                opp_val = getattr(value, "accounting_BalanceAccount", None)
                setattr(value, "accounting_BalanceAccount", self)

    @property
    def accounting_Accounting8(self):
        return self.__accounting_Accounting8

    @accounting_Accounting8.setter
    def accounting_Accounting8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Accounting__accounting_Accounting8", None)
        self.__accounting_Accounting8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_Report"):
                opp_val = getattr(old_value, "accounting_Report", None)
                if opp_val == self:
                    setattr(old_value, "accounting_Report", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_Report"):
                opp_val = getattr(value, "accounting_Report", None)
                setattr(value, "accounting_Report", self)

    @property
    def accounting_Accounting10(self):
        return self.__accounting_Accounting10

    @accounting_Accounting10.setter
    def accounting_Accounting10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Accounting__accounting_Accounting10", None)
        self.__accounting_Accounting10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "accounting_JournalGroup"):
                    opp_val = getattr(item, "accounting_JournalGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "accounting_JournalGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "accounting_JournalGroup"):
                    opp_val = getattr(item, "accounting_JournalGroup", None)
                    
                    setattr(item, "accounting_JournalGroup", self)
                    

    @property
    def accounting_Accounting(self):
        return self.__accounting_Accounting

    @accounting_Accounting.setter
    def accounting_Accounting(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Accounting__accounting_Accounting", None)
        self.__accounting_Accounting = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "accounting_AccountGroup2"):
                    opp_val = getattr(item, "accounting_AccountGroup2", None)
                    
                    if opp_val == self:
                        setattr(item, "accounting_AccountGroup2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "accounting_AccountGroup2"):
                    opp_val = getattr(item, "accounting_AccountGroup2", None)
                    
                    setattr(item, "accounting_AccountGroup2", self)
                    

    @property
    def accounting_Accounting4(self):
        return self.__accounting_Accounting4

    @accounting_Accounting4.setter
    def accounting_Accounting4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Accounting__accounting_Accounting4", None)
        self.__accounting_Accounting4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "accounting_Vat"):
                    opp_val = getattr(item, "accounting_Vat", None)
                    
                    if opp_val == self:
                        setattr(item, "accounting_Vat", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "accounting_Vat"):
                    opp_val = getattr(item, "accounting_Vat", None)
                    
                    setattr(item, "accounting_Vat", self)
                    

class accounting_AccountGroup:

    def __init__(self, name: str, accounting_AccountGroup: set["accounting_Account"] = None, accounting_AccountGroup2: "accounting_Accounting" = None):
        self.name = name
        self.accounting_AccountGroup = accounting_AccountGroup if accounting_AccountGroup is not None else set()
        self.accounting_AccountGroup2 = accounting_AccountGroup2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def accounting_AccountGroup(self):
        return self.__accounting_AccountGroup

    @accounting_AccountGroup.setter
    def accounting_AccountGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_AccountGroup__accounting_AccountGroup", None)
        self.__accounting_AccountGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "accounting_Account"):
                    opp_val = getattr(item, "accounting_Account", None)
                    
                    if opp_val == self:
                        setattr(item, "accounting_Account", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "accounting_Account"):
                    opp_val = getattr(item, "accounting_Account", None)
                    
                    setattr(item, "accounting_Account", self)
                    

    @property
    def accounting_AccountGroup2(self):
        return self.__accounting_AccountGroup2

    @accounting_AccountGroup2.setter
    def accounting_AccountGroup2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_AccountGroup__accounting_AccountGroup2", None)
        self.__accounting_AccountGroup2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_Accounting"):
                opp_val = getattr(old_value, "accounting_Accounting", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_Accounting"):
                opp_val = getattr(value, "accounting_Accounting", None)
                if opp_val is None:
                    setattr(value, "accounting_Accounting", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class accounting_Account(ABC):

    def __init__(self, name: str, accounting_Account: "accounting_AccountGroup" = None, accounting_Account19: "accounting_JournalStatement" = None, accounting_Account22: "accounting_JournalStatement" = None):
        self.name = name
        self.accounting_Account = accounting_Account
        self.accounting_Account19 = accounting_Account19
        self.accounting_Account22 = accounting_Account22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def accounting_Account(self):
        return self.__accounting_Account

    @accounting_Account.setter
    def accounting_Account(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Account__accounting_Account", None)
        self.__accounting_Account = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_AccountGroup"):
                opp_val = getattr(old_value, "accounting_AccountGroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_AccountGroup"):
                opp_val = getattr(value, "accounting_AccountGroup", None)
                if opp_val is None:
                    setattr(value, "accounting_AccountGroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def accounting_Account19(self):
        return self.__accounting_Account19

    @accounting_Account19.setter
    def accounting_Account19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Account__accounting_Account19", None)
        self.__accounting_Account19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_JournalStatement18"):
                opp_val = getattr(old_value, "accounting_JournalStatement18", None)
                if opp_val == self:
                    setattr(old_value, "accounting_JournalStatement18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_JournalStatement18"):
                opp_val = getattr(value, "accounting_JournalStatement18", None)
                setattr(value, "accounting_JournalStatement18", self)

    @property
    def accounting_Account22(self):
        return self.__accounting_Account22

    @accounting_Account22.setter
    def accounting_Account22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accounting_Account__accounting_Account22", None)
        self.__accounting_Account22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accounting_JournalStatement21"):
                opp_val = getattr(old_value, "accounting_JournalStatement21", None)
                if opp_val == self:
                    setattr(old_value, "accounting_JournalStatement21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accounting_JournalStatement21"):
                opp_val = getattr(value, "accounting_JournalStatement21", None)
                setattr(value, "accounting_JournalStatement21", self)
