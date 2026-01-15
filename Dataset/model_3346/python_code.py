from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Map_Address:

    def __init__(self, longitude: float, latitude: float, description: str, name: str, telephone: str, downtown: bool, pictures: str, Map_Address: "Map_Map" = None):
        self.longitude = longitude
        self.latitude = latitude
        self.description = description
        self.name = name
        self.telephone = telephone
        self.downtown = downtown
        self.pictures = pictures
        self.Map_Address = Map_Address
        
    @property
    def longitude(self) -> float:
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude: float):
        self.__longitude = longitude

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def telephone(self) -> str:
        return self.__telephone

    @telephone.setter
    def telephone(self, telephone: str):
        self.__telephone = telephone

    @property
    def pictures(self) -> str:
        return self.__pictures

    @pictures.setter
    def pictures(self, pictures: str):
        self.__pictures = pictures

    @property
    def latitude(self) -> float:
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude: float):
        self.__latitude = latitude

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def downtown(self) -> bool:
        return self.__downtown

    @downtown.setter
    def downtown(self, downtown: bool):
        self.__downtown = downtown

    @property
    def Map_Address(self):
        return self.__Map_Address

    @Map_Address.setter
    def Map_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Map_Address__Map_Address", None)
        self.__Map_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Map_Map"):
                opp_val = getattr(old_value, "Map_Map", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Map_Map"):
                opp_val = getattr(value, "Map_Map", None)
                if opp_val is None:
                    setattr(value, "Map_Map", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Map_Map:

    pass