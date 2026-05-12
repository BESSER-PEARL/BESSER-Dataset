from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Gender(Enum):
    pass

############################################
# Definition of Classes
############################################










class Person:

    def __init__(self, gender: Gender, age: int, address: str, phone: str):
        self.gender = gender
        self.age = age
        self.address = address
        self.phone = phone
        
        pass
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender: Gender):
        self.__gender = gender



class JuniorDoctor:

    pass


class ConsultantDoctor:

    pass


class Doctor:

    def __init__(self, specialty: str, locations: str, team5: set["Team"] = None, patient10: set["Patient"] = None):
        self.specialty = specialty
        self.locations = locations
        self.team5 = team5 if team5 is not None else set()
        self.patient10 = patient10 if patient10 is not None else set()
        
        pass
    @property
    def locations(self):
        return self.__locations
    @locations.setter
    def locations(self, locations: str):
        self.__locations = locations

    @property
    def specialty(self):
        return self.__specialty
    @specialty.setter
    def specialty(self, specialty: str):
        self.__specialty = specialty

    @property
    def patient10(self):
        return self.__patient10
    @patient10.setter
    def patient10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__patient10", None)
        self.__patient10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "doctor11"):
                    opp_val = getattr(item, "doctor11", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "doctor11"):
                    opp_val = getattr(item, "doctor11", None)
                    
                    if opp_val is None:
                        setattr(item, "doctor11", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def team5(self):
        return self.__team5
    @team5.setter
    def team5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__team5", None)
        self.__team5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "doctor4"):
                    opp_val = getattr(item, "doctor4", None)
                    
                    if opp_val == self:
                        setattr(item, "doctor4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "doctor4"):
                    opp_val = getattr(item, "doctor4", None)
                    
                    setattr(item, "doctor4", self)
                    



class Patient:

    def __init__(self, id: int, sickness: str, prescriptions: str, allergies: str, specialReqs: str, ward6: "Ward" = None, doctor11: set["Doctor"] = None, consultantDoctor13: "ConsultantDoctor" = None):
        self.id = id
        self.sickness = sickness
        self.prescriptions = prescriptions
        self.allergies = allergies
        self.specialReqs = specialReqs
        self.ward6 = ward6
        self.doctor11 = doctor11 if doctor11 is not None else set()
        self.consultantDoctor13 = consultantDoctor13
        
        pass
    @property
    def allergies(self):
        return self.__allergies
    @allergies.setter
    def allergies(self, allergies: str):
        self.__allergies = allergies

    @property
    def prescriptions(self):
        return self.__prescriptions
    @prescriptions.setter
    def prescriptions(self, prescriptions: str):
        self.__prescriptions = prescriptions

    @property
    def specialReqs(self):
        return self.__specialReqs
    @specialReqs.setter
    def specialReqs(self, specialReqs: str):
        self.__specialReqs = specialReqs

    @property
    def sickness(self):
        return self.__sickness
    @sickness.setter
    def sickness(self, sickness: str):
        self.__sickness = sickness

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def ward6(self):
        return self.__ward6
    @ward6.setter
    def ward6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__ward6", None)
        self.__ward6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient7"):
                opp_val = getattr(old_value, "patient7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient7"):
                opp_val = getattr(value, "patient7", None)
                if opp_val is None:
                    setattr(value, "patient7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def consultantDoctor13(self):
        return self.__consultantDoctor13
    @consultantDoctor13.setter
    def consultantDoctor13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__consultantDoctor13", None)
        self.__consultantDoctor13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient12"):
                opp_val = getattr(old_value, "patient12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient12"):
                opp_val = getattr(value, "patient12", None)
                if opp_val is None:
                    setattr(value, "patient12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def doctor11(self):
        return self.__doctor11
    @doctor11.setter
    def doctor11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__doctor11", None)
        self.__doctor11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patient10"):
                    opp_val = getattr(item, "patient10", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patient10"):
                    opp_val = getattr(item, "patient10", None)
                    
                    if opp_val is None:
                        setattr(item, "patient10", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Ward:

    def __init__(self, name: str, capacity: int, hospital1: "Hospital" = None, patient7: set["Patient"] = None):
        self.name = name
        self.capacity = capacity
        self.hospital1 = hospital1
        self.patient7 = patient7 if patient7 is not None else set()
        
        pass
    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def patient7(self):
        return self.__patient7
    @patient7.setter
    def patient7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ward__patient7", None)
        self.__patient7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ward6"):
                    opp_val = getattr(item, "ward6", None)
                    
                    if opp_val == self:
                        setattr(item, "ward6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ward6"):
                    opp_val = getattr(item, "ward6", None)
                    
                    setattr(item, "ward6", self)
                    

    @property
    def hospital1(self):
        return self.__hospital1
    @hospital1.setter
    def hospital1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ward__hospital1", None)
        self.__hospital1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ward0"):
                opp_val = getattr(old_value, "ward0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ward0"):
                opp_val = getattr(value, "ward0", None)
                if opp_val is None:
                    setattr(value, "ward0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Team:

    def __init__(self, name: str, hospital3: "Hospital" = None, doctor4: "Doctor" = None, consultantDoctor9: "ConsultantDoctor" = None):
        self.name = name
        self.hospital3 = hospital3
        self.doctor4 = doctor4
        self.consultantDoctor9 = consultantDoctor9
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def doctor4(self):
        return self.__doctor4
    @doctor4.setter
    def doctor4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Team__doctor4", None)
        self.__doctor4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "team5"):
                opp_val = getattr(old_value, "team5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "team5"):
                opp_val = getattr(value, "team5", None)
                if opp_val is None:
                    setattr(value, "team5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def consultantDoctor9(self):
        return self.__consultantDoctor9
    @consultantDoctor9.setter
    def consultantDoctor9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Team__consultantDoctor9", None)
        self.__consultantDoctor9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "team8"):
                opp_val = getattr(old_value, "team8", None)
                if opp_val == self:
                    setattr(old_value, "team8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "team8"):
                opp_val = getattr(value, "team8", None)
                setattr(value, "team8", self)

    @property
    def hospital3(self):
        return self.__hospital3
    @hospital3.setter
    def hospital3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Team__hospital3", None)
        self.__hospital3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "team2"):
                opp_val = getattr(old_value, "team2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "team2"):
                opp_val = getattr(value, "team2", None)
                if opp_val is None:
                    setattr(value, "team2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Hospital:

    def __init__(self, name: str, address: str, phone: str, ward0: set["Ward"] = None, team2: set["Team"] = None):
        self.name = name
        self.address = address
        self.phone = phone
        self.ward0 = ward0 if ward0 is not None else set()
        self.team2 = team2 if team2 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def ward0(self):
        return self.__ward0
    @ward0.setter
    def ward0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hospital__ward0", None)
        self.__ward0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hospital1"):
                    opp_val = getattr(item, "hospital1", None)
                    
                    if opp_val == self:
                        setattr(item, "hospital1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hospital1"):
                    opp_val = getattr(item, "hospital1", None)
                    
                    setattr(item, "hospital1", self)
                    

    @property
    def team2(self):
        return self.__team2
    @team2.setter
    def team2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hospital__team2", None)
        self.__team2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hospital3"):
                    opp_val = getattr(item, "hospital3", None)
                    
                    if opp_val == self:
                        setattr(item, "hospital3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hospital3"):
                    opp_val = getattr(item, "hospital3", None)
                    
                    setattr(item, "hospital3", self)
                    

