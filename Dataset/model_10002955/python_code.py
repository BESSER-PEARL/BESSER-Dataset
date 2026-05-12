from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Enumeration(Enum):
    pass

############################################
# Definition of Classes
############################################










class OutOfServiceMechanism:

    pass


class FloorButton:

    def __init__(self, direction: Enumeration, floor5: "Floor" = None):
        self.direction = direction
        self.floor5 = floor5
        
        pass
    @property
    def direction(self):
        return self.__direction
    @direction.setter
    def direction(self, direction: Enumeration):
        self.__direction = direction

    @property
    def floor5(self):
        return self.__floor5
    @floor5.setter
    def floor5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FloorButton__floor5", None)
        self.__floor5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "floorButton4"):
                opp_val = getattr(old_value, "floorButton4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "floorButton4"):
                opp_val = getattr(value, "floorButton4", None)
                if opp_val is None:
                    setattr(value, "floorButton4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Button_Interface:

    pass


class EmergencyButton:

    pass


class Elevator_Button:

    def __init__(self, floorID: int, elevator9: "Elevator" = None):
        self.floorID = floorID
        self.elevator9 = elevator9
        
        pass
    @property
    def floorID(self):
        return self.__floorID
    @floorID.setter
    def floorID(self, floorID: int):
        self.__floorID = floorID

    @property
    def elevator9(self):
        return self.__elevator9
    @elevator9.setter
    def elevator9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elevator_Button__elevator9", None)
        self.__elevator9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elevator_Button8"):
                opp_val = getattr(old_value, "elevator_Button8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elevator_Button8"):
                opp_val = getattr(value, "elevator_Button8", None)
                if opp_val is None:
                    setattr(value, "elevator_Button8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Queue:

    def __init__(self, currentDirection: Enumeration, floorQueue: int, elevator7: "Elevator" = None):
        self.currentDirection = currentDirection
        self.floorQueue = floorQueue
        self.elevator7 = elevator7
        
        pass
    @property
    def floorQueue(self):
        return self.__floorQueue
    @floorQueue.setter
    def floorQueue(self, floorQueue: int):
        self.__floorQueue = floorQueue

    @property
    def currentDirection(self):
        return self.__currentDirection
    @currentDirection.setter
    def currentDirection(self, currentDirection: Enumeration):
        self.__currentDirection = currentDirection

    @property
    def elevator7(self):
        return self.__elevator7
    @elevator7.setter
    def elevator7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Queue__elevator7", None)
        self.__elevator7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "queue6"):
                opp_val = getattr(old_value, "queue6", None)
                if opp_val == self:
                    setattr(old_value, "queue6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "queue6"):
                opp_val = getattr(value, "queue6", None)
                setattr(value, "queue6", self)



class Elevator:

    def __init__(self, emergencyButton: EmergencyButton, queue: Queue, outOfServiceMech: OutOfServiceMechanism, buttons: Elevator_Button, isOutOfService: bool, elevator_Button8: set["Elevator_Button"] = None, emergencyButton10: "EmergencyButton" = None, outOfServiceMechanism12: "OutOfServiceMechanism" = None, elevatorController1: "ElevatorController" = None, queue6: "Queue" = None):
        self.emergencyButton = emergencyButton
        self.queue = queue
        self.outOfServiceMech = outOfServiceMech
        self.buttons = buttons
        self.isOutOfService = isOutOfService
        self.elevator_Button8 = elevator_Button8 if elevator_Button8 is not None else set()
        self.emergencyButton10 = emergencyButton10
        self.outOfServiceMechanism12 = outOfServiceMechanism12
        self.elevatorController1 = elevatorController1
        self.queue6 = queue6
        
        pass
    @property
    def outOfServiceMech(self):
        return self.__outOfServiceMech
    @outOfServiceMech.setter
    def outOfServiceMech(self, outOfServiceMech: OutOfServiceMechanism):
        self.__outOfServiceMech = outOfServiceMech

    @property
    def buttons(self):
        return self.__buttons
    @buttons.setter
    def buttons(self, buttons: Elevator_Button):
        self.__buttons = buttons

    @property
    def isOutOfService(self):
        return self.__isOutOfService
    @isOutOfService.setter
    def isOutOfService(self, isOutOfService: bool):
        self.__isOutOfService = isOutOfService

    @property
    def emergencyButton(self):
        return self.__emergencyButton
    @emergencyButton.setter
    def emergencyButton(self, emergencyButton: EmergencyButton):
        self.__emergencyButton = emergencyButton

    @property
    def queue(self):
        return self.__queue
    @queue.setter
    def queue(self, queue: Queue):
        self.__queue = queue

    @property
    def emergencyButton10(self):
        return self.__emergencyButton10
    @emergencyButton10.setter
    def emergencyButton10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elevator__emergencyButton10", None)
        self.__emergencyButton10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elevator11"):
                opp_val = getattr(old_value, "elevator11", None)
                if opp_val == self:
                    setattr(old_value, "elevator11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elevator11"):
                opp_val = getattr(value, "elevator11", None)
                setattr(value, "elevator11", self)

    @property
    def queue6(self):
        return self.__queue6
    @queue6.setter
    def queue6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elevator__queue6", None)
        self.__queue6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elevator7"):
                opp_val = getattr(old_value, "elevator7", None)
                if opp_val == self:
                    setattr(old_value, "elevator7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elevator7"):
                opp_val = getattr(value, "elevator7", None)
                setattr(value, "elevator7", self)

    @property
    def elevator_Button8(self):
        return self.__elevator_Button8
    @elevator_Button8.setter
    def elevator_Button8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elevator__elevator_Button8", None)
        self.__elevator_Button8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "elevator9"):
                    opp_val = getattr(item, "elevator9", None)
                    
                    if opp_val == self:
                        setattr(item, "elevator9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elevator9"):
                    opp_val = getattr(item, "elevator9", None)
                    
                    setattr(item, "elevator9", self)
                    

    @property
    def elevatorController1(self):
        return self.__elevatorController1
    @elevatorController1.setter
    def elevatorController1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elevator__elevatorController1", None)
        self.__elevatorController1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elevator0"):
                opp_val = getattr(old_value, "elevator0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elevator0"):
                opp_val = getattr(value, "elevator0", None)
                if opp_val is None:
                    setattr(value, "elevator0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outOfServiceMechanism12(self):
        return self.__outOfServiceMechanism12
    @outOfServiceMechanism12.setter
    def outOfServiceMechanism12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elevator__outOfServiceMechanism12", None)
        self.__outOfServiceMechanism12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elevator13"):
                opp_val = getattr(old_value, "elevator13", None)
                if opp_val == self:
                    setattr(old_value, "elevator13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elevator13"):
                opp_val = getattr(value, "elevator13", None)
                setattr(value, "elevator13", self)



class Floor:

    def __init__(self, floorID: int, floorButtons: FloorButton, elevatorController3: "ElevatorController" = None, floorButton4: set["FloorButton"] = None):
        self.floorID = floorID
        self.floorButtons = floorButtons
        self.elevatorController3 = elevatorController3
        self.floorButton4 = floorButton4 if floorButton4 is not None else set()
        
        pass
    @property
    def floorID(self):
        return self.__floorID
    @floorID.setter
    def floorID(self, floorID: int):
        self.__floorID = floorID

    @property
    def floorButtons(self):
        return self.__floorButtons
    @floorButtons.setter
    def floorButtons(self, floorButtons: FloorButton):
        self.__floorButtons = floorButtons

    @property
    def elevatorController3(self):
        return self.__elevatorController3
    @elevatorController3.setter
    def elevatorController3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Floor__elevatorController3", None)
        self.__elevatorController3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "floor2"):
                opp_val = getattr(old_value, "floor2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "floor2"):
                opp_val = getattr(value, "floor2", None)
                if opp_val is None:
                    setattr(value, "floor2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def floorButton4(self):
        return self.__floorButton4
    @floorButton4.setter
    def floorButton4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Floor__floorButton4", None)
        self.__floorButton4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "floor5"):
                    opp_val = getattr(item, "floor5", None)
                    
                    if opp_val == self:
                        setattr(item, "floor5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "floor5"):
                    opp_val = getattr(item, "floor5", None)
                    
                    setattr(item, "floor5", self)
                    



class ElevatorController:

    def __init__(self, floors: Floor, elevators: Elevator, elevator0: set["Elevator"] = None, floor2: set["Floor"] = None):
        self.floors = floors
        self.elevators = elevators
        self.elevator0 = elevator0 if elevator0 is not None else set()
        self.floor2 = floor2 if floor2 is not None else set()
        
        pass
    @property
    def floors(self):
        return self.__floors
    @floors.setter
    def floors(self, floors: Floor):
        self.__floors = floors

    @property
    def elevators(self):
        return self.__elevators
    @elevators.setter
    def elevators(self, elevators: Elevator):
        self.__elevators = elevators

    @property
    def elevator0(self):
        return self.__elevator0
    @elevator0.setter
    def elevator0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ElevatorController__elevator0", None)
        self.__elevator0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "elevatorController1"):
                    opp_val = getattr(item, "elevatorController1", None)
                    
                    if opp_val == self:
                        setattr(item, "elevatorController1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elevatorController1"):
                    opp_val = getattr(item, "elevatorController1", None)
                    
                    setattr(item, "elevatorController1", self)
                    

    @property
    def floor2(self):
        return self.__floor2
    @floor2.setter
    def floor2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ElevatorController__floor2", None)
        self.__floor2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "elevatorController3"):
                    opp_val = getattr(item, "elevatorController3", None)
                    
                    if opp_val == self:
                        setattr(item, "elevatorController3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elevatorController3"):
                    opp_val = getattr(item, "elevatorController3", None)
                    
                    setattr(item, "elevatorController3", self)
                    

