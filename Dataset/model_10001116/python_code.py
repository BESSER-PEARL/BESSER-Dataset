from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Staff:

    def __init__(self, Name: str, Id: int, Type: str, Do_Cleaning13: "Patient" = None):
        self.Name = Name
        self.Id = Id
        self.Type = Type
        self.Do_Cleaning13 = Do_Cleaning13
        
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
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Do_Cleaning13(self):
        return self.__Do_Cleaning13
    @Do_Cleaning13.setter
    def Do_Cleaning13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__Do_Cleaning13", None)
        self.__Do_Cleaning13 = value
        
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



class Rooms:

    def __init__(self, RoomNo: int, WardNo: str, patient11: "Patient" = None):
        self.RoomNo = RoomNo
        self.WardNo = WardNo
        self.patient11 = patient11
        
        pass
    @property
    def RoomNo(self):
        return self.__RoomNo
    @RoomNo.setter
    def RoomNo(self, RoomNo: int):
        self.__RoomNo = RoomNo

    @property
    def WardNo(self):
        return self.__WardNo
    @WardNo.setter
    def WardNo(self, WardNo: str):
        self.__WardNo = WardNo

    @property
    def patient11(self):
        return self.__patient11
    @patient11.setter
    def patient11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rooms__patient11", None)
        self.__patient11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Alloted_To10"):
                opp_val = getattr(old_value, "Alloted_To10", None)
                if opp_val == self:
                    setattr(old_value, "Alloted_To10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Alloted_To10"):
                opp_val = getattr(value, "Alloted_To10", None)
                setattr(value, "Alloted_To10", self)



class Bill:

    def __init__(self, BillNo: str, PatientName: str, Amount: str, patient5: "Patient" = None, receptionsit7: "Receptionsit" = None):
        self.BillNo = BillNo
        self.PatientName = PatientName
        self.Amount = Amount
        self.patient5 = patient5
        self.receptionsit7 = receptionsit7
        
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
    def BillNo(self):
        return self.__BillNo
    @BillNo.setter
    def BillNo(self, BillNo: str):
        self.__BillNo = BillNo

    @property
    def receptionsit7(self):
        return self.__receptionsit7
    @receptionsit7.setter
    def receptionsit7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__receptionsit7", None)
        self.__receptionsit7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Generate_Bills6"):
                opp_val = getattr(old_value, "Generate_Bills6", None)
                if opp_val == self:
                    setattr(old_value, "Generate_Bills6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Generate_Bills6"):
                opp_val = getattr(value, "Generate_Bills6", None)
                setattr(value, "Generate_Bills6", self)

    @property
    def patient5(self):
        return self.__patient5
    @patient5.setter
    def patient5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__patient5", None)
        self.__patient5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pay_Bill4"):
                opp_val = getattr(old_value, "Pay_Bill4", None)
                if opp_val == self:
                    setattr(old_value, "Pay_Bill4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pay_Bill4"):
                opp_val = getattr(value, "Pay_Bill4", None)
                setattr(value, "Pay_Bill4", self)



class Deparment:

    def __init__(self, Name: str, Id: int, PhNo: int, doctor9: "Doctor" = None):
        self.Name = Name
        self.Id = Id
        self.PhNo = PhNo
        self.doctor9 = doctor9
        
        pass
    @property
    def PhNo(self):
        return self.__PhNo
    @PhNo.setter
    def PhNo(self, PhNo: int):
        self.__PhNo = PhNo

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
    def doctor9(self):
        return self.__doctor9
    @doctor9.setter
    def doctor9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Deparment__doctor9", None)
        self.__doctor9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Belongs_To8"):
                opp_val = getattr(old_value, "Belongs_To8", None)
                if opp_val == self:
                    setattr(old_value, "Belongs_To8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Belongs_To8"):
                opp_val = getattr(value, "Belongs_To8", None)
                setattr(value, "Belongs_To8", self)



class Receptionsit:

    def __init__(self, Name: str, Id: int, patient3: "Patient" = None, Generate_Bills6: "Bill" = None):
        self.Name = Name
        self.Id = Id
        self.patient3 = patient3
        self.Generate_Bills6 = Generate_Bills6
        
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
    def Generate_Bills6(self):
        return self.__Generate_Bills6
    @Generate_Bills6.setter
    def Generate_Bills6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionsit__Generate_Bills6", None)
        self.__Generate_Bills6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "receptionsit7"):
                opp_val = getattr(old_value, "receptionsit7", None)
                if opp_val == self:
                    setattr(old_value, "receptionsit7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "receptionsit7"):
                opp_val = getattr(value, "receptionsit7", None)
                setattr(value, "receptionsit7", self)

    @property
    def patient3(self):
        return self.__patient3
    @patient3.setter
    def patient3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionsit__patient3", None)
        self.__patient3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Give_Appointment2"):
                opp_val = getattr(old_value, "Give_Appointment2", None)
                if opp_val == self:
                    setattr(old_value, "Give_Appointment2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Give_Appointment2"):
                opp_val = getattr(value, "Give_Appointment2", None)
                setattr(value, "Give_Appointment2", self)



class Patient:

    def __init__(self, Name: str, PatientId: int, age: int, Give_Appointment2: "Receptionsit" = None, Pay_Bill4: "Bill" = None, Alloted_To10: "Rooms" = None, staff12: "Staff" = None, doctor1: "Doctor" = None):
        self.Name = Name
        self.PatientId = PatientId
        self.age = age
        self.Give_Appointment2 = Give_Appointment2
        self.Pay_Bill4 = Pay_Bill4
        self.Alloted_To10 = Alloted_To10
        self.staff12 = staff12
        self.doctor1 = doctor1
        
        pass
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def PatientId(self):
        return self.__PatientId
    @PatientId.setter
    def PatientId(self, PatientId: int):
        self.__PatientId = PatientId

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Give_Appointment2(self):
        return self.__Give_Appointment2
    @Give_Appointment2.setter
    def Give_Appointment2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__Give_Appointment2", None)
        self.__Give_Appointment2 = value
        
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
    def Pay_Bill4(self):
        return self.__Pay_Bill4
    @Pay_Bill4.setter
    def Pay_Bill4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__Pay_Bill4", None)
        self.__Pay_Bill4 = value
        
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
            if hasattr(old_value, "Checks0"):
                opp_val = getattr(old_value, "Checks0", None)
                if opp_val == self:
                    setattr(old_value, "Checks0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Checks0"):
                opp_val = getattr(value, "Checks0", None)
                setattr(value, "Checks0", self)

    @property
    def Alloted_To10(self):
        return self.__Alloted_To10
    @Alloted_To10.setter
    def Alloted_To10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__Alloted_To10", None)
        self.__Alloted_To10 = value
        
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
    def staff12(self):
        return self.__staff12
    @staff12.setter
    def staff12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__staff12", None)
        self.__staff12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Do_Cleaning13"):
                opp_val = getattr(old_value, "Do_Cleaning13", None)
                if opp_val == self:
                    setattr(old_value, "Do_Cleaning13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Do_Cleaning13"):
                opp_val = getattr(value, "Do_Cleaning13", None)
                setattr(value, "Do_Cleaning13", self)



class Doctor:

    def __init__(self, Name: str, DocId: int, Department: str, Specialization: str, PhNo: int, Belongs_To8: "Deparment" = None, Checks0: "Patient" = None):
        self.Name = Name
        self.DocId = DocId
        self.Department = Department
        self.Specialization = Specialization
        self.PhNo = PhNo
        self.Belongs_To8 = Belongs_To8
        self.Checks0 = Checks0
        
        pass
    @property
    def PhNo(self):
        return self.__PhNo
    @PhNo.setter
    def PhNo(self, PhNo: int):
        self.__PhNo = PhNo

    @property
    def DocId(self):
        return self.__DocId
    @DocId.setter
    def DocId(self, DocId: int):
        self.__DocId = DocId

    @property
    def Specialization(self):
        return self.__Specialization
    @Specialization.setter
    def Specialization(self, Specialization: str):
        self.__Specialization = Specialization

    @property
    def Department(self):
        return self.__Department
    @Department.setter
    def Department(self, Department: str):
        self.__Department = Department

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Belongs_To8(self):
        return self.__Belongs_To8
    @Belongs_To8.setter
    def Belongs_To8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__Belongs_To8", None)
        self.__Belongs_To8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor9"):
                opp_val = getattr(old_value, "doctor9", None)
                if opp_val == self:
                    setattr(old_value, "doctor9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor9"):
                opp_val = getattr(value, "doctor9", None)
                setattr(value, "doctor9", self)

    @property
    def Checks0(self):
        return self.__Checks0
    @Checks0.setter
    def Checks0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__Checks0", None)
        self.__Checks0 = value
        
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

