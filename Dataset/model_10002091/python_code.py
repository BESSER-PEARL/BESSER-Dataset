from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class patient:

    pass


class team:

    pass


class junior_doctor:

    pass


class consultant_doctor:

    pass


class ward:

    def __init__(self, ward_id: int, no_of_patients: str, hospital1: "Hospital" = None):
        self.ward_id = ward_id
        self.no_of_patients = no_of_patients
        self.hospital1 = hospital1
        
        pass
    @property
    def ward_id(self):
        return self.__ward_id
    @ward_id.setter
    def ward_id(self, ward_id: int):
        self.__ward_id = ward_id

    @property
    def no_of_patients(self):
        return self.__no_of_patients
    @no_of_patients.setter
    def no_of_patients(self, no_of_patients: str):
        self.__no_of_patients = no_of_patients

    @property
    def hospital1(self):
        return self.__hospital1
    @hospital1.setter
    def hospital1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ward__hospital1", None)
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



class Hospital:

    def __init__(self, name: str, totalwards: int, ward0: set["ward"] = None):
        self.name = name
        self.totalwards = totalwards
        self.ward0 = ward0 if ward0 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def totalwards(self):
        return self.__totalwards
    @totalwards.setter
    def totalwards(self, totalwards: int):
        self.__totalwards = totalwards

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
                    



class doctor:

    def __init__(self, name: str, grade: str, address: str, consultant_doctor2: "consultant_doctor" = None, junior_doctor4: "junior_doctor" = None, team6: "team" = None):
        self.name = name
        self.grade = grade
        self.address = address
        self.consultant_doctor2 = consultant_doctor2
        self.junior_doctor4 = junior_doctor4
        self.team6 = team6
        
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
    def grade(self):
        return self.__grade
    @grade.setter
    def grade(self, grade: str):
        self.__grade = grade

    @property
    def junior_doctor4(self):
        return self.__junior_doctor4
    @junior_doctor4.setter
    def junior_doctor4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doctor__junior_doctor4", None)
        self.__junior_doctor4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor5"):
                opp_val = getattr(old_value, "doctor5", None)
                if opp_val == self:
                    setattr(old_value, "doctor5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor5"):
                opp_val = getattr(value, "doctor5", None)
                setattr(value, "doctor5", self)

    @property
    def consultant_doctor2(self):
        return self.__consultant_doctor2
    @consultant_doctor2.setter
    def consultant_doctor2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doctor__consultant_doctor2", None)
        self.__consultant_doctor2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor3"):
                opp_val = getattr(old_value, "doctor3", None)
                if opp_val == self:
                    setattr(old_value, "doctor3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor3"):
                opp_val = getattr(value, "doctor3", None)
                setattr(value, "doctor3", self)

    @property
    def team6(self):
        return self.__team6
    @team6.setter
    def team6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doctor__team6", None)
        self.__team6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor7"):
                opp_val = getattr(old_value, "doctor7", None)
                if opp_val == self:
                    setattr(old_value, "doctor7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor7"):
                opp_val = getattr(value, "doctor7", None)
                setattr(value, "doctor7", self)



class Class1:

    pass
