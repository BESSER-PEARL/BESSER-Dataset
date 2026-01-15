from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class EvoCompany_Category:

    def __init__(self, name: str, EvoCompany_Category: "EvoCompany_CompanyModel" = None, category: set["EvoCompany_Topic"] = None, Category: "EvoCompany_Topic" = None):
        self.name = name
        self.EvoCompany_Category = EvoCompany_Category
        self.category = category if category is not None else set()
        self.Category = Category
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Category(self):
        return self.__Category

    @Category.setter
    def Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EvoCompany_Category__Category", None)
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
        old_value = getattr(self, f"_EvoCompany_Category__category", None)
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
    def EvoCompany_Category(self):
        return self.__EvoCompany_Category

    @EvoCompany_Category.setter
    def EvoCompany_Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EvoCompany_Category__EvoCompany_Category", None)
        self.__EvoCompany_Category = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EvoCompany_CompanyModel17"):
                opp_val = getattr(old_value, "EvoCompany_CompanyModel17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EvoCompany_CompanyModel17"):
                opp_val = getattr(value, "EvoCompany_CompanyModel17", None)
                if opp_val is None:
                    setattr(value, "EvoCompany_CompanyModel17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class EvoCompany_Topic:

    def __init__(self, id: str, EvoCompany_Topic20: "EvoCompany_CompanyModel" = None, EvoCompany_Topic: "EvoCompany_Project" = None, Topic: "EvoCompany_Category" = None, topics: "EvoCompany_Category" = None):
        self.id = id
        self.EvoCompany_Topic20 = EvoCompany_Topic20
        self.EvoCompany_Topic = EvoCompany_Topic
        self.Topic = Topic
        self.topics = topics
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def Topic(self):
        return self.__Topic

    @Topic.setter
    def Topic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EvoCompany_Topic__Topic", None)
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
    def EvoCompany_Topic20(self):
        return self.__EvoCompany_Topic20

    @EvoCompany_Topic20.setter
    def EvoCompany_Topic20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EvoCompany_Topic__EvoCompany_Topic20", None)
        self.__EvoCompany_Topic20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EvoCompany_CompanyModel19"):
                opp_val = getattr(old_value, "EvoCompany_CompanyModel19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EvoCompany_CompanyModel19"):
                opp_val = getattr(value, "EvoCompany_CompanyModel19", None)
                if opp_val is None:
                    setattr(value, "EvoCompany_CompanyModel19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EvoCompany_Topic(self):
        return self.__EvoCompany_Topic

    @EvoCompany_Topic.setter
    def EvoCompany_Topic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EvoCompany_Topic__EvoCompany_Topic", None)
        self.__EvoCompany_Topic = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EvoCompany_Project11"):
                opp_val = getattr(old_value, "EvoCompany_Project11", None)
                if opp_val == self:
                    setattr(old_value, "EvoCompany_Project11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EvoCompany_Project11"):
                opp_val = getattr(value, "EvoCompany_Project11", None)
                setattr(value, "EvoCompany_Project11", self)

    @property
    def topics(self):
        return self.__topics

    @topics.setter
    def topics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EvoCompany_Topic__topics", None)
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

class EvoCompany_Division(ABC):

    def __init__(self, name: str, EvoCompany_Division23: "EvoCompany_CompanyModel" = None, EvoCompany_Division: "EvoCompany_Organisation" = None):
        self.name = name
        self.EvoCompany_Division23 = EvoCompany_Division23
        self.EvoCompany_Division = EvoCompany_Division
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def EvoCompany_Division23(self):
        return self.__EvoCompany_Division23

    @EvoCompany_Division23.setter
    def EvoCompany_Division23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EvoCompany_Division__EvoCompany_Division23", None)
        self.__EvoCompany_Division23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EvoCompany_CompanyModel22"):
                opp_val = getattr(old_value, "EvoCompany_CompanyModel22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EvoCompany_CompanyModel22"):
                opp_val = getattr(value, "EvoCompany_CompanyModel22", None)
                if opp_val is None:
                    setattr(value, "EvoCompany_CompanyModel22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EvoCompany_Division(self):
        return self.__EvoCompany_Division

    @EvoCompany_Division.setter
    def EvoCompany_Division(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EvoCompany_Division__EvoCompany_Division", None)
        self.__EvoCompany_Division = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EvoCompany_Organisation9"):
                opp_val = getattr(old_value, "EvoCompany_Organisation9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EvoCompany_Organisation9"):
                opp_val = getattr(value, "EvoCompany_Organisation9", None)
                if opp_val is None:
                    setattr(value, "EvoCompany_Organisation9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Division:

    pass
class EvoCompany_ServiceLine(Division):

    pass
class Person:

    pass
class EvoCompany_Client(Person):

    pass
class EvoCompany_Employee(Person):

    pass
class EvoCompany_CompanyModel:

    pass
class EvoCompany_Organisation:

    def __init__(self, name: str, city: str, completeAddress: str, EvoCompany_Organisation: set["EvoCompany_Person"] = None, EvoCompany_Organisation6: set["EvoCompany_Project"] = None, EvoCompany_Organisation15: "EvoCompany_CompanyModel" = None, EvoCompany_Organisation9: set["EvoCompany_Division"] = None):
        self.name = name
        self.city = city
        self.completeAddress = completeAddress
        self.EvoCompany_Organisation = EvoCompany_Organisation if EvoCompany_Organisation is not None else set()
        self.EvoCompany_Organisation6 = EvoCompany_Organisation6 if EvoCompany_Organisation6 is not None else set()
        self.EvoCompany_Organisation15 = EvoCompany_Organisation15
        self.EvoCompany_Organisation9 = EvoCompany_Organisation9 if EvoCompany_Organisation9 is not None else set()
        
    @property
    def completeAddress(self) -> str:
        return self.__completeAddress

    @completeAddress.setter
    def completeAddress(self, completeAddress: str):
        self.__completeAddress = completeAddress

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def EvoCompany_Organisation15(self):
        return self.__EvoCompany_Organisation15

    @EvoCompany_Organisation15.setter
    def EvoCompany_Organisation15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EvoCompany_Organisation__EvoCompany_Organisation15", None)
        self.__EvoCompany_Organisation15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EvoCompany_CompanyModel"):
                opp_val = getattr(old_value, "EvoCompany_CompanyModel", None)
                if opp_val == self:
                    setattr(old_value, "EvoCompany_CompanyModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EvoCompany_CompanyModel"):
                opp_val = getattr(value, "EvoCompany_CompanyModel", None)
                setattr(value, "EvoCompany_CompanyModel", self)

    @property
    def EvoCompany_Organisation6(self):
        return self.__EvoCompany_Organisation6

    @EvoCompany_Organisation6.setter
    def EvoCompany_Organisation6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EvoCompany_Organisation__EvoCompany_Organisation6", None)
        self.__EvoCompany_Organisation6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EvoCompany_Project7"):
                    opp_val = getattr(item, "EvoCompany_Project7", None)
                    
                    if opp_val == self:
                        setattr(item, "EvoCompany_Project7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EvoCompany_Project7"):
                    opp_val = getattr(item, "EvoCompany_Project7", None)
                    
                    setattr(item, "EvoCompany_Project7", self)
                    

    @property
    def EvoCompany_Organisation(self):
        return self.__EvoCompany_Organisation

    @EvoCompany_Organisation.setter
    def EvoCompany_Organisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EvoCompany_Organisation__EvoCompany_Organisation", None)
        self.__EvoCompany_Organisation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EvoCompany_Person4"):
                    opp_val = getattr(item, "EvoCompany_Person4", None)
                    
                    if opp_val == self:
                        setattr(item, "EvoCompany_Person4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EvoCompany_Person4"):
                    opp_val = getattr(item, "EvoCompany_Person4", None)
                    
                    setattr(item, "EvoCompany_Person4", self)
                    

    @property
    def EvoCompany_Organisation9(self):
        return self.__EvoCompany_Organisation9

    @EvoCompany_Organisation9.setter
    def EvoCompany_Organisation9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EvoCompany_Organisation__EvoCompany_Organisation9", None)
        self.__EvoCompany_Organisation9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EvoCompany_Division"):
                    opp_val = getattr(item, "EvoCompany_Division", None)
                    
                    if opp_val == self:
                        setattr(item, "EvoCompany_Division", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EvoCompany_Division"):
                    opp_val = getattr(item, "EvoCompany_Division", None)
                    
                    setattr(item, "EvoCompany_Division", self)
                    

class EvoCompany_Unit(Division):

    pass
class EvoCompany_Project:

    def __init__(self, name: str, budget: int, EvoCompany_Project: "EvoCompany_Person" = None, EvoCompany_Project7: "EvoCompany_Organisation" = None, EvoCompany_Project11: "EvoCompany_Topic" = None):
        self.name = name
        self.budget = budget
        self.EvoCompany_Project = EvoCompany_Project
        self.EvoCompany_Project7 = EvoCompany_Project7
        self.EvoCompany_Project11 = EvoCompany_Project11
        
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
    def EvoCompany_Project(self):
        return self.__EvoCompany_Project

    @EvoCompany_Project.setter
    def EvoCompany_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EvoCompany_Project__EvoCompany_Project", None)
        self.__EvoCompany_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EvoCompany_Person"):
                opp_val = getattr(old_value, "EvoCompany_Person", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EvoCompany_Person"):
                opp_val = getattr(value, "EvoCompany_Person", None)
                if opp_val is None:
                    setattr(value, "EvoCompany_Person", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EvoCompany_Project7(self):
        return self.__EvoCompany_Project7

    @EvoCompany_Project7.setter
    def EvoCompany_Project7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EvoCompany_Project__EvoCompany_Project7", None)
        self.__EvoCompany_Project7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EvoCompany_Organisation6"):
                opp_val = getattr(old_value, "EvoCompany_Organisation6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EvoCompany_Organisation6"):
                opp_val = getattr(value, "EvoCompany_Organisation6", None)
                if opp_val is None:
                    setattr(value, "EvoCompany_Organisation6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EvoCompany_Project11(self):
        return self.__EvoCompany_Project11

    @EvoCompany_Project11.setter
    def EvoCompany_Project11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EvoCompany_Project__EvoCompany_Project11", None)
        self.__EvoCompany_Project11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EvoCompany_Topic"):
                opp_val = getattr(old_value, "EvoCompany_Topic", None)
                if opp_val == self:
                    setattr(old_value, "EvoCompany_Topic", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EvoCompany_Topic"):
                opp_val = getattr(value, "EvoCompany_Topic", None)
                setattr(value, "EvoCompany_Topic", self)

class EvoCompany_Person(ABC):

    def __init__(self, fullName: str, EvoCompany_Person: set["EvoCompany_Project"] = None, EvoCompany_Person2: "EvoCompany_Unit" = None, EvoCompany_Person4: "EvoCompany_Organisation" = None):
        self.fullName = fullName
        self.EvoCompany_Person = EvoCompany_Person if EvoCompany_Person is not None else set()
        self.EvoCompany_Person2 = EvoCompany_Person2
        self.EvoCompany_Person4 = EvoCompany_Person4
        
    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    @property
    def EvoCompany_Person2(self):
        return self.__EvoCompany_Person2

    @EvoCompany_Person2.setter
    def EvoCompany_Person2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EvoCompany_Person__EvoCompany_Person2", None)
        self.__EvoCompany_Person2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EvoCompany_Unit"):
                opp_val = getattr(old_value, "EvoCompany_Unit", None)
                if opp_val == self:
                    setattr(old_value, "EvoCompany_Unit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EvoCompany_Unit"):
                opp_val = getattr(value, "EvoCompany_Unit", None)
                setattr(value, "EvoCompany_Unit", self)

    @property
    def EvoCompany_Person(self):
        return self.__EvoCompany_Person

    @EvoCompany_Person.setter
    def EvoCompany_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EvoCompany_Person__EvoCompany_Person", None)
        self.__EvoCompany_Person = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EvoCompany_Project"):
                    opp_val = getattr(item, "EvoCompany_Project", None)
                    
                    if opp_val == self:
                        setattr(item, "EvoCompany_Project", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EvoCompany_Project"):
                    opp_val = getattr(item, "EvoCompany_Project", None)
                    
                    setattr(item, "EvoCompany_Project", self)
                    

    @property
    def EvoCompany_Person4(self):
        return self.__EvoCompany_Person4

    @EvoCompany_Person4.setter
    def EvoCompany_Person4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EvoCompany_Person__EvoCompany_Person4", None)
        self.__EvoCompany_Person4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EvoCompany_Organisation"):
                opp_val = getattr(old_value, "EvoCompany_Organisation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EvoCompany_Organisation"):
                opp_val = getattr(value, "EvoCompany_Organisation", None)
                if opp_val is None:
                    setattr(value, "EvoCompany_Organisation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
