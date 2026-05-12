from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Enumeration2(Enum):
    pass
class Enumeration(Enum):
    pass

############################################
# Definition of Classes
############################################










class LocationManager:

    pass


class MyClass3:

    pass


class MyClass:

    pass


class DistanceInfo:

    def __init__(self, Distaince: str, ShortestPath: str, TraficInfo: str):
        self.Distaince = Distaince
        self.ShortestPath = ShortestPath
        self.TraficInfo = TraficInfo
        
        pass
    @property
    def Distaince(self):
        return self.__Distaince
    @Distaince.setter
    def Distaince(self, Distaince: str):
        self.__Distaince = Distaince

    @property
    def ShortestPath(self):
        return self.__ShortestPath
    @ShortestPath.setter
    def ShortestPath(self, ShortestPath: str):
        self.__ShortestPath = ShortestPath

    @property
    def TraficInfo(self):
        return self.__TraficInfo
    @TraficInfo.setter
    def TraficInfo(self, TraficInfo: str):
        self.__TraficInfo = TraficInfo



class LocationConnector_Interface:

    pass


class MyClass2:

    pass


class PlaceDetail:

    def __init__(self, DistanceInfo: DistanceInfo, Category: Category):
        self.DistanceInfo = DistanceInfo
        self.Category = Category
        
        pass
    @property
    def DistanceInfo(self):
        return self.__DistanceInfo
    @DistanceInfo.setter
    def DistanceInfo(self, DistanceInfo: DistanceInfo):
        self.__DistanceInfo = DistanceInfo

    @property
    def Category(self):
        return self.__Category
    @Category.setter
    def Category(self, Category: Category):
        self.__Category = Category



class Place:

    def __init__(self, Name: str, Details: str):
        self.Name = Name
        self.Details = Details
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Details(self):
        return self.__Details
    @Details.setter
    def Details(self, Details: str):
        self.__Details = Details



class Location:

    def __init__(self, Latitude: str, Longitude: str):
        self.Latitude = Latitude
        self.Longitude = Longitude
        
        pass
    @property
    def Latitude(self):
        return self.__Latitude
    @Latitude.setter
    def Latitude(self, Latitude: str):
        self.__Latitude = Latitude

    @property
    def Longitude(self):
        return self.__Longitude
    @Longitude.setter
    def Longitude(self, Longitude: str):
        self.__Longitude = Longitude



class Category:

    def __init__(self, Type: str, Name: str, Id: int):
        self.Type = Type
        self.Name = Name
        self.Id = Id
        
        pass
    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

