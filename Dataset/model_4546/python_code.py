from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class RobotStatus(Enum):
    Ready = "Ready"
    TurnedOff = "TurnedOff"
    Waiting = "Waiting"
    Executing = "Executing"
class TaskExecutionStatus(Enum):
    Ready = "Ready"
    Finished = "Finished"
    Suspended = "Suspended"
    InProgress = "InProgress"
    Waiting = "Waiting"


############################################
# Definition of Classes
############################################

class behaviour_TaskDescriptor:

    pass
class behaviour_CapabilityProperties:

    pass
class behaviour_Capability:

    pass
class PropertyKeyContainer:

    pass
class behaviour_DetectedObject:

    def __init__(self, obstacle: bool, behaviour_DetectedObject: "behaviour_AreaObject" = None, behaviour_DetectedObject63: "behaviour_DynamicRobot" = None):
        self.obstacle = obstacle
        self.behaviour_DetectedObject = behaviour_DetectedObject
        self.behaviour_DetectedObject63 = behaviour_DetectedObject63
        
    @property
    def obstacle(self) -> bool:
        return self.__obstacle

    @obstacle.setter
    def obstacle(self, obstacle: bool):
        self.__obstacle = obstacle

    @property
    def behaviour_DetectedObject63(self):
        return self.__behaviour_DetectedObject63

    @behaviour_DetectedObject63.setter
    def behaviour_DetectedObject63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_DetectedObject__behaviour_DetectedObject63", None)
        self.__behaviour_DetectedObject63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_DynamicRobot62"):
                opp_val = getattr(old_value, "behaviour_DynamicRobot62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_DynamicRobot62"):
                opp_val = getattr(value, "behaviour_DynamicRobot62", None)
                if opp_val is None:
                    setattr(value, "behaviour_DynamicRobot62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behaviour_DetectedObject(self):
        return self.__behaviour_DetectedObject

    @behaviour_DetectedObject.setter
    def behaviour_DetectedObject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_DetectedObject__behaviour_DetectedObject", None)
        self.__behaviour_DetectedObject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_AreaObject58"):
                opp_val = getattr(old_value, "behaviour_AreaObject58", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_AreaObject58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_AreaObject58"):
                opp_val = getattr(value, "behaviour_AreaObject58", None)
                setattr(value, "behaviour_AreaObject58", self)

class behaviour_RobotCollaboration:

    pass
class behaviour_Robot:

    pass
class CommunicationAction:

    pass
class behaviour_BroadcastCommunication(CommunicationAction):

    pass
class behaviour_MulticastCommunication(CommunicationAction):

    pass
class behaviour_UnicastCommunication(CommunicationAction):

    pass
class behaviour_Task:

    pass
class behaviour_BehaviourContainer:

    pass
class Action:

    pass
class behaviour_CommunicationAction(Action):

    pass
class behaviour_MeasureValue:

    pass
class behaviour_AreaObject:

    pass
class behaviour_Property:

    pass
class NamedElement:

    pass
class behaviour_TaskExecution(NamedElement):

    def __init__(self, status: str, behaviour_TaskExecution8: "behaviour_Message" = None, behaviour_TaskExecution: "behaviour_BehaviourContainer" = None, behaviour_TaskExecution36: "behaviour_Action" = None, behaviour_TaskExecution40: set["behaviour_DynamicRobot"] = None, behaviour_TaskExecution43: "behaviour_MeasureValue" = None, behaviour_TaskExecution73: "behaviour_DynamicRobot" = None, TaskExecution: "behaviour_TaskRequirement" = None, behaviour_TaskExecution46: "behaviour_Task" = None, taskExecution: "behaviour_TaskRequirement" = None, behaviour_TaskExecution77: "behaviour_TaskRequirement" = None):
        self.status = status
        self.behaviour_TaskExecution8 = behaviour_TaskExecution8
        self.behaviour_TaskExecution = behaviour_TaskExecution
        self.behaviour_TaskExecution36 = behaviour_TaskExecution36
        self.behaviour_TaskExecution40 = behaviour_TaskExecution40 if behaviour_TaskExecution40 is not None else set()
        self.behaviour_TaskExecution43 = behaviour_TaskExecution43
        self.behaviour_TaskExecution73 = behaviour_TaskExecution73
        self.TaskExecution = TaskExecution
        self.behaviour_TaskExecution46 = behaviour_TaskExecution46
        self.taskExecution = taskExecution
        self.behaviour_TaskExecution77 = behaviour_TaskExecution77
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def TaskExecution(self):
        return self.__TaskExecution

    @TaskExecution.setter
    def TaskExecution(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_TaskExecution__TaskExecution", None)
        self.__TaskExecution = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirement"):
                opp_val = getattr(old_value, "requirement", None)
                if opp_val == self:
                    setattr(old_value, "requirement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirement"):
                opp_val = getattr(value, "requirement", None)
                setattr(value, "requirement", self)

    @property
    def behaviour_TaskExecution40(self):
        return self.__behaviour_TaskExecution40

    @behaviour_TaskExecution40.setter
    def behaviour_TaskExecution40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_TaskExecution__behaviour_TaskExecution40", None)
        self.__behaviour_TaskExecution40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_DynamicRobot41"):
                    opp_val = getattr(item, "behaviour_DynamicRobot41", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_DynamicRobot41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_DynamicRobot41"):
                    opp_val = getattr(item, "behaviour_DynamicRobot41", None)
                    
                    setattr(item, "behaviour_DynamicRobot41", self)
                    

    @property
    def behaviour_TaskExecution36(self):
        return self.__behaviour_TaskExecution36

    @behaviour_TaskExecution36.setter
    def behaviour_TaskExecution36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_TaskExecution__behaviour_TaskExecution36", None)
        self.__behaviour_TaskExecution36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Action35"):
                opp_val = getattr(old_value, "behaviour_Action35", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Action35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Action35"):
                opp_val = getattr(value, "behaviour_Action35", None)
                setattr(value, "behaviour_Action35", self)

    @property
    def behaviour_TaskExecution73(self):
        return self.__behaviour_TaskExecution73

    @behaviour_TaskExecution73.setter
    def behaviour_TaskExecution73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_TaskExecution__behaviour_TaskExecution73", None)
        self.__behaviour_TaskExecution73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_DynamicRobot72"):
                opp_val = getattr(old_value, "behaviour_DynamicRobot72", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_DynamicRobot72"):
                opp_val = getattr(value, "behaviour_DynamicRobot72", None)
                if opp_val is None:
                    setattr(value, "behaviour_DynamicRobot72", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behaviour_TaskExecution8(self):
        return self.__behaviour_TaskExecution8

    @behaviour_TaskExecution8.setter
    def behaviour_TaskExecution8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_TaskExecution__behaviour_TaskExecution8", None)
        self.__behaviour_TaskExecution8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Message"):
                opp_val = getattr(old_value, "behaviour_Message", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Message"):
                opp_val = getattr(value, "behaviour_Message", None)
                if opp_val is None:
                    setattr(value, "behaviour_Message", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behaviour_TaskExecution43(self):
        return self.__behaviour_TaskExecution43

    @behaviour_TaskExecution43.setter
    def behaviour_TaskExecution43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_TaskExecution__behaviour_TaskExecution43", None)
        self.__behaviour_TaskExecution43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_MeasureValue44"):
                opp_val = getattr(old_value, "behaviour_MeasureValue44", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_MeasureValue44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_MeasureValue44"):
                opp_val = getattr(value, "behaviour_MeasureValue44", None)
                setattr(value, "behaviour_MeasureValue44", self)

    @property
    def behaviour_TaskExecution(self):
        return self.__behaviour_TaskExecution

    @behaviour_TaskExecution.setter
    def behaviour_TaskExecution(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_TaskExecution__behaviour_TaskExecution", None)
        self.__behaviour_TaskExecution = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_BehaviourContainer2"):
                opp_val = getattr(old_value, "behaviour_BehaviourContainer2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_BehaviourContainer2"):
                opp_val = getattr(value, "behaviour_BehaviourContainer2", None)
                if opp_val is None:
                    setattr(value, "behaviour_BehaviourContainer2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behaviour_TaskExecution46(self):
        return self.__behaviour_TaskExecution46

    @behaviour_TaskExecution46.setter
    def behaviour_TaskExecution46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_TaskExecution__behaviour_TaskExecution46", None)
        self.__behaviour_TaskExecution46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Task47"):
                opp_val = getattr(old_value, "behaviour_Task47", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Task47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Task47"):
                opp_val = getattr(value, "behaviour_Task47", None)
                setattr(value, "behaviour_Task47", self)

    @property
    def taskExecution(self):
        return self.__taskExecution

    @taskExecution.setter
    def taskExecution(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_TaskExecution__taskExecution", None)
        self.__taskExecution = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TaskRequirement"):
                opp_val = getattr(old_value, "TaskRequirement", None)
                if opp_val == self:
                    setattr(old_value, "TaskRequirement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TaskRequirement"):
                opp_val = getattr(value, "TaskRequirement", None)
                setattr(value, "TaskRequirement", self)

    @property
    def behaviour_TaskExecution77(self):
        return self.__behaviour_TaskExecution77

    @behaviour_TaskExecution77.setter
    def behaviour_TaskExecution77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_TaskExecution__behaviour_TaskExecution77", None)
        self.__behaviour_TaskExecution77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_TaskRequirement76"):
                opp_val = getattr(old_value, "behaviour_TaskRequirement76", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_TaskRequirement76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_TaskRequirement76"):
                opp_val = getattr(value, "behaviour_TaskRequirement76", None)
                setattr(value, "behaviour_TaskRequirement76", self)

class behaviour_DynamicRobot(NamedElement):

    def __init__(self, status: str, behaviour_DynamicRobot: "behaviour_BehaviourContainer" = None, behaviour_DynamicRobot41: "behaviour_TaskExecution" = None, behaviour_DynamicRobot21: "behaviour_UnicastCommunication" = None, behaviour_DynamicRobot23: "behaviour_MulticastCommunication" = None, behaviour_DynamicRobot25: "behaviour_BroadcastCommunication" = None, DynamicRobot: "behaviour_MessageRepository" = None, behaviour_DynamicRobot60: "behaviour_Robot" = None, behaviour_DynamicRobot62: set["behaviour_DetectedObject"] = None, behaviour_DynamicRobot65: set["behaviour_RobotCollaboration"] = None, robot: "behaviour_MessageRepository" = None, behaviour_DynamicRobot69: set["behaviour_Action"] = None, behaviour_DynamicRobot72: set["behaviour_TaskExecution"] = None, behaviour_DynamicRobot50: "behaviour_RobotCollaboration" = None):
        self.status = status
        self.behaviour_DynamicRobot = behaviour_DynamicRobot
        self.behaviour_DynamicRobot41 = behaviour_DynamicRobot41
        self.behaviour_DynamicRobot21 = behaviour_DynamicRobot21
        self.behaviour_DynamicRobot23 = behaviour_DynamicRobot23
        self.behaviour_DynamicRobot25 = behaviour_DynamicRobot25
        self.DynamicRobot = DynamicRobot
        self.behaviour_DynamicRobot60 = behaviour_DynamicRobot60
        self.behaviour_DynamicRobot62 = behaviour_DynamicRobot62 if behaviour_DynamicRobot62 is not None else set()
        self.behaviour_DynamicRobot65 = behaviour_DynamicRobot65 if behaviour_DynamicRobot65 is not None else set()
        self.robot = robot
        self.behaviour_DynamicRobot69 = behaviour_DynamicRobot69 if behaviour_DynamicRobot69 is not None else set()
        self.behaviour_DynamicRobot72 = behaviour_DynamicRobot72 if behaviour_DynamicRobot72 is not None else set()
        self.behaviour_DynamicRobot50 = behaviour_DynamicRobot50
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def DynamicRobot(self):
        return self.__DynamicRobot

    @DynamicRobot.setter
    def DynamicRobot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_DynamicRobot__DynamicRobot", None)
        self.__DynamicRobot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "messageRepository"):
                opp_val = getattr(old_value, "messageRepository", None)
                if opp_val == self:
                    setattr(old_value, "messageRepository", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "messageRepository"):
                opp_val = getattr(value, "messageRepository", None)
                setattr(value, "messageRepository", self)

    @property
    def behaviour_DynamicRobot23(self):
        return self.__behaviour_DynamicRobot23

    @behaviour_DynamicRobot23.setter
    def behaviour_DynamicRobot23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_DynamicRobot__behaviour_DynamicRobot23", None)
        self.__behaviour_DynamicRobot23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_MulticastCommunication"):
                opp_val = getattr(old_value, "behaviour_MulticastCommunication", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_MulticastCommunication"):
                opp_val = getattr(value, "behaviour_MulticastCommunication", None)
                if opp_val is None:
                    setattr(value, "behaviour_MulticastCommunication", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behaviour_DynamicRobot41(self):
        return self.__behaviour_DynamicRobot41

    @behaviour_DynamicRobot41.setter
    def behaviour_DynamicRobot41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_DynamicRobot__behaviour_DynamicRobot41", None)
        self.__behaviour_DynamicRobot41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_TaskExecution40"):
                opp_val = getattr(old_value, "behaviour_TaskExecution40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_TaskExecution40"):
                opp_val = getattr(value, "behaviour_TaskExecution40", None)
                if opp_val is None:
                    setattr(value, "behaviour_TaskExecution40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behaviour_DynamicRobot72(self):
        return self.__behaviour_DynamicRobot72

    @behaviour_DynamicRobot72.setter
    def behaviour_DynamicRobot72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_DynamicRobot__behaviour_DynamicRobot72", None)
        self.__behaviour_DynamicRobot72 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_TaskExecution73"):
                    opp_val = getattr(item, "behaviour_TaskExecution73", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_TaskExecution73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_TaskExecution73"):
                    opp_val = getattr(item, "behaviour_TaskExecution73", None)
                    
                    setattr(item, "behaviour_TaskExecution73", self)
                    

    @property
    def behaviour_DynamicRobot60(self):
        return self.__behaviour_DynamicRobot60

    @behaviour_DynamicRobot60.setter
    def behaviour_DynamicRobot60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_DynamicRobot__behaviour_DynamicRobot60", None)
        self.__behaviour_DynamicRobot60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Robot"):
                opp_val = getattr(old_value, "behaviour_Robot", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Robot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Robot"):
                opp_val = getattr(value, "behaviour_Robot", None)
                setattr(value, "behaviour_Robot", self)

    @property
    def behaviour_DynamicRobot25(self):
        return self.__behaviour_DynamicRobot25

    @behaviour_DynamicRobot25.setter
    def behaviour_DynamicRobot25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_DynamicRobot__behaviour_DynamicRobot25", None)
        self.__behaviour_DynamicRobot25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_BroadcastCommunication"):
                opp_val = getattr(old_value, "behaviour_BroadcastCommunication", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_BroadcastCommunication"):
                opp_val = getattr(value, "behaviour_BroadcastCommunication", None)
                if opp_val is None:
                    setattr(value, "behaviour_BroadcastCommunication", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behaviour_DynamicRobot65(self):
        return self.__behaviour_DynamicRobot65

    @behaviour_DynamicRobot65.setter
    def behaviour_DynamicRobot65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_DynamicRobot__behaviour_DynamicRobot65", None)
        self.__behaviour_DynamicRobot65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_RobotCollaboration66"):
                    opp_val = getattr(item, "behaviour_RobotCollaboration66", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_RobotCollaboration66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_RobotCollaboration66"):
                    opp_val = getattr(item, "behaviour_RobotCollaboration66", None)
                    
                    setattr(item, "behaviour_RobotCollaboration66", self)
                    

    @property
    def behaviour_DynamicRobot50(self):
        return self.__behaviour_DynamicRobot50

    @behaviour_DynamicRobot50.setter
    def behaviour_DynamicRobot50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_DynamicRobot__behaviour_DynamicRobot50", None)
        self.__behaviour_DynamicRobot50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_RobotCollaboration"):
                opp_val = getattr(old_value, "behaviour_RobotCollaboration", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_RobotCollaboration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_RobotCollaboration"):
                opp_val = getattr(value, "behaviour_RobotCollaboration", None)
                setattr(value, "behaviour_RobotCollaboration", self)

    @property
    def behaviour_DynamicRobot69(self):
        return self.__behaviour_DynamicRobot69

    @behaviour_DynamicRobot69.setter
    def behaviour_DynamicRobot69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_DynamicRobot__behaviour_DynamicRobot69", None)
        self.__behaviour_DynamicRobot69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_Action70"):
                    opp_val = getattr(item, "behaviour_Action70", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_Action70", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_Action70"):
                    opp_val = getattr(item, "behaviour_Action70", None)
                    
                    setattr(item, "behaviour_Action70", self)
                    

    @property
    def behaviour_DynamicRobot21(self):
        return self.__behaviour_DynamicRobot21

    @behaviour_DynamicRobot21.setter
    def behaviour_DynamicRobot21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_DynamicRobot__behaviour_DynamicRobot21", None)
        self.__behaviour_DynamicRobot21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_UnicastCommunication"):
                opp_val = getattr(old_value, "behaviour_UnicastCommunication", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_UnicastCommunication", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_UnicastCommunication"):
                opp_val = getattr(value, "behaviour_UnicastCommunication", None)
                setattr(value, "behaviour_UnicastCommunication", self)

    @property
    def robot(self):
        return self.__robot

    @robot.setter
    def robot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_DynamicRobot__robot", None)
        self.__robot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MessageRepository"):
                opp_val = getattr(old_value, "MessageRepository", None)
                if opp_val == self:
                    setattr(old_value, "MessageRepository", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MessageRepository"):
                opp_val = getattr(value, "MessageRepository", None)
                setattr(value, "MessageRepository", self)

    @property
    def behaviour_DynamicRobot62(self):
        return self.__behaviour_DynamicRobot62

    @behaviour_DynamicRobot62.setter
    def behaviour_DynamicRobot62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_DynamicRobot__behaviour_DynamicRobot62", None)
        self.__behaviour_DynamicRobot62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_DetectedObject63"):
                    opp_val = getattr(item, "behaviour_DetectedObject63", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_DetectedObject63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_DetectedObject63"):
                    opp_val = getattr(item, "behaviour_DetectedObject63", None)
                    
                    setattr(item, "behaviour_DetectedObject63", self)
                    

    @property
    def behaviour_DynamicRobot(self):
        return self.__behaviour_DynamicRobot

    @behaviour_DynamicRobot.setter
    def behaviour_DynamicRobot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_DynamicRobot__behaviour_DynamicRobot", None)
        self.__behaviour_DynamicRobot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_BehaviourContainer"):
                opp_val = getattr(old_value, "behaviour_BehaviourContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_BehaviourContainer"):
                opp_val = getattr(value, "behaviour_BehaviourContainer", None)
                if opp_val is None:
                    setattr(value, "behaviour_BehaviourContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class behaviour_Action(NamedElement):

    pass
class behaviour_MessageRepository(NamedElement):

    pass
class behaviour_Message(NamedElement):

    def __init__(self, timestamp: date, needResponse: bool, behaviour_Message: set["behaviour_TaskExecution"] = None, behaviour_Message10: set["behaviour_Property"] = None, behaviour_Message12: set["behaviour_AreaObject"] = None, behaviour_Message14: "behaviour_MeasureValue" = None, behaviour_Message17: "behaviour_Message" = None, behaviour_Message15: "behaviour_Message" = None, behaviour_Message31: "behaviour_MessageRepository" = None, behaviour_Message19: "behaviour_CommunicationAction" = None, behaviour_Message28: "behaviour_MessageRepository" = None):
        self.timestamp = timestamp
        self.needResponse = needResponse
        self.behaviour_Message = behaviour_Message if behaviour_Message is not None else set()
        self.behaviour_Message10 = behaviour_Message10 if behaviour_Message10 is not None else set()
        self.behaviour_Message12 = behaviour_Message12 if behaviour_Message12 is not None else set()
        self.behaviour_Message14 = behaviour_Message14
        self.behaviour_Message17 = behaviour_Message17
        self.behaviour_Message15 = behaviour_Message15
        self.behaviour_Message31 = behaviour_Message31
        self.behaviour_Message19 = behaviour_Message19
        self.behaviour_Message28 = behaviour_Message28
        
    @property
    def needResponse(self) -> bool:
        return self.__needResponse

    @needResponse.setter
    def needResponse(self, needResponse: bool):
        self.__needResponse = needResponse

    @property
    def timestamp(self) -> date:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: date):
        self.__timestamp = timestamp

    @property
    def behaviour_Message31(self):
        return self.__behaviour_Message31

    @behaviour_Message31.setter
    def behaviour_Message31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Message__behaviour_Message31", None)
        self.__behaviour_Message31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_MessageRepository30"):
                opp_val = getattr(old_value, "behaviour_MessageRepository30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_MessageRepository30"):
                opp_val = getattr(value, "behaviour_MessageRepository30", None)
                if opp_val is None:
                    setattr(value, "behaviour_MessageRepository30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behaviour_Message10(self):
        return self.__behaviour_Message10

    @behaviour_Message10.setter
    def behaviour_Message10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Message__behaviour_Message10", None)
        self.__behaviour_Message10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_Property"):
                    opp_val = getattr(item, "behaviour_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_Property"):
                    opp_val = getattr(item, "behaviour_Property", None)
                    
                    setattr(item, "behaviour_Property", self)
                    

    @property
    def behaviour_Message(self):
        return self.__behaviour_Message

    @behaviour_Message.setter
    def behaviour_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Message__behaviour_Message", None)
        self.__behaviour_Message = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_TaskExecution8"):
                    opp_val = getattr(item, "behaviour_TaskExecution8", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_TaskExecution8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_TaskExecution8"):
                    opp_val = getattr(item, "behaviour_TaskExecution8", None)
                    
                    setattr(item, "behaviour_TaskExecution8", self)
                    

    @property
    def behaviour_Message15(self):
        return self.__behaviour_Message15

    @behaviour_Message15.setter
    def behaviour_Message15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Message__behaviour_Message15", None)
        self.__behaviour_Message15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Message17"):
                opp_val = getattr(old_value, "behaviour_Message17", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Message17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Message17"):
                opp_val = getattr(value, "behaviour_Message17", None)
                setattr(value, "behaviour_Message17", self)

    @property
    def behaviour_Message17(self):
        return self.__behaviour_Message17

    @behaviour_Message17.setter
    def behaviour_Message17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Message__behaviour_Message17", None)
        self.__behaviour_Message17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Message15"):
                opp_val = getattr(old_value, "behaviour_Message15", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Message15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Message15"):
                opp_val = getattr(value, "behaviour_Message15", None)
                setattr(value, "behaviour_Message15", self)

    @property
    def behaviour_Message28(self):
        return self.__behaviour_Message28

    @behaviour_Message28.setter
    def behaviour_Message28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Message__behaviour_Message28", None)
        self.__behaviour_Message28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_MessageRepository"):
                opp_val = getattr(old_value, "behaviour_MessageRepository", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_MessageRepository"):
                opp_val = getattr(value, "behaviour_MessageRepository", None)
                if opp_val is None:
                    setattr(value, "behaviour_MessageRepository", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def behaviour_Message14(self):
        return self.__behaviour_Message14

    @behaviour_Message14.setter
    def behaviour_Message14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Message__behaviour_Message14", None)
        self.__behaviour_Message14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_MeasureValue"):
                opp_val = getattr(old_value, "behaviour_MeasureValue", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_MeasureValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_MeasureValue"):
                opp_val = getattr(value, "behaviour_MeasureValue", None)
                setattr(value, "behaviour_MeasureValue", self)

    @property
    def behaviour_Message12(self):
        return self.__behaviour_Message12

    @behaviour_Message12.setter
    def behaviour_Message12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Message__behaviour_Message12", None)
        self.__behaviour_Message12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_AreaObject"):
                    opp_val = getattr(item, "behaviour_AreaObject", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_AreaObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_AreaObject"):
                    opp_val = getattr(item, "behaviour_AreaObject", None)
                    
                    setattr(item, "behaviour_AreaObject", self)
                    

    @property
    def behaviour_Message19(self):
        return self.__behaviour_Message19

    @behaviour_Message19.setter
    def behaviour_Message19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_Message__behaviour_Message19", None)
        self.__behaviour_Message19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_CommunicationAction"):
                opp_val = getattr(old_value, "behaviour_CommunicationAction", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_CommunicationAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_CommunicationAction"):
                opp_val = getattr(value, "behaviour_CommunicationAction", None)
                setattr(value, "behaviour_CommunicationAction", self)

class behaviour_BehaviouralPropertyKeyContainer(PropertyKeyContainer):

    pass
class behaviour_TaskRequirement(NamedElement):

    def __init__(self, participants: int, behaviour_TaskRequirement: "behaviour_BehaviourContainer" = None, TaskRequirement: "behaviour_TaskExecution" = None, requirement: "behaviour_TaskExecution" = None, behaviour_TaskRequirement76: "behaviour_TaskExecution" = None, behaviour_TaskRequirement79: set["behaviour_Property"] = None, behaviour_TaskRequirement82: set["behaviour_Capability"] = None, behaviour_TaskRequirement84: set["behaviour_CapabilityProperties"] = None, behaviour_TaskRequirement86: "behaviour_TaskDescriptor" = None, behaviour_TaskRequirement88: "behaviour_Task" = None):
        self.participants = participants
        self.behaviour_TaskRequirement = behaviour_TaskRequirement
        self.TaskRequirement = TaskRequirement
        self.requirement = requirement
        self.behaviour_TaskRequirement76 = behaviour_TaskRequirement76
        self.behaviour_TaskRequirement79 = behaviour_TaskRequirement79 if behaviour_TaskRequirement79 is not None else set()
        self.behaviour_TaskRequirement82 = behaviour_TaskRequirement82 if behaviour_TaskRequirement82 is not None else set()
        self.behaviour_TaskRequirement84 = behaviour_TaskRequirement84 if behaviour_TaskRequirement84 is not None else set()
        self.behaviour_TaskRequirement86 = behaviour_TaskRequirement86
        self.behaviour_TaskRequirement88 = behaviour_TaskRequirement88
        
    @property
    def participants(self) -> int:
        return self.__participants

    @participants.setter
    def participants(self, participants: int):
        self.__participants = participants

    @property
    def behaviour_TaskRequirement86(self):
        return self.__behaviour_TaskRequirement86

    @behaviour_TaskRequirement86.setter
    def behaviour_TaskRequirement86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_TaskRequirement__behaviour_TaskRequirement86", None)
        self.__behaviour_TaskRequirement86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_TaskDescriptor"):
                opp_val = getattr(old_value, "behaviour_TaskDescriptor", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_TaskDescriptor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_TaskDescriptor"):
                opp_val = getattr(value, "behaviour_TaskDescriptor", None)
                setattr(value, "behaviour_TaskDescriptor", self)

    @property
    def behaviour_TaskRequirement82(self):
        return self.__behaviour_TaskRequirement82

    @behaviour_TaskRequirement82.setter
    def behaviour_TaskRequirement82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_TaskRequirement__behaviour_TaskRequirement82", None)
        self.__behaviour_TaskRequirement82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_Capability"):
                    opp_val = getattr(item, "behaviour_Capability", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_Capability", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_Capability"):
                    opp_val = getattr(item, "behaviour_Capability", None)
                    
                    setattr(item, "behaviour_Capability", self)
                    

    @property
    def behaviour_TaskRequirement76(self):
        return self.__behaviour_TaskRequirement76

    @behaviour_TaskRequirement76.setter
    def behaviour_TaskRequirement76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_TaskRequirement__behaviour_TaskRequirement76", None)
        self.__behaviour_TaskRequirement76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_TaskExecution77"):
                opp_val = getattr(old_value, "behaviour_TaskExecution77", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_TaskExecution77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_TaskExecution77"):
                opp_val = getattr(value, "behaviour_TaskExecution77", None)
                setattr(value, "behaviour_TaskExecution77", self)

    @property
    def behaviour_TaskRequirement(self):
        return self.__behaviour_TaskRequirement

    @behaviour_TaskRequirement.setter
    def behaviour_TaskRequirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_TaskRequirement__behaviour_TaskRequirement", None)
        self.__behaviour_TaskRequirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_BehaviourContainer4"):
                opp_val = getattr(old_value, "behaviour_BehaviourContainer4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_BehaviourContainer4"):
                opp_val = getattr(value, "behaviour_BehaviourContainer4", None)
                if opp_val is None:
                    setattr(value, "behaviour_BehaviourContainer4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TaskRequirement(self):
        return self.__TaskRequirement

    @TaskRequirement.setter
    def TaskRequirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_TaskRequirement__TaskRequirement", None)
        self.__TaskRequirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "taskExecution"):
                opp_val = getattr(old_value, "taskExecution", None)
                if opp_val == self:
                    setattr(old_value, "taskExecution", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "taskExecution"):
                opp_val = getattr(value, "taskExecution", None)
                setattr(value, "taskExecution", self)

    @property
    def behaviour_TaskRequirement88(self):
        return self.__behaviour_TaskRequirement88

    @behaviour_TaskRequirement88.setter
    def behaviour_TaskRequirement88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_TaskRequirement__behaviour_TaskRequirement88", None)
        self.__behaviour_TaskRequirement88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "behaviour_Task89"):
                opp_val = getattr(old_value, "behaviour_Task89", None)
                if opp_val == self:
                    setattr(old_value, "behaviour_Task89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "behaviour_Task89"):
                opp_val = getattr(value, "behaviour_Task89", None)
                setattr(value, "behaviour_Task89", self)

    @property
    def requirement(self):
        return self.__requirement

    @requirement.setter
    def requirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_TaskRequirement__requirement", None)
        self.__requirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TaskExecution"):
                opp_val = getattr(old_value, "TaskExecution", None)
                if opp_val == self:
                    setattr(old_value, "TaskExecution", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TaskExecution"):
                opp_val = getattr(value, "TaskExecution", None)
                setattr(value, "TaskExecution", self)

    @property
    def behaviour_TaskRequirement79(self):
        return self.__behaviour_TaskRequirement79

    @behaviour_TaskRequirement79.setter
    def behaviour_TaskRequirement79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_TaskRequirement__behaviour_TaskRequirement79", None)
        self.__behaviour_TaskRequirement79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_Property80"):
                    opp_val = getattr(item, "behaviour_Property80", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_Property80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_Property80"):
                    opp_val = getattr(item, "behaviour_Property80", None)
                    
                    setattr(item, "behaviour_Property80", self)
                    

    @property
    def behaviour_TaskRequirement84(self):
        return self.__behaviour_TaskRequirement84

    @behaviour_TaskRequirement84.setter
    def behaviour_TaskRequirement84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_behaviour_TaskRequirement__behaviour_TaskRequirement84", None)
        self.__behaviour_TaskRequirement84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "behaviour_CapabilityProperties"):
                    opp_val = getattr(item, "behaviour_CapabilityProperties", None)
                    
                    if opp_val == self:
                        setattr(item, "behaviour_CapabilityProperties", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "behaviour_CapabilityProperties"):
                    opp_val = getattr(item, "behaviour_CapabilityProperties", None)
                    
                    setattr(item, "behaviour_CapabilityProperties", self)
                    
