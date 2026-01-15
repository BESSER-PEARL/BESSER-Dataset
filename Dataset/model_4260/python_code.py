from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class StructureType(Enum):
    team = "team"
    service = "service"
    department = "department"
    businessUnit = "businessUnit"
    division = "division"


############################################
# Definition of Classes
############################################

class organizationchart_Organization:

    def __init__(self, name: str, organizationchart_Organization: set["organizationchart_Employee"] = None, organizationchart_Organization14: set["organizationchart_OrganizationalStructure"] = None, organizationchart_Organization16: set["organizationchart_Location"] = None):
        self.name = name
        self.organizationchart_Organization = organizationchart_Organization if organizationchart_Organization is not None else set()
        self.organizationchart_Organization14 = organizationchart_Organization14 if organizationchart_Organization14 is not None else set()
        self.organizationchart_Organization16 = organizationchart_Organization16 if organizationchart_Organization16 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def organizationchart_Organization(self):
        return self.__organizationchart_Organization

    @organizationchart_Organization.setter
    def organizationchart_Organization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_Organization__organizationchart_Organization", None)
        self.__organizationchart_Organization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "organizationchart_Employee"):
                    opp_val = getattr(item, "organizationchart_Employee", None)
                    
                    if opp_val == self:
                        setattr(item, "organizationchart_Employee", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "organizationchart_Employee"):
                    opp_val = getattr(item, "organizationchart_Employee", None)
                    
                    setattr(item, "organizationchart_Employee", self)
                    

    @property
    def organizationchart_Organization16(self):
        return self.__organizationchart_Organization16

    @organizationchart_Organization16.setter
    def organizationchart_Organization16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_Organization__organizationchart_Organization16", None)
        self.__organizationchart_Organization16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "organizationchart_Location"):
                    opp_val = getattr(item, "organizationchart_Location", None)
                    
                    if opp_val == self:
                        setattr(item, "organizationchart_Location", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "organizationchart_Location"):
                    opp_val = getattr(item, "organizationchart_Location", None)
                    
                    setattr(item, "organizationchart_Location", self)
                    

    @property
    def organizationchart_Organization14(self):
        return self.__organizationchart_Organization14

    @organizationchart_Organization14.setter
    def organizationchart_Organization14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_Organization__organizationchart_Organization14", None)
        self.__organizationchart_Organization14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "organizationchart_OrganizationalStructure"):
                    opp_val = getattr(item, "organizationchart_OrganizationalStructure", None)
                    
                    if opp_val == self:
                        setattr(item, "organizationchart_OrganizationalStructure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "organizationchart_OrganizationalStructure"):
                    opp_val = getattr(item, "organizationchart_OrganizationalStructure", None)
                    
                    setattr(item, "organizationchart_OrganizationalStructure", self)
                    

class organizationchart_Function:

    def __init__(self, name: str, organizationchart_Function: "organizationchart_OrganizationalStructure" = None, Function: "organizationchart_Employee" = None, performs: set["organizationchart_Employee"] = None):
        self.name = name
        self.organizationchart_Function = organizationchart_Function
        self.Function = Function
        self.performs = performs if performs is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Function(self):
        return self.__Function

    @Function.setter
    def Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_Function__Function", None)
        self.__Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "isPerformedBy"):
                opp_val = getattr(old_value, "isPerformedBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "isPerformedBy"):
                opp_val = getattr(value, "isPerformedBy", None)
                if opp_val is None:
                    setattr(value, "isPerformedBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def performs(self):
        return self.__performs

    @performs.setter
    def performs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_Function__performs", None)
        self.__performs = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee29"):
                    opp_val = getattr(item, "Employee29", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee29"):
                    opp_val = getattr(item, "Employee29", None)
                    
                    setattr(item, "Employee29", self)
                    

    @property
    def organizationchart_Function(self):
        return self.__organizationchart_Function

    @organizationchart_Function.setter
    def organizationchart_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_Function__organizationchart_Function", None)
        self.__organizationchart_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "organizationchart_OrganizationalStructure23"):
                opp_val = getattr(old_value, "organizationchart_OrganizationalStructure23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "organizationchart_OrganizationalStructure23"):
                opp_val = getattr(value, "organizationchart_OrganizationalStructure23", None)
                if opp_val is None:
                    setattr(value, "organizationchart_OrganizationalStructure23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class organizationchart_Location:

    def __init__(self, name: str, location: set["organizationchart_Employee"] = None, Location: "organizationchart_Employee" = None, organizationchart_Location: "organizationchart_Organization" = None):
        self.name = name
        self.location = location if location is not None else set()
        self.Location = Location
        self.organizationchart_Location = organizationchart_Location
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def organizationchart_Location(self):
        return self.__organizationchart_Location

    @organizationchart_Location.setter
    def organizationchart_Location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_Location__organizationchart_Location", None)
        self.__organizationchart_Location = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "organizationchart_Organization16"):
                opp_val = getattr(old_value, "organizationchart_Organization16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "organizationchart_Organization16"):
                opp_val = getattr(value, "organizationchart_Organization16", None)
                if opp_val is None:
                    setattr(value, "organizationchart_Organization16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Location(self):
        return self.__Location

    @Location.setter
    def Location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_Location__Location", None)
        self.__Location = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employees4"):
                opp_val = getattr(old_value, "employees4", None)
                if opp_val == self:
                    setattr(old_value, "employees4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employees4"):
                opp_val = getattr(value, "employees4", None)
                setattr(value, "employees4", self)

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_Location__location", None)
        self.__location = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee27"):
                    opp_val = getattr(item, "Employee27", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee27"):
                    opp_val = getattr(item, "Employee27", None)
                    
                    setattr(item, "Employee27", self)
                    

class organizationchart_OrganizationalStructure:

    def __init__(self, name: str, type: str, organizationchart_OrganizationalStructure19: set["organizationchart_OrganizationalStructure"] = None, organizationchart_OrganizationalStructure23: set["organizationchart_Function"] = None, leads: "organizationchart_Employee" = None, OrganizationalStructure: "organizationchart_Employee" = None, OrganizationalStructure11: "organizationchart_Employee" = None, organizationchart_OrganizationalStructure: "organizationchart_Organization" = None, belongsTo: set["organizationchart_Employee"] = None, organizationchart_OrganizationalStructure21: "organizationchart_OrganizationalStructure" = None):
        self.name = name
        self.type = type
        self.organizationchart_OrganizationalStructure19 = organizationchart_OrganizationalStructure19 if organizationchart_OrganizationalStructure19 is not None else set()
        self.organizationchart_OrganizationalStructure23 = organizationchart_OrganizationalStructure23 if organizationchart_OrganizationalStructure23 is not None else set()
        self.leads = leads
        self.OrganizationalStructure = OrganizationalStructure
        self.OrganizationalStructure11 = OrganizationalStructure11
        self.organizationchart_OrganizationalStructure = organizationchart_OrganizationalStructure
        self.belongsTo = belongsTo if belongsTo is not None else set()
        self.organizationchart_OrganizationalStructure21 = organizationchart_OrganizationalStructure21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def OrganizationalStructure(self):
        return self.__OrganizationalStructure

    @OrganizationalStructure.setter
    def OrganizationalStructure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_OrganizationalStructure__OrganizationalStructure", None)
        self.__OrganizationalStructure = value
        
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
    def leads(self):
        return self.__leads

    @leads.setter
    def leads(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_OrganizationalStructure__leads", None)
        self.__leads = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee25"):
                opp_val = getattr(old_value, "Employee25", None)
                if opp_val == self:
                    setattr(old_value, "Employee25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee25"):
                opp_val = getattr(value, "Employee25", None)
                setattr(value, "Employee25", self)

    @property
    def belongsTo(self):
        return self.__belongsTo

    @belongsTo.setter
    def belongsTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_OrganizationalStructure__belongsTo", None)
        self.__belongsTo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee18"):
                    opp_val = getattr(item, "Employee18", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee18"):
                    opp_val = getattr(item, "Employee18", None)
                    
                    setattr(item, "Employee18", self)
                    

    @property
    def OrganizationalStructure11(self):
        return self.__OrganizationalStructure11

    @OrganizationalStructure11.setter
    def OrganizationalStructure11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_OrganizationalStructure__OrganizationalStructure11", None)
        self.__OrganizationalStructure11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manager10"):
                opp_val = getattr(old_value, "manager10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manager10"):
                opp_val = getattr(value, "manager10", None)
                if opp_val is None:
                    setattr(value, "manager10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def organizationchart_OrganizationalStructure19(self):
        return self.__organizationchart_OrganizationalStructure19

    @organizationchart_OrganizationalStructure19.setter
    def organizationchart_OrganizationalStructure19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_OrganizationalStructure__organizationchart_OrganizationalStructure19", None)
        self.__organizationchart_OrganizationalStructure19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "organizationchart_OrganizationalStructure21"):
                    opp_val = getattr(item, "organizationchart_OrganizationalStructure21", None)
                    
                    if opp_val == self:
                        setattr(item, "organizationchart_OrganizationalStructure21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "organizationchart_OrganizationalStructure21"):
                    opp_val = getattr(item, "organizationchart_OrganizationalStructure21", None)
                    
                    setattr(item, "organizationchart_OrganizationalStructure21", self)
                    

    @property
    def organizationchart_OrganizationalStructure23(self):
        return self.__organizationchart_OrganizationalStructure23

    @organizationchart_OrganizationalStructure23.setter
    def organizationchart_OrganizationalStructure23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_OrganizationalStructure__organizationchart_OrganizationalStructure23", None)
        self.__organizationchart_OrganizationalStructure23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "organizationchart_Function"):
                    opp_val = getattr(item, "organizationchart_Function", None)
                    
                    if opp_val == self:
                        setattr(item, "organizationchart_Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "organizationchart_Function"):
                    opp_val = getattr(item, "organizationchart_Function", None)
                    
                    setattr(item, "organizationchart_Function", self)
                    

    @property
    def organizationchart_OrganizationalStructure(self):
        return self.__organizationchart_OrganizationalStructure

    @organizationchart_OrganizationalStructure.setter
    def organizationchart_OrganizationalStructure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_OrganizationalStructure__organizationchart_OrganizationalStructure", None)
        self.__organizationchart_OrganizationalStructure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "organizationchart_Organization14"):
                opp_val = getattr(old_value, "organizationchart_Organization14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "organizationchart_Organization14"):
                opp_val = getattr(value, "organizationchart_Organization14", None)
                if opp_val is None:
                    setattr(value, "organizationchart_Organization14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def organizationchart_OrganizationalStructure21(self):
        return self.__organizationchart_OrganizationalStructure21

    @organizationchart_OrganizationalStructure21.setter
    def organizationchart_OrganizationalStructure21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_OrganizationalStructure__organizationchart_OrganizationalStructure21", None)
        self.__organizationchart_OrganizationalStructure21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "organizationchart_OrganizationalStructure19"):
                opp_val = getattr(old_value, "organizationchart_OrganizationalStructure19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "organizationchart_OrganizationalStructure19"):
                opp_val = getattr(value, "organizationchart_OrganizationalStructure19", None)
                if opp_val is None:
                    setattr(value, "organizationchart_OrganizationalStructure19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class organizationchart_Employee:

    def __init__(self, firstname: str, lastname: str, title: str, trigraph: str, Employee25: "organizationchart_OrganizationalStructure" = None, Employee27: "organizationchart_Location" = None, Employee: "organizationchart_Employee" = None, manager: set["organizationchart_Employee"] = None, employees: "organizationchart_OrganizationalStructure" = None, employees4: "organizationchart_Location" = None, Employee7: "organizationchart_Employee" = None, manages: "organizationchart_Employee" = None, isPerformedBy: set["organizationchart_Function"] = None, manager10: set["organizationchart_OrganizationalStructure"] = None, organizationchart_Employee: "organizationchart_Organization" = None, Employee18: "organizationchart_OrganizationalStructure" = None, Employee29: "organizationchart_Function" = None):
        self.firstname = firstname
        self.lastname = lastname
        self.title = title
        self.trigraph = trigraph
        self.Employee25 = Employee25
        self.Employee27 = Employee27
        self.Employee = Employee
        self.manager = manager if manager is not None else set()
        self.employees = employees
        self.employees4 = employees4
        self.Employee7 = Employee7
        self.manages = manages
        self.isPerformedBy = isPerformedBy if isPerformedBy is not None else set()
        self.manager10 = manager10 if manager10 is not None else set()
        self.organizationchart_Employee = organizationchart_Employee
        self.Employee18 = Employee18
        self.Employee29 = Employee29
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def trigraph(self) -> str:
        return self.__trigraph

    @trigraph.setter
    def trigraph(self, trigraph: str):
        self.__trigraph = trigraph

    @property
    def Employee(self):
        return self.__Employee

    @Employee.setter
    def Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_Employee__Employee", None)
        self.__Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manager"):
                opp_val = getattr(old_value, "manager", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manager"):
                opp_val = getattr(value, "manager", None)
                if opp_val is None:
                    setattr(value, "manager", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def employees4(self):
        return self.__employees4

    @employees4.setter
    def employees4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_Employee__employees4", None)
        self.__employees4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Location"):
                opp_val = getattr(old_value, "Location", None)
                if opp_val == self:
                    setattr(old_value, "Location", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Location"):
                opp_val = getattr(value, "Location", None)
                setattr(value, "Location", self)

    @property
    def isPerformedBy(self):
        return self.__isPerformedBy

    @isPerformedBy.setter
    def isPerformedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_Employee__isPerformedBy", None)
        self.__isPerformedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Function"):
                    opp_val = getattr(item, "Function", None)
                    
                    if opp_val == self:
                        setattr(item, "Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Function"):
                    opp_val = getattr(item, "Function", None)
                    
                    setattr(item, "Function", self)
                    

    @property
    def manages(self):
        return self.__manages

    @manages.setter
    def manages(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_Employee__manages", None)
        self.__manages = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee7"):
                opp_val = getattr(old_value, "Employee7", None)
                if opp_val == self:
                    setattr(old_value, "Employee7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee7"):
                opp_val = getattr(value, "Employee7", None)
                setattr(value, "Employee7", self)

    @property
    def Employee25(self):
        return self.__Employee25

    @Employee25.setter
    def Employee25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_Employee__Employee25", None)
        self.__Employee25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "leads"):
                opp_val = getattr(old_value, "leads", None)
                if opp_val == self:
                    setattr(old_value, "leads", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "leads"):
                opp_val = getattr(value, "leads", None)
                setattr(value, "leads", self)

    @property
    def Employee7(self):
        return self.__Employee7

    @Employee7.setter
    def Employee7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_Employee__Employee7", None)
        self.__Employee7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manages"):
                opp_val = getattr(old_value, "manages", None)
                if opp_val == self:
                    setattr(old_value, "manages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manages"):
                opp_val = getattr(value, "manages", None)
                setattr(value, "manages", self)

    @property
    def Employee18(self):
        return self.__Employee18

    @Employee18.setter
    def Employee18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_Employee__Employee18", None)
        self.__Employee18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "belongsTo"):
                opp_val = getattr(old_value, "belongsTo", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "belongsTo"):
                opp_val = getattr(value, "belongsTo", None)
                if opp_val is None:
                    setattr(value, "belongsTo", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Employee27(self):
        return self.__Employee27

    @Employee27.setter
    def Employee27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_Employee__Employee27", None)
        self.__Employee27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "location"):
                opp_val = getattr(old_value, "location", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "location"):
                opp_val = getattr(value, "location", None)
                if opp_val is None:
                    setattr(value, "location", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Employee29(self):
        return self.__Employee29

    @Employee29.setter
    def Employee29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_Employee__Employee29", None)
        self.__Employee29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "performs"):
                opp_val = getattr(old_value, "performs", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "performs"):
                opp_val = getattr(value, "performs", None)
                if opp_val is None:
                    setattr(value, "performs", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def organizationchart_Employee(self):
        return self.__organizationchart_Employee

    @organizationchart_Employee.setter
    def organizationchart_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_Employee__organizationchart_Employee", None)
        self.__organizationchart_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "organizationchart_Organization"):
                opp_val = getattr(old_value, "organizationchart_Organization", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "organizationchart_Organization"):
                opp_val = getattr(value, "organizationchart_Organization", None)
                if opp_val is None:
                    setattr(value, "organizationchart_Organization", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_Employee__manager", None)
        self.__manager = value if value is not None else set()
        
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
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_Employee__employees", None)
        self.__employees = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OrganizationalStructure"):
                opp_val = getattr(old_value, "OrganizationalStructure", None)
                if opp_val == self:
                    setattr(old_value, "OrganizationalStructure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OrganizationalStructure"):
                opp_val = getattr(value, "OrganizationalStructure", None)
                setattr(value, "OrganizationalStructure", self)

    @property
    def manager10(self):
        return self.__manager10

    @manager10.setter
    def manager10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_organizationchart_Employee__manager10", None)
        self.__manager10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OrganizationalStructure11"):
                    opp_val = getattr(item, "OrganizationalStructure11", None)
                    
                    if opp_val == self:
                        setattr(item, "OrganizationalStructure11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OrganizationalStructure11"):
                    opp_val = getattr(item, "OrganizationalStructure11", None)
                    
                    setattr(item, "OrganizationalStructure11", self)
                    
