from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Test_Report:

    pass


class Passenger:

    def __init__(self, WEIGHT: int, START_FLOOR: int, DEST: int, carNum: int, waiting: bool, traveling: bool, readyToDie: bool, sim17: "Sim" = None):
        self.WEIGHT = WEIGHT
        self.START_FLOOR = START_FLOOR
        self.DEST = DEST
        self.carNum = carNum
        self.waiting = waiting
        self.traveling = traveling
        self.readyToDie = readyToDie
        self.sim17 = sim17
        
        pass
    @property
    def WEIGHT(self):
        return self.__WEIGHT
    @WEIGHT.setter
    def WEIGHT(self, WEIGHT: int):
        self.__WEIGHT = WEIGHT

    @property
    def traveling(self):
        return self.__traveling
    @traveling.setter
    def traveling(self, traveling: bool):
        self.__traveling = traveling

    @property
    def readyToDie(self):
        return self.__readyToDie
    @readyToDie.setter
    def readyToDie(self, readyToDie: bool):
        self.__readyToDie = readyToDie

    @property
    def carNum(self):
        return self.__carNum
    @carNum.setter
    def carNum(self, carNum: int):
        self.__carNum = carNum

    @property
    def waiting(self):
        return self.__waiting
    @waiting.setter
    def waiting(self, waiting: bool):
        self.__waiting = waiting

    @property
    def START_FLOOR(self):
        return self.__START_FLOOR
    @START_FLOOR.setter
    def START_FLOOR(self, START_FLOOR: int):
        self.__START_FLOOR = START_FLOOR

    @property
    def DEST(self):
        return self.__DEST
    @DEST.setter
    def DEST(self, DEST: int):
        self.__DEST = DEST

    @property
    def sim17(self):
        return self.__sim17
    @sim17.setter
    def sim17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Passenger__sim17", None)
        self.__sim17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "passenger16"):
                opp_val = getattr(old_value, "passenger16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "passenger16"):
                opp_val = getattr(value, "passenger16", None)
                if opp_val is None:
                    setattr(value, "passenger16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class CarCallBox:

    def __init__(self, buttons: str, car3: "Car" = None):
        self.buttons = buttons
        self.car3 = car3
        
        pass
    @property
    def buttons(self):
        return self.__buttons
    @buttons.setter
    def buttons(self, buttons: str):
        self.__buttons = buttons

    @property
    def car3(self):
        return self.__car3
    @car3.setter
    def car3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CarCallBox__car3", None)
        self.__car3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "carCallBox2"):
                opp_val = getattr(old_value, "carCallBox2", None)
                if opp_val == self:
                    setattr(old_value, "carCallBox2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "carCallBox2"):
                opp_val = getattr(value, "carCallBox2", None)
                setattr(value, "carCallBox2", self)



class Sim:

    def __init__(self, elevator: Controller, people: str, director14: "Controller" = None, passenger16: set["Passenger"] = None):
        self.elevator = elevator
        self.people = people
        self.director14 = director14
        self.passenger16 = passenger16 if passenger16 is not None else set()
        
        pass
    @property
    def elevator(self):
        return self.__elevator
    @elevator.setter
    def elevator(self, elevator: Controller):
        self.__elevator = elevator

    @property
    def people(self):
        return self.__people
    @people.setter
    def people(self, people: str):
        self.__people = people

    @property
    def passenger16(self):
        return self.__passenger16
    @passenger16.setter
    def passenger16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sim__passenger16", None)
        self.__passenger16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sim17"):
                    opp_val = getattr(item, "sim17", None)
                    
                    if opp_val == self:
                        setattr(item, "sim17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sim17"):
                    opp_val = getattr(item, "sim17", None)
                    
                    setattr(item, "sim17", self)
                    

    @property
    def director14(self):
        return self.__director14
    @director14.setter
    def director14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sim__director14", None)
        self.__director14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sim15"):
                opp_val = getattr(old_value, "sim15", None)
                if opp_val == self:
                    setattr(old_value, "sim15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sim15"):
                opp_val = getattr(value, "sim15", None)
                setattr(value, "sim15", self)



class BackgroundCallListener:

    pass


class BackgroundStopLoader:

    def __init__(self, stops: str, car1: "Car" = None):
        self.stops = stops
        self.car1 = car1
        
        pass
    @property
    def stops(self):
        return self.__stops
    @stops.setter
    def stops(self, stops: str):
        self.__stops = stops

    @property
    def car1(self):
        return self.__car1
    @car1.setter
    def car1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BackgroundStopLoader__car1", None)
        self.__car1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "backgroundStopLoader0"):
                opp_val = getattr(old_value, "backgroundStopLoader0", None)
                if opp_val == self:
                    setattr(old_value, "backgroundStopLoader0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "backgroundStopLoader0"):
                opp_val = getattr(value, "backgroundStopLoader0", None)
                setattr(value, "backgroundStopLoader0", self)



class array_enum_:

    pass


class FloorCallBox:

    def __init__(self, LOCATION: int, BUTTONS: array_enum_, floor9: "Floor" = None):
        self.LOCATION = LOCATION
        self.BUTTONS = BUTTONS
        self.floor9 = floor9
        
        pass
    @property
    def LOCATION(self):
        return self.__LOCATION
    @LOCATION.setter
    def LOCATION(self, LOCATION: int):
        self.__LOCATION = LOCATION

    @property
    def BUTTONS(self):
        return self.__BUTTONS
    @BUTTONS.setter
    def BUTTONS(self, BUTTONS: array_enum_):
        self.__BUTTONS = BUTTONS

    @property
    def floor9(self):
        return self.__floor9
    @floor9.setter
    def floor9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FloorCallBox__floor9", None)
        self.__floor9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "floorCallBox8"):
                opp_val = getattr(old_value, "floorCallBox8", None)
                if opp_val == self:
                    setattr(old_value, "floorCallBox8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "floorCallBox8"):
                opp_val = getattr(value, "floorCallBox8", None)
                setattr(value, "floorCallBox8", self)



class Controller:

    def __init__(self, callQueue: str, cars: str, floors: str, callAdmin: BackgroundCallListener, car12: set["Car"] = None, sim15: "Sim" = None, floor18: set["Floor"] = None, backgroundCallListener4: "BackgroundCallListener" = None, call6: set["Call"] = None):
        self.callQueue = callQueue
        self.cars = cars
        self.floors = floors
        self.callAdmin = callAdmin
        self.car12 = car12 if car12 is not None else set()
        self.sim15 = sim15
        self.floor18 = floor18 if floor18 is not None else set()
        self.backgroundCallListener4 = backgroundCallListener4
        self.call6 = call6 if call6 is not None else set()
        
        pass
    @property
    def callAdmin(self):
        return self.__callAdmin
    @callAdmin.setter
    def callAdmin(self, callAdmin: BackgroundCallListener):
        self.__callAdmin = callAdmin

    @property
    def cars(self):
        return self.__cars
    @cars.setter
    def cars(self, cars: str):
        self.__cars = cars

    @property
    def floors(self):
        return self.__floors
    @floors.setter
    def floors(self, floors: str):
        self.__floors = floors

    @property
    def callQueue(self):
        return self.__callQueue
    @callQueue.setter
    def callQueue(self, callQueue: str):
        self.__callQueue = callQueue

    @property
    def floor18(self):
        return self.__floor18
    @floor18.setter
    def floor18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Controller__floor18", None)
        self.__floor18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "director19"):
                    opp_val = getattr(item, "director19", None)
                    
                    if opp_val == self:
                        setattr(item, "director19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "director19"):
                    opp_val = getattr(item, "director19", None)
                    
                    setattr(item, "director19", self)
                    

    @property
    def backgroundCallListener4(self):
        return self.__backgroundCallListener4
    @backgroundCallListener4.setter
    def backgroundCallListener4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Controller__backgroundCallListener4", None)
        self.__backgroundCallListener4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "director5"):
                opp_val = getattr(old_value, "director5", None)
                if opp_val == self:
                    setattr(old_value, "director5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "director5"):
                opp_val = getattr(value, "director5", None)
                setattr(value, "director5", self)

    @property
    def car12(self):
        return self.__car12
    @car12.setter
    def car12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Controller__car12", None)
        self.__car12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "director13"):
                    opp_val = getattr(item, "director13", None)
                    
                    if opp_val == self:
                        setattr(item, "director13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "director13"):
                    opp_val = getattr(item, "director13", None)
                    
                    setattr(item, "director13", self)
                    

    @property
    def call6(self):
        return self.__call6
    @call6.setter
    def call6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Controller__call6", None)
        self.__call6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "director7"):
                    opp_val = getattr(item, "director7", None)
                    
                    if opp_val == self:
                        setattr(item, "director7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "director7"):
                    opp_val = getattr(item, "director7", None)
                    
                    setattr(item, "director7", self)
                    

    @property
    def sim15(self):
        return self.__sim15
    @sim15.setter
    def sim15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Controller__sim15", None)
        self.__sim15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "director14"):
                opp_val = getattr(old_value, "director14", None)
                if opp_val == self:
                    setattr(old_value, "director14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "director14"):
                opp_val = getattr(value, "director14", None)
                setattr(value, "director14", self)



class Call:

    def __init__(self, location: Floor, created: str, direction: str, car11: "Car" = None, director7: "Controller" = None):
        self.location = location
        self.created = created
        self.direction = direction
        self.car11 = car11
        self.director7 = director7
        
        pass
    @property
    def created(self):
        return self.__created
    @created.setter
    def created(self, created: str):
        self.__created = created

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: Floor):
        self.__location = location

    @property
    def direction(self):
        return self.__direction
    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def car11(self):
        return self.__car11
    @car11.setter
    def car11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Call__car11", None)
        self.__car11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "call10"):
                opp_val = getattr(old_value, "call10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "call10"):
                opp_val = getattr(value, "call10", None)
                if opp_val is None:
                    setattr(value, "call10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def director7(self):
        return self.__director7
    @director7.setter
    def director7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Call__director7", None)
        self.__director7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "call6"):
                opp_val = getattr(old_value, "call6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "call6"):
                opp_val = getattr(value, "call6", None)
                if opp_val is None:
                    setattr(value, "call6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Floor:

    def __init__(self, BOTTOM: int, TOP: int, number: int, LOCATION: int, box: FloorCallBox, director19: "Controller" = None, floorCallBox8: "FloorCallBox" = None):
        self.BOTTOM = BOTTOM
        self.TOP = TOP
        self.number = number
        self.LOCATION = LOCATION
        self.box = box
        self.director19 = director19
        self.floorCallBox8 = floorCallBox8
        
        pass
    @property
    def BOTTOM(self):
        return self.__BOTTOM
    @BOTTOM.setter
    def BOTTOM(self, BOTTOM: int):
        self.__BOTTOM = BOTTOM

    @property
    def TOP(self):
        return self.__TOP
    @TOP.setter
    def TOP(self, TOP: int):
        self.__TOP = TOP

    @property
    def LOCATION(self):
        return self.__LOCATION
    @LOCATION.setter
    def LOCATION(self, LOCATION: int):
        self.__LOCATION = LOCATION

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def box(self):
        return self.__box
    @box.setter
    def box(self, box: FloorCallBox):
        self.__box = box

    @property
    def director19(self):
        return self.__director19
    @director19.setter
    def director19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Floor__director19", None)
        self.__director19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "floor18"):
                opp_val = getattr(old_value, "floor18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "floor18"):
                opp_val = getattr(value, "floor18", None)
                if opp_val is None:
                    setattr(value, "floor18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def floorCallBox8(self):
        return self.__floorCallBox8
    @floorCallBox8.setter
    def floorCallBox8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Floor__floorCallBox8", None)
        self.__floorCallBox8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "floor9"):
                opp_val = getattr(old_value, "floor9", None)
                if opp_val == self:
                    setattr(old_value, "floor9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "floor9"):
                opp_val = getattr(value, "floor9", None)
                setattr(value, "floor9", self)



class Car:

    def __init__(self, WEIGHT_LIMIT: int, destination: Floor, direction: str, floorNum: int, location: int, stopQueue: str, destQueue: str, weightLoad: int, box: CarCallBox, stopLoader: BackgroundStopLoader, call10: set["Call"] = None, director13: "Controller" = None, backgroundStopLoader0: "BackgroundStopLoader" = None, carCallBox2: "CarCallBox" = None):
        self.WEIGHT_LIMIT = WEIGHT_LIMIT
        self.destination = destination
        self.direction = direction
        self.floorNum = floorNum
        self.location = location
        self.stopQueue = stopQueue
        self.destQueue = destQueue
        self.weightLoad = weightLoad
        self.box = box
        self.stopLoader = stopLoader
        self.call10 = call10 if call10 is not None else set()
        self.director13 = director13
        self.backgroundStopLoader0 = backgroundStopLoader0
        self.carCallBox2 = carCallBox2
        
        pass
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: int):
        self.__location = location

    @property
    def stopQueue(self):
        return self.__stopQueue
    @stopQueue.setter
    def stopQueue(self, stopQueue: str):
        self.__stopQueue = stopQueue

    @property
    def destQueue(self):
        return self.__destQueue
    @destQueue.setter
    def destQueue(self, destQueue: str):
        self.__destQueue = destQueue

    @property
    def floorNum(self):
        return self.__floorNum
    @floorNum.setter
    def floorNum(self, floorNum: int):
        self.__floorNum = floorNum

    @property
    def weightLoad(self):
        return self.__weightLoad
    @weightLoad.setter
    def weightLoad(self, weightLoad: int):
        self.__weightLoad = weightLoad

    @property
    def stopLoader(self):
        return self.__stopLoader
    @stopLoader.setter
    def stopLoader(self, stopLoader: BackgroundStopLoader):
        self.__stopLoader = stopLoader

    @property
    def box(self):
        return self.__box
    @box.setter
    def box(self, box: CarCallBox):
        self.__box = box

    @property
    def WEIGHT_LIMIT(self):
        return self.__WEIGHT_LIMIT
    @WEIGHT_LIMIT.setter
    def WEIGHT_LIMIT(self, WEIGHT_LIMIT: int):
        self.__WEIGHT_LIMIT = WEIGHT_LIMIT

    @property
    def destination(self):
        return self.__destination
    @destination.setter
    def destination(self, destination: Floor):
        self.__destination = destination

    @property
    def direction(self):
        return self.__direction
    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def backgroundStopLoader0(self):
        return self.__backgroundStopLoader0
    @backgroundStopLoader0.setter
    def backgroundStopLoader0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Car__backgroundStopLoader0", None)
        self.__backgroundStopLoader0 = value
        
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
    def director13(self):
        return self.__director13
    @director13.setter
    def director13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Car__director13", None)
        self.__director13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "car12"):
                opp_val = getattr(old_value, "car12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "car12"):
                opp_val = getattr(value, "car12", None)
                if opp_val is None:
                    setattr(value, "car12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def carCallBox2(self):
        return self.__carCallBox2
    @carCallBox2.setter
    def carCallBox2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Car__carCallBox2", None)
        self.__carCallBox2 = value
        
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

    @property
    def call10(self):
        return self.__call10
    @call10.setter
    def call10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Car__call10", None)
        self.__call10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "car11"):
                    opp_val = getattr(item, "car11", None)
                    
                    if opp_val == self:
                        setattr(item, "car11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "car11"):
                    opp_val = getattr(item, "car11", None)
                    
                    setattr(item, "car11", self)
                    

