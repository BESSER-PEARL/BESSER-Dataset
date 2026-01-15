from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Division:

    pass
class Company_ServiceLine(Division):

    pass
class Person:

    pass
class Company_Client(Person):

    pass
class Company_Employee(Person):

    pass
class Company_CompanyModel:

    pass
class Company_Category:

    def __init__(self, name: str, category: set["Company_Topic"] = None, Category: "Company_Topic" = None, Company_Category: "Company_CompanyModel" = None):
        self.name = name
        self.category = category if category is not None else set()
        self.Category = Category
        self.Company_Category = Company_Category
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "Company_CompanyModel17"):
                opp_val = getattr(old_value, "Company_CompanyModel17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company_CompanyModel17"):
                opp_val = getattr(value, "Company_CompanyModel17", None)
                if opp_val is None:
                    setattr(value, "Company_CompanyModel17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class Company_Topic:

    def __init__(self, id: str, Company_Topic: "Company_Project" = None, Topic: "Company_Category" = None, topics: "Company_Category" = None, Company_Topic20: "Company_CompanyModel" = None):
        self.id = id
        self.Company_Topic = Company_Topic
        self.Topic = Topic
        self.topics = topics
        self.Company_Topic20 = Company_Topic20
        
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

    @property
    def Company_Topic20(self):
        return self.__Company_Topic20

    @Company_Topic20.setter
    def Company_Topic20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Topic__Company_Topic20", None)
        self.__Company_Topic20 = value
        
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
    def Company_Topic(self):
        return self.__Company_Topic

    @Company_Topic.setter
    def Company_Topic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Topic__Company_Topic", None)
        self.__Company_Topic = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company_Project11"):
                opp_val = getattr(old_value, "Company_Project11", None)
                if opp_val == self:
                    setattr(old_value, "Company_Project11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company_Project11"):
                opp_val = getattr(value, "Company_Project11", None)
                setattr(value, "Company_Project11", self)

class Company_Division(ABC):

    def __init__(self, name: str, Company_Division: "Company_Organisation" = None, Company_Division23: "Company_CompanyModel" = None):
        self.name = name
        self.Company_Division = Company_Division
        self.Company_Division23 = Company_Division23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Company_Division23(self):
        return self.__Company_Division23

    @Company_Division23.setter
    def Company_Division23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Division__Company_Division23", None)
        self.__Company_Division23 = value
        
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
    def Company_Division(self):
        return self.__Company_Division

    @Company_Division.setter
    def Company_Division(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Division__Company_Division", None)
        self.__Company_Division = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company_Organisation9"):
                opp_val = getattr(old_value, "Company_Organisation9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company_Organisation9"):
                opp_val = getattr(value, "Company_Organisation9", None)
                if opp_val is None:
                    setattr(value, "Company_Organisation9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Company_Unit(Division):

    pass
class Company_Project:

    def __init__(self, name: str, budget: int, Company_Project: "Company_Person" = None, Company_Project7: "Company_Organisation" = None, Company_Project11: "Company_Topic" = None):
        self.name = name
        self.budget = budget
        self.Company_Project = Company_Project
        self.Company_Project7 = Company_Project7
        self.Company_Project11 = Company_Project11
        
    @property
    def budget(self) -> int:
        return self.__budget

    @budget.setter
    def budget(self, budget: int):
        self.__budget = budget

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def Company_Project11(self):
        return self.__Company_Project11

    @Company_Project11.setter
    def Company_Project11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Project__Company_Project11", None)
        self.__Company_Project11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company_Topic"):
                opp_val = getattr(old_value, "Company_Topic", None)
                if opp_val == self:
                    setattr(old_value, "Company_Topic", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company_Topic"):
                opp_val = getattr(value, "Company_Topic", None)
                setattr(value, "Company_Topic", self)

class Company_Person(ABC):

    def __init__(self, fullName: str, Company_Person: set["Company_Project"] = None, Company_Person2: "Company_Unit" = None, Company_Person4: "Company_Organisation" = None):
        self.fullName = fullName
        self.Company_Person = Company_Person if Company_Person is not None else set()
        self.Company_Person2 = Company_Person2
        self.Company_Person4 = Company_Person4
        
    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

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
    def Company_Person2(self):
        return self.__Company_Person2

    @Company_Person2.setter
    def Company_Person2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Person__Company_Person2", None)
        self.__Company_Person2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company_Unit"):
                opp_val = getattr(old_value, "Company_Unit", None)
                if opp_val == self:
                    setattr(old_value, "Company_Unit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company_Unit"):
                opp_val = getattr(value, "Company_Unit", None)
                setattr(value, "Company_Unit", self)

class Company_Organisation:

    def __init__(self, name: str, city: str, completeAddress: str, Company_Organisation: set["Company_Person"] = None, Company_Organisation6: set["Company_Project"] = None, Company_Organisation9: set["Company_Division"] = None, Company_Organisation15: "Company_CompanyModel" = None):
        self.name = name
        self.city = city
        self.completeAddress = completeAddress
        self.Company_Organisation = Company_Organisation if Company_Organisation is not None else set()
        self.Company_Organisation6 = Company_Organisation6 if Company_Organisation6 is not None else set()
        self.Company_Organisation9 = Company_Organisation9 if Company_Organisation9 is not None else set()
        self.Company_Organisation15 = Company_Organisation15
        
    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def completeAddress(self) -> str:
        return self.__completeAddress

    @completeAddress.setter
    def completeAddress(self, completeAddress: str):
        self.__completeAddress = completeAddress

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
                    

    @property
    def Company_Organisation15(self):
        return self.__Company_Organisation15

    @Company_Organisation15.setter
    def Company_Organisation15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Organisation__Company_Organisation15", None)
        self.__Company_Organisation15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company_CompanyModel"):
                opp_val = getattr(old_value, "Company_CompanyModel", None)
                if opp_val == self:
                    setattr(old_value, "Company_CompanyModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company_CompanyModel"):
                opp_val = getattr(value, "Company_CompanyModel", None)
                setattr(value, "Company_CompanyModel", self)

    @property
    def Company_Organisation9(self):
        return self.__Company_Organisation9

    @Company_Organisation9.setter
    def Company_Organisation9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Company_Organisation__Company_Organisation9", None)
        self.__Company_Organisation9 = value if value is not None else set()
        
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
                    
