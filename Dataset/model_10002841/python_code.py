from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Patient_Check_In_aPatient:

    def __init__(self, Patient_s_Name: str, MRN_Number: int, Symptoms: str, Phone_Number: int, doctor1: "Patient_Check_In_aDoctor" = None, Receptionist2: "Patient_Check_In__aReceptionist" = None):
        self.Patient_s_Name = Patient_s_Name
        self.MRN_Number = MRN_Number
        self.Symptoms = Symptoms
        self.Phone_Number = Phone_Number
        self.doctor1 = doctor1
        self.Receptionist2 = Receptionist2
        
        pass
    @property
    def Phone_Number(self):
        return self.__Phone_Number
    @Phone_Number.setter
    def Phone_Number(self, Phone_Number: int):
        self.__Phone_Number = Phone_Number

    @property
    def MRN_Number(self):
        return self.__MRN_Number
    @MRN_Number.setter
    def MRN_Number(self, MRN_Number: int):
        self.__MRN_Number = MRN_Number

    @property
    def Symptoms(self):
        return self.__Symptoms
    @Symptoms.setter
    def Symptoms(self, Symptoms: str):
        self.__Symptoms = Symptoms

    @property
    def Patient_s_Name(self):
        return self.__Patient_s_Name
    @Patient_s_Name.setter
    def Patient_s_Name(self, Patient_s_Name: str):
        self.__Patient_s_Name = Patient_s_Name

    @property
    def Receptionist2(self):
        return self.__Receptionist2
    @Receptionist2.setter
    def Receptionist2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient_Check_In_aPatient__Receptionist2", None)
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
        old_value = getattr(self, f"_Patient_Check_In_aPatient__doctor1", None)
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



class Patient_Check_In_aDoctor:

    def __init__(self, ID: int, Name: str, Specialization: str, Rank: str, patient0: set["Patient_Check_In_aPatient"] = None):
        self.ID = ID
        self.Name = Name
        self.Specialization = Specialization
        self.Rank = Rank
        self.patient0 = patient0 if patient0 is not None else set()
        
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
        old_value = getattr(self, f"_Patient_Check_In_aDoctor__patient0", None)
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
                    



class Patient_Check_In__aReceptionist:

    def __init__(self, Employee_ID: int, Name: str, patients3: set["Patient_Check_In_aPatient"] = None):
        self.Employee_ID = Employee_ID
        self.Name = Name
        self.patients3 = patients3 if patients3 is not None else set()
        
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
        old_value = getattr(self, f"_Patient_Check_In__aReceptionist__patients3", None)
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
                    



class Patient_Check_In_aNurse:

    def __init__(self, ID: int, Name: str, Ranking: str):
        self.ID = ID
        self.Name = Name
        self.Ranking = Ranking
        
        pass
    @property
    def Ranking(self):
        return self.__Ranking
    @Ranking.setter
    def Ranking(self, Ranking: str):
        self.__Ranking = Ranking

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

