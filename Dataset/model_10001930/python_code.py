from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class ff:

    def __init__(self, fd: int, e13: "e" = None):
        self.fd = fd
        self.e13 = e13
        
        pass
    @property
    def fd(self):
        return self.__fd
    @fd.setter
    def fd(self, fd: int):
        self.__fd = fd

    @property
    def e13(self):
        return self.__e13
    @e13.setter
    def e13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ff__e13", None)
        self.__e13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ff12"):
                opp_val = getattr(old_value, "ff12", None)
                if opp_val == self:
                    setattr(old_value, "ff12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ff12"):
                opp_val = getattr(value, "ff12", None)
                setattr(value, "ff12", self)



class e:

    def __init__(self, ee: int, ff12: "ff" = None):
        self.ee = ee
        self.ff12 = ff12
        
        pass
    @property
    def ee(self):
        return self.__ee
    @ee.setter
    def ee(self, ee: int):
        self.__ee = ee

    @property
    def ff12(self):
        return self.__ff12
    @ff12.setter
    def ff12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e__ff12", None)
        self.__ff12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e13"):
                opp_val = getattr(old_value, "e13", None)
                if opp_val == self:
                    setattr(old_value, "e13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e13"):
                opp_val = getattr(value, "e13", None)
                setattr(value, "e13", self)



class Dept:

    def __init__(self, id: int, DeptName: str, Docid: int, Doctor_Dept_17: set["Doctor"] = None):
        self.id = id
        self.DeptName = DeptName
        self.Docid = Docid
        self.Doctor_Dept_17 = Doctor_Dept_17 if Doctor_Dept_17 is not None else set()
        
        pass
    @property
    def Docid(self):
        return self.__Docid
    @Docid.setter
    def Docid(self, Docid: int):
        self.__Docid = Docid

    @property
    def DeptName(self):
        return self.__DeptName
    @DeptName.setter
    def DeptName(self, DeptName: str):
        self.__DeptName = DeptName

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Doctor_Dept_17(self):
        return self.__Doctor_Dept_17
    @Doctor_Dept_17.setter
    def Doctor_Dept_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dept__Doctor_Dept_17", None)
        self.__Doctor_Dept_17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dept6"):
                    opp_val = getattr(item, "dept6", None)
                    
                    if opp_val == self:
                        setattr(item, "dept6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dept6"):
                    opp_val = getattr(item, "dept6", None)
                    
                    setattr(item, "dept6", self)
                    



class Bill:

    def __init__(self, BillNo: str, PatientName: str, Amt: str, patient11: "Patient" = None, receptionist5: "Receptionist" = None):
        self.BillNo = BillNo
        self.PatientName = PatientName
        self.Amt = Amt
        self.patient11 = patient11
        self.receptionist5 = receptionist5
        
        pass
    @property
    def PatientName(self):
        return self.__PatientName
    @PatientName.setter
    def PatientName(self, PatientName: str):
        self.__PatientName = PatientName

    @property
    def BillNo(self):
        return self.__BillNo
    @BillNo.setter
    def BillNo(self, BillNo: str):
        self.__BillNo = BillNo

    @property
    def Amt(self):
        return self.__Amt
    @Amt.setter
    def Amt(self, Amt: str):
        self.__Amt = Amt

    @property
    def patient11(self):
        return self.__patient11
    @patient11.setter
    def patient11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__patient11", None)
        self.__patient11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Patient_Bill_010"):
                opp_val = getattr(old_value, "Patient_Bill_010", None)
                if opp_val == self:
                    setattr(old_value, "Patient_Bill_010", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Patient_Bill_010"):
                opp_val = getattr(value, "Patient_Bill_010", None)
                setattr(value, "Patient_Bill_010", self)

    @property
    def receptionist5(self):
        return self.__receptionist5
    @receptionist5.setter
    def receptionist5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__receptionist5", None)
        self.__receptionist5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bill4"):
                opp_val = getattr(old_value, "bill4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bill4"):
                opp_val = getattr(value, "bill4", None)
                if opp_val is None:
                    setattr(value, "bill4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Rooms:

    def __init__(self, RoomNo: int, Location: str, Patient_Rooms_19: "Patient" = None):
        self.RoomNo = RoomNo
        self.Location = Location
        self.Patient_Rooms_19 = Patient_Rooms_19
        
        pass
    @property
    def RoomNo(self):
        return self.__RoomNo
    @RoomNo.setter
    def RoomNo(self, RoomNo: int):
        self.__RoomNo = RoomNo

    @property
    def Location(self):
        return self.__Location
    @Location.setter
    def Location(self, Location: str):
        self.__Location = Location

    @property
    def Patient_Rooms_19(self):
        return self.__Patient_Rooms_19
    @Patient_Rooms_19.setter
    def Patient_Rooms_19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rooms__Patient_Rooms_19", None)
        self.__Patient_Rooms_19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rooms8"):
                opp_val = getattr(old_value, "rooms8", None)
                if opp_val == self:
                    setattr(old_value, "rooms8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rooms8"):
                opp_val = getattr(value, "rooms8", None)
                setattr(value, "rooms8", self)



class Receptionist:

    def __init__(self, Receptionid: int, RecName: str, patient3: set["Patient"] = None, bill4: set["Bill"] = None):
        self.Receptionid = Receptionid
        self.RecName = RecName
        self.patient3 = patient3 if patient3 is not None else set()
        self.bill4 = bill4 if bill4 is not None else set()
        
        pass
    @property
    def Receptionid(self):
        return self.__Receptionid
    @Receptionid.setter
    def Receptionid(self, Receptionid: int):
        self.__Receptionid = Receptionid

    @property
    def RecName(self):
        return self.__RecName
    @RecName.setter
    def RecName(self, RecName: str):
        self.__RecName = RecName

    @property
    def bill4(self):
        return self.__bill4
    @bill4.setter
    def bill4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__bill4", None)
        self.__bill4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "receptionist5"):
                    opp_val = getattr(item, "receptionist5", None)
                    
                    if opp_val == self:
                        setattr(item, "receptionist5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "receptionist5"):
                    opp_val = getattr(item, "receptionist5", None)
                    
                    setattr(item, "receptionist5", self)
                    

    @property
    def patient3(self):
        return self.__patient3
    @patient3.setter
    def patient3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__patient3", None)
        self.__patient3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "receptionist2"):
                    opp_val = getattr(item, "receptionist2", None)
                    
                    if opp_val == self:
                        setattr(item, "receptionist2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "receptionist2"):
                    opp_val = getattr(item, "receptionist2", None)
                    
                    setattr(item, "receptionist2", self)
                    



class Patient:

    def __init__(self, Age: int, Sex: str, RoomNo: int, Patientid: int, PatientName: str, PhoneNo: int, Address: str, rooms8: "Rooms" = None, Patient_Bill_010: "Bill" = None, doctor1: "Doctor" = None, receptionist2: "Receptionist" = None):
        self.Age = Age
        self.Sex = Sex
        self.RoomNo = RoomNo
        self.Patientid = Patientid
        self.PatientName = PatientName
        self.PhoneNo = PhoneNo
        self.Address = Address
        self.rooms8 = rooms8
        self.Patient_Bill_010 = Patient_Bill_010
        self.doctor1 = doctor1
        self.receptionist2 = receptionist2
        
        pass
    @property
    def Age(self):
        return self.__Age
    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age

    @property
    def PhoneNo(self):
        return self.__PhoneNo
    @PhoneNo.setter
    def PhoneNo(self, PhoneNo: int):
        self.__PhoneNo = PhoneNo

    @property
    def Sex(self):
        return self.__Sex
    @Sex.setter
    def Sex(self, Sex: str):
        self.__Sex = Sex

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def PatientName(self):
        return self.__PatientName
    @PatientName.setter
    def PatientName(self, PatientName: str):
        self.__PatientName = PatientName

    @property
    def RoomNo(self):
        return self.__RoomNo
    @RoomNo.setter
    def RoomNo(self, RoomNo: int):
        self.__RoomNo = RoomNo

    @property
    def Patientid(self):
        return self.__Patientid
    @Patientid.setter
    def Patientid(self, Patientid: int):
        self.__Patientid = Patientid

    @property
    def Patient_Bill_010(self):
        return self.__Patient_Bill_010
    @Patient_Bill_010.setter
    def Patient_Bill_010(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__Patient_Bill_010", None)
        self.__Patient_Bill_010 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient11"):
                opp_val = getattr(old_value, "patient11", None)
                if opp_val == self:
                    setattr(old_value, "patient11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient11"):
                opp_val = getattr(value, "patient11", None)
                setattr(value, "patient11", self)

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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient0"):
                opp_val = getattr(value, "patient0", None)
                if opp_val is None:
                    setattr(value, "patient0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def rooms8(self):
        return self.__rooms8
    @rooms8.setter
    def rooms8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__rooms8", None)
        self.__rooms8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Patient_Rooms_19"):
                opp_val = getattr(old_value, "Patient_Rooms_19", None)
                if opp_val == self:
                    setattr(old_value, "Patient_Rooms_19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Patient_Rooms_19"):
                opp_val = getattr(value, "Patient_Rooms_19", None)
                setattr(value, "Patient_Rooms_19", self)

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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient3"):
                opp_val = getattr(value, "patient3", None)
                if opp_val is None:
                    setattr(value, "patient3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Doctor:

    def __init__(self, Docid: int, DocName: str, Dept: str, Specialization: str, Phoneno: str, Location: str, patient0: set["Patient"] = None, dept6: "Dept" = None):
        self.Docid = Docid
        self.DocName = DocName
        self.Dept = Dept
        self.Specialization = Specialization
        self.Phoneno = Phoneno
        self.Location = Location
        self.patient0 = patient0 if patient0 is not None else set()
        self.dept6 = dept6
        
        pass
    @property
    def DocName(self):
        return self.__DocName
    @DocName.setter
    def DocName(self, DocName: str):
        self.__DocName = DocName

    @property
    def Specialization(self):
        return self.__Specialization
    @Specialization.setter
    def Specialization(self, Specialization: str):
        self.__Specialization = Specialization

    @property
    def Dept(self):
        return self.__Dept
    @Dept.setter
    def Dept(self, Dept: str):
        self.__Dept = Dept

    @property
    def Phoneno(self):
        return self.__Phoneno
    @Phoneno.setter
    def Phoneno(self, Phoneno: str):
        self.__Phoneno = Phoneno

    @property
    def Location(self):
        return self.__Location
    @Location.setter
    def Location(self, Location: str):
        self.__Location = Location

    @property
    def Docid(self):
        return self.__Docid
    @Docid.setter
    def Docid(self, Docid: int):
        self.__Docid = Docid

    @property
    def dept6(self):
        return self.__dept6
    @dept6.setter
    def dept6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__dept6", None)
        self.__dept6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Doctor_Dept_17"):
                opp_val = getattr(old_value, "Doctor_Dept_17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Doctor_Dept_17"):
                opp_val = getattr(value, "Doctor_Dept_17", None)
                if opp_val is None:
                    setattr(value, "Doctor_Dept_17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def patient0(self):
        return self.__patient0
    @patient0.setter
    def patient0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__patient0", None)
        self.__patient0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "doctor1"):
                    opp_val = getattr(item, "doctor1", None)
                    
                    if opp_val == self:
                        setattr(item, "doctor1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "doctor1"):
                    opp_val = getattr(item, "doctor1", None)
                    
                    setattr(item, "doctor1", self)
                    

