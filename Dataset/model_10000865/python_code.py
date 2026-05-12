from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class pay_bills_UseCase:

    pass


class Follow_doc_instrn_UseCase:

    pass


class Consult_the_doctor_UseCase:

    pass


class Takes_Appt_UseCase:

    pass


class Doctor_Actor:

    pass


class Patient_Actor:

    pass





class Doctor:

    def __init__(self, Name: str, Department: str, specialization: str, phno: str, Docid: int, patient0: "Patient" = None, departmnt4: "Departmnt" = None, staff6: "Staff" = None):
        self.Name = Name
        self.Department = Department
        self.specialization = specialization
        self.phno = phno
        self.Docid = Docid
        self.patient0 = patient0
        self.departmnt4 = departmnt4
        self.staff6 = staff6
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def specialization(self):
        return self.__specialization
    @specialization.setter
    def specialization(self, specialization: str):
        self.__specialization = specialization

    @property
    def Docid(self):
        return self.__Docid
    @Docid.setter
    def Docid(self, Docid: int):
        self.__Docid = Docid

    @property
    def Department(self):
        return self.__Department
    @Department.setter
    def Department(self, Department: str):
        self.__Department = Department

    @property
    def phno(self):
        return self.__phno
    @phno.setter
    def phno(self, phno: str):
        self.__phno = phno

    @property
    def departmnt4(self):
        return self.__departmnt4
    @departmnt4.setter
    def departmnt4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__departmnt4", None)
        self.__departmnt4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor5"):
                opp_val = getattr(old_value, "doctor5", None)
                if opp_val == self:
                    setattr(old_value, "doctor5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor5"):
                opp_val = getattr(value, "doctor5", None)
                setattr(value, "doctor5", self)

    @property
    def patient0(self):
        return self.__patient0
    @patient0.setter
    def patient0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__patient0", None)
        self.__patient0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor1"):
                opp_val = getattr(old_value, "doctor1", None)
                if opp_val == self:
                    setattr(old_value, "doctor1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor1"):
                opp_val = getattr(value, "doctor1", None)
                setattr(value, "doctor1", self)

    @property
    def staff6(self):
        return self.__staff6
    @staff6.setter
    def staff6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__staff6", None)
        self.__staff6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rooms7"):
                opp_val = getattr(old_value, "rooms7", None)
                if opp_val == self:
                    setattr(old_value, "rooms7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rooms7"):
                opp_val = getattr(value, "rooms7", None)
                setattr(value, "rooms7", self)



class Staff:

    def __init__(self, id: int, Name: str, type: str, rooms7: "Doctor" = None):
        self.id = id
        self.Name = Name
        self.type = type
        self.rooms7 = rooms7
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def rooms7(self):
        return self.__rooms7
    @rooms7.setter
    def rooms7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__rooms7", None)
        self.__rooms7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff6"):
                opp_val = getattr(old_value, "staff6", None)
                if opp_val == self:
                    setattr(old_value, "staff6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff6"):
                opp_val = getattr(value, "staff6", None)
                setattr(value, "staff6", self)



class Rooms:

    def __init__(self, Roomno: int, location: str, patient8: "Patient" = None):
        self.Roomno = Roomno
        self.location = location
        self.patient8 = patient8
        
        pass
    @property
    def Roomno(self):
        return self.__Roomno
    @Roomno.setter
    def Roomno(self, Roomno: int):
        self.__Roomno = Roomno

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def patient8(self):
        return self.__patient8
    @patient8.setter
    def patient8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rooms__patient8", None)
        self.__patient8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rooms9"):
                opp_val = getattr(old_value, "rooms9", None)
                if opp_val == self:
                    setattr(old_value, "rooms9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rooms9"):
                opp_val = getattr(value, "rooms9", None)
                setattr(value, "rooms9", self)



class Departmnt:

    def __init__(self, id: int, name: str, docid: int, doctor5: "Doctor" = None):
        self.id = id
        self.name = name
        self.docid = docid
        self.doctor5 = doctor5
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def docid(self):
        return self.__docid
    @docid.setter
    def docid(self, docid: int):
        self.__docid = docid

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def doctor5(self):
        return self.__doctor5
    @doctor5.setter
    def doctor5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Departmnt__doctor5", None)
        self.__doctor5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "departmnt4"):
                opp_val = getattr(old_value, "departmnt4", None)
                if opp_val == self:
                    setattr(old_value, "departmnt4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "departmnt4"):
                opp_val = getattr(value, "departmnt4", None)
                setattr(value, "departmnt4", self)



class Receptionist:

    def __init__(self, id: int, Name: str, patient3: "Patient" = None):
        self.id = id
        self.Name = Name
        self.patient3 = patient3
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def patient3(self):
        return self.__patient3
    @patient3.setter
    def patient3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__patient3", None)
        self.__patient3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "receptionist2"):
                opp_val = getattr(old_value, "receptionist2", None)
                if opp_val == self:
                    setattr(old_value, "receptionist2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "receptionist2"):
                opp_val = getattr(value, "receptionist2", None)
                setattr(value, "receptionist2", self)



class Patient:

    def __init__(self, id: int, Sex: str, Name: int, Address: str, TelNo: int, Rno: int, Age: int, doctor1: "Doctor" = None, receptionist2: "Receptionist" = None, rooms9: "Rooms" = None):
        self.id = id
        self.Sex = Sex
        self.Name = Name
        self.Address = Address
        self.TelNo = TelNo
        self.Rno = Rno
        self.Age = Age
        self.doctor1 = doctor1
        self.receptionist2 = receptionist2
        self.rooms9 = rooms9
        
        pass
    @property
    def Sex(self):
        return self.__Sex
    @Sex.setter
    def Sex(self, Sex: str):
        self.__Sex = Sex

    @property
    def TelNo(self):
        return self.__TelNo
    @TelNo.setter
    def TelNo(self, TelNo: int):
        self.__TelNo = TelNo

    @property
    def Age(self):
        return self.__Age
    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Rno(self):
        return self.__Rno
    @Rno.setter
    def Rno(self, Rno: int):
        self.__Rno = Rno

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: int):
        self.__Name = Name

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def receptionist2(self):
        return self.__receptionist2
    @receptionist2.setter
    def receptionist2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__receptionist2", None)
        self.__receptionist2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient3"):
                opp_val = getattr(old_value, "patient3", None)
                if opp_val == self:
                    setattr(old_value, "patient3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient3"):
                opp_val = getattr(value, "patient3", None)
                setattr(value, "patient3", self)

    @property
    def doctor1(self):
        return self.__doctor1
    @doctor1.setter
    def doctor1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__doctor1", None)
        self.__doctor1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient0"):
                opp_val = getattr(old_value, "patient0", None)
                if opp_val == self:
                    setattr(old_value, "patient0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient0"):
                opp_val = getattr(value, "patient0", None)
                setattr(value, "patient0", self)

    @property
    def rooms9(self):
        return self.__rooms9
    @rooms9.setter
    def rooms9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__rooms9", None)
        self.__rooms9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient8"):
                opp_val = getattr(old_value, "patient8", None)
                if opp_val == self:
                    setattr(old_value, "patient8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient8"):
                opp_val = getattr(value, "patient8", None)
                setattr(value, "patient8", self)

