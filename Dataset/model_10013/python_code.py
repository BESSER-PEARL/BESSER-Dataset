from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class cards(Enum):
    small = "small"
    medium = "medium"
    big = "big"


############################################
# Definition of Classes
############################################

class PublicSpace:

    pass
class maps_Square(PublicSpace):

    pass
class maps_Garden(PublicSpace):

    pass
class Road:

    pass
class maps_Boulevard(Road):

    pass
class maps_Pedestrian(Road):

    pass
class maps_Street(Road):

    pass
class maps_Road(ABC):

    def __init__(self, name: str, length: int, district: str, borderedBy: set["maps_PublicSpace"] = None, maps_Road6: "maps_Road" = None, maps_Road4: set["maps_Road"] = None, Road: "maps_PublicSpace" = None, maps_Road: "maps_map" = None):
        self.name = name
        self.length = length
        self.district = district
        self.borderedBy = borderedBy if borderedBy is not None else set()
        self.maps_Road6 = maps_Road6
        self.maps_Road4 = maps_Road4 if maps_Road4 is not None else set()
        self.Road = Road
        self.maps_Road = maps_Road
        
        pass
    @property
    def district(self):
        return self.__district

    @district.setter
    def district(self, district: str):
        self.__district = district


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, length: int):
        self.__length = length


    @property
    def maps_Road4(self):
        return self.__maps_Road4

    @maps_Road4.setter
    def maps_Road4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_maps_Road__maps_Road4", None)
        self.__maps_Road4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "maps_Road6"):
                    opp_val = getattr(item, "maps_Road6", None)
                    
                    if opp_val == self:
                        setattr(item, "maps_Road6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "maps_Road6"):
                    opp_val = getattr(item, "maps_Road6", None)
                    
                    setattr(item, "maps_Road6", self)
                    

    @property
    def borderedBy(self):
        return self.__borderedBy

    @borderedBy.setter
    def borderedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_maps_Road__borderedBy", None)
        self.__borderedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PublicSpace"):
                    opp_val = getattr(item, "PublicSpace", None)
                    
                    if opp_val == self:
                        setattr(item, "PublicSpace", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PublicSpace"):
                    opp_val = getattr(item, "PublicSpace", None)
                    
                    setattr(item, "PublicSpace", self)
                    

    @property
    def maps_Road(self):
        return self.__maps_Road

    @maps_Road.setter
    def maps_Road(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_maps_Road__maps_Road", None)
        self.__maps_Road = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "maps_map"):
                opp_val = getattr(old_value, "maps_map", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "maps_map"):
                opp_val = getattr(value, "maps_map", None)
                if opp_val is None:
                    setattr(value, "maps_map", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Road(self):
        return self.__Road

    @Road.setter
    def Road(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_maps_Road__Road", None)
        self.__Road = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "border"):
                opp_val = getattr(old_value, "border", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "border"):
                opp_val = getattr(value, "border", None)
                if opp_val is None:
                    setattr(value, "border", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def maps_Road6(self):
        return self.__maps_Road6

    @maps_Road6.setter
    def maps_Road6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_maps_Road__maps_Road6", None)
        self.__maps_Road6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "maps_Road4"):
                opp_val = getattr(old_value, "maps_Road4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "maps_Road4"):
                opp_val = getattr(value, "maps_Road4", None)
                if opp_val is None:
                    setattr(value, "maps_Road4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class maps_map:

    def __init__(self, name: str, isCity: bool, country: str, size: str, maps_map2: set["maps_PublicSpace"] = None, maps_map: set["maps_Road"] = None):
        self.name = name
        self.isCity = isCity
        self.country = country
        self.size = size
        self.maps_map2 = maps_map2 if maps_map2 is not None else set()
        self.maps_map = maps_map if maps_map is not None else set()
        
        pass
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size


    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def isCity(self):
        return self.__isCity

    @isCity.setter
    def isCity(self, isCity: bool):
        self.__isCity = isCity


    @property
    def maps_map2(self):
        return self.__maps_map2

    @maps_map2.setter
    def maps_map2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_maps_map__maps_map2", None)
        self.__maps_map2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "maps_PublicSpace"):
                    opp_val = getattr(item, "maps_PublicSpace", None)
                    
                    if opp_val == self:
                        setattr(item, "maps_PublicSpace", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "maps_PublicSpace"):
                    opp_val = getattr(item, "maps_PublicSpace", None)
                    
                    setattr(item, "maps_PublicSpace", self)
                    

    @property
    def maps_map(self):
        return self.__maps_map

    @maps_map.setter
    def maps_map(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_maps_map__maps_map", None)
        self.__maps_map = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "maps_Road"):
                    opp_val = getattr(item, "maps_Road", None)
                    
                    if opp_val == self:
                        setattr(item, "maps_Road", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "maps_Road"):
                    opp_val = getattr(item, "maps_Road", None)
                    
                    setattr(item, "maps_Road", self)
                    

class maps_PublicSpace(ABC):

    def __init__(self, name: str, maps_PublicSpace: "maps_map" = None, PublicSpace: "maps_Road" = None, border: set["maps_Road"] = None):
        self.name = name
        self.maps_PublicSpace = maps_PublicSpace
        self.PublicSpace = PublicSpace
        self.border = border if border is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def border(self):
        return self.__border

    @border.setter
    def border(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_maps_PublicSpace__border", None)
        self.__border = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Road"):
                    opp_val = getattr(item, "Road", None)
                    
                    if opp_val == self:
                        setattr(item, "Road", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Road"):
                    opp_val = getattr(item, "Road", None)
                    
                    setattr(item, "Road", self)
                    

    @property
    def maps_PublicSpace(self):
        return self.__maps_PublicSpace

    @maps_PublicSpace.setter
    def maps_PublicSpace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_maps_PublicSpace__maps_PublicSpace", None)
        self.__maps_PublicSpace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "maps_map2"):
                opp_val = getattr(old_value, "maps_map2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "maps_map2"):
                opp_val = getattr(value, "maps_map2", None)
                if opp_val is None:
                    setattr(value, "maps_map2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PublicSpace(self):
        return self.__PublicSpace

    @PublicSpace.setter
    def PublicSpace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_maps_PublicSpace__PublicSpace", None)
        self.__PublicSpace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "borderedBy"):
                opp_val = getattr(old_value, "borderedBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "borderedBy"):
                opp_val = getattr(value, "borderedBy", None)
                if opp_val is None:
                    setattr(value, "borderedBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
