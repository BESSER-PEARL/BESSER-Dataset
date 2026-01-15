from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RandLColor(Enum):
    gold = "gold"
    silver = "silver"
class Gender(Enum):
    male = "male"
    female = "female"


############################################
# Definition of Classes
############################################

class RandL_Customer:

    def __init__(self, gender: str, isMale: str, name: str, title: str, age: str, RandL_Customer: "RandL_Membership" = None, RandL_Customer53: "RandL_Container_RandL" = None, Customer: "RandL_CustomerCard" = None, RandL_Customer92: "RandL_Date" = None, participants: set["RandL_LoyaltyProgram"] = None, owner: set["RandL_CustomerCard"] = None, RandL_Customer99: set["RandL_Membership"] = None, Customer114: "RandL_LoyaltyProgram" = None):
        self.gender = gender
        self.isMale = isMale
        self.name = name
        self.title = title
        self.age = age
        self.RandL_Customer = RandL_Customer
        self.RandL_Customer53 = RandL_Customer53
        self.Customer = Customer
        self.RandL_Customer92 = RandL_Customer92
        self.participants = participants if participants is not None else set()
        self.owner = owner if owner is not None else set()
        self.RandL_Customer99 = RandL_Customer99 if RandL_Customer99 is not None else set()
        self.Customer114 = Customer114
        
    @property
    def age(self) -> str:
        return self.__age

    @age.setter
    def age(self, age: str):
        self.__age = age

    @property
    def isMale(self) -> str:
        return self.__isMale

    @isMale.setter
    def isMale(self, isMale: str):
        self.__isMale = isMale

    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

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
    def RandL_Customer92(self):
        return self.__RandL_Customer92

    @RandL_Customer92.setter
    def RandL_Customer92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Customer__RandL_Customer92", None)
        self.__RandL_Customer92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_Date93"):
                opp_val = getattr(old_value, "RandL_Date93", None)
                if opp_val == self:
                    setattr(old_value, "RandL_Date93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_Date93"):
                opp_val = getattr(value, "RandL_Date93", None)
                setattr(value, "RandL_Date93", self)

    @property
    def Customer(self):
        return self.__Customer

    @Customer.setter
    def Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Customer__Customer", None)
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
    def participants(self):
        return self.__participants

    @participants.setter
    def participants(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Customer__participants", None)
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
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Customer__owner", None)
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
    def RandL_Customer53(self):
        return self.__RandL_Customer53

    @RandL_Customer53.setter
    def RandL_Customer53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Customer__RandL_Customer53", None)
        self.__RandL_Customer53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_Container_RandL"):
                opp_val = getattr(old_value, "RandL_Container_RandL", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_Container_RandL"):
                opp_val = getattr(value, "RandL_Container_RandL", None)
                if opp_val is None:
                    setattr(value, "RandL_Container_RandL", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RandL_Customer99(self):
        return self.__RandL_Customer99

    @RandL_Customer99.setter
    def RandL_Customer99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Customer__RandL_Customer99", None)
        self.__RandL_Customer99 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RandL_Membership100"):
                    opp_val = getattr(item, "RandL_Membership100", None)
                    
                    if opp_val == self:
                        setattr(item, "RandL_Membership100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RandL_Membership100"):
                    opp_val = getattr(item, "RandL_Membership100", None)
                    
                    setattr(item, "RandL_Membership100", self)
                    

    @property
    def RandL_Customer(self):
        return self.__RandL_Customer

    @RandL_Customer.setter
    def RandL_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Customer__RandL_Customer", None)
        self.__RandL_Customer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_Membership51"):
                opp_val = getattr(old_value, "RandL_Membership51", None)
                if opp_val == self:
                    setattr(old_value, "RandL_Membership51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_Membership51"):
                opp_val = getattr(value, "RandL_Membership51", None)
                setattr(value, "RandL_Membership51", self)

    @property
    def Customer114(self):
        return self.__Customer114

    @Customer114.setter
    def Customer114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Customer__Customer114", None)
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

    def birthdayHappens(self):
        # TODO: Implement birthdayHappens method
        pass

    def age(self) -> str:
        # TODO: Implement age method
        pass

class RandL_Container_RandL:

    pass
class RandL_TransactionReportLine:

    def __init__(self, amount: str, partnerName: str, serviceDesc: str, points: str, TransactionReportLine: "RandL_TransactionReport" = None, RandL_TransactionReportLine: "RandL_Container_RandL" = None, RandL_TransactionReportLine102: "RandL_Date" = None, RandL_TransactionReportLine105: "RandL_Transaction" = None, lines: "RandL_TransactionReport" = None):
        self.amount = amount
        self.partnerName = partnerName
        self.serviceDesc = serviceDesc
        self.points = points
        self.TransactionReportLine = TransactionReportLine
        self.RandL_TransactionReportLine = RandL_TransactionReportLine
        self.RandL_TransactionReportLine102 = RandL_TransactionReportLine102
        self.RandL_TransactionReportLine105 = RandL_TransactionReportLine105
        self.lines = lines
        
    @property
    def serviceDesc(self) -> str:
        return self.__serviceDesc

    @serviceDesc.setter
    def serviceDesc(self, serviceDesc: str):
        self.__serviceDesc = serviceDesc

    @property
    def points(self) -> str:
        return self.__points

    @points.setter
    def points(self, points: str):
        self.__points = points

    @property
    def amount(self) -> str:
        return self.__amount

    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

    @property
    def partnerName(self) -> str:
        return self.__partnerName

    @partnerName.setter
    def partnerName(self, partnerName: str):
        self.__partnerName = partnerName

    @property
    def TransactionReportLine(self):
        return self.__TransactionReportLine

    @TransactionReportLine.setter
    def TransactionReportLine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_TransactionReportLine__TransactionReportLine", None)
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
    def RandL_TransactionReportLine102(self):
        return self.__RandL_TransactionReportLine102

    @RandL_TransactionReportLine102.setter
    def RandL_TransactionReportLine102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_TransactionReportLine__RandL_TransactionReportLine102", None)
        self.__RandL_TransactionReportLine102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_Date103"):
                opp_val = getattr(old_value, "RandL_Date103", None)
                if opp_val == self:
                    setattr(old_value, "RandL_Date103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_Date103"):
                opp_val = getattr(value, "RandL_Date103", None)
                setattr(value, "RandL_Date103", self)

    @property
    def lines(self):
        return self.__lines

    @lines.setter
    def lines(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_TransactionReportLine__lines", None)
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
    def RandL_TransactionReportLine(self):
        return self.__RandL_TransactionReportLine

    @RandL_TransactionReportLine.setter
    def RandL_TransactionReportLine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_TransactionReportLine__RandL_TransactionReportLine", None)
        self.__RandL_TransactionReportLine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_Container_RandL85"):
                opp_val = getattr(old_value, "RandL_Container_RandL85", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_Container_RandL85"):
                opp_val = getattr(value, "RandL_Container_RandL85", None)
                if opp_val is None:
                    setattr(value, "RandL_Container_RandL85", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RandL_TransactionReportLine105(self):
        return self.__RandL_TransactionReportLine105

    @RandL_TransactionReportLine105.setter
    def RandL_TransactionReportLine105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_TransactionReportLine__RandL_TransactionReportLine105", None)
        self.__RandL_TransactionReportLine105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_Transaction106"):
                opp_val = getattr(old_value, "RandL_Transaction106", None)
                if opp_val == self:
                    setattr(old_value, "RandL_Transaction106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_Transaction106"):
                opp_val = getattr(value, "RandL_Transaction106", None)
                setattr(value, "RandL_Transaction106", self)

class RandL_TransactionReport:

    def __init__(self, balance: str, totalEarned: str, totalBurned: str, number: str, name: str, RandL_TransactionReport26: "RandL_CustomerCard" = None, RandL_TransactionReport: "RandL_Date" = None, RandL_TransactionReport22: "RandL_Date" = None, report: set["RandL_TransactionReportLine"] = None, RandL_TransactionReport79: "RandL_Container_RandL" = None, TransactionReport: "RandL_TransactionReportLine" = None):
        self.balance = balance
        self.totalEarned = totalEarned
        self.totalBurned = totalBurned
        self.number = number
        self.name = name
        self.RandL_TransactionReport26 = RandL_TransactionReport26
        self.RandL_TransactionReport = RandL_TransactionReport
        self.RandL_TransactionReport22 = RandL_TransactionReport22
        self.report = report if report is not None else set()
        self.RandL_TransactionReport79 = RandL_TransactionReport79
        self.TransactionReport = TransactionReport
        
    @property
    def totalEarned(self) -> str:
        return self.__totalEarned

    @totalEarned.setter
    def totalEarned(self, totalEarned: str):
        self.__totalEarned = totalEarned

    @property
    def totalBurned(self) -> str:
        return self.__totalBurned

    @totalBurned.setter
    def totalBurned(self, totalBurned: str):
        self.__totalBurned = totalBurned

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def balance(self) -> str:
        return self.__balance

    @balance.setter
    def balance(self, balance: str):
        self.__balance = balance

    @property
    def report(self):
        return self.__report

    @report.setter
    def report(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_TransactionReport__report", None)
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
    def RandL_TransactionReport22(self):
        return self.__RandL_TransactionReport22

    @RandL_TransactionReport22.setter
    def RandL_TransactionReport22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_TransactionReport__RandL_TransactionReport22", None)
        self.__RandL_TransactionReport22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_Date23"):
                opp_val = getattr(old_value, "RandL_Date23", None)
                if opp_val == self:
                    setattr(old_value, "RandL_Date23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_Date23"):
                opp_val = getattr(value, "RandL_Date23", None)
                setattr(value, "RandL_Date23", self)

    @property
    def TransactionReport(self):
        return self.__TransactionReport

    @TransactionReport.setter
    def TransactionReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_TransactionReport__TransactionReport", None)
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
    def RandL_TransactionReport79(self):
        return self.__RandL_TransactionReport79

    @RandL_TransactionReport79.setter
    def RandL_TransactionReport79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_TransactionReport__RandL_TransactionReport79", None)
        self.__RandL_TransactionReport79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_Container_RandL78"):
                opp_val = getattr(old_value, "RandL_Container_RandL78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_Container_RandL78"):
                opp_val = getattr(value, "RandL_Container_RandL78", None)
                if opp_val is None:
                    setattr(value, "RandL_Container_RandL78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RandL_TransactionReport(self):
        return self.__RandL_TransactionReport

    @RandL_TransactionReport.setter
    def RandL_TransactionReport(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_TransactionReport__RandL_TransactionReport", None)
        self.__RandL_TransactionReport = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_Date20"):
                opp_val = getattr(old_value, "RandL_Date20", None)
                if opp_val == self:
                    setattr(old_value, "RandL_Date20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_Date20"):
                opp_val = getattr(value, "RandL_Date20", None)
                setattr(value, "RandL_Date20", self)

    @property
    def RandL_TransactionReport26(self):
        return self.__RandL_TransactionReport26

    @RandL_TransactionReport26.setter
    def RandL_TransactionReport26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_TransactionReport__RandL_TransactionReport26", None)
        self.__RandL_TransactionReport26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_CustomerCard"):
                opp_val = getattr(old_value, "RandL_CustomerCard", None)
                if opp_val == self:
                    setattr(old_value, "RandL_CustomerCard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_CustomerCard"):
                opp_val = getattr(value, "RandL_CustomerCard", None)
                setattr(value, "RandL_CustomerCard", self)

class RandL_CustomerCard:

    def __init__(self, valid: str, color: str, printedName: str, CustomerCard: "RandL_Transaction" = None, RandL_CustomerCard: "RandL_TransactionReport" = None, RandL_CustomerCard28: "RandL_Date" = None, RandL_CustomerCard31: "RandL_Date" = None, CustomerCard45: "RandL_Membership" = None, RandL_CustomerCard59: "RandL_Container_RandL" = None, RandL_CustomerCard34: "RandL_ServiceLevel" = None, cards: "RandL_Customer" = None, card: "RandL_Membership" = None, card39: set["RandL_Transaction"] = None, CustomerCard97: "RandL_Customer" = None):
        self.valid = valid
        self.color = color
        self.printedName = printedName
        self.CustomerCard = CustomerCard
        self.RandL_CustomerCard = RandL_CustomerCard
        self.RandL_CustomerCard28 = RandL_CustomerCard28
        self.RandL_CustomerCard31 = RandL_CustomerCard31
        self.CustomerCard45 = CustomerCard45
        self.RandL_CustomerCard59 = RandL_CustomerCard59
        self.RandL_CustomerCard34 = RandL_CustomerCard34
        self.cards = cards
        self.card = card
        self.card39 = card39 if card39 is not None else set()
        self.CustomerCard97 = CustomerCard97
        
    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

    @property
    def valid(self) -> str:
        return self.__valid

    @valid.setter
    def valid(self, valid: str):
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
        old_value = getattr(self, f"_RandL_CustomerCard__card", None)
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
    def CustomerCard45(self):
        return self.__CustomerCard45

    @CustomerCard45.setter
    def CustomerCard45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_CustomerCard__CustomerCard45", None)
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
    def CustomerCard97(self):
        return self.__CustomerCard97

    @CustomerCard97.setter
    def CustomerCard97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_CustomerCard__CustomerCard97", None)
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
    def RandL_CustomerCard31(self):
        return self.__RandL_CustomerCard31

    @RandL_CustomerCard31.setter
    def RandL_CustomerCard31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_CustomerCard__RandL_CustomerCard31", None)
        self.__RandL_CustomerCard31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_Date32"):
                opp_val = getattr(old_value, "RandL_Date32", None)
                if opp_val == self:
                    setattr(old_value, "RandL_Date32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_Date32"):
                opp_val = getattr(value, "RandL_Date32", None)
                setattr(value, "RandL_Date32", self)

    @property
    def RandL_CustomerCard34(self):
        return self.__RandL_CustomerCard34

    @RandL_CustomerCard34.setter
    def RandL_CustomerCard34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_CustomerCard__RandL_CustomerCard34", None)
        self.__RandL_CustomerCard34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_ServiceLevel"):
                opp_val = getattr(old_value, "RandL_ServiceLevel", None)
                if opp_val == self:
                    setattr(old_value, "RandL_ServiceLevel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_ServiceLevel"):
                opp_val = getattr(value, "RandL_ServiceLevel", None)
                setattr(value, "RandL_ServiceLevel", self)

    @property
    def RandL_CustomerCard(self):
        return self.__RandL_CustomerCard

    @RandL_CustomerCard.setter
    def RandL_CustomerCard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_CustomerCard__RandL_CustomerCard", None)
        self.__RandL_CustomerCard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_TransactionReport26"):
                opp_val = getattr(old_value, "RandL_TransactionReport26", None)
                if opp_val == self:
                    setattr(old_value, "RandL_TransactionReport26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_TransactionReport26"):
                opp_val = getattr(value, "RandL_TransactionReport26", None)
                setattr(value, "RandL_TransactionReport26", self)

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_CustomerCard__cards", None)
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
    def RandL_CustomerCard28(self):
        return self.__RandL_CustomerCard28

    @RandL_CustomerCard28.setter
    def RandL_CustomerCard28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_CustomerCard__RandL_CustomerCard28", None)
        self.__RandL_CustomerCard28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_Date29"):
                opp_val = getattr(old_value, "RandL_Date29", None)
                if opp_val == self:
                    setattr(old_value, "RandL_Date29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_Date29"):
                opp_val = getattr(value, "RandL_Date29", None)
                setattr(value, "RandL_Date29", self)

    @property
    def card39(self):
        return self.__card39

    @card39.setter
    def card39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_CustomerCard__card39", None)
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
                    

    @property
    def CustomerCard(self):
        return self.__CustomerCard

    @CustomerCard.setter
    def CustomerCard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_CustomerCard__CustomerCard", None)
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
    def RandL_CustomerCard59(self):
        return self.__RandL_CustomerCard59

    @RandL_CustomerCard59.setter
    def RandL_CustomerCard59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_CustomerCard__RandL_CustomerCard59", None)
        self.__RandL_CustomerCard59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_Container_RandL58"):
                opp_val = getattr(old_value, "RandL_Container_RandL58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_Container_RandL58"):
                opp_val = getattr(value, "RandL_Container_RandL58", None)
                if opp_val is None:
                    setattr(value, "RandL_Container_RandL58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getTransactions(self, until: str, from: str) -> Transaction:
        # TODO: Implement getTransactions method
        pass

class RandL_LoyaltyAccount:

    def __init__(self, number: str, points: str, totalPointsEarned: str, RandL_LoyaltyAccount: set["RandL_Service"] = None, account: "RandL_Membership" = None, account14: set["RandL_Transaction"] = None, LoyaltyAccount: "RandL_Transaction" = None, LoyaltyAccount48: "RandL_Membership" = None, RandL_LoyaltyAccount73: "RandL_Container_RandL" = None):
        self.number = number
        self.points = points
        self.totalPointsEarned = totalPointsEarned
        self.RandL_LoyaltyAccount = RandL_LoyaltyAccount if RandL_LoyaltyAccount is not None else set()
        self.account = account
        self.account14 = account14 if account14 is not None else set()
        self.LoyaltyAccount = LoyaltyAccount
        self.LoyaltyAccount48 = LoyaltyAccount48
        self.RandL_LoyaltyAccount73 = RandL_LoyaltyAccount73
        
    @property
    def totalPointsEarned(self) -> str:
        return self.__totalPointsEarned

    @totalPointsEarned.setter
    def totalPointsEarned(self, totalPointsEarned: str):
        self.__totalPointsEarned = totalPointsEarned

    @property
    def points(self) -> str:
        return self.__points

    @points.setter
    def points(self, points: str):
        self.__points = points

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def RandL_LoyaltyAccount(self):
        return self.__RandL_LoyaltyAccount

    @RandL_LoyaltyAccount.setter
    def RandL_LoyaltyAccount(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_LoyaltyAccount__RandL_LoyaltyAccount", None)
        self.__RandL_LoyaltyAccount = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RandL_Service"):
                    opp_val = getattr(item, "RandL_Service", None)
                    
                    if opp_val == self:
                        setattr(item, "RandL_Service", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RandL_Service"):
                    opp_val = getattr(item, "RandL_Service", None)
                    
                    setattr(item, "RandL_Service", self)
                    

    @property
    def RandL_LoyaltyAccount73(self):
        return self.__RandL_LoyaltyAccount73

    @RandL_LoyaltyAccount73.setter
    def RandL_LoyaltyAccount73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_LoyaltyAccount__RandL_LoyaltyAccount73", None)
        self.__RandL_LoyaltyAccount73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_Container_RandL72"):
                opp_val = getattr(old_value, "RandL_Container_RandL72", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_Container_RandL72"):
                opp_val = getattr(value, "RandL_Container_RandL72", None)
                if opp_val is None:
                    setattr(value, "RandL_Container_RandL72", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def LoyaltyAccount48(self):
        return self.__LoyaltyAccount48

    @LoyaltyAccount48.setter
    def LoyaltyAccount48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_LoyaltyAccount__LoyaltyAccount48", None)
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
        old_value = getattr(self, f"_RandL_LoyaltyAccount__account14", None)
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
    def LoyaltyAccount(self):
        return self.__LoyaltyAccount

    @LoyaltyAccount.setter
    def LoyaltyAccount(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_LoyaltyAccount__LoyaltyAccount", None)
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
    def account(self):
        return self.__account

    @account.setter
    def account(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_LoyaltyAccount__account", None)
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

    def burn(self, i: str):
        # TODO: Implement burn method
        pass

    def isEmpty(self) -> str:
        # TODO: Implement isEmpty method
        pass

    def getCustomerName(self) -> str:
        # TODO: Implement getCustomerName method
        pass

    def earn(self, i: str):
        # TODO: Implement earn method
        pass

class RandL_Date:

    def __init__(self, year: str, month: str, day: str, RandL_Date: "RandL_Transaction" = None, RandL_Date29: "RandL_CustomerCard" = None, RandL_Date32: "RandL_CustomerCard" = None, RandL_Date20: "RandL_TransactionReport" = None, RandL_Date23: "RandL_TransactionReport" = None, RandL_Date56: "RandL_Container_RandL" = None, RandL_Date103: "RandL_TransactionReportLine" = None, RandL_Date93: "RandL_Customer" = None):
        self.year = year
        self.month = month
        self.day = day
        self.RandL_Date = RandL_Date
        self.RandL_Date29 = RandL_Date29
        self.RandL_Date32 = RandL_Date32
        self.RandL_Date20 = RandL_Date20
        self.RandL_Date23 = RandL_Date23
        self.RandL_Date56 = RandL_Date56
        self.RandL_Date103 = RandL_Date103
        self.RandL_Date93 = RandL_Date93
        
    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def day(self) -> str:
        return self.__day

    @day.setter
    def day(self, day: str):
        self.__day = day

    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def RandL_Date56(self):
        return self.__RandL_Date56

    @RandL_Date56.setter
    def RandL_Date56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Date__RandL_Date56", None)
        self.__RandL_Date56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_Container_RandL55"):
                opp_val = getattr(old_value, "RandL_Container_RandL55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_Container_RandL55"):
                opp_val = getattr(value, "RandL_Container_RandL55", None)
                if opp_val is None:
                    setattr(value, "RandL_Container_RandL55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RandL_Date23(self):
        return self.__RandL_Date23

    @RandL_Date23.setter
    def RandL_Date23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Date__RandL_Date23", None)
        self.__RandL_Date23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_TransactionReport22"):
                opp_val = getattr(old_value, "RandL_TransactionReport22", None)
                if opp_val == self:
                    setattr(old_value, "RandL_TransactionReport22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_TransactionReport22"):
                opp_val = getattr(value, "RandL_TransactionReport22", None)
                setattr(value, "RandL_TransactionReport22", self)

    @property
    def RandL_Date32(self):
        return self.__RandL_Date32

    @RandL_Date32.setter
    def RandL_Date32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Date__RandL_Date32", None)
        self.__RandL_Date32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_CustomerCard31"):
                opp_val = getattr(old_value, "RandL_CustomerCard31", None)
                if opp_val == self:
                    setattr(old_value, "RandL_CustomerCard31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_CustomerCard31"):
                opp_val = getattr(value, "RandL_CustomerCard31", None)
                setattr(value, "RandL_CustomerCard31", self)

    @property
    def RandL_Date29(self):
        return self.__RandL_Date29

    @RandL_Date29.setter
    def RandL_Date29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Date__RandL_Date29", None)
        self.__RandL_Date29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_CustomerCard28"):
                opp_val = getattr(old_value, "RandL_CustomerCard28", None)
                if opp_val == self:
                    setattr(old_value, "RandL_CustomerCard28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_CustomerCard28"):
                opp_val = getattr(value, "RandL_CustomerCard28", None)
                setattr(value, "RandL_CustomerCard28", self)

    @property
    def RandL_Date(self):
        return self.__RandL_Date

    @RandL_Date.setter
    def RandL_Date(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Date__RandL_Date", None)
        self.__RandL_Date = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_Transaction"):
                opp_val = getattr(old_value, "RandL_Transaction", None)
                if opp_val == self:
                    setattr(old_value, "RandL_Transaction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_Transaction"):
                opp_val = getattr(value, "RandL_Transaction", None)
                setattr(value, "RandL_Transaction", self)

    @property
    def RandL_Date20(self):
        return self.__RandL_Date20

    @RandL_Date20.setter
    def RandL_Date20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Date__RandL_Date20", None)
        self.__RandL_Date20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_TransactionReport"):
                opp_val = getattr(old_value, "RandL_TransactionReport", None)
                if opp_val == self:
                    setattr(old_value, "RandL_TransactionReport", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_TransactionReport"):
                opp_val = getattr(value, "RandL_TransactionReport", None)
                setattr(value, "RandL_TransactionReport", self)

    @property
    def RandL_Date103(self):
        return self.__RandL_Date103

    @RandL_Date103.setter
    def RandL_Date103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Date__RandL_Date103", None)
        self.__RandL_Date103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_TransactionReportLine102"):
                opp_val = getattr(old_value, "RandL_TransactionReportLine102", None)
                if opp_val == self:
                    setattr(old_value, "RandL_TransactionReportLine102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_TransactionReportLine102"):
                opp_val = getattr(value, "RandL_TransactionReportLine102", None)
                setattr(value, "RandL_TransactionReportLine102", self)

    @property
    def RandL_Date93(self):
        return self.__RandL_Date93

    @RandL_Date93.setter
    def RandL_Date93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Date__RandL_Date93", None)
        self.__RandL_Date93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_Customer92"):
                opp_val = getattr(old_value, "RandL_Customer92", None)
                if opp_val == self:
                    setattr(old_value, "RandL_Customer92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_Customer92"):
                opp_val = getattr(value, "RandL_Customer92", None)
                setattr(value, "RandL_Customer92", self)

    def fromYMD(self, y: str, m: str, k: str) -> str:
        # TODO: Implement fromYMD method
        pass

    def isBefore(self, t: str) -> str:
        # TODO: Implement isBefore method
        pass

    def isAfter(self, t: str) -> str:
        # TODO: Implement isAfter method
        pass

    def isEqual(self, t: str) -> str:
        # TODO: Implement isEqual method
        pass

class RandL_ProgramPartner:

    def __init__(self, name: str, numberOfCustomers: str, partner: set["RandL_Service"] = None, partners: set["RandL_LoyaltyProgram"] = None, ProgramPartner: "RandL_Service" = None, RandL_ProgramPartner: "RandL_Container_RandL" = None, ProgramPartner109: "RandL_LoyaltyProgram" = None):
        self.name = name
        self.numberOfCustomers = numberOfCustomers
        self.partner = partner if partner is not None else set()
        self.partners = partners if partners is not None else set()
        self.ProgramPartner = ProgramPartner
        self.RandL_ProgramPartner = RandL_ProgramPartner
        self.ProgramPartner109 = ProgramPartner109
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def numberOfCustomers(self) -> str:
        return self.__numberOfCustomers

    @numberOfCustomers.setter
    def numberOfCustomers(self, numberOfCustomers: str):
        self.__numberOfCustomers = numberOfCustomers

    @property
    def ProgramPartner(self):
        return self.__ProgramPartner

    @ProgramPartner.setter
    def ProgramPartner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_ProgramPartner__ProgramPartner", None)
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
    def partners(self):
        return self.__partners

    @partners.setter
    def partners(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_ProgramPartner__partners", None)
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
                    

    @property
    def ProgramPartner109(self):
        return self.__ProgramPartner109

    @ProgramPartner109.setter
    def ProgramPartner109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_ProgramPartner__ProgramPartner109", None)
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
        old_value = getattr(self, f"_RandL_ProgramPartner__partner", None)
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
    def RandL_ProgramPartner(self):
        return self.__RandL_ProgramPartner

    @RandL_ProgramPartner.setter
    def RandL_ProgramPartner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_ProgramPartner__RandL_ProgramPartner", None)
        self.__RandL_ProgramPartner = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_Container_RandL81"):
                opp_val = getattr(old_value, "RandL_Container_RandL81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_Container_RandL81"):
                opp_val = getattr(value, "RandL_Container_RandL81", None)
                if opp_val is None:
                    setattr(value, "RandL_Container_RandL81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Transaction:

    pass
class RandL_Burning(Transaction):

    pass
class RandL_Earning(Transaction):

    pass
class RandL_Transaction(ABC):

    def __init__(self, amount: str, points: str, Transaction: "RandL_LoyaltyAccount" = None, RandL_Transaction: "RandL_Date" = None, transactions: "RandL_LoyaltyAccount" = None, transactions6: "RandL_Service" = None, transactions9: "RandL_CustomerCard" = None, Transaction40: "RandL_CustomerCard" = None, Transaction88: "RandL_Service" = None, RandL_Transaction106: "RandL_TransactionReportLine" = None):
        self.amount = amount
        self.points = points
        self.Transaction = Transaction
        self.RandL_Transaction = RandL_Transaction
        self.transactions = transactions
        self.transactions6 = transactions6
        self.transactions9 = transactions9
        self.Transaction40 = Transaction40
        self.Transaction88 = Transaction88
        self.RandL_Transaction106 = RandL_Transaction106
        
    @property
    def points(self) -> str:
        return self.__points

    @points.setter
    def points(self, points: str):
        self.__points = points

    @property
    def amount(self) -> str:
        return self.__amount

    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

    @property
    def transactions9(self):
        return self.__transactions9

    @transactions9.setter
    def transactions9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Transaction__transactions9", None)
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
    def Transaction88(self):
        return self.__Transaction88

    @Transaction88.setter
    def Transaction88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Transaction__Transaction88", None)
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
    def transactions6(self):
        return self.__transactions6

    @transactions6.setter
    def transactions6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Transaction__transactions6", None)
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
    def transactions(self):
        return self.__transactions

    @transactions.setter
    def transactions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Transaction__transactions", None)
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
    def RandL_Transaction106(self):
        return self.__RandL_Transaction106

    @RandL_Transaction106.setter
    def RandL_Transaction106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Transaction__RandL_Transaction106", None)
        self.__RandL_Transaction106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_TransactionReportLine105"):
                opp_val = getattr(old_value, "RandL_TransactionReportLine105", None)
                if opp_val == self:
                    setattr(old_value, "RandL_TransactionReportLine105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_TransactionReportLine105"):
                opp_val = getattr(value, "RandL_TransactionReportLine105", None)
                setattr(value, "RandL_TransactionReportLine105", self)

    @property
    def Transaction40(self):
        return self.__Transaction40

    @Transaction40.setter
    def Transaction40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Transaction__Transaction40", None)
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
    def RandL_Transaction(self):
        return self.__RandL_Transaction

    @RandL_Transaction.setter
    def RandL_Transaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Transaction__RandL_Transaction", None)
        self.__RandL_Transaction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_Date"):
                opp_val = getattr(old_value, "RandL_Date", None)
                if opp_val == self:
                    setattr(old_value, "RandL_Date", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_Date"):
                opp_val = getattr(value, "RandL_Date", None)
                setattr(value, "RandL_Date", self)

    @property
    def Transaction(self):
        return self.__Transaction

    @Transaction.setter
    def Transaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Transaction__Transaction", None)
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

class RandL_Membership:

    pass
class RandL_Service:

    def __init__(self, serviceNr: str, description: str, pointsEarned: str, condition: str, pointsBurned: str, Service: "RandL_ServiceLevel" = None, RandL_Service: "RandL_LoyaltyAccount" = None, Service16: "RandL_ProgramPartner" = None, Service7: "RandL_Transaction" = None, deliveredServices: "RandL_ProgramPartner" = None, generatedBy: set["RandL_Transaction"] = None, availableServices: "RandL_ServiceLevel" = None, RandL_Service65: "RandL_Container_RandL" = None):
        self.serviceNr = serviceNr
        self.description = description
        self.pointsEarned = pointsEarned
        self.condition = condition
        self.pointsBurned = pointsBurned
        self.Service = Service
        self.RandL_Service = RandL_Service
        self.Service16 = Service16
        self.Service7 = Service7
        self.deliveredServices = deliveredServices
        self.generatedBy = generatedBy if generatedBy is not None else set()
        self.availableServices = availableServices
        self.RandL_Service65 = RandL_Service65
        
    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

    @property
    def pointsEarned(self) -> str:
        return self.__pointsEarned

    @pointsEarned.setter
    def pointsEarned(self, pointsEarned: str):
        self.__pointsEarned = pointsEarned

    @property
    def serviceNr(self) -> str:
        return self.__serviceNr

    @serviceNr.setter
    def serviceNr(self, serviceNr: str):
        self.__serviceNr = serviceNr

    @property
    def pointsBurned(self) -> str:
        return self.__pointsBurned

    @pointsBurned.setter
    def pointsBurned(self, pointsBurned: str):
        self.__pointsBurned = pointsBurned

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def RandL_Service65(self):
        return self.__RandL_Service65

    @RandL_Service65.setter
    def RandL_Service65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Service__RandL_Service65", None)
        self.__RandL_Service65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_Container_RandL64"):
                opp_val = getattr(old_value, "RandL_Container_RandL64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_Container_RandL64"):
                opp_val = getattr(value, "RandL_Container_RandL64", None)
                if opp_val is None:
                    setattr(value, "RandL_Container_RandL64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def RandL_Service(self):
        return self.__RandL_Service

    @RandL_Service.setter
    def RandL_Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Service__RandL_Service", None)
        self.__RandL_Service = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_LoyaltyAccount"):
                opp_val = getattr(old_value, "RandL_LoyaltyAccount", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_LoyaltyAccount"):
                opp_val = getattr(value, "RandL_LoyaltyAccount", None)
                if opp_val is None:
                    setattr(value, "RandL_LoyaltyAccount", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def deliveredServices(self):
        return self.__deliveredServices

    @deliveredServices.setter
    def deliveredServices(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Service__deliveredServices", None)
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

    @property
    def Service7(self):
        return self.__Service7

    @Service7.setter
    def Service7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Service__Service7", None)
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
    def Service(self):
        return self.__Service

    @Service.setter
    def Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Service__Service", None)
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
        old_value = getattr(self, f"_RandL_Service__availableServices", None)
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
    def Service16(self):
        return self.__Service16

    @Service16.setter
    def Service16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Service__Service16", None)
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
    def generatedBy(self):
        return self.__generatedBy

    @generatedBy.setter
    def generatedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_Service__generatedBy", None)
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
                    

    def calcPoints(self) -> str:
        # TODO: Implement calcPoints method
        pass

    def upgradePointsEarned(self, amount: str):
        # TODO: Implement upgradePointsEarned method
        pass

class RandL_LoyaltyProgram:

    def __init__(self, name: str, LoyaltyProgram: "RandL_ServiceLevel" = None, LoyaltyProgram18: "RandL_ProgramPartner" = None, RandL_LoyaltyProgram: "RandL_Membership" = None, RandL_LoyaltyProgram68: "RandL_Container_RandL" = None, LoyaltyProgram95: "RandL_Customer" = None, programs: set["RandL_ProgramPartner"] = None, program: set["RandL_ServiceLevel"] = None, programs113: set["RandL_Customer"] = None, RandL_LoyaltyProgram116: set["RandL_Membership"] = None):
        self.name = name
        self.LoyaltyProgram = LoyaltyProgram
        self.LoyaltyProgram18 = LoyaltyProgram18
        self.RandL_LoyaltyProgram = RandL_LoyaltyProgram
        self.RandL_LoyaltyProgram68 = RandL_LoyaltyProgram68
        self.LoyaltyProgram95 = LoyaltyProgram95
        self.programs = programs if programs is not None else set()
        self.program = program if program is not None else set()
        self.programs113 = programs113 if programs113 is not None else set()
        self.RandL_LoyaltyProgram116 = RandL_LoyaltyProgram116 if RandL_LoyaltyProgram116 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def RandL_LoyaltyProgram116(self):
        return self.__RandL_LoyaltyProgram116

    @RandL_LoyaltyProgram116.setter
    def RandL_LoyaltyProgram116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_LoyaltyProgram__RandL_LoyaltyProgram116", None)
        self.__RandL_LoyaltyProgram116 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RandL_Membership117"):
                    opp_val = getattr(item, "RandL_Membership117", None)
                    
                    if opp_val == self:
                        setattr(item, "RandL_Membership117", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RandL_Membership117"):
                    opp_val = getattr(item, "RandL_Membership117", None)
                    
                    setattr(item, "RandL_Membership117", self)
                    

    @property
    def RandL_LoyaltyProgram(self):
        return self.__RandL_LoyaltyProgram

    @RandL_LoyaltyProgram.setter
    def RandL_LoyaltyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_LoyaltyProgram__RandL_LoyaltyProgram", None)
        self.__RandL_LoyaltyProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_Membership"):
                opp_val = getattr(old_value, "RandL_Membership", None)
                if opp_val == self:
                    setattr(old_value, "RandL_Membership", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_Membership"):
                opp_val = getattr(value, "RandL_Membership", None)
                setattr(value, "RandL_Membership", self)

    @property
    def RandL_LoyaltyProgram68(self):
        return self.__RandL_LoyaltyProgram68

    @RandL_LoyaltyProgram68.setter
    def RandL_LoyaltyProgram68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_LoyaltyProgram__RandL_LoyaltyProgram68", None)
        self.__RandL_LoyaltyProgram68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_Container_RandL67"):
                opp_val = getattr(old_value, "RandL_Container_RandL67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_Container_RandL67"):
                opp_val = getattr(value, "RandL_Container_RandL67", None)
                if opp_val is None:
                    setattr(value, "RandL_Container_RandL67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def LoyaltyProgram95(self):
        return self.__LoyaltyProgram95

    @LoyaltyProgram95.setter
    def LoyaltyProgram95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_LoyaltyProgram__LoyaltyProgram95", None)
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
        old_value = getattr(self, f"_RandL_LoyaltyProgram__LoyaltyProgram18", None)
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
    def program(self):
        return self.__program

    @program.setter
    def program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_LoyaltyProgram__program", None)
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
        old_value = getattr(self, f"_RandL_LoyaltyProgram__LoyaltyProgram", None)
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
    def programs(self):
        return self.__programs

    @programs.setter
    def programs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_LoyaltyProgram__programs", None)
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
                    

    @property
    def programs113(self):
        return self.__programs113

    @programs113.setter
    def programs113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_LoyaltyProgram__programs113", None)
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
                    

    def addService(self, p: str, l: str, s: str):
        # TODO: Implement addService method
        pass

    def enrollAndCreateCustomer(self, d: str, n: str) -> str:
        # TODO: Implement enrollAndCreateCustomer method
        pass

    def selectPopularPartners(self, d: str) -> str:
        # TODO: Implement selectPopularPartners method
        pass

    def addTransaction(self, amnt: str, pName: str, accNr: str, d: str, servId: str):
        # TODO: Implement addTransaction method
        pass

    def getServices(self, pp: str) -> str:
        # TODO: Implement getServices method
        pass

    def getServices(self) -> str:
        # TODO: Implement getServices method
        pass

    def enroll(self, c: str):
        # TODO: Implement enroll method
        pass

class RandL_ServiceLevel:

    def __init__(self, name: str, levels: "RandL_LoyaltyProgram" = None, level: set["RandL_Service"] = None, currentLevel: set["RandL_Membership"] = None, ServiceLevel: "RandL_Membership" = None, RandL_ServiceLevel: "RandL_CustomerCard" = None, ServiceLevel90: "RandL_Service" = None, RandL_ServiceLevel76: "RandL_Container_RandL" = None, ServiceLevel111: "RandL_LoyaltyProgram" = None):
        self.name = name
        self.levels = levels
        self.level = level if level is not None else set()
        self.currentLevel = currentLevel if currentLevel is not None else set()
        self.ServiceLevel = ServiceLevel
        self.RandL_ServiceLevel = RandL_ServiceLevel
        self.ServiceLevel90 = ServiceLevel90
        self.RandL_ServiceLevel76 = RandL_ServiceLevel76
        self.ServiceLevel111 = ServiceLevel111
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_ServiceLevel__level", None)
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
    def RandL_ServiceLevel76(self):
        return self.__RandL_ServiceLevel76

    @RandL_ServiceLevel76.setter
    def RandL_ServiceLevel76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_ServiceLevel__RandL_ServiceLevel76", None)
        self.__RandL_ServiceLevel76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_Container_RandL75"):
                opp_val = getattr(old_value, "RandL_Container_RandL75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_Container_RandL75"):
                opp_val = getattr(value, "RandL_Container_RandL75", None)
                if opp_val is None:
                    setattr(value, "RandL_Container_RandL75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ServiceLevel90(self):
        return self.__ServiceLevel90

    @ServiceLevel90.setter
    def ServiceLevel90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_ServiceLevel__ServiceLevel90", None)
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
    def RandL_ServiceLevel(self):
        return self.__RandL_ServiceLevel

    @RandL_ServiceLevel.setter
    def RandL_ServiceLevel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_ServiceLevel__RandL_ServiceLevel", None)
        self.__RandL_ServiceLevel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RandL_CustomerCard34"):
                opp_val = getattr(old_value, "RandL_CustomerCard34", None)
                if opp_val == self:
                    setattr(old_value, "RandL_CustomerCard34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RandL_CustomerCard34"):
                opp_val = getattr(value, "RandL_CustomerCard34", None)
                setattr(value, "RandL_CustomerCard34", self)

    @property
    def ServiceLevel111(self):
        return self.__ServiceLevel111

    @ServiceLevel111.setter
    def ServiceLevel111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_ServiceLevel__ServiceLevel111", None)
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
    def ServiceLevel(self):
        return self.__ServiceLevel

    @ServiceLevel.setter
    def ServiceLevel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_ServiceLevel__ServiceLevel", None)
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
    def levels(self):
        return self.__levels

    @levels.setter
    def levels(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_ServiceLevel__levels", None)
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
    def currentLevel(self):
        return self.__currentLevel

    @currentLevel.setter
    def currentLevel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RandL_ServiceLevel__currentLevel", None)
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
                    
