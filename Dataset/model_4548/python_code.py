from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TaskState(Enum):
    NOT_STARTED = "NOT_STARTED"
    WAITING = "WAITING"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
class DroneState(Enum):
    CREATED = "CREATED"
    HOVERING = "HOVERING"
    MOVING = "MOVING"
    DONE = "DONE"


############################################
# Definition of Classes
############################################

class dronesSimulation_Obstacle:

    pass
class Observation:

    pass
class dronesSimulation_DroneObservation(Observation):

    pass
class dronesSimulation_ObstacleObservation(Observation):

    pass
class dronesSimulation_Role:

    pass
class dronesSimulation_Task:

    pass
class dronesSimulation_Drone:

    pass
class dronesSimulation_DroneInstance:

    def __init__(self, currentBattery: float, state: str, dronesSimulation_DroneInstance8: "dronesSimulation_Position" = None, allocatedDrone: "dronesSimulation_RoleInstance" = None, dronesSimulation_DroneInstance11: set["dronesSimulation_Observation"] = None, dronesSimulation_DroneInstance: "dronesSimulation_DronesSimulation" = None, dronesSimulation_DroneInstance6: "dronesSimulation_Drone" = None, DroneInstance: "dronesSimulation_RoleInstance" = None):
        self.currentBattery = currentBattery
        self.state = state
        self.dronesSimulation_DroneInstance8 = dronesSimulation_DroneInstance8
        self.allocatedDrone = allocatedDrone
        self.dronesSimulation_DroneInstance11 = dronesSimulation_DroneInstance11 if dronesSimulation_DroneInstance11 is not None else set()
        self.dronesSimulation_DroneInstance = dronesSimulation_DroneInstance
        self.dronesSimulation_DroneInstance6 = dronesSimulation_DroneInstance6
        self.DroneInstance = DroneInstance
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def currentBattery(self) -> float:
        return self.__currentBattery

    @currentBattery.setter
    def currentBattery(self, currentBattery: float):
        self.__currentBattery = currentBattery

    @property
    def dronesSimulation_DroneInstance8(self):
        return self.__dronesSimulation_DroneInstance8

    @dronesSimulation_DroneInstance8.setter
    def dronesSimulation_DroneInstance8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesSimulation_DroneInstance__dronesSimulation_DroneInstance8", None)
        self.__dronesSimulation_DroneInstance8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesSimulation_Position"):
                opp_val = getattr(old_value, "dronesSimulation_Position", None)
                if opp_val == self:
                    setattr(old_value, "dronesSimulation_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesSimulation_Position"):
                opp_val = getattr(value, "dronesSimulation_Position", None)
                setattr(value, "dronesSimulation_Position", self)

    @property
    def dronesSimulation_DroneInstance6(self):
        return self.__dronesSimulation_DroneInstance6

    @dronesSimulation_DroneInstance6.setter
    def dronesSimulation_DroneInstance6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesSimulation_DroneInstance__dronesSimulation_DroneInstance6", None)
        self.__dronesSimulation_DroneInstance6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesSimulation_Drone"):
                opp_val = getattr(old_value, "dronesSimulation_Drone", None)
                if opp_val == self:
                    setattr(old_value, "dronesSimulation_Drone", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesSimulation_Drone"):
                opp_val = getattr(value, "dronesSimulation_Drone", None)
                setattr(value, "dronesSimulation_Drone", self)

    @property
    def DroneInstance(self):
        return self.__DroneInstance

    @DroneInstance.setter
    def DroneInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesSimulation_DroneInstance__DroneInstance", None)
        self.__DroneInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "currentRole"):
                opp_val = getattr(old_value, "currentRole", None)
                if opp_val == self:
                    setattr(old_value, "currentRole", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "currentRole"):
                opp_val = getattr(value, "currentRole", None)
                setattr(value, "currentRole", self)

    @property
    def dronesSimulation_DroneInstance11(self):
        return self.__dronesSimulation_DroneInstance11

    @dronesSimulation_DroneInstance11.setter
    def dronesSimulation_DroneInstance11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesSimulation_DroneInstance__dronesSimulation_DroneInstance11", None)
        self.__dronesSimulation_DroneInstance11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dronesSimulation_Observation"):
                    opp_val = getattr(item, "dronesSimulation_Observation", None)
                    
                    if opp_val == self:
                        setattr(item, "dronesSimulation_Observation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dronesSimulation_Observation"):
                    opp_val = getattr(item, "dronesSimulation_Observation", None)
                    
                    setattr(item, "dronesSimulation_Observation", self)
                    

    @property
    def dronesSimulation_DroneInstance(self):
        return self.__dronesSimulation_DroneInstance

    @dronesSimulation_DroneInstance.setter
    def dronesSimulation_DroneInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesSimulation_DroneInstance__dronesSimulation_DroneInstance", None)
        self.__dronesSimulation_DroneInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesSimulation_DronesSimulation4"):
                opp_val = getattr(old_value, "dronesSimulation_DronesSimulation4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesSimulation_DronesSimulation4"):
                opp_val = getattr(value, "dronesSimulation_DronesSimulation4", None)
                if opp_val is None:
                    setattr(value, "dronesSimulation_DronesSimulation4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def allocatedDrone(self):
        return self.__allocatedDrone

    @allocatedDrone.setter
    def allocatedDrone(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesSimulation_DroneInstance__allocatedDrone", None)
        self.__allocatedDrone = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RoleInstance"):
                opp_val = getattr(old_value, "RoleInstance", None)
                if opp_val == self:
                    setattr(old_value, "RoleInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RoleInstance"):
                opp_val = getattr(value, "RoleInstance", None)
                setattr(value, "RoleInstance", self)

class dronesSimulation_TaskInstance:

    def __init__(self, state: str, dronesSimulation_TaskInstance: "dronesSimulation_DronesSimulation" = None, dronesSimulation_TaskInstance13: "dronesSimulation_Task" = None, taskInstance: set["dronesSimulation_RoleInstance"] = None, TaskInstance: "dronesSimulation_RoleInstance" = None):
        self.state = state
        self.dronesSimulation_TaskInstance = dronesSimulation_TaskInstance
        self.dronesSimulation_TaskInstance13 = dronesSimulation_TaskInstance13
        self.taskInstance = taskInstance if taskInstance is not None else set()
        self.TaskInstance = TaskInstance
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def dronesSimulation_TaskInstance13(self):
        return self.__dronesSimulation_TaskInstance13

    @dronesSimulation_TaskInstance13.setter
    def dronesSimulation_TaskInstance13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesSimulation_TaskInstance__dronesSimulation_TaskInstance13", None)
        self.__dronesSimulation_TaskInstance13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesSimulation_Task"):
                opp_val = getattr(old_value, "dronesSimulation_Task", None)
                if opp_val == self:
                    setattr(old_value, "dronesSimulation_Task", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesSimulation_Task"):
                opp_val = getattr(value, "dronesSimulation_Task", None)
                setattr(value, "dronesSimulation_Task", self)

    @property
    def taskInstance(self):
        return self.__taskInstance

    @taskInstance.setter
    def taskInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesSimulation_TaskInstance__taskInstance", None)
        self.__taskInstance = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RoleInstance15"):
                    opp_val = getattr(item, "RoleInstance15", None)
                    
                    if opp_val == self:
                        setattr(item, "RoleInstance15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RoleInstance15"):
                    opp_val = getattr(item, "RoleInstance15", None)
                    
                    setattr(item, "RoleInstance15", self)
                    

    @property
    def dronesSimulation_TaskInstance(self):
        return self.__dronesSimulation_TaskInstance

    @dronesSimulation_TaskInstance.setter
    def dronesSimulation_TaskInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesSimulation_TaskInstance__dronesSimulation_TaskInstance", None)
        self.__dronesSimulation_TaskInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesSimulation_DronesSimulation2"):
                opp_val = getattr(old_value, "dronesSimulation_DronesSimulation2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesSimulation_DronesSimulation2"):
                opp_val = getattr(value, "dronesSimulation_DronesSimulation2", None)
                if opp_val is None:
                    setattr(value, "dronesSimulation_DronesSimulation2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TaskInstance(self):
        return self.__TaskInstance

    @TaskInstance.setter
    def TaskInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesSimulation_TaskInstance__TaskInstance", None)
        self.__TaskInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roleInstances"):
                opp_val = getattr(old_value, "roleInstances", None)
                if opp_val == self:
                    setattr(old_value, "roleInstances", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roleInstances"):
                opp_val = getattr(value, "roleInstances", None)
                setattr(value, "roleInstances", self)

class dronesSimulation_Scenario:

    pass
class dronesSimulation_DronesSimulation:

    pass
class dronesSimulation_Observation(ABC):

    def __init__(self, time: str, id: str, dronesSimulation_Observation: "dronesSimulation_DroneInstance" = None):
        self.time = time
        self.id = id
        self.dronesSimulation_Observation = dronesSimulation_Observation
        
    @property
    def time(self) -> str:
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def dronesSimulation_Observation(self):
        return self.__dronesSimulation_Observation

    @dronesSimulation_Observation.setter
    def dronesSimulation_Observation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesSimulation_Observation__dronesSimulation_Observation", None)
        self.__dronesSimulation_Observation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesSimulation_DroneInstance11"):
                opp_val = getattr(old_value, "dronesSimulation_DroneInstance11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesSimulation_DroneInstance11"):
                opp_val = getattr(value, "dronesSimulation_DroneInstance11", None)
                if opp_val is None:
                    setattr(value, "dronesSimulation_DroneInstance11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dronesSimulation_RoleInstance:

    pass
class dronesSimulation_Position:

    pass