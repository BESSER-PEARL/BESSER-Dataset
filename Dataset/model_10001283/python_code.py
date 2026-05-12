from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Patient:

    def __init__(self, weight: float, Height: float, Allergies: str, DiagnosisList: str, Surgeries: str, Medicine: str, MedicalTest: str, diagnosis10: set["Diagnosis"] = None):
        self.weight = weight
        self.Height = Height
        self.Allergies = Allergies
        self.DiagnosisList = DiagnosisList
        self.Surgeries = Surgeries
        self.Medicine = Medicine
        self.MedicalTest = MedicalTest
        self.diagnosis10 = diagnosis10 if diagnosis10 is not None else set()
        
        pass
    @property
    def MedicalTest(self):
        return self.__MedicalTest
    @MedicalTest.setter
    def MedicalTest(self, MedicalTest: str):
        self.__MedicalTest = MedicalTest

    @property
    def Medicine(self):
        return self.__Medicine
    @Medicine.setter
    def Medicine(self, Medicine: str):
        self.__Medicine = Medicine

    @property
    def Height(self):
        return self.__Height
    @Height.setter
    def Height(self, Height: float):
        self.__Height = Height

    @property
    def Allergies(self):
        return self.__Allergies
    @Allergies.setter
    def Allergies(self, Allergies: str):
        self.__Allergies = Allergies

    @property
    def DiagnosisList(self):
        return self.__DiagnosisList
    @DiagnosisList.setter
    def DiagnosisList(self, DiagnosisList: str):
        self.__DiagnosisList = DiagnosisList

    @property
    def Surgeries(self):
        return self.__Surgeries
    @Surgeries.setter
    def Surgeries(self, Surgeries: str):
        self.__Surgeries = Surgeries

    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, weight: float):
        self.__weight = weight

    @property
    def diagnosis10(self):
        return self.__diagnosis10
    @diagnosis10.setter
    def diagnosis10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__diagnosis10", None)
        self.__diagnosis10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patient11"):
                    opp_val = getattr(item, "patient11", None)
                    
                    if opp_val == self:
                        setattr(item, "patient11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patient11"):
                    opp_val = getattr(item, "patient11", None)
                    
                    setattr(item, "patient11", self)
                    



class Medicine:

    def __init__(self, ID: int, name: str, Price: str, ActiveIngredient: str, Type: str, diagnosis1: "Diagnosis" = None):
        self.ID = ID
        self.name = name
        self.Price = Price
        self.ActiveIngredient = ActiveIngredient
        self.Type = Type
        self.diagnosis1 = diagnosis1
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def ActiveIngredient(self):
        return self.__ActiveIngredient
    @ActiveIngredient.setter
    def ActiveIngredient(self, ActiveIngredient: str):
        self.__ActiveIngredient = ActiveIngredient

    @property
    def Price(self):
        return self.__Price
    @Price.setter
    def Price(self, Price: str):
        self.__Price = Price

    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def diagnosis1(self):
        return self.__diagnosis1
    @diagnosis1.setter
    def diagnosis1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Medicine__diagnosis1", None)
        self.__diagnosis1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "medicine0"):
                opp_val = getattr(old_value, "medicine0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "medicine0"):
                opp_val = getattr(value, "medicine0", None)
                if opp_val is None:
                    setattr(value, "medicine0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Symptoms:

    def __init__(self, name: str, ID: int, diagnosis3: "Diagnosis" = None):
        self.name = name
        self.ID = ID
        self.diagnosis3 = diagnosis3
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def diagnosis3(self):
        return self.__diagnosis3
    @diagnosis3.setter
    def diagnosis3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Symptoms__diagnosis3", None)
        self.__diagnosis3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "symptoms2"):
                opp_val = getattr(old_value, "symptoms2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "symptoms2"):
                opp_val = getattr(value, "symptoms2", None)
                if opp_val is None:
                    setattr(value, "symptoms2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Instructions:

    def __init__(self, name: str, ID: int, descriptions: str, diagnosis7: "Diagnosis" = None):
        self.name = name
        self.ID = ID
        self.descriptions = descriptions
        self.diagnosis7 = diagnosis7
        
        pass
    @property
    def descriptions(self):
        return self.__descriptions
    @descriptions.setter
    def descriptions(self, descriptions: str):
        self.__descriptions = descriptions

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def diagnosis7(self):
        return self.__diagnosis7
    @diagnosis7.setter
    def diagnosis7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Instructions__diagnosis7", None)
        self.__diagnosis7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "instructions6"):
                opp_val = getattr(old_value, "instructions6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "instructions6"):
                opp_val = getattr(value, "instructions6", None)
                if opp_val is None:
                    setattr(value, "instructions6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Medical_test:

    def __init__(self, ID: int, name: str, Image: str, Lab: str, Date: str, diagnosis9: "Diagnosis" = None):
        self.ID = ID
        self.name = name
        self.Image = Image
        self.Lab = Lab
        self.Date = Date
        self.diagnosis9 = diagnosis9
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def Image(self):
        return self.__Image
    @Image.setter
    def Image(self, Image: str):
        self.__Image = Image

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def Lab(self):
        return self.__Lab
    @Lab.setter
    def Lab(self, Lab: str):
        self.__Lab = Lab

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def diagnosis9(self):
        return self.__diagnosis9
    @diagnosis9.setter
    def diagnosis9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Medical_test__diagnosis9", None)
        self.__diagnosis9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "medical_test8"):
                opp_val = getattr(old_value, "medical_test8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "medical_test8"):
                opp_val = getattr(value, "medical_test8", None)
                if opp_val is None:
                    setattr(value, "medical_test8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Signs:

    def __init__(self, name: str, ID: int, diagnosis5: "Diagnosis" = None):
        self.name = name
        self.ID = ID
        self.diagnosis5 = diagnosis5
        
        pass
    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def diagnosis5(self):
        return self.__diagnosis5
    @diagnosis5.setter
    def diagnosis5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Signs__diagnosis5", None)
        self.__diagnosis5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "signs4"):
                opp_val = getattr(old_value, "signs4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "signs4"):
                opp_val = getattr(value, "signs4", None)
                if opp_val is None:
                    setattr(value, "signs4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Diagnosis:

    def __init__(self, ID: int, Patient_Id: int, Doctor_Id: int, Date: str, Condition: str, LIst_of_Diagnosis: str, LIst_of_Medical_Test: str, LIst_of_Instructions: str, LIst_of_Symptoms: str, LIst_of_Medicine: str, medicine0: set["Medicine"] = None, symptoms2: set["Symptoms"] = None, signs4: set["Signs"] = None, instructions6: set["Instructions"] = None, medical_test8: set["Medical_test"] = None, patient11: "Patient" = None):
        self.ID = ID
        self.Patient_Id = Patient_Id
        self.Doctor_Id = Doctor_Id
        self.Date = Date
        self.Condition = Condition
        self.LIst_of_Diagnosis = LIst_of_Diagnosis
        self.LIst_of_Medical_Test = LIst_of_Medical_Test
        self.LIst_of_Instructions = LIst_of_Instructions
        self.LIst_of_Symptoms = LIst_of_Symptoms
        self.LIst_of_Medicine = LIst_of_Medicine
        self.medicine0 = medicine0 if medicine0 is not None else set()
        self.symptoms2 = symptoms2 if symptoms2 is not None else set()
        self.signs4 = signs4 if signs4 is not None else set()
        self.instructions6 = instructions6 if instructions6 is not None else set()
        self.medical_test8 = medical_test8 if medical_test8 is not None else set()
        self.patient11 = patient11
        
        pass
    @property
    def Patient_Id(self):
        return self.__Patient_Id
    @Patient_Id.setter
    def Patient_Id(self, Patient_Id: int):
        self.__Patient_Id = Patient_Id

    @property
    def LIst_of_Medicine(self):
        return self.__LIst_of_Medicine
    @LIst_of_Medicine.setter
    def LIst_of_Medicine(self, LIst_of_Medicine: str):
        self.__LIst_of_Medicine = LIst_of_Medicine

    @property
    def Doctor_Id(self):
        return self.__Doctor_Id
    @Doctor_Id.setter
    def Doctor_Id(self, Doctor_Id: int):
        self.__Doctor_Id = Doctor_Id

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def LIst_of_Medical_Test(self):
        return self.__LIst_of_Medical_Test
    @LIst_of_Medical_Test.setter
    def LIst_of_Medical_Test(self, LIst_of_Medical_Test: str):
        self.__LIst_of_Medical_Test = LIst_of_Medical_Test

    @property
    def LIst_of_Instructions(self):
        return self.__LIst_of_Instructions
    @LIst_of_Instructions.setter
    def LIst_of_Instructions(self, LIst_of_Instructions: str):
        self.__LIst_of_Instructions = LIst_of_Instructions

    @property
    def LIst_of_Diagnosis(self):
        return self.__LIst_of_Diagnosis
    @LIst_of_Diagnosis.setter
    def LIst_of_Diagnosis(self, LIst_of_Diagnosis: str):
        self.__LIst_of_Diagnosis = LIst_of_Diagnosis

    @property
    def Condition(self):
        return self.__Condition
    @Condition.setter
    def Condition(self, Condition: str):
        self.__Condition = Condition

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def LIst_of_Symptoms(self):
        return self.__LIst_of_Symptoms
    @LIst_of_Symptoms.setter
    def LIst_of_Symptoms(self, LIst_of_Symptoms: str):
        self.__LIst_of_Symptoms = LIst_of_Symptoms

    @property
    def signs4(self):
        return self.__signs4
    @signs4.setter
    def signs4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Diagnosis__signs4", None)
        self.__signs4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagnosis5"):
                    opp_val = getattr(item, "diagnosis5", None)
                    
                    if opp_val == self:
                        setattr(item, "diagnosis5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagnosis5"):
                    opp_val = getattr(item, "diagnosis5", None)
                    
                    setattr(item, "diagnosis5", self)
                    

    @property
    def instructions6(self):
        return self.__instructions6
    @instructions6.setter
    def instructions6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Diagnosis__instructions6", None)
        self.__instructions6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagnosis7"):
                    opp_val = getattr(item, "diagnosis7", None)
                    
                    if opp_val == self:
                        setattr(item, "diagnosis7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagnosis7"):
                    opp_val = getattr(item, "diagnosis7", None)
                    
                    setattr(item, "diagnosis7", self)
                    

    @property
    def symptoms2(self):
        return self.__symptoms2
    @symptoms2.setter
    def symptoms2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Diagnosis__symptoms2", None)
        self.__symptoms2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagnosis3"):
                    opp_val = getattr(item, "diagnosis3", None)
                    
                    if opp_val == self:
                        setattr(item, "diagnosis3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagnosis3"):
                    opp_val = getattr(item, "diagnosis3", None)
                    
                    setattr(item, "diagnosis3", self)
                    

    @property
    def medicine0(self):
        return self.__medicine0
    @medicine0.setter
    def medicine0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Diagnosis__medicine0", None)
        self.__medicine0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagnosis1"):
                    opp_val = getattr(item, "diagnosis1", None)
                    
                    if opp_val == self:
                        setattr(item, "diagnosis1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagnosis1"):
                    opp_val = getattr(item, "diagnosis1", None)
                    
                    setattr(item, "diagnosis1", self)
                    

    @property
    def medical_test8(self):
        return self.__medical_test8
    @medical_test8.setter
    def medical_test8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Diagnosis__medical_test8", None)
        self.__medical_test8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagnosis9"):
                    opp_val = getattr(item, "diagnosis9", None)
                    
                    if opp_val == self:
                        setattr(item, "diagnosis9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagnosis9"):
                    opp_val = getattr(item, "diagnosis9", None)
                    
                    setattr(item, "diagnosis9", self)
                    

    @property
    def patient11(self):
        return self.__patient11
    @patient11.setter
    def patient11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Diagnosis__patient11", None)
        self.__patient11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagnosis10"):
                opp_val = getattr(old_value, "diagnosis10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagnosis10"):
                opp_val = getattr(value, "diagnosis10", None)
                if opp_val is None:
                    setattr(value, "diagnosis10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Person:

    def __init__(self, Name: str, Email: str, Password: str, ID: int, Ssn: str, Image: str, PhoneNumeber: str, InsuranceNumber: str, Gender: int, Last_Seen: str, Balance: str, Lat: str, Long: str):
        self.Name = Name
        self.Email = Email
        self.Password = Password
        self.ID = ID
        self.Ssn = Ssn
        self.Image = Image
        self.PhoneNumeber = PhoneNumeber
        self.InsuranceNumber = InsuranceNumber
        self.Gender = Gender
        self.Last_Seen = Last_Seen
        self.Balance = Balance
        self.Lat = Lat
        self.Long = Long
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Last_Seen(self):
        return self.__Last_Seen
    @Last_Seen.setter
    def Last_Seen(self, Last_Seen: str):
        self.__Last_Seen = Last_Seen

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def Gender(self):
        return self.__Gender
    @Gender.setter
    def Gender(self, Gender: int):
        self.__Gender = Gender

    @property
    def Image(self):
        return self.__Image
    @Image.setter
    def Image(self, Image: str):
        self.__Image = Image

    @property
    def Balance(self):
        return self.__Balance
    @Balance.setter
    def Balance(self, Balance: str):
        self.__Balance = Balance

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Long(self):
        return self.__Long
    @Long.setter
    def Long(self, Long: str):
        self.__Long = Long

    @property
    def PhoneNumeber(self):
        return self.__PhoneNumeber
    @PhoneNumeber.setter
    def PhoneNumeber(self, PhoneNumeber: str):
        self.__PhoneNumeber = PhoneNumeber

    @property
    def Lat(self):
        return self.__Lat
    @Lat.setter
    def Lat(self, Lat: str):
        self.__Lat = Lat

    @property
    def InsuranceNumber(self):
        return self.__InsuranceNumber
    @InsuranceNumber.setter
    def InsuranceNumber(self, InsuranceNumber: str):
        self.__InsuranceNumber = InsuranceNumber

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Ssn(self):
        return self.__Ssn
    @Ssn.setter
    def Ssn(self, Ssn: str):
        self.__Ssn = Ssn

