from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class company_Company:

    def __init__(self, eotmDelta: str, name: str, Company: "company_Division" = None, company: "company_Division" = None, company_Company: "company_Employee" = None):
        self.eotmDelta = eotmDelta
        self.name = name
        self.Company = Company
        self.company = company
        self.company_Company = company_Company
        
    @property
    def eotmDelta(self) -> str:
        return self.__eotmDelta

    @eotmDelta.setter
    def eotmDelta(self, eotmDelta: str):
        self.__eotmDelta = eotmDelta

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def company_Company(self):
        return self.__company_Company

    @company_Company.setter
    def company_Company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Company__company_Company", None)
        self.__company_Company = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Employee30"):
                opp_val = getattr(old_value, "company_Employee30", None)
                if opp_val == self:
                    setattr(old_value, "company_Employee30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Employee30"):
                opp_val = getattr(value, "company_Employee30", None)
                setattr(value, "company_Employee30", self)

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Company__company", None)
        self.__company = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Division28"):
                opp_val = getattr(old_value, "Division28", None)
                if opp_val == self:
                    setattr(old_value, "Division28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Division28"):
                opp_val = getattr(value, "Division28", None)
                setattr(value, "Division28", self)

    @property
    def Company(self):
        return self.__Company

    @Company.setter
    def Company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Company__Company", None)
        self.__Company = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "division"):
                opp_val = getattr(old_value, "division", None)
                if opp_val == self:
                    setattr(old_value, "division", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "division"):
                opp_val = getattr(value, "division", None)
                setattr(value, "division", self)

class Employee:

    pass
class company_Freelance(Employee):

    def __init__(self, assignment: str):
        self.assignment = assignment
        
    @property
    def assignment(self) -> str:
        return self.__assignment

    @assignment.setter
    def assignment(self, assignment: str):
        self.__assignment = assignment

class company_Student(Employee):

    pass
class company_Division:

    def __init__(self, budget: str, name: str, numberEmployeesOfTheMonth: str, Division: "company_Employee" = None, company_Division: set["company_Department"] = None, directed: "company_Employee" = None, company_Division24: set["company_Employee"] = None, division: "company_Company" = None, Division28: "company_Company" = None):
        self.budget = budget
        self.name = name
        self.numberEmployeesOfTheMonth = numberEmployeesOfTheMonth
        self.Division = Division
        self.company_Division = company_Division if company_Division is not None else set()
        self.directed = directed
        self.company_Division24 = company_Division24 if company_Division24 is not None else set()
        self.division = division
        self.Division28 = Division28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def numberEmployeesOfTheMonth(self) -> str:
        return self.__numberEmployeesOfTheMonth

    @numberEmployeesOfTheMonth.setter
    def numberEmployeesOfTheMonth(self, numberEmployeesOfTheMonth: str):
        self.__numberEmployeesOfTheMonth = numberEmployeesOfTheMonth

    @property
    def budget(self) -> str:
        return self.__budget

    @budget.setter
    def budget(self, budget: str):
        self.__budget = budget

    @property
    def company_Division(self):
        return self.__company_Division

    @company_Division.setter
    def company_Division(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Division__company_Division", None)
        self.__company_Division = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company_Department20"):
                    opp_val = getattr(item, "company_Department20", None)
                    
                    if opp_val == self:
                        setattr(item, "company_Department20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company_Department20"):
                    opp_val = getattr(item, "company_Department20", None)
                    
                    setattr(item, "company_Department20", self)
                    

    @property
    def Division(self):
        return self.__Division

    @Division.setter
    def Division(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Division__Division", None)
        self.__Division = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "director"):
                opp_val = getattr(old_value, "director", None)
                if opp_val == self:
                    setattr(old_value, "director", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "director"):
                opp_val = getattr(value, "director", None)
                setattr(value, "director", self)

    @property
    def Division28(self):
        return self.__Division28

    @Division28.setter
    def Division28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Division__Division28", None)
        self.__Division28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company"):
                opp_val = getattr(old_value, "company", None)
                if opp_val == self:
                    setattr(old_value, "company", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company"):
                opp_val = getattr(value, "company", None)
                setattr(value, "company", self)

    @property
    def division(self):
        return self.__division

    @division.setter
    def division(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Division__division", None)
        self.__division = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company"):
                opp_val = getattr(old_value, "Company", None)
                if opp_val == self:
                    setattr(old_value, "Company", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company"):
                opp_val = getattr(value, "Company", None)
                setattr(value, "Company", self)

    @property
    def directed(self):
        return self.__directed

    @directed.setter
    def directed(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Division__directed", None)
        self.__directed = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee22"):
                opp_val = getattr(old_value, "Employee22", None)
                if opp_val == self:
                    setattr(old_value, "Employee22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee22"):
                opp_val = getattr(value, "Employee22", None)
                setattr(value, "Employee22", self)

    @property
    def company_Division24(self):
        return self.__company_Division24

    @company_Division24.setter
    def company_Division24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Division__company_Division24", None)
        self.__company_Division24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company_Employee25"):
                    opp_val = getattr(item, "company_Employee25", None)
                    
                    if opp_val == self:
                        setattr(item, "company_Employee25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company_Employee25"):
                    opp_val = getattr(item, "company_Employee25", None)
                    
                    setattr(item, "company_Employee25", self)
                    

class company_Department:

    def __init__(self, name: str, biggestNumberOfStudentsOrFreelancers: str, maxJuniors: str, budget: str, Department2: "company_Employee" = None, Department: "company_Employee" = None, employer: set["company_Employee"] = None, managed: "company_Employee" = None, Department13: "company_Department" = None, parentDepartment: set["company_Department"] = None, Department16: "company_Department" = None, subDepartment: "company_Department" = None, company_Department: set["company_Employee"] = None, company_Department20: "company_Division" = None):
        self.name = name
        self.biggestNumberOfStudentsOrFreelancers = biggestNumberOfStudentsOrFreelancers
        self.maxJuniors = maxJuniors
        self.budget = budget
        self.Department2 = Department2
        self.Department = Department
        self.employer = employer if employer is not None else set()
        self.managed = managed
        self.Department13 = Department13
        self.parentDepartment = parentDepartment if parentDepartment is not None else set()
        self.Department16 = Department16
        self.subDepartment = subDepartment
        self.company_Department = company_Department if company_Department is not None else set()
        self.company_Department20 = company_Department20
        
    @property
    def maxJuniors(self) -> str:
        return self.__maxJuniors

    @maxJuniors.setter
    def maxJuniors(self, maxJuniors: str):
        self.__maxJuniors = maxJuniors

    @property
    def budget(self) -> str:
        return self.__budget

    @budget.setter
    def budget(self, budget: str):
        self.__budget = budget

    @property
    def biggestNumberOfStudentsOrFreelancers(self) -> str:
        return self.__biggestNumberOfStudentsOrFreelancers

    @biggestNumberOfStudentsOrFreelancers.setter
    def biggestNumberOfStudentsOrFreelancers(self, biggestNumberOfStudentsOrFreelancers: str):
        self.__biggestNumberOfStudentsOrFreelancers = biggestNumberOfStudentsOrFreelancers

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def parentDepartment(self):
        return self.__parentDepartment

    @parentDepartment.setter
    def parentDepartment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Department__parentDepartment", None)
        self.__parentDepartment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Department13"):
                    opp_val = getattr(item, "Department13", None)
                    
                    if opp_val == self:
                        setattr(item, "Department13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Department13"):
                    opp_val = getattr(item, "Department13", None)
                    
                    setattr(item, "Department13", self)
                    

    @property
    def managed(self):
        return self.__managed

    @managed.setter
    def managed(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Department__managed", None)
        self.__managed = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee10"):
                opp_val = getattr(old_value, "Employee10", None)
                if opp_val == self:
                    setattr(old_value, "Employee10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee10"):
                opp_val = getattr(value, "Employee10", None)
                setattr(value, "Employee10", self)

    @property
    def employer(self):
        return self.__employer

    @employer.setter
    def employer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Department__employer", None)
        self.__employer = value if value is not None else set()
        
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
    def Department16(self):
        return self.__Department16

    @Department16.setter
    def Department16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Department__Department16", None)
        self.__Department16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subDepartment"):
                opp_val = getattr(old_value, "subDepartment", None)
                if opp_val == self:
                    setattr(old_value, "subDepartment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subDepartment"):
                opp_val = getattr(value, "subDepartment", None)
                setattr(value, "subDepartment", self)

    @property
    def subDepartment(self):
        return self.__subDepartment

    @subDepartment.setter
    def subDepartment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Department__subDepartment", None)
        self.__subDepartment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department16"):
                opp_val = getattr(old_value, "Department16", None)
                if opp_val == self:
                    setattr(old_value, "Department16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department16"):
                opp_val = getattr(value, "Department16", None)
                setattr(value, "Department16", self)

    @property
    def company_Department(self):
        return self.__company_Department

    @company_Department.setter
    def company_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Department__company_Department", None)
        self.__company_Department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "company_Employee18"):
                    opp_val = getattr(item, "company_Employee18", None)
                    
                    if opp_val == self:
                        setattr(item, "company_Employee18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "company_Employee18"):
                    opp_val = getattr(item, "company_Employee18", None)
                    
                    setattr(item, "company_Employee18", self)
                    

    @property
    def Department2(self):
        return self.__Department2

    @Department2.setter
    def Department2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Department__Department2", None)
        self.__Department2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boss"):
                opp_val = getattr(old_value, "boss", None)
                if opp_val == self:
                    setattr(old_value, "boss", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boss"):
                opp_val = getattr(value, "boss", None)
                setattr(value, "boss", self)

    @property
    def Department(self):
        return self.__Department

    @Department.setter
    def Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Department__Department", None)
        self.__Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee"):
                opp_val = getattr(old_value, "employee", None)
                if opp_val == self:
                    setattr(old_value, "employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee"):
                opp_val = getattr(value, "employee", None)
                setattr(value, "employee", self)

    @property
    def company_Department20(self):
        return self.__company_Department20

    @company_Department20.setter
    def company_Department20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Department__company_Department20", None)
        self.__company_Department20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Division"):
                opp_val = getattr(old_value, "company_Division", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Division"):
                opp_val = getattr(value, "company_Division", None)
                if opp_val is None:
                    setattr(value, "company_Division", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Department13(self):
        return self.__Department13

    @Department13.setter
    def Department13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Department__Department13", None)
        self.__Department13 = value
        
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

    def sumBudget(self) -> str:
        # TODO: Implement sumBudget method
        pass

    def calcExpenses(self) -> str:
        # TODO: Implement calcExpenses method
        pass

class company_Employee:

    def __init__(self, name: str, age: str, salary: str, boss: "company_Department" = None, employee: "company_Department" = None, director: "company_Division" = None, company_Employee: "company_Employee" = None, company_Employee4: "company_Employee" = None, company_Employee7: "company_Student" = None, Employee: "company_Department" = None, Employee10: "company_Department" = None, company_Employee18: "company_Department" = None, Employee22: "company_Division" = None, company_Employee25: "company_Division" = None, company_Employee30: "company_Company" = None):
        self.name = name
        self.age = age
        self.salary = salary
        self.boss = boss
        self.employee = employee
        self.director = director
        self.company_Employee = company_Employee
        self.company_Employee4 = company_Employee4
        self.company_Employee7 = company_Employee7
        self.Employee = Employee
        self.Employee10 = Employee10
        self.company_Employee18 = company_Employee18
        self.Employee22 = Employee22
        self.company_Employee25 = company_Employee25
        self.company_Employee30 = company_Employee30
        
    @property
    def age(self) -> str:
        return self.__age

    @age.setter
    def age(self, age: str):
        self.__age = age

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
    def employee(self):
        return self.__employee

    @employee.setter
    def employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__employee", None)
        self.__employee = value
        
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
    def company_Employee(self):
        return self.__company_Employee

    @company_Employee.setter
    def company_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__company_Employee", None)
        self.__company_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Employee4"):
                opp_val = getattr(old_value, "company_Employee4", None)
                if opp_val == self:
                    setattr(old_value, "company_Employee4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Employee4"):
                opp_val = getattr(value, "company_Employee4", None)
                setattr(value, "company_Employee4", self)

    @property
    def Employee10(self):
        return self.__Employee10

    @Employee10.setter
    def Employee10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__Employee10", None)
        self.__Employee10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "managed"):
                opp_val = getattr(old_value, "managed", None)
                if opp_val == self:
                    setattr(old_value, "managed", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "managed"):
                opp_val = getattr(value, "managed", None)
                setattr(value, "managed", self)

    @property
    def company_Employee7(self):
        return self.__company_Employee7

    @company_Employee7.setter
    def company_Employee7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__company_Employee7", None)
        self.__company_Employee7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Student"):
                opp_val = getattr(old_value, "company_Student", None)
                if opp_val == self:
                    setattr(old_value, "company_Student", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Student"):
                opp_val = getattr(value, "company_Student", None)
                setattr(value, "company_Student", self)

    @property
    def Employee22(self):
        return self.__Employee22

    @Employee22.setter
    def Employee22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__Employee22", None)
        self.__Employee22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "directed"):
                opp_val = getattr(old_value, "directed", None)
                if opp_val == self:
                    setattr(old_value, "directed", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "directed"):
                opp_val = getattr(value, "directed", None)
                setattr(value, "directed", self)

    @property
    def boss(self):
        return self.__boss

    @boss.setter
    def boss(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__boss", None)
        self.__boss = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department2"):
                opp_val = getattr(old_value, "Department2", None)
                if opp_val == self:
                    setattr(old_value, "Department2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department2"):
                opp_val = getattr(value, "Department2", None)
                setattr(value, "Department2", self)

    @property
    def company_Employee30(self):
        return self.__company_Employee30

    @company_Employee30.setter
    def company_Employee30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__company_Employee30", None)
        self.__company_Employee30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Company"):
                opp_val = getattr(old_value, "company_Company", None)
                if opp_val == self:
                    setattr(old_value, "company_Company", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Company"):
                opp_val = getattr(value, "company_Company", None)
                setattr(value, "company_Company", self)

    @property
    def company_Employee18(self):
        return self.__company_Employee18

    @company_Employee18.setter
    def company_Employee18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__company_Employee18", None)
        self.__company_Employee18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Department"):
                opp_val = getattr(old_value, "company_Department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Department"):
                opp_val = getattr(value, "company_Department", None)
                if opp_val is None:
                    setattr(value, "company_Department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Employee(self):
        return self.__Employee

    @Employee.setter
    def Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__Employee", None)
        self.__Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employer"):
                opp_val = getattr(old_value, "employer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employer"):
                opp_val = getattr(value, "employer", None)
                if opp_val is None:
                    setattr(value, "employer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def company_Employee4(self):
        return self.__company_Employee4

    @company_Employee4.setter
    def company_Employee4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__company_Employee4", None)
        self.__company_Employee4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Employee"):
                opp_val = getattr(old_value, "company_Employee", None)
                if opp_val == self:
                    setattr(old_value, "company_Employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Employee"):
                opp_val = getattr(value, "company_Employee", None)
                setattr(value, "company_Employee", self)

    @property
    def company_Employee25(self):
        return self.__company_Employee25

    @company_Employee25.setter
    def company_Employee25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__company_Employee25", None)
        self.__company_Employee25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company_Division24"):
                opp_val = getattr(old_value, "company_Division24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company_Division24"):
                opp_val = getattr(value, "company_Division24", None)
                if opp_val is None:
                    setattr(value, "company_Division24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_company_Employee__director", None)
        self.__director = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Division"):
                opp_val = getattr(old_value, "Division", None)
                if opp_val == self:
                    setattr(old_value, "Division", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Division"):
                opp_val = getattr(value, "Division", None)
                setattr(value, "Division", self)
