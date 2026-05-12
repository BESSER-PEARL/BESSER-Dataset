from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Nurse:

    def __init__(self, ID: int, Name: str, patient6: "Patient" = None, doctor4: "Doctor" = None):
        self.ID = ID
        self.Name = Name
        self.patient6 = patient6
        self.doctor4 = doctor4
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def patient6(self):
        return self.__patient6
    @patient6.setter
    def patient6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Nurse__patient6", None)
        self.__patient6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nurse7"):
                opp_val = getattr(old_value, "nurse7", None)
                if opp_val == self:
                    setattr(old_value, "nurse7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nurse7"):
                opp_val = getattr(value, "nurse7", None)
                setattr(value, "nurse7", self)

    @property
    def doctor4(self):
        return self.__doctor4
    @doctor4.setter
    def doctor4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Nurse__doctor4", None)
        self.__doctor4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nurse5"):
                opp_val = getattr(old_value, "nurse5", None)
                if opp_val == self:
                    setattr(old_value, "nurse5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nurse5"):
                opp_val = getattr(value, "nurse5", None)
                setattr(value, "nurse5", self)



class Patient:

    def __init__(self, Name: str, PatientID: int, TelephoneNo: str, Address: str, Age: int, Sex: str, RoomNo: int, nurse7: "Nurse" = None, doctor1: set["Doctor"] = None, bill2: "Bill" = None):
        self.Name = Name
        self.PatientID = PatientID
        self.TelephoneNo = TelephoneNo
        self.Address = Address
        self.Age = Age
        self.Sex = Sex
        self.RoomNo = RoomNo
        self.nurse7 = nurse7
        self.doctor1 = doctor1 if doctor1 is not None else set()
        self.bill2 = bill2
        
        pass
    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def RoomNo(self):
        return self.__RoomNo
    @RoomNo.setter
    def RoomNo(self, RoomNo: int):
        self.__RoomNo = RoomNo

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Sex(self):
        return self.__Sex
    @Sex.setter
    def Sex(self, Sex: str):
        self.__Sex = Sex

    @property
    def PatientID(self):
        return self.__PatientID
    @PatientID.setter
    def PatientID(self, PatientID: int):
        self.__PatientID = PatientID

    @property
    def Age(self):
        return self.__Age
    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age

    @property
    def TelephoneNo(self):
        return self.__TelephoneNo
    @TelephoneNo.setter
    def TelephoneNo(self, TelephoneNo: str):
        self.__TelephoneNo = TelephoneNo

    @property
    def nurse7(self):
        return self.__nurse7
    @nurse7.setter
    def nurse7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__nurse7", None)
        self.__nurse7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient6"):
                opp_val = getattr(old_value, "patient6", None)
                if opp_val == self:
                    setattr(old_value, "patient6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient6"):
                opp_val = getattr(value, "patient6", None)
                setattr(value, "patient6", self)

    @property
    def doctor1(self):
        return self.__doctor1
    @doctor1.setter
    def doctor1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__doctor1", None)
        self.__doctor1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patient0"):
                    opp_val = getattr(item, "patient0", None)
                    
                    if opp_val == self:
                        setattr(item, "patient0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patient0"):
                    opp_val = getattr(item, "patient0", None)
                    
                    setattr(item, "patient0", self)
                    

    @property
    def bill2(self):
        return self.__bill2
    @bill2.setter
    def bill2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__bill2", None)
        self.__bill2 = value
        
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



class Bill:

    def __init__(self, PatientName: str, Amount: str, patient3: "Patient" = None):
        self.PatientName = PatientName
        self.Amount = Amount
        self.patient3 = patient3
        
        pass
    @property
    def PatientName(self):
        return self.__PatientName
    @PatientName.setter
    def PatientName(self, PatientName: str):
        self.__PatientName = PatientName

    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: str):
        self.__Amount = Amount

    @property
    def patient3(self):
        return self.__patient3
    @patient3.setter
    def patient3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__patient3", None)
        self.__patient3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bill2"):
                opp_val = getattr(old_value, "bill2", None)
                if opp_val == self:
                    setattr(old_value, "bill2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bill2"):
                opp_val = getattr(value, "bill2", None)
                setattr(value, "bill2", self)



class Doctor:

    def __init__(self, DoctorID: int, Name: str, DepartmentID: int, Specialization: str, attribute: str, PhoneNo: str, Address: str, patient0: "Patient" = None, nurse5: "Nurse" = None):
        self.DoctorID = DoctorID
        self.Name = Name
        self.DepartmentID = DepartmentID
        self.Specialization = Specialization
        self.attribute = attribute
        self.PhoneNo = PhoneNo
        self.Address = Address
        self.patient0 = patient0
        self.nurse5 = nurse5
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def PhoneNo(self):
        return self.__PhoneNo
    @PhoneNo.setter
    def PhoneNo(self, PhoneNo: str):
        self.__PhoneNo = PhoneNo

    @property
    def DoctorID(self):
        return self.__DoctorID
    @DoctorID.setter
    def DoctorID(self, DoctorID: int):
        self.__DoctorID = DoctorID

    @property
    def DepartmentID(self):
        return self.__DepartmentID
    @DepartmentID.setter
    def DepartmentID(self, DepartmentID: int):
        self.__DepartmentID = DepartmentID

    @property
    def Specialization(self):
        return self.__Specialization
    @Specialization.setter
    def Specialization(self, Specialization: str):
        self.__Specialization = Specialization

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor1"):
                opp_val = getattr(value, "doctor1", None)
                if opp_val is None:
                    setattr(value, "doctor1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def nurse5(self):
        return self.__nurse5
    @nurse5.setter
    def nurse5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__nurse5", None)
        self.__nurse5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor4"):
                opp_val = getattr(old_value, "doctor4", None)
                if opp_val == self:
                    setattr(old_value, "doctor4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor4"):
                opp_val = getattr(value, "doctor4", None)
                setattr(value, "doctor4", self)

