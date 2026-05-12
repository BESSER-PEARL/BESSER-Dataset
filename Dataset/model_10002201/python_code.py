from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Staff:

    def __init__(self, Type: str, Id: int, Staff_name: str, rooms13: "Rooms" = None):
        self.Type = Type
        self.Id = Id
        self.Staff_name = Staff_name
        self.rooms13 = rooms13
        
        pass
    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Staff_name(self):
        return self.__Staff_name
    @Staff_name.setter
    def Staff_name(self, Staff_name: str):
        self.__Staff_name = Staff_name

    @property
    def rooms13(self):
        return self.__rooms13
    @rooms13.setter
    def rooms13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__rooms13", None)
        self.__rooms13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff12"):
                opp_val = getattr(old_value, "staff12", None)
                if opp_val == self:
                    setattr(old_value, "staff12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff12"):
                opp_val = getattr(value, "staff12", None)
                setattr(value, "staff12", self)



class Patient:

    def __init__(self, PhoneNo_: int, Patient_id: int, Name: str, Address: str, Age: int, Sex: str, RoomNo_: int, receptionist3: "Receptionist" = None, doctor4: "Doctor" = None, rooms8: "Rooms" = None, bill10: "Bill" = None):
        self.PhoneNo_ = PhoneNo_
        self.Patient_id = Patient_id
        self.Name = Name
        self.Address = Address
        self.Age = Age
        self.Sex = Sex
        self.RoomNo_ = RoomNo_
        self.receptionist3 = receptionist3
        self.doctor4 = doctor4
        self.rooms8 = rooms8
        self.bill10 = bill10
        
        pass
    @property
    def Age(self):
        return self.__Age
    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age

    @property
    def RoomNo_(self):
        return self.__RoomNo_
    @RoomNo_.setter
    def RoomNo_(self, RoomNo_: int):
        self.__RoomNo_ = RoomNo_

    @property
    def Sex(self):
        return self.__Sex
    @Sex.setter
    def Sex(self, Sex: str):
        self.__Sex = Sex

    @property
    def Patient_id(self):
        return self.__Patient_id
    @Patient_id.setter
    def Patient_id(self, Patient_id: int):
        self.__Patient_id = Patient_id

    @property
    def PhoneNo_(self):
        return self.__PhoneNo_
    @PhoneNo_.setter
    def PhoneNo_(self, PhoneNo_: int):
        self.__PhoneNo_ = PhoneNo_

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
    def bill10(self):
        return self.__bill10
    @bill10.setter
    def bill10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__bill10", None)
        self.__bill10 = value
        
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
    def rooms8(self):
        return self.__rooms8
    @rooms8.setter
    def rooms8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__rooms8", None)
        self.__rooms8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient9"):
                opp_val = getattr(old_value, "patient9", None)
                if opp_val == self:
                    setattr(old_value, "patient9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient9"):
                opp_val = getattr(value, "patient9", None)
                setattr(value, "patient9", self)

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
    def doctor4(self):
        return self.__doctor4
    @doctor4.setter
    def doctor4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__doctor4", None)
        self.__doctor4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient5"):
                opp_val = getattr(old_value, "patient5", None)
                if opp_val == self:
                    setattr(old_value, "patient5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient5"):
                opp_val = getattr(value, "patient5", None)
                setattr(value, "patient5", self)



class Bill:

    def __init__(self, BillNo_: str, PatientName: str, Amount: int, receptionist0: "Receptionist" = None, patient11: "Patient" = None):
        self.BillNo_ = BillNo_
        self.PatientName = PatientName
        self.Amount = Amount
        self.receptionist0 = receptionist0
        self.patient11 = patient11
        
        pass
    @property
    def PatientName(self):
        return self.__PatientName
    @PatientName.setter
    def PatientName(self, PatientName: str):
        self.__PatientName = PatientName

    @property
    def BillNo_(self):
        return self.__BillNo_
    @BillNo_.setter
    def BillNo_(self, BillNo_: str):
        self.__BillNo_ = BillNo_

    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: int):
        self.__Amount = Amount

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
            if hasattr(old_value, "bill10"):
                opp_val = getattr(old_value, "bill10", None)
                if opp_val == self:
                    setattr(old_value, "bill10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bill10"):
                opp_val = getattr(value, "bill10", None)
                setattr(value, "bill10", self)

    @property
    def receptionist0(self):
        return self.__receptionist0
    @receptionist0.setter
    def receptionist0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__receptionist0", None)
        self.__receptionist0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Class_Receptionist_11"):
                opp_val = getattr(old_value, "Class_Receptionist_11", None)
                if opp_val == self:
                    setattr(old_value, "Class_Receptionist_11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Class_Receptionist_11"):
                opp_val = getattr(value, "Class_Receptionist_11", None)
                setattr(value, "Class_Receptionist_11", self)



class Dept:

    def __init__(self, Id: int, Name: str, Doc_id: int, doctor7: "Doctor" = None):
        self.Id = Id
        self.Name = Name
        self.Doc_id = Doc_id
        self.doctor7 = doctor7
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def Doc_id(self):
        return self.__Doc_id
    @Doc_id.setter
    def Doc_id(self, Doc_id: int):
        self.__Doc_id = Doc_id

    @property
    def doctor7(self):
        return self.__doctor7
    @doctor7.setter
    def doctor7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dept__doctor7", None)
        self.__doctor7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dept6"):
                opp_val = getattr(old_value, "dept6", None)
                if opp_val == self:
                    setattr(old_value, "dept6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dept6"):
                opp_val = getattr(value, "dept6", None)
                setattr(value, "dept6", self)



class Doctor:

    def __init__(self, Doct_id: int, DocName: str, Dept: str, Specialization: str, PhoneNo_: int, Location: str, patient5: "Patient" = None, dept6: "Dept" = None):
        self.Doct_id = Doct_id
        self.DocName = DocName
        self.Dept = Dept
        self.Specialization = Specialization
        self.PhoneNo_ = PhoneNo_
        self.Location = Location
        self.patient5 = patient5
        self.dept6 = dept6
        
        pass
    @property
    def Specialization(self):
        return self.__Specialization
    @Specialization.setter
    def Specialization(self, Specialization: str):
        self.__Specialization = Specialization

    @property
    def Location(self):
        return self.__Location
    @Location.setter
    def Location(self, Location: str):
        self.__Location = Location

    @property
    def Doct_id(self):
        return self.__Doct_id
    @Doct_id.setter
    def Doct_id(self, Doct_id: int):
        self.__Doct_id = Doct_id

    @property
    def PhoneNo_(self):
        return self.__PhoneNo_
    @PhoneNo_.setter
    def PhoneNo_(self, PhoneNo_: int):
        self.__PhoneNo_ = PhoneNo_

    @property
    def Dept(self):
        return self.__Dept
    @Dept.setter
    def Dept(self, Dept: str):
        self.__Dept = Dept

    @property
    def DocName(self):
        return self.__DocName
    @DocName.setter
    def DocName(self, DocName: str):
        self.__DocName = DocName

    @property
    def patient5(self):
        return self.__patient5
    @patient5.setter
    def patient5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__patient5", None)
        self.__patient5 = value
        
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
            if hasattr(old_value, "doctor7"):
                opp_val = getattr(old_value, "doctor7", None)
                if opp_val == self:
                    setattr(old_value, "doctor7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor7"):
                opp_val = getattr(value, "doctor7", None)
                setattr(value, "doctor7", self)



class Rooms:

    def __init__(self, Roomno_: int, Location: str, patient9: "Patient" = None, staff12: "Staff" = None):
        self.Roomno_ = Roomno_
        self.Location = Location
        self.patient9 = patient9
        self.staff12 = staff12
        
        pass
    @property
    def Location(self):
        return self.__Location
    @Location.setter
    def Location(self, Location: str):
        self.__Location = Location

    @property
    def Roomno_(self):
        return self.__Roomno_
    @Roomno_.setter
    def Roomno_(self, Roomno_: int):
        self.__Roomno_ = Roomno_

    @property
    def patient9(self):
        return self.__patient9
    @patient9.setter
    def patient9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rooms__patient9", None)
        self.__patient9 = value
        
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

    @property
    def staff12(self):
        return self.__staff12
    @staff12.setter
    def staff12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rooms__staff12", None)
        self.__staff12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rooms13"):
                opp_val = getattr(old_value, "rooms13", None)
                if opp_val == self:
                    setattr(old_value, "rooms13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rooms13"):
                opp_val = getattr(value, "rooms13", None)
                setattr(value, "rooms13", self)



class Receptionist:

    def __init__(self, Receptional_id: int, Name: str, Class_Receptionist_11: "Bill" = None, patient2: "Patient" = None):
        self.Receptional_id = Receptional_id
        self.Name = Name
        self.Class_Receptionist_11 = Class_Receptionist_11
        self.patient2 = patient2
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Receptional_id(self):
        return self.__Receptional_id
    @Receptional_id.setter
    def Receptional_id(self, Receptional_id: int):
        self.__Receptional_id = Receptional_id

    @property
    def Class_Receptionist_11(self):
        return self.__Class_Receptionist_11
    @Class_Receptionist_11.setter
    def Class_Receptionist_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__Class_Receptionist_11", None)
        self.__Class_Receptionist_11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "receptionist0"):
                opp_val = getattr(old_value, "receptionist0", None)
                if opp_val == self:
                    setattr(old_value, "receptionist0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "receptionist0"):
                opp_val = getattr(value, "receptionist0", None)
                setattr(value, "receptionist0", self)

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

