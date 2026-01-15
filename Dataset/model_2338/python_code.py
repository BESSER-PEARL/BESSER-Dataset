from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class person_EStringToStringMapEntry:

    pass
class person_DocumentRoot:

    def __init__(self, mixed: str, person_DocumentRoot3: set["person_EStringToStringMapEntry"] = None, person_DocumentRoot6: set["person_CompanyType"] = None, person_DocumentRoot: set["person_EStringToStringMapEntry"] = None):
        self.mixed = mixed
        self.person_DocumentRoot3 = person_DocumentRoot3 if person_DocumentRoot3 is not None else set()
        self.person_DocumentRoot6 = person_DocumentRoot6 if person_DocumentRoot6 is not None else set()
        self.person_DocumentRoot = person_DocumentRoot if person_DocumentRoot is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def person_DocumentRoot(self):
        return self.__person_DocumentRoot

    @person_DocumentRoot.setter
    def person_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_person_DocumentRoot__person_DocumentRoot", None)
        self.__person_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "person_EStringToStringMapEntry"):
                    opp_val = getattr(item, "person_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "person_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "person_EStringToStringMapEntry"):
                    opp_val = getattr(item, "person_EStringToStringMapEntry", None)
                    
                    setattr(item, "person_EStringToStringMapEntry", self)
                    

    @property
    def person_DocumentRoot6(self):
        return self.__person_DocumentRoot6

    @person_DocumentRoot6.setter
    def person_DocumentRoot6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_person_DocumentRoot__person_DocumentRoot6", None)
        self.__person_DocumentRoot6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "person_CompanyType7"):
                    opp_val = getattr(item, "person_CompanyType7", None)
                    
                    if opp_val == self:
                        setattr(item, "person_CompanyType7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "person_CompanyType7"):
                    opp_val = getattr(item, "person_CompanyType7", None)
                    
                    setattr(item, "person_CompanyType7", self)
                    

    @property
    def person_DocumentRoot3(self):
        return self.__person_DocumentRoot3

    @person_DocumentRoot3.setter
    def person_DocumentRoot3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_person_DocumentRoot__person_DocumentRoot3", None)
        self.__person_DocumentRoot3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "person_EStringToStringMapEntry4"):
                    opp_val = getattr(item, "person_EStringToStringMapEntry4", None)
                    
                    if opp_val == self:
                        setattr(item, "person_EStringToStringMapEntry4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "person_EStringToStringMapEntry4"):
                    opp_val = getattr(item, "person_EStringToStringMapEntry4", None)
                    
                    setattr(item, "person_EStringToStringMapEntry4", self)
                    

class person_PersonType:

    def __init__(self, age: str, email: str, name: str, country: str, person_PersonType: "person_CompanyType" = None):
        self.age = age
        self.email = email
        self.name = name
        self.country = country
        self.person_PersonType = person_PersonType
        
    @property
    def age(self) -> str:
        return self.__age

    @age.setter
    def age(self, age: str):
        self.__age = age

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def person_PersonType(self):
        return self.__person_PersonType

    @person_PersonType.setter
    def person_PersonType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_person_PersonType__person_PersonType", None)
        self.__person_PersonType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "person_CompanyType"):
                opp_val = getattr(old_value, "person_CompanyType", None)
                if opp_val == self:
                    setattr(old_value, "person_CompanyType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "person_CompanyType"):
                opp_val = getattr(value, "person_CompanyType", None)
                setattr(value, "person_CompanyType", self)

class person_CompanyType:

    pass