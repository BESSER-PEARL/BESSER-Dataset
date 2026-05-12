from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Hospital_Doctor:

    def __init__(self, ID: int, Name: str, Specialization: str, Rank: str, Salary: int, patient0: set["Hospital_Patients"] = None):
        self.ID = ID
        self.Name = Name
        self.Specialization = Specialization
        self.Rank = Rank
        self.Salary = Salary
        self.patient0 = patient0 if patient0 is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Salary(self):
        return self.__Salary
    @Salary.setter
    def Salary(self, Salary: int):
        self.__Salary = Salary

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def Rank(self):
        return self.__Rank
    @Rank.setter
    def Rank(self, Rank: str):
        self.__Rank = Rank

    @property
    def Specialization(self):
        return self.__Specialization
    @Specialization.setter
    def Specialization(self, Specialization: str):
        self.__Specialization = Specialization

    @property
    def patient0(self):
        return self.__patient0
    @patient0.setter
    def patient0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hospital_Doctor__patient0", None)
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
                    



class Hospital__Receptionist:

    def __init__(self, Employee_ID: int, Name: str, patients3: set["Hospital_Patients"] = None):
        self.Employee_ID = Employee_ID
        self.Name = Name
        self.patients3 = patients3 if patients3 is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Employee_ID(self):
        return self.__Employee_ID
    @Employee_ID.setter
    def Employee_ID(self, Employee_ID: int):
        self.__Employee_ID = Employee_ID

    @property
    def patients3(self):
        return self.__patients3
    @patients3.setter
    def patients3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hospital__Receptionist__patients3", None)
        self.__patients3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Receptionist2"):
                    opp_val = getattr(item, "Receptionist2", None)
                    
                    if opp_val == self:
                        setattr(item, "Receptionist2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Receptionist2"):
                    opp_val = getattr(item, "Receptionist2", None)
                    
                    setattr(item, "Receptionist2", self)
                    



class Hospital:

    def __init__(self, HR: str, Operation_Theater: str, Cancer_Center: str, Cardiology: str):
        self.HR = HR
        self.Operation_Theater = Operation_Theater
        self.Cancer_Center = Cancer_Center
        self.Cardiology = Cardiology
        
        pass
    @property
    def HR(self):
        return self.__HR
    @HR.setter
    def HR(self, HR: str):
        self.__HR = HR

    @property
    def Operation_Theater(self):
        return self.__Operation_Theater
    @Operation_Theater.setter
    def Operation_Theater(self, Operation_Theater: str):
        self.__Operation_Theater = Operation_Theater

    @property
    def Cancer_Center(self):
        return self.__Cancer_Center
    @Cancer_Center.setter
    def Cancer_Center(self, Cancer_Center: str):
        self.__Cancer_Center = Cancer_Center

    @property
    def Cardiology(self):
        return self.__Cardiology
    @Cardiology.setter
    def Cardiology(self, Cardiology: str):
        self.__Cardiology = Cardiology



class Hospital_Patients:

    def __init__(self, Patient_s_Name: str, NIC_Number: int, Sickness: str, Phone_Number: int, doctor1: "Hospital_Doctor" = None, Receptionist2: "Hospital__Receptionist" = None):
        self.Patient_s_Name = Patient_s_Name
        self.NIC_Number = NIC_Number
        self.Sickness = Sickness
        self.Phone_Number = Phone_Number
        self.doctor1 = doctor1
        self.Receptionist2 = Receptionist2
        
        pass
    @property
    def Patient_s_Name(self):
        return self.__Patient_s_Name
    @Patient_s_Name.setter
    def Patient_s_Name(self, Patient_s_Name: str):
        self.__Patient_s_Name = Patient_s_Name

    @property
    def Phone_Number(self):
        return self.__Phone_Number
    @Phone_Number.setter
    def Phone_Number(self, Phone_Number: int):
        self.__Phone_Number = Phone_Number

    @property
    def NIC_Number(self):
        return self.__NIC_Number
    @NIC_Number.setter
    def NIC_Number(self, NIC_Number: int):
        self.__NIC_Number = NIC_Number

    @property
    def Sickness(self):
        return self.__Sickness
    @Sickness.setter
    def Sickness(self, Sickness: str):
        self.__Sickness = Sickness

    @property
    def Receptionist2(self):
        return self.__Receptionist2
    @Receptionist2.setter
    def Receptionist2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hospital_Patients__Receptionist2", None)
        self.__Receptionist2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patients3"):
                opp_val = getattr(old_value, "patients3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patients3"):
                opp_val = getattr(value, "patients3", None)
                if opp_val is None:
                    setattr(value, "patients3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def doctor1(self):
        return self.__doctor1
    @doctor1.setter
    def doctor1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hospital_Patients__doctor1", None)
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

