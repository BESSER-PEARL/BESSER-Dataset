from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Gender(Enum):
    male = "male"
    female = "female"
class RandLColor(Enum):
    silver = "silver"
    gold = "gold"


############################################
# Definition of Classes
############################################

class RoyalAndLoyal_Container_RandL:

    pass
class RoyalAndLoyal_TransactionReportLine:

    def __init__(self, partnerName: str, serviceDesc: str, points: int, amount: float, TransactionReportLine: "RoyalAndLoyal_TransactionReport" = None, RoyalAndLoyal_TransactionReportLine: "RoyalAndLoyal_Container_RandL" = None, RoyalAndLoyal_TransactionReportLine102: "RoyalAndLoyal_Date" = None, RoyalAndLoyal_TransactionReportLine105: "RoyalAndLoyal_Transaction" = None, lines: "RoyalAndLoyal_TransactionReport" = None):
        self.partnerName = partnerName
        self.serviceDesc = serviceDesc
        self.points = points
        self.amount = amount
        self.TransactionReportLine = TransactionReportLine
        self.RoyalAndLoyal_TransactionReportLine = RoyalAndLoyal_TransactionReportLine
        self.RoyalAndLoyal_TransactionReportLine102 = RoyalAndLoyal_TransactionReportLine102
        self.RoyalAndLoyal_TransactionReportLine105 = RoyalAndLoyal_TransactionReportLine105
        self.lines = lines
        
    @property
    def amount(self) -> float:
        return self.__amount

    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount

    @property
    def partnerName(self) -> str:
        return self.__partnerName

    @partnerName.setter
    def partnerName(self, partnerName: str):
        self.__partnerName = partnerName

    @property
    def serviceDesc(self) -> str:
        return self.__serviceDesc

    @serviceDesc.setter
    def serviceDesc(self, serviceDesc: str):
        self.__serviceDesc = serviceDesc

    @property
    def points(self) -> int:
        return self.__points

    @points.setter
    def points(self, points: int):
        self.__points = points

    @property
    def lines(self):
        return self.__lines

    @lines.setter
    def lines(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_TransactionReportLine__lines", None)
        self.__lines = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TransactionReport"):
                opp_val = getattr(old_value, "TransactionReport", None)
                if opp_val == self:
                    setattr(old_value, "TransactionReport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TransactionReport"):
                opp_val = getattr(value, "TransactionReport", None)
                setattr(value, "TransactionReport", self)

    @property
    def RoyalAndLoyal_TransactionReportLine(self):
        return self.__RoyalAndLoyal_TransactionReportLine

    @RoyalAndLoyal_TransactionReportLine.setter
    def RoyalAndLoyal_TransactionReportLine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_TransactionReportLine__RoyalAndLoyal_TransactionReportLine", None)
        self.__RoyalAndLoyal_TransactionReportLine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Container_RandL85"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Container_RandL85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Container_RandL85"):
                opp_val = getattr(value, "RoyalAndLoyal_Container_RandL85", None)
                if opp_val is None:
                    setattr(value, "RoyalAndLoyal_Container_RandL85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RoyalAndLoyal_TransactionReportLine102(self):
        return self.__RoyalAndLoyal_TransactionReportLine102

    @RoyalAndLoyal_TransactionReportLine102.setter
    def RoyalAndLoyal_TransactionReportLine102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_TransactionReportLine__RoyalAndLoyal_TransactionReportLine102", None)
        self.__RoyalAndLoyal_TransactionReportLine102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Date103"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Date103", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_Date103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Date103"):
                opp_val = getattr(value, "RoyalAndLoyal_Date103", None)
                setattr(value, "RoyalAndLoyal_Date103", self)

    @property
    def TransactionReportLine(self):
        return self.__TransactionReportLine

    @TransactionReportLine.setter
    def TransactionReportLine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_TransactionReportLine__TransactionReportLine", None)
        self.__TransactionReportLine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "report"):
                opp_val = getattr(old_value, "report", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "report"):
                opp_val = getattr(value, "report", None)
                if opp_val is None:
                    setattr(value, "report", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RoyalAndLoyal_TransactionReportLine105(self):
        return self.__RoyalAndLoyal_TransactionReportLine105

    @RoyalAndLoyal_TransactionReportLine105.setter
    def RoyalAndLoyal_TransactionReportLine105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_TransactionReportLine__RoyalAndLoyal_TransactionReportLine105", None)
        self.__RoyalAndLoyal_TransactionReportLine105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Transaction106"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Transaction106", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_Transaction106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Transaction106"):
                opp_val = getattr(value, "RoyalAndLoyal_Transaction106", None)
                setattr(value, "RoyalAndLoyal_Transaction106", self)

class RoyalAndLoyal_TransactionReport:

    def __init__(self, balance: int, totalEarned: int, totalBurned: int, number: int, name: str, RoyalAndLoyal_TransactionReport: "RoyalAndLoyal_Date" = None, RoyalAndLoyal_TransactionReport22: "RoyalAndLoyal_Date" = None, report: set["RoyalAndLoyal_TransactionReportLine"] = None, RoyalAndLoyal_TransactionReport26: "RoyalAndLoyal_CustomerCard" = None, RoyalAndLoyal_TransactionReport79: "RoyalAndLoyal_Container_RandL" = None, TransactionReport: "RoyalAndLoyal_TransactionReportLine" = None):
        self.balance = balance
        self.totalEarned = totalEarned
        self.totalBurned = totalBurned
        self.number = number
        self.name = name
        self.RoyalAndLoyal_TransactionReport = RoyalAndLoyal_TransactionReport
        self.RoyalAndLoyal_TransactionReport22 = RoyalAndLoyal_TransactionReport22
        self.report = report if report is not None else set()
        self.RoyalAndLoyal_TransactionReport26 = RoyalAndLoyal_TransactionReport26
        self.RoyalAndLoyal_TransactionReport79 = RoyalAndLoyal_TransactionReport79
        self.TransactionReport = TransactionReport
        
    @property
    def totalEarned(self) -> int:
        return self.__totalEarned

    @totalEarned.setter
    def totalEarned(self, totalEarned: int):
        self.__totalEarned = totalEarned

    @property
    def balance(self) -> int:
        return self.__balance

    @balance.setter
    def balance(self, balance: int):
        self.__balance = balance

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def totalBurned(self) -> int:
        return self.__totalBurned

    @totalBurned.setter
    def totalBurned(self, totalBurned: int):
        self.__totalBurned = totalBurned

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def TransactionReport(self):
        return self.__TransactionReport

    @TransactionReport.setter
    def TransactionReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_TransactionReport__TransactionReport", None)
        self.__TransactionReport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lines"):
                opp_val = getattr(old_value, "lines", None)
                if opp_val == self:
                    setattr(old_value, "lines", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lines"):
                opp_val = getattr(value, "lines", None)
                setattr(value, "lines", self)

    @property
    def RoyalAndLoyal_TransactionReport26(self):
        return self.__RoyalAndLoyal_TransactionReport26

    @RoyalAndLoyal_TransactionReport26.setter
    def RoyalAndLoyal_TransactionReport26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_TransactionReport__RoyalAndLoyal_TransactionReport26", None)
        self.__RoyalAndLoyal_TransactionReport26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_CustomerCard"):
                opp_val = getattr(old_value, "RoyalAndLoyal_CustomerCard", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_CustomerCard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_CustomerCard"):
                opp_val = getattr(value, "RoyalAndLoyal_CustomerCard", None)
                setattr(value, "RoyalAndLoyal_CustomerCard", self)

    @property
    def RoyalAndLoyal_TransactionReport22(self):
        return self.__RoyalAndLoyal_TransactionReport22

    @RoyalAndLoyal_TransactionReport22.setter
    def RoyalAndLoyal_TransactionReport22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_TransactionReport__RoyalAndLoyal_TransactionReport22", None)
        self.__RoyalAndLoyal_TransactionReport22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Date23"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Date23", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_Date23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Date23"):
                opp_val = getattr(value, "RoyalAndLoyal_Date23", None)
                setattr(value, "RoyalAndLoyal_Date23", self)

    @property
    def RoyalAndLoyal_TransactionReport(self):
        return self.__RoyalAndLoyal_TransactionReport

    @RoyalAndLoyal_TransactionReport.setter
    def RoyalAndLoyal_TransactionReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_TransactionReport__RoyalAndLoyal_TransactionReport", None)
        self.__RoyalAndLoyal_TransactionReport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Date20"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Date20", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_Date20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Date20"):
                opp_val = getattr(value, "RoyalAndLoyal_Date20", None)
                setattr(value, "RoyalAndLoyal_Date20", self)

    @property
    def report(self):
        return self.__report

    @report.setter
    def report(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_TransactionReport__report", None)
        self.__report = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TransactionReportLine"):
                    opp_val = getattr(item, "TransactionReportLine", None)
                    
                    if opp_val == self:
                        setattr(item, "TransactionReportLine", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TransactionReportLine"):
                    opp_val = getattr(item, "TransactionReportLine", None)
                    
                    setattr(item, "TransactionReportLine", self)
                    

    @property
    def RoyalAndLoyal_TransactionReport79(self):
        return self.__RoyalAndLoyal_TransactionReport79

    @RoyalAndLoyal_TransactionReport79.setter
    def RoyalAndLoyal_TransactionReport79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_TransactionReport__RoyalAndLoyal_TransactionReport79", None)
        self.__RoyalAndLoyal_TransactionReport79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Container_RandL78"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Container_RandL78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Container_RandL78"):
                opp_val = getattr(value, "RoyalAndLoyal_Container_RandL78", None)
                if opp_val is None:
                    setattr(value, "RoyalAndLoyal_Container_RandL78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class RoyalAndLoyal_Customer:

    def __init__(self, gender: str, isMale: bool, name: str, title: str, age: int, Customer: "RoyalAndLoyal_CustomerCard" = None, RoyalAndLoyal_Customer53: "RoyalAndLoyal_Container_RandL" = None, RoyalAndLoyal_Customer: "RoyalAndLoyal_Membership" = None, RoyalAndLoyal_Customer92: "RoyalAndLoyal_Date" = None, participants: set["RoyalAndLoyal_LoyaltyProgram"] = None, owner: set["RoyalAndLoyal_CustomerCard"] = None, Customer114: "RoyalAndLoyal_LoyaltyProgram" = None, RoyalAndLoyal_Customer99: set["RoyalAndLoyal_Membership"] = None):
        self.gender = gender
        self.isMale = isMale
        self.name = name
        self.title = title
        self.age = age
        self.Customer = Customer
        self.RoyalAndLoyal_Customer53 = RoyalAndLoyal_Customer53
        self.RoyalAndLoyal_Customer = RoyalAndLoyal_Customer
        self.RoyalAndLoyal_Customer92 = RoyalAndLoyal_Customer92
        self.participants = participants if participants is not None else set()
        self.owner = owner if owner is not None else set()
        self.Customer114 = Customer114
        self.RoyalAndLoyal_Customer99 = RoyalAndLoyal_Customer99 if RoyalAndLoyal_Customer99 is not None else set()
        
    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def isMale(self) -> bool:
        return self.__isMale

    @isMale.setter
    def isMale(self, isMale: bool):
        self.__isMale = isMale

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
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def participants(self):
        return self.__participants

    @participants.setter
    def participants(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Customer__participants", None)
        self.__participants = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LoyaltyProgram95"):
                    opp_val = getattr(item, "LoyaltyProgram95", None)
                    
                    if opp_val == self:
                        setattr(item, "LoyaltyProgram95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LoyaltyProgram95"):
                    opp_val = getattr(item, "LoyaltyProgram95", None)
                    
                    setattr(item, "LoyaltyProgram95", self)
                    

    @property
    def Customer114(self):
        return self.__Customer114

    @Customer114.setter
    def Customer114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Customer__Customer114", None)
        self.__Customer114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programs113"):
                opp_val = getattr(old_value, "programs113", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programs113"):
                opp_val = getattr(value, "programs113", None)
                if opp_val is None:
                    setattr(value, "programs113", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Customer(self):
        return self.__Customer

    @Customer.setter
    def Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Customer__Customer", None)
        self.__Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cards"):
                opp_val = getattr(old_value, "cards", None)
                if opp_val == self:
                    setattr(old_value, "cards", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cards"):
                opp_val = getattr(value, "cards", None)
                setattr(value, "cards", self)

    @property
    def RoyalAndLoyal_Customer92(self):
        return self.__RoyalAndLoyal_Customer92

    @RoyalAndLoyal_Customer92.setter
    def RoyalAndLoyal_Customer92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Customer__RoyalAndLoyal_Customer92", None)
        self.__RoyalAndLoyal_Customer92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Date93"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Date93", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_Date93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Date93"):
                opp_val = getattr(value, "RoyalAndLoyal_Date93", None)
                setattr(value, "RoyalAndLoyal_Date93", self)

    @property
    def RoyalAndLoyal_Customer53(self):
        return self.__RoyalAndLoyal_Customer53

    @RoyalAndLoyal_Customer53.setter
    def RoyalAndLoyal_Customer53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Customer__RoyalAndLoyal_Customer53", None)
        self.__RoyalAndLoyal_Customer53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Container_RandL"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Container_RandL", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Container_RandL"):
                opp_val = getattr(value, "RoyalAndLoyal_Container_RandL", None)
                if opp_val is None:
                    setattr(value, "RoyalAndLoyal_Container_RandL", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Customer__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CustomerCard97"):
                    opp_val = getattr(item, "CustomerCard97", None)
                    
                    if opp_val == self:
                        setattr(item, "CustomerCard97", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CustomerCard97"):
                    opp_val = getattr(item, "CustomerCard97", None)
                    
                    setattr(item, "CustomerCard97", self)
                    

    @property
    def RoyalAndLoyal_Customer99(self):
        return self.__RoyalAndLoyal_Customer99

    @RoyalAndLoyal_Customer99.setter
    def RoyalAndLoyal_Customer99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Customer__RoyalAndLoyal_Customer99", None)
        self.__RoyalAndLoyal_Customer99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RoyalAndLoyal_Membership100"):
                    opp_val = getattr(item, "RoyalAndLoyal_Membership100", None)
                    
                    if opp_val == self:
                        setattr(item, "RoyalAndLoyal_Membership100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RoyalAndLoyal_Membership100"):
                    opp_val = getattr(item, "RoyalAndLoyal_Membership100", None)
                    
                    setattr(item, "RoyalAndLoyal_Membership100", self)
                    

    @property
    def RoyalAndLoyal_Customer(self):
        return self.__RoyalAndLoyal_Customer

    @RoyalAndLoyal_Customer.setter
    def RoyalAndLoyal_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Customer__RoyalAndLoyal_Customer", None)
        self.__RoyalAndLoyal_Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Membership51"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Membership51", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_Membership51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Membership51"):
                opp_val = getattr(value, "RoyalAndLoyal_Membership51", None)
                setattr(value, "RoyalAndLoyal_Membership51", self)

    def age(self) -> int:
        # TODO: Implement age method
        pass

    def birthdayHappens(self):
        # TODO: Implement birthdayHappens method
        pass

    def updateName(self, name: str):
        # TODO: Implement updateName method
        pass

class RoyalAndLoyal_CustomerCard:

    def __init__(self, valid: bool, color: str, printedName: str, CustomerCard: "RoyalAndLoyal_Transaction" = None, RoyalAndLoyal_CustomerCard28: "RoyalAndLoyal_Date" = None, RoyalAndLoyal_CustomerCard31: "RoyalAndLoyal_Date" = None, RoyalAndLoyal_CustomerCard34: "RoyalAndLoyal_ServiceLevel" = None, cards: "RoyalAndLoyal_Customer" = None, RoyalAndLoyal_CustomerCard: "RoyalAndLoyal_TransactionReport" = None, RoyalAndLoyal_CustomerCard59: "RoyalAndLoyal_Container_RandL" = None, card: "RoyalAndLoyal_Membership" = None, card39: set["RoyalAndLoyal_Transaction"] = None, CustomerCard45: "RoyalAndLoyal_Membership" = None, CustomerCard97: "RoyalAndLoyal_Customer" = None):
        self.valid = valid
        self.color = color
        self.printedName = printedName
        self.CustomerCard = CustomerCard
        self.RoyalAndLoyal_CustomerCard28 = RoyalAndLoyal_CustomerCard28
        self.RoyalAndLoyal_CustomerCard31 = RoyalAndLoyal_CustomerCard31
        self.RoyalAndLoyal_CustomerCard34 = RoyalAndLoyal_CustomerCard34
        self.cards = cards
        self.RoyalAndLoyal_CustomerCard = RoyalAndLoyal_CustomerCard
        self.RoyalAndLoyal_CustomerCard59 = RoyalAndLoyal_CustomerCard59
        self.card = card
        self.card39 = card39 if card39 is not None else set()
        self.CustomerCard45 = CustomerCard45
        self.CustomerCard97 = CustomerCard97
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def valid(self) -> bool:
        return self.__valid

    @valid.setter
    def valid(self, valid: bool):
        self.__valid = valid

    @property
    def printedName(self) -> str:
        return self.__printedName

    @printedName.setter
    def printedName(self, printedName: str):
        self.__printedName = printedName

    @property
    def card(self):
        return self.__card

    @card.setter
    def card(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_CustomerCard__card", None)
        self.__card = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Membership37"):
                opp_val = getattr(old_value, "Membership37", None)
                if opp_val == self:
                    setattr(old_value, "Membership37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Membership37"):
                opp_val = getattr(value, "Membership37", None)
                setattr(value, "Membership37", self)

    @property
    def CustomerCard97(self):
        return self.__CustomerCard97

    @CustomerCard97.setter
    def CustomerCard97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_CustomerCard__CustomerCard97", None)
        self.__CustomerCard97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner"):
                opp_val = getattr(old_value, "owner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner"):
                opp_val = getattr(value, "owner", None)
                if opp_val is None:
                    setattr(value, "owner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_CustomerCard__cards", None)
        self.__cards = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer"):
                opp_val = getattr(old_value, "Customer", None)
                if opp_val == self:
                    setattr(old_value, "Customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer"):
                opp_val = getattr(value, "Customer", None)
                setattr(value, "Customer", self)

    @property
    def CustomerCard(self):
        return self.__CustomerCard

    @CustomerCard.setter
    def CustomerCard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_CustomerCard__CustomerCard", None)
        self.__CustomerCard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transactions9"):
                opp_val = getattr(old_value, "transactions9", None)
                if opp_val == self:
                    setattr(old_value, "transactions9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transactions9"):
                opp_val = getattr(value, "transactions9", None)
                setattr(value, "transactions9", self)

    @property
    def RoyalAndLoyal_CustomerCard(self):
        return self.__RoyalAndLoyal_CustomerCard

    @RoyalAndLoyal_CustomerCard.setter
    def RoyalAndLoyal_CustomerCard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_CustomerCard__RoyalAndLoyal_CustomerCard", None)
        self.__RoyalAndLoyal_CustomerCard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_TransactionReport26"):
                opp_val = getattr(old_value, "RoyalAndLoyal_TransactionReport26", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_TransactionReport26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_TransactionReport26"):
                opp_val = getattr(value, "RoyalAndLoyal_TransactionReport26", None)
                setattr(value, "RoyalAndLoyal_TransactionReport26", self)

    @property
    def RoyalAndLoyal_CustomerCard59(self):
        return self.__RoyalAndLoyal_CustomerCard59

    @RoyalAndLoyal_CustomerCard59.setter
    def RoyalAndLoyal_CustomerCard59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_CustomerCard__RoyalAndLoyal_CustomerCard59", None)
        self.__RoyalAndLoyal_CustomerCard59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Container_RandL58"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Container_RandL58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Container_RandL58"):
                opp_val = getattr(value, "RoyalAndLoyal_Container_RandL58", None)
                if opp_val is None:
                    setattr(value, "RoyalAndLoyal_Container_RandL58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RoyalAndLoyal_CustomerCard31(self):
        return self.__RoyalAndLoyal_CustomerCard31

    @RoyalAndLoyal_CustomerCard31.setter
    def RoyalAndLoyal_CustomerCard31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_CustomerCard__RoyalAndLoyal_CustomerCard31", None)
        self.__RoyalAndLoyal_CustomerCard31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Date32"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Date32", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_Date32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Date32"):
                opp_val = getattr(value, "RoyalAndLoyal_Date32", None)
                setattr(value, "RoyalAndLoyal_Date32", self)

    @property
    def RoyalAndLoyal_CustomerCard28(self):
        return self.__RoyalAndLoyal_CustomerCard28

    @RoyalAndLoyal_CustomerCard28.setter
    def RoyalAndLoyal_CustomerCard28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_CustomerCard__RoyalAndLoyal_CustomerCard28", None)
        self.__RoyalAndLoyal_CustomerCard28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Date29"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Date29", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_Date29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Date29"):
                opp_val = getattr(value, "RoyalAndLoyal_Date29", None)
                setattr(value, "RoyalAndLoyal_Date29", self)

    @property
    def CustomerCard45(self):
        return self.__CustomerCard45

    @CustomerCard45.setter
    def CustomerCard45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_CustomerCard__CustomerCard45", None)
        self.__CustomerCard45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Membership44"):
                opp_val = getattr(old_value, "Membership44", None)
                if opp_val == self:
                    setattr(old_value, "Membership44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Membership44"):
                opp_val = getattr(value, "Membership44", None)
                setattr(value, "Membership44", self)

    @property
    def RoyalAndLoyal_CustomerCard34(self):
        return self.__RoyalAndLoyal_CustomerCard34

    @RoyalAndLoyal_CustomerCard34.setter
    def RoyalAndLoyal_CustomerCard34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_CustomerCard__RoyalAndLoyal_CustomerCard34", None)
        self.__RoyalAndLoyal_CustomerCard34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_ServiceLevel"):
                opp_val = getattr(old_value, "RoyalAndLoyal_ServiceLevel", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_ServiceLevel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_ServiceLevel"):
                opp_val = getattr(value, "RoyalAndLoyal_ServiceLevel", None)
                setattr(value, "RoyalAndLoyal_ServiceLevel", self)

    @property
    def card39(self):
        return self.__card39

    @card39.setter
    def card39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_CustomerCard__card39", None)
        self.__card39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transaction40"):
                    opp_val = getattr(item, "Transaction40", None)
                    
                    if opp_val == self:
                        setattr(item, "Transaction40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transaction40"):
                    opp_val = getattr(item, "Transaction40", None)
                    
                    setattr(item, "Transaction40", self)
                    

    def getTransactions(self, until: str, from: str) -> Transaction:
        # TODO: Implement getTransactions method
        pass

class RoyalAndLoyal_LoyaltyAccount:

    def __init__(self, points: int, totalPointsEarned: int, number: int, RoyalAndLoyal_LoyaltyAccount: set["RoyalAndLoyal_Service"] = None, account: "RoyalAndLoyal_Membership" = None, account14: set["RoyalAndLoyal_Transaction"] = None, LoyaltyAccount: "RoyalAndLoyal_Transaction" = None, LoyaltyAccount48: "RoyalAndLoyal_Membership" = None, RoyalAndLoyal_LoyaltyAccount73: "RoyalAndLoyal_Container_RandL" = None):
        self.points = points
        self.totalPointsEarned = totalPointsEarned
        self.number = number
        self.RoyalAndLoyal_LoyaltyAccount = RoyalAndLoyal_LoyaltyAccount if RoyalAndLoyal_LoyaltyAccount is not None else set()
        self.account = account
        self.account14 = account14 if account14 is not None else set()
        self.LoyaltyAccount = LoyaltyAccount
        self.LoyaltyAccount48 = LoyaltyAccount48
        self.RoyalAndLoyal_LoyaltyAccount73 = RoyalAndLoyal_LoyaltyAccount73
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def totalPointsEarned(self) -> int:
        return self.__totalPointsEarned

    @totalPointsEarned.setter
    def totalPointsEarned(self, totalPointsEarned: int):
        self.__totalPointsEarned = totalPointsEarned

    @property
    def points(self) -> int:
        return self.__points

    @points.setter
    def points(self, points: int):
        self.__points = points

    @property
    def RoyalAndLoyal_LoyaltyAccount73(self):
        return self.__RoyalAndLoyal_LoyaltyAccount73

    @RoyalAndLoyal_LoyaltyAccount73.setter
    def RoyalAndLoyal_LoyaltyAccount73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_LoyaltyAccount__RoyalAndLoyal_LoyaltyAccount73", None)
        self.__RoyalAndLoyal_LoyaltyAccount73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Container_RandL72"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Container_RandL72", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Container_RandL72"):
                opp_val = getattr(value, "RoyalAndLoyal_Container_RandL72", None)
                if opp_val is None:
                    setattr(value, "RoyalAndLoyal_Container_RandL72", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_LoyaltyAccount__account", None)
        self.__account = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Membership12"):
                opp_val = getattr(old_value, "Membership12", None)
                if opp_val == self:
                    setattr(old_value, "Membership12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Membership12"):
                opp_val = getattr(value, "Membership12", None)
                setattr(value, "Membership12", self)

    @property
    def LoyaltyAccount(self):
        return self.__LoyaltyAccount

    @LoyaltyAccount.setter
    def LoyaltyAccount(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_LoyaltyAccount__LoyaltyAccount", None)
        self.__LoyaltyAccount = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transactions"):
                opp_val = getattr(old_value, "transactions", None)
                if opp_val == self:
                    setattr(old_value, "transactions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transactions"):
                opp_val = getattr(value, "transactions", None)
                setattr(value, "transactions", self)

    @property
    def LoyaltyAccount48(self):
        return self.__LoyaltyAccount48

    @LoyaltyAccount48.setter
    def LoyaltyAccount48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_LoyaltyAccount__LoyaltyAccount48", None)
        self.__LoyaltyAccount48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Membership47"):
                opp_val = getattr(old_value, "Membership47", None)
                if opp_val == self:
                    setattr(old_value, "Membership47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Membership47"):
                opp_val = getattr(value, "Membership47", None)
                setattr(value, "Membership47", self)

    @property
    def account14(self):
        return self.__account14

    @account14.setter
    def account14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_LoyaltyAccount__account14", None)
        self.__account14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transaction"):
                    opp_val = getattr(item, "Transaction", None)
                    
                    if opp_val == self:
                        setattr(item, "Transaction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transaction"):
                    opp_val = getattr(item, "Transaction", None)
                    
                    setattr(item, "Transaction", self)
                    

    @property
    def RoyalAndLoyal_LoyaltyAccount(self):
        return self.__RoyalAndLoyal_LoyaltyAccount

    @RoyalAndLoyal_LoyaltyAccount.setter
    def RoyalAndLoyal_LoyaltyAccount(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_LoyaltyAccount__RoyalAndLoyal_LoyaltyAccount", None)
        self.__RoyalAndLoyal_LoyaltyAccount = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RoyalAndLoyal_Service"):
                    opp_val = getattr(item, "RoyalAndLoyal_Service", None)
                    
                    if opp_val == self:
                        setattr(item, "RoyalAndLoyal_Service", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RoyalAndLoyal_Service"):
                    opp_val = getattr(item, "RoyalAndLoyal_Service", None)
                    
                    setattr(item, "RoyalAndLoyal_Service", self)
                    

    def earn(self, i: int):
        # TODO: Implement earn method
        pass

    def getCustomerName(self) -> str:
        # TODO: Implement getCustomerName method
        pass

    def burn(self, i: int):
        # TODO: Implement burn method
        pass

    def isEmpty(self) -> bool:
        # TODO: Implement isEmpty method
        pass

class RoyalAndLoyal_Date:

    def __init__(self, year: int, month: int, day: int, RoyalAndLoyal_Date: "RoyalAndLoyal_Transaction" = None, RoyalAndLoyal_Date29: "RoyalAndLoyal_CustomerCard" = None, RoyalAndLoyal_Date32: "RoyalAndLoyal_CustomerCard" = None, RoyalAndLoyal_Date20: "RoyalAndLoyal_TransactionReport" = None, RoyalAndLoyal_Date23: "RoyalAndLoyal_TransactionReport" = None, RoyalAndLoyal_Date56: "RoyalAndLoyal_Container_RandL" = None, RoyalAndLoyal_Date93: "RoyalAndLoyal_Customer" = None, RoyalAndLoyal_Date103: "RoyalAndLoyal_TransactionReportLine" = None):
        self.year = year
        self.month = month
        self.day = day
        self.RoyalAndLoyal_Date = RoyalAndLoyal_Date
        self.RoyalAndLoyal_Date29 = RoyalAndLoyal_Date29
        self.RoyalAndLoyal_Date32 = RoyalAndLoyal_Date32
        self.RoyalAndLoyal_Date20 = RoyalAndLoyal_Date20
        self.RoyalAndLoyal_Date23 = RoyalAndLoyal_Date23
        self.RoyalAndLoyal_Date56 = RoyalAndLoyal_Date56
        self.RoyalAndLoyal_Date93 = RoyalAndLoyal_Date93
        self.RoyalAndLoyal_Date103 = RoyalAndLoyal_Date103
        
    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def day(self) -> int:
        return self.__day

    @day.setter
    def day(self, day: int):
        self.__day = day

    @property
    def month(self) -> int:
        return self.__month

    @month.setter
    def month(self, month: int):
        self.__month = month

    @property
    def RoyalAndLoyal_Date32(self):
        return self.__RoyalAndLoyal_Date32

    @RoyalAndLoyal_Date32.setter
    def RoyalAndLoyal_Date32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Date__RoyalAndLoyal_Date32", None)
        self.__RoyalAndLoyal_Date32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_CustomerCard31"):
                opp_val = getattr(old_value, "RoyalAndLoyal_CustomerCard31", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_CustomerCard31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_CustomerCard31"):
                opp_val = getattr(value, "RoyalAndLoyal_CustomerCard31", None)
                setattr(value, "RoyalAndLoyal_CustomerCard31", self)

    @property
    def RoyalAndLoyal_Date(self):
        return self.__RoyalAndLoyal_Date

    @RoyalAndLoyal_Date.setter
    def RoyalAndLoyal_Date(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Date__RoyalAndLoyal_Date", None)
        self.__RoyalAndLoyal_Date = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Transaction"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Transaction", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_Transaction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Transaction"):
                opp_val = getattr(value, "RoyalAndLoyal_Transaction", None)
                setattr(value, "RoyalAndLoyal_Transaction", self)

    @property
    def RoyalAndLoyal_Date93(self):
        return self.__RoyalAndLoyal_Date93

    @RoyalAndLoyal_Date93.setter
    def RoyalAndLoyal_Date93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Date__RoyalAndLoyal_Date93", None)
        self.__RoyalAndLoyal_Date93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Customer92"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Customer92", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_Customer92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Customer92"):
                opp_val = getattr(value, "RoyalAndLoyal_Customer92", None)
                setattr(value, "RoyalAndLoyal_Customer92", self)

    @property
    def RoyalAndLoyal_Date29(self):
        return self.__RoyalAndLoyal_Date29

    @RoyalAndLoyal_Date29.setter
    def RoyalAndLoyal_Date29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Date__RoyalAndLoyal_Date29", None)
        self.__RoyalAndLoyal_Date29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_CustomerCard28"):
                opp_val = getattr(old_value, "RoyalAndLoyal_CustomerCard28", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_CustomerCard28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_CustomerCard28"):
                opp_val = getattr(value, "RoyalAndLoyal_CustomerCard28", None)
                setattr(value, "RoyalAndLoyal_CustomerCard28", self)

    @property
    def RoyalAndLoyal_Date20(self):
        return self.__RoyalAndLoyal_Date20

    @RoyalAndLoyal_Date20.setter
    def RoyalAndLoyal_Date20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Date__RoyalAndLoyal_Date20", None)
        self.__RoyalAndLoyal_Date20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_TransactionReport"):
                opp_val = getattr(old_value, "RoyalAndLoyal_TransactionReport", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_TransactionReport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_TransactionReport"):
                opp_val = getattr(value, "RoyalAndLoyal_TransactionReport", None)
                setattr(value, "RoyalAndLoyal_TransactionReport", self)

    @property
    def RoyalAndLoyal_Date103(self):
        return self.__RoyalAndLoyal_Date103

    @RoyalAndLoyal_Date103.setter
    def RoyalAndLoyal_Date103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Date__RoyalAndLoyal_Date103", None)
        self.__RoyalAndLoyal_Date103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_TransactionReportLine102"):
                opp_val = getattr(old_value, "RoyalAndLoyal_TransactionReportLine102", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_TransactionReportLine102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_TransactionReportLine102"):
                opp_val = getattr(value, "RoyalAndLoyal_TransactionReportLine102", None)
                setattr(value, "RoyalAndLoyal_TransactionReportLine102", self)

    @property
    def RoyalAndLoyal_Date23(self):
        return self.__RoyalAndLoyal_Date23

    @RoyalAndLoyal_Date23.setter
    def RoyalAndLoyal_Date23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Date__RoyalAndLoyal_Date23", None)
        self.__RoyalAndLoyal_Date23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_TransactionReport22"):
                opp_val = getattr(old_value, "RoyalAndLoyal_TransactionReport22", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_TransactionReport22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_TransactionReport22"):
                opp_val = getattr(value, "RoyalAndLoyal_TransactionReport22", None)
                setattr(value, "RoyalAndLoyal_TransactionReport22", self)

    @property
    def RoyalAndLoyal_Date56(self):
        return self.__RoyalAndLoyal_Date56

    @RoyalAndLoyal_Date56.setter
    def RoyalAndLoyal_Date56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Date__RoyalAndLoyal_Date56", None)
        self.__RoyalAndLoyal_Date56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Container_RandL55"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Container_RandL55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Container_RandL55"):
                opp_val = getattr(value, "RoyalAndLoyal_Container_RandL55", None)
                if opp_val is None:
                    setattr(value, "RoyalAndLoyal_Container_RandL55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def fromYMD(self, y: int, m: int, k: int) -> str:
        # TODO: Implement fromYMD method
        pass

    def isEqual(self, t: str) -> bool:
        # TODO: Implement isEqual method
        pass

    def isBefore(self, t: str) -> bool:
        # TODO: Implement isBefore method
        pass

    def isAfter(self, t: str) -> bool:
        # TODO: Implement isAfter method
        pass

class RoyalAndLoyal_Transaction(ABC):

    def __init__(self, amount: float, points: int, Transaction: "RoyalAndLoyal_LoyaltyAccount" = None, RoyalAndLoyal_Transaction: "RoyalAndLoyal_Date" = None, transactions: "RoyalAndLoyal_LoyaltyAccount" = None, transactions6: "RoyalAndLoyal_Service" = None, transactions9: "RoyalAndLoyal_CustomerCard" = None, Transaction40: "RoyalAndLoyal_CustomerCard" = None, Transaction88: "RoyalAndLoyal_Service" = None, RoyalAndLoyal_Transaction106: "RoyalAndLoyal_TransactionReportLine" = None):
        self.amount = amount
        self.points = points
        self.Transaction = Transaction
        self.RoyalAndLoyal_Transaction = RoyalAndLoyal_Transaction
        self.transactions = transactions
        self.transactions6 = transactions6
        self.transactions9 = transactions9
        self.Transaction40 = Transaction40
        self.Transaction88 = Transaction88
        self.RoyalAndLoyal_Transaction106 = RoyalAndLoyal_Transaction106
        
    @property
    def amount(self) -> float:
        return self.__amount

    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount

    @property
    def points(self) -> int:
        return self.__points

    @points.setter
    def points(self, points: int):
        self.__points = points

    @property
    def RoyalAndLoyal_Transaction(self):
        return self.__RoyalAndLoyal_Transaction

    @RoyalAndLoyal_Transaction.setter
    def RoyalAndLoyal_Transaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Transaction__RoyalAndLoyal_Transaction", None)
        self.__RoyalAndLoyal_Transaction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Date"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Date", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_Date", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Date"):
                opp_val = getattr(value, "RoyalAndLoyal_Date", None)
                setattr(value, "RoyalAndLoyal_Date", self)

    @property
    def RoyalAndLoyal_Transaction106(self):
        return self.__RoyalAndLoyal_Transaction106

    @RoyalAndLoyal_Transaction106.setter
    def RoyalAndLoyal_Transaction106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Transaction__RoyalAndLoyal_Transaction106", None)
        self.__RoyalAndLoyal_Transaction106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_TransactionReportLine105"):
                opp_val = getattr(old_value, "RoyalAndLoyal_TransactionReportLine105", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_TransactionReportLine105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_TransactionReportLine105"):
                opp_val = getattr(value, "RoyalAndLoyal_TransactionReportLine105", None)
                setattr(value, "RoyalAndLoyal_TransactionReportLine105", self)

    @property
    def Transaction88(self):
        return self.__Transaction88

    @Transaction88.setter
    def Transaction88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Transaction__Transaction88", None)
        self.__Transaction88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generatedBy"):
                opp_val = getattr(old_value, "generatedBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generatedBy"):
                opp_val = getattr(value, "generatedBy", None)
                if opp_val is None:
                    setattr(value, "generatedBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transactions9(self):
        return self.__transactions9

    @transactions9.setter
    def transactions9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Transaction__transactions9", None)
        self.__transactions9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CustomerCard"):
                opp_val = getattr(old_value, "CustomerCard", None)
                if opp_val == self:
                    setattr(old_value, "CustomerCard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CustomerCard"):
                opp_val = getattr(value, "CustomerCard", None)
                setattr(value, "CustomerCard", self)

    @property
    def transactions(self):
        return self.__transactions

    @transactions.setter
    def transactions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Transaction__transactions", None)
        self.__transactions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LoyaltyAccount"):
                opp_val = getattr(old_value, "LoyaltyAccount", None)
                if opp_val == self:
                    setattr(old_value, "LoyaltyAccount", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LoyaltyAccount"):
                opp_val = getattr(value, "LoyaltyAccount", None)
                setattr(value, "LoyaltyAccount", self)

    @property
    def Transaction40(self):
        return self.__Transaction40

    @Transaction40.setter
    def Transaction40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Transaction__Transaction40", None)
        self.__Transaction40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "card39"):
                opp_val = getattr(old_value, "card39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "card39"):
                opp_val = getattr(value, "card39", None)
                if opp_val is None:
                    setattr(value, "card39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transactions6(self):
        return self.__transactions6

    @transactions6.setter
    def transactions6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Transaction__transactions6", None)
        self.__transactions6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Service7"):
                opp_val = getattr(old_value, "Service7", None)
                if opp_val == self:
                    setattr(old_value, "Service7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Service7"):
                opp_val = getattr(value, "Service7", None)
                setattr(value, "Service7", self)

    @property
    def Transaction(self):
        return self.__Transaction

    @Transaction.setter
    def Transaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Transaction__Transaction", None)
        self.__Transaction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account14"):
                opp_val = getattr(old_value, "account14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account14"):
                opp_val = getattr(value, "account14", None)
                if opp_val is None:
                    setattr(value, "account14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def program(self) -> str:
        # TODO: Implement program method
        pass

class RoyalAndLoyal_Membership:

    pass
class RoyalAndLoyal_Service:

    def __init__(self, serviceNr: int, description: str, pointsEarned: int, condition: bool, pointsBurned: int, RoyalAndLoyal_Service: "RoyalAndLoyal_LoyaltyAccount" = None, Service: "RoyalAndLoyal_ServiceLevel" = None, Service7: "RoyalAndLoyal_Transaction" = None, Service16: "RoyalAndLoyal_ProgramPartner" = None, RoyalAndLoyal_Service65: "RoyalAndLoyal_Container_RandL" = None, availableServices: "RoyalAndLoyal_ServiceLevel" = None, deliveredServices: "RoyalAndLoyal_ProgramPartner" = None, generatedBy: set["RoyalAndLoyal_Transaction"] = None):
        self.serviceNr = serviceNr
        self.description = description
        self.pointsEarned = pointsEarned
        self.condition = condition
        self.pointsBurned = pointsBurned
        self.RoyalAndLoyal_Service = RoyalAndLoyal_Service
        self.Service = Service
        self.Service7 = Service7
        self.Service16 = Service16
        self.RoyalAndLoyal_Service65 = RoyalAndLoyal_Service65
        self.availableServices = availableServices
        self.deliveredServices = deliveredServices
        self.generatedBy = generatedBy if generatedBy is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def pointsBurned(self) -> int:
        return self.__pointsBurned

    @pointsBurned.setter
    def pointsBurned(self, pointsBurned: int):
        self.__pointsBurned = pointsBurned

    @property
    def serviceNr(self) -> int:
        return self.__serviceNr

    @serviceNr.setter
    def serviceNr(self, serviceNr: int):
        self.__serviceNr = serviceNr

    @property
    def pointsEarned(self) -> int:
        return self.__pointsEarned

    @pointsEarned.setter
    def pointsEarned(self, pointsEarned: int):
        self.__pointsEarned = pointsEarned

    @property
    def condition(self) -> bool:
        return self.__condition

    @condition.setter
    def condition(self, condition: bool):
        self.__condition = condition

    @property
    def RoyalAndLoyal_Service65(self):
        return self.__RoyalAndLoyal_Service65

    @RoyalAndLoyal_Service65.setter
    def RoyalAndLoyal_Service65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Service__RoyalAndLoyal_Service65", None)
        self.__RoyalAndLoyal_Service65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Container_RandL64"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Container_RandL64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Container_RandL64"):
                opp_val = getattr(value, "RoyalAndLoyal_Container_RandL64", None)
                if opp_val is None:
                    setattr(value, "RoyalAndLoyal_Container_RandL64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def generatedBy(self):
        return self.__generatedBy

    @generatedBy.setter
    def generatedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Service__generatedBy", None)
        self.__generatedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Transaction88"):
                    opp_val = getattr(item, "Transaction88", None)
                    
                    if opp_val == self:
                        setattr(item, "Transaction88", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Transaction88"):
                    opp_val = getattr(item, "Transaction88", None)
                    
                    setattr(item, "Transaction88", self)
                    

    @property
    def RoyalAndLoyal_Service(self):
        return self.__RoyalAndLoyal_Service

    @RoyalAndLoyal_Service.setter
    def RoyalAndLoyal_Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Service__RoyalAndLoyal_Service", None)
        self.__RoyalAndLoyal_Service = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_LoyaltyAccount"):
                opp_val = getattr(old_value, "RoyalAndLoyal_LoyaltyAccount", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_LoyaltyAccount"):
                opp_val = getattr(value, "RoyalAndLoyal_LoyaltyAccount", None)
                if opp_val is None:
                    setattr(value, "RoyalAndLoyal_LoyaltyAccount", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Service16(self):
        return self.__Service16

    @Service16.setter
    def Service16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Service__Service16", None)
        self.__Service16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partner"):
                opp_val = getattr(old_value, "partner", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partner"):
                opp_val = getattr(value, "partner", None)
                if opp_val is None:
                    setattr(value, "partner", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Service(self):
        return self.__Service

    @Service.setter
    def Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Service__Service", None)
        self.__Service = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "level"):
                opp_val = getattr(old_value, "level", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "level"):
                opp_val = getattr(value, "level", None)
                if opp_val is None:
                    setattr(value, "level", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def availableServices(self):
        return self.__availableServices

    @availableServices.setter
    def availableServices(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Service__availableServices", None)
        self.__availableServices = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ServiceLevel90"):
                opp_val = getattr(old_value, "ServiceLevel90", None)
                if opp_val == self:
                    setattr(old_value, "ServiceLevel90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ServiceLevel90"):
                opp_val = getattr(value, "ServiceLevel90", None)
                setattr(value, "ServiceLevel90", self)

    @property
    def Service7(self):
        return self.__Service7

    @Service7.setter
    def Service7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Service__Service7", None)
        self.__Service7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transactions6"):
                opp_val = getattr(old_value, "transactions6", None)
                if opp_val == self:
                    setattr(old_value, "transactions6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transactions6"):
                opp_val = getattr(value, "transactions6", None)
                setattr(value, "transactions6", self)

    @property
    def deliveredServices(self):
        return self.__deliveredServices

    @deliveredServices.setter
    def deliveredServices(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_Service__deliveredServices", None)
        self.__deliveredServices = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProgramPartner"):
                opp_val = getattr(old_value, "ProgramPartner", None)
                if opp_val == self:
                    setattr(old_value, "ProgramPartner", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProgramPartner"):
                opp_val = getattr(value, "ProgramPartner", None)
                setattr(value, "ProgramPartner", self)

    def upgradePointsEarned(self, amount: int):
        # TODO: Implement upgradePointsEarned method
        pass

    def calcPoints(self) -> int:
        # TODO: Implement calcPoints method
        pass

class RoyalAndLoyal_LoyaltyProgram:

    def __init__(self, name: str, LoyaltyProgram: "RoyalAndLoyal_ServiceLevel" = None, LoyaltyProgram18: "RoyalAndLoyal_ProgramPartner" = None, RoyalAndLoyal_LoyaltyProgram68: "RoyalAndLoyal_Container_RandL" = None, RoyalAndLoyal_LoyaltyProgram: "RoyalAndLoyal_Membership" = None, LoyaltyProgram95: "RoyalAndLoyal_Customer" = None, programs: set["RoyalAndLoyal_ProgramPartner"] = None, program: set["RoyalAndLoyal_ServiceLevel"] = None, programs113: set["RoyalAndLoyal_Customer"] = None, RoyalAndLoyal_LoyaltyProgram116: set["RoyalAndLoyal_Membership"] = None):
        self.name = name
        self.LoyaltyProgram = LoyaltyProgram
        self.LoyaltyProgram18 = LoyaltyProgram18
        self.RoyalAndLoyal_LoyaltyProgram68 = RoyalAndLoyal_LoyaltyProgram68
        self.RoyalAndLoyal_LoyaltyProgram = RoyalAndLoyal_LoyaltyProgram
        self.LoyaltyProgram95 = LoyaltyProgram95
        self.programs = programs if programs is not None else set()
        self.program = program if program is not None else set()
        self.programs113 = programs113 if programs113 is not None else set()
        self.RoyalAndLoyal_LoyaltyProgram116 = RoyalAndLoyal_LoyaltyProgram116 if RoyalAndLoyal_LoyaltyProgram116 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_LoyaltyProgram__program", None)
        self.__program = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ServiceLevel111"):
                    opp_val = getattr(item, "ServiceLevel111", None)
                    
                    if opp_val == self:
                        setattr(item, "ServiceLevel111", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ServiceLevel111"):
                    opp_val = getattr(item, "ServiceLevel111", None)
                    
                    setattr(item, "ServiceLevel111", self)
                    

    @property
    def LoyaltyProgram(self):
        return self.__LoyaltyProgram

    @LoyaltyProgram.setter
    def LoyaltyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_LoyaltyProgram__LoyaltyProgram", None)
        self.__LoyaltyProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "levels"):
                opp_val = getattr(old_value, "levels", None)
                if opp_val == self:
                    setattr(old_value, "levels", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "levels"):
                opp_val = getattr(value, "levels", None)
                setattr(value, "levels", self)

    @property
    def LoyaltyProgram95(self):
        return self.__LoyaltyProgram95

    @LoyaltyProgram95.setter
    def LoyaltyProgram95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_LoyaltyProgram__LoyaltyProgram95", None)
        self.__LoyaltyProgram95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "participants"):
                opp_val = getattr(old_value, "participants", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "participants"):
                opp_val = getattr(value, "participants", None)
                if opp_val is None:
                    setattr(value, "participants", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def LoyaltyProgram18(self):
        return self.__LoyaltyProgram18

    @LoyaltyProgram18.setter
    def LoyaltyProgram18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_LoyaltyProgram__LoyaltyProgram18", None)
        self.__LoyaltyProgram18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "partners"):
                opp_val = getattr(old_value, "partners", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "partners"):
                opp_val = getattr(value, "partners", None)
                if opp_val is None:
                    setattr(value, "partners", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RoyalAndLoyal_LoyaltyProgram116(self):
        return self.__RoyalAndLoyal_LoyaltyProgram116

    @RoyalAndLoyal_LoyaltyProgram116.setter
    def RoyalAndLoyal_LoyaltyProgram116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_LoyaltyProgram__RoyalAndLoyal_LoyaltyProgram116", None)
        self.__RoyalAndLoyal_LoyaltyProgram116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RoyalAndLoyal_Membership117"):
                    opp_val = getattr(item, "RoyalAndLoyal_Membership117", None)
                    
                    if opp_val == self:
                        setattr(item, "RoyalAndLoyal_Membership117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RoyalAndLoyal_Membership117"):
                    opp_val = getattr(item, "RoyalAndLoyal_Membership117", None)
                    
                    setattr(item, "RoyalAndLoyal_Membership117", self)
                    

    @property
    def RoyalAndLoyal_LoyaltyProgram(self):
        return self.__RoyalAndLoyal_LoyaltyProgram

    @RoyalAndLoyal_LoyaltyProgram.setter
    def RoyalAndLoyal_LoyaltyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_LoyaltyProgram__RoyalAndLoyal_LoyaltyProgram", None)
        self.__RoyalAndLoyal_LoyaltyProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Membership"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Membership", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_Membership", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Membership"):
                opp_val = getattr(value, "RoyalAndLoyal_Membership", None)
                setattr(value, "RoyalAndLoyal_Membership", self)

    @property
    def RoyalAndLoyal_LoyaltyProgram68(self):
        return self.__RoyalAndLoyal_LoyaltyProgram68

    @RoyalAndLoyal_LoyaltyProgram68.setter
    def RoyalAndLoyal_LoyaltyProgram68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_LoyaltyProgram__RoyalAndLoyal_LoyaltyProgram68", None)
        self.__RoyalAndLoyal_LoyaltyProgram68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Container_RandL67"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Container_RandL67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Container_RandL67"):
                opp_val = getattr(value, "RoyalAndLoyal_Container_RandL67", None)
                if opp_val is None:
                    setattr(value, "RoyalAndLoyal_Container_RandL67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def programs113(self):
        return self.__programs113

    @programs113.setter
    def programs113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_LoyaltyProgram__programs113", None)
        self.__programs113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Customer114"):
                    opp_val = getattr(item, "Customer114", None)
                    
                    if opp_val == self:
                        setattr(item, "Customer114", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Customer114"):
                    opp_val = getattr(item, "Customer114", None)
                    
                    setattr(item, "Customer114", self)
                    

    @property
    def programs(self):
        return self.__programs

    @programs.setter
    def programs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_LoyaltyProgram__programs", None)
        self.__programs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProgramPartner109"):
                    opp_val = getattr(item, "ProgramPartner109", None)
                    
                    if opp_val == self:
                        setattr(item, "ProgramPartner109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProgramPartner109"):
                    opp_val = getattr(item, "ProgramPartner109", None)
                    
                    setattr(item, "ProgramPartner109", self)
                    

    def enrollAndCreateCustomer(self, n: str, d: str) -> str:
        # TODO: Implement enrollAndCreateCustomer method
        pass

    def enroll(self, c: str):
        # TODO: Implement enroll method
        pass

    def addService(self, s: str, l: str, p: str):
        # TODO: Implement addService method
        pass

    def selectPopularPartners(self, d: str) -> str:
        # TODO: Implement selectPopularPartners method
        pass

    def addTransaction(self, amnt: float, accNr: int, servId: int, pName: str, d: str):
        # TODO: Implement addTransaction method
        pass

    def getServices(self, pp: str) -> str:
        # TODO: Implement getServices method
        pass

class RoyalAndLoyal_ProgramPartner:

    def __init__(self, name: str, numberOfCustomers: int, partner: set["RoyalAndLoyal_Service"] = None, partners: set["RoyalAndLoyal_LoyaltyProgram"] = None, RoyalAndLoyal_ProgramPartner: "RoyalAndLoyal_Container_RandL" = None, ProgramPartner: "RoyalAndLoyal_Service" = None, ProgramPartner109: "RoyalAndLoyal_LoyaltyProgram" = None):
        self.name = name
        self.numberOfCustomers = numberOfCustomers
        self.partner = partner if partner is not None else set()
        self.partners = partners if partners is not None else set()
        self.RoyalAndLoyal_ProgramPartner = RoyalAndLoyal_ProgramPartner
        self.ProgramPartner = ProgramPartner
        self.ProgramPartner109 = ProgramPartner109
        
    @property
    def numberOfCustomers(self) -> int:
        return self.__numberOfCustomers

    @numberOfCustomers.setter
    def numberOfCustomers(self, numberOfCustomers: int):
        self.__numberOfCustomers = numberOfCustomers

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def RoyalAndLoyal_ProgramPartner(self):
        return self.__RoyalAndLoyal_ProgramPartner

    @RoyalAndLoyal_ProgramPartner.setter
    def RoyalAndLoyal_ProgramPartner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_ProgramPartner__RoyalAndLoyal_ProgramPartner", None)
        self.__RoyalAndLoyal_ProgramPartner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Container_RandL81"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Container_RandL81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Container_RandL81"):
                opp_val = getattr(value, "RoyalAndLoyal_Container_RandL81", None)
                if opp_val is None:
                    setattr(value, "RoyalAndLoyal_Container_RandL81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ProgramPartner(self):
        return self.__ProgramPartner

    @ProgramPartner.setter
    def ProgramPartner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_ProgramPartner__ProgramPartner", None)
        self.__ProgramPartner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deliveredServices"):
                opp_val = getattr(old_value, "deliveredServices", None)
                if opp_val == self:
                    setattr(old_value, "deliveredServices", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deliveredServices"):
                opp_val = getattr(value, "deliveredServices", None)
                setattr(value, "deliveredServices", self)

    @property
    def ProgramPartner109(self):
        return self.__ProgramPartner109

    @ProgramPartner109.setter
    def ProgramPartner109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_ProgramPartner__ProgramPartner109", None)
        self.__ProgramPartner109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programs"):
                opp_val = getattr(old_value, "programs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programs"):
                opp_val = getattr(value, "programs", None)
                if opp_val is None:
                    setattr(value, "programs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def partner(self):
        return self.__partner

    @partner.setter
    def partner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_ProgramPartner__partner", None)
        self.__partner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service16"):
                    opp_val = getattr(item, "Service16", None)
                    
                    if opp_val == self:
                        setattr(item, "Service16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service16"):
                    opp_val = getattr(item, "Service16", None)
                    
                    setattr(item, "Service16", self)
                    

    @property
    def partners(self):
        return self.__partners

    @partners.setter
    def partners(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_ProgramPartner__partners", None)
        self.__partners = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "LoyaltyProgram18"):
                    opp_val = getattr(item, "LoyaltyProgram18", None)
                    
                    if opp_val == self:
                        setattr(item, "LoyaltyProgram18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "LoyaltyProgram18"):
                    opp_val = getattr(item, "LoyaltyProgram18", None)
                    
                    setattr(item, "LoyaltyProgram18", self)
                    

class Transaction:

    pass
class RoyalAndLoyal_Burning(Transaction):

    pass
class RoyalAndLoyal_Earning(Transaction):

    pass
class RoyalAndLoyal_ServiceLevel:

    def __init__(self, name: str, levels: "RoyalAndLoyal_LoyaltyProgram" = None, level: set["RoyalAndLoyal_Service"] = None, currentLevel: set["RoyalAndLoyal_Membership"] = None, RoyalAndLoyal_ServiceLevel: "RoyalAndLoyal_CustomerCard" = None, ServiceLevel: "RoyalAndLoyal_Membership" = None, ServiceLevel90: "RoyalAndLoyal_Service" = None, RoyalAndLoyal_ServiceLevel76: "RoyalAndLoyal_Container_RandL" = None, ServiceLevel111: "RoyalAndLoyal_LoyaltyProgram" = None):
        self.name = name
        self.levels = levels
        self.level = level if level is not None else set()
        self.currentLevel = currentLevel if currentLevel is not None else set()
        self.RoyalAndLoyal_ServiceLevel = RoyalAndLoyal_ServiceLevel
        self.ServiceLevel = ServiceLevel
        self.ServiceLevel90 = ServiceLevel90
        self.RoyalAndLoyal_ServiceLevel76 = RoyalAndLoyal_ServiceLevel76
        self.ServiceLevel111 = ServiceLevel111
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ServiceLevel(self):
        return self.__ServiceLevel

    @ServiceLevel.setter
    def ServiceLevel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_ServiceLevel__ServiceLevel", None)
        self.__ServiceLevel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Membership42"):
                opp_val = getattr(old_value, "Membership42", None)
                if opp_val == self:
                    setattr(old_value, "Membership42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Membership42"):
                opp_val = getattr(value, "Membership42", None)
                setattr(value, "Membership42", self)

    @property
    def ServiceLevel111(self):
        return self.__ServiceLevel111

    @ServiceLevel111.setter
    def ServiceLevel111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_ServiceLevel__ServiceLevel111", None)
        self.__ServiceLevel111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "program"):
                opp_val = getattr(old_value, "program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "program"):
                opp_val = getattr(value, "program", None)
                if opp_val is None:
                    setattr(value, "program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_ServiceLevel__level", None)
        self.__level = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service"):
                    opp_val = getattr(item, "Service", None)
                    
                    if opp_val == self:
                        setattr(item, "Service", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service"):
                    opp_val = getattr(item, "Service", None)
                    
                    setattr(item, "Service", self)
                    

    @property
    def levels(self):
        return self.__levels

    @levels.setter
    def levels(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_ServiceLevel__levels", None)
        self.__levels = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LoyaltyProgram"):
                opp_val = getattr(old_value, "LoyaltyProgram", None)
                if opp_val == self:
                    setattr(old_value, "LoyaltyProgram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LoyaltyProgram"):
                opp_val = getattr(value, "LoyaltyProgram", None)
                setattr(value, "LoyaltyProgram", self)

    @property
    def RoyalAndLoyal_ServiceLevel(self):
        return self.__RoyalAndLoyal_ServiceLevel

    @RoyalAndLoyal_ServiceLevel.setter
    def RoyalAndLoyal_ServiceLevel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_ServiceLevel__RoyalAndLoyal_ServiceLevel", None)
        self.__RoyalAndLoyal_ServiceLevel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_CustomerCard34"):
                opp_val = getattr(old_value, "RoyalAndLoyal_CustomerCard34", None)
                if opp_val == self:
                    setattr(old_value, "RoyalAndLoyal_CustomerCard34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_CustomerCard34"):
                opp_val = getattr(value, "RoyalAndLoyal_CustomerCard34", None)
                setattr(value, "RoyalAndLoyal_CustomerCard34", self)

    @property
    def RoyalAndLoyal_ServiceLevel76(self):
        return self.__RoyalAndLoyal_ServiceLevel76

    @RoyalAndLoyal_ServiceLevel76.setter
    def RoyalAndLoyal_ServiceLevel76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_ServiceLevel__RoyalAndLoyal_ServiceLevel76", None)
        self.__RoyalAndLoyal_ServiceLevel76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoyalAndLoyal_Container_RandL75"):
                opp_val = getattr(old_value, "RoyalAndLoyal_Container_RandL75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoyalAndLoyal_Container_RandL75"):
                opp_val = getattr(value, "RoyalAndLoyal_Container_RandL75", None)
                if opp_val is None:
                    setattr(value, "RoyalAndLoyal_Container_RandL75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ServiceLevel90(self):
        return self.__ServiceLevel90

    @ServiceLevel90.setter
    def ServiceLevel90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_ServiceLevel__ServiceLevel90", None)
        self.__ServiceLevel90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "availableServices"):
                opp_val = getattr(old_value, "availableServices", None)
                if opp_val == self:
                    setattr(old_value, "availableServices", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "availableServices"):
                opp_val = getattr(value, "availableServices", None)
                setattr(value, "availableServices", self)

    @property
    def currentLevel(self):
        return self.__currentLevel

    @currentLevel.setter
    def currentLevel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoyalAndLoyal_ServiceLevel__currentLevel", None)
        self.__currentLevel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Membership"):
                    opp_val = getattr(item, "Membership", None)
                    
                    if opp_val == self:
                        setattr(item, "Membership", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Membership"):
                    opp_val = getattr(item, "Membership", None)
                    
                    setattr(item, "Membership", self)
                    
