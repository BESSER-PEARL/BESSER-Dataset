from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Task:

    pass
class turtlebotmission_LineTask(Task):

    pass
class turtlebotmission_Task(ABC):

    pass
class turtlebotmission_ReturnToStartTask(Task):

    pass
class turtlebotmission_ShortestPathTask(Task):

    pass
class turtlebotmission_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class turtlebotmission_Area:

    def __init__(self, xmax: int, ymax: int, turtlebotmission_Area: "turtlebotmission_TurtleBot" = None):
        self.xmax = xmax
        self.ymax = ymax
        self.turtlebotmission_Area = turtlebotmission_Area
        
    @property
    def xmax(self) -> int:
        return self.__xmax

    @xmax.setter
    def xmax(self, xmax: int):
        self.__xmax = xmax

    @property
    def ymax(self) -> int:
        return self.__ymax

    @ymax.setter
    def ymax(self, ymax: int):
        self.__ymax = ymax

    @property
    def turtlebotmission_Area(self):
        return self.__turtlebotmission_Area

    @turtlebotmission_Area.setter
    def turtlebotmission_Area(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_turtlebotmission_Area__turtlebotmission_Area", None)
        self.__turtlebotmission_Area = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "turtlebotmission_TurtleBot"):
                opp_val = getattr(old_value, "turtlebotmission_TurtleBot", None)
                if opp_val == self:
                    setattr(old_value, "turtlebotmission_TurtleBot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "turtlebotmission_TurtleBot"):
                opp_val = getattr(value, "turtlebotmission_TurtleBot", None)
                setattr(value, "turtlebotmission_TurtleBot", self)

class NamedElement:

    pass
class turtlebotmission_Mission(NamedElement):

    pass
class turtlebotmission_WaypointType(NamedElement):

    pass
class turtlebotmission_WayPoint(NamedElement):

    def __init__(self, coord_x: int, coord_y: int, turtlebotmission_WayPoint: "turtlebotmission_TurtleBot" = None, turtlebotmission_WayPoint7: "turtlebotmission_TurtleBot" = None, turtlebotmission_WayPoint16: "turtlebotmission_LineTask" = None, turtlebotmission_WayPoint18: "turtlebotmission_ShortestPathTask" = None, turtlebotmission_WayPoint11: set["turtlebotmission_WaypointType"] = None):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.turtlebotmission_WayPoint = turtlebotmission_WayPoint
        self.turtlebotmission_WayPoint7 = turtlebotmission_WayPoint7
        self.turtlebotmission_WayPoint16 = turtlebotmission_WayPoint16
        self.turtlebotmission_WayPoint18 = turtlebotmission_WayPoint18
        self.turtlebotmission_WayPoint11 = turtlebotmission_WayPoint11 if turtlebotmission_WayPoint11 is not None else set()
        
    @property
    def coord_y(self) -> int:
        return self.__coord_y

    @coord_y.setter
    def coord_y(self, coord_y: int):
        self.__coord_y = coord_y

    @property
    def coord_x(self) -> int:
        return self.__coord_x

    @coord_x.setter
    def coord_x(self, coord_x: int):
        self.__coord_x = coord_x

    @property
    def turtlebotmission_WayPoint(self):
        return self.__turtlebotmission_WayPoint

    @turtlebotmission_WayPoint.setter
    def turtlebotmission_WayPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_turtlebotmission_WayPoint__turtlebotmission_WayPoint", None)
        self.__turtlebotmission_WayPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "turtlebotmission_TurtleBot4"):
                opp_val = getattr(old_value, "turtlebotmission_TurtleBot4", None)
                if opp_val == self:
                    setattr(old_value, "turtlebotmission_TurtleBot4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "turtlebotmission_TurtleBot4"):
                opp_val = getattr(value, "turtlebotmission_TurtleBot4", None)
                setattr(value, "turtlebotmission_TurtleBot4", self)

    @property
    def turtlebotmission_WayPoint7(self):
        return self.__turtlebotmission_WayPoint7

    @turtlebotmission_WayPoint7.setter
    def turtlebotmission_WayPoint7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_turtlebotmission_WayPoint__turtlebotmission_WayPoint7", None)
        self.__turtlebotmission_WayPoint7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "turtlebotmission_TurtleBot6"):
                opp_val = getattr(old_value, "turtlebotmission_TurtleBot6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "turtlebotmission_TurtleBot6"):
                opp_val = getattr(value, "turtlebotmission_TurtleBot6", None)
                if opp_val is None:
                    setattr(value, "turtlebotmission_TurtleBot6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def turtlebotmission_WayPoint18(self):
        return self.__turtlebotmission_WayPoint18

    @turtlebotmission_WayPoint18.setter
    def turtlebotmission_WayPoint18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_turtlebotmission_WayPoint__turtlebotmission_WayPoint18", None)
        self.__turtlebotmission_WayPoint18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "turtlebotmission_ShortestPathTask"):
                opp_val = getattr(old_value, "turtlebotmission_ShortestPathTask", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "turtlebotmission_ShortestPathTask"):
                opp_val = getattr(value, "turtlebotmission_ShortestPathTask", None)
                if opp_val is None:
                    setattr(value, "turtlebotmission_ShortestPathTask", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def turtlebotmission_WayPoint16(self):
        return self.__turtlebotmission_WayPoint16

    @turtlebotmission_WayPoint16.setter
    def turtlebotmission_WayPoint16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_turtlebotmission_WayPoint__turtlebotmission_WayPoint16", None)
        self.__turtlebotmission_WayPoint16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "turtlebotmission_LineTask"):
                opp_val = getattr(old_value, "turtlebotmission_LineTask", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "turtlebotmission_LineTask"):
                opp_val = getattr(value, "turtlebotmission_LineTask", None)
                if opp_val is None:
                    setattr(value, "turtlebotmission_LineTask", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def turtlebotmission_WayPoint11(self):
        return self.__turtlebotmission_WayPoint11

    @turtlebotmission_WayPoint11.setter
    def turtlebotmission_WayPoint11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_turtlebotmission_WayPoint__turtlebotmission_WayPoint11", None)
        self.__turtlebotmission_WayPoint11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "turtlebotmission_WaypointType12"):
                    opp_val = getattr(item, "turtlebotmission_WaypointType12", None)
                    
                    if opp_val == self:
                        setattr(item, "turtlebotmission_WaypointType12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "turtlebotmission_WaypointType12"):
                    opp_val = getattr(item, "turtlebotmission_WaypointType12", None)
                    
                    setattr(item, "turtlebotmission_WaypointType12", self)
                    

class turtlebotmission_TurtleBot(NamedElement):

    pass