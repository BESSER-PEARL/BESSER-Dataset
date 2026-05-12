from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Break_in:

    def __init__(self, Detect_Froce: bool):
        self.Detect_Froce = Detect_Froce
        
        pass
    @property
    def Detect_Froce(self):
        return self.__Detect_Froce
    @Detect_Froce.setter
    def Detect_Froce(self, Detect_Froce: bool):
        self.__Detect_Froce = Detect_Froce



class Light_Motion:

    def __init__(self, Detects_Obstruction: bool):
        self.Detects_Obstruction = Detects_Obstruction
        
        pass
    @property
    def Detects_Obstruction(self):
        return self.__Detects_Obstruction
    @Detects_Obstruction.setter
    def Detects_Obstruction(self, Detects_Obstruction: bool):
        self.__Detects_Obstruction = Detects_Obstruction



class Door_Status:

    def __init__(self, Door_Open: bool, Door_Close: str):
        self.Door_Open = Door_Open
        self.Door_Close = Door_Close
        
        pass
    @property
    def Door_Close(self):
        return self.__Door_Close
    @Door_Close.setter
    def Door_Close(self, Door_Close: str):
        self.__Door_Close = Door_Close

    @property
    def Door_Open(self):
        return self.__Door_Open
    @Door_Open.setter
    def Door_Open(self, Door_Open: bool):
        self.__Door_Open = Door_Open



class External_Component:

    def __init__(self, Sensor: bool):
        self.Sensor = Sensor
        
        pass
    @property
    def Sensor(self):
        return self.__Sensor
    @Sensor.setter
    def Sensor(self, Sensor: bool):
        self.__Sensor = Sensor



class In_house_Component:

    def __init__(self, Manufacture_Product: str, Quality: str):
        self.Manufacture_Product = Manufacture_Product
        self.Quality = Quality
        
        pass
    @property
    def Quality(self):
        return self.__Quality
    @Quality.setter
    def Quality(self, Quality: str):
        self.__Quality = Quality

    @property
    def Manufacture_Product(self):
        return self.__Manufacture_Product
    @Manufacture_Product.setter
    def Manufacture_Product(self, Manufacture_Product: str):
        self.__Manufacture_Product = Manufacture_Product



class T:

    pass


class Controlling_Circuit:

    def __init__(self, MIcro_processor: str, Software: str):
        self.MIcro_processor = MIcro_processor
        self.Software = Software
        
        pass
    @property
    def Software(self):
        return self.__Software
    @Software.setter
    def Software(self, Software: str):
        self.__Software = Software

    @property
    def MIcro_processor(self):
        return self.__MIcro_processor
    @MIcro_processor.setter
    def MIcro_processor(self, MIcro_processor: str):
        self.__MIcro_processor = MIcro_processor



class Rollers_Rails:

    def __init__(self, Good_Quality: str):
        self.Good_Quality = Good_Quality
        
        pass
    @property
    def Good_Quality(self):
        return self.__Good_Quality
    @Good_Quality.setter
    def Good_Quality(self, Good_Quality: str):
        self.__Good_Quality = Good_Quality



class Motor:

    def __init__(self, Durable: str, Suitable_Speed: str):
        self.Durable = Durable
        self.Suitable_Speed = Suitable_Speed
        
        pass
    @property
    def Suitable_Speed(self):
        return self.__Suitable_Speed
    @Suitable_Speed.setter
    def Suitable_Speed(self, Suitable_Speed: str):
        self.__Suitable_Speed = Suitable_Speed

    @property
    def Durable(self):
        return self.__Durable
    @Durable.setter
    def Durable(self, Durable: str):
        self.__Durable = Durable



class Remote_Controller_Interface:

    def __init__(self, Bluebooth: str, Control_Garade_Door: str):
        self.Bluebooth = Bluebooth
        self.Control_Garade_Door = Control_Garade_Door
        
        pass
    @property
    def Control_Garade_Door(self):
        return self.__Control_Garade_Door
    @Control_Garade_Door.setter
    def Control_Garade_Door(self, Control_Garade_Door: str):
        self.__Control_Garade_Door = Control_Garade_Door

    @property
    def Bluebooth(self):
        return self.__Bluebooth
    @Bluebooth.setter
    def Bluebooth(self, Bluebooth: str):
        self.__Bluebooth = Bluebooth



class Coil_Spring_Cables:

    def __init__(self, Spring_Stiffness: str):
        self.Spring_Stiffness = Spring_Stiffness
        
        pass
    @property
    def Spring_Stiffness(self):
        return self.__Spring_Stiffness
    @Spring_Stiffness.setter
    def Spring_Stiffness(self, Spring_Stiffness: str):
        self.__Spring_Stiffness = Spring_Stiffness



class Locks_Handles:

    def __init__(self, Durable: str, Secure: str):
        self.Durable = Durable
        self.Secure = Secure
        
        pass
    @property
    def Secure(self):
        return self.__Secure
    @Secure.setter
    def Secure(self, Secure: str):
        self.__Secure = Secure

    @property
    def Durable(self):
        return self.__Durable
    @Durable.setter
    def Durable(self, Durable: str):
        self.__Durable = Durable



class Swing_out:

    def __init__(self, Space_Clearance: str):
        self.Space_Clearance = Space_Clearance
        
        pass
    @property
    def Space_Clearance(self):
        return self.__Space_Clearance
    @Space_Clearance.setter
    def Space_Clearance(self, Space_Clearance: str):
        self.__Space_Clearance = Space_Clearance



class Rolling:

    def __init__(self, Minimum_Space: str):
        self.Minimum_Space = Minimum_Space
        
        pass
    @property
    def Minimum_Space(self):
        return self.__Minimum_Space
    @Minimum_Space.setter
    def Minimum_Space(self, Minimum_Space: str):
        self.__Minimum_Space = Minimum_Space



class Abstract_Component:

    def __init__(self, Type_Of_Component: str):
        self.Type_Of_Component = Type_Of_Component
        
        pass
    @property
    def Type_Of_Component(self):
        return self.__Type_Of_Component
    @Type_Of_Component.setter
    def Type_Of_Component(self, Type_Of_Component: str):
        self.__Type_Of_Component = Type_Of_Component



class Abstract_Door:

    def __init__(self, Automatic: str, Materials: str, Security: str):
        self.Automatic = Automatic
        self.Materials = Materials
        self.Security = Security
        
        pass
    @property
    def Automatic(self):
        return self.__Automatic
    @Automatic.setter
    def Automatic(self, Automatic: str):
        self.__Automatic = Automatic

    @property
    def Materials(self):
        return self.__Materials
    @Materials.setter
    def Materials(self, Materials: str):
        self.__Materials = Materials

    @property
    def Security(self):
        return self.__Security
    @Security.setter
    def Security(self, Security: str):
        self.__Security = Security

