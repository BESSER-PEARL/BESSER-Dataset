from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class _101companies_Employee:

    def __init__(self, name: str, address: str, salary: float, _101companies_Employee5: "_101companies_Department" = None, _101companies_Employee: "_101companies_Department" = None):
        self.name = name
        self.address = address
        self.salary = salary
        self._101companies_Employee5 = _101companies_Employee5
        self._101companies_Employee = _101companies_Employee
        
    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, salary: float):
        self.__salary = salary

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def _101companies_Employee(self):
        return self.___101companies_Employee

    @_101companies_Employee.setter
    def _101companies_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__101companies_Employee___101companies_Employee", None)
        self.___101companies_Employee = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_101companies_Department2"):
                opp_val = getattr(old_value, "_101companies_Department2", None)
                if opp_val == self:
                    setattr(old_value, "_101companies_Department2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_101companies_Department2"):
                opp_val = getattr(value, "_101companies_Department2", None)
                setattr(value, "_101companies_Department2", self)

    @property
    def _101companies_Employee5(self):
        return self.___101companies_Employee5

    @_101companies_Employee5.setter
    def _101companies_Employee5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__101companies_Employee___101companies_Employee5", None)
        self.___101companies_Employee5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_101companies_Department4"):
                opp_val = getattr(old_value, "_101companies_Department4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_101companies_Department4"):
                opp_val = getattr(value, "_101companies_Department4", None)
                if opp_val is None:
                    setattr(value, "_101companies_Department4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class _101companies_Department:

    def __init__(self, name: str, totalSalary: float, _101companies_Department4: set["_101companies_Employee"] = None, _101companies_Department: "_101companies_Company" = None, _101companies_Department2: "_101companies_Employee" = None, _101companies_Department8: "_101companies_Department" = None, _101companies_Department6: set["_101companies_Department"] = None):
        self.name = name
        self.totalSalary = totalSalary
        self._101companies_Department4 = _101companies_Department4 if _101companies_Department4 is not None else set()
        self._101companies_Department = _101companies_Department
        self._101companies_Department2 = _101companies_Department2
        self._101companies_Department8 = _101companies_Department8
        self._101companies_Department6 = _101companies_Department6 if _101companies_Department6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def totalSalary(self) -> float:
        return self.__totalSalary

    @totalSalary.setter
    def totalSalary(self, totalSalary: float):
        self.__totalSalary = totalSalary

    @property
    def _101companies_Department8(self):
        return self.___101companies_Department8

    @_101companies_Department8.setter
    def _101companies_Department8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__101companies_Department___101companies_Department8", None)
        self.___101companies_Department8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_101companies_Department6"):
                opp_val = getattr(old_value, "_101companies_Department6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_101companies_Department6"):
                opp_val = getattr(value, "_101companies_Department6", None)
                if opp_val is None:
                    setattr(value, "_101companies_Department6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def _101companies_Department(self):
        return self.___101companies_Department

    @_101companies_Department.setter
    def _101companies_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__101companies_Department___101companies_Department", None)
        self.___101companies_Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_101companies_Company"):
                opp_val = getattr(old_value, "_101companies_Company", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_101companies_Company"):
                opp_val = getattr(value, "_101companies_Company", None)
                if opp_val is None:
                    setattr(value, "_101companies_Company", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def _101companies_Department4(self):
        return self.___101companies_Department4

    @_101companies_Department4.setter
    def _101companies_Department4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__101companies_Department___101companies_Department4", None)
        self.___101companies_Department4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "_101companies_Employee5"):
                    opp_val = getattr(item, "_101companies_Employee5", None)
                    
                    if opp_val == self:
                        setattr(item, "_101companies_Employee5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "_101companies_Employee5"):
                    opp_val = getattr(item, "_101companies_Employee5", None)
                    
                    setattr(item, "_101companies_Employee5", self)
                    

    @property
    def _101companies_Department6(self):
        return self.___101companies_Department6

    @_101companies_Department6.setter
    def _101companies_Department6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__101companies_Department___101companies_Department6", None)
        self.___101companies_Department6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "_101companies_Department8"):
                    opp_val = getattr(item, "_101companies_Department8", None)
                    
                    if opp_val == self:
                        setattr(item, "_101companies_Department8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "_101companies_Department8"):
                    opp_val = getattr(item, "_101companies_Department8", None)
                    
                    setattr(item, "_101companies_Department8", self)
                    

    @property
    def _101companies_Department2(self):
        return self.___101companies_Department2

    @_101companies_Department2.setter
    def _101companies_Department2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__101companies_Department___101companies_Department2", None)
        self.___101companies_Department2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_101companies_Employee"):
                opp_val = getattr(old_value, "_101companies_Employee", None)
                if opp_val == self:
                    setattr(old_value, "_101companies_Employee", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_101companies_Employee"):
                opp_val = getattr(value, "_101companies_Employee", None)
                setattr(value, "_101companies_Employee", self)

class _101companies_Company:

    def __init__(self, name: str, totalSalary: float, _101companies_Company: set["_101companies_Department"] = None):
        self.name = name
        self.totalSalary = totalSalary
        self._101companies_Company = _101companies_Company if _101companies_Company is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def totalSalary(self) -> float:
        return self.__totalSalary

    @totalSalary.setter
    def totalSalary(self, totalSalary: float):
        self.__totalSalary = totalSalary

    @property
    def _101companies_Company(self):
        return self.___101companies_Company

    @_101companies_Company.setter
    def _101companies_Company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__101companies_Company___101companies_Company", None)
        self.___101companies_Company = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "_101companies_Department"):
                    opp_val = getattr(item, "_101companies_Department", None)
                    
                    if opp_val == self:
                        setattr(item, "_101companies_Department", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "_101companies_Department"):
                    opp_val = getattr(item, "_101companies_Department", None)
                    
                    setattr(item, "_101companies_Department", self)
                    
