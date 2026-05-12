from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class BankAccount:

    def __init__(self, owner: str, balance: str):
        self.owner = owner
        self.balance = balance
        
        pass
    @property
    def owner(self):
        return self.__owner
    @owner.setter
    def owner(self, owner: str):
        self.__owner = owner

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: str):
        self.__balance = balance



class Manufacturer:

    def __init__(self, brand: str, location: str, engine5: "Engine" = None, wheel7: "Wheel" = None):
        self.brand = brand
        self.location = location
        self.engine5 = engine5
        self.wheel7 = wheel7
        
        pass
    @property
    def brand(self):
        return self.__brand
    @brand.setter
    def brand(self, brand: str):
        self.__brand = brand

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def wheel7(self):
        return self.__wheel7
    @wheel7.setter
    def wheel7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manufacturer__wheel7", None)
        self.__wheel7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manufacturer6"):
                opp_val = getattr(old_value, "manufacturer6", None)
                if opp_val == self:
                    setattr(old_value, "manufacturer6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manufacturer6"):
                opp_val = getattr(value, "manufacturer6", None)
                setattr(value, "manufacturer6", self)

    @property
    def engine5(self):
        return self.__engine5
    @engine5.setter
    def engine5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manufacturer__engine5", None)
        self.__engine5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manufacturer4"):
                opp_val = getattr(old_value, "manufacturer4", None)
                if opp_val == self:
                    setattr(old_value, "manufacturer4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manufacturer4"):
                opp_val = getattr(value, "manufacturer4", None)
                setattr(value, "manufacturer4", self)



class Wheel:

    def __init__(self, manufacturer: Manufacturer, width: int, diameter: int, car3: "Car1" = None, manufacturer6: "Manufacturer" = None):
        self.manufacturer = manufacturer
        self.width = width
        self.diameter = diameter
        self.car3 = car3
        self.manufacturer6 = manufacturer6
        
        pass
    @property
    def manufacturer(self):
        return self.__manufacturer
    @manufacturer.setter
    def manufacturer(self, manufacturer: Manufacturer):
        self.__manufacturer = manufacturer

    @property
    def diameter(self):
        return self.__diameter
    @diameter.setter
    def diameter(self, diameter: int):
        self.__diameter = diameter

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def car3(self):
        return self.__car3
    @car3.setter
    def car3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Wheel__car3", None)
        self.__car3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wheel2"):
                opp_val = getattr(old_value, "wheel2", None)
                if opp_val == self:
                    setattr(old_value, "wheel2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wheel2"):
                opp_val = getattr(value, "wheel2", None)
                setattr(value, "wheel2", self)

    @property
    def manufacturer6(self):
        return self.__manufacturer6
    @manufacturer6.setter
    def manufacturer6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Wheel__manufacturer6", None)
        self.__manufacturer6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "wheel7"):
                opp_val = getattr(old_value, "wheel7", None)
                if opp_val == self:
                    setattr(old_value, "wheel7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "wheel7"):
                opp_val = getattr(value, "wheel7", None)
                setattr(value, "wheel7", self)



class Engine:

    def __init__(self, manufacturer: str, volume: int, power: int, rpm: int, weight: int, manufacturer4: "Manufacturer" = None, car1: "Car1" = None):
        self.manufacturer = manufacturer
        self.volume = volume
        self.power = power
        self.rpm = rpm
        self.weight = weight
        self.manufacturer4 = manufacturer4
        self.car1 = car1
        
        pass
    @property
    def volume(self):
        return self.__volume
    @volume.setter
    def volume(self, volume: int):
        self.__volume = volume

    @property
    def power(self):
        return self.__power
    @power.setter
    def power(self, power: int):
        self.__power = power

    @property
    def manufacturer(self):
        return self.__manufacturer
    @manufacturer.setter
    def manufacturer(self, manufacturer: str):
        self.__manufacturer = manufacturer

    @property
    def rpm(self):
        return self.__rpm
    @rpm.setter
    def rpm(self, rpm: int):
        self.__rpm = rpm

    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def manufacturer4(self):
        return self.__manufacturer4
    @manufacturer4.setter
    def manufacturer4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Engine__manufacturer4", None)
        self.__manufacturer4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "engine5"):
                opp_val = getattr(old_value, "engine5", None)
                if opp_val == self:
                    setattr(old_value, "engine5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "engine5"):
                opp_val = getattr(value, "engine5", None)
                setattr(value, "engine5", self)

    @property
    def car1(self):
        return self.__car1
    @car1.setter
    def car1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Engine__car1", None)
        self.__car1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "engine0"):
                opp_val = getattr(old_value, "engine0", None)
                if opp_val == self:
                    setattr(old_value, "engine0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "engine0"):
                opp_val = getattr(value, "engine0", None)
                setattr(value, "engine0", self)



class Car1:

    def __init__(self, model: str, engine: str, wheels: str, doors: int, width: int, length: int, height: int, engine0: "Engine" = None, wheel2: "Wheel" = None):
        self.model = model
        self.engine = engine
        self.wheels = wheels
        self.doors = doors
        self.width = width
        self.length = length
        self.height = height
        self.engine0 = engine0
        self.wheel2 = wheel2
        
        pass
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def engine(self):
        return self.__engine
    @engine.setter
    def engine(self, engine: str):
        self.__engine = engine

    @property
    def length(self):
        return self.__length
    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def doors(self):
        return self.__doors
    @doors.setter
    def doors(self, doors: int):
        self.__doors = doors

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def wheels(self):
        return self.__wheels
    @wheels.setter
    def wheels(self, wheels: str):
        self.__wheels = wheels

    @property
    def engine0(self):
        return self.__engine0
    @engine0.setter
    def engine0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Car1__engine0", None)
        self.__engine0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "car1"):
                opp_val = getattr(old_value, "car1", None)
                if opp_val == self:
                    setattr(old_value, "car1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "car1"):
                opp_val = getattr(value, "car1", None)
                setattr(value, "car1", self)

    @property
    def wheel2(self):
        return self.__wheel2
    @wheel2.setter
    def wheel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Car1__wheel2", None)
        self.__wheel2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "car3"):
                opp_val = getattr(old_value, "car3", None)
                if opp_val == self:
                    setattr(old_value, "car3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "car3"):
                opp_val = getattr(value, "car3", None)
                setattr(value, "car3", self)



class Car:

    def __init__(self, model: str, engine: str, wheels: str, doors: int, width: int, length: int, height: int):
        self.model = model
        self.engine = engine
        self.wheels = wheels
        self.doors = doors
        self.width = width
        self.length = length
        self.height = height
        
        pass
    @property
    def wheels(self):
        return self.__wheels
    @wheels.setter
    def wheels(self, wheels: str):
        self.__wheels = wheels

    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, width: int):
        self.__width = width

    @property
    def model(self):
        return self.__model
    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height: int):
        self.__height = height

    @property
    def length(self):
        return self.__length
    @length.setter
    def length(self, length: int):
        self.__length = length

    @property
    def engine(self):
        return self.__engine
    @engine.setter
    def engine(self, engine: str):
        self.__engine = engine

    @property
    def doors(self):
        return self.__doors
    @doors.setter
    def doors(self, doors: int):
        self.__doors = doors



class Book:

    def __init__(self, name: str, autor: str, realese_date: str, pages: int):
        self.name = name
        self.autor = autor
        self.realese_date = realese_date
        self.pages = pages
        
        pass
    @property
    def autor(self):
        return self.__autor
    @autor.setter
    def autor(self, autor: str):
        self.__autor = autor

    @property
    def pages(self):
        return self.__pages
    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def realese_date(self):
        return self.__realese_date
    @realese_date.setter
    def realese_date(self, realese_date: str):
        self.__realese_date = realese_date

