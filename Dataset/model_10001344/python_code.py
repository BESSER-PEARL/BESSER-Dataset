from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Direction(Enum):
    pass

############################################
# Definition of Classes
############################################










class Algorithm(ABC):

    def __init__(self, TimeBetweenFloors: str):
        self.TimeBetweenFloors = TimeBetweenFloors
        
        pass
    @property
    def TimeBetweenFloors(self):
        return self.__TimeBetweenFloors
    @TimeBetweenFloors.setter
    def TimeBetweenFloors(self, TimeBetweenFloors: str):
        self.__TimeBetweenFloors = TimeBetweenFloors



class Elevator:

    def __init__(self, ElevatorNumber: int, ElevatorBayNumber: int, CurrentFloor: int, FloorButtons: str, CurrentMovement: str, ArrivedAtFloor: str, button8: "Button" = None, floorButton0: set["FloorButton"] = None, elevatorBay3: "ElevatorBay" = None):
        self.ElevatorNumber = ElevatorNumber
        self.ElevatorBayNumber = ElevatorBayNumber
        self.CurrentFloor = CurrentFloor
        self.FloorButtons = FloorButtons
        self.CurrentMovement = CurrentMovement
        self.ArrivedAtFloor = ArrivedAtFloor
        self.button8 = button8
        self.floorButton0 = floorButton0 if floorButton0 is not None else set()
        self.elevatorBay3 = elevatorBay3
        
        pass
    @property
    def ElevatorNumber(self):
        return self.__ElevatorNumber
    @ElevatorNumber.setter
    def ElevatorNumber(self, ElevatorNumber: int):
        self.__ElevatorNumber = ElevatorNumber

    @property
    def CurrentMovement(self):
        return self.__CurrentMovement
    @CurrentMovement.setter
    def CurrentMovement(self, CurrentMovement: str):
        self.__CurrentMovement = CurrentMovement

    @property
    def ElevatorBayNumber(self):
        return self.__ElevatorBayNumber
    @ElevatorBayNumber.setter
    def ElevatorBayNumber(self, ElevatorBayNumber: int):
        self.__ElevatorBayNumber = ElevatorBayNumber

    @property
    def FloorButtons(self):
        return self.__FloorButtons
    @FloorButtons.setter
    def FloorButtons(self, FloorButtons: str):
        self.__FloorButtons = FloorButtons

    @property
    def ArrivedAtFloor(self):
        return self.__ArrivedAtFloor
    @ArrivedAtFloor.setter
    def ArrivedAtFloor(self, ArrivedAtFloor: str):
        self.__ArrivedAtFloor = ArrivedAtFloor

    @property
    def CurrentFloor(self):
        return self.__CurrentFloor
    @CurrentFloor.setter
    def CurrentFloor(self, CurrentFloor: int):
        self.__CurrentFloor = CurrentFloor

    @property
    def elevatorBay3(self):
        return self.__elevatorBay3
    @elevatorBay3.setter
    def elevatorBay3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elevator__elevatorBay3", None)
        self.__elevatorBay3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elevator2"):
                opp_val = getattr(old_value, "elevator2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elevator2"):
                opp_val = getattr(value, "elevator2", None)
                if opp_val is None:
                    setattr(value, "elevator2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def button8(self):
        return self.__button8
    @button8.setter
    def button8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elevator__button8", None)
        self.__button8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elevator9"):
                opp_val = getattr(old_value, "elevator9", None)
                if opp_val == self:
                    setattr(old_value, "elevator9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elevator9"):
                opp_val = getattr(value, "elevator9", None)
                setattr(value, "elevator9", self)

    @property
    def floorButton0(self):
        return self.__floorButton0
    @floorButton0.setter
    def floorButton0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elevator__floorButton0", None)
        self.__floorButton0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "elevator1"):
                    opp_val = getattr(item, "elevator1", None)
                    
                    if opp_val == self:
                        setattr(item, "elevator1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elevator1"):
                    opp_val = getattr(item, "elevator1", None)
                    
                    setattr(item, "elevator1", self)
                    



class Building:

    def __init__(self, ElevatorBays: str, Controller: Controller, elevatorBay6: set["ElevatorBay"] = None, controller10: "Controller" = None):
        self.ElevatorBays = ElevatorBays
        self.Controller = Controller
        self.elevatorBay6 = elevatorBay6 if elevatorBay6 is not None else set()
        self.controller10 = controller10
        
        pass
    @property
    def ElevatorBays(self):
        return self.__ElevatorBays
    @ElevatorBays.setter
    def ElevatorBays(self, ElevatorBays: str):
        self.__ElevatorBays = ElevatorBays

    @property
    def Controller(self):
        return self.__Controller
    @Controller.setter
    def Controller(self, Controller: Controller):
        self.__Controller = Controller

    @property
    def elevatorBay6(self):
        return self.__elevatorBay6
    @elevatorBay6.setter
    def elevatorBay6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Building__elevatorBay6", None)
        self.__elevatorBay6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "building7"):
                    opp_val = getattr(item, "building7", None)
                    
                    if opp_val == self:
                        setattr(item, "building7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "building7"):
                    opp_val = getattr(item, "building7", None)
                    
                    setattr(item, "building7", self)
                    

    @property
    def controller10(self):
        return self.__controller10
    @controller10.setter
    def controller10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Building__controller10", None)
        self.__controller10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "building11"):
                opp_val = getattr(old_value, "building11", None)
                if opp_val == self:
                    setattr(old_value, "building11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "building11"):
                opp_val = getattr(value, "building11", None)
                setattr(value, "building11", self)



class Controller:

    pass


class ElevatorBay:

    def __init__(self, Elevators: str, BayNumber: int, UpDownButtons: str, building7: "Building" = None, elevator2: set["Elevator"] = None, upDownButton4: set["UpDownButton"] = None):
        self.Elevators = Elevators
        self.BayNumber = BayNumber
        self.UpDownButtons = UpDownButtons
        self.building7 = building7
        self.elevator2 = elevator2 if elevator2 is not None else set()
        self.upDownButton4 = upDownButton4 if upDownButton4 is not None else set()
        
        pass
    @property
    def UpDownButtons(self):
        return self.__UpDownButtons
    @UpDownButtons.setter
    def UpDownButtons(self, UpDownButtons: str):
        self.__UpDownButtons = UpDownButtons

    @property
    def BayNumber(self):
        return self.__BayNumber
    @BayNumber.setter
    def BayNumber(self, BayNumber: int):
        self.__BayNumber = BayNumber

    @property
    def Elevators(self):
        return self.__Elevators
    @Elevators.setter
    def Elevators(self, Elevators: str):
        self.__Elevators = Elevators

    @property
    def upDownButton4(self):
        return self.__upDownButton4
    @upDownButton4.setter
    def upDownButton4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ElevatorBay__upDownButton4", None)
        self.__upDownButton4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "elevatorBay5"):
                    opp_val = getattr(item, "elevatorBay5", None)
                    
                    if opp_val == self:
                        setattr(item, "elevatorBay5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elevatorBay5"):
                    opp_val = getattr(item, "elevatorBay5", None)
                    
                    setattr(item, "elevatorBay5", self)
                    

    @property
    def building7(self):
        return self.__building7
    @building7.setter
    def building7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ElevatorBay__building7", None)
        self.__building7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elevatorBay6"):
                opp_val = getattr(old_value, "elevatorBay6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elevatorBay6"):
                opp_val = getattr(value, "elevatorBay6", None)
                if opp_val is None:
                    setattr(value, "elevatorBay6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def elevator2(self):
        return self.__elevator2
    @elevator2.setter
    def elevator2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ElevatorBay__elevator2", None)
        self.__elevator2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "elevatorBay3"):
                    opp_val = getattr(item, "elevatorBay3", None)
                    
                    if opp_val == self:
                        setattr(item, "elevatorBay3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "elevatorBay3"):
                    opp_val = getattr(item, "elevatorBay3", None)
                    
                    setattr(item, "elevatorBay3", self)
                    



class UpDownButton:

    def __init__(self, Direction: Direction, ElevatorBay: ElevatorBay, elevatorBay5: "ElevatorBay" = None):
        self.Direction = Direction
        self.ElevatorBay = ElevatorBay
        self.elevatorBay5 = elevatorBay5
        
        pass
    @property
    def Direction(self):
        return self.__Direction
    @Direction.setter
    def Direction(self, Direction: Direction):
        self.__Direction = Direction

    @property
    def ElevatorBay(self):
        return self.__ElevatorBay
    @ElevatorBay.setter
    def ElevatorBay(self, ElevatorBay: ElevatorBay):
        self.__ElevatorBay = ElevatorBay

    @property
    def elevatorBay5(self):
        return self.__elevatorBay5
    @elevatorBay5.setter
    def elevatorBay5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UpDownButton__elevatorBay5", None)
        self.__elevatorBay5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "upDownButton4"):
                opp_val = getattr(old_value, "upDownButton4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "upDownButton4"):
                opp_val = getattr(value, "upDownButton4", None)
                if opp_val is None:
                    setattr(value, "upDownButton4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class FloorButton:

    def __init__(self, Elevator: Elevator, elevator1: "Elevator" = None):
        self.Elevator = Elevator
        self.elevator1 = elevator1
        
        pass
    @property
    def Elevator(self):
        return self.__Elevator
    @Elevator.setter
    def Elevator(self, Elevator: Elevator):
        self.__Elevator = Elevator

    @property
    def elevator1(self):
        return self.__elevator1
    @elevator1.setter
    def elevator1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_FloorButton__elevator1", None)
        self.__elevator1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "floorButton0"):
                opp_val = getattr(old_value, "floorButton0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "floorButton0"):
                opp_val = getattr(value, "floorButton0", None)
                if opp_val is None:
                    setattr(value, "floorButton0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Button(ABC):

    def __init__(self, IsOn: bool, FloorNumber: int, Clicked: str, elevator9: "Elevator" = None):
        self.IsOn = IsOn
        self.FloorNumber = FloorNumber
        self.Clicked = Clicked
        self.elevator9 = elevator9
        
        pass
    @property
    def Clicked(self):
        return self.__Clicked
    @Clicked.setter
    def Clicked(self, Clicked: str):
        self.__Clicked = Clicked

    @property
    def IsOn(self):
        return self.__IsOn
    @IsOn.setter
    def IsOn(self, IsOn: bool):
        self.__IsOn = IsOn

    @property
    def FloorNumber(self):
        return self.__FloorNumber
    @FloorNumber.setter
    def FloorNumber(self, FloorNumber: int):
        self.__FloorNumber = FloorNumber

    @property
    def elevator9(self):
        return self.__elevator9
    @elevator9.setter
    def elevator9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Button__elevator9", None)
        self.__elevator9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "button8"):
                opp_val = getattr(old_value, "button8", None)
                if opp_val == self:
                    setattr(old_value, "button8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "button8"):
                opp_val = getattr(value, "button8", None)
                setattr(value, "button8", self)



class object:

    pass
