from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class Nurse:

    pass


class Staff:

    pass


class Bill:

    def __init__(self, billno: str, patientname: str, amount: float, pat9: "Patient" = None, receptionist13: "Receptionist" = None):
        self.billno = billno
        self.patientname = patientname
        self.amount = amount
        self.pat9 = pat9
        self.receptionist13 = receptionist13
        
        pass
    @property
    def billno(self):
        return self.__billno
    @billno.setter
    def billno(self, billno: str):
        self.__billno = billno

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount

    @property
    def patientname(self):
        return self.__patientname
    @patientname.setter
    def patientname(self, patientname: str):
        self.__patientname = patientname

    @property
    def receptionist13(self):
        return self.__receptionist13
    @receptionist13.setter
    def receptionist13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__receptionist13", None)
        self.__receptionist13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sbill12"):
                opp_val = getattr(old_value, "sbill12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sbill12"):
                opp_val = getattr(value, "sbill12", None)
                if opp_val is None:
                    setattr(value, "sbill12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pat9(self):
        return self.__pat9
    @pat9.setter
    def pat9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__pat9", None)
        self.__pat9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bill8"):
                opp_val = getattr(old_value, "bill8", None)
                if opp_val == self:
                    setattr(old_value, "bill8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bill8"):
                opp_val = getattr(value, "bill8", None)
                setattr(value, "bill8", self)



class Person(ABC):

    def __init__(self, id: int, name: str, type: str):
        self.id = id
        self.name = name
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

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



class Receptionist:

    def __init__(self, id: int, attribute2: str, p11: "Patient" = None, sbill12: set["Bill"] = None):
        self.id = id
        self.attribute2 = attribute2
        self.p11 = p11
        self.sbill12 = sbill12 if sbill12 is not None else set()
        
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
    def p11(self):
        return self.__p11
    @p11.setter
    def p11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__p11", None)
        self.__p11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "receptionist10"):
                opp_val = getattr(old_value, "receptionist10", None)
                if opp_val == self:
                    setattr(old_value, "receptionist10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "receptionist10"):
                opp_val = getattr(value, "receptionist10", None)
                setattr(value, "receptionist10", self)

    @property
    def sbill12(self):
        return self.__sbill12
    @sbill12.setter
    def sbill12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__sbill12", None)
        self.__sbill12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "receptionist13"):
                    opp_val = getattr(item, "receptionist13", None)
                    
                    if opp_val == self:
                        setattr(item, "receptionist13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "receptionist13"):
                    opp_val = getattr(item, "receptionist13", None)
                    
                    setattr(item, "receptionist13", self)
                    



class Room:

    def __init__(self, location: str, roomno: int, patient5: set["Patient"] = None, staff6: set["Staff"] = None):
        self.location = location
        self.roomno = roomno
        self.patient5 = patient5 if patient5 is not None else set()
        self.staff6 = staff6 if staff6 is not None else set()
        
        pass
    @property
    def roomno(self):
        return self.__roomno
    @roomno.setter
    def roomno(self, roomno: int):
        self.__roomno = roomno

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def patient5(self):
        return self.__patient5
    @patient5.setter
    def patient5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Room__patient5", None)
        self.__patient5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room4"):
                    opp_val = getattr(item, "room4", None)
                    
                    if opp_val == self:
                        setattr(item, "room4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room4"):
                    opp_val = getattr(item, "room4", None)
                    
                    setattr(item, "room4", self)
                    

    @property
    def staff6(self):
        return self.__staff6
    @staff6.setter
    def staff6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Room__staff6", None)
        self.__staff6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room7"):
                    opp_val = getattr(item, "room7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room7"):
                    opp_val = getattr(item, "room7", None)
                    
                    if opp_val is None:
                        setattr(item, "room7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Patient:

    def __init__(self, id: int, name: str, telno: int, address: str, age: int, sex: str, roomno: int, doctors1: set["Doctor"] = None, room4: "Room" = None, bill8: "Bill" = None, receptionist10: "Receptionist" = None):
        self.id = id
        self.name = name
        self.telno = telno
        self.address = address
        self.age = age
        self.sex = sex
        self.roomno = roomno
        self.doctors1 = doctors1 if doctors1 is not None else set()
        self.room4 = room4
        self.bill8 = bill8
        self.receptionist10 = receptionist10
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def telno(self):
        return self.__telno
    @telno.setter
    def telno(self, telno: int):
        self.__telno = telno

    @property
    def roomno(self):
        return self.__roomno
    @roomno.setter
    def roomno(self, roomno: int):
        self.__roomno = roomno

    @property
    def sex(self):
        return self.__sex
    @sex.setter
    def sex(self, sex: str):
        self.__sex = sex

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

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
                    

    @property
    def receptionist10(self):
        return self.__receptionist10
    @receptionist10.setter
    def receptionist10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__receptionist10", None)
        self.__receptionist10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p11"):
                opp_val = getattr(old_value, "p11", None)
                if opp_val == self:
                    setattr(old_value, "p11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p11"):
                opp_val = getattr(value, "p11", None)
                setattr(value, "p11", self)

    @property
    def room4(self):
        return self.__room4
    @room4.setter
    def room4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__room4", None)
        self.__room4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient5"):
                opp_val = getattr(old_value, "patient5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient5"):
                opp_val = getattr(value, "patient5", None)
                if opp_val is None:
                    setattr(value, "patient5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bill8(self):
        return self.__bill8
    @bill8.setter
    def bill8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__bill8", None)
        self.__bill8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pat9"):
                opp_val = getattr(old_value, "pat9", None)
                if opp_val == self:
                    setattr(old_value, "pat9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pat9"):
                opp_val = getattr(value, "pat9", None)
                setattr(value, "pat9", self)



class Department:

    def __init__(self, id: int, name: str, doctorid: int, doctor3: set["Doctor"] = None):
        self.id = id
        self.name = name
        self.doctorid = doctorid
        self.doctor3 = doctor3 if doctor3 is not None else set()
        
        pass
    @property
    def doctorid(self):
        return self.__doctorid
    @doctorid.setter
    def doctorid(self, doctorid: int):
        self.__doctorid = doctorid

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def doctor3(self):
        return self.__doctor3
    @doctor3.setter
    def doctor3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__doctor3", None)
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

    def __init__(self, docid: int, name: str, department: str, specialization: str, phno: int, address: str, patients0: set["Patient"] = None, depmt2: "Department" = None):
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
    def specialization(self):
        return self.__specialization
    @specialization.setter
    def specialization(self, specialization: str):
        self.__specialization = specialization

    @property
    def phno(self):
        return self.__phno
    @phno.setter
    def phno(self, phno: int):
        self.__phno = phno

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
    def docid(self):
        return self.__docid
    @docid.setter
    def docid(self, docid: int):
        self.__docid = docid

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

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
                    

