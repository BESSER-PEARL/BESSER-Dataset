from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Hospital:

    def __init__(self, HR: str, Operation_Theater: str, Cariology: str):
        self.HR = HR
        self.Operation_Theater = Operation_Theater
        self.Cariology = Cariology
        
        pass
    @property
    def Operation_Theater(self):
        return self.__Operation_Theater
    @Operation_Theater.setter
    def Operation_Theater(self, Operation_Theater: str):
        self.__Operation_Theater = Operation_Theater

    @property
    def Cariology(self):
        return self.__Cariology
    @Cariology.setter
    def Cariology(self, Cariology: str):
        self.__Cariology = Cariology

    @property
    def HR(self):
        return self.__HR
    @HR.setter
    def HR(self, HR: str):
        self.__HR = HR



class Patients:

    def __init__(self, Patient_name: str, NIC_NO: int, Sickness: str, Phone_no: int, docter1: "Docter" = None, receptionist2: "Receptionist" = None):
        self.Patient_name = Patient_name
        self.NIC_NO = NIC_NO
        self.Sickness = Sickness
        self.Phone_no = Phone_no
        self.docter1 = docter1
        self.receptionist2 = receptionist2
        
        pass
    @property
    def NIC_NO(self):
        return self.__NIC_NO
    @NIC_NO.setter
    def NIC_NO(self, NIC_NO: int):
        self.__NIC_NO = NIC_NO

    @property
    def Phone_no(self):
        return self.__Phone_no
    @Phone_no.setter
    def Phone_no(self, Phone_no: int):
        self.__Phone_no = Phone_no

    @property
    def Patient_name(self):
        return self.__Patient_name
    @Patient_name.setter
    def Patient_name(self, Patient_name: str):
        self.__Patient_name = Patient_name

    @property
    def Sickness(self):
        return self.__Sickness
    @Sickness.setter
    def Sickness(self, Sickness: str):
        self.__Sickness = Sickness

    @property
    def receptionist2(self):
        return self.__receptionist2
    @receptionist2.setter
    def receptionist2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patients__receptionist2", None)
        self.__receptionist2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patients3"):
                opp_val = getattr(old_value, "patients3", None)
                if opp_val == self:
                    setattr(old_value, "patients3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patients3"):
                opp_val = getattr(value, "patients3", None)
                setattr(value, "patients3", self)

    @property
    def docter1(self):
        return self.__docter1
    @docter1.setter
    def docter1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patients__docter1", None)
        self.__docter1 = value
        
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



class Receptionist:

    def __init__(self, Employee_ID: int, Name: str, patients3: "Patients" = None):
        self.Employee_ID = Employee_ID
        self.Name = Name
        self.patients3 = patients3
        
        pass
    @property
    def Employee_ID(self):
        return self.__Employee_ID
    @Employee_ID.setter
    def Employee_ID(self, Employee_ID: int):
        self.__Employee_ID = Employee_ID

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def patients3(self):
        return self.__patients3
    @patients3.setter
    def patients3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__patients3", None)
        self.__patients3 = value
        
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



class Docter:

    def __init__(self, ID: int, Name: str, Specialization: str, Rank: str, Salary: str, attribute2: str, patient0: set["Patients"] = None):
        self.ID = ID
        self.Name = Name
        self.Specialization = Specialization
        self.Rank = Rank
        self.Salary = Salary
        self.attribute2 = attribute2
        self.patient0 = patient0 if patient0 is not None else set()
        
        pass
    @property
    def Specialization(self):
        return self.__Specialization
    @Specialization.setter
    def Specialization(self, Specialization: str):
        self.__Specialization = Specialization

    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def Salary(self):
        return self.__Salary
    @Salary.setter
    def Salary(self, Salary: str):
        self.__Salary = Salary

    @property
    def Rank(self):
        return self.__Rank
    @Rank.setter
    def Rank(self, Rank: str):
        self.__Rank = Rank

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def patient0(self):
        return self.__patient0
    @patient0.setter
    def patient0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Docter__patient0", None)
        self.__patient0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "docter1"):
                    opp_val = getattr(item, "docter1", None)
                    
                    if opp_val == self:
                        setattr(item, "docter1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "docter1"):
                    opp_val = getattr(item, "docter1", None)
                    
                    setattr(item, "docter1", self)
                    

