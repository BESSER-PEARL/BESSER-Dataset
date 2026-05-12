from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Receptionist:

    pass


class Technologist:

    pass


class Technician:

    pass


class Front_Desk_Staff:

    pass


class Nurse:

    pass


class Technical_Staff:

    pass


class Administrative_Staff:

    pass


class Operations_Staff:

    pass


class Department:

    pass


class Doctor:

    def __init__(self, specialty: str, locations: str):
        self.specialty = specialty
        self.locations = locations
        
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



class Staff:

    def __init__(self, joined: str, education: str, certification: str, languages: str, department5: "Department" = None):
        self.joined = joined
        self.education = education
        self.certification = certification
        self.languages = languages
        self.department5 = department5
        
        pass
    @property
    def certification(self):
        return self.__certification
    @certification.setter
    def certification(self, certification: str):
        self.__certification = certification

    @property
    def joined(self):
        return self.__joined
    @joined.setter
    def joined(self, joined: str):
        self.__joined = joined

    @property
    def languages(self):
        return self.__languages
    @languages.setter
    def languages(self, languages: str):
        self.__languages = languages

    @property
    def education(self):
        return self.__education
    @education.setter
    def education(self, education: str):
        self.__education = education

    @property
    def department5(self):
        return self.__department5
    @department5.setter
    def department5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__department5", None)
        self.__department5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff4"):
                opp_val = getattr(old_value, "staff4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff4"):
                opp_val = getattr(value, "staff4", None)
                if opp_val is None:
                    setattr(value, "staff4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Hospital:

    def __init__(self, name: str, address: str, phone: str, person1: set["Person"] = None, department2: set["Department"] = None):
        self.name = name
        self.address = address
        self.phone = phone
        self.person1 = person1 if person1 is not None else set()
        self.department2 = department2 if department2 is not None else set()
        
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
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def person1(self):
        return self.__person1
    @person1.setter
    def person1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hospital__person1", None)
        self.__person1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hospital0"):
                    opp_val = getattr(item, "hospital0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hospital0"):
                    opp_val = getattr(item, "hospital0", None)
                    
                    if opp_val is None:
                        setattr(item, "hospital0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def department2(self):
        return self.__department2
    @department2.setter
    def department2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hospital__department2", None)
        self.__department2 = value if value is not None else set()
        
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
                    



class Patient:

    def __init__(self, id: str, name: str, gender: str, birthDate: str, age: int, accepted: str, sickness: str, prescriptions: str, allergies: str, specialReqs: str, operations_Staff6: set["Operations_Staff"] = None):
        self.id = id
        self.name = name
        self.gender = gender
        self.birthDate = birthDate
        self.age = age
        self.accepted = accepted
        self.sickness = sickness
        self.prescriptions = prescriptions
        self.allergies = allergies
        self.specialReqs = specialReqs
        self.operations_Staff6 = operations_Staff6 if operations_Staff6 is not None else set()
        
        pass
    @property
    def allergies(self):
        return self.__allergies
    @allergies.setter
    def allergies(self, allergies: str):
        self.__allergies = allergies

    @property
    def accepted(self):
        return self.__accepted
    @accepted.setter
    def accepted(self, accepted: str):
        self.__accepted = accepted

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
    def id(self, id: str):
        self.__id = id

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def birthDate(self):
        return self.__birthDate
    @birthDate.setter
    def birthDate(self, birthDate: str):
        self.__birthDate = birthDate

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def operations_Staff6(self):
        return self.__operations_Staff6
    @operations_Staff6.setter
    def operations_Staff6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__operations_Staff6", None)
        self.__operations_Staff6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patient7"):
                    opp_val = getattr(item, "patient7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patient7"):
                    opp_val = getattr(item, "patient7", None)
                    
                    if opp_val is None:
                        setattr(item, "patient7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Person:

    def __init__(self, title: str, givenName: str, middleName: str, familyName: str, name: str, birthDate: str, gender: str, homeAddress: str, phone: str, hospital0: set["Hospital"] = None):
        self.title = title
        self.givenName = givenName
        self.middleName = middleName
        self.familyName = familyName
        self.name = name
        self.birthDate = birthDate
        self.gender = gender
        self.homeAddress = homeAddress
        self.phone = phone
        self.hospital0 = hospital0 if hospital0 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def familyName(self):
        return self.__familyName
    @familyName.setter
    def familyName(self, familyName: str):
        self.__familyName = familyName

    @property
    def middleName(self):
        return self.__middleName
    @middleName.setter
    def middleName(self, middleName: str):
        self.__middleName = middleName

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def birthDate(self):
        return self.__birthDate
    @birthDate.setter
    def birthDate(self, birthDate: str):
        self.__birthDate = birthDate

    @property
    def homeAddress(self):
        return self.__homeAddress
    @homeAddress.setter
    def homeAddress(self, homeAddress: str):
        self.__homeAddress = homeAddress

    @property
    def givenName(self):
        return self.__givenName
    @givenName.setter
    def givenName(self, givenName: str):
        self.__givenName = givenName

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def hospital0(self):
        return self.__hospital0
    @hospital0.setter
    def hospital0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Person__hospital0", None)
        self.__hospital0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "person1"):
                    opp_val = getattr(item, "person1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "person1"):
                    opp_val = getattr(item, "person1", None)
                    
                    if opp_val is None:
                        setattr(item, "person1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

