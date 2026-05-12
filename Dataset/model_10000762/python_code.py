from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Building:

    def __init__(self, Building: TKinter_Canvas, Panel: TKinter_Canvas, Elevator_list: Elevator_Elevator, Panel_list: Panel_Panel, panel4: "Panel_Panel" = None, elevator6: "Elevator_Elevator" = None, floor8: "Floor_Floor" = None):
        self.Building = Building
        self.Panel = Panel
        self.Elevator_list = Elevator_list
        self.Panel_list = Panel_list
        self.panel4 = panel4
        self.elevator6 = elevator6
        self.floor8 = floor8
        
        pass
    @property
    def Building(self):
        return self.__Building
    @Building.setter
    def Building(self, Building: TKinter_Canvas):
        self.__Building = Building

    @property
    def Panel_list(self):
        return self.__Panel_list
    @Panel_list.setter
    def Panel_list(self, Panel_list: Panel_Panel):
        self.__Panel_list = Panel_list

    @property
    def Elevator_list(self):
        return self.__Elevator_list
    @Elevator_list.setter
    def Elevator_list(self, Elevator_list: Elevator_Elevator):
        self.__Elevator_list = Elevator_list

    @property
    def Panel(self):
        return self.__Panel
    @Panel.setter
    def Panel(self, Panel: TKinter_Canvas):
        self.__Panel = Panel

    @property
    def floor8(self):
        return self.__floor8
    @floor8.setter
    def floor8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Building__floor8", None)
        self.__floor8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "building9"):
                opp_val = getattr(old_value, "building9", None)
                if opp_val == self:
                    setattr(old_value, "building9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "building9"):
                opp_val = getattr(value, "building9", None)
                setattr(value, "building9", self)

    @property
    def elevator6(self):
        return self.__elevator6
    @elevator6.setter
    def elevator6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Building__elevator6", None)
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

    @property
    def panel4(self):
        return self.__panel4
    @panel4.setter
    def panel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Building__panel4", None)
        self.__panel4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "building5"):
                opp_val = getattr(old_value, "building5", None)
                if opp_val == self:
                    setattr(old_value, "building5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "building5"):
                opp_val = getattr(value, "building5", None)
                setattr(value, "building5", self)



class Floor_Floor:

    def __init__(self, name: int, canvas: TKinter_Canvas, up_status: str, down_status: str, elevator2: "Elevator_Elevator" = None, building9: "Building" = None):
        self.name = name
        self.canvas = canvas
        self.up_status = up_status
        self.down_status = down_status
        self.elevator2 = elevator2
        self.building9 = building9
        
        pass
    @property
    def up_status(self):
        return self.__up_status
    @up_status.setter
    def up_status(self, up_status: str):
        self.__up_status = up_status

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: int):
        self.__name = name

    @property
    def down_status(self):
        return self.__down_status
    @down_status.setter
    def down_status(self, down_status: str):
        self.__down_status = down_status

    @property
    def canvas(self):
        return self.__canvas
    @canvas.setter
    def canvas(self, canvas: TKinter_Canvas):
        self.__canvas = canvas

    @property
    def building9(self):
        return self.__building9
    @building9.setter
    def building9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Floor_Floor__building9", None)
        self.__building9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "floor8"):
                opp_val = getattr(old_value, "floor8", None)
                if opp_val == self:
                    setattr(old_value, "floor8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "floor8"):
                opp_val = getattr(value, "floor8", None)
                setattr(value, "floor8", self)

    @property
    def elevator2(self):
        return self.__elevator2
    @elevator2.setter
    def elevator2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Floor_Floor__elevator2", None)
        self.__elevator2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "floor3"):
                opp_val = getattr(old_value, "floor3", None)
                if opp_val == self:
                    setattr(old_value, "floor3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "floor3"):
                opp_val = getattr(value, "floor3", None)
                setattr(value, "floor3", self)



class Elevator_Elevator:

    def __init__(self, Width: int, Height: int, Velocity: int, building: TKinter_Canvas, name: int, destination: int, body: TKinter_Canvas, call_queue: Floor_Floor, move_direction: str, gate_status: str, people: int, ready: bool, floor_list: Floor_Floor, panel1: "Panel_Panel" = None, floor3: "Floor_Floor" = None, building7: "Building" = None):
        self.Width = Width
        self.Height = Height
        self.Velocity = Velocity
        self.building = building
        self.name = name
        self.destination = destination
        self.body = body
        self.call_queue = call_queue
        self.move_direction = move_direction
        self.gate_status = gate_status
        self.people = people
        self.ready = ready
        self.floor_list = floor_list
        self.panel1 = panel1
        self.floor3 = floor3
        self.building7 = building7
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: int):
        self.__name = name

    @property
    def call_queue(self):
        return self.__call_queue
    @call_queue.setter
    def call_queue(self, call_queue: Floor_Floor):
        self.__call_queue = call_queue

    @property
    def building(self):
        return self.__building
    @building.setter
    def building(self, building: TKinter_Canvas):
        self.__building = building

    @property
    def body(self):
        return self.__body
    @body.setter
    def body(self, body: TKinter_Canvas):
        self.__body = body

    @property
    def Height(self):
        return self.__Height
    @Height.setter
    def Height(self, Height: int):
        self.__Height = Height

    @property
    def Width(self):
        return self.__Width
    @Width.setter
    def Width(self, Width: int):
        self.__Width = Width

    @property
    def gate_status(self):
        return self.__gate_status
    @gate_status.setter
    def gate_status(self, gate_status: str):
        self.__gate_status = gate_status

    @property
    def Velocity(self):
        return self.__Velocity
    @Velocity.setter
    def Velocity(self, Velocity: int):
        self.__Velocity = Velocity

    @property
    def destination(self):
        return self.__destination
    @destination.setter
    def destination(self, destination: int):
        self.__destination = destination

    @property
    def people(self):
        return self.__people
    @people.setter
    def people(self, people: int):
        self.__people = people

    @property
    def ready(self):
        return self.__ready
    @ready.setter
    def ready(self, ready: bool):
        self.__ready = ready

    @property
    def floor_list(self):
        return self.__floor_list
    @floor_list.setter
    def floor_list(self, floor_list: Floor_Floor):
        self.__floor_list = floor_list

    @property
    def move_direction(self):
        return self.__move_direction
    @move_direction.setter
    def move_direction(self, move_direction: str):
        self.__move_direction = move_direction

    @property
    def floor3(self):
        return self.__floor3
    @floor3.setter
    def floor3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elevator_Elevator__floor3", None)
        self.__floor3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elevator2"):
                opp_val = getattr(old_value, "elevator2", None)
                if opp_val == self:
                    setattr(old_value, "elevator2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elevator2"):
                opp_val = getattr(value, "elevator2", None)
                setattr(value, "elevator2", self)

    @property
    def building7(self):
        return self.__building7
    @building7.setter
    def building7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elevator_Elevator__building7", None)
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

    @property
    def panel1(self):
        return self.__panel1
    @panel1.setter
    def panel1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Elevator_Elevator__panel1", None)
        self.__panel1 = value
        
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



class Panel_Panel:

    def __init__(self, flag_list: bool, canvas: TKinter_Canvas, button_list: TKinter_Button, elevator0: "Elevator_Elevator" = None, building5: "Building" = None):
        self.flag_list = flag_list
        self.canvas = canvas
        self.button_list = button_list
        self.elevator0 = elevator0
        self.building5 = building5
        
        pass
    @property
    def flag_list(self):
        return self.__flag_list
    @flag_list.setter
    def flag_list(self, flag_list: bool):
        self.__flag_list = flag_list

    @property
    def button_list(self):
        return self.__button_list
    @button_list.setter
    def button_list(self, button_list: TKinter_Button):
        self.__button_list = button_list

    @property
    def canvas(self):
        return self.__canvas
    @canvas.setter
    def canvas(self, canvas: TKinter_Canvas):
        self.__canvas = canvas

    @property
    def building5(self):
        return self.__building5
    @building5.setter
    def building5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Panel_Panel__building5", None)
        self.__building5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "panel4"):
                opp_val = getattr(old_value, "panel4", None)
                if opp_val == self:
                    setattr(old_value, "panel4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "panel4"):
                opp_val = getattr(value, "panel4", None)
                setattr(value, "panel4", self)

    @property
    def elevator0(self):
        return self.__elevator0
    @elevator0.setter
    def elevator0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Panel_Panel__elevator0", None)
        self.__elevator0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "panel1"):
                opp_val = getattr(old_value, "panel1", None)
                if opp_val == self:
                    setattr(old_value, "panel1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "panel1"):
                opp_val = getattr(value, "panel1", None)
                setattr(value, "panel1", self)



class TKinter_Text:

    pass


class TKinter_TK:

    pass


class TKinter_Button:

    pass


class TKinter_Frame:

    pass


class TKinter_Canvas:

    pass
