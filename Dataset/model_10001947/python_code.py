from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Medical_staff_Actor:

    pass


class Patient_Actor:

    pass


class Decision_support_system_Check_treatment_recommendation_for_diagnosed_disease_UseCase:

    pass


class Decision_support_system_Generate_heart_disease_diagnosis_UseCase:

    pass


class Decision_support_system_Input_heart_disease_symptoms_UseCase:

    pass





class Doctor:

    def __init__(self, qualification: str, model10: "Model" = None, treatment12: set["Treatment"] = None):
        self.qualification = qualification
        self.model10 = model10
        self.treatment12 = treatment12 if treatment12 is not None else set()
        
        pass
    @property
    def qualification(self):
        return self.__qualification
    @qualification.setter
    def qualification(self, qualification: str):
        self.__qualification = qualification

    @property
    def model10(self):
        return self.__model10
    @model10.setter
    def model10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__model10", None)
        self.__model10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor11"):
                opp_val = getattr(old_value, "doctor11", None)
                if opp_val == self:
                    setattr(old_value, "doctor11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor11"):
                opp_val = getattr(value, "doctor11", None)
                setattr(value, "doctor11", self)

    @property
    def treatment12(self):
        return self.__treatment12
    @treatment12.setter
    def treatment12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__treatment12", None)
        self.__treatment12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "doctor13"):
                    opp_val = getattr(item, "doctor13", None)
                    
                    if opp_val == self:
                        setattr(item, "doctor13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "doctor13"):
                    opp_val = getattr(item, "doctor13", None)
                    
                    setattr(item, "doctor13", self)
                    



class Patient:

    def __init__(self, age: int, address: str, phone: str):
        self.age = age
        self.address = address
        self.phone = phone
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age: int):
        self.__age = age



class Treatment:

    def __init__(self, id: str, disease: str, doctor13: "Doctor" = None):
        self.id = id
        self.disease = disease
        self.doctor13 = doctor13
        
        pass
    @property
    def disease(self):
        return self.__disease
    @disease.setter
    def disease(self, disease: str):
        self.__disease = disease

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def doctor13(self):
        return self.__doctor13
    @doctor13.setter
    def doctor13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Treatment__doctor13", None)
        self.__doctor13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "treatment12"):
                opp_val = getattr(old_value, "treatment12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "treatment12"):
                opp_val = getattr(value, "treatment12", None)
                if opp_val is None:
                    setattr(value, "treatment12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Model:

    pass


class Input_Data:

    def __init__(self, id: str, Symptoms_list: str, user9: "user" = None):
        self.id = id
        self.Symptoms_list = Symptoms_list
        self.user9 = user9
        
        pass
    @property
    def Symptoms_list(self):
        return self.__Symptoms_list
    @Symptoms_list.setter
    def Symptoms_list(self, Symptoms_list: str):
        self.__Symptoms_list = Symptoms_list

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def user9(self):
        return self.__user9
    @user9.setter
    def user9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Input_Data__user9", None)
        self.__user9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "input_Data8"):
                opp_val = getattr(old_value, "input_Data8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "input_Data8"):
                opp_val = getattr(value, "input_Data8", None)
                if opp_val is None:
                    setattr(value, "input_Data8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class user:

    def __init__(self, name: str, id: str, input_Data8: set["Input_Data"] = None):
        self.name = name
        self.id = id
        self.input_Data8 = input_Data8 if input_Data8 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def input_Data8(self):
        return self.__input_Data8
    @input_Data8.setter
    def input_Data8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_user__input_Data8", None)
        self.__input_Data8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user9"):
                    opp_val = getattr(item, "user9", None)
                    
                    if opp_val == self:
                        setattr(item, "user9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user9"):
                    opp_val = getattr(item, "user9", None)
                    
                    setattr(item, "user9", self)
                    

