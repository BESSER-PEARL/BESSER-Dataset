from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class ControlTask:

    pass
class mission_Join(ControlTask):

    pass
class mission_Fork(ControlTask):

    pass
class Task:

    pass
class mission_PointTask(Task):

    pass
class mission_PolygonTask(Task):

    pass
class mission_LineTask(Task):

    pass
class mission_ControlTask(Task):

    pass
class mission_Coordinate:

    def __init__(self, latitude: float, longitude: float, altitude: float, mission_Coordinate: "mission_Drone" = None, mission_Coordinate18: "mission_PolygonTask" = None, mission_Coordinate21: "mission_PolygonTask" = None, mission_Coordinate23: "mission_PointTask" = None, mission_Coordinate25: "mission_LineTask" = None, mission_Coordinate28: "mission_LineTask" = None, mission_Coordinate10: "mission_ControlTask" = None):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.mission_Coordinate = mission_Coordinate
        self.mission_Coordinate18 = mission_Coordinate18
        self.mission_Coordinate21 = mission_Coordinate21
        self.mission_Coordinate23 = mission_Coordinate23
        self.mission_Coordinate25 = mission_Coordinate25
        self.mission_Coordinate28 = mission_Coordinate28
        self.mission_Coordinate10 = mission_Coordinate10
        
    @property
    def longitude(self) -> float:
        return self.__longitude

    @longitude.setter
    def longitude(self, longitude: float):
        self.__longitude = longitude

    @property
    def altitude(self) -> float:
        return self.__altitude

    @altitude.setter
    def altitude(self, altitude: float):
        self.__altitude = altitude

    @property
    def latitude(self) -> float:
        return self.__latitude

    @latitude.setter
    def latitude(self, latitude: float):
        self.__latitude = latitude

    @property
    def mission_Coordinate25(self):
        return self.__mission_Coordinate25

    @mission_Coordinate25.setter
    def mission_Coordinate25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mission_Coordinate__mission_Coordinate25", None)
        self.__mission_Coordinate25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mission_LineTask"):
                opp_val = getattr(old_value, "mission_LineTask", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mission_LineTask"):
                opp_val = getattr(value, "mission_LineTask", None)
                if opp_val is None:
                    setattr(value, "mission_LineTask", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mission_Coordinate28(self):
        return self.__mission_Coordinate28

    @mission_Coordinate28.setter
    def mission_Coordinate28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mission_Coordinate__mission_Coordinate28", None)
        self.__mission_Coordinate28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mission_LineTask27"):
                opp_val = getattr(old_value, "mission_LineTask27", None)
                if opp_val == self:
                    setattr(old_value, "mission_LineTask27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mission_LineTask27"):
                opp_val = getattr(value, "mission_LineTask27", None)
                setattr(value, "mission_LineTask27", self)

    @property
    def mission_Coordinate10(self):
        return self.__mission_Coordinate10

    @mission_Coordinate10.setter
    def mission_Coordinate10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mission_Coordinate__mission_Coordinate10", None)
        self.__mission_Coordinate10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mission_ControlTask"):
                opp_val = getattr(old_value, "mission_ControlTask", None)
                if opp_val == self:
                    setattr(old_value, "mission_ControlTask", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mission_ControlTask"):
                opp_val = getattr(value, "mission_ControlTask", None)
                setattr(value, "mission_ControlTask", self)

    @property
    def mission_Coordinate(self):
        return self.__mission_Coordinate

    @mission_Coordinate.setter
    def mission_Coordinate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mission_Coordinate__mission_Coordinate", None)
        self.__mission_Coordinate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mission_Drone8"):
                opp_val = getattr(old_value, "mission_Drone8", None)
                if opp_val == self:
                    setattr(old_value, "mission_Drone8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mission_Drone8"):
                opp_val = getattr(value, "mission_Drone8", None)
                setattr(value, "mission_Drone8", self)

    @property
    def mission_Coordinate18(self):
        return self.__mission_Coordinate18

    @mission_Coordinate18.setter
    def mission_Coordinate18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mission_Coordinate__mission_Coordinate18", None)
        self.__mission_Coordinate18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mission_PolygonTask"):
                opp_val = getattr(old_value, "mission_PolygonTask", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mission_PolygonTask"):
                opp_val = getattr(value, "mission_PolygonTask", None)
                if opp_val is None:
                    setattr(value, "mission_PolygonTask", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mission_Coordinate21(self):
        return self.__mission_Coordinate21

    @mission_Coordinate21.setter
    def mission_Coordinate21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mission_Coordinate__mission_Coordinate21", None)
        self.__mission_Coordinate21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mission_PolygonTask20"):
                opp_val = getattr(old_value, "mission_PolygonTask20", None)
                if opp_val == self:
                    setattr(old_value, "mission_PolygonTask20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mission_PolygonTask20"):
                opp_val = getattr(value, "mission_PolygonTask20", None)
                setattr(value, "mission_PolygonTask20", self)

    @property
    def mission_Coordinate23(self):
        return self.__mission_Coordinate23

    @mission_Coordinate23.setter
    def mission_Coordinate23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mission_Coordinate__mission_Coordinate23", None)
        self.__mission_Coordinate23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mission_PointTask"):
                opp_val = getattr(old_value, "mission_PointTask", None)
                if opp_val == self:
                    setattr(old_value, "mission_PointTask", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mission_PointTask"):
                opp_val = getattr(value, "mission_PointTask", None)
                setattr(value, "mission_PointTask", self)

class mission_Swarm:

    pass
class NamedElement:

    pass
class mission_Task(NamedElement):

    pass
class mission_TaskDependency(NamedElement):

    pass
class mission_Drone(NamedElement):

    def __init__(self, type: str, returnHome: bool, mission_Drone: "mission_Swarm" = None, mission_Drone8: "mission_Coordinate" = None):
        self.type = type
        self.returnHome = returnHome
        self.mission_Drone = mission_Drone
        self.mission_Drone8 = mission_Drone8
        
    @property
    def returnHome(self) -> bool:
        return self.__returnHome

    @returnHome.setter
    def returnHome(self, returnHome: bool):
        self.__returnHome = returnHome

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mission_Drone8(self):
        return self.__mission_Drone8

    @mission_Drone8.setter
    def mission_Drone8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mission_Drone__mission_Drone8", None)
        self.__mission_Drone8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mission_Coordinate"):
                opp_val = getattr(old_value, "mission_Coordinate", None)
                if opp_val == self:
                    setattr(old_value, "mission_Coordinate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mission_Coordinate"):
                opp_val = getattr(value, "mission_Coordinate", None)
                setattr(value, "mission_Coordinate", self)

    @property
    def mission_Drone(self):
        return self.__mission_Drone

    @mission_Drone.setter
    def mission_Drone(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mission_Drone__mission_Drone", None)
        self.__mission_Drone = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mission_Swarm6"):
                opp_val = getattr(old_value, "mission_Swarm6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mission_Swarm6"):
                opp_val = getattr(value, "mission_Swarm6", None)
                if opp_val is None:
                    setattr(value, "mission_Swarm6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mission_Mission(NamedElement):

    def __init__(self, crs: str, mission_Mission: set["mission_Task"] = None, mission_Mission2: set["mission_TaskDependency"] = None, mission_Mission4: "mission_Swarm" = None):
        self.crs = crs
        self.mission_Mission = mission_Mission if mission_Mission is not None else set()
        self.mission_Mission2 = mission_Mission2 if mission_Mission2 is not None else set()
        self.mission_Mission4 = mission_Mission4
        
    @property
    def crs(self) -> str:
        return self.__crs

    @crs.setter
    def crs(self, crs: str):
        self.__crs = crs

    @property
    def mission_Mission(self):
        return self.__mission_Mission

    @mission_Mission.setter
    def mission_Mission(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mission_Mission__mission_Mission", None)
        self.__mission_Mission = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mission_Task"):
                    opp_val = getattr(item, "mission_Task", None)
                    
                    if opp_val == self:
                        setattr(item, "mission_Task", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mission_Task"):
                    opp_val = getattr(item, "mission_Task", None)
                    
                    setattr(item, "mission_Task", self)
                    

    @property
    def mission_Mission2(self):
        return self.__mission_Mission2

    @mission_Mission2.setter
    def mission_Mission2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mission_Mission__mission_Mission2", None)
        self.__mission_Mission2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mission_TaskDependency"):
                    opp_val = getattr(item, "mission_TaskDependency", None)
                    
                    if opp_val == self:
                        setattr(item, "mission_TaskDependency", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mission_TaskDependency"):
                    opp_val = getattr(item, "mission_TaskDependency", None)
                    
                    setattr(item, "mission_TaskDependency", self)
                    

    @property
    def mission_Mission4(self):
        return self.__mission_Mission4

    @mission_Mission4.setter
    def mission_Mission4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mission_Mission__mission_Mission4", None)
        self.__mission_Mission4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mission_Swarm"):
                opp_val = getattr(old_value, "mission_Swarm", None)
                if opp_val == self:
                    setattr(old_value, "mission_Swarm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mission_Swarm"):
                opp_val = getattr(value, "mission_Swarm", None)
                setattr(value, "mission_Swarm", self)

class mission_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
