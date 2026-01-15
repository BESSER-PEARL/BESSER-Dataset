from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ObjectiveType(Enum):
    None = "None"
    Strategic = "Strategic"
    Tactic = "Tactic"
    Operational = "Operational"
class ObjectiveNature(Enum):
    None = "None"
    Performance = "Performance"
    Quality = "Quality"
    Delay = "Delay"
    Cost = "Cost"
    Environmental = "Environmental"
    Legal = "Legal"
    Human = "Human"
    Economical = "Economical"
    Other = "Other"
class RoleType(Enum):
    Composite = "Composite"
    Decision = "Decision"
    Transformation = "Transformation"
    Control = "Control"
class Hierarchy(Enum):
    Supervisor = "Supervisor"
    Subordinate = "Subordinate"


############################################
# Definition of Classes
############################################

class company104_Interval(ABC):

    def __init__(self, dateFrom: str, dateTo: str):
        self.dateFrom = dateFrom
        self.dateTo = dateTo
        
    @property
    def dateTo(self) -> str:
        return self.__dateTo

    @dateTo.setter
    def dateTo(self, dateTo: str):
        self.__dateTo = dateTo

    @property
    def dateFrom(self) -> str:
        return self.__dateFrom

    @dateFrom.setter
    def dateFrom(self, dateFrom: str):
        self.__dateFrom = dateFrom

class company104_ObjectiveReach:

    def __init__(self, value: float, statement: str, company104_ObjectiveReach: "company104_Agency" = None, company104_ObjectiveReach36: "company104_Objective" = None, company104_ObjectiveReach39: "company104_Agency" = None):
        self.value = value
        self.statement = statement
        self.company104_ObjectiveReach = company104_ObjectiveReach
        self.company104_ObjectiveReach36 = company104_ObjectiveReach36
        self.company104_ObjectiveReach39 = company104_ObjectiveReach39
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def statement(self) -> str:
        return self.__statement

    @statement.setter
    def statement(self, statement: str):
        self.__statement = statement

    @property
    def company104_ObjectiveReach39(self):
        return self.__company104_ObjectiveReach39

    @company104_ObjectiveReach39.setter
    def company104_ObjectiveReach39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_ObjectiveReach__company104_ObjectiveReach39", None)
        self.__company104_ObjectiveReach39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company104_Agency40"):
                opp_val = getattr(old_value, "company104_Agency40", None)
                if opp_val == self:
                    setattr(old_value, "company104_Agency40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company104_Agency40"):
                opp_val = getattr(value, "company104_Agency40", None)
                setattr(value, "company104_Agency40", self)

    @property
    def company104_ObjectiveReach(self):
        return self.__company104_ObjectiveReach

    @company104_ObjectiveReach.setter
    def company104_ObjectiveReach(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_ObjectiveReach__company104_ObjectiveReach", None)
        self.__company104_ObjectiveReach = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company104_Agency34"):
                opp_val = getattr(old_value, "company104_Agency34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company104_Agency34"):
                opp_val = getattr(value, "company104_Agency34", None)
                if opp_val is None:
                    setattr(value, "company104_Agency34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def company104_ObjectiveReach36(self):
        return self.__company104_ObjectiveReach36

    @company104_ObjectiveReach36.setter
    def company104_ObjectiveReach36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_ObjectiveReach__company104_ObjectiveReach36", None)
        self.__company104_ObjectiveReach36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company104_Objective37"):
                opp_val = getattr(old_value, "company104_Objective37", None)
                if opp_val == self:
                    setattr(old_value, "company104_Objective37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company104_Objective37"):
                opp_val = getattr(value, "company104_Objective37", None)
                setattr(value, "company104_Objective37", self)

class company104_Objective:

    def __init__(self, nature: str, type: str, value: float, company104_Objective: "company104_Goal" = None, company104_Objective37: "company104_ObjectiveReach" = None):
        self.nature = nature
        self.type = type
        self.value = value
        self.company104_Objective = company104_Objective
        self.company104_Objective37 = company104_Objective37
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def nature(self) -> str:
        return self.__nature

    @nature.setter
    def nature(self, nature: str):
        self.__nature = nature

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def company104_Objective37(self):
        return self.__company104_Objective37

    @company104_Objective37.setter
    def company104_Objective37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_Objective__company104_Objective37", None)
        self.__company104_Objective37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company104_ObjectiveReach36"):
                opp_val = getattr(old_value, "company104_ObjectiveReach36", None)
                if opp_val == self:
                    setattr(old_value, "company104_ObjectiveReach36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company104_ObjectiveReach36"):
                opp_val = getattr(value, "company104_ObjectiveReach36", None)
                setattr(value, "company104_ObjectiveReach36", self)

    @property
    def company104_Objective(self):
        return self.__company104_Objective

    @company104_Objective.setter
    def company104_Objective(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_Objective__company104_Objective", None)
        self.__company104_Objective = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company104_Goal26"):
                opp_val = getattr(old_value, "company104_Goal26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company104_Goal26"):
                opp_val = getattr(value, "company104_Goal26", None)
                if opp_val is None:
                    setattr(value, "company104_Goal26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Interval:

    pass
class company104_HierarchyLink:

    def __init__(self, hierarchy: str, company104_HierarchyLink: "company104_Employee" = None, company104_HierarchyLink14: "company104_Employee" = None, company104_HierarchyLink17: "company104_Employee" = None):
        self.hierarchy = hierarchy
        self.company104_HierarchyLink = company104_HierarchyLink
        self.company104_HierarchyLink14 = company104_HierarchyLink14
        self.company104_HierarchyLink17 = company104_HierarchyLink17
        
    @property
    def hierarchy(self) -> str:
        return self.__hierarchy

    @hierarchy.setter
    def hierarchy(self, hierarchy: str):
        self.__hierarchy = hierarchy

    @property
    def company104_HierarchyLink14(self):
        return self.__company104_HierarchyLink14

    @company104_HierarchyLink14.setter
    def company104_HierarchyLink14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_HierarchyLink__company104_HierarchyLink14", None)
        self.__company104_HierarchyLink14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company104_Employee15"):
                opp_val = getattr(old_value, "company104_Employee15", None)
                if opp_val == self:
                    setattr(old_value, "company104_Employee15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company104_Employee15"):
                opp_val = getattr(value, "company104_Employee15", None)
                setattr(value, "company104_Employee15", self)

    @property
    def company104_HierarchyLink17(self):
        return self.__company104_HierarchyLink17

    @company104_HierarchyLink17.setter
    def company104_HierarchyLink17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_HierarchyLink__company104_HierarchyLink17", None)
        self.__company104_HierarchyLink17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company104_Employee18"):
                opp_val = getattr(old_value, "company104_Employee18", None)
                if opp_val == self:
                    setattr(old_value, "company104_Employee18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company104_Employee18"):
                opp_val = getattr(value, "company104_Employee18", None)
                setattr(value, "company104_Employee18", self)

    @property
    def company104_HierarchyLink(self):
        return self.__company104_HierarchyLink

    @company104_HierarchyLink.setter
    def company104_HierarchyLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_HierarchyLink__company104_HierarchyLink", None)
        self.__company104_HierarchyLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company104_Employee"):
                opp_val = getattr(old_value, "company104_Employee", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company104_Employee"):
                opp_val = getattr(value, "company104_Employee", None)
                if opp_val is None:
                    setattr(value, "company104_Employee", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class company104_Employee:

    def __init__(self, fullName: str, socialSecurityNumber: str, address: int, company104_Employee: set["company104_HierarchyLink"] = None, company104_Employee10: "company104_Room" = None, owners: "company104_Workstation" = None, company104_Employee15: "company104_HierarchyLink" = None, company104_Employee18: "company104_HierarchyLink" = None, Employee: "company104_Workstation" = None, company104_Employee32: "company104_Agency" = None):
        self.fullName = fullName
        self.socialSecurityNumber = socialSecurityNumber
        self.address = address
        self.company104_Employee = company104_Employee if company104_Employee is not None else set()
        self.company104_Employee10 = company104_Employee10
        self.owners = owners
        self.company104_Employee15 = company104_Employee15
        self.company104_Employee18 = company104_Employee18
        self.Employee = Employee
        self.company104_Employee32 = company104_Employee32
        
    @property
    def address(self) -> int:
        return self.__address

    @address.setter
    def address(self, address: int):
        self.__address = address

    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    @property
    def socialSecurityNumber(self) -> str:
        return self.__socialSecurityNumber

    @socialSecurityNumber.setter
    def socialSecurityNumber(self, socialSecurityNumber: str):
        self.__socialSecurityNumber = socialSecurityNumber

    @property
    def owners(self):
        return self.__owners

    @owners.setter
    def owners(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_Employee__owners", None)
        self.__owners = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Workstation"):
                opp_val = getattr(old_value, "Workstation", None)
                if opp_val == self:
                    setattr(old_value, "Workstation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Workstation"):
                opp_val = getattr(value, "Workstation", None)
                setattr(value, "Workstation", self)

    @property
    def Employee(self):
        return self.__Employee

    @Employee.setter
    def Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_Employee__Employee", None)
        self.__Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inChargeOf"):
                opp_val = getattr(old_value, "inChargeOf", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inChargeOf"):
                opp_val = getattr(value, "inChargeOf", None)
                if opp_val is None:
                    setattr(value, "inChargeOf", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def company104_Employee15(self):
        return self.__company104_Employee15

    @company104_Employee15.setter
    def company104_Employee15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_Employee__company104_Employee15", None)
        self.__company104_Employee15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company104_HierarchyLink14"):
                opp_val = getattr(old_value, "company104_HierarchyLink14", None)
                if opp_val == self:
                    setattr(old_value, "company104_HierarchyLink14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company104_HierarchyLink14"):
                opp_val = getattr(value, "company104_HierarchyLink14", None)
                setattr(value, "company104_HierarchyLink14", self)

    @property
    def company104_Employee(self):
        return self.__company104_Employee

    @company104_Employee.setter
    def company104_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_Employee__company104_Employee", None)
        self.__company104_Employee = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company104_HierarchyLink"):
                    opp_val = getattr(item, "company104_HierarchyLink", None)
                    
                    if opp_val == self:
                        setattr(item, "company104_HierarchyLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company104_HierarchyLink"):
                    opp_val = getattr(item, "company104_HierarchyLink", None)
                    
                    setattr(item, "company104_HierarchyLink", self)
                    

    @property
    def company104_Employee10(self):
        return self.__company104_Employee10

    @company104_Employee10.setter
    def company104_Employee10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_Employee__company104_Employee10", None)
        self.__company104_Employee10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company104_Room11"):
                opp_val = getattr(old_value, "company104_Room11", None)
                if opp_val == self:
                    setattr(old_value, "company104_Room11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company104_Room11"):
                opp_val = getattr(value, "company104_Room11", None)
                setattr(value, "company104_Room11", self)

    @property
    def company104_Employee18(self):
        return self.__company104_Employee18

    @company104_Employee18.setter
    def company104_Employee18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_Employee__company104_Employee18", None)
        self.__company104_Employee18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company104_HierarchyLink17"):
                opp_val = getattr(old_value, "company104_HierarchyLink17", None)
                if opp_val == self:
                    setattr(old_value, "company104_HierarchyLink17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company104_HierarchyLink17"):
                opp_val = getattr(value, "company104_HierarchyLink17", None)
                setattr(value, "company104_HierarchyLink17", self)

    @property
    def company104_Employee32(self):
        return self.__company104_Employee32

    @company104_Employee32.setter
    def company104_Employee32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_Employee__company104_Employee32", None)
        self.__company104_Employee32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company104_Agency31"):
                opp_val = getattr(old_value, "company104_Agency31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company104_Agency31"):
                opp_val = getattr(value, "company104_Agency31", None)
                if opp_val is None:
                    setattr(value, "company104_Agency31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class company104_Workstation(NamedElement):

    def __init__(self, ProfileDescription: str, Workstation: "company104_Employee" = None, company104_Workstation: "company104_Room" = None, inChargeOf: set["company104_Employee"] = None):
        self.ProfileDescription = ProfileDescription
        self.Workstation = Workstation
        self.company104_Workstation = company104_Workstation
        self.inChargeOf = inChargeOf if inChargeOf is not None else set()
        
    @property
    def ProfileDescription(self) -> str:
        return self.__ProfileDescription

    @ProfileDescription.setter
    def ProfileDescription(self, ProfileDescription: str):
        self.__ProfileDescription = ProfileDescription

    @property
    def inChargeOf(self):
        return self.__inChargeOf

    @inChargeOf.setter
    def inChargeOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_Workstation__inChargeOf", None)
        self.__inChargeOf = value if value is not None else set()
        
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
    def Workstation(self):
        return self.__Workstation

    @Workstation.setter
    def Workstation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_Workstation__Workstation", None)
        self.__Workstation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owners"):
                opp_val = getattr(old_value, "owners", None)
                if opp_val == self:
                    setattr(old_value, "owners", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owners"):
                opp_val = getattr(value, "owners", None)
                setattr(value, "owners", self)

    @property
    def company104_Workstation(self):
        return self.__company104_Workstation

    @company104_Workstation.setter
    def company104_Workstation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_Workstation__company104_Workstation", None)
        self.__company104_Workstation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company104_Room23"):
                opp_val = getattr(old_value, "company104_Room23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company104_Room23"):
                opp_val = getattr(value, "company104_Room23", None)
                if opp_val is None:
                    setattr(value, "company104_Room23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class company104_Function(NamedElement):

    pass
class company104_Flow(NamedElement):

    pass
class company104_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Function:

    pass
class company104_Room(Function):

    pass
class company104_Department(Function):

    pass
class company104_Goal(Interval):

    def __init__(self, statement: str, company104_Goal: "company104_Company" = None, company104_Goal26: set["company104_Objective"] = None):
        self.statement = statement
        self.company104_Goal = company104_Goal
        self.company104_Goal26 = company104_Goal26 if company104_Goal26 is not None else set()
        
    @property
    def statement(self) -> str:
        return self.__statement

    @statement.setter
    def statement(self, statement: str):
        self.__statement = statement

    @property
    def company104_Goal26(self):
        return self.__company104_Goal26

    @company104_Goal26.setter
    def company104_Goal26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_Goal__company104_Goal26", None)
        self.__company104_Goal26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company104_Objective"):
                    opp_val = getattr(item, "company104_Objective", None)
                    
                    if opp_val == self:
                        setattr(item, "company104_Objective", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company104_Objective"):
                    opp_val = getattr(item, "company104_Objective", None)
                    
                    setattr(item, "company104_Objective", self)
                    

    @property
    def company104_Goal(self):
        return self.__company104_Goal

    @company104_Goal.setter
    def company104_Goal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_Goal__company104_Goal", None)
        self.__company104_Goal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company104_Company2"):
                opp_val = getattr(old_value, "company104_Company2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company104_Company2"):
                opp_val = getattr(value, "company104_Company2", None)
                if opp_val is None:
                    setattr(value, "company104_Company2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class company104_Agency(Function):

    def __init__(self, Accronym: str, Status: str, company104_Agency: "company104_Company" = None, company104_Agency28: set["company104_Department"] = None, company104_Agency31: set["company104_Employee"] = None, company104_Agency34: set["company104_ObjectiveReach"] = None, company104_Agency40: "company104_ObjectiveReach" = None):
        self.Accronym = Accronym
        self.Status = Status
        self.company104_Agency = company104_Agency
        self.company104_Agency28 = company104_Agency28 if company104_Agency28 is not None else set()
        self.company104_Agency31 = company104_Agency31 if company104_Agency31 is not None else set()
        self.company104_Agency34 = company104_Agency34 if company104_Agency34 is not None else set()
        self.company104_Agency40 = company104_Agency40
        
    @property
    def Status(self) -> str:
        return self.__Status

    @Status.setter
    def Status(self, Status: str):
        self.__Status = Status

    @property
    def Accronym(self) -> str:
        return self.__Accronym

    @Accronym.setter
    def Accronym(self, Accronym: str):
        self.__Accronym = Accronym

    @property
    def company104_Agency31(self):
        return self.__company104_Agency31

    @company104_Agency31.setter
    def company104_Agency31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_Agency__company104_Agency31", None)
        self.__company104_Agency31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company104_Employee32"):
                    opp_val = getattr(item, "company104_Employee32", None)
                    
                    if opp_val == self:
                        setattr(item, "company104_Employee32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company104_Employee32"):
                    opp_val = getattr(item, "company104_Employee32", None)
                    
                    setattr(item, "company104_Employee32", self)
                    

    @property
    def company104_Agency40(self):
        return self.__company104_Agency40

    @company104_Agency40.setter
    def company104_Agency40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_Agency__company104_Agency40", None)
        self.__company104_Agency40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company104_ObjectiveReach39"):
                opp_val = getattr(old_value, "company104_ObjectiveReach39", None)
                if opp_val == self:
                    setattr(old_value, "company104_ObjectiveReach39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company104_ObjectiveReach39"):
                opp_val = getattr(value, "company104_ObjectiveReach39", None)
                setattr(value, "company104_ObjectiveReach39", self)

    @property
    def company104_Agency(self):
        return self.__company104_Agency

    @company104_Agency.setter
    def company104_Agency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_Agency__company104_Agency", None)
        self.__company104_Agency = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company104_Company"):
                opp_val = getattr(old_value, "company104_Company", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company104_Company"):
                opp_val = getattr(value, "company104_Company", None)
                if opp_val is None:
                    setattr(value, "company104_Company", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def company104_Agency34(self):
        return self.__company104_Agency34

    @company104_Agency34.setter
    def company104_Agency34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_Agency__company104_Agency34", None)
        self.__company104_Agency34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company104_ObjectiveReach"):
                    opp_val = getattr(item, "company104_ObjectiveReach", None)
                    
                    if opp_val == self:
                        setattr(item, "company104_ObjectiveReach", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company104_ObjectiveReach"):
                    opp_val = getattr(item, "company104_ObjectiveReach", None)
                    
                    setattr(item, "company104_ObjectiveReach", self)
                    

    @property
    def company104_Agency28(self):
        return self.__company104_Agency28

    @company104_Agency28.setter
    def company104_Agency28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company104_Agency__company104_Agency28", None)
        self.__company104_Agency28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company104_Department29"):
                    opp_val = getattr(item, "company104_Department29", None)
                    
                    if opp_val == self:
                        setattr(item, "company104_Department29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company104_Department29"):
                    opp_val = getattr(item, "company104_Department29", None)
                    
                    setattr(item, "company104_Department29", self)
                    

class company104_Company:

    pass