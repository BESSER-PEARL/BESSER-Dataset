from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class employee_Employee:

    def __init__(self, name: str, accounts: str, employee_Employee: "employee_Employee" = None, employee_Employee0: "employee_Employee" = None, employee_Employee4: "employee_Employee" = None, employee_Employee2: set["employee_Employee"] = None, employee_Employee7: "employee_Employee" = None, employee_Employee5: set["employee_Employee"] = None):
        self.name = name
        self.accounts = accounts
        self.employee_Employee = employee_Employee
        self.employee_Employee0 = employee_Employee0
        self.employee_Employee4 = employee_Employee4
        self.employee_Employee2 = employee_Employee2 if employee_Employee2 is not None else set()
        self.employee_Employee7 = employee_Employee7
        self.employee_Employee5 = employee_Employee5 if employee_Employee5 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def accounts(self) -> str:
        return self.__accounts

    @accounts.setter
    def accounts(self, accounts: str):
        self.__accounts = accounts

    @property
    def employee_Employee0(self):
        return self.__employee_Employee0

    @employee_Employee0.setter
    def employee_Employee0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee0", None)
        self.__employee_Employee0 = value
        
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
    def employee_Employee4(self):
        return self.__employee_Employee4

    @employee_Employee4.setter
    def employee_Employee4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee4", None)
        self.__employee_Employee4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Employee2"):
                opp_val = getattr(old_value, "employee_Employee2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee2"):
                opp_val = getattr(value, "employee_Employee2", None)
                if opp_val is None:
                    setattr(value, "employee_Employee2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "employee_Employee0"):
                opp_val = getattr(old_value, "employee_Employee0", None)
                if opp_val == self:
                    setattr(old_value, "employee_Employee0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee0"):
                opp_val = getattr(value, "employee_Employee0", None)
                setattr(value, "employee_Employee0", self)

    @property
    def employee_Employee5(self):
        return self.__employee_Employee5

    @employee_Employee5.setter
    def employee_Employee5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee5", None)
        self.__employee_Employee5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee_Employee7"):
                    opp_val = getattr(item, "employee_Employee7", None)
                    
                    if opp_val == self:
                        setattr(item, "employee_Employee7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee_Employee7"):
                    opp_val = getattr(item, "employee_Employee7", None)
                    
                    setattr(item, "employee_Employee7", self)
                    

    @property
    def employee_Employee7(self):
        return self.__employee_Employee7

    @employee_Employee7.setter
    def employee_Employee7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee7", None)
        self.__employee_Employee7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee_Employee5"):
                opp_val = getattr(old_value, "employee_Employee5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee_Employee5"):
                opp_val = getattr(value, "employee_Employee5", None)
                if opp_val is None:
                    setattr(value, "employee_Employee5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def employee_Employee2(self):
        return self.__employee_Employee2

    @employee_Employee2.setter
    def employee_Employee2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_employee_Employee__employee_Employee2", None)
        self.__employee_Employee2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "employee_Employee4"):
                    opp_val = getattr(item, "employee_Employee4", None)
                    
                    if opp_val == self:
                        setattr(item, "employee_Employee4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "employee_Employee4"):
                    opp_val = getattr(item, "employee_Employee4", None)
                    
                    setattr(item, "employee_Employee4", self)
                    
