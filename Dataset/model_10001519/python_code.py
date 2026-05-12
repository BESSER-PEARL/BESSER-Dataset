from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Receptionist:

    pass


class Bill:

    def __init__(self, BillNo: int, patientName: str, amount: int, patient9: "Patient" = None, generates_bill11: "Receptionist" = None):
        self.BillNo = BillNo
        self.patientName = patientName
        self.amount = amount
        self.patient9 = patient9
        self.generates_bill11 = generates_bill11
        
        pass
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount

    @property
    def BillNo(self):
        return self.__BillNo
    @BillNo.setter
    def BillNo(self, BillNo: int):
        self.__BillNo = BillNo

    @property
    def patientName(self):
        return self.__patientName
    @patientName.setter
    def patientName(self, patientName: str):
        self.__patientName = patientName

    @property
    def generates_bill11(self):
        return self.__generates_bill11
    @generates_bill11.setter
    def generates_bill11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__generates_bill11", None)
        self.__generates_bill11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bill10"):
                opp_val = getattr(old_value, "bill10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bill10"):
                opp_val = getattr(value, "bill10", None)
                if opp_val is None:
                    setattr(value, "bill10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def patient9(self):
        return self.__patient9
    @patient9.setter
    def patient9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__patient9", None)
        self.__patient9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pays_bill8"):
                opp_val = getattr(old_value, "pays_bill8", None)
                if opp_val == self:
                    setattr(old_value, "pays_bill8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pays_bill8"):
                opp_val = getattr(value, "pays_bill8", None)
                setattr(value, "pays_bill8", self)



class Department:

    def __init__(self, deptID: str, Name: str, DocID: str, belongs_to3: set["Doctor"] = None):
        self.deptID = deptID
        self.Name = Name
        self.DocID = DocID
        self.belongs_to3 = belongs_to3 if belongs_to3 is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def deptID(self):
        return self.__deptID
    @deptID.setter
    def deptID(self, deptID: str):
        self.__deptID = deptID

    @property
    def DocID(self):
        return self.__DocID
    @DocID.setter
    def DocID(self, DocID: str):
        self.__DocID = DocID

    @property
    def belongs_to3(self):
        return self.__belongs_to3
    @belongs_to3.setter
    def belongs_to3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__belongs_to3", None)
        self.__belongs_to3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "department2"):
                    opp_val = getattr(item, "department2", None)
                    
                    if opp_val == self:
                        setattr(item, "department2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "department2"):
                    opp_val = getattr(item, "department2", None)
                    
                    setattr(item, "department2", self)
                    



class Ward:

    def __init__(self, wardNo: int, Location: str, patient7: "Patient" = None):
        self.wardNo = wardNo
        self.Location = Location
        self.patient7 = patient7
        
        pass
    @property
    def wardNo(self):
        return self.__wardNo
    @wardNo.setter
    def wardNo(self, wardNo: int):
        self.__wardNo = wardNo

    @property
    def Location(self):
        return self.__Location
    @Location.setter
    def Location(self, Location: str):
        self.__Location = Location

    @property
    def patient7(self):
        return self.__patient7
    @patient7.setter
    def patient7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ward__patient7", None)
        self.__patient7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "alloted_to6"):
                opp_val = getattr(old_value, "alloted_to6", None)
                if opp_val == self:
                    setattr(old_value, "alloted_to6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "alloted_to6"):
                opp_val = getattr(value, "alloted_to6", None)
                setattr(value, "alloted_to6", self)



class Patient:

    def __init__(self, PatientID: int, Name: str, Address: str, Age: str, WardNo: int, Gender: str, doctor1: "Doctor" = None, give_appointment4: "Receptionist" = None, alloted_to6: "Ward" = None, pays_bill8: "Bill" = None):
        self.PatientID = PatientID
        self.Name = Name
        self.Address = Address
        self.Age = Age
        self.WardNo = WardNo
        self.Gender = Gender
        self.doctor1 = doctor1
        self.give_appointment4 = give_appointment4
        self.alloted_to6 = alloted_to6
        self.pays_bill8 = pays_bill8
        
        pass
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
    def Age(self, Age: str):
        self.__Age = Age

    @property
    def Gender(self):
        return self.__Gender
    @Gender.setter
    def Gender(self, Gender: str):
        self.__Gender = Gender

    @property
    def PatientID(self):
        return self.__PatientID
    @PatientID.setter
    def PatientID(self, PatientID: int):
        self.__PatientID = PatientID

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def pays_bill8(self):
        return self.__pays_bill8
    @pays_bill8.setter
    def pays_bill8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__pays_bill8", None)
        self.__pays_bill8 = value
        
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
    def doctor1(self):
        return self.__doctor1
    @doctor1.setter
    def doctor1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__doctor1", None)
        self.__doctor1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "checks0"):
                opp_val = getattr(old_value, "checks0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "checks0"):
                opp_val = getattr(value, "checks0", None)
                if opp_val is None:
                    setattr(value, "checks0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def give_appointment4(self):
        return self.__give_appointment4
    @give_appointment4.setter
    def give_appointment4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__give_appointment4", None)
        self.__give_appointment4 = value
        
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
    def alloted_to6(self):
        return self.__alloted_to6
    @alloted_to6.setter
    def alloted_to6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__alloted_to6", None)
        self.__alloted_to6 = value
        
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

    def __init__(self, DocID: str, Name: str, Department: str, Specialization: int, PhoneNumber: int, Address: str, checks0: set["Patient"] = None, department2: "Department" = None):
        self.DocID = DocID
        self.Name = Name
        self.Department = Department
        self.Specialization = Specialization
        self.PhoneNumber = PhoneNumber
        self.Address = Address
        self.checks0 = checks0 if checks0 is not None else set()
        self.department2 = department2
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def PhoneNumber(self):
        return self.__PhoneNumber
    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber: int):
        self.__PhoneNumber = PhoneNumber

    @property
    def DocID(self):
        return self.__DocID
    @DocID.setter
    def DocID(self, DocID: str):
        self.__DocID = DocID

    @property
    def Department(self):
        return self.__Department
    @Department.setter
    def Department(self, Department: str):
        self.__Department = Department

    @property
    def Specialization(self):
        return self.__Specialization
    @Specialization.setter
    def Specialization(self, Specialization: int):
        self.__Specialization = Specialization

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def department2(self):
        return self.__department2
    @department2.setter
    def department2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__department2", None)
        self.__department2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "belongs_to3"):
                opp_val = getattr(old_value, "belongs_to3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "belongs_to3"):
                opp_val = getattr(value, "belongs_to3", None)
                if opp_val is None:
                    setattr(value, "belongs_to3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def checks0(self):
        return self.__checks0
    @checks0.setter
    def checks0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__checks0", None)
        self.__checks0 = value if value is not None else set()
        
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
                    

