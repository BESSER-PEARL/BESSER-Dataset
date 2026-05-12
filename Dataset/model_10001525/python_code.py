from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Receptionist:

    def __init__(self, Id: int, Name: str, Email: str, patient3: "Patient" = None, bill4: "Bill" = None):
        self.Id = Id
        self.Name = Name
        self.Email = Email
        self.patient3 = patient3
        self.bill4 = bill4
        
        pass
    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def bill4(self):
        return self.__bill4
    @bill4.setter
    def bill4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__bill4", None)
        self.__bill4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "receptionist5"):
                opp_val = getattr(old_value, "receptionist5", None)
                if opp_val == self:
                    setattr(old_value, "receptionist5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "receptionist5"):
                opp_val = getattr(value, "receptionist5", None)
                setattr(value, "receptionist5", self)

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

    def __init__(self, Id: int, Name: str, PhNo_: int, Address: str, Age: int, WardNo: int, doctor1: "Doctor" = None, receptionist2: "Receptionist" = None, bill6: "Bill" = None, rooms8: "Ward" = None):
        self.Id = Id
        self.Name = Name
        self.PhNo_ = PhNo_
        self.Address = Address
        self.Age = Age
        self.WardNo = WardNo
        self.doctor1 = doctor1
        self.receptionist2 = receptionist2
        self.bill6 = bill6
        self.rooms8 = rooms8
        
        pass
    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def WardNo(self):
        return self.__WardNo
    @WardNo.setter
    def WardNo(self, WardNo: int):
        self.__WardNo = WardNo

    @property
    def Age(self):
        return self.__Age
    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age

    @property
    def PhNo_(self):
        return self.__PhNo_
    @PhNo_.setter
    def PhNo_(self, PhNo_: int):
        self.__PhNo_ = PhNo_

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

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
    def bill6(self):
        return self.__bill6
    @bill6.setter
    def bill6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__bill6", None)
        self.__bill6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient7"):
                opp_val = getattr(old_value, "patient7", None)
                if opp_val == self:
                    setattr(old_value, "patient7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient7"):
                opp_val = getattr(value, "patient7", None)
                setattr(value, "patient7", self)



class Doctor:

    def __init__(self, DocId_: int, Name: str, Department: str, Address: str, Email: str, patient0: "Patient" = None):
        self.DocId_ = DocId_
        self.Name = Name
        self.Department = Department
        self.Address = Address
        self.Email = Email
        self.patient0 = patient0
        
        pass
    @property
    def Department(self):
        return self.__Department
    @Department.setter
    def Department(self, Department: str):
        self.__Department = Department

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def DocId_(self):
        return self.__DocId_
    @DocId_.setter
    def DocId_(self, DocId_: int):
        self.__DocId_ = DocId_

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



class Ward:

    def __init__(self, WardNo: int, Ward_Type: str, patient9: "Patient" = None):
        self.WardNo = WardNo
        self.Ward_Type = Ward_Type
        self.patient9 = patient9
        
        pass
    @property
    def WardNo(self):
        return self.__WardNo
    @WardNo.setter
    def WardNo(self, WardNo: int):
        self.__WardNo = WardNo

    @property
    def Ward_Type(self):
        return self.__Ward_Type
    @Ward_Type.setter
    def Ward_Type(self, Ward_Type: str):
        self.__Ward_Type = Ward_Type

    @property
    def patient9(self):
        return self.__patient9
    @patient9.setter
    def patient9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ward__patient9", None)
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



class Bill:

    def __init__(self, BillNo: str, Patient_Id: int, Amount: str, receptionist5: "Receptionist" = None, patient7: "Patient" = None):
        self.BillNo = BillNo
        self.Patient_Id = Patient_Id
        self.Amount = Amount
        self.receptionist5 = receptionist5
        self.patient7 = patient7
        
        pass
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
    def Patient_Id(self):
        return self.__Patient_Id
    @Patient_Id.setter
    def Patient_Id(self, Patient_Id: int):
        self.__Patient_Id = Patient_Id

    @property
    def patient7(self):
        return self.__patient7
    @patient7.setter
    def patient7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__patient7", None)
        self.__patient7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bill6"):
                opp_val = getattr(old_value, "bill6", None)
                if opp_val == self:
                    setattr(old_value, "bill6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bill6"):
                opp_val = getattr(value, "bill6", None)
                setattr(value, "bill6", self)

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
                if opp_val == self:
                    setattr(old_value, "bill4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bill4"):
                opp_val = getattr(value, "bill4", None)
                setattr(value, "bill4", self)

