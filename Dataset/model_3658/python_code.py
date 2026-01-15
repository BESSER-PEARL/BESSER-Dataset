from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Employee:

    pass
class toe_Manager(Employee):

    pass
class AllBase:

    pass
class toe_Contribution(AllBase):

    def __init__(self, description: str, Contribution: "toe_Employee" = None, Contribution26: "toe_Project" = None, contributions: "toe_Employee" = None, contributions10: "toe_Project" = None):
        self.description = description
        self.Contribution = Contribution
        self.Contribution26 = Contribution26
        self.contributions = contributions
        self.contributions10 = contributions10
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def Contribution26(self):
        return self.__Contribution26

    @Contribution26.setter
    def Contribution26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Contribution__Contribution26", None)
        self.__Contribution26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "project"):
                opp_val = getattr(old_value, "project", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "project"):
                opp_val = getattr(value, "project", None)
                if opp_val is None:
                    setattr(value, "project", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Contribution(self):
        return self.__Contribution

    @Contribution.setter
    def Contribution(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Contribution__Contribution", None)
        self.__Contribution = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee"):
                opp_val = getattr(old_value, "employee", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee"):
                opp_val = getattr(value, "employee", None)
                if opp_val is None:
                    setattr(value, "employee", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def contributions10(self):
        return self.__contributions10

    @contributions10.setter
    def contributions10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Contribution__contributions10", None)
        self.__contributions10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Project11"):
                opp_val = getattr(old_value, "Project11", None)
                if opp_val == self:
                    setattr(old_value, "Project11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Project11"):
                opp_val = getattr(value, "Project11", None)
                setattr(value, "Project11", self)

    @property
    def contributions(self):
        return self.__contributions

    @contributions.setter
    def contributions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Contribution__contributions", None)
        self.__contributions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee"):
                opp_val = getattr(old_value, "Employee", None)
                if opp_val == self:
                    setattr(old_value, "Employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee"):
                opp_val = getattr(value, "Employee", None)
                setattr(value, "Employee", self)

class toe_Project(AllBase):

    def __init__(self, name: str, departmentWide: bool, Project: "toe_Employee" = None, Project5: "toe_Manager" = None, projects: set["toe_Employee"] = None, leads: "toe_Manager" = None, project: set["toe_Contribution"] = None, Project11: "toe_Contribution" = None):
        self.name = name
        self.departmentWide = departmentWide
        self.Project = Project
        self.Project5 = Project5
        self.projects = projects if projects is not None else set()
        self.leads = leads
        self.project = project if project is not None else set()
        self.Project11 = Project11
        
    @property
    def departmentWide(self) -> bool:
        return self.__departmentWide

    @departmentWide.setter
    def departmentWide(self, departmentWide: bool):
        self.__departmentWide = departmentWide

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Project11(self):
        return self.__Project11

    @Project11.setter
    def Project11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Project__Project11", None)
        self.__Project11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contributions10"):
                opp_val = getattr(old_value, "contributions10", None)
                if opp_val == self:
                    setattr(old_value, "contributions10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contributions10"):
                opp_val = getattr(value, "contributions10", None)
                setattr(value, "contributions10", self)

    @property
    def leads(self):
        return self.__leads

    @leads.setter
    def leads(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Project__leads", None)
        self.__leads = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Manager24"):
                opp_val = getattr(old_value, "Manager24", None)
                if opp_val == self:
                    setattr(old_value, "Manager24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Manager24"):
                opp_val = getattr(value, "Manager24", None)
                setattr(value, "Manager24", self)

    @property
    def Project5(self):
        return self.__Project5

    @Project5.setter
    def Project5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Project__Project5", None)
        self.__Project5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lead"):
                opp_val = getattr(old_value, "lead", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lead"):
                opp_val = getattr(value, "lead", None)
                if opp_val is None:
                    setattr(value, "lead", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def projects(self):
        return self.__projects

    @projects.setter
    def projects(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Project__projects", None)
        self.__projects = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee22"):
                    opp_val = getattr(item, "Employee22", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee22"):
                    opp_val = getattr(item, "Employee22", None)
                    
                    setattr(item, "Employee22", self)
                    

    @property
    def Project(self):
        return self.__Project

    @Project.setter
    def Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Project__Project", None)
        self.__Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projectTeam"):
                opp_val = getattr(old_value, "projectTeam", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projectTeam"):
                opp_val = getattr(value, "projectTeam", None)
                if opp_val is None:
                    setattr(value, "projectTeam", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def project(self):
        return self.__project

    @project.setter
    def project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Project__project", None)
        self.__project = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Contribution26"):
                    opp_val = getattr(item, "Contribution26", None)
                    
                    if opp_val == self:
                        setattr(item, "Contribution26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Contribution26"):
                    opp_val = getattr(item, "Contribution26", None)
                    
                    setattr(item, "Contribution26", self)
                    

class toe_Department(AllBase):

    def __init__(self, name: str, Department: "toe_Employee" = None, Department7: "toe_Manager" = None, department: set["toe_Employee"] = None, Department19: "toe_Department" = None, subDepartments: "toe_Department" = None, managedDepartment: "toe_Manager" = None, Department14: "toe_Department" = None, parentDepartment: set["toe_Department"] = None):
        self.name = name
        self.Department = Department
        self.Department7 = Department7
        self.department = department if department is not None else set()
        self.Department19 = Department19
        self.subDepartments = subDepartments
        self.managedDepartment = managedDepartment
        self.Department14 = Department14
        self.parentDepartment = parentDepartment if parentDepartment is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Department14(self):
        return self.__Department14

    @Department14.setter
    def Department14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Department__Department14", None)
        self.__Department14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentDepartment"):
                opp_val = getattr(old_value, "parentDepartment", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentDepartment"):
                opp_val = getattr(value, "parentDepartment", None)
                if opp_val is None:
                    setattr(value, "parentDepartment", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Department7(self):
        return self.__Department7

    @Department7.setter
    def Department7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Department__Department7", None)
        self.__Department7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manager"):
                opp_val = getattr(old_value, "manager", None)
                if opp_val == self:
                    setattr(old_value, "manager", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manager"):
                opp_val = getattr(value, "manager", None)
                setattr(value, "manager", self)

    @property
    def managedDepartment(self):
        return self.__managedDepartment

    @managedDepartment.setter
    def managedDepartment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Department__managedDepartment", None)
        self.__managedDepartment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Manager"):
                opp_val = getattr(old_value, "Manager", None)
                if opp_val == self:
                    setattr(old_value, "Manager", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Manager"):
                opp_val = getattr(value, "Manager", None)
                setattr(value, "Manager", self)

    @property
    def subDepartments(self):
        return self.__subDepartments

    @subDepartments.setter
    def subDepartments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Department__subDepartments", None)
        self.__subDepartments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department19"):
                opp_val = getattr(old_value, "Department19", None)
                if opp_val == self:
                    setattr(old_value, "Department19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department19"):
                opp_val = getattr(value, "Department19", None)
                setattr(value, "Department19", self)

    @property
    def parentDepartment(self):
        return self.__parentDepartment

    @parentDepartment.setter
    def parentDepartment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Department__parentDepartment", None)
        self.__parentDepartment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Department14"):
                    opp_val = getattr(item, "Department14", None)
                    
                    if opp_val == self:
                        setattr(item, "Department14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Department14"):
                    opp_val = getattr(item, "Department14", None)
                    
                    setattr(item, "Department14", self)
                    

    @property
    def Department19(self):
        return self.__Department19

    @Department19.setter
    def Department19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Department__Department19", None)
        self.__Department19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subDepartments"):
                opp_val = getattr(old_value, "subDepartments", None)
                if opp_val == self:
                    setattr(old_value, "subDepartments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subDepartments"):
                opp_val = getattr(value, "subDepartments", None)
                setattr(value, "subDepartments", self)

    @property
    def Department(self):
        return self.__Department

    @Department.setter
    def Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Department__Department", None)
        self.__Department = value
        
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
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Department__department", None)
        self.__department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee16"):
                    opp_val = getattr(item, "Employee16", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee16"):
                    opp_val = getattr(item, "Employee16", None)
                    
                    setattr(item, "Employee16", self)
                    

    def allSubDepartments(self) -> str:
        # TODO: Implement allSubDepartments method
        pass

class toe_Employee(AllBase):

    def __init__(self, name: str, salary: int, projectTeam: set["toe_Project"] = None, employees: "toe_Department" = None, employee: set["toe_Contribution"] = None, Employee22: "toe_Project" = None, Employee: "toe_Contribution" = None, Employee16: "toe_Department" = None):
        self.name = name
        self.salary = salary
        self.projectTeam = projectTeam if projectTeam is not None else set()
        self.employees = employees
        self.employee = employee if employee is not None else set()
        self.Employee22 = Employee22
        self.Employee = Employee
        self.Employee16 = Employee16
        
    @property
    def salary(self) -> int:
        return self.__salary

    @salary.setter
    def salary(self, salary: int):
        self.__salary = salary

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Employee16(self):
        return self.__Employee16

    @Employee16.setter
    def Employee16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Employee__Employee16", None)
        self.__Employee16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department"):
                opp_val = getattr(old_value, "department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department"):
                opp_val = getattr(value, "department", None)
                if opp_val is None:
                    setattr(value, "department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Employee22(self):
        return self.__Employee22

    @Employee22.setter
    def Employee22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Employee__Employee22", None)
        self.__Employee22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projects"):
                opp_val = getattr(old_value, "projects", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projects"):
                opp_val = getattr(value, "projects", None)
                if opp_val is None:
                    setattr(value, "projects", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Employee__employees", None)
        self.__employees = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department"):
                opp_val = getattr(old_value, "Department", None)
                if opp_val == self:
                    setattr(old_value, "Department", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department"):
                opp_val = getattr(value, "Department", None)
                setattr(value, "Department", self)

    @property
    def projectTeam(self):
        return self.__projectTeam

    @projectTeam.setter
    def projectTeam(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Employee__projectTeam", None)
        self.__projectTeam = value if value is not None else set()
        
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
        old_value = getattr(self, f"_toe_Employee__Employee", None)
        self.__Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contributions"):
                opp_val = getattr(old_value, "contributions", None)
                if opp_val == self:
                    setattr(old_value, "contributions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contributions"):
                opp_val = getattr(value, "contributions", None)
                setattr(value, "contributions", self)

    @property
    def employee(self):
        return self.__employee

    @employee.setter
    def employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_toe_Employee__employee", None)
        self.__employee = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Contribution"):
                    opp_val = getattr(item, "Contribution", None)
                    
                    if opp_val == self:
                        setattr(item, "Contribution", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Contribution"):
                    opp_val = getattr(item, "Contribution", None)
                    
                    setattr(item, "Contribution", self)
                    

class toe_AllBase(ABC):

    pass
class toe_AllHolder:

    pass