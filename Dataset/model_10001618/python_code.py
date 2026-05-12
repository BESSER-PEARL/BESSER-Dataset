from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Hospital_Management_System:

    def __init__(self, Name: str, Address: str, Code: str):
        self.Name = Name
        self.Address = Address
        self.Code = Code
        
        pass
    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Code(self):
        return self.__Code
    @Code.setter
    def Code(self, Code: str):
        self.__Code = Code



class Receptionist:

    def __init__(self, ID: int, Name: str, patient2: "Patient" = None, doctor4: set["Doctor"] = None):
        self.ID = ID
        self.Name = Name
        self.patient2 = patient2
        self.doctor4 = doctor4 if doctor4 is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def patient2(self):
        return self.__patient2
    @patient2.setter
    def patient2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__patient2", None)
        self.__patient2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "receptionist3"):
                opp_val = getattr(old_value, "receptionist3", None)
                if opp_val == self:
                    setattr(old_value, "receptionist3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "receptionist3"):
                opp_val = getattr(value, "receptionist3", None)
                setattr(value, "receptionist3", self)

    @property
    def doctor4(self):
        return self.__doctor4
    @doctor4.setter
    def doctor4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__doctor4", None)
        self.__doctor4 = value if value is not None else set()
        
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
                    



class Patient:

    def __init__(self, PatID: int, Name: str, TelNo: int, Address: str, Age: int, Gender: str, RoomNo: int, doctor1: "Doctor" = None, receptionist3: "Receptionist" = None):
        self.PatID = PatID
        self.Name = Name
        self.TelNo = TelNo
        self.Address = Address
        self.Age = Age
        self.Gender = Gender
        self.RoomNo = RoomNo
        self.doctor1 = doctor1
        self.receptionist3 = receptionist3
        
        pass
    @property
    def TelNo(self):
        return self.__TelNo
    @TelNo.setter
    def TelNo(self, TelNo: int):
        self.__TelNo = TelNo

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

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
    def Gender(self):
        return self.__Gender
    @Gender.setter
    def Gender(self, Gender: str):
        self.__Gender = Gender

    @property
    def PatID(self):
        return self.__PatID
    @PatID.setter
    def PatID(self, PatID: int):
        self.__PatID = PatID

    @property
    def Age(self):
        return self.__Age
    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age

    @property
    def receptionist3(self):
        return self.__receptionist3
    @receptionist3.setter
    def receptionist3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__receptionist3", None)
        self.__receptionist3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient2"):
                opp_val = getattr(old_value, "patient2", None)
                if opp_val == self:
                    setattr(old_value, "patient2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient2"):
                opp_val = getattr(value, "patient2", None)
                setattr(value, "patient2", self)

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



class Doctor:

    def __init__(self, DocID: int, Name: str, Department: str, Specialization: str, Phone: int, Address: str, patient0: set["Patient"] = None, receptionist5: "Receptionist" = None):
        self.DocID = DocID
        self.Name = Name
        self.Department = Department
        self.Specialization = Specialization
        self.Phone = Phone
        self.Address = Address
        self.patient0 = patient0 if patient0 is not None else set()
        self.receptionist5 = receptionist5
        
        pass
    @property
    def Department(self):
        return self.__Department
    @Department.setter
    def Department(self, Department: str):
        self.__Department = Department

    @property
    def DocID(self):
        return self.__DocID
    @DocID.setter
    def DocID(self, DocID: int):
        self.__DocID = DocID

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Specialization(self):
        return self.__Specialization
    @Specialization.setter
    def Specialization(self, Specialization: str):
        self.__Specialization = Specialization

    @property
    def Phone(self):
        return self.__Phone
    @Phone.setter
    def Phone(self, Phone: int):
        self.__Phone = Phone

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
                    

    @property
    def receptionist5(self):
        return self.__receptionist5
    @receptionist5.setter
    def receptionist5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__receptionist5", None)
        self.__receptionist5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor4"):
                opp_val = getattr(old_value, "doctor4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor4"):
                opp_val = getattr(value, "doctor4", None)
                if opp_val is None:
                    setattr(value, "doctor4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

