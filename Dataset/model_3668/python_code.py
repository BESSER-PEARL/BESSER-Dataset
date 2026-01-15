from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Company_Project:

    def __init__(self, name: str, budget: int, Project4: "Company_Department" = None, Project: "Company_Employee" = None, WorksOn_Project: set["Company_Employee"] = None, Controls_Project: "Company_Department" = None):
        self.name = name
        self.budget = budget
        self.Project4 = Project4
        self.Project = Project
        self.WorksOn_Project = WorksOn_Project if WorksOn_Project is not None else set()
        self.Controls_Project = Controls_Project
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def budget(self) -> int:
        return self.__budget

    @budget.setter
    def budget(self, budget: int):
        self.__budget = budget

    @property
    def WorksOn_Project(self):
        return self.__WorksOn_Project

    @WorksOn_Project.setter
    def WorksOn_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Project__WorksOn_Project", None)
        self.__WorksOn_Project = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee6"):
                    opp_val = getattr(item, "Employee6", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee6"):
                    opp_val = getattr(item, "Employee6", None)
                    
                    setattr(item, "Employee6", self)
                    

    @property
    def Project4(self):
        return self.__Project4

    @Project4.setter
    def Project4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Project__Project4", None)
        self.__Project4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Controls_Department"):
                opp_val = getattr(old_value, "Controls_Department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Controls_Department"):
                opp_val = getattr(value, "Controls_Department", None)
                if opp_val is None:
                    setattr(value, "Controls_Department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Project(self):
        return self.__Project

    @Project.setter
    def Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Project__Project", None)
        self.__Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorksOn_Employee"):
                opp_val = getattr(old_value, "WorksOn_Employee", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorksOn_Employee"):
                opp_val = getattr(value, "WorksOn_Employee", None)
                if opp_val is None:
                    setattr(value, "WorksOn_Employee", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Controls_Project(self):
        return self.__Controls_Project

    @Controls_Project.setter
    def Controls_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Project__Controls_Project", None)
        self.__Controls_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department8"):
                opp_val = getattr(old_value, "Department8", None)
                if opp_val == self:
                    setattr(old_value, "Department8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department8"):
                opp_val = getattr(value, "Department8", None)
                setattr(value, "Department8", self)

class Company_Department:

    def __init__(self, name: str, location: str, budget: int, Controls_Department: set["Company_Project"] = None, Department: "Company_Employee" = None, WorksIn_Department: set["Company_Employee"] = None, Department8: "Company_Project" = None):
        self.name = name
        self.location = location
        self.budget = budget
        self.Controls_Department = Controls_Department if Controls_Department is not None else set()
        self.Department = Department
        self.WorksIn_Department = WorksIn_Department if WorksIn_Department is not None else set()
        self.Department8 = Department8
        
    @property
    def budget(self) -> int:
        return self.__budget

    @budget.setter
    def budget(self, budget: int):
        self.__budget = budget

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def Controls_Department(self):
        return self.__Controls_Department

    @Controls_Department.setter
    def Controls_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Department__Controls_Department", None)
        self.__Controls_Department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Project4"):
                    opp_val = getattr(item, "Project4", None)
                    
                    if opp_val == self:
                        setattr(item, "Project4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Project4"):
                    opp_val = getattr(item, "Project4", None)
                    
                    setattr(item, "Project4", self)
                    

    @property
    def Department(self):
        return self.__Department

    @Department.setter
    def Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Department__Department", None)
        self.__Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorksIn_Employee"):
                opp_val = getattr(old_value, "WorksIn_Employee", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorksIn_Employee"):
                opp_val = getattr(value, "WorksIn_Employee", None)
                if opp_val is None:
                    setattr(value, "WorksIn_Employee", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Department8(self):
        return self.__Department8

    @Department8.setter
    def Department8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Department__Department8", None)
        self.__Department8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Controls_Project"):
                opp_val = getattr(old_value, "Controls_Project", None)
                if opp_val == self:
                    setattr(old_value, "Controls_Project", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Controls_Project"):
                opp_val = getattr(value, "Controls_Project", None)
                setattr(value, "Controls_Project", self)

    @property
    def WorksIn_Department(self):
        return self.__WorksIn_Department

    @WorksIn_Department.setter
    def WorksIn_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Department__WorksIn_Department", None)
        self.__WorksIn_Department = value if value is not None else set()
        
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
                    

class Company_Employee:

    def __init__(self, name: str, salary: int, WorksIn_Employee: set["Company_Department"] = None, WorksOn_Employee: set["Company_Project"] = None, Employee: "Company_Department" = None, Employee6: "Company_Project" = None):
        self.name = name
        self.salary = salary
        self.WorksIn_Employee = WorksIn_Employee if WorksIn_Employee is not None else set()
        self.WorksOn_Employee = WorksOn_Employee if WorksOn_Employee is not None else set()
        self.Employee = Employee
        self.Employee6 = Employee6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def salary(self) -> int:
        return self.__salary

    @salary.setter
    def salary(self, salary: int):
        self.__salary = salary

    @property
    def Employee(self):
        return self.__Employee

    @Employee.setter
    def Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Employee__Employee", None)
        self.__Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorksIn_Department"):
                opp_val = getattr(old_value, "WorksIn_Department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorksIn_Department"):
                opp_val = getattr(value, "WorksIn_Department", None)
                if opp_val is None:
                    setattr(value, "WorksIn_Department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WorksOn_Employee(self):
        return self.__WorksOn_Employee

    @WorksOn_Employee.setter
    def WorksOn_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Employee__WorksOn_Employee", None)
        self.__WorksOn_Employee = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Project"):
                    opp_val = getattr(item, "Project", None)
                    
                    if opp_val == self:
                        setattr(item, "Project", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Project"):
                    opp_val = getattr(item, "Project", None)
                    
                    setattr(item, "Project", self)
                    

    @property
    def Employee6(self):
        return self.__Employee6

    @Employee6.setter
    def Employee6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Employee__Employee6", None)
        self.__Employee6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorksOn_Project"):
                opp_val = getattr(old_value, "WorksOn_Project", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorksOn_Project"):
                opp_val = getattr(value, "WorksOn_Project", None)
                if opp_val is None:
                    setattr(value, "WorksOn_Project", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WorksIn_Employee(self):
        return self.__WorksIn_Employee

    @WorksIn_Employee.setter
    def WorksIn_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Employee__WorksIn_Employee", None)
        self.__WorksIn_Employee = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Department"):
                    opp_val = getattr(item, "Department", None)
                    
                    if opp_val == self:
                        setattr(item, "Department", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Department"):
                    opp_val = getattr(item, "Department", None)
                    
                    setattr(item, "Department", self)
                    
