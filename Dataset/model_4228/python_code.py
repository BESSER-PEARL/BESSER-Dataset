from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ObjectiveNature(Enum):
    None = "None"
    Quality = "Quality"
    Delay = "Delay"
    Cost = "Cost"
    Environmental = "Environmental"
    Legal = "Legal"
    Human = "Human"
    Economical = "Economical"
class ObjectiveType(Enum):
    None = "None"
    Strategic = "Strategic"
    Tactic = "Tactic"
    Operational = "Operational"
class Hierarchy(Enum):
    Supervisor = "Supervisor"
    Subordinate = "Subordinate"
class RoleType(Enum):
    Composite = "Composite"
    Decision = "Decision"
    Transformation = "Transformation"
    Control = "Control"


############################################
# Definition of Classes
############################################

class company106_ObjectiveReach:

    def __init__(self, value: float, statement: str, company106_ObjectiveReach36: "company106_Objective" = None, company106_ObjectiveReach39: "company106_Agency" = None, company106_ObjectiveReach42: "company106_Action" = None, company106_ObjectiveReach: "company106_Agency" = None):
        self.value = value
        self.statement = statement
        self.company106_ObjectiveReach36 = company106_ObjectiveReach36
        self.company106_ObjectiveReach39 = company106_ObjectiveReach39
        self.company106_ObjectiveReach42 = company106_ObjectiveReach42
        self.company106_ObjectiveReach = company106_ObjectiveReach
        
    @property
    def statement(self) -> str:
        return self.__statement

    @statement.setter
    def statement(self, statement: str):
        self.__statement = statement

    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def company106_ObjectiveReach39(self):
        return self.__company106_ObjectiveReach39

    @company106_ObjectiveReach39.setter
    def company106_ObjectiveReach39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_ObjectiveReach__company106_ObjectiveReach39", None)
        self.__company106_ObjectiveReach39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company106_Agency40"):
                opp_val = getattr(old_value, "company106_Agency40", None)
                if opp_val == self:
                    setattr(old_value, "company106_Agency40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company106_Agency40"):
                opp_val = getattr(value, "company106_Agency40", None)
                setattr(value, "company106_Agency40", self)

    @property
    def company106_ObjectiveReach42(self):
        return self.__company106_ObjectiveReach42

    @company106_ObjectiveReach42.setter
    def company106_ObjectiveReach42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_ObjectiveReach__company106_ObjectiveReach42", None)
        self.__company106_ObjectiveReach42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company106_Action"):
                opp_val = getattr(old_value, "company106_Action", None)
                if opp_val == self:
                    setattr(old_value, "company106_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company106_Action"):
                opp_val = getattr(value, "company106_Action", None)
                setattr(value, "company106_Action", self)

    @property
    def company106_ObjectiveReach36(self):
        return self.__company106_ObjectiveReach36

    @company106_ObjectiveReach36.setter
    def company106_ObjectiveReach36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_ObjectiveReach__company106_ObjectiveReach36", None)
        self.__company106_ObjectiveReach36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company106_Objective37"):
                opp_val = getattr(old_value, "company106_Objective37", None)
                if opp_val == self:
                    setattr(old_value, "company106_Objective37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company106_Objective37"):
                opp_val = getattr(value, "company106_Objective37", None)
                setattr(value, "company106_Objective37", self)

    @property
    def company106_ObjectiveReach(self):
        return self.__company106_ObjectiveReach

    @company106_ObjectiveReach.setter
    def company106_ObjectiveReach(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_ObjectiveReach__company106_ObjectiveReach", None)
        self.__company106_ObjectiveReach = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company106_Agency34"):
                opp_val = getattr(old_value, "company106_Agency34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company106_Agency34"):
                opp_val = getattr(value, "company106_Agency34", None)
                if opp_val is None:
                    setattr(value, "company106_Agency34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class company106_Interval(ABC):

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

class company106_Objective:

    def __init__(self, nature: str, type: str, value: float, company106_Objective: "company106_Goal" = None, company106_Objective37: "company106_ObjectiveReach" = None):
        self.nature = nature
        self.type = type
        self.value = value
        self.company106_Objective = company106_Objective
        self.company106_Objective37 = company106_Objective37
        
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
    def company106_Objective(self):
        return self.__company106_Objective

    @company106_Objective.setter
    def company106_Objective(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_Objective__company106_Objective", None)
        self.__company106_Objective = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company106_Goal26"):
                opp_val = getattr(old_value, "company106_Goal26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company106_Goal26"):
                opp_val = getattr(value, "company106_Goal26", None)
                if opp_val is None:
                    setattr(value, "company106_Goal26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def company106_Objective37(self):
        return self.__company106_Objective37

    @company106_Objective37.setter
    def company106_Objective37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_Objective__company106_Objective37", None)
        self.__company106_Objective37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company106_ObjectiveReach36"):
                opp_val = getattr(old_value, "company106_ObjectiveReach36", None)
                if opp_val == self:
                    setattr(old_value, "company106_ObjectiveReach36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company106_ObjectiveReach36"):
                opp_val = getattr(value, "company106_ObjectiveReach36", None)
                setattr(value, "company106_ObjectiveReach36", self)

class Interval:

    pass
class company106_Company:

    pass
class company106_HierarchyLink:

    def __init__(self, hierarchy: str, company106_HierarchyLink: "company106_Employee" = None, company106_HierarchyLink14: "company106_Employee" = None, company106_HierarchyLink17: "company106_Employee" = None):
        self.hierarchy = hierarchy
        self.company106_HierarchyLink = company106_HierarchyLink
        self.company106_HierarchyLink14 = company106_HierarchyLink14
        self.company106_HierarchyLink17 = company106_HierarchyLink17
        
    @property
    def hierarchy(self) -> str:
        return self.__hierarchy

    @hierarchy.setter
    def hierarchy(self, hierarchy: str):
        self.__hierarchy = hierarchy

    @property
    def company106_HierarchyLink17(self):
        return self.__company106_HierarchyLink17

    @company106_HierarchyLink17.setter
    def company106_HierarchyLink17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_HierarchyLink__company106_HierarchyLink17", None)
        self.__company106_HierarchyLink17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company106_Employee18"):
                opp_val = getattr(old_value, "company106_Employee18", None)
                if opp_val == self:
                    setattr(old_value, "company106_Employee18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company106_Employee18"):
                opp_val = getattr(value, "company106_Employee18", None)
                setattr(value, "company106_Employee18", self)

    @property
    def company106_HierarchyLink(self):
        return self.__company106_HierarchyLink

    @company106_HierarchyLink.setter
    def company106_HierarchyLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_HierarchyLink__company106_HierarchyLink", None)
        self.__company106_HierarchyLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company106_Employee"):
                opp_val = getattr(old_value, "company106_Employee", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company106_Employee"):
                opp_val = getattr(value, "company106_Employee", None)
                if opp_val is None:
                    setattr(value, "company106_Employee", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def company106_HierarchyLink14(self):
        return self.__company106_HierarchyLink14

    @company106_HierarchyLink14.setter
    def company106_HierarchyLink14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_HierarchyLink__company106_HierarchyLink14", None)
        self.__company106_HierarchyLink14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company106_Employee15"):
                opp_val = getattr(old_value, "company106_Employee15", None)
                if opp_val == self:
                    setattr(old_value, "company106_Employee15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company106_Employee15"):
                opp_val = getattr(value, "company106_Employee15", None)
                setattr(value, "company106_Employee15", self)

class company106_Employee:

    def __init__(self, fullName: str, socialSecurityNumber: str, address: int, company106_Employee: set["company106_HierarchyLink"] = None, company106_Employee10: "company106_Room" = None, Employee: "company106_Workstation" = None, owners: "company106_Workstation" = None, company106_Employee15: "company106_HierarchyLink" = None, company106_Employee18: "company106_HierarchyLink" = None, company106_Employee32: "company106_Agency" = None):
        self.fullName = fullName
        self.socialSecurityNumber = socialSecurityNumber
        self.address = address
        self.company106_Employee = company106_Employee if company106_Employee is not None else set()
        self.company106_Employee10 = company106_Employee10
        self.Employee = Employee
        self.owners = owners
        self.company106_Employee15 = company106_Employee15
        self.company106_Employee18 = company106_Employee18
        self.company106_Employee32 = company106_Employee32
        
    @property
    def socialSecurityNumber(self) -> str:
        return self.__socialSecurityNumber

    @socialSecurityNumber.setter
    def socialSecurityNumber(self, socialSecurityNumber: str):
        self.__socialSecurityNumber = socialSecurityNumber

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
    def Employee(self):
        return self.__Employee

    @Employee.setter
    def Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_Employee__Employee", None)
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
    def owners(self):
        return self.__owners

    @owners.setter
    def owners(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_Employee__owners", None)
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
    def company106_Employee(self):
        return self.__company106_Employee

    @company106_Employee.setter
    def company106_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_Employee__company106_Employee", None)
        self.__company106_Employee = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company106_HierarchyLink"):
                    opp_val = getattr(item, "company106_HierarchyLink", None)
                    
                    if opp_val == self:
                        setattr(item, "company106_HierarchyLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company106_HierarchyLink"):
                    opp_val = getattr(item, "company106_HierarchyLink", None)
                    
                    setattr(item, "company106_HierarchyLink", self)
                    

    @property
    def company106_Employee15(self):
        return self.__company106_Employee15

    @company106_Employee15.setter
    def company106_Employee15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_Employee__company106_Employee15", None)
        self.__company106_Employee15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company106_HierarchyLink14"):
                opp_val = getattr(old_value, "company106_HierarchyLink14", None)
                if opp_val == self:
                    setattr(old_value, "company106_HierarchyLink14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company106_HierarchyLink14"):
                opp_val = getattr(value, "company106_HierarchyLink14", None)
                setattr(value, "company106_HierarchyLink14", self)

    @property
    def company106_Employee18(self):
        return self.__company106_Employee18

    @company106_Employee18.setter
    def company106_Employee18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_Employee__company106_Employee18", None)
        self.__company106_Employee18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company106_HierarchyLink17"):
                opp_val = getattr(old_value, "company106_HierarchyLink17", None)
                if opp_val == self:
                    setattr(old_value, "company106_HierarchyLink17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company106_HierarchyLink17"):
                opp_val = getattr(value, "company106_HierarchyLink17", None)
                setattr(value, "company106_HierarchyLink17", self)

    @property
    def company106_Employee10(self):
        return self.__company106_Employee10

    @company106_Employee10.setter
    def company106_Employee10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_Employee__company106_Employee10", None)
        self.__company106_Employee10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company106_Room11"):
                opp_val = getattr(old_value, "company106_Room11", None)
                if opp_val == self:
                    setattr(old_value, "company106_Room11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company106_Room11"):
                opp_val = getattr(value, "company106_Room11", None)
                setattr(value, "company106_Room11", self)

    @property
    def company106_Employee32(self):
        return self.__company106_Employee32

    @company106_Employee32.setter
    def company106_Employee32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_Employee__company106_Employee32", None)
        self.__company106_Employee32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company106_Agency31"):
                opp_val = getattr(old_value, "company106_Agency31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company106_Agency31"):
                opp_val = getattr(value, "company106_Agency31", None)
                if opp_val is None:
                    setattr(value, "company106_Agency31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class company106_Action(NamedElement):

    def __init__(self, statement: str, company106_Action: "company106_ObjectiveReach" = None, company106_Action47: "company106_Flow" = None):
        self.statement = statement
        self.company106_Action = company106_Action
        self.company106_Action47 = company106_Action47
        
    @property
    def statement(self) -> str:
        return self.__statement

    @statement.setter
    def statement(self, statement: str):
        self.__statement = statement

    @property
    def company106_Action(self):
        return self.__company106_Action

    @company106_Action.setter
    def company106_Action(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_Action__company106_Action", None)
        self.__company106_Action = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company106_ObjectiveReach42"):
                opp_val = getattr(old_value, "company106_ObjectiveReach42", None)
                if opp_val == self:
                    setattr(old_value, "company106_ObjectiveReach42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company106_ObjectiveReach42"):
                opp_val = getattr(value, "company106_ObjectiveReach42", None)
                setattr(value, "company106_ObjectiveReach42", self)

    @property
    def company106_Action47(self):
        return self.__company106_Action47

    @company106_Action47.setter
    def company106_Action47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_Action__company106_Action47", None)
        self.__company106_Action47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company106_Flow48"):
                opp_val = getattr(old_value, "company106_Flow48", None)
                if opp_val == self:
                    setattr(old_value, "company106_Flow48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company106_Flow48"):
                opp_val = getattr(value, "company106_Flow48", None)
                setattr(value, "company106_Flow48", self)

class company106_Function(NamedElement):

    pass
class company106_Workstation(NamedElement):

    def __init__(self, profileDescription: str, company106_Workstation: "company106_Room" = None, inChargeOf: set["company106_Employee"] = None, Workstation: "company106_Employee" = None):
        self.profileDescription = profileDescription
        self.company106_Workstation = company106_Workstation
        self.inChargeOf = inChargeOf if inChargeOf is not None else set()
        self.Workstation = Workstation
        
    @property
    def profileDescription(self) -> str:
        return self.__profileDescription

    @profileDescription.setter
    def profileDescription(self, profileDescription: str):
        self.__profileDescription = profileDescription

    @property
    def company106_Workstation(self):
        return self.__company106_Workstation

    @company106_Workstation.setter
    def company106_Workstation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_Workstation__company106_Workstation", None)
        self.__company106_Workstation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company106_Room23"):
                opp_val = getattr(old_value, "company106_Room23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company106_Room23"):
                opp_val = getattr(value, "company106_Room23", None)
                if opp_val is None:
                    setattr(value, "company106_Room23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def inChargeOf(self):
        return self.__inChargeOf

    @inChargeOf.setter
    def inChargeOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_Workstation__inChargeOf", None)
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
        old_value = getattr(self, f"_company106_Workstation__Workstation", None)
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

class company106_Flow(NamedElement):

    pass
class company106_NamedElement(ABC):

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
class company106_Room(Function):

    pass
class company106_Agency(Function):

    def __init__(self, acronym: str, status: str, company106_Agency: "company106_Company" = None, company106_Agency40: "company106_ObjectiveReach" = None, company106_Agency28: set["company106_Department"] = None, company106_Agency31: set["company106_Employee"] = None, company106_Agency34: set["company106_ObjectiveReach"] = None):
        self.acronym = acronym
        self.status = status
        self.company106_Agency = company106_Agency
        self.company106_Agency40 = company106_Agency40
        self.company106_Agency28 = company106_Agency28 if company106_Agency28 is not None else set()
        self.company106_Agency31 = company106_Agency31 if company106_Agency31 is not None else set()
        self.company106_Agency34 = company106_Agency34 if company106_Agency34 is not None else set()
        
    @property
    def acronym(self) -> str:
        return self.__acronym

    @acronym.setter
    def acronym(self, acronym: str):
        self.__acronym = acronym

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def company106_Agency28(self):
        return self.__company106_Agency28

    @company106_Agency28.setter
    def company106_Agency28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_Agency__company106_Agency28", None)
        self.__company106_Agency28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company106_Department29"):
                    opp_val = getattr(item, "company106_Department29", None)
                    
                    if opp_val == self:
                        setattr(item, "company106_Department29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company106_Department29"):
                    opp_val = getattr(item, "company106_Department29", None)
                    
                    setattr(item, "company106_Department29", self)
                    

    @property
    def company106_Agency31(self):
        return self.__company106_Agency31

    @company106_Agency31.setter
    def company106_Agency31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_Agency__company106_Agency31", None)
        self.__company106_Agency31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company106_Employee32"):
                    opp_val = getattr(item, "company106_Employee32", None)
                    
                    if opp_val == self:
                        setattr(item, "company106_Employee32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company106_Employee32"):
                    opp_val = getattr(item, "company106_Employee32", None)
                    
                    setattr(item, "company106_Employee32", self)
                    

    @property
    def company106_Agency40(self):
        return self.__company106_Agency40

    @company106_Agency40.setter
    def company106_Agency40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_Agency__company106_Agency40", None)
        self.__company106_Agency40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company106_ObjectiveReach39"):
                opp_val = getattr(old_value, "company106_ObjectiveReach39", None)
                if opp_val == self:
                    setattr(old_value, "company106_ObjectiveReach39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company106_ObjectiveReach39"):
                opp_val = getattr(value, "company106_ObjectiveReach39", None)
                setattr(value, "company106_ObjectiveReach39", self)

    @property
    def company106_Agency34(self):
        return self.__company106_Agency34

    @company106_Agency34.setter
    def company106_Agency34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_Agency__company106_Agency34", None)
        self.__company106_Agency34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company106_ObjectiveReach"):
                    opp_val = getattr(item, "company106_ObjectiveReach", None)
                    
                    if opp_val == self:
                        setattr(item, "company106_ObjectiveReach", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company106_ObjectiveReach"):
                    opp_val = getattr(item, "company106_ObjectiveReach", None)
                    
                    setattr(item, "company106_ObjectiveReach", self)
                    

    @property
    def company106_Agency(self):
        return self.__company106_Agency

    @company106_Agency.setter
    def company106_Agency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_Agency__company106_Agency", None)
        self.__company106_Agency = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company106_Company"):
                opp_val = getattr(old_value, "company106_Company", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company106_Company"):
                opp_val = getattr(value, "company106_Company", None)
                if opp_val is None:
                    setattr(value, "company106_Company", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class company106_Department(Function):

    pass
class company106_Goal(Interval):

    def __init__(self, statement: str, company106_Goal: "company106_Company" = None, company106_Goal26: set["company106_Objective"] = None):
        self.statement = statement
        self.company106_Goal = company106_Goal
        self.company106_Goal26 = company106_Goal26 if company106_Goal26 is not None else set()
        
    @property
    def statement(self) -> str:
        return self.__statement

    @statement.setter
    def statement(self, statement: str):
        self.__statement = statement

    @property
    def company106_Goal26(self):
        return self.__company106_Goal26

    @company106_Goal26.setter
    def company106_Goal26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_Goal__company106_Goal26", None)
        self.__company106_Goal26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company106_Objective"):
                    opp_val = getattr(item, "company106_Objective", None)
                    
                    if opp_val == self:
                        setattr(item, "company106_Objective", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company106_Objective"):
                    opp_val = getattr(item, "company106_Objective", None)
                    
                    setattr(item, "company106_Objective", self)
                    

    @property
    def company106_Goal(self):
        return self.__company106_Goal

    @company106_Goal.setter
    def company106_Goal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company106_Goal__company106_Goal", None)
        self.__company106_Goal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company106_Company2"):
                opp_val = getattr(old_value, "company106_Company2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company106_Company2"):
                opp_val = getattr(value, "company106_Company2", None)
                if opp_val is None:
                    setattr(value, "company106_Company2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
