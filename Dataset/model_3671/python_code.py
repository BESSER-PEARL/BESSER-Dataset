from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Demo_Project:

    def __init__(self, budget: int, name: bool, WorksOn_project: set["Demo_Employee"] = None, Controls_project: "Demo_Department" = None, Project: "Demo_Employee" = None, Project4: "Demo_Department" = None):
        self.budget = budget
        self.name = name
        self.WorksOn_project = WorksOn_project if WorksOn_project is not None else set()
        self.Controls_project = Controls_project
        self.Project = Project
        self.Project4 = Project4
        
    @property
    def budget(self) -> int:
        return self.__budget

    @budget.setter
    def budget(self, budget: int):
        self.__budget = budget

    @property
    def name(self) -> bool:
        return self.__name

    @name.setter
    def name(self, name: bool):
        self.__name = name

    @property
    def WorksOn_project(self):
        return self.__WorksOn_project

    @WorksOn_project.setter
    def WorksOn_project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Demo_Project__WorksOn_project", None)
        self.__WorksOn_project = value if value is not None else set()
        
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
    def Controls_project(self):
        return self.__Controls_project

    @Controls_project.setter
    def Controls_project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Demo_Project__Controls_project", None)
        self.__Controls_project = value
        
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

    @property
    def Project4(self):
        return self.__Project4

    @Project4.setter
    def Project4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Demo_Project__Project4", None)
        self.__Project4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Controls_department"):
                opp_val = getattr(old_value, "Controls_department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Controls_department"):
                opp_val = getattr(value, "Controls_department", None)
                if opp_val is None:
                    setattr(value, "Controls_department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Project(self):
        return self.__Project

    @Project.setter
    def Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Demo_Project__Project", None)
        self.__Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorksOn_employee"):
                opp_val = getattr(old_value, "WorksOn_employee", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorksOn_employee"):
                opp_val = getattr(value, "WorksOn_employee", None)
                if opp_val is None:
                    setattr(value, "WorksOn_employee", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Demo_Department:

    def __init__(self, name: bool, location: bool, budget: int, Department: "Demo_Employee" = None, Department8: "Demo_Project" = None, WorksIn_department: set["Demo_Employee"] = None, Controls_department: set["Demo_Project"] = None):
        self.name = name
        self.location = location
        self.budget = budget
        self.Department = Department
        self.Department8 = Department8
        self.WorksIn_department = WorksIn_department if WorksIn_department is not None else set()
        self.Controls_department = Controls_department if Controls_department is not None else set()
        
    @property
    def budget(self) -> int:
        return self.__budget

    @budget.setter
    def budget(self, budget: int):
        self.__budget = budget

    @property
    def name(self) -> bool:
        return self.__name

    @name.setter
    def name(self, name: bool):
        self.__name = name

    @property
    def location(self) -> bool:
        return self.__location

    @location.setter
    def location(self, location: bool):
        self.__location = location

    @property
    def Department(self):
        return self.__Department

    @Department.setter
    def Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Demo_Department__Department", None)
        self.__Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorksIn_employee"):
                opp_val = getattr(old_value, "WorksIn_employee", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorksIn_employee"):
                opp_val = getattr(value, "WorksIn_employee", None)
                if opp_val is None:
                    setattr(value, "WorksIn_employee", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WorksIn_department(self):
        return self.__WorksIn_department

    @WorksIn_department.setter
    def WorksIn_department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Demo_Department__WorksIn_department", None)
        self.__WorksIn_department = value if value is not None else set()
        
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
    def Department8(self):
        return self.__Department8

    @Department8.setter
    def Department8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Demo_Department__Department8", None)
        self.__Department8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Controls_project"):
                opp_val = getattr(old_value, "Controls_project", None)
                if opp_val == self:
                    setattr(old_value, "Controls_project", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Controls_project"):
                opp_val = getattr(value, "Controls_project", None)
                setattr(value, "Controls_project", self)

    @property
    def Controls_department(self):
        return self.__Controls_department

    @Controls_department.setter
    def Controls_department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Demo_Department__Controls_department", None)
        self.__Controls_department = value if value is not None else set()
        
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
                    

class Demo_Employee:

    def __init__(self, name: bool, salary: int, WorksIn_employee: set["Demo_Department"] = None, Employee6: "Demo_Project" = None, WorksOn_employee: set["Demo_Project"] = None, Employee: "Demo_Department" = None):
        self.name = name
        self.salary = salary
        self.WorksIn_employee = WorksIn_employee if WorksIn_employee is not None else set()
        self.Employee6 = Employee6
        self.WorksOn_employee = WorksOn_employee if WorksOn_employee is not None else set()
        self.Employee = Employee
        
    @property
    def salary(self) -> int:
        return self.__salary

    @salary.setter
    def salary(self, salary: int):
        self.__salary = salary

    @property
    def name(self) -> bool:
        return self.__name

    @name.setter
    def name(self, name: bool):
        self.__name = name

    @property
    def Employee6(self):
        return self.__Employee6

    @Employee6.setter
    def Employee6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Demo_Employee__Employee6", None)
        self.__Employee6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorksOn_project"):
                opp_val = getattr(old_value, "WorksOn_project", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorksOn_project"):
                opp_val = getattr(value, "WorksOn_project", None)
                if opp_val is None:
                    setattr(value, "WorksOn_project", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WorksOn_employee(self):
        return self.__WorksOn_employee

    @WorksOn_employee.setter
    def WorksOn_employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Demo_Employee__WorksOn_employee", None)
        self.__WorksOn_employee = value if value is not None else set()
        
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
    def Employee(self):
        return self.__Employee

    @Employee.setter
    def Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Demo_Employee__Employee", None)
        self.__Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorksIn_department"):
                opp_val = getattr(old_value, "WorksIn_department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorksIn_department"):
                opp_val = getattr(value, "WorksIn_department", None)
                if opp_val is None:
                    setattr(value, "WorksIn_department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def WorksIn_employee(self):
        return self.__WorksIn_employee

    @WorksIn_employee.setter
    def WorksIn_employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Demo_Employee__WorksIn_employee", None)
        self.__WorksIn_employee = value if value is not None else set()
        
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
                    
