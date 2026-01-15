from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ToleranceMarkerDirectionKind(Enum):
    START = "START"
    UP = "UP"
    DOWN = "DOWN"
class MarkerKind(Enum):
    value = "value"
    INTERNALEVENT = "INTERNALEVENT"
    EXTERNALEVENT = "EXTERNALEVENT"
    ACTIONNEEDED = "ACTIONNEEDED"
    TOLERANCECROSSED = "TOLERANCECROSSED"


############################################
# Definition of Classes
############################################

class Marker:

    pass
class operators_ToleranceMarker(Marker):

    def __init__(self, direction: str, level: str):
        self.direction = direction
        self.level = level
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

class operators_DateTimeRange:

    pass
class operators_Protocol:

    pass
class operators_Service:

    pass
class operators_ServiceUser:

    pass
class operators_Location:

    pass
class operators_NodeType:

    pass
class Company:

    pass
class operators_Operator(Company):

    pass
class operators_Lifecycle:

    pass
class operators_Person:

    pass
class operators_MetricSource:

    pass
class operators_DiagramInfo:

    pass
class operators_NetXResource:

    pass
class operators_Value:

    pass
class Base:

    pass
class operators_ResourceMonitor(Base):

    pass
class operators_Warehouse(Base):

    def __init__(self, description: str, name: str, operators_Warehouse: "operators_Operator" = None, operators_Warehouse78: set["operators_Node"] = None, operators_Warehouse81: set["operators_Equipment"] = None):
        self.description = description
        self.name = name
        self.operators_Warehouse = operators_Warehouse
        self.operators_Warehouse78 = operators_Warehouse78 if operators_Warehouse78 is not None else set()
        self.operators_Warehouse81 = operators_Warehouse81 if operators_Warehouse81 is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def operators_Warehouse(self):
        return self.__operators_Warehouse

    @operators_Warehouse.setter
    def operators_Warehouse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Warehouse__operators_Warehouse", None)
        self.__operators_Warehouse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Operator42"):
                opp_val = getattr(old_value, "operators_Operator42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Operator42"):
                opp_val = getattr(value, "operators_Operator42", None)
                if opp_val is None:
                    setattr(value, "operators_Operator42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def operators_Warehouse81(self):
        return self.__operators_Warehouse81

    @operators_Warehouse81.setter
    def operators_Warehouse81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Warehouse__operators_Warehouse81", None)
        self.__operators_Warehouse81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operators_Equipment82"):
                    opp_val = getattr(item, "operators_Equipment82", None)
                    
                    if opp_val == self:
                        setattr(item, "operators_Equipment82", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operators_Equipment82"):
                    opp_val = getattr(item, "operators_Equipment82", None)
                    
                    setattr(item, "operators_Equipment82", self)
                    

    @property
    def operators_Warehouse78(self):
        return self.__operators_Warehouse78

    @operators_Warehouse78.setter
    def operators_Warehouse78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Warehouse__operators_Warehouse78", None)
        self.__operators_Warehouse78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operators_Node79"):
                    opp_val = getattr(item, "operators_Node79", None)
                    
                    if opp_val == self:
                        setattr(item, "operators_Node79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operators_Node79"):
                    opp_val = getattr(item, "operators_Node79", None)
                    
                    setattr(item, "operators_Node79", self)
                    

class operators_Relationship(Base):

    def __init__(self, name: str, operators_Relationship52: "operators_Node" = None, operators_Relationship55: "operators_Protocol" = None, operators_Relationship: "operators_Node" = None):
        self.name = name
        self.operators_Relationship52 = operators_Relationship52
        self.operators_Relationship55 = operators_Relationship55
        self.operators_Relationship = operators_Relationship
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def operators_Relationship52(self):
        return self.__operators_Relationship52

    @operators_Relationship52.setter
    def operators_Relationship52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Relationship__operators_Relationship52", None)
        self.__operators_Relationship52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Node53"):
                opp_val = getattr(old_value, "operators_Node53", None)
                if opp_val == self:
                    setattr(old_value, "operators_Node53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Node53"):
                opp_val = getattr(value, "operators_Node53", None)
                setattr(value, "operators_Node53", self)

    @property
    def operators_Relationship(self):
        return self.__operators_Relationship

    @operators_Relationship.setter
    def operators_Relationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Relationship__operators_Relationship", None)
        self.__operators_Relationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Node50"):
                opp_val = getattr(old_value, "operators_Node50", None)
                if opp_val == self:
                    setattr(old_value, "operators_Node50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Node50"):
                opp_val = getattr(value, "operators_Node50", None)
                setattr(value, "operators_Node50", self)

    @property
    def operators_Relationship55(self):
        return self.__operators_Relationship55

    @operators_Relationship55.setter
    def operators_Relationship55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Relationship__operators_Relationship55", None)
        self.__operators_Relationship55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Protocol"):
                opp_val = getattr(old_value, "operators_Protocol", None)
                if opp_val == self:
                    setattr(old_value, "operators_Protocol", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Protocol"):
                opp_val = getattr(value, "operators_Protocol", None)
                setattr(value, "operators_Protocol", self)

class operators_ResourceForecast(Base):

    pass
class operators_Network(Base):

    def __init__(self, createdDate: str, description: str, name: str, operators_Network: set["operators_DiagramInfo"] = None, operators_Network13: set["operators_Node"] = None, operators_Network21: set["operators_EquipmentRelationship"] = None, operators_Network24: set["operators_MetricSource"] = None, operators_Network26: "operators_Person" = None, operators_Network16: "operators_Network" = None, operators_Network14: set["operators_Network"] = None, operators_Network18: set["operators_FunctionRelationship"] = None, operators_Network40: "operators_Operator" = None):
        self.createdDate = createdDate
        self.description = description
        self.name = name
        self.operators_Network = operators_Network if operators_Network is not None else set()
        self.operators_Network13 = operators_Network13 if operators_Network13 is not None else set()
        self.operators_Network21 = operators_Network21 if operators_Network21 is not None else set()
        self.operators_Network24 = operators_Network24 if operators_Network24 is not None else set()
        self.operators_Network26 = operators_Network26
        self.operators_Network16 = operators_Network16
        self.operators_Network14 = operators_Network14 if operators_Network14 is not None else set()
        self.operators_Network18 = operators_Network18 if operators_Network18 is not None else set()
        self.operators_Network40 = operators_Network40
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def createdDate(self) -> str:
        return self.__createdDate

    @createdDate.setter
    def createdDate(self, createdDate: str):
        self.__createdDate = createdDate

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def operators_Network16(self):
        return self.__operators_Network16

    @operators_Network16.setter
    def operators_Network16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Network__operators_Network16", None)
        self.__operators_Network16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Network14"):
                opp_val = getattr(old_value, "operators_Network14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Network14"):
                opp_val = getattr(value, "operators_Network14", None)
                if opp_val is None:
                    setattr(value, "operators_Network14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def operators_Network40(self):
        return self.__operators_Network40

    @operators_Network40.setter
    def operators_Network40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Network__operators_Network40", None)
        self.__operators_Network40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Operator"):
                opp_val = getattr(old_value, "operators_Operator", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Operator"):
                opp_val = getattr(value, "operators_Operator", None)
                if opp_val is None:
                    setattr(value, "operators_Operator", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def operators_Network(self):
        return self.__operators_Network

    @operators_Network.setter
    def operators_Network(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Network__operators_Network", None)
        self.__operators_Network = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operators_DiagramInfo"):
                    opp_val = getattr(item, "operators_DiagramInfo", None)
                    
                    if opp_val == self:
                        setattr(item, "operators_DiagramInfo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operators_DiagramInfo"):
                    opp_val = getattr(item, "operators_DiagramInfo", None)
                    
                    setattr(item, "operators_DiagramInfo", self)
                    

    @property
    def operators_Network13(self):
        return self.__operators_Network13

    @operators_Network13.setter
    def operators_Network13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Network__operators_Network13", None)
        self.__operators_Network13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operators_Node"):
                    opp_val = getattr(item, "operators_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "operators_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operators_Node"):
                    opp_val = getattr(item, "operators_Node", None)
                    
                    setattr(item, "operators_Node", self)
                    

    @property
    def operators_Network24(self):
        return self.__operators_Network24

    @operators_Network24.setter
    def operators_Network24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Network__operators_Network24", None)
        self.__operators_Network24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operators_MetricSource"):
                    opp_val = getattr(item, "operators_MetricSource", None)
                    
                    if opp_val == self:
                        setattr(item, "operators_MetricSource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operators_MetricSource"):
                    opp_val = getattr(item, "operators_MetricSource", None)
                    
                    setattr(item, "operators_MetricSource", self)
                    

    @property
    def operators_Network21(self):
        return self.__operators_Network21

    @operators_Network21.setter
    def operators_Network21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Network__operators_Network21", None)
        self.__operators_Network21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operators_EquipmentRelationship22"):
                    opp_val = getattr(item, "operators_EquipmentRelationship22", None)
                    
                    if opp_val == self:
                        setattr(item, "operators_EquipmentRelationship22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operators_EquipmentRelationship22"):
                    opp_val = getattr(item, "operators_EquipmentRelationship22", None)
                    
                    setattr(item, "operators_EquipmentRelationship22", self)
                    

    @property
    def operators_Network14(self):
        return self.__operators_Network14

    @operators_Network14.setter
    def operators_Network14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Network__operators_Network14", None)
        self.__operators_Network14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operators_Network16"):
                    opp_val = getattr(item, "operators_Network16", None)
                    
                    if opp_val == self:
                        setattr(item, "operators_Network16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operators_Network16"):
                    opp_val = getattr(item, "operators_Network16", None)
                    
                    setattr(item, "operators_Network16", self)
                    

    @property
    def operators_Network18(self):
        return self.__operators_Network18

    @operators_Network18.setter
    def operators_Network18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Network__operators_Network18", None)
        self.__operators_Network18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "operators_FunctionRelationship19"):
                    opp_val = getattr(item, "operators_FunctionRelationship19", None)
                    
                    if opp_val == self:
                        setattr(item, "operators_FunctionRelationship19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "operators_FunctionRelationship19"):
                    opp_val = getattr(item, "operators_FunctionRelationship19", None)
                    
                    setattr(item, "operators_FunctionRelationship19", self)
                    

    @property
    def operators_Network26(self):
        return self.__operators_Network26

    @operators_Network26.setter
    def operators_Network26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Network__operators_Network26", None)
        self.__operators_Network26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Person"):
                opp_val = getattr(old_value, "operators_Person", None)
                if opp_val == self:
                    setattr(old_value, "operators_Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Person"):
                opp_val = getattr(value, "operators_Person", None)
                setattr(value, "operators_Person", self)

class operators_Node(Base):

    def __init__(self, nodeID: str, operators_Node: "operators_Network" = None, operators_Node28: "operators_Lifecycle" = None, operators_Node37: "operators_NodeType" = None, operators_Node30: "operators_NodeType" = None, operators_Node32: "operators_Person" = None, operators_Node35: "operators_Location" = None, operators_Node53: "operators_Relationship" = None, operators_Node50: "operators_Relationship" = None, operators_Node58: "operators_ResourceExpansion" = None, operators_Node71: "operators_ResourceMonitor" = None, operators_Node79: "operators_Warehouse" = None):
        self.nodeID = nodeID
        self.operators_Node = operators_Node
        self.operators_Node28 = operators_Node28
        self.operators_Node37 = operators_Node37
        self.operators_Node30 = operators_Node30
        self.operators_Node32 = operators_Node32
        self.operators_Node35 = operators_Node35
        self.operators_Node53 = operators_Node53
        self.operators_Node50 = operators_Node50
        self.operators_Node58 = operators_Node58
        self.operators_Node71 = operators_Node71
        self.operators_Node79 = operators_Node79
        
    @property
    def nodeID(self) -> str:
        return self.__nodeID

    @nodeID.setter
    def nodeID(self, nodeID: str):
        self.__nodeID = nodeID

    @property
    def operators_Node53(self):
        return self.__operators_Node53

    @operators_Node53.setter
    def operators_Node53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node53", None)
        self.__operators_Node53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Relationship52"):
                opp_val = getattr(old_value, "operators_Relationship52", None)
                if opp_val == self:
                    setattr(old_value, "operators_Relationship52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Relationship52"):
                opp_val = getattr(value, "operators_Relationship52", None)
                setattr(value, "operators_Relationship52", self)

    @property
    def operators_Node58(self):
        return self.__operators_Node58

    @operators_Node58.setter
    def operators_Node58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node58", None)
        self.__operators_Node58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_ResourceExpansion57"):
                opp_val = getattr(old_value, "operators_ResourceExpansion57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_ResourceExpansion57"):
                opp_val = getattr(value, "operators_ResourceExpansion57", None)
                if opp_val is None:
                    setattr(value, "operators_ResourceExpansion57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def operators_Node28(self):
        return self.__operators_Node28

    @operators_Node28.setter
    def operators_Node28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node28", None)
        self.__operators_Node28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Lifecycle"):
                opp_val = getattr(old_value, "operators_Lifecycle", None)
                if opp_val == self:
                    setattr(old_value, "operators_Lifecycle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Lifecycle"):
                opp_val = getattr(value, "operators_Lifecycle", None)
                setattr(value, "operators_Lifecycle", self)

    @property
    def operators_Node37(self):
        return self.__operators_Node37

    @operators_Node37.setter
    def operators_Node37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node37", None)
        self.__operators_Node37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_NodeType38"):
                opp_val = getattr(old_value, "operators_NodeType38", None)
                if opp_val == self:
                    setattr(old_value, "operators_NodeType38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_NodeType38"):
                opp_val = getattr(value, "operators_NodeType38", None)
                setattr(value, "operators_NodeType38", self)

    @property
    def operators_Node79(self):
        return self.__operators_Node79

    @operators_Node79.setter
    def operators_Node79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node79", None)
        self.__operators_Node79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Warehouse78"):
                opp_val = getattr(old_value, "operators_Warehouse78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Warehouse78"):
                opp_val = getattr(value, "operators_Warehouse78", None)
                if opp_val is None:
                    setattr(value, "operators_Warehouse78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def operators_Node71(self):
        return self.__operators_Node71

    @operators_Node71.setter
    def operators_Node71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node71", None)
        self.__operators_Node71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_ResourceMonitor70"):
                opp_val = getattr(old_value, "operators_ResourceMonitor70", None)
                if opp_val == self:
                    setattr(old_value, "operators_ResourceMonitor70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_ResourceMonitor70"):
                opp_val = getattr(value, "operators_ResourceMonitor70", None)
                setattr(value, "operators_ResourceMonitor70", self)

    @property
    def operators_Node50(self):
        return self.__operators_Node50

    @operators_Node50.setter
    def operators_Node50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node50", None)
        self.__operators_Node50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Relationship"):
                opp_val = getattr(old_value, "operators_Relationship", None)
                if opp_val == self:
                    setattr(old_value, "operators_Relationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Relationship"):
                opp_val = getattr(value, "operators_Relationship", None)
                setattr(value, "operators_Relationship", self)

    @property
    def operators_Node(self):
        return self.__operators_Node

    @operators_Node.setter
    def operators_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node", None)
        self.__operators_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Network13"):
                opp_val = getattr(old_value, "operators_Network13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Network13"):
                opp_val = getattr(value, "operators_Network13", None)
                if opp_val is None:
                    setattr(value, "operators_Network13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def operators_Node32(self):
        return self.__operators_Node32

    @operators_Node32.setter
    def operators_Node32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node32", None)
        self.__operators_Node32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Person33"):
                opp_val = getattr(old_value, "operators_Person33", None)
                if opp_val == self:
                    setattr(old_value, "operators_Person33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Person33"):
                opp_val = getattr(value, "operators_Person33", None)
                setattr(value, "operators_Person33", self)

    @property
    def operators_Node30(self):
        return self.__operators_Node30

    @operators_Node30.setter
    def operators_Node30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node30", None)
        self.__operators_Node30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_NodeType"):
                opp_val = getattr(old_value, "operators_NodeType", None)
                if opp_val == self:
                    setattr(old_value, "operators_NodeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_NodeType"):
                opp_val = getattr(value, "operators_NodeType", None)
                setattr(value, "operators_NodeType", self)

    @property
    def operators_Node35(self):
        return self.__operators_Node35

    @operators_Node35.setter
    def operators_Node35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Node__operators_Node35", None)
        self.__operators_Node35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Location"):
                opp_val = getattr(old_value, "operators_Location", None)
                if opp_val == self:
                    setattr(old_value, "operators_Location", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Location"):
                opp_val = getattr(value, "operators_Location", None)
                setattr(value, "operators_Location", self)

class operators_ResourceExpansion(Base):

    pass
class operators_Marker(Base):

    def __init__(self, description: str, kind: str, operators_Marker: "operators_Value" = None, operators_Marker10: "operators_NetXResource" = None, operators_Marker66: "operators_ResourceForecast" = None, operators_Marker68: "operators_ResourceMonitor" = None):
        self.description = description
        self.kind = kind
        self.operators_Marker = operators_Marker
        self.operators_Marker10 = operators_Marker10
        self.operators_Marker66 = operators_Marker66
        self.operators_Marker68 = operators_Marker68
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def operators_Marker66(self):
        return self.__operators_Marker66

    @operators_Marker66.setter
    def operators_Marker66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Marker__operators_Marker66", None)
        self.__operators_Marker66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_ResourceForecast"):
                opp_val = getattr(old_value, "operators_ResourceForecast", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_ResourceForecast"):
                opp_val = getattr(value, "operators_ResourceForecast", None)
                if opp_val is None:
                    setattr(value, "operators_ResourceForecast", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def operators_Marker(self):
        return self.__operators_Marker

    @operators_Marker.setter
    def operators_Marker(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Marker__operators_Marker", None)
        self.__operators_Marker = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_Value"):
                opp_val = getattr(old_value, "operators_Value", None)
                if opp_val == self:
                    setattr(old_value, "operators_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_Value"):
                opp_val = getattr(value, "operators_Value", None)
                setattr(value, "operators_Value", self)

    @property
    def operators_Marker68(self):
        return self.__operators_Marker68

    @operators_Marker68.setter
    def operators_Marker68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Marker__operators_Marker68", None)
        self.__operators_Marker68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_ResourceMonitor"):
                opp_val = getattr(old_value, "operators_ResourceMonitor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_ResourceMonitor"):
                opp_val = getattr(value, "operators_ResourceMonitor", None)
                if opp_val is None:
                    setattr(value, "operators_ResourceMonitor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def operators_Marker10(self):
        return self.__operators_Marker10

    @operators_Marker10.setter
    def operators_Marker10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_operators_Marker__operators_Marker10", None)
        self.__operators_Marker10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "operators_NetXResource"):
                opp_val = getattr(old_value, "operators_NetXResource", None)
                if opp_val == self:
                    setattr(old_value, "operators_NetXResource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "operators_NetXResource"):
                opp_val = getattr(value, "operators_NetXResource", None)
                setattr(value, "operators_NetXResource", self)

class operators_Function:

    pass
class operators_Equipment:

    pass
class Relationship:

    pass
class operators_FunctionRelationship(Relationship):

    pass
class operators_EquipmentRelationship(Relationship):

    pass