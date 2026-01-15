from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class employee_Department:

    def __init__(self, deptID: int, name: str, employee_Department: "employee_Employee" = None, Department: "employee_Company" = None, department: set["employee_Employee"] = None, departments: "employee_Company" = None, Department8: "employee_Employee" = None):
        self.deptID = deptID
        self.name = name
        self.employee_Department = employee_Department
        self.Department = Department
        self.department = department if department is not None else set()
        self.departments = departments
        self.Department8 = Department8
        
    @property
    def deptID(self) -> int:
        return self.__deptID

    @deptID.setter
    def deptID(self, deptID: int):
        self.__deptID = deptID

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Department__department", None)
        self.__department = value if value is not None else set()
        
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
    def employee_Department(self):
        return self.__employee_Department

    @employee_Department.setter
    def employee_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Department__employee_Department", None)
        self.__employee_Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Employee"):
                opp_val = getattr(old_value, "employee_Employee", None)
                if opp_val == self:
                    setattr(old_value, "employee_Employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee"):
                opp_val = getattr(value, "employee_Employee", None)
                setattr(value, "employee_Employee", self)

    @property
    def Department8(self):
        return self.__Department8

    @Department8.setter
    def Department8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Department__Department8", None)
        self.__Department8 = value
        
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
    def departments(self):
        return self.__departments

    @departments.setter
    def departments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Department__departments", None)
        self.__departments = value
        
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
    def Department(self):
        return self.__Department

    @Department.setter
    def Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Department__Department", None)
        self.__Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company2"):
                opp_val = getattr(old_value, "company2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company2"):
                opp_val = getattr(value, "company2", None)
                if opp_val is None:
                    setattr(value, "company2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class employee_Employee:

    def __init__(self, isManager: bool, empID: int, name: str, employee_Employee: "employee_Department" = None, Employee: "employee_Company" = None, Employee5: "employee_Department" = None, employees: "employee_Department" = None, Employee11: "employee_Employee" = None, directReports: "employee_Employee" = None, Employee14: "employee_Employee" = None, manager: set["employee_Employee"] = None, employees16: "employee_Company" = None):
        self.isManager = isManager
        self.empID = empID
        self.name = name
        self.employee_Employee = employee_Employee
        self.Employee = Employee
        self.Employee5 = Employee5
        self.employees = employees
        self.Employee11 = Employee11
        self.directReports = directReports
        self.Employee14 = Employee14
        self.manager = manager if manager is not None else set()
        self.employees16 = employees16
        
    @property
    def empID(self) -> int:
        return self.__empID

    @empID.setter
    def empID(self, empID: int):
        self.__empID = empID

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def isManager(self) -> bool:
        return self.__isManager

    @isManager.setter
    def isManager(self, isManager: bool):
        self.__isManager = isManager

    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__manager", None)
        self.__manager = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee14"):
                    opp_val = getattr(item, "Employee14", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee14"):
                    opp_val = getattr(item, "Employee14", None)
                    
                    setattr(item, "Employee14", self)
                    

    @property
    def directReports(self):
        return self.__directReports

    @directReports.setter
    def directReports(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__directReports", None)
        self.__directReports = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Employee11"):
                opp_val = getattr(old_value, "Employee11", None)
                if opp_val == self:
                    setattr(old_value, "Employee11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Employee11"):
                opp_val = getattr(value, "Employee11", None)
                setattr(value, "Employee11", self)

    @property
    def Employee5(self):
        return self.__Employee5

    @Employee5.setter
    def Employee5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__Employee5", None)
        self.__Employee5 = value
        
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
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employees", None)
        self.__employees = value
        
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
    def employees16(self):
        return self.__employees16

    @employees16.setter
    def employees16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employees16", None)
        self.__employees16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company17"):
                opp_val = getattr(old_value, "Company17", None)
                if opp_val == self:
                    setattr(old_value, "Company17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company17"):
                opp_val = getattr(value, "Company17", None)
                setattr(value, "Company17", self)

    @property
    def Employee14(self):
        return self.__Employee14

    @Employee14.setter
    def Employee14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__Employee14", None)
        self.__Employee14 = value
        
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
    def Employee(self):
        return self.__Employee

    @Employee.setter
    def Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__Employee", None)
        self.__Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company"):
                opp_val = getattr(old_value, "company", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company"):
                opp_val = getattr(value, "company", None)
                if opp_val is None:
                    setattr(value, "company", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Employee11(self):
        return self.__Employee11

    @Employee11.setter
    def Employee11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__Employee11", None)
        self.__Employee11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "directReports"):
                opp_val = getattr(old_value, "directReports", None)
                if opp_val == self:
                    setattr(old_value, "directReports", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "directReports"):
                opp_val = getattr(value, "directReports", None)
                setattr(value, "directReports", self)

    @property
    def employee_Employee(self):
        return self.__employee_Employee

    @employee_Employee.setter
    def employee_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee", None)
        self.__employee_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Department"):
                opp_val = getattr(old_value, "employee_Department", None)
                if opp_val == self:
                    setattr(old_value, "employee_Department", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Department"):
                opp_val = getattr(value, "employee_Department", None)
                setattr(value, "employee_Department", self)

    def reportsTo(self, mgr: str) -> bool:
        # TODO: Implement reportsTo method
        pass

    def reportingChain(self) -> str:
        # TODO: Implement reportingChain method
        pass

    def allReports(self) -> str:
        # TODO: Implement allReports method
        pass

class employee_Company:

    def __init__(self, name: str, company: set["employee_Employee"] = None, company2: set["employee_Department"] = None, Company: "employee_Department" = None, Company17: "employee_Employee" = None):
        self.name = name
        self.company = company if company is not None else set()
        self.company2 = company2 if company2 is not None else set()
        self.Company = Company
        self.Company17 = Company17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def company2(self):
        return self.__company2

    @company2.setter
    def company2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Company__company2", None)
        self.__company2 = value if value is not None else set()
        
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
                    

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Company__company", None)
        self.__company = value if value is not None else set()
        
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
    def Company(self):
        return self.__Company

    @Company.setter
    def Company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Company__Company", None)
        self.__Company = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "departments"):
                opp_val = getattr(old_value, "departments", None)
                if opp_val == self:
                    setattr(old_value, "departments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "departments"):
                opp_val = getattr(value, "departments", None)
                setattr(value, "departments", self)

    @property
    def Company17(self):
        return self.__Company17

    @Company17.setter
    def Company17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Company__Company17", None)
        self.__Company17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employees16"):
                opp_val = getattr(old_value, "employees16", None)
                if opp_val == self:
                    setattr(old_value, "employees16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employees16"):
                opp_val = getattr(value, "employees16", None)
                setattr(value, "employees16", self)
