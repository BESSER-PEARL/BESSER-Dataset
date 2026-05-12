from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Patient:

    def __init__(self, id: int, name: str, telno: int, address: str, age: int, sex: str, doctors1: set["Doctor"] = None):
        self.id = id
        self.name = name
        self.telno = telno
        self.address = address
        self.age = age
        self.sex = sex
        self.doctors1 = doctors1 if doctors1 is not None else set()
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def telno(self):
        return self.__telno
    @telno.setter
    def telno(self, telno: int):
        self.__telno = telno

    @property
    def sex(self):
        return self.__sex
    @sex.setter
    def sex(self, sex: str):
        self.__sex = sex

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def doctors1(self):
        return self.__doctors1
    @doctors1.setter
    def doctors1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__doctors1", None)
        self.__doctors1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patients0"):
                    opp_val = getattr(item, "patients0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patients0"):
                    opp_val = getattr(item, "patients0", None)
                    
                    if opp_val is None:
                        setattr(item, "patients0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Admin:

    def __init__(self, User_Name: Admin, name: str, Password: str, doctor3: set["Doctor"] = None):
        self.User_Name = User_Name
        self.name = name
        self.Password = Password
        self.doctor3 = doctor3 if doctor3 is not None else set()
        
        pass
    @property
    def User_Name(self):
        return self.__User_Name
    @User_Name.setter
    def User_Name(self, User_Name: Admin):
        self.__User_Name = User_Name

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def doctor3(self):
        return self.__doctor3
    @doctor3.setter
    def doctor3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__doctor3", None)
        self.__doctor3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "depmt2"):
                    opp_val = getattr(item, "depmt2", None)
                    
                    if opp_val == self:
                        setattr(item, "depmt2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "depmt2"):
                    opp_val = getattr(item, "depmt2", None)
                    
                    setattr(item, "depmt2", self)
                    



class Doctor:

    def __init__(self, docid: int, name: str, department: str, specialization: str, phno: int, address: str, patients0: set["Patient"] = None, depmt2: "Admin" = None):
        self.docid = docid
        self.name = name
        self.department = department
        self.specialization = specialization
        self.phno = phno
        self.address = address
        self.patients0 = patients0 if patients0 is not None else set()
        self.depmt2 = depmt2
        
        pass
    @property
    def phno(self):
        return self.__phno
    @phno.setter
    def phno(self, phno: int):
        self.__phno = phno

    @property
    def specialization(self):
        return self.__specialization
    @specialization.setter
    def specialization(self, specialization: str):
        self.__specialization = specialization

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def docid(self):
        return self.__docid
    @docid.setter
    def docid(self, docid: int):
        self.__docid = docid

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def department(self):
        return self.__department
    @department.setter
    def department(self, department: str):
        self.__department = department

    @property
    def depmt2(self):
        return self.__depmt2
    @depmt2.setter
    def depmt2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__depmt2", None)
        self.__depmt2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor3"):
                opp_val = getattr(old_value, "doctor3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor3"):
                opp_val = getattr(value, "doctor3", None)
                if opp_val is None:
                    setattr(value, "doctor3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def patients0(self):
        return self.__patients0
    @patients0.setter
    def patients0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__patients0", None)
        self.__patients0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "doctors1"):
                    opp_val = getattr(item, "doctors1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "doctors1"):
                    opp_val = getattr(item, "doctors1", None)
                    
                    if opp_val is None:
                        setattr(item, "doctors1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

