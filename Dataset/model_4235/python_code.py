from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class taskType(Enum):
    development = "development"
    documentation = "documentation"


############################################
# Definition of Classes
############################################

class projectDsl_Task:

    def __init__(self, name: str, type: str, projectDsl_Task: "projectDsl_Project" = None):
        self.name = name
        self.type = type
        self.projectDsl_Task = projectDsl_Task
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def projectDsl_Task(self):
        return self.__projectDsl_Task

    @projectDsl_Task.setter
    def projectDsl_Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_projectDsl_Task__projectDsl_Task", None)
        self.__projectDsl_Task = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projectDsl_Project6"):
                opp_val = getattr(old_value, "projectDsl_Project6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projectDsl_Project6"):
                opp_val = getattr(value, "projectDsl_Project6", None)
                if opp_val is None:
                    setattr(value, "projectDsl_Project6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class projectDsl_Employee:

    def __init__(self, name: str, weight: int, height: int, projectDsl_Employee: "projectDsl_Employees" = None):
        self.name = name
        self.weight = weight
        self.height = height
        self.projectDsl_Employee = projectDsl_Employee
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def projectDsl_Employee(self):
        return self.__projectDsl_Employee

    @projectDsl_Employee.setter
    def projectDsl_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_projectDsl_Employee__projectDsl_Employee", None)
        self.__projectDsl_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projectDsl_Employees4"):
                opp_val = getattr(old_value, "projectDsl_Employees4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projectDsl_Employees4"):
                opp_val = getattr(value, "projectDsl_Employees4", None)
                if opp_val is None:
                    setattr(value, "projectDsl_Employees4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class projectDsl_Project:

    def __init__(self, name: str, type: str, projectDsl_Project: "projectDsl_Company" = None, projectDsl_Project6: set["projectDsl_Task"] = None):
        self.name = name
        self.type = type
        self.projectDsl_Project = projectDsl_Project
        self.projectDsl_Project6 = projectDsl_Project6 if projectDsl_Project6 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def projectDsl_Project(self):
        return self.__projectDsl_Project

    @projectDsl_Project.setter
    def projectDsl_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_projectDsl_Project__projectDsl_Project", None)
        self.__projectDsl_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projectDsl_Company2"):
                opp_val = getattr(old_value, "projectDsl_Company2", None)
                if opp_val == self:
                    setattr(old_value, "projectDsl_Company2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projectDsl_Company2"):
                opp_val = getattr(value, "projectDsl_Company2", None)
                setattr(value, "projectDsl_Company2", self)

    @property
    def projectDsl_Project6(self):
        return self.__projectDsl_Project6

    @projectDsl_Project6.setter
    def projectDsl_Project6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_projectDsl_Project__projectDsl_Project6", None)
        self.__projectDsl_Project6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "projectDsl_Task"):
                    opp_val = getattr(item, "projectDsl_Task", None)
                    
                    if opp_val == self:
                        setattr(item, "projectDsl_Task", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "projectDsl_Task"):
                    opp_val = getattr(item, "projectDsl_Task", None)
                    
                    setattr(item, "projectDsl_Task", self)
                    

class projectDsl_Employees:

    pass
class projectDsl_Company:

    def __init__(self, name: str, projectDsl_Company: "projectDsl_Employees" = None, projectDsl_Company2: "projectDsl_Project" = None):
        self.name = name
        self.projectDsl_Company = projectDsl_Company
        self.projectDsl_Company2 = projectDsl_Company2
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def projectDsl_Company(self):
        return self.__projectDsl_Company

    @projectDsl_Company.setter
    def projectDsl_Company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_projectDsl_Company__projectDsl_Company", None)
        self.__projectDsl_Company = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projectDsl_Employees"):
                opp_val = getattr(old_value, "projectDsl_Employees", None)
                if opp_val == self:
                    setattr(old_value, "projectDsl_Employees", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projectDsl_Employees"):
                opp_val = getattr(value, "projectDsl_Employees", None)
                setattr(value, "projectDsl_Employees", self)

    @property
    def projectDsl_Company2(self):
        return self.__projectDsl_Company2

    @projectDsl_Company2.setter
    def projectDsl_Company2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_projectDsl_Company__projectDsl_Company2", None)
        self.__projectDsl_Company2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projectDsl_Project"):
                opp_val = getattr(old_value, "projectDsl_Project", None)
                if opp_val == self:
                    setattr(old_value, "projectDsl_Project", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projectDsl_Project"):
                opp_val = getattr(value, "projectDsl_Project", None)
                setattr(value, "projectDsl_Project", self)
