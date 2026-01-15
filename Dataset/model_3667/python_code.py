from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class exo1_Company:

    pass
class exo1_Employee:

    def __init__(self, salary: str, name: str, Employee5: "exo1_Project" = None, Employee: "exo1_Departement" = None, employees: set["exo1_Project"] = None, employees9: set["exo1_Departement"] = None, exo1_Employee: "exo1_Company" = None):
        self.salary = salary
        self.name = name
        self.Employee5 = Employee5
        self.Employee = Employee
        self.employees = employees if employees is not None else set()
        self.employees9 = employees9 if employees9 is not None else set()
        self.exo1_Employee = exo1_Employee
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def salary(self) -> str:
        return self.__salary

    @salary.setter
    def salary(self, salary: str):
        self.__salary = salary

    @property
    def employees9(self):
        return self.__employees9

    @employees9.setter
    def employees9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exo1_Employee__employees9", None)
        self.__employees9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Departement10"):
                    opp_val = getattr(item, "Departement10", None)
                    
                    if opp_val == self:
                        setattr(item, "Departement10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Departement10"):
                    opp_val = getattr(item, "Departement10", None)
                    
                    setattr(item, "Departement10", self)
                    

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exo1_Employee__employees", None)
        self.__employees = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Project7"):
                    opp_val = getattr(item, "Project7", None)
                    
                    if opp_val == self:
                        setattr(item, "Project7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Project7"):
                    opp_val = getattr(item, "Project7", None)
                    
                    setattr(item, "Project7", self)
                    

    @property
    def exo1_Employee(self):
        return self.__exo1_Employee

    @exo1_Employee.setter
    def exo1_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exo1_Employee__exo1_Employee", None)
        self.__exo1_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exo1_Company"):
                opp_val = getattr(old_value, "exo1_Company", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exo1_Company"):
                opp_val = getattr(value, "exo1_Company", None)
                if opp_val is None:
                    setattr(value, "exo1_Company", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Employee5(self):
        return self.__Employee5

    @Employee5.setter
    def Employee5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exo1_Employee__Employee5", None)
        self.__Employee5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projects4"):
                opp_val = getattr(old_value, "projects4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projects4"):
                opp_val = getattr(value, "projects4", None)
                if opp_val is None:
                    setattr(value, "projects4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Employee(self):
        return self.__Employee

    @Employee.setter
    def Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exo1_Employee__Employee", None)
        self.__Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "departements"):
                opp_val = getattr(old_value, "departements", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "departements"):
                opp_val = getattr(value, "departements", None)
                if opp_val is None:
                    setattr(value, "departements", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class exo1_Project:

    def __init__(self, name: str, budget: int, projects: "exo1_Departement" = None, projects4: set["exo1_Employee"] = None, Project: "exo1_Departement" = None, exo1_Project: "exo1_Company" = None, Project7: "exo1_Employee" = None):
        self.name = name
        self.budget = budget
        self.projects = projects
        self.projects4 = projects4 if projects4 is not None else set()
        self.Project = Project
        self.exo1_Project = exo1_Project
        self.Project7 = Project7
        
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
    def projects4(self):
        return self.__projects4

    @projects4.setter
    def projects4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exo1_Project__projects4", None)
        self.__projects4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee5"):
                    opp_val = getattr(item, "Employee5", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee5"):
                    opp_val = getattr(item, "Employee5", None)
                    
                    setattr(item, "Employee5", self)
                    

    @property
    def projects(self):
        return self.__projects

    @projects.setter
    def projects(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exo1_Project__projects", None)
        self.__projects = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Departement"):
                opp_val = getattr(old_value, "Departement", None)
                if opp_val == self:
                    setattr(old_value, "Departement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Departement"):
                opp_val = getattr(value, "Departement", None)
                setattr(value, "Departement", self)

    @property
    def Project7(self):
        return self.__Project7

    @Project7.setter
    def Project7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exo1_Project__Project7", None)
        self.__Project7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employees"):
                opp_val = getattr(old_value, "employees", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employees"):
                opp_val = getattr(value, "employees", None)
                if opp_val is None:
                    setattr(value, "employees", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def exo1_Project(self):
        return self.__exo1_Project

    @exo1_Project.setter
    def exo1_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exo1_Project__exo1_Project", None)
        self.__exo1_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exo1_Company13"):
                opp_val = getattr(old_value, "exo1_Company13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exo1_Company13"):
                opp_val = getattr(value, "exo1_Company13", None)
                if opp_val is None:
                    setattr(value, "exo1_Company13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Project(self):
        return self.__Project

    @Project.setter
    def Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exo1_Project__Project", None)
        self.__Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "departement"):
                opp_val = getattr(old_value, "departement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "departement"):
                opp_val = getattr(value, "departement", None)
                if opp_val is None:
                    setattr(value, "departement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class exo1_Departement:

    def __init__(self, name: str, location: str, budget: int, Departement: "exo1_Project" = None, departement: set["exo1_Project"] = None, departements: set["exo1_Employee"] = None, exo1_Departement: "exo1_Company" = None, Departement10: "exo1_Employee" = None):
        self.name = name
        self.location = location
        self.budget = budget
        self.Departement = Departement
        self.departement = departement if departement is not None else set()
        self.departements = departements if departements is not None else set()
        self.exo1_Departement = exo1_Departement
        self.Departement10 = Departement10
        
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
    def departement(self):
        return self.__departement

    @departement.setter
    def departement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exo1_Departement__departement", None)
        self.__departement = value if value is not None else set()
        
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
    def Departement10(self):
        return self.__Departement10

    @Departement10.setter
    def Departement10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exo1_Departement__Departement10", None)
        self.__Departement10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employees9"):
                opp_val = getattr(old_value, "employees9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employees9"):
                opp_val = getattr(value, "employees9", None)
                if opp_val is None:
                    setattr(value, "employees9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def exo1_Departement(self):
        return self.__exo1_Departement

    @exo1_Departement.setter
    def exo1_Departement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exo1_Departement__exo1_Departement", None)
        self.__exo1_Departement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "exo1_Company15"):
                opp_val = getattr(old_value, "exo1_Company15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "exo1_Company15"):
                opp_val = getattr(value, "exo1_Company15", None)
                if opp_val is None:
                    setattr(value, "exo1_Company15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Departement(self):
        return self.__Departement

    @Departement.setter
    def Departement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exo1_Departement__Departement", None)
        self.__Departement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projects"):
                opp_val = getattr(old_value, "projects", None)
                if opp_val == self:
                    setattr(old_value, "projects", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projects"):
                opp_val = getattr(value, "projects", None)
                setattr(value, "projects", self)

    @property
    def departements(self):
        return self.__departements

    @departements.setter
    def departements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_exo1_Departement__departements", None)
        self.__departements = value if value is not None else set()
        
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
                    
