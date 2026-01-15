from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Organization_Skill:

    def __init__(self, Name: str, Organization_Skill: "Organization_Employee" = None):
        self.Name = Name
        self.Organization_Skill = Organization_Skill
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Organization_Skill(self):
        return self.__Organization_Skill

    @Organization_Skill.setter
    def Organization_Skill(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Organization_Skill__Organization_Skill", None)
        self.__Organization_Skill = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Organization_Employee"):
                opp_val = getattr(old_value, "Organization_Employee", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Organization_Employee"):
                opp_val = getattr(value, "Organization_Employee", None)
                if opp_val is None:
                    setattr(value, "Organization_Employee", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Organization_Employee:

    def __init__(self, Name: str, EmpID: str, Address: str, Organization_Employee: set["Organization_Skill"] = None):
        self.Name = Name
        self.EmpID = EmpID
        self.Address = Address
        self.Organization_Employee = Organization_Employee if Organization_Employee is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Address(self) -> str:
        return self.__Address

    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def EmpID(self) -> str:
        return self.__EmpID

    @EmpID.setter
    def EmpID(self, EmpID: str):
        self.__EmpID = EmpID

    @property
    def Organization_Employee(self):
        return self.__Organization_Employee

    @Organization_Employee.setter
    def Organization_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Organization_Employee__Organization_Employee", None)
        self.__Organization_Employee = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Organization_Skill"):
                    opp_val = getattr(item, "Organization_Skill", None)
                    
                    if opp_val == self:
                        setattr(item, "Organization_Skill", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Organization_Skill"):
                    opp_val = getattr(item, "Organization_Skill", None)
                    
                    setattr(item, "Organization_Skill", self)
                    
