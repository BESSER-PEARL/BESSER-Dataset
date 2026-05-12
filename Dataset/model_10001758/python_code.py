from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Receiptionist:

    pass


class Room:

    def __init__(self, Room_Rent: str, Room_NO: int, Room_TYPE: str, patient5: set["patient"] = None, nurse7: "Nurse" = None):
        self.Room_Rent = Room_Rent
        self.Room_NO = Room_NO
        self.Room_TYPE = Room_TYPE
        self.patient5 = patient5 if patient5 is not None else set()
        self.nurse7 = nurse7
        
        pass
    @property
    def Room_TYPE(self):
        return self.__Room_TYPE
    @Room_TYPE.setter
    def Room_TYPE(self, Room_TYPE: str):
        self.__Room_TYPE = Room_TYPE

    @property
    def Room_NO(self):
        return self.__Room_NO
    @Room_NO.setter
    def Room_NO(self, Room_NO: int):
        self.__Room_NO = Room_NO

    @property
    def Room_Rent(self):
        return self.__Room_Rent
    @Room_Rent.setter
    def Room_Rent(self, Room_Rent: str):
        self.__Room_Rent = Room_Rent

    @property
    def nurse7(self):
        return self.__nurse7
    @nurse7.setter
    def nurse7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Room__nurse7", None)
        self.__nurse7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room6"):
                opp_val = getattr(old_value, "room6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room6"):
                opp_val = getattr(value, "room6", None)
                if opp_val is None:
                    setattr(value, "room6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def patient5(self):
        return self.__patient5
    @patient5.setter
    def patient5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Room__patient5", None)
        self.__patient5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "room4"):
                    opp_val = getattr(item, "room4", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "room4"):
                    opp_val = getattr(item, "room4", None)
                    
                    if opp_val is None:
                        setattr(item, "room4", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class patient:

    def __init__(self, Patient_ID: int, Patient_Name: str, Patient_Address: str, Patient_Contact_NO: int, DOB: str, Sex: str, Status: str, doctor1: set["Doctor"] = None, receiptionist3: set["Receiptionist"] = None, room4: set["Room"] = None):
        self.Patient_ID = Patient_ID
        self.Patient_Name = Patient_Name
        self.Patient_Address = Patient_Address
        self.Patient_Contact_NO = Patient_Contact_NO
        self.DOB = DOB
        self.Sex = Sex
        self.Status = Status
        self.doctor1 = doctor1 if doctor1 is not None else set()
        self.receiptionist3 = receiptionist3 if receiptionist3 is not None else set()
        self.room4 = room4 if room4 is not None else set()
        
        pass
    @property
    def Patient_Name(self):
        return self.__Patient_Name
    @Patient_Name.setter
    def Patient_Name(self, Patient_Name: str):
        self.__Patient_Name = Patient_Name

    @property
    def DOB(self):
        return self.__DOB
    @DOB.setter
    def DOB(self, DOB: str):
        self.__DOB = DOB

    @property
    def Sex(self):
        return self.__Sex
    @Sex.setter
    def Sex(self, Sex: str):
        self.__Sex = Sex

    @property
    def Patient_ID(self):
        return self.__Patient_ID
    @Patient_ID.setter
    def Patient_ID(self, Patient_ID: int):
        self.__Patient_ID = Patient_ID

    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: str):
        self.__Status = Status

    @property
    def Patient_Address(self):
        return self.__Patient_Address
    @Patient_Address.setter
    def Patient_Address(self, Patient_Address: str):
        self.__Patient_Address = Patient_Address

    @property
    def Patient_Contact_NO(self):
        return self.__Patient_Contact_NO
    @Patient_Contact_NO.setter
    def Patient_Contact_NO(self, Patient_Contact_NO: int):
        self.__Patient_Contact_NO = Patient_Contact_NO

    @property
    def receiptionist3(self):
        return self.__receiptionist3
    @receiptionist3.setter
    def receiptionist3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_patient__receiptionist3", None)
        self.__receiptionist3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patient2"):
                    opp_val = getattr(item, "patient2", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patient2"):
                    opp_val = getattr(item, "patient2", None)
                    
                    if opp_val is None:
                        setattr(item, "patient2", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def room4(self):
        return self.__room4
    @room4.setter
    def room4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_patient__room4", None)
        self.__room4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patient5"):
                    opp_val = getattr(item, "patient5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patient5"):
                    opp_val = getattr(item, "patient5", None)
                    
                    if opp_val is None:
                        setattr(item, "patient5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def doctor1(self):
        return self.__doctor1
    @doctor1.setter
    def doctor1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_patient__doctor1", None)
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

    pass


class Nurse:

    pass


class Employee:

    def __init__(self, Emp_ID: int, Emp_Name: str, Contact_NO: int, Address: str, Salary: str, Designation: str, Joindate: str):
        self.Emp_ID = Emp_ID
        self.Emp_Name = Emp_Name
        self.Contact_NO = Contact_NO
        self.Address = Address
        self.Salary = Salary
        self.Designation = Designation
        self.Joindate = Joindate
        
        pass
    @property
    def Joindate(self):
        return self.__Joindate
    @Joindate.setter
    def Joindate(self, Joindate: str):
        self.__Joindate = Joindate

    @property
    def Emp_Name(self):
        return self.__Emp_Name
    @Emp_Name.setter
    def Emp_Name(self, Emp_Name: str):
        self.__Emp_Name = Emp_Name

    @property
    def Designation(self):
        return self.__Designation
    @Designation.setter
    def Designation(self, Designation: str):
        self.__Designation = Designation

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Emp_ID(self):
        return self.__Emp_ID
    @Emp_ID.setter
    def Emp_ID(self, Emp_ID: int):
        self.__Emp_ID = Emp_ID

    @property
    def Contact_NO(self):
        return self.__Contact_NO
    @Contact_NO.setter
    def Contact_NO(self, Contact_NO: int):
        self.__Contact_NO = Contact_NO

    @property
    def Salary(self):
        return self.__Salary
    @Salary.setter
    def Salary(self, Salary: str):
        self.__Salary = Salary

