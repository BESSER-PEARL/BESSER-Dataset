from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class Comparable_Patient__Interface:

    pass


class genmymodelreverse_java_lang_Object:

    pass


class genmymodelreverse_java_lang_Exception:

    pass


class genmymodelreverse_C1:

    pass


class genmymodelreverse_java_lang_Comparable_Interface(ABC):

    pass


class sec05_Patient:

    def __init__(self, urgencyIndex: int, person17: "sec05_Person" = None):
        self.urgencyIndex = urgencyIndex
        self.person17 = person17
        
        pass
    @property
    def urgencyIndex(self):
        return self.__urgencyIndex
    @urgencyIndex.setter
    def urgencyIndex(self, urgencyIndex: int):
        self.__urgencyIndex = urgencyIndex

    @property
    def person17(self):
        return self.__person17
    @person17.setter
    def person17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sec05_Patient__person17", None)
        self.__person17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient16"):
                opp_val = getattr(old_value, "patient16", None)
                if opp_val == self:
                    setattr(old_value, "patient16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient16"):
                opp_val = getattr(value, "patient16", None)
                setattr(value, "patient16", self)



class sec05_Person:

    def __init__(self, name: str, patient16: "sec05_Patient" = None):
        self.name = name
        self.patient16 = patient16
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def patient16(self):
        return self.__patient16
    @patient16.setter
    def patient16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sec05_Person__patient16", None)
        self.__patient16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "person17"):
                opp_val = getattr(old_value, "person17", None)
                if opp_val == self:
                    setattr(old_value, "person17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "person17"):
                opp_val = getattr(value, "person17", None)
                setattr(value, "person17", self)



class sec05_demoSec05:

    pass


class hw3test_HW3ElevatorSimulationTest:

    pass


class hw3_Passenger:

    def __init__(self, UNDEFINED_FLOOR: int, id: int, currentFloor: int, destinationFloor: int, floor2: "hw3_Floor" = None, floor6: "hw3_Floor" = None, elevator8: "hw3_Elevator" = None, floor18: "hw3_Floor" = None):
        self.UNDEFINED_FLOOR = UNDEFINED_FLOOR
        self.id = id
        self.currentFloor = currentFloor
        self.destinationFloor = destinationFloor
        self.floor2 = floor2
        self.floor6 = floor6
        self.elevator8 = elevator8
        self.floor18 = floor18
        
        pass
    @property
    def UNDEFINED_FLOOR(self):
        return self.__UNDEFINED_FLOOR
    @UNDEFINED_FLOOR.setter
    def UNDEFINED_FLOOR(self, UNDEFINED_FLOOR: int):
        self.__UNDEFINED_FLOOR = UNDEFINED_FLOOR

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def currentFloor(self):
        return self.__currentFloor
    @currentFloor.setter
    def currentFloor(self, currentFloor: int):
        self.__currentFloor = currentFloor

    @property
    def destinationFloor(self):
        return self.__destinationFloor
    @destinationFloor.setter
    def destinationFloor(self, destinationFloor: int):
        self.__destinationFloor = destinationFloor

    @property
    def floor18(self):
        return self.__floor18
    @floor18.setter
    def floor18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw3_Passenger__floor18", None)
        self.__floor18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "upwardBound19"):
                opp_val = getattr(old_value, "upwardBound19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "upwardBound19"):
                opp_val = getattr(value, "upwardBound19", None)
                if opp_val is None:
                    setattr(value, "upwardBound19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def elevator8(self):
        return self.__elevator8
    @elevator8.setter
    def elevator8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw3_Passenger__elevator8", None)
        self.__elevator8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boardedPassengers9"):
                opp_val = getattr(old_value, "boardedPassengers9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boardedPassengers9"):
                opp_val = getattr(value, "boardedPassengers9", None)
                if opp_val is None:
                    setattr(value, "boardedPassengers9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def floor2(self):
        return self.__floor2
    @floor2.setter
    def floor2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw3_Passenger__floor2", None)
        self.__floor2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "residents3"):
                opp_val = getattr(old_value, "residents3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "residents3"):
                opp_val = getattr(value, "residents3", None)
                if opp_val is None:
                    setattr(value, "residents3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def floor6(self):
        return self.__floor6
    @floor6.setter
    def floor6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw3_Passenger__floor6", None)
        self.__floor6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "downwardBound7"):
                opp_val = getattr(old_value, "downwardBound7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "downwardBound7"):
                opp_val = getattr(value, "downwardBound7", None)
                if opp_val is None:
                    setattr(value, "downwardBound7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class hw3_Floor:

    def __init__(self, passengersWaiting: int, myFloorNumber: int, residents3: set["hw3_Passenger"] = None, downwardBound7: set["hw3_Passenger"] = None, upwardBound19: set["hw3_Passenger"] = None):
        self.passengersWaiting = passengersWaiting
        self.myFloorNumber = myFloorNumber
        self.residents3 = residents3 if residents3 is not None else set()
        self.downwardBound7 = downwardBound7 if downwardBound7 is not None else set()
        self.upwardBound19 = upwardBound19 if upwardBound19 is not None else set()
        
        pass
    @property
    def passengersWaiting(self):
        return self.__passengersWaiting
    @passengersWaiting.setter
    def passengersWaiting(self, passengersWaiting: int):
        self.__passengersWaiting = passengersWaiting

    @property
    def myFloorNumber(self):
        return self.__myFloorNumber
    @myFloorNumber.setter
    def myFloorNumber(self, myFloorNumber: int):
        self.__myFloorNumber = myFloorNumber

    @property
    def upwardBound19(self):
        return self.__upwardBound19
    @upwardBound19.setter
    def upwardBound19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw3_Floor__upwardBound19", None)
        self.__upwardBound19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "floor18"):
                    opp_val = getattr(item, "floor18", None)
                    
                    if opp_val == self:
                        setattr(item, "floor18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "floor18"):
                    opp_val = getattr(item, "floor18", None)
                    
                    setattr(item, "floor18", self)
                    

    @property
    def residents3(self):
        return self.__residents3
    @residents3.setter
    def residents3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw3_Floor__residents3", None)
        self.__residents3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "floor2"):
                    opp_val = getattr(item, "floor2", None)
                    
                    if opp_val == self:
                        setattr(item, "floor2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "floor2"):
                    opp_val = getattr(item, "floor2", None)
                    
                    setattr(item, "floor2", self)
                    

    @property
    def downwardBound7(self):
        return self.__downwardBound7
    @downwardBound7.setter
    def downwardBound7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw3_Floor__downwardBound7", None)
        self.__downwardBound7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "floor6"):
                    opp_val = getattr(item, "floor6", None)
                    
                    if opp_val == self:
                        setattr(item, "floor6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "floor6"):
                    opp_val = getattr(item, "floor6", None)
                    
                    setattr(item, "floor6", self)
                    



class hw3_ElevatorFullException:

    pass


class hw3_Elevator:

    def __init__(self, NUMBER_OF_FLOORS: int, CAPACITY: int, currentFloorIndex: int, isGoingUp: bool, passengersToFloor: str, numOfPassengers: int, building1: "hw3_Building" = None, building4: "hw3_Building" = None, boardedPassengers9: set["hw3_Passenger"] = None):
        self.NUMBER_OF_FLOORS = NUMBER_OF_FLOORS
        self.CAPACITY = CAPACITY
        self.currentFloorIndex = currentFloorIndex
        self.isGoingUp = isGoingUp
        self.passengersToFloor = passengersToFloor
        self.numOfPassengers = numOfPassengers
        self.building1 = building1
        self.building4 = building4
        self.boardedPassengers9 = boardedPassengers9 if boardedPassengers9 is not None else set()
        
        pass
    @property
    def numOfPassengers(self):
        return self.__numOfPassengers
    @numOfPassengers.setter
    def numOfPassengers(self, numOfPassengers: int):
        self.__numOfPassengers = numOfPassengers

    @property
    def passengersToFloor(self):
        return self.__passengersToFloor
    @passengersToFloor.setter
    def passengersToFloor(self, passengersToFloor: str):
        self.__passengersToFloor = passengersToFloor

    @property
    def CAPACITY(self):
        return self.__CAPACITY
    @CAPACITY.setter
    def CAPACITY(self, CAPACITY: int):
        self.__CAPACITY = CAPACITY

    @property
    def NUMBER_OF_FLOORS(self):
        return self.__NUMBER_OF_FLOORS
    @NUMBER_OF_FLOORS.setter
    def NUMBER_OF_FLOORS(self, NUMBER_OF_FLOORS: int):
        self.__NUMBER_OF_FLOORS = NUMBER_OF_FLOORS

    @property
    def currentFloorIndex(self):
        return self.__currentFloorIndex
    @currentFloorIndex.setter
    def currentFloorIndex(self, currentFloorIndex: int):
        self.__currentFloorIndex = currentFloorIndex

    @property
    def isGoingUp(self):
        return self.__isGoingUp
    @isGoingUp.setter
    def isGoingUp(self, isGoingUp: bool):
        self.__isGoingUp = isGoingUp

    @property
    def boardedPassengers9(self):
        return self.__boardedPassengers9
    @boardedPassengers9.setter
    def boardedPassengers9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw3_Elevator__boardedPassengers9", None)
        self.__boardedPassengers9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "elevator8"):
                    opp_val = getattr(item, "elevator8", None)
                    
                    if opp_val == self:
                        setattr(item, "elevator8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elevator8"):
                    opp_val = getattr(item, "elevator8", None)
                    
                    setattr(item, "elevator8", self)
                    

    @property
    def building4(self):
        return self.__building4
    @building4.setter
    def building4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw3_Elevator__building4", None)
        self.__building4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elevator5"):
                opp_val = getattr(old_value, "elevator5", None)
                if opp_val == self:
                    setattr(old_value, "elevator5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elevator5"):
                opp_val = getattr(value, "elevator5", None)
                setattr(value, "elevator5", self)

    @property
    def building1(self):
        return self.__building1
    @building1.setter
    def building1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw3_Elevator__building1", None)
        self.__building1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elevator0"):
                opp_val = getattr(old_value, "elevator0", None)
                if opp_val == self:
                    setattr(old_value, "elevator0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elevator0"):
                opp_val = getattr(value, "elevator0", None)
                setattr(value, "elevator0", self)



class hw3_Building:

    def __init__(self, FLOORS: int, floors: str, elevator0: "hw3_Elevator" = None, elevator5: "hw3_Elevator" = None):
        self.FLOORS = FLOORS
        self.floors = floors
        self.elevator0 = elevator0
        self.elevator5 = elevator5
        
        pass
    @property
    def FLOORS(self):
        return self.__FLOORS
    @FLOORS.setter
    def FLOORS(self, FLOORS: int):
        self.__FLOORS = FLOORS

    @property
    def floors(self):
        return self.__floors
    @floors.setter
    def floors(self, floors: str):
        self.__floors = floors

    @property
    def elevator5(self):
        return self.__elevator5
    @elevator5.setter
    def elevator5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw3_Building__elevator5", None)
        self.__elevator5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "building4"):
                opp_val = getattr(old_value, "building4", None)
                if opp_val == self:
                    setattr(old_value, "building4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "building4"):
                opp_val = getattr(value, "building4", None)
                setattr(value, "building4", self)

    @property
    def elevator0(self):
        return self.__elevator0
    @elevator0.setter
    def elevator0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw3_Building__elevator0", None)
        self.__elevator0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "building1"):
                opp_val = getattr(old_value, "building1", None)
                if opp_val == self:
                    setattr(old_value, "building1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "building1"):
                opp_val = getattr(value, "building1", None)
                setattr(value, "building1", self)



class hw2test_HW2ElevatorSimulationTest:

    pass


class hw2_Floor:

    def __init__(self, passengersWaiting: int):
        self.passengersWaiting = passengersWaiting
        
        pass
    @property
    def passengersWaiting(self):
        return self.__passengersWaiting
    @passengersWaiting.setter
    def passengersWaiting(self, passengersWaiting: int):
        self.__passengersWaiting = passengersWaiting



class hw2_ElevatorFullException:

    pass


class hw2_Elevator:

    def __init__(self, NUMBER_OF_FLOORS: int, CAPACITY: int, currentFloorIndex: int, isGoingUp: bool, passengersToFloor: str, numOfPassengers: int, building13: "hw2_Building" = None, building14: "hw2_Building" = None):
        self.NUMBER_OF_FLOORS = NUMBER_OF_FLOORS
        self.CAPACITY = CAPACITY
        self.currentFloorIndex = currentFloorIndex
        self.isGoingUp = isGoingUp
        self.passengersToFloor = passengersToFloor
        self.numOfPassengers = numOfPassengers
        self.building13 = building13
        self.building14 = building14
        
        pass
    @property
    def numOfPassengers(self):
        return self.__numOfPassengers
    @numOfPassengers.setter
    def numOfPassengers(self, numOfPassengers: int):
        self.__numOfPassengers = numOfPassengers

    @property
    def passengersToFloor(self):
        return self.__passengersToFloor
    @passengersToFloor.setter
    def passengersToFloor(self, passengersToFloor: str):
        self.__passengersToFloor = passengersToFloor

    @property
    def isGoingUp(self):
        return self.__isGoingUp
    @isGoingUp.setter
    def isGoingUp(self, isGoingUp: bool):
        self.__isGoingUp = isGoingUp

    @property
    def currentFloorIndex(self):
        return self.__currentFloorIndex
    @currentFloorIndex.setter
    def currentFloorIndex(self, currentFloorIndex: int):
        self.__currentFloorIndex = currentFloorIndex

    @property
    def NUMBER_OF_FLOORS(self):
        return self.__NUMBER_OF_FLOORS
    @NUMBER_OF_FLOORS.setter
    def NUMBER_OF_FLOORS(self, NUMBER_OF_FLOORS: int):
        self.__NUMBER_OF_FLOORS = NUMBER_OF_FLOORS

    @property
    def CAPACITY(self):
        return self.__CAPACITY
    @CAPACITY.setter
    def CAPACITY(self, CAPACITY: int):
        self.__CAPACITY = CAPACITY

    @property
    def building14(self):
        return self.__building14
    @building14.setter
    def building14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw2_Elevator__building14", None)
        self.__building14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elevator15"):
                opp_val = getattr(old_value, "elevator15", None)
                if opp_val == self:
                    setattr(old_value, "elevator15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elevator15"):
                opp_val = getattr(value, "elevator15", None)
                setattr(value, "elevator15", self)

    @property
    def building13(self):
        return self.__building13
    @building13.setter
    def building13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw2_Elevator__building13", None)
        self.__building13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elevator12"):
                opp_val = getattr(old_value, "elevator12", None)
                if opp_val == self:
                    setattr(old_value, "elevator12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elevator12"):
                opp_val = getattr(value, "elevator12", None)
                setattr(value, "elevator12", self)



class hw2_Building:

    def __init__(self, FLOORS: int, floors: str, elevator12: "hw2_Elevator" = None, elevator15: "hw2_Elevator" = None):
        self.FLOORS = FLOORS
        self.floors = floors
        self.elevator12 = elevator12
        self.elevator15 = elevator15
        
        pass
    @property
    def floors(self):
        return self.__floors
    @floors.setter
    def floors(self, floors: str):
        self.__floors = floors

    @property
    def FLOORS(self):
        return self.__FLOORS
    @FLOORS.setter
    def FLOORS(self, FLOORS: int):
        self.__FLOORS = FLOORS

    @property
    def elevator12(self):
        return self.__elevator12
    @elevator12.setter
    def elevator12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw2_Building__elevator12", None)
        self.__elevator12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "building13"):
                opp_val = getattr(old_value, "building13", None)
                if opp_val == self:
                    setattr(old_value, "building13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "building13"):
                opp_val = getattr(value, "building13", None)
                setattr(value, "building13", self)

    @property
    def elevator15(self):
        return self.__elevator15
    @elevator15.setter
    def elevator15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw2_Building__elevator15", None)
        self.__elevator15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "building14"):
                opp_val = getattr(old_value, "building14", None)
                if opp_val == self:
                    setattr(old_value, "building14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "building14"):
                opp_val = getattr(value, "building14", None)
                setattr(value, "building14", self)



class elevatortest_Patient:

    def __init__(self, urgencyIndex: int, person11: "elevatortest_Person" = None):
        self.urgencyIndex = urgencyIndex
        self.person11 = person11
        
        pass
    @property
    def urgencyIndex(self):
        return self.__urgencyIndex
    @urgencyIndex.setter
    def urgencyIndex(self, urgencyIndex: int):
        self.__urgencyIndex = urgencyIndex

    @property
    def person11(self):
        return self.__person11
    @person11.setter
    def person11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_elevatortest_Patient__person11", None)
        self.__person11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient10"):
                opp_val = getattr(old_value, "patient10", None)
                if opp_val == self:
                    setattr(old_value, "patient10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient10"):
                opp_val = getattr(value, "patient10", None)
                setattr(value, "patient10", self)



class elevatortest_Person:

    def __init__(self, name: str, patient10: "elevatortest_Patient" = None):
        self.name = name
        self.patient10 = patient10
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def patient10(self):
        return self.__patient10
    @patient10.setter
    def patient10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_elevatortest_Person__patient10", None)
        self.__patient10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "person11"):
                opp_val = getattr(old_value, "person11", None)
                if opp_val == self:
                    setattr(old_value, "person11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "person11"):
                opp_val = getattr(value, "person11", None)
                setattr(value, "person11", self)



class elevatortest_ElevatorTest:

    pass


class elevator_Elevator:

    def __init__(self, NUMBER_OF_FLOORS: int, currentFloor: int, isGoingUp: bool, passengersToFloor: str, numOfPassengers: int):
        self.NUMBER_OF_FLOORS = NUMBER_OF_FLOORS
        self.currentFloor = currentFloor
        self.isGoingUp = isGoingUp
        self.passengersToFloor = passengersToFloor
        self.numOfPassengers = numOfPassengers
        
        pass
    @property
    def currentFloor(self):
        return self.__currentFloor
    @currentFloor.setter
    def currentFloor(self, currentFloor: int):
        self.__currentFloor = currentFloor

    @property
    def isGoingUp(self):
        return self.__isGoingUp
    @isGoingUp.setter
    def isGoingUp(self, isGoingUp: bool):
        self.__isGoingUp = isGoingUp

    @property
    def NUMBER_OF_FLOORS(self):
        return self.__NUMBER_OF_FLOORS
    @NUMBER_OF_FLOORS.setter
    def NUMBER_OF_FLOORS(self, NUMBER_OF_FLOORS: int):
        self.__NUMBER_OF_FLOORS = NUMBER_OF_FLOORS

    @property
    def numOfPassengers(self):
        return self.__numOfPassengers
    @numOfPassengers.setter
    def numOfPassengers(self, numOfPassengers: int):
        self.__numOfPassengers = numOfPassengers

    @property
    def passengersToFloor(self):
        return self.__passengersToFloor
    @passengersToFloor.setter
    def passengersToFloor(self, passengersToFloor: str):
        self.__passengersToFloor = passengersToFloor

