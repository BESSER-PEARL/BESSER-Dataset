from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ProjectType(Enum):
    Development = "Development"
    Regie = "Regie"


############################################
# Definition of Classes
############################################

class chartDsl_Task:

    def __init__(self, name: str, chartDsl_Task: "chartDsl_Project" = None, chartDsl_Task6: "chartDsl_Employee" = None):
        self.name = name
        self.chartDsl_Task = chartDsl_Task
        self.chartDsl_Task6 = chartDsl_Task6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def chartDsl_Task(self):
        return self.__chartDsl_Task

    @chartDsl_Task.setter
    def chartDsl_Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_chartDsl_Task__chartDsl_Task", None)
        self.__chartDsl_Task = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "chartDsl_Project4"):
                opp_val = getattr(old_value, "chartDsl_Project4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "chartDsl_Project4"):
                opp_val = getattr(value, "chartDsl_Project4", None)
                if opp_val is None:
                    setattr(value, "chartDsl_Project4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def chartDsl_Task6(self):
        return self.__chartDsl_Task6

    @chartDsl_Task6.setter
    def chartDsl_Task6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_chartDsl_Task__chartDsl_Task6", None)
        self.__chartDsl_Task6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "chartDsl_Employee7"):
                opp_val = getattr(old_value, "chartDsl_Employee7", None)
                if opp_val == self:
                    setattr(old_value, "chartDsl_Employee7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "chartDsl_Employee7"):
                opp_val = getattr(value, "chartDsl_Employee7", None)
                setattr(value, "chartDsl_Employee7", self)

class chartDsl_Project:

    def __init__(self, name: str, projectType: str, chartDsl_Project: "chartDsl_Company" = None, chartDsl_Project4: set["chartDsl_Task"] = None):
        self.name = name
        self.projectType = projectType
        self.chartDsl_Project = chartDsl_Project
        self.chartDsl_Project4 = chartDsl_Project4 if chartDsl_Project4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def projectType(self) -> str:
        return self.__projectType

    @projectType.setter
    def projectType(self, projectType: str):
        self.__projectType = projectType

    @property
    def chartDsl_Project4(self):
        return self.__chartDsl_Project4

    @chartDsl_Project4.setter
    def chartDsl_Project4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_chartDsl_Project__chartDsl_Project4", None)
        self.__chartDsl_Project4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "chartDsl_Task"):
                    opp_val = getattr(item, "chartDsl_Task", None)
                    
                    if opp_val == self:
                        setattr(item, "chartDsl_Task", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "chartDsl_Task"):
                    opp_val = getattr(item, "chartDsl_Task", None)
                    
                    setattr(item, "chartDsl_Task", self)
                    

    @property
    def chartDsl_Project(self):
        return self.__chartDsl_Project

    @chartDsl_Project.setter
    def chartDsl_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_chartDsl_Project__chartDsl_Project", None)
        self.__chartDsl_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "chartDsl_Company2"):
                opp_val = getattr(old_value, "chartDsl_Company2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "chartDsl_Company2"):
                opp_val = getattr(value, "chartDsl_Company2", None)
                if opp_val is None:
                    setattr(value, "chartDsl_Company2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class chartDsl_Employee:

    def __init__(self, name: str, chartDsl_Employee: "chartDsl_Company" = None, chartDsl_Employee7: "chartDsl_Task" = None):
        self.name = name
        self.chartDsl_Employee = chartDsl_Employee
        self.chartDsl_Employee7 = chartDsl_Employee7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def chartDsl_Employee(self):
        return self.__chartDsl_Employee

    @chartDsl_Employee.setter
    def chartDsl_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_chartDsl_Employee__chartDsl_Employee", None)
        self.__chartDsl_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "chartDsl_Company"):
                opp_val = getattr(old_value, "chartDsl_Company", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "chartDsl_Company"):
                opp_val = getattr(value, "chartDsl_Company", None)
                if opp_val is None:
                    setattr(value, "chartDsl_Company", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def chartDsl_Employee7(self):
        return self.__chartDsl_Employee7

    @chartDsl_Employee7.setter
    def chartDsl_Employee7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_chartDsl_Employee__chartDsl_Employee7", None)
        self.__chartDsl_Employee7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "chartDsl_Task6"):
                opp_val = getattr(old_value, "chartDsl_Task6", None)
                if opp_val == self:
                    setattr(old_value, "chartDsl_Task6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "chartDsl_Task6"):
                opp_val = getattr(value, "chartDsl_Task6", None)
                setattr(value, "chartDsl_Task6", self)

class chartDsl_Company:

    def __init__(self, name: str, chartDsl_Company: set["chartDsl_Employee"] = None, chartDsl_Company2: set["chartDsl_Project"] = None):
        self.name = name
        self.chartDsl_Company = chartDsl_Company if chartDsl_Company is not None else set()
        self.chartDsl_Company2 = chartDsl_Company2 if chartDsl_Company2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def chartDsl_Company(self):
        return self.__chartDsl_Company

    @chartDsl_Company.setter
    def chartDsl_Company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_chartDsl_Company__chartDsl_Company", None)
        self.__chartDsl_Company = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "chartDsl_Employee"):
                    opp_val = getattr(item, "chartDsl_Employee", None)
                    
                    if opp_val == self:
                        setattr(item, "chartDsl_Employee", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "chartDsl_Employee"):
                    opp_val = getattr(item, "chartDsl_Employee", None)
                    
                    setattr(item, "chartDsl_Employee", self)
                    

    @property
    def chartDsl_Company2(self):
        return self.__chartDsl_Company2

    @chartDsl_Company2.setter
    def chartDsl_Company2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_chartDsl_Company__chartDsl_Company2", None)
        self.__chartDsl_Company2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "chartDsl_Project"):
                    opp_val = getattr(item, "chartDsl_Project", None)
                    
                    if opp_val == self:
                        setattr(item, "chartDsl_Project", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "chartDsl_Project"):
                    opp_val = getattr(item, "chartDsl_Project", None)
                    
                    setattr(item, "chartDsl_Project", self)
                    
