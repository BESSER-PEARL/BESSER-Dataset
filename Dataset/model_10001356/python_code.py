from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class char_Interface:

    pass


class Staff:

    def __init__(self, ID: int, Name: str, Type: str, Rooms_Staff_113: set["Rooms"] = None):
        self.ID = ID
        self.Name = Name
        self.Type = Type
        self.Rooms_Staff_113 = Rooms_Staff_113 if Rooms_Staff_113 is not None else set()
        
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
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Rooms_Staff_113(self):
        return self.__Rooms_Staff_113
    @Rooms_Staff_113.setter
    def Rooms_Staff_113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__Rooms_Staff_113", None)
        self.__Rooms_Staff_113 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "staff12"):
                    opp_val = getattr(item, "staff12", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "staff12"):
                    opp_val = getattr(item, "staff12", None)
                    
                    if opp_val is None:
                        setattr(item, "staff12", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Rooms:

    def __init__(self, Room_No: int, Location: str, Patient_Rooms_19: set["Patient"] = None, staff12: set["Staff"] = None):
        self.Room_No = Room_No
        self.Location = Location
        self.Patient_Rooms_19 = Patient_Rooms_19 if Patient_Rooms_19 is not None else set()
        self.staff12 = staff12 if staff12 is not None else set()
        
        pass
    @property
    def Location(self):
        return self.__Location
    @Location.setter
    def Location(self, Location: str):
        self.__Location = Location

    @property
    def Room_No(self):
        return self.__Room_No
    @Room_No.setter
    def Room_No(self, Room_No: int):
        self.__Room_No = Room_No

    @property
    def Patient_Rooms_19(self):
        return self.__Patient_Rooms_19
    @Patient_Rooms_19.setter
    def Patient_Rooms_19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rooms__Patient_Rooms_19", None)
        self.__Patient_Rooms_19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Patient_Rooms_08"):
                    opp_val = getattr(item, "Patient_Rooms_08", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Patient_Rooms_08"):
                    opp_val = getattr(item, "Patient_Rooms_08", None)
                    
                    if opp_val is None:
                        setattr(item, "Patient_Rooms_08", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def staff12(self):
        return self.__staff12
    @staff12.setter
    def staff12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rooms__staff12", None)
        self.__staff12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Rooms_Staff_113"):
                    opp_val = getattr(item, "Rooms_Staff_113", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Rooms_Staff_113"):
                    opp_val = getattr(item, "Rooms_Staff_113", None)
                    
                    if opp_val is None:
                        setattr(item, "Rooms_Staff_113", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Department:

    def __init__(self, ID: int, Name: str, Doctor_ID: int, Doctor_Department_111: "Doctor" = None):
        self.ID = ID
        self.Name = Name
        self.Doctor_ID = Doctor_ID
        self.Doctor_Department_111 = Doctor_Department_111
        
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
    def Doctor_ID(self):
        return self.__Doctor_ID
    @Doctor_ID.setter
    def Doctor_ID(self, Doctor_ID: int):
        self.__Doctor_ID = Doctor_ID

    @property
    def Doctor_Department_111(self):
        return self.__Doctor_Department_111
    @Doctor_Department_111.setter
    def Doctor_Department_111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__Doctor_Department_111", None)
        self.__Doctor_Department_111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Doctor_Department_010"):
                opp_val = getattr(old_value, "Doctor_Department_010", None)
                if opp_val == self:
                    setattr(old_value, "Doctor_Department_010", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Doctor_Department_010"):
                opp_val = getattr(value, "Doctor_Department_010", None)
                setattr(value, "Doctor_Department_010", self)



class Bill:

    def __init__(self, Bill_No: str, Patient_Name: str, Amount: str, patient5: "Patient" = None, receptionist7: "Receptionist" = None):
        self.Bill_No = Bill_No
        self.Patient_Name = Patient_Name
        self.Amount = Amount
        self.patient5 = patient5
        self.receptionist7 = receptionist7
        
        pass
    @property
    def Bill_No(self):
        return self.__Bill_No
    @Bill_No.setter
    def Bill_No(self, Bill_No: str):
        self.__Bill_No = Bill_No

    @property
    def Patient_Name(self):
        return self.__Patient_Name
    @Patient_Name.setter
    def Patient_Name(self, Patient_Name: str):
        self.__Patient_Name = Patient_Name

    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: str):
        self.__Amount = Amount

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
            if hasattr(old_value, "Patient_Bill_04"):
                opp_val = getattr(old_value, "Patient_Bill_04", None)
                if opp_val == self:
                    setattr(old_value, "Patient_Bill_04", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Patient_Bill_04"):
                opp_val = getattr(value, "Patient_Bill_04", None)
                setattr(value, "Patient_Bill_04", self)

    @property
    def receptionist7(self):
        return self.__receptionist7
    @receptionist7.setter
    def receptionist7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__receptionist7", None)
        self.__receptionist7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bill6"):
                opp_val = getattr(old_value, "bill6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bill6"):
                opp_val = getattr(value, "bill6", None)
                if opp_val is None:
                    setattr(value, "bill6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Doctor:

    def __init__(self, DocID: int, Name: str, Department: str, Specialization: str, PhNo: int, Address: str, Doctor_Patient_00: set["Patient"] = None, Doctor_Department_010: "Department" = None):
        self.DocID = DocID
        self.Name = Name
        self.Department = Department
        self.Specialization = Specialization
        self.PhNo = PhNo
        self.Address = Address
        self.Doctor_Patient_00 = Doctor_Patient_00 if Doctor_Patient_00 is not None else set()
        self.Doctor_Department_010 = Doctor_Department_010
        
        pass
    @property
    def PhNo(self):
        return self.__PhNo
    @PhNo.setter
    def PhNo(self, PhNo: int):
        self.__PhNo = PhNo

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
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Doctor_Patient_00(self):
        return self.__Doctor_Patient_00
    @Doctor_Patient_00.setter
    def Doctor_Patient_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__Doctor_Patient_00", None)
        self.__Doctor_Patient_00 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Doctor_Patient_11"):
                    opp_val = getattr(item, "Doctor_Patient_11", None)
                    
                    if opp_val == self:
                        setattr(item, "Doctor_Patient_11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Doctor_Patient_11"):
                    opp_val = getattr(item, "Doctor_Patient_11", None)
                    
                    setattr(item, "Doctor_Patient_11", self)
                    

    @property
    def Doctor_Department_010(self):
        return self.__Doctor_Department_010
    @Doctor_Department_010.setter
    def Doctor_Department_010(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__Doctor_Department_010", None)
        self.__Doctor_Department_010 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Doctor_Department_111"):
                opp_val = getattr(old_value, "Doctor_Department_111", None)
                if opp_val == self:
                    setattr(old_value, "Doctor_Department_111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Doctor_Department_111"):
                opp_val = getattr(value, "Doctor_Department_111", None)
                setattr(value, "Doctor_Department_111", self)



class Patient:

    def __init__(self, Pid: int, Name: str, TelNO: int, Address: str, Age: int, Sex: int, RoomNo_: int, Doctor_Patient_11: "Doctor" = None, Patient_Receptionist_02: "Receptionist" = None, Patient_Bill_04: "Bill" = None, Patient_Rooms_08: set["Rooms"] = None):
        self.Pid = Pid
        self.Name = Name
        self.TelNO = TelNO
        self.Address = Address
        self.Age = Age
        self.Sex = Sex
        self.RoomNo_ = RoomNo_
        self.Doctor_Patient_11 = Doctor_Patient_11
        self.Patient_Receptionist_02 = Patient_Receptionist_02
        self.Patient_Bill_04 = Patient_Bill_04
        self.Patient_Rooms_08 = Patient_Rooms_08 if Patient_Rooms_08 is not None else set()
        
        pass
    @property
    def Sex(self):
        return self.__Sex
    @Sex.setter
    def Sex(self, Sex: int):
        self.__Sex = Sex

    @property
    def RoomNo_(self):
        return self.__RoomNo_
    @RoomNo_.setter
    def RoomNo_(self, RoomNo_: int):
        self.__RoomNo_ = RoomNo_

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Age(self):
        return self.__Age
    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def TelNO(self):
        return self.__TelNO
    @TelNO.setter
    def TelNO(self, TelNO: int):
        self.__TelNO = TelNO

    @property
    def Pid(self):
        return self.__Pid
    @Pid.setter
    def Pid(self, Pid: int):
        self.__Pid = Pid

    @property
    def Patient_Bill_04(self):
        return self.__Patient_Bill_04
    @Patient_Bill_04.setter
    def Patient_Bill_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__Patient_Bill_04", None)
        self.__Patient_Bill_04 = value
        
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
    def Patient_Receptionist_02(self):
        return self.__Patient_Receptionist_02
    @Patient_Receptionist_02.setter
    def Patient_Receptionist_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__Patient_Receptionist_02", None)
        self.__Patient_Receptionist_02 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Patient_Receptionist_13"):
                opp_val = getattr(old_value, "Patient_Receptionist_13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Patient_Receptionist_13"):
                opp_val = getattr(value, "Patient_Receptionist_13", None)
                if opp_val is None:
                    setattr(value, "Patient_Receptionist_13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Doctor_Patient_11(self):
        return self.__Doctor_Patient_11
    @Doctor_Patient_11.setter
    def Doctor_Patient_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__Doctor_Patient_11", None)
        self.__Doctor_Patient_11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Doctor_Patient_00"):
                opp_val = getattr(old_value, "Doctor_Patient_00", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Doctor_Patient_00"):
                opp_val = getattr(value, "Doctor_Patient_00", None)
                if opp_val is None:
                    setattr(value, "Doctor_Patient_00", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Patient_Rooms_08(self):
        return self.__Patient_Rooms_08
    @Patient_Rooms_08.setter
    def Patient_Rooms_08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__Patient_Rooms_08", None)
        self.__Patient_Rooms_08 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Patient_Rooms_19"):
                    opp_val = getattr(item, "Patient_Rooms_19", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Patient_Rooms_19"):
                    opp_val = getattr(item, "Patient_Rooms_19", None)
                    
                    if opp_val is None:
                        setattr(item, "Patient_Rooms_19", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Receptionist:

    def __init__(self, Rid: str, Rname: str, Patient_Receptionist_13: set["Patient"] = None, bill6: set["Bill"] = None):
        self.Rid = Rid
        self.Rname = Rname
        self.Patient_Receptionist_13 = Patient_Receptionist_13 if Patient_Receptionist_13 is not None else set()
        self.bill6 = bill6 if bill6 is not None else set()
        
        pass
    @property
    def Rname(self):
        return self.__Rname
    @Rname.setter
    def Rname(self, Rname: str):
        self.__Rname = Rname

    @property
    def Rid(self):
        return self.__Rid
    @Rid.setter
    def Rid(self, Rid: str):
        self.__Rid = Rid

    @property
    def bill6(self):
        return self.__bill6
    @bill6.setter
    def bill6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__bill6", None)
        self.__bill6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "receptionist7"):
                    opp_val = getattr(item, "receptionist7", None)
                    
                    if opp_val == self:
                        setattr(item, "receptionist7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "receptionist7"):
                    opp_val = getattr(item, "receptionist7", None)
                    
                    setattr(item, "receptionist7", self)
                    

    @property
    def Patient_Receptionist_13(self):
        return self.__Patient_Receptionist_13
    @Patient_Receptionist_13.setter
    def Patient_Receptionist_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__Patient_Receptionist_13", None)
        self.__Patient_Receptionist_13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Patient_Receptionist_02"):
                    opp_val = getattr(item, "Patient_Receptionist_02", None)
                    
                    if opp_val == self:
                        setattr(item, "Patient_Receptionist_02", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Patient_Receptionist_02"):
                    opp_val = getattr(item, "Patient_Receptionist_02", None)
                    
                    setattr(item, "Patient_Receptionist_02", self)
                    

