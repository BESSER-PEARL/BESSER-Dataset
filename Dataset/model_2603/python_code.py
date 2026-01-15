from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Gender(Enum):
    Male = "Male"
    Female = "Female"


############################################
# Definition of Classes
############################################

class PersonList_LivingPlace:

    def __init__(self, address: str, home: set["PersonList_Person"] = None, PersonList_LivingPlace: "PersonList_List" = None, LivingPlace: "PersonList_Person" = None):
        self.address = address
        self.home = home if home is not None else set()
        self.PersonList_LivingPlace = PersonList_LivingPlace
        self.LivingPlace = LivingPlace
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def PersonList_LivingPlace(self):
        return self.__PersonList_LivingPlace

    @PersonList_LivingPlace.setter
    def PersonList_LivingPlace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_LivingPlace__PersonList_LivingPlace", None)
        self.__PersonList_LivingPlace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PersonList_List3"):
                opp_val = getattr(old_value, "PersonList_List3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PersonList_List3"):
                opp_val = getattr(value, "PersonList_List3", None)
                if opp_val is None:
                    setattr(value, "PersonList_List3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def home(self):
        return self.__home

    @home.setter
    def home(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_LivingPlace__home", None)
        self.__home = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person11"):
                    opp_val = getattr(item, "Person11", None)
                    
                    if opp_val == self:
                        setattr(item, "Person11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person11"):
                    opp_val = getattr(item, "Person11", None)
                    
                    setattr(item, "Person11", self)
                    

    @property
    def LivingPlace(self):
        return self.__LivingPlace

    @LivingPlace.setter
    def LivingPlace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_LivingPlace__LivingPlace", None)
        self.__LivingPlace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persons7"):
                opp_val = getattr(old_value, "persons7", None)
                if opp_val == self:
                    setattr(old_value, "persons7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persons7"):
                opp_val = getattr(value, "persons7", None)
                setattr(value, "persons7", self)

class PersonList_WorkPlace:

    def __init__(self, address: str, PersonList_WorkPlace: "PersonList_List" = None, WorkPlace: "PersonList_Person" = None, works: set["PersonList_Person"] = None):
        self.address = address
        self.PersonList_WorkPlace = PersonList_WorkPlace
        self.WorkPlace = WorkPlace
        self.works = works if works is not None else set()
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def WorkPlace(self):
        return self.__WorkPlace

    @WorkPlace.setter
    def WorkPlace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_WorkPlace__WorkPlace", None)
        self.__WorkPlace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persons"):
                opp_val = getattr(old_value, "persons", None)
                if opp_val == self:
                    setattr(old_value, "persons", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persons"):
                opp_val = getattr(value, "persons", None)
                setattr(value, "persons", self)

    @property
    def works(self):
        return self.__works

    @works.setter
    def works(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_WorkPlace__works", None)
        self.__works = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person9"):
                    opp_val = getattr(item, "Person9", None)
                    
                    if opp_val == self:
                        setattr(item, "Person9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person9"):
                    opp_val = getattr(item, "Person9", None)
                    
                    setattr(item, "Person9", self)
                    

    @property
    def PersonList_WorkPlace(self):
        return self.__PersonList_WorkPlace

    @PersonList_WorkPlace.setter
    def PersonList_WorkPlace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_WorkPlace__PersonList_WorkPlace", None)
        self.__PersonList_WorkPlace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PersonList_List"):
                opp_val = getattr(old_value, "PersonList_List", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PersonList_List"):
                opp_val = getattr(value, "PersonList_List", None)
                if opp_val is None:
                    setattr(value, "PersonList_List", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PersonList_Person:

    def __init__(self, firstname: str, lastname: str, gender: str, Person: "PersonList_List" = None, Person11: "PersonList_LivingPlace" = None, members: "PersonList_List" = None, persons: "PersonList_WorkPlace" = None, persons7: "PersonList_LivingPlace" = None, Person9: "PersonList_WorkPlace" = None):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.Person = Person
        self.Person11 = Person11
        self.members = members
        self.persons = persons
        self.persons7 = persons7
        self.Person9 = Person9
        
    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def persons7(self):
        return self.__persons7

    @persons7.setter
    def persons7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_Person__persons7", None)
        self.__persons7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "LivingPlace"):
                opp_val = getattr(old_value, "LivingPlace", None)
                if opp_val == self:
                    setattr(old_value, "LivingPlace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "LivingPlace"):
                opp_val = getattr(value, "LivingPlace", None)
                setattr(value, "LivingPlace", self)

    @property
    def Person9(self):
        return self.__Person9

    @Person9.setter
    def Person9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_Person__Person9", None)
        self.__Person9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "works"):
                opp_val = getattr(old_value, "works", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "works"):
                opp_val = getattr(value, "works", None)
                if opp_val is None:
                    setattr(value, "works", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def members(self):
        return self.__members

    @members.setter
    def members(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_Person__members", None)
        self.__members = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "List"):
                opp_val = getattr(old_value, "List", None)
                if opp_val == self:
                    setattr(old_value, "List", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "List"):
                opp_val = getattr(value, "List", None)
                setattr(value, "List", self)

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "list"):
                opp_val = getattr(old_value, "list", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "list"):
                opp_val = getattr(value, "list", None)
                if opp_val is None:
                    setattr(value, "list", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persons(self):
        return self.__persons

    @persons.setter
    def persons(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_Person__persons", None)
        self.__persons = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WorkPlace"):
                opp_val = getattr(old_value, "WorkPlace", None)
                if opp_val == self:
                    setattr(old_value, "WorkPlace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WorkPlace"):
                opp_val = getattr(value, "WorkPlace", None)
                setattr(value, "WorkPlace", self)

    @property
    def Person11(self):
        return self.__Person11

    @Person11.setter
    def Person11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonList_Person__Person11", None)
        self.__Person11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "home"):
                opp_val = getattr(old_value, "home", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "home"):
                opp_val = getattr(value, "home", None)
                if opp_val is None:
                    setattr(value, "home", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PersonList_List:

    pass