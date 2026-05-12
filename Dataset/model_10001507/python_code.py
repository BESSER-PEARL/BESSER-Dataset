from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Nurse:

    def __init__(self, id: int, attribute2: str, p5: "Patient" = None):
        self.id = id
        self.attribute2 = attribute2
        self.p5 = p5
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def p5(self):
        return self.__p5
    @p5.setter
    def p5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Nurse__p5", None)
        self.__p5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Nurse4"):
                opp_val = getattr(old_value, "Nurse4", None)
                if opp_val == self:
                    setattr(old_value, "Nurse4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Nurse4"):
                opp_val = getattr(value, "Nurse4", None)
                setattr(value, "Nurse4", self)



class Patient:

    def __init__(self, id: int, name: str, telno: int, address: str, age: int, sex: str, doctors1: set["Doctor"] = None, Nurse4: "Nurse" = None):
        self.id = id
        self.name = name
        self.telno = telno
        self.address = address
        self.age = age
        self.sex = sex
        self.doctors1 = doctors1 if doctors1 is not None else set()
        self.Nurse4 = Nurse4
        
        pass
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def telno(self):
        return self.__telno
    @telno.setter
    def telno(self, telno: int):
        self.__telno = telno

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
    def sex(self):
        return self.__sex
    @sex.setter
    def sex(self, sex: str):
        self.__sex = sex

    @property
    def Nurse4(self):
        return self.__Nurse4
    @Nurse4.setter
    def Nurse4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__Nurse4", None)
        self.__Nurse4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p5"):
                opp_val = getattr(old_value, "p5", None)
                if opp_val == self:
                    setattr(old_value, "p5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p5"):
                opp_val = getattr(value, "p5", None)
                setattr(value, "p5", self)

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
                    



class System_Admin:

    def __init__(self, id: int, name: str, adminid: int, doctor3: set["Doctor"] = None):
        self.id = id
        self.name = name
        self.adminid = adminid
        self.doctor3 = doctor3 if doctor3 is not None else set()
        
        pass
    @property
    def adminid(self):
        return self.__adminid
    @adminid.setter
    def adminid(self, adminid: int):
        self.__adminid = adminid

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
    def doctor3(self):
        return self.__doctor3
    @doctor3.setter
    def doctor3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_System_Admin__doctor3", None)
        self.__doctor3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "admin2"):
                    opp_val = getattr(item, "admin2", None)
                    
                    if opp_val == self:
                        setattr(item, "admin2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "admin2"):
                    opp_val = getattr(item, "admin2", None)
                    
                    setattr(item, "admin2", self)
                    



class Doctor:

    def __init__(self, docid: int, name: str, department: str, specialization: str, phno: int, address: str, patients0: set["Patient"] = None, admin2: "System_Admin" = None):
        self.docid = docid
        self.name = name
        self.department = department
        self.specialization = specialization
        self.phno = phno
        self.address = address
        self.patients0 = patients0 if patients0 is not None else set()
        self.admin2 = admin2
        
        pass
    @property
    def specialization(self):
        return self.__specialization
    @specialization.setter
    def specialization(self, specialization: str):
        self.__specialization = specialization

    @property
    def docid(self):
        return self.__docid
    @docid.setter
    def docid(self, docid: int):
        self.__docid = docid

    @property
    def department(self):
        return self.__department
    @department.setter
    def department(self, department: str):
        self.__department = department

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def phno(self):
        return self.__phno
    @phno.setter
    def phno(self, phno: int):
        self.__phno = phno

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

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
                    

    @property
    def admin2(self):
        return self.__admin2
    @admin2.setter
    def admin2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__admin2", None)
        self.__admin2 = value
        
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

