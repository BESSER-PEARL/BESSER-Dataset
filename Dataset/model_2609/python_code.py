from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class type(Enum):
    employee = "employee"
    client = "client"


############################################
# Definition of Classes
############################################

class Division:

    pass
class Company_Unit(Division):

    pass
class Company_Topic:

    def __init__(self, id: str, topics: "Company_Category" = None, Company_Topic: "Company_CompanyModel" = None, Topic: "Company_Category" = None):
        self.id = id
        self.topics = topics
        self.Company_Topic = Company_Topic
        self.Topic = Topic
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def topics(self):
        return self.__topics

    @topics.setter
    def topics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Topic__topics", None)
        self.__topics = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Category"):
                opp_val = getattr(old_value, "Category", None)
                if opp_val == self:
                    setattr(old_value, "Category", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Category"):
                opp_val = getattr(value, "Category", None)
                setattr(value, "Category", self)

    @property
    def Company_Topic(self):
        return self.__Company_Topic

    @Company_Topic.setter
    def Company_Topic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Topic__Company_Topic", None)
        self.__Company_Topic = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company_CompanyModel22"):
                opp_val = getattr(old_value, "Company_CompanyModel22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company_CompanyModel22"):
                opp_val = getattr(value, "Company_CompanyModel22", None)
                if opp_val is None:
                    setattr(value, "Company_CompanyModel22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Topic(self):
        return self.__Topic

    @Topic.setter
    def Topic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Topic__Topic", None)
        self.__Topic = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "category"):
                opp_val = getattr(old_value, "category", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "category"):
                opp_val = getattr(value, "category", None)
                if opp_val is None:
                    setattr(value, "category", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Project:

    pass
class Company_National(Project):

    def __init__(self, budget: int):
        self.budget = budget
        
    @property
    def budget(self) -> int:
        return self.__budget

    @budget.setter
    def budget(self, budget: int):
        self.__budget = budget

class Company_European(Project):

    def __init__(self, budget: int):
        self.budget = budget
        
    @property
    def budget(self) -> int:
        return self.__budget

    @budget.setter
    def budget(self, budget: int):
        self.__budget = budget

class Company_CompanyModel:

    pass
class Company_Organisation:

    def __init__(self, name: str, Company_Organisation9: "Company_Address" = None, Company_Organisation11: set["Company_Division"] = None, Company_Organisation: set["Company_Person"] = None, Company_Organisation6: set["Company_Project"] = None, Company_Organisation17: "Company_CompanyModel" = None):
        self.name = name
        self.Company_Organisation9 = Company_Organisation9
        self.Company_Organisation11 = Company_Organisation11 if Company_Organisation11 is not None else set()
        self.Company_Organisation = Company_Organisation if Company_Organisation is not None else set()
        self.Company_Organisation6 = Company_Organisation6 if Company_Organisation6 is not None else set()
        self.Company_Organisation17 = Company_Organisation17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Company_Organisation17(self):
        return self.__Company_Organisation17

    @Company_Organisation17.setter
    def Company_Organisation17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Organisation__Company_Organisation17", None)
        self.__Company_Organisation17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company_CompanyModel"):
                opp_val = getattr(old_value, "Company_CompanyModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company_CompanyModel"):
                opp_val = getattr(value, "Company_CompanyModel", None)
                if opp_val is None:
                    setattr(value, "Company_CompanyModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Company_Organisation9(self):
        return self.__Company_Organisation9

    @Company_Organisation9.setter
    def Company_Organisation9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Organisation__Company_Organisation9", None)
        self.__Company_Organisation9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company_Address"):
                opp_val = getattr(old_value, "Company_Address", None)
                if opp_val == self:
                    setattr(old_value, "Company_Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company_Address"):
                opp_val = getattr(value, "Company_Address", None)
                setattr(value, "Company_Address", self)

    @property
    def Company_Organisation11(self):
        return self.__Company_Organisation11

    @Company_Organisation11.setter
    def Company_Organisation11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Organisation__Company_Organisation11", None)
        self.__Company_Organisation11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Company_Division"):
                    opp_val = getattr(item, "Company_Division", None)
                    
                    if opp_val == self:
                        setattr(item, "Company_Division", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Company_Division"):
                    opp_val = getattr(item, "Company_Division", None)
                    
                    setattr(item, "Company_Division", self)
                    

    @property
    def Company_Organisation6(self):
        return self.__Company_Organisation6

    @Company_Organisation6.setter
    def Company_Organisation6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Organisation__Company_Organisation6", None)
        self.__Company_Organisation6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Company_Project7"):
                    opp_val = getattr(item, "Company_Project7", None)
                    
                    if opp_val == self:
                        setattr(item, "Company_Project7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Company_Project7"):
                    opp_val = getattr(item, "Company_Project7", None)
                    
                    setattr(item, "Company_Project7", self)
                    

    @property
    def Company_Organisation(self):
        return self.__Company_Organisation

    @Company_Organisation.setter
    def Company_Organisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Organisation__Company_Organisation", None)
        self.__Company_Organisation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Company_Person4"):
                    opp_val = getattr(item, "Company_Person4", None)
                    
                    if opp_val == self:
                        setattr(item, "Company_Person4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Company_Person4"):
                    opp_val = getattr(item, "Company_Person4", None)
                    
                    setattr(item, "Company_Person4", self)
                    

class Company_ServiceLine(Division):

    pass
class Company_Project(ABC):

    def __init__(self, name: str, Company_Project13: "Company_Category" = None, Company_Project: "Company_Person" = None, Company_Project7: "Company_Organisation" = None):
        self.name = name
        self.Company_Project13 = Company_Project13
        self.Company_Project = Company_Project
        self.Company_Project7 = Company_Project7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Company_Project(self):
        return self.__Company_Project

    @Company_Project.setter
    def Company_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Project__Company_Project", None)
        self.__Company_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company_Person"):
                opp_val = getattr(old_value, "Company_Person", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company_Person"):
                opp_val = getattr(value, "Company_Person", None)
                if opp_val is None:
                    setattr(value, "Company_Person", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Company_Project13(self):
        return self.__Company_Project13

    @Company_Project13.setter
    def Company_Project13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Project__Company_Project13", None)
        self.__Company_Project13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company_Category"):
                opp_val = getattr(old_value, "Company_Category", None)
                if opp_val == self:
                    setattr(old_value, "Company_Category", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company_Category"):
                opp_val = getattr(value, "Company_Category", None)
                setattr(value, "Company_Category", self)

    @property
    def Company_Project7(self):
        return self.__Company_Project7

    @Company_Project7.setter
    def Company_Project7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Project__Company_Project7", None)
        self.__Company_Project7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company_Organisation6"):
                opp_val = getattr(old_value, "Company_Organisation6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company_Organisation6"):
                opp_val = getattr(value, "Company_Organisation6", None)
                if opp_val is None:
                    setattr(value, "Company_Organisation6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Company_Category:

    def __init__(self, name: str, Company_Category: "Company_Project" = None, Company_Category20: "Company_CompanyModel" = None, category: set["Company_Topic"] = None, Category: "Company_Topic" = None):
        self.name = name
        self.Company_Category = Company_Category
        self.Company_Category20 = Company_Category20
        self.category = category if category is not None else set()
        self.Category = Category
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Company_Category20(self):
        return self.__Company_Category20

    @Company_Category20.setter
    def Company_Category20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Category__Company_Category20", None)
        self.__Company_Category20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company_CompanyModel19"):
                opp_val = getattr(old_value, "Company_CompanyModel19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company_CompanyModel19"):
                opp_val = getattr(value, "Company_CompanyModel19", None)
                if opp_val is None:
                    setattr(value, "Company_CompanyModel19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Category(self):
        return self.__Category

    @Category.setter
    def Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Category__Category", None)
        self.__Category = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "topics"):
                opp_val = getattr(old_value, "topics", None)
                if opp_val == self:
                    setattr(old_value, "topics", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "topics"):
                opp_val = getattr(value, "topics", None)
                setattr(value, "topics", self)

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Category__category", None)
        self.__category = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Topic"):
                    opp_val = getattr(item, "Topic", None)
                    
                    if opp_val == self:
                        setattr(item, "Topic", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Topic"):
                    opp_val = getattr(item, "Topic", None)
                    
                    setattr(item, "Topic", self)
                    

    @property
    def Company_Category(self):
        return self.__Company_Category

    @Company_Category.setter
    def Company_Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Category__Company_Category", None)
        self.__Company_Category = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company_Project13"):
                opp_val = getattr(old_value, "Company_Project13", None)
                if opp_val == self:
                    setattr(old_value, "Company_Project13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company_Project13"):
                opp_val = getattr(value, "Company_Project13", None)
                setattr(value, "Company_Project13", self)

class Company_Division(ABC):

    def __init__(self, name: str, Company_Division: "Company_Organisation" = None, Company_Division28: "Company_CompanyModel" = None):
        self.name = name
        self.Company_Division = Company_Division
        self.Company_Division28 = Company_Division28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Company_Division(self):
        return self.__Company_Division

    @Company_Division.setter
    def Company_Division(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Division__Company_Division", None)
        self.__Company_Division = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company_Organisation11"):
                opp_val = getattr(old_value, "Company_Organisation11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company_Organisation11"):
                opp_val = getattr(value, "Company_Organisation11", None)
                if opp_val is None:
                    setattr(value, "Company_Organisation11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Company_Division28(self):
        return self.__Company_Division28

    @Company_Division28.setter
    def Company_Division28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Division__Company_Division28", None)
        self.__Company_Division28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company_CompanyModel27"):
                opp_val = getattr(old_value, "Company_CompanyModel27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company_CompanyModel27"):
                opp_val = getattr(value, "Company_CompanyModel27", None)
                if opp_val is None:
                    setattr(value, "Company_CompanyModel27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Company_Address:

    def __init__(self, city: str, completeAddress: str, Company_Address: "Company_Organisation" = None, Company_Address25: "Company_CompanyModel" = None):
        self.city = city
        self.completeAddress = completeAddress
        self.Company_Address = Company_Address
        self.Company_Address25 = Company_Address25
        
    @property
    def completeAddress(self) -> str:
        return self.__completeAddress

    @completeAddress.setter
    def completeAddress(self, completeAddress: str):
        self.__completeAddress = completeAddress

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def Company_Address25(self):
        return self.__Company_Address25

    @Company_Address25.setter
    def Company_Address25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Address__Company_Address25", None)
        self.__Company_Address25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company_CompanyModel24"):
                opp_val = getattr(old_value, "Company_CompanyModel24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company_CompanyModel24"):
                opp_val = getattr(value, "Company_CompanyModel24", None)
                if opp_val is None:
                    setattr(value, "Company_CompanyModel24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Company_Address(self):
        return self.__Company_Address

    @Company_Address.setter
    def Company_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Address__Company_Address", None)
        self.__Company_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company_Organisation9"):
                opp_val = getattr(old_value, "Company_Organisation9", None)
                if opp_val == self:
                    setattr(old_value, "Company_Organisation9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company_Organisation9"):
                opp_val = getattr(value, "Company_Organisation9", None)
                setattr(value, "Company_Organisation9", self)

class Company_Person:

    def __init__(self, firstname: str, lastname: str, position: str, Company_Person: set["Company_Project"] = None, Company_Person2: "Company_ServiceLine" = None, Company_Person4: "Company_Organisation" = None):
        self.firstname = firstname
        self.lastname = lastname
        self.position = position
        self.Company_Person = Company_Person if Company_Person is not None else set()
        self.Company_Person2 = Company_Person2
        self.Company_Person4 = Company_Person4
        
    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def Company_Person2(self):
        return self.__Company_Person2

    @Company_Person2.setter
    def Company_Person2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Person__Company_Person2", None)
        self.__Company_Person2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company_ServiceLine"):
                opp_val = getattr(old_value, "Company_ServiceLine", None)
                if opp_val == self:
                    setattr(old_value, "Company_ServiceLine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company_ServiceLine"):
                opp_val = getattr(value, "Company_ServiceLine", None)
                setattr(value, "Company_ServiceLine", self)

    @property
    def Company_Person4(self):
        return self.__Company_Person4

    @Company_Person4.setter
    def Company_Person4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Person__Company_Person4", None)
        self.__Company_Person4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company_Organisation"):
                opp_val = getattr(old_value, "Company_Organisation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company_Organisation"):
                opp_val = getattr(value, "Company_Organisation", None)
                if opp_val is None:
                    setattr(value, "Company_Organisation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Company_Person(self):
        return self.__Company_Person

    @Company_Person.setter
    def Company_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Person__Company_Person", None)
        self.__Company_Person = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Company_Project"):
                    opp_val = getattr(item, "Company_Project", None)
                    
                    if opp_val == self:
                        setattr(item, "Company_Project", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Company_Project"):
                    opp_val = getattr(item, "Company_Project", None)
                    
                    setattr(item, "Company_Project", self)
                    
