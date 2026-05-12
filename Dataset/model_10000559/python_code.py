from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class genmymodelreverse_java_lang_Exception:

    pass


class hw3_Passenger:

    def __init__(self, UNDEFINED_FLOOR: int, id: int, currentFloor: int, destinationFloor: int, floor0: "hw3_Floor" = None, elevator2: "hw3_Elevator" = None, floor8: "hw3_Floor" = None, floor10: "hw3_Floor" = None):
        self.UNDEFINED_FLOOR = UNDEFINED_FLOOR
        self.id = id
        self.currentFloor = currentFloor
        self.destinationFloor = destinationFloor
        self.floor0 = floor0
        self.elevator2 = elevator2
        self.floor8 = floor8
        self.floor10 = floor10
        
        pass
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
    def UNDEFINED_FLOOR(self):
        return self.__UNDEFINED_FLOOR
    @UNDEFINED_FLOOR.setter
    def UNDEFINED_FLOOR(self, UNDEFINED_FLOOR: int):
        self.__UNDEFINED_FLOOR = UNDEFINED_FLOOR

    @property
    def destinationFloor(self):
        return self.__destinationFloor
    @destinationFloor.setter
    def destinationFloor(self, destinationFloor: int):
        self.__destinationFloor = destinationFloor

    @property
    def elevator2(self):
        return self.__elevator2
    @elevator2.setter
    def elevator2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw3_Passenger__elevator2", None)
        self.__elevator2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "boardedPassengers3"):
                opp_val = getattr(old_value, "boardedPassengers3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "boardedPassengers3"):
                opp_val = getattr(value, "boardedPassengers3", None)
                if opp_val is None:
                    setattr(value, "boardedPassengers3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def floor8(self):
        return self.__floor8
    @floor8.setter
    def floor8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw3_Passenger__floor8", None)
        self.__floor8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "residents9"):
                opp_val = getattr(old_value, "residents9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "residents9"):
                opp_val = getattr(value, "residents9", None)
                if opp_val is None:
                    setattr(value, "residents9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def floor0(self):
        return self.__floor0
    @floor0.setter
    def floor0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw3_Passenger__floor0", None)
        self.__floor0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "upwardBound1"):
                opp_val = getattr(old_value, "upwardBound1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "upwardBound1"):
                opp_val = getattr(value, "upwardBound1", None)
                if opp_val is None:
                    setattr(value, "upwardBound1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def floor10(self):
        return self.__floor10
    @floor10.setter
    def floor10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw3_Passenger__floor10", None)
        self.__floor10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "downwardBound11"):
                opp_val = getattr(old_value, "downwardBound11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "downwardBound11"):
                opp_val = getattr(value, "downwardBound11", None)
                if opp_val is None:
                    setattr(value, "downwardBound11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class hw3_Floor:

    def __init__(self, passengersWaiting: int, myFloorNumber: int, upwardBound1: set["hw3_Passenger"] = None, residents9: set["hw3_Passenger"] = None, downwardBound11: set["hw3_Passenger"] = None):
        self.passengersWaiting = passengersWaiting
        self.myFloorNumber = myFloorNumber
        self.upwardBound1 = upwardBound1 if upwardBound1 is not None else set()
        self.residents9 = residents9 if residents9 is not None else set()
        self.downwardBound11 = downwardBound11 if downwardBound11 is not None else set()
        
        pass
    @property
    def myFloorNumber(self):
        return self.__myFloorNumber
    @myFloorNumber.setter
    def myFloorNumber(self, myFloorNumber: int):
        self.__myFloorNumber = myFloorNumber

    @property
    def passengersWaiting(self):
        return self.__passengersWaiting
    @passengersWaiting.setter
    def passengersWaiting(self, passengersWaiting: int):
        self.__passengersWaiting = passengersWaiting

    @property
    def residents9(self):
        return self.__residents9
    @residents9.setter
    def residents9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw3_Floor__residents9", None)
        self.__residents9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "floor8"):
                    opp_val = getattr(item, "floor8", None)
                    
                    if opp_val == self:
                        setattr(item, "floor8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "floor8"):
                    opp_val = getattr(item, "floor8", None)
                    
                    setattr(item, "floor8", self)
                    

    @property
    def upwardBound1(self):
        return self.__upwardBound1
    @upwardBound1.setter
    def upwardBound1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw3_Floor__upwardBound1", None)
        self.__upwardBound1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "floor0"):
                    opp_val = getattr(item, "floor0", None)
                    
                    if opp_val == self:
                        setattr(item, "floor0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "floor0"):
                    opp_val = getattr(item, "floor0", None)
                    
                    setattr(item, "floor0", self)
                    

    @property
    def downwardBound11(self):
        return self.__downwardBound11
    @downwardBound11.setter
    def downwardBound11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw3_Floor__downwardBound11", None)
        self.__downwardBound11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "floor10"):
                    opp_val = getattr(item, "floor10", None)
                    
                    if opp_val == self:
                        setattr(item, "floor10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "floor10"):
                    opp_val = getattr(item, "floor10", None)
                    
                    setattr(item, "floor10", self)
                    



class hw3_ElevatorFullException:

    pass


class hw3_Elevator:

    def __init__(self, NUMBER_OF_FLOORS: int, CAPACITY: int, currentFloorIndex: int, isGoingUp: bool, passengersToFloor: str, numOfPassengers: int, boardedPassengers3: set["hw3_Passenger"] = None, building4: "hw3_Building" = None, building7: "hw3_Building" = None):
        self.NUMBER_OF_FLOORS = NUMBER_OF_FLOORS
        self.CAPACITY = CAPACITY
        self.currentFloorIndex = currentFloorIndex
        self.isGoingUp = isGoingUp
        self.passengersToFloor = passengersToFloor
        self.numOfPassengers = numOfPassengers
        self.boardedPassengers3 = boardedPassengers3 if boardedPassengers3 is not None else set()
        self.building4 = building4
        self.building7 = building7
        
        pass
    @property
    def isGoingUp(self):
        return self.__isGoingUp
    @isGoingUp.setter
    def isGoingUp(self, isGoingUp: bool):
        self.__isGoingUp = isGoingUp

    @property
    def CAPACITY(self):
        return self.__CAPACITY
    @CAPACITY.setter
    def CAPACITY(self, CAPACITY: int):
        self.__CAPACITY = CAPACITY

    @property
    def passengersToFloor(self):
        return self.__passengersToFloor
    @passengersToFloor.setter
    def passengersToFloor(self, passengersToFloor: str):
        self.__passengersToFloor = passengersToFloor

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
    def numOfPassengers(self):
        return self.__numOfPassengers
    @numOfPassengers.setter
    def numOfPassengers(self, numOfPassengers: int):
        self.__numOfPassengers = numOfPassengers

    @property
    def boardedPassengers3(self):
        return self.__boardedPassengers3
    @boardedPassengers3.setter
    def boardedPassengers3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw3_Elevator__boardedPassengers3", None)
        self.__boardedPassengers3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "elevator2"):
                    opp_val = getattr(item, "elevator2", None)
                    
                    if opp_val == self:
                        setattr(item, "elevator2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elevator2"):
                    opp_val = getattr(item, "elevator2", None)
                    
                    setattr(item, "elevator2", self)
                    

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
    def building7(self):
        return self.__building7
    @building7.setter
    def building7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw3_Elevator__building7", None)
        self.__building7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elevator6"):
                opp_val = getattr(old_value, "elevator6", None)
                if opp_val == self:
                    setattr(old_value, "elevator6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elevator6"):
                opp_val = getattr(value, "elevator6", None)
                setattr(value, "elevator6", self)



class hw3_Building:

    def __init__(self, FLOORS: int, floors: str, elevator5: "hw3_Elevator" = None, elevator6: "hw3_Elevator" = None):
        self.FLOORS = FLOORS
        self.floors = floors
        self.elevator5 = elevator5
        self.elevator6 = elevator6
        
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
    def elevator6(self):
        return self.__elevator6
    @elevator6.setter
    def elevator6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_hw3_Building__elevator6", None)
        self.__elevator6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "building7"):
                opp_val = getattr(old_value, "building7", None)
                if opp_val == self:
                    setattr(old_value, "building7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "building7"):
                opp_val = getattr(value, "building7", None)
                setattr(value, "building7", self)

