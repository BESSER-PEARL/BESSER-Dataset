from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Train:

    def __init__(self, milesPerHour: float, totalCars: int, freightTrain0: "FreightTrain" = None, passengerTrain2: "PassengerTrain" = None):
        self.milesPerHour = milesPerHour
        self.totalCars = totalCars
        self.freightTrain0 = freightTrain0
        self.passengerTrain2 = passengerTrain2
        
        pass
    @property
    def totalCars(self):
        return self.__totalCars
    @totalCars.setter
    def totalCars(self, totalCars: int):
        self.__totalCars = totalCars

    @property
    def milesPerHour(self):
        return self.__milesPerHour
    @milesPerHour.setter
    def milesPerHour(self, milesPerHour: float):
        self.__milesPerHour = milesPerHour

    @property
    def passengerTrain2(self):
        return self.__passengerTrain2
    @passengerTrain2.setter
    def passengerTrain2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Train__passengerTrain2", None)
        self.__passengerTrain2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "train3"):
                opp_val = getattr(old_value, "train3", None)
                if opp_val == self:
                    setattr(old_value, "train3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "train3"):
                opp_val = getattr(value, "train3", None)
                setattr(value, "train3", self)

    @property
    def freightTrain0(self):
        return self.__freightTrain0
    @freightTrain0.setter
    def freightTrain0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Train__freightTrain0", None)
        self.__freightTrain0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "train1"):
                opp_val = getattr(old_value, "train1", None)
                if opp_val == self:
                    setattr(old_value, "train1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "train1"):
                opp_val = getattr(value, "train1", None)
                setattr(value, "train1", self)



class Interface_Interface:

    pass


class MaglevCar:

    def __init__(self, NUMSEATS: int, numSeatsOccupied: int, maglev15: "Maglev" = None):
        self.NUMSEATS = NUMSEATS
        self.numSeatsOccupied = numSeatsOccupied
        self.maglev15 = maglev15
        
        pass
    @property
    def numSeatsOccupied(self):
        return self.__numSeatsOccupied
    @numSeatsOccupied.setter
    def numSeatsOccupied(self, numSeatsOccupied: int):
        self.__numSeatsOccupied = numSeatsOccupied

    @property
    def NUMSEATS(self):
        return self.__NUMSEATS
    @NUMSEATS.setter
    def NUMSEATS(self, NUMSEATS: int):
        self.__NUMSEATS = NUMSEATS

    @property
    def maglev15(self):
        return self.__maglev15
    @maglev15.setter
    def maglev15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MaglevCar__maglev15", None)
        self.__maglev15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "maglevCar14"):
                opp_val = getattr(old_value, "maglevCar14", None)
                if opp_val == self:
                    setattr(old_value, "maglevCar14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "maglevCar14"):
                opp_val = getattr(value, "maglevCar14", None)
                setattr(value, "maglevCar14", self)



class ElectricTrain:

    def __init__(self, MAXSPEED: float, passengerTrain9: "PassengerTrain" = None, engineCar10: "EngineCar" = None, passengerCar12: "PassengerCar" = None):
        self.MAXSPEED = MAXSPEED
        self.passengerTrain9 = passengerTrain9
        self.engineCar10 = engineCar10
        self.passengerCar12 = passengerCar12
        
        pass
    @property
    def MAXSPEED(self):
        return self.__MAXSPEED
    @MAXSPEED.setter
    def MAXSPEED(self, MAXSPEED: float):
        self.__MAXSPEED = MAXSPEED

    @property
    def passengerTrain9(self):
        return self.__passengerTrain9
    @passengerTrain9.setter
    def passengerTrain9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ElectricTrain__passengerTrain9", None)
        self.__passengerTrain9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "electricTrain8"):
                opp_val = getattr(old_value, "electricTrain8", None)
                if opp_val == self:
                    setattr(old_value, "electricTrain8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "electricTrain8"):
                opp_val = getattr(value, "electricTrain8", None)
                setattr(value, "electricTrain8", self)

    @property
    def passengerCar12(self):
        return self.__passengerCar12
    @passengerCar12.setter
    def passengerCar12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ElectricTrain__passengerCar12", None)
        self.__passengerCar12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "electricTrain13"):
                opp_val = getattr(old_value, "electricTrain13", None)
                if opp_val == self:
                    setattr(old_value, "electricTrain13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "electricTrain13"):
                opp_val = getattr(value, "electricTrain13", None)
                setattr(value, "electricTrain13", self)

    @property
    def engineCar10(self):
        return self.__engineCar10
    @engineCar10.setter
    def engineCar10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ElectricTrain__engineCar10", None)
        self.__engineCar10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "electricTrain11"):
                opp_val = getattr(old_value, "electricTrain11", None)
                if opp_val == self:
                    setattr(old_value, "electricTrain11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "electricTrain11"):
                opp_val = getattr(value, "electricTrain11", None)
                setattr(value, "electricTrain11", self)



class Maglev:

    def __init__(self, MAXSPEED: float, passengerTrain7: "PassengerTrain" = None, maglevCar14: "MaglevCar" = None):
        self.MAXSPEED = MAXSPEED
        self.passengerTrain7 = passengerTrain7
        self.maglevCar14 = maglevCar14
        
        pass
    @property
    def MAXSPEED(self):
        return self.__MAXSPEED
    @MAXSPEED.setter
    def MAXSPEED(self, MAXSPEED: float):
        self.__MAXSPEED = MAXSPEED

    @property
    def maglevCar14(self):
        return self.__maglevCar14
    @maglevCar14.setter
    def maglevCar14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Maglev__maglevCar14", None)
        self.__maglevCar14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "maglev15"):
                opp_val = getattr(old_value, "maglev15", None)
                if opp_val == self:
                    setattr(old_value, "maglev15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "maglev15"):
                opp_val = getattr(value, "maglev15", None)
                setattr(value, "maglev15", self)

    @property
    def passengerTrain7(self):
        return self.__passengerTrain7
    @passengerTrain7.setter
    def passengerTrain7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Maglev__passengerTrain7", None)
        self.__passengerTrain7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "maglev6"):
                opp_val = getattr(old_value, "maglev6", None)
                if opp_val == self:
                    setattr(old_value, "maglev6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "maglev6"):
                opp_val = getattr(value, "maglev6", None)
                setattr(value, "maglev6", self)



class ContainerCar:

    def __init__(self, cubicFeet: float, climateControlled: bool, temp: float, freightTrain4: "FreightTrain" = None):
        self.cubicFeet = cubicFeet
        self.climateControlled = climateControlled
        self.temp = temp
        self.freightTrain4 = freightTrain4
        
        pass
    @property
    def cubicFeet(self):
        return self.__cubicFeet
    @cubicFeet.setter
    def cubicFeet(self, cubicFeet: float):
        self.__cubicFeet = cubicFeet

    @property
    def temp(self):
        return self.__temp
    @temp.setter
    def temp(self, temp: float):
        self.__temp = temp

    @property
    def climateControlled(self):
        return self.__climateControlled
    @climateControlled.setter
    def climateControlled(self, climateControlled: bool):
        self.__climateControlled = climateControlled

    @property
    def freightTrain4(self):
        return self.__freightTrain4
    @freightTrain4.setter
    def freightTrain4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ContainerCar__freightTrain4", None)
        self.__freightTrain4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "containerCar5"):
                opp_val = getattr(old_value, "containerCar5", None)
                if opp_val == self:
                    setattr(old_value, "containerCar5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "containerCar5"):
                opp_val = getattr(value, "containerCar5", None)
                setattr(value, "containerCar5", self)



class PassengerCar:

    def __init__(self, NUMSEATS: int, numSeatsOccupied: int, electricTrain13: "ElectricTrain" = None):
        self.NUMSEATS = NUMSEATS
        self.numSeatsOccupied = numSeatsOccupied
        self.electricTrain13 = electricTrain13
        
        pass
    @property
    def NUMSEATS(self):
        return self.__NUMSEATS
    @NUMSEATS.setter
    def NUMSEATS(self, NUMSEATS: int):
        self.__NUMSEATS = NUMSEATS

    @property
    def numSeatsOccupied(self):
        return self.__numSeatsOccupied
    @numSeatsOccupied.setter
    def numSeatsOccupied(self, numSeatsOccupied: int):
        self.__numSeatsOccupied = numSeatsOccupied

    @property
    def electricTrain13(self):
        return self.__electricTrain13
    @electricTrain13.setter
    def electricTrain13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PassengerCar__electricTrain13", None)
        self.__electricTrain13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "passengerCar12"):
                opp_val = getattr(old_value, "passengerCar12", None)
                if opp_val == self:
                    setattr(old_value, "passengerCar12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "passengerCar12"):
                opp_val = getattr(value, "passengerCar12", None)
                setattr(value, "passengerCar12", self)



class EngineCar:

    def __init__(self, MAXSPEED: float, electricTrain11: "ElectricTrain" = None):
        self.MAXSPEED = MAXSPEED
        self.electricTrain11 = electricTrain11
        
        pass
    @property
    def MAXSPEED(self):
        return self.__MAXSPEED
    @MAXSPEED.setter
    def MAXSPEED(self, MAXSPEED: float):
        self.__MAXSPEED = MAXSPEED

    @property
    def electricTrain11(self):
        return self.__electricTrain11
    @electricTrain11.setter
    def electricTrain11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EngineCar__electricTrain11", None)
        self.__electricTrain11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "engineCar10"):
                opp_val = getattr(old_value, "engineCar10", None)
                if opp_val == self:
                    setattr(old_value, "engineCar10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "engineCar10"):
                opp_val = getattr(value, "engineCar10", None)
                setattr(value, "engineCar10", self)



class PassengerTrain:

    pass


class FreightTrain:

    def __init__(self, containerTrain: bool, train1: "Train" = None, containerCar5: "ContainerCar" = None):
        self.containerTrain = containerTrain
        self.train1 = train1
        self.containerCar5 = containerCar5
        
        pass
    @property
    def containerTrain(self):
        return self.__containerTrain
    @containerTrain.setter
    def containerTrain(self, containerTrain: bool):
        self.__containerTrain = containerTrain

    @property
    def containerCar5(self):
        return self.__containerCar5
    @containerCar5.setter
    def containerCar5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FreightTrain__containerCar5", None)
        self.__containerCar5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "freightTrain4"):
                opp_val = getattr(old_value, "freightTrain4", None)
                if opp_val == self:
                    setattr(old_value, "freightTrain4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "freightTrain4"):
                opp_val = getattr(value, "freightTrain4", None)
                setattr(value, "freightTrain4", self)

    @property
    def train1(self):
        return self.__train1
    @train1.setter
    def train1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FreightTrain__train1", None)
        self.__train1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "freightTrain0"):
                opp_val = getattr(old_value, "freightTrain0", None)
                if opp_val == self:
                    setattr(old_value, "freightTrain0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "freightTrain0"):
                opp_val = getattr(value, "freightTrain0", None)
                setattr(value, "freightTrain0", self)



class T:

    pass
