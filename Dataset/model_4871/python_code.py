from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class collection_Person:

    pass
class collection_Category:

    pass
class collection_Organisation:

    pass
class collection_MetaTag:

    pass
class collection_Tag:

    pass
class ItemsCollection:

    pass
class collection_ManualCollection(ItemsCollection):

    def __init__(self):
        
    def addItem(self, item: str) -> str:
        # TODO: Implement addItem method
        pass

    def removeItem(self, item: str) -> str:
        # TODO: Implement removeItem method
        pass

class collection_RemoteCollection(ItemsCollection):

    def __init__(self, remoteURL: str):
        self.remoteURL = remoteURL
        
    @property
    def remoteURL(self) -> str:
        return self.__remoteURL

    @remoteURL.setter
    def remoteURL(self, remoteURL: str):
        self.__remoteURL = remoteURL

class collection_SmartInformationObjectCollection(ItemsCollection):

    def __init__(self, includePersons: str, includeOrganisations: str, includeContents: str, minimumAge: date, collection_SmartInformationObjectCollection: set["collection_Tag"] = None, collection_SmartInformationObjectCollection5: set["collection_Tag"] = None, collection_SmartInformationObjectCollection8: set["collection_MetaTag"] = None, collection_SmartInformationObjectCollection17: set["collection_Category"] = None, collection_SmartInformationObjectCollection20: set["collection_Person"] = None, collection_SmartInformationObjectCollection23: set["collection_Organisation"] = None, collection_SmartInformationObjectCollection25: set["collection_Organisation"] = None, collection_SmartInformationObjectCollection10: set["collection_Category"] = None, collection_SmartInformationObjectCollection12: set["collection_Person"] = None, collection_SmartInformationObjectCollection14: set["collection_MetaTag"] = None):
        self.includePersons = includePersons
        self.includeOrganisations = includeOrganisations
        self.includeContents = includeContents
        self.minimumAge = minimumAge
        self.collection_SmartInformationObjectCollection = collection_SmartInformationObjectCollection if collection_SmartInformationObjectCollection is not None else set()
        self.collection_SmartInformationObjectCollection5 = collection_SmartInformationObjectCollection5 if collection_SmartInformationObjectCollection5 is not None else set()
        self.collection_SmartInformationObjectCollection8 = collection_SmartInformationObjectCollection8 if collection_SmartInformationObjectCollection8 is not None else set()
        self.collection_SmartInformationObjectCollection17 = collection_SmartInformationObjectCollection17 if collection_SmartInformationObjectCollection17 is not None else set()
        self.collection_SmartInformationObjectCollection20 = collection_SmartInformationObjectCollection20 if collection_SmartInformationObjectCollection20 is not None else set()
        self.collection_SmartInformationObjectCollection23 = collection_SmartInformationObjectCollection23 if collection_SmartInformationObjectCollection23 is not None else set()
        self.collection_SmartInformationObjectCollection25 = collection_SmartInformationObjectCollection25 if collection_SmartInformationObjectCollection25 is not None else set()
        self.collection_SmartInformationObjectCollection10 = collection_SmartInformationObjectCollection10 if collection_SmartInformationObjectCollection10 is not None else set()
        self.collection_SmartInformationObjectCollection12 = collection_SmartInformationObjectCollection12 if collection_SmartInformationObjectCollection12 is not None else set()
        self.collection_SmartInformationObjectCollection14 = collection_SmartInformationObjectCollection14 if collection_SmartInformationObjectCollection14 is not None else set()
        
    @property
    def includeOrganisations(self) -> str:
        return self.__includeOrganisations

    @includeOrganisations.setter
    def includeOrganisations(self, includeOrganisations: str):
        self.__includeOrganisations = includeOrganisations

    @property
    def includePersons(self) -> str:
        return self.__includePersons

    @includePersons.setter
    def includePersons(self, includePersons: str):
        self.__includePersons = includePersons

    @property
    def minimumAge(self) -> date:
        return self.__minimumAge

    @minimumAge.setter
    def minimumAge(self, minimumAge: date):
        self.__minimumAge = minimumAge

    @property
    def includeContents(self) -> str:
        return self.__includeContents

    @includeContents.setter
    def includeContents(self, includeContents: str):
        self.__includeContents = includeContents

    @property
    def collection_SmartInformationObjectCollection12(self):
        return self.__collection_SmartInformationObjectCollection12

    @collection_SmartInformationObjectCollection12.setter
    def collection_SmartInformationObjectCollection12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_collection_SmartInformationObjectCollection__collection_SmartInformationObjectCollection12", None)
        self.__collection_SmartInformationObjectCollection12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "collection_Person"):
                    opp_val = getattr(item, "collection_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "collection_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "collection_Person"):
                    opp_val = getattr(item, "collection_Person", None)
                    
                    setattr(item, "collection_Person", self)
                    

    @property
    def collection_SmartInformationObjectCollection17(self):
        return self.__collection_SmartInformationObjectCollection17

    @collection_SmartInformationObjectCollection17.setter
    def collection_SmartInformationObjectCollection17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_collection_SmartInformationObjectCollection__collection_SmartInformationObjectCollection17", None)
        self.__collection_SmartInformationObjectCollection17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "collection_Category18"):
                    opp_val = getattr(item, "collection_Category18", None)
                    
                    if opp_val == self:
                        setattr(item, "collection_Category18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "collection_Category18"):
                    opp_val = getattr(item, "collection_Category18", None)
                    
                    setattr(item, "collection_Category18", self)
                    

    @property
    def collection_SmartInformationObjectCollection23(self):
        return self.__collection_SmartInformationObjectCollection23

    @collection_SmartInformationObjectCollection23.setter
    def collection_SmartInformationObjectCollection23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_collection_SmartInformationObjectCollection__collection_SmartInformationObjectCollection23", None)
        self.__collection_SmartInformationObjectCollection23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "collection_Organisation"):
                    opp_val = getattr(item, "collection_Organisation", None)
                    
                    if opp_val == self:
                        setattr(item, "collection_Organisation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "collection_Organisation"):
                    opp_val = getattr(item, "collection_Organisation", None)
                    
                    setattr(item, "collection_Organisation", self)
                    

    @property
    def collection_SmartInformationObjectCollection14(self):
        return self.__collection_SmartInformationObjectCollection14

    @collection_SmartInformationObjectCollection14.setter
    def collection_SmartInformationObjectCollection14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_collection_SmartInformationObjectCollection__collection_SmartInformationObjectCollection14", None)
        self.__collection_SmartInformationObjectCollection14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "collection_MetaTag15"):
                    opp_val = getattr(item, "collection_MetaTag15", None)
                    
                    if opp_val == self:
                        setattr(item, "collection_MetaTag15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "collection_MetaTag15"):
                    opp_val = getattr(item, "collection_MetaTag15", None)
                    
                    setattr(item, "collection_MetaTag15", self)
                    

    @property
    def collection_SmartInformationObjectCollection20(self):
        return self.__collection_SmartInformationObjectCollection20

    @collection_SmartInformationObjectCollection20.setter
    def collection_SmartInformationObjectCollection20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_collection_SmartInformationObjectCollection__collection_SmartInformationObjectCollection20", None)
        self.__collection_SmartInformationObjectCollection20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "collection_Person21"):
                    opp_val = getattr(item, "collection_Person21", None)
                    
                    if opp_val == self:
                        setattr(item, "collection_Person21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "collection_Person21"):
                    opp_val = getattr(item, "collection_Person21", None)
                    
                    setattr(item, "collection_Person21", self)
                    

    @property
    def collection_SmartInformationObjectCollection10(self):
        return self.__collection_SmartInformationObjectCollection10

    @collection_SmartInformationObjectCollection10.setter
    def collection_SmartInformationObjectCollection10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_collection_SmartInformationObjectCollection__collection_SmartInformationObjectCollection10", None)
        self.__collection_SmartInformationObjectCollection10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "collection_Category"):
                    opp_val = getattr(item, "collection_Category", None)
                    
                    if opp_val == self:
                        setattr(item, "collection_Category", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "collection_Category"):
                    opp_val = getattr(item, "collection_Category", None)
                    
                    setattr(item, "collection_Category", self)
                    

    @property
    def collection_SmartInformationObjectCollection5(self):
        return self.__collection_SmartInformationObjectCollection5

    @collection_SmartInformationObjectCollection5.setter
    def collection_SmartInformationObjectCollection5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_collection_SmartInformationObjectCollection__collection_SmartInformationObjectCollection5", None)
        self.__collection_SmartInformationObjectCollection5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "collection_Tag6"):
                    opp_val = getattr(item, "collection_Tag6", None)
                    
                    if opp_val == self:
                        setattr(item, "collection_Tag6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "collection_Tag6"):
                    opp_val = getattr(item, "collection_Tag6", None)
                    
                    setattr(item, "collection_Tag6", self)
                    

    @property
    def collection_SmartInformationObjectCollection25(self):
        return self.__collection_SmartInformationObjectCollection25

    @collection_SmartInformationObjectCollection25.setter
    def collection_SmartInformationObjectCollection25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_collection_SmartInformationObjectCollection__collection_SmartInformationObjectCollection25", None)
        self.__collection_SmartInformationObjectCollection25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "collection_Organisation26"):
                    opp_val = getattr(item, "collection_Organisation26", None)
                    
                    if opp_val == self:
                        setattr(item, "collection_Organisation26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "collection_Organisation26"):
                    opp_val = getattr(item, "collection_Organisation26", None)
                    
                    setattr(item, "collection_Organisation26", self)
                    

    @property
    def collection_SmartInformationObjectCollection(self):
        return self.__collection_SmartInformationObjectCollection

    @collection_SmartInformationObjectCollection.setter
    def collection_SmartInformationObjectCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_collection_SmartInformationObjectCollection__collection_SmartInformationObjectCollection", None)
        self.__collection_SmartInformationObjectCollection = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "collection_Tag"):
                    opp_val = getattr(item, "collection_Tag", None)
                    
                    if opp_val == self:
                        setattr(item, "collection_Tag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "collection_Tag"):
                    opp_val = getattr(item, "collection_Tag", None)
                    
                    setattr(item, "collection_Tag", self)
                    

    @property
    def collection_SmartInformationObjectCollection8(self):
        return self.__collection_SmartInformationObjectCollection8

    @collection_SmartInformationObjectCollection8.setter
    def collection_SmartInformationObjectCollection8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_collection_SmartInformationObjectCollection__collection_SmartInformationObjectCollection8", None)
        self.__collection_SmartInformationObjectCollection8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "collection_MetaTag"):
                    opp_val = getattr(item, "collection_MetaTag", None)
                    
                    if opp_val == self:
                        setattr(item, "collection_MetaTag", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "collection_MetaTag"):
                    opp_val = getattr(item, "collection_MetaTag", None)
                    
                    setattr(item, "collection_MetaTag", self)
                    

    def remove(self, item: str) -> str:
        # TODO: Implement remove method
        pass

    def addNegative(self, item: str) -> str:
        # TODO: Implement addNegative method
        pass

    def addPositive(self, item: str) -> str:
        # TODO: Implement addPositive method
        pass

class collection_DataSet:

    pass
class collection_Item:

    pass
class collection_ItemsCollection(ABC):

    pass