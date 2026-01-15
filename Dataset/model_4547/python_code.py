from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class dronesStructure_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Region:

    pass
class dronesStructure_Charger(Region):

    pass
class AABB:

    pass
class dronesStructure_AABB(ABC):

    pass
class dronesStructure_ProvidedCapability:

    def __init__(self, maximalValue: float, energyConsumptionPerValue: float, dronesStructure_ProvidedCapability: "dronesStructure_DroneType" = None, dronesStructure_ProvidedCapability24: "dronesStructure_DroneType" = None, dronesStructure_ProvidedCapability26: "dronesStructure_Capability" = None, providedCapabilities: "dronesStructure_DroneType" = None, ProvidedCapability: "dronesStructure_DroneType" = None):
        self.maximalValue = maximalValue
        self.energyConsumptionPerValue = energyConsumptionPerValue
        self.dronesStructure_ProvidedCapability = dronesStructure_ProvidedCapability
        self.dronesStructure_ProvidedCapability24 = dronesStructure_ProvidedCapability24
        self.dronesStructure_ProvidedCapability26 = dronesStructure_ProvidedCapability26
        self.providedCapabilities = providedCapabilities
        self.ProvidedCapability = ProvidedCapability
        
    @property
    def energyConsumptionPerValue(self) -> float:
        return self.__energyConsumptionPerValue

    @energyConsumptionPerValue.setter
    def energyConsumptionPerValue(self, energyConsumptionPerValue: float):
        self.__energyConsumptionPerValue = energyConsumptionPerValue

    @property
    def maximalValue(self) -> float:
        return self.__maximalValue

    @maximalValue.setter
    def maximalValue(self, maximalValue: float):
        self.__maximalValue = maximalValue

    @property
    def dronesStructure_ProvidedCapability(self):
        return self.__dronesStructure_ProvidedCapability

    @dronesStructure_ProvidedCapability.setter
    def dronesStructure_ProvidedCapability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_ProvidedCapability__dronesStructure_ProvidedCapability", None)
        self.__dronesStructure_ProvidedCapability = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesStructure_DroneType19"):
                opp_val = getattr(old_value, "dronesStructure_DroneType19", None)
                if opp_val == self:
                    setattr(old_value, "dronesStructure_DroneType19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesStructure_DroneType19"):
                opp_val = getattr(value, "dronesStructure_DroneType19", None)
                setattr(value, "dronesStructure_DroneType19", self)

    @property
    def providedCapabilities(self):
        return self.__providedCapabilities

    @providedCapabilities.setter
    def providedCapabilities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_ProvidedCapability__providedCapabilities", None)
        self.__providedCapabilities = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DroneType"):
                opp_val = getattr(old_value, "DroneType", None)
                if opp_val == self:
                    setattr(old_value, "DroneType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DroneType"):
                opp_val = getattr(value, "DroneType", None)
                setattr(value, "DroneType", self)

    @property
    def ProvidedCapability(self):
        return self.__ProvidedCapability

    @ProvidedCapability.setter
    def ProvidedCapability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_ProvidedCapability__ProvidedCapability", None)
        self.__ProvidedCapability = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "droneType"):
                opp_val = getattr(old_value, "droneType", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "droneType"):
                opp_val = getattr(value, "droneType", None)
                if opp_val is None:
                    setattr(value, "droneType", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dronesStructure_ProvidedCapability24(self):
        return self.__dronesStructure_ProvidedCapability24

    @dronesStructure_ProvidedCapability24.setter
    def dronesStructure_ProvidedCapability24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_ProvidedCapability__dronesStructure_ProvidedCapability24", None)
        self.__dronesStructure_ProvidedCapability24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesStructure_DroneType23"):
                opp_val = getattr(old_value, "dronesStructure_DroneType23", None)
                if opp_val == self:
                    setattr(old_value, "dronesStructure_DroneType23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesStructure_DroneType23"):
                opp_val = getattr(value, "dronesStructure_DroneType23", None)
                setattr(value, "dronesStructure_DroneType23", self)

    @property
    def dronesStructure_ProvidedCapability26(self):
        return self.__dronesStructure_ProvidedCapability26

    @dronesStructure_ProvidedCapability26.setter
    def dronesStructure_ProvidedCapability26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_ProvidedCapability__dronesStructure_ProvidedCapability26", None)
        self.__dronesStructure_ProvidedCapability26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesStructure_Capability27"):
                opp_val = getattr(old_value, "dronesStructure_Capability27", None)
                if opp_val == self:
                    setattr(old_value, "dronesStructure_Capability27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesStructure_Capability27"):
                opp_val = getattr(value, "dronesStructure_Capability27", None)
                setattr(value, "dronesStructure_Capability27", self)

class dronesStructure_Position:

    def __init__(self, x: float, y: float, z: float, dronesStructure_Position: "dronesStructure_Drone" = None, dronesStructure_Position42: "dronesStructure_AABB" = None):
        self.x = x
        self.y = y
        self.z = z
        self.dronesStructure_Position = dronesStructure_Position
        self.dronesStructure_Position42 = dronesStructure_Position42
        
    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def z(self) -> float:
        return self.__z

    @z.setter
    def z(self, z: float):
        self.__z = z

    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def dronesStructure_Position(self):
        return self.__dronesStructure_Position

    @dronesStructure_Position.setter
    def dronesStructure_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_Position__dronesStructure_Position", None)
        self.__dronesStructure_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesStructure_Drone37"):
                opp_val = getattr(old_value, "dronesStructure_Drone37", None)
                if opp_val == self:
                    setattr(old_value, "dronesStructure_Drone37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesStructure_Drone37"):
                opp_val = getattr(value, "dronesStructure_Drone37", None)
                setattr(value, "dronesStructure_Drone37", self)

    @property
    def dronesStructure_Position42(self):
        return self.__dronesStructure_Position42

    @dronesStructure_Position42.setter
    def dronesStructure_Position42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_Position__dronesStructure_Position42", None)
        self.__dronesStructure_Position42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesStructure_AABB"):
                opp_val = getattr(old_value, "dronesStructure_AABB", None)
                if opp_val == self:
                    setattr(old_value, "dronesStructure_AABB", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesStructure_AABB"):
                opp_val = getattr(value, "dronesStructure_AABB", None)
                setattr(value, "dronesStructure_AABB", self)

class dronesStructure_RequiredCapability:

    def __init__(self, minimalValue: float, RequiredCapability: "dronesStructure_Role" = None, dronesStructure_RequiredCapability: "dronesStructure_Capability" = None, requiredCapabilities: "dronesStructure_Role" = None):
        self.minimalValue = minimalValue
        self.RequiredCapability = RequiredCapability
        self.dronesStructure_RequiredCapability = dronesStructure_RequiredCapability
        self.requiredCapabilities = requiredCapabilities
        
    @property
    def minimalValue(self) -> float:
        return self.__minimalValue

    @minimalValue.setter
    def minimalValue(self, minimalValue: float):
        self.__minimalValue = minimalValue

    @property
    def requiredCapabilities(self):
        return self.__requiredCapabilities

    @requiredCapabilities.setter
    def requiredCapabilities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_RequiredCapability__requiredCapabilities", None)
        self.__requiredCapabilities = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Role35"):
                opp_val = getattr(old_value, "Role35", None)
                if opp_val == self:
                    setattr(old_value, "Role35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Role35"):
                opp_val = getattr(value, "Role35", None)
                setattr(value, "Role35", self)

    @property
    def RequiredCapability(self):
        return self.__RequiredCapability

    @RequiredCapability.setter
    def RequiredCapability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_RequiredCapability__RequiredCapability", None)
        self.__RequiredCapability = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "role"):
                opp_val = getattr(old_value, "role", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "role"):
                opp_val = getattr(value, "role", None)
                if opp_val is None:
                    setattr(value, "role", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dronesStructure_RequiredCapability(self):
        return self.__dronesStructure_RequiredCapability

    @dronesStructure_RequiredCapability.setter
    def dronesStructure_RequiredCapability(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_RequiredCapability__dronesStructure_RequiredCapability", None)
        self.__dronesStructure_RequiredCapability = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesStructure_Capability33"):
                opp_val = getattr(old_value, "dronesStructure_Capability33", None)
                if opp_val == self:
                    setattr(old_value, "dronesStructure_Capability33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesStructure_Capability33"):
                opp_val = getattr(value, "dronesStructure_Capability33", None)
                setattr(value, "dronesStructure_Capability33", self)

class Capability:

    pass
class dronesStructure_ScanningCapability(Capability):

    pass
class dronesStructure_MovementCapability(Capability):

    pass
class dronesStructure_Dimension:

    def __init__(self, width: float, height: float, depth: float, dronesStructure_Dimension: "dronesStructure_DroneType" = None, dronesStructure_Dimension45: "dronesStructure_AABB" = None):
        self.width = width
        self.height = height
        self.depth = depth
        self.dronesStructure_Dimension = dronesStructure_Dimension
        self.dronesStructure_Dimension45 = dronesStructure_Dimension45
        
    @property
    def depth(self) -> float:
        return self.__depth

    @depth.setter
    def depth(self, depth: float):
        self.__depth = depth

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, width: float):
        self.__width = width

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, height: float):
        self.__height = height

    @property
    def dronesStructure_Dimension(self):
        return self.__dronesStructure_Dimension

    @dronesStructure_Dimension.setter
    def dronesStructure_Dimension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_Dimension__dronesStructure_Dimension", None)
        self.__dronesStructure_Dimension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesStructure_DroneType21"):
                opp_val = getattr(old_value, "dronesStructure_DroneType21", None)
                if opp_val == self:
                    setattr(old_value, "dronesStructure_DroneType21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesStructure_DroneType21"):
                opp_val = getattr(value, "dronesStructure_DroneType21", None)
                setattr(value, "dronesStructure_DroneType21", self)

    @property
    def dronesStructure_Dimension45(self):
        return self.__dronesStructure_Dimension45

    @dronesStructure_Dimension45.setter
    def dronesStructure_Dimension45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_Dimension__dronesStructure_Dimension45", None)
        self.__dronesStructure_Dimension45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesStructure_AABB44"):
                opp_val = getattr(old_value, "dronesStructure_AABB44", None)
                if opp_val == self:
                    setattr(old_value, "dronesStructure_AABB44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesStructure_AABB44"):
                opp_val = getattr(value, "dronesStructure_AABB44", None)
                setattr(value, "dronesStructure_AABB44", self)

class dronesStructure_ScenarioBounds(AABB):

    pass
class NamedElement:

    pass
class dronesStructure_Task(NamedElement):

    pass
class dronesStructure_Region(NamedElement, AABB):

    pass
class dronesStructure_Drone(NamedElement):

    pass
class dronesStructure_Role(NamedElement):

    pass
class dronesStructure_Obstacle(NamedElement, AABB):

    pass
class dronesStructure_Capability(NamedElement):

    pass
class dronesStructure_CooperativeAction(NamedElement):

    def __init__(self, startTimeout: float, duration: float, dronesStructure_CooperativeAction: "dronesStructure_DronesStructure" = None, cooperativeAction: set["dronesStructure_Role"] = None, CooperativeAction: "dronesStructure_Role" = None, dronesStructure_CooperativeAction50: "dronesStructure_Task" = None):
        self.startTimeout = startTimeout
        self.duration = duration
        self.dronesStructure_CooperativeAction = dronesStructure_CooperativeAction
        self.cooperativeAction = cooperativeAction if cooperativeAction is not None else set()
        self.CooperativeAction = CooperativeAction
        self.dronesStructure_CooperativeAction50 = dronesStructure_CooperativeAction50
        
    @property
    def duration(self) -> float:
        return self.__duration

    @duration.setter
    def duration(self, duration: float):
        self.__duration = duration

    @property
    def startTimeout(self) -> float:
        return self.__startTimeout

    @startTimeout.setter
    def startTimeout(self, startTimeout: float):
        self.__startTimeout = startTimeout

    @property
    def dronesStructure_CooperativeAction50(self):
        return self.__dronesStructure_CooperativeAction50

    @dronesStructure_CooperativeAction50.setter
    def dronesStructure_CooperativeAction50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_CooperativeAction__dronesStructure_CooperativeAction50", None)
        self.__dronesStructure_CooperativeAction50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesStructure_Task49"):
                opp_val = getattr(old_value, "dronesStructure_Task49", None)
                if opp_val == self:
                    setattr(old_value, "dronesStructure_Task49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesStructure_Task49"):
                opp_val = getattr(value, "dronesStructure_Task49", None)
                setattr(value, "dronesStructure_Task49", self)

    @property
    def dronesStructure_CooperativeAction(self):
        return self.__dronesStructure_CooperativeAction

    @dronesStructure_CooperativeAction.setter
    def dronesStructure_CooperativeAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_CooperativeAction__dronesStructure_CooperativeAction", None)
        self.__dronesStructure_CooperativeAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesStructure_DronesStructure4"):
                opp_val = getattr(old_value, "dronesStructure_DronesStructure4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesStructure_DronesStructure4"):
                opp_val = getattr(value, "dronesStructure_DronesStructure4", None)
                if opp_val is None:
                    setattr(value, "dronesStructure_DronesStructure4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cooperativeAction(self):
        return self.__cooperativeAction

    @cooperativeAction.setter
    def cooperativeAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_CooperativeAction__cooperativeAction", None)
        self.__cooperativeAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Role"):
                    opp_val = getattr(item, "Role", None)
                    
                    if opp_val == self:
                        setattr(item, "Role", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Role"):
                    opp_val = getattr(item, "Role", None)
                    
                    setattr(item, "Role", self)
                    

    @property
    def CooperativeAction(self):
        return self.__CooperativeAction

    @CooperativeAction.setter
    def CooperativeAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_CooperativeAction__CooperativeAction", None)
        self.__CooperativeAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roles"):
                opp_val = getattr(old_value, "roles", None)
                if opp_val == self:
                    setattr(old_value, "roles", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roles"):
                opp_val = getattr(value, "roles", None)
                setattr(value, "roles", self)

class dronesStructure_DroneType(NamedElement):

    def __init__(self, weight: float, maxBatteryCapacity: float, idleEneryConsumption: float, dronesStructure_DroneType: "dronesStructure_DronesStructure" = None, dronesStructure_DroneType19: "dronesStructure_ProvidedCapability" = None, dronesStructure_DroneType21: "dronesStructure_Dimension" = None, dronesStructure_DroneType23: "dronesStructure_ProvidedCapability" = None, DroneType: "dronesStructure_ProvidedCapability" = None, droneType: set["dronesStructure_ProvidedCapability"] = None, dronesStructure_DroneType40: "dronesStructure_Drone" = None):
        self.weight = weight
        self.maxBatteryCapacity = maxBatteryCapacity
        self.idleEneryConsumption = idleEneryConsumption
        self.dronesStructure_DroneType = dronesStructure_DroneType
        self.dronesStructure_DroneType19 = dronesStructure_DroneType19
        self.dronesStructure_DroneType21 = dronesStructure_DroneType21
        self.dronesStructure_DroneType23 = dronesStructure_DroneType23
        self.DroneType = DroneType
        self.droneType = droneType if droneType is not None else set()
        self.dronesStructure_DroneType40 = dronesStructure_DroneType40
        
    @property
    def idleEneryConsumption(self) -> float:
        return self.__idleEneryConsumption

    @idleEneryConsumption.setter
    def idleEneryConsumption(self, idleEneryConsumption: float):
        self.__idleEneryConsumption = idleEneryConsumption

    @property
    def maxBatteryCapacity(self) -> float:
        return self.__maxBatteryCapacity

    @maxBatteryCapacity.setter
    def maxBatteryCapacity(self, maxBatteryCapacity: float):
        self.__maxBatteryCapacity = maxBatteryCapacity

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, weight: float):
        self.__weight = weight

    @property
    def dronesStructure_DroneType19(self):
        return self.__dronesStructure_DroneType19

    @dronesStructure_DroneType19.setter
    def dronesStructure_DroneType19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_DroneType__dronesStructure_DroneType19", None)
        self.__dronesStructure_DroneType19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesStructure_ProvidedCapability"):
                opp_val = getattr(old_value, "dronesStructure_ProvidedCapability", None)
                if opp_val == self:
                    setattr(old_value, "dronesStructure_ProvidedCapability", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesStructure_ProvidedCapability"):
                opp_val = getattr(value, "dronesStructure_ProvidedCapability", None)
                setattr(value, "dronesStructure_ProvidedCapability", self)

    @property
    def dronesStructure_DroneType23(self):
        return self.__dronesStructure_DroneType23

    @dronesStructure_DroneType23.setter
    def dronesStructure_DroneType23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_DroneType__dronesStructure_DroneType23", None)
        self.__dronesStructure_DroneType23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesStructure_ProvidedCapability24"):
                opp_val = getattr(old_value, "dronesStructure_ProvidedCapability24", None)
                if opp_val == self:
                    setattr(old_value, "dronesStructure_ProvidedCapability24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesStructure_ProvidedCapability24"):
                opp_val = getattr(value, "dronesStructure_ProvidedCapability24", None)
                setattr(value, "dronesStructure_ProvidedCapability24", self)

    @property
    def dronesStructure_DroneType(self):
        return self.__dronesStructure_DroneType

    @dronesStructure_DroneType.setter
    def dronesStructure_DroneType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_DroneType__dronesStructure_DroneType", None)
        self.__dronesStructure_DroneType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesStructure_DronesStructure2"):
                opp_val = getattr(old_value, "dronesStructure_DronesStructure2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesStructure_DronesStructure2"):
                opp_val = getattr(value, "dronesStructure_DronesStructure2", None)
                if opp_val is None:
                    setattr(value, "dronesStructure_DronesStructure2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def droneType(self):
        return self.__droneType

    @droneType.setter
    def droneType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_DroneType__droneType", None)
        self.__droneType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProvidedCapability"):
                    opp_val = getattr(item, "ProvidedCapability", None)
                    
                    if opp_val == self:
                        setattr(item, "ProvidedCapability", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProvidedCapability"):
                    opp_val = getattr(item, "ProvidedCapability", None)
                    
                    setattr(item, "ProvidedCapability", self)
                    

    @property
    def DroneType(self):
        return self.__DroneType

    @DroneType.setter
    def DroneType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_DroneType__DroneType", None)
        self.__DroneType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "providedCapabilities"):
                opp_val = getattr(old_value, "providedCapabilities", None)
                if opp_val == self:
                    setattr(old_value, "providedCapabilities", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "providedCapabilities"):
                opp_val = getattr(value, "providedCapabilities", None)
                setattr(value, "providedCapabilities", self)

    @property
    def dronesStructure_DroneType40(self):
        return self.__dronesStructure_DroneType40

    @dronesStructure_DroneType40.setter
    def dronesStructure_DroneType40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_DroneType__dronesStructure_DroneType40", None)
        self.__dronesStructure_DroneType40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesStructure_Drone39"):
                opp_val = getattr(old_value, "dronesStructure_Drone39", None)
                if opp_val == self:
                    setattr(old_value, "dronesStructure_Drone39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesStructure_Drone39"):
                opp_val = getattr(value, "dronesStructure_Drone39", None)
                setattr(value, "dronesStructure_Drone39", self)

    @property
    def dronesStructure_DroneType21(self):
        return self.__dronesStructure_DroneType21

    @dronesStructure_DroneType21.setter
    def dronesStructure_DroneType21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_DroneType__dronesStructure_DroneType21", None)
        self.__dronesStructure_DroneType21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesStructure_Dimension"):
                opp_val = getattr(old_value, "dronesStructure_Dimension", None)
                if opp_val == self:
                    setattr(old_value, "dronesStructure_Dimension", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesStructure_Dimension"):
                opp_val = getattr(value, "dronesStructure_Dimension", None)
                setattr(value, "dronesStructure_Dimension", self)

class dronesStructure_Scenario(NamedElement):

    def __init__(self, safeCommunicationDistance: float, maximumCommunicationDistance: float, dronesStructure_Scenario: "dronesStructure_DronesStructure" = None, dronesStructure_Scenario8: set["dronesStructure_Drone"] = None, dronesStructure_Scenario10: "dronesStructure_ScenarioBounds" = None, dronesStructure_Scenario12: set["dronesStructure_Obstacle"] = None, dronesStructure_Scenario14: set["dronesStructure_Region"] = None, dronesStructure_Scenario16: set["dronesStructure_Task"] = None):
        self.safeCommunicationDistance = safeCommunicationDistance
        self.maximumCommunicationDistance = maximumCommunicationDistance
        self.dronesStructure_Scenario = dronesStructure_Scenario
        self.dronesStructure_Scenario8 = dronesStructure_Scenario8 if dronesStructure_Scenario8 is not None else set()
        self.dronesStructure_Scenario10 = dronesStructure_Scenario10
        self.dronesStructure_Scenario12 = dronesStructure_Scenario12 if dronesStructure_Scenario12 is not None else set()
        self.dronesStructure_Scenario14 = dronesStructure_Scenario14 if dronesStructure_Scenario14 is not None else set()
        self.dronesStructure_Scenario16 = dronesStructure_Scenario16 if dronesStructure_Scenario16 is not None else set()
        
    @property
    def safeCommunicationDistance(self) -> float:
        return self.__safeCommunicationDistance

    @safeCommunicationDistance.setter
    def safeCommunicationDistance(self, safeCommunicationDistance: float):
        self.__safeCommunicationDistance = safeCommunicationDistance

    @property
    def maximumCommunicationDistance(self) -> float:
        return self.__maximumCommunicationDistance

    @maximumCommunicationDistance.setter
    def maximumCommunicationDistance(self, maximumCommunicationDistance: float):
        self.__maximumCommunicationDistance = maximumCommunicationDistance

    @property
    def dronesStructure_Scenario10(self):
        return self.__dronesStructure_Scenario10

    @dronesStructure_Scenario10.setter
    def dronesStructure_Scenario10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_Scenario__dronesStructure_Scenario10", None)
        self.__dronesStructure_Scenario10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesStructure_ScenarioBounds"):
                opp_val = getattr(old_value, "dronesStructure_ScenarioBounds", None)
                if opp_val == self:
                    setattr(old_value, "dronesStructure_ScenarioBounds", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesStructure_ScenarioBounds"):
                opp_val = getattr(value, "dronesStructure_ScenarioBounds", None)
                setattr(value, "dronesStructure_ScenarioBounds", self)

    @property
    def dronesStructure_Scenario12(self):
        return self.__dronesStructure_Scenario12

    @dronesStructure_Scenario12.setter
    def dronesStructure_Scenario12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_Scenario__dronesStructure_Scenario12", None)
        self.__dronesStructure_Scenario12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dronesStructure_Obstacle"):
                    opp_val = getattr(item, "dronesStructure_Obstacle", None)
                    
                    if opp_val == self:
                        setattr(item, "dronesStructure_Obstacle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dronesStructure_Obstacle"):
                    opp_val = getattr(item, "dronesStructure_Obstacle", None)
                    
                    setattr(item, "dronesStructure_Obstacle", self)
                    

    @property
    def dronesStructure_Scenario16(self):
        return self.__dronesStructure_Scenario16

    @dronesStructure_Scenario16.setter
    def dronesStructure_Scenario16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_Scenario__dronesStructure_Scenario16", None)
        self.__dronesStructure_Scenario16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dronesStructure_Task"):
                    opp_val = getattr(item, "dronesStructure_Task", None)
                    
                    if opp_val == self:
                        setattr(item, "dronesStructure_Task", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dronesStructure_Task"):
                    opp_val = getattr(item, "dronesStructure_Task", None)
                    
                    setattr(item, "dronesStructure_Task", self)
                    

    @property
    def dronesStructure_Scenario8(self):
        return self.__dronesStructure_Scenario8

    @dronesStructure_Scenario8.setter
    def dronesStructure_Scenario8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_Scenario__dronesStructure_Scenario8", None)
        self.__dronesStructure_Scenario8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dronesStructure_Drone"):
                    opp_val = getattr(item, "dronesStructure_Drone", None)
                    
                    if opp_val == self:
                        setattr(item, "dronesStructure_Drone", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dronesStructure_Drone"):
                    opp_val = getattr(item, "dronesStructure_Drone", None)
                    
                    setattr(item, "dronesStructure_Drone", self)
                    

    @property
    def dronesStructure_Scenario(self):
        return self.__dronesStructure_Scenario

    @dronesStructure_Scenario.setter
    def dronesStructure_Scenario(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_Scenario__dronesStructure_Scenario", None)
        self.__dronesStructure_Scenario = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dronesStructure_DronesStructure"):
                opp_val = getattr(old_value, "dronesStructure_DronesStructure", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dronesStructure_DronesStructure"):
                opp_val = getattr(value, "dronesStructure_DronesStructure", None)
                if opp_val is None:
                    setattr(value, "dronesStructure_DronesStructure", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dronesStructure_Scenario14(self):
        return self.__dronesStructure_Scenario14

    @dronesStructure_Scenario14.setter
    def dronesStructure_Scenario14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dronesStructure_Scenario__dronesStructure_Scenario14", None)
        self.__dronesStructure_Scenario14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dronesStructure_Region"):
                    opp_val = getattr(item, "dronesStructure_Region", None)
                    
                    if opp_val == self:
                        setattr(item, "dronesStructure_Region", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dronesStructure_Region"):
                    opp_val = getattr(item, "dronesStructure_Region", None)
                    
                    setattr(item, "dronesStructure_Region", self)
                    

class dronesStructure_DronesStructure:

    pass