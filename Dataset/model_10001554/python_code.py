from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class system_Component:

    pass


class Float:

    pass


class Dept:

    def __init__(self, Id: int, Name: str, DocId: int, doctor11: set["Doctor"] = None):
        self.Id = Id
        self.Name = Name
        self.DocId = DocId
        self.doctor11 = doctor11 if doctor11 is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def DocId(self):
        return self.__DocId
    @DocId.setter
    def DocId(self, DocId: int):
        self.__DocId = DocId

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def doctor11(self):
        return self.__doctor11
    @doctor11.setter
    def doctor11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Dept__doctor11", None)
        self.__doctor11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dept10"):
                    opp_val = getattr(item, "dept10", None)
                    
                    if opp_val == self:
                        setattr(item, "dept10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dept10"):
                    opp_val = getattr(item, "dept10", None)
                    
                    setattr(item, "dept10", self)
                    



class Rooms:

    def __init__(self, RoomNo: int, Location: str, patient8: "Patient" = None):
        self.RoomNo = RoomNo
        self.Location = Location
        self.patient8 = patient8
        
        pass
    @property
    def Location(self):
        return self.__Location
    @Location.setter
    def Location(self, Location: str):
        self.__Location = Location

    @property
    def RoomNo(self):
        return self.__RoomNo
    @RoomNo.setter
    def RoomNo(self, RoomNo: int):
        self.__RoomNo = RoomNo

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



class Bill:

    def __init__(self, BillId: int, PatientName: str, Amount: Float, patient4: "Patient" = None, receptionList6: "ReceptionList" = None):
        self.BillId = BillId
        self.PatientName = PatientName
        self.Amount = Amount
        self.patient4 = patient4
        self.receptionList6 = receptionList6
        
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
    def Amount(self, Amount: Float):
        self.__Amount = Amount

    @property
    def BillId(self):
        return self.__BillId
    @BillId.setter
    def BillId(self, BillId: int):
        self.__BillId = BillId

    @property
    def patient4(self):
        return self.__patient4
    @patient4.setter
    def patient4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__patient4", None)
        self.__patient4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bill5"):
                opp_val = getattr(old_value, "bill5", None)
                if opp_val == self:
                    setattr(old_value, "bill5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bill5"):
                opp_val = getattr(value, "bill5", None)
                setattr(value, "bill5", self)

    @property
    def receptionList6(self):
        return self.__receptionList6
    @receptionList6.setter
    def receptionList6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__receptionList6", None)
        self.__receptionList6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bill7"):
                opp_val = getattr(old_value, "bill7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bill7"):
                opp_val = getattr(value, "bill7", None)
                if opp_val is None:
                    setattr(value, "bill7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class ReceptionList:

    def __init__(self, RepId: int, name: str, patient3: set["Patient"] = None, bill7: set["Bill"] = None):
        self.RepId = RepId
        self.name = name
        self.patient3 = patient3 if patient3 is not None else set()
        self.bill7 = bill7 if bill7 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def RepId(self):
        return self.__RepId
    @RepId.setter
    def RepId(self, RepId: int):
        self.__RepId = RepId

    @property
    def bill7(self):
        return self.__bill7
    @bill7.setter
    def bill7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ReceptionList__bill7", None)
        self.__bill7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "receptionList6"):
                    opp_val = getattr(item, "receptionList6", None)
                    
                    if opp_val == self:
                        setattr(item, "receptionList6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "receptionList6"):
                    opp_val = getattr(item, "receptionList6", None)
                    
                    setattr(item, "receptionList6", self)
                    

    @property
    def patient3(self):
        return self.__patient3
    @patient3.setter
    def patient3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ReceptionList__patient3", None)
        self.__patient3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "receptionList2"):
                    opp_val = getattr(item, "receptionList2", None)
                    
                    if opp_val == self:
                        setattr(item, "receptionList2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "receptionList2"):
                    opp_val = getattr(item, "receptionList2", None)
                    
                    setattr(item, "receptionList2", self)
                    



class Patient:

    def __init__(self, PatientId: int, PatientName: str, PhoneNo: int, Address: str, Age: int, Sex: str, RoomNo: int, doctor1: set["Doctor"] = None, receptionList2: "ReceptionList" = None, bill5: "Bill" = None, rooms9: "Rooms" = None):
        self.PatientId = PatientId
        self.PatientName = PatientName
        self.PhoneNo = PhoneNo
        self.Address = Address
        self.Age = Age
        self.Sex = Sex
        self.RoomNo = RoomNo
        self.doctor1 = doctor1 if doctor1 is not None else set()
        self.receptionList2 = receptionList2
        self.bill5 = bill5
        self.rooms9 = rooms9
        
        pass
    @property
    def RoomNo(self):
        return self.__RoomNo
    @RoomNo.setter
    def RoomNo(self, RoomNo: int):
        self.__RoomNo = RoomNo

    @property
    def Sex(self):
        return self.__Sex
    @Sex.setter
    def Sex(self, Sex: str):
        self.__Sex = Sex

    @property
    def PhoneNo(self):
        return self.__PhoneNo
    @PhoneNo.setter
    def PhoneNo(self, PhoneNo: int):
        self.__PhoneNo = PhoneNo

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def PatientId(self):
        return self.__PatientId
    @PatientId.setter
    def PatientId(self, PatientId: int):
        self.__PatientId = PatientId

    @property
    def PatientName(self):
        return self.__PatientName
    @PatientName.setter
    def PatientName(self, PatientName: str):
        self.__PatientName = PatientName

    @property
    def Age(self):
        return self.__Age
    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age

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

    @property
    def receptionList2(self):
        return self.__receptionList2
    @receptionList2.setter
    def receptionList2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__receptionList2", None)
        self.__receptionList2 = value
        
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

    @property
    def bill5(self):
        return self.__bill5
    @bill5.setter
    def bill5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__bill5", None)
        self.__bill5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient4"):
                opp_val = getattr(old_value, "patient4", None)
                if opp_val == self:
                    setattr(old_value, "patient4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient4"):
                opp_val = getattr(value, "patient4", None)
                setattr(value, "patient4", self)

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
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patient0"):
                    opp_val = getattr(item, "patient0", None)
                    
                    if opp_val is None:
                        setattr(item, "patient0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Doctor:

    def __init__(self, Dept: str, Specialization: str, PhoneNo: int, Location: str, docId: int, Name: str, patient0: set["Patient"] = None, dept10: "Dept" = None):
        self.Dept = Dept
        self.Specialization = Specialization
        self.PhoneNo = PhoneNo
        self.Location = Location
        self.docId = docId
        self.Name = Name
        self.patient0 = patient0 if patient0 is not None else set()
        self.dept10 = dept10
        
        pass
    @property
    def PhoneNo(self):
        return self.__PhoneNo
    @PhoneNo.setter
    def PhoneNo(self, PhoneNo: int):
        self.__PhoneNo = PhoneNo

    @property
    def Specialization(self):
        return self.__Specialization
    @Specialization.setter
    def Specialization(self, Specialization: str):
        self.__Specialization = Specialization

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Location(self):
        return self.__Location
    @Location.setter
    def Location(self, Location: str):
        self.__Location = Location

    @property
    def docId(self):
        return self.__docId
    @docId.setter
    def docId(self, docId: int):
        self.__docId = docId

    @property
    def Dept(self):
        return self.__Dept
    @Dept.setter
    def Dept(self, Dept: str):
        self.__Dept = Dept

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
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "doctor1"):
                    opp_val = getattr(item, "doctor1", None)
                    
                    if opp_val is None:
                        setattr(item, "doctor1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def dept10(self):
        return self.__dept10
    @dept10.setter
    def dept10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__dept10", None)
        self.__dept10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor11"):
                opp_val = getattr(old_value, "doctor11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor11"):
                opp_val = getattr(value, "doctor11", None)
                if opp_val is None:
                    setattr(value, "doctor11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

