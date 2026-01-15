from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class EdgeKind(Enum):
    DEPENDENCY = "DEPENDENCY"
    TRIGGER = "TRIGGER"
class Nature(Enum):
    Attack = "Attack"
    Fault = "Fault"
    Hybrid = "Hybrid"
class RoleType(Enum):
    Contributing = "Contributing"
    Counteracting = "Counteracting"


############################################
# Definition of Classes
############################################

class Connector:

    pass
class UATMM_structure_SAND(Connector):

    pass
class UATMM_structure_SOR(Connector):

    pass
class UATMM_structure_TAND(Connector):

    pass
class UATMM_structure_RDEP(Connector):

    def __init__(self, factor: float):
        self.factor = factor
        
    @property
    def factor(self) -> float:
        return self.__factor

    @factor.setter
    def factor(self, factor: float):
        self.__factor = factor

class UATMM_structure_PAND(Connector):

    pass
class UATMM_structure_Weighted(Connector):

    def __init__(self, Treshold: float, Weights: float):
        self.Treshold = Treshold
        self.Weights = Weights
        
    @property
    def Treshold(self) -> float:
        return self.__Treshold

    @Treshold.setter
    def Treshold(self, Treshold: float):
        self.__Treshold = Treshold

    @property
    def Weights(self) -> float:
        return self.__Weights

    @Weights.setter
    def Weights(self, Weights: float):
        self.__Weights = Weights

class UATMM_structure_XOR(Connector):

    pass
class UATMM_structure_Spare(Connector):

    pass
class UATMM_structure_KofN(Connector):

    def __init__(self, Threshold: int):
        self.Threshold = Threshold
        
    @property
    def Threshold(self) -> int:
        return self.__Threshold

    @Threshold.setter
    def Threshold(self, Threshold: int):
        self.__Threshold = Threshold

class UATMM_structure_OR(Connector):

    pass
class UATMM_structure_AND(Connector):

    pass
class UATMM_structure_FDEP(Connector):

    pass
class UATMM_structure_Connector:

    pass
class UATMM_structure_TreeMetaData:

    def __init__(self, Key: str, Value: str, UATMM_structure_TreeMetaData: "UATMM_structure_AttackTree" = None):
        self.Key = Key
        self.Value = Value
        self.UATMM_structure_TreeMetaData = UATMM_structure_TreeMetaData
        
    @property
    def Value(self) -> str:
        return self.__Value

    @Value.setter
    def Value(self, Value: str):
        self.__Value = Value

    @property
    def Key(self) -> str:
        return self.__Key

    @Key.setter
    def Key(self, Key: str):
        self.__Key = Key

    @property
    def UATMM_structure_TreeMetaData(self):
        return self.__UATMM_structure_TreeMetaData

    @UATMM_structure_TreeMetaData.setter
    def UATMM_structure_TreeMetaData(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UATMM_structure_TreeMetaData__UATMM_structure_TreeMetaData", None)
        self.__UATMM_structure_TreeMetaData = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UATMM_structure_AttackTree7"):
                opp_val = getattr(old_value, "UATMM_structure_AttackTree7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UATMM_structure_AttackTree7"):
                opp_val = getattr(value, "UATMM_structure_AttackTree7", None)
                if opp_val is None:
                    setattr(value, "UATMM_structure_AttackTree7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class UATMM_structure_Edge:

    def __init__(self, edgeKind: str, UATMM_structure_Edge: "UATMM_structure_AttackTree" = None, UATMM_structure_Edge15: "UATMM_structure_Node" = None, UATMM_structure_Edge18: "UATMM_structure_Node" = None):
        self.edgeKind = edgeKind
        self.UATMM_structure_Edge = UATMM_structure_Edge
        self.UATMM_structure_Edge15 = UATMM_structure_Edge15
        self.UATMM_structure_Edge18 = UATMM_structure_Edge18
        
    @property
    def edgeKind(self) -> str:
        return self.__edgeKind

    @edgeKind.setter
    def edgeKind(self, edgeKind: str):
        self.__edgeKind = edgeKind

    @property
    def UATMM_structure_Edge(self):
        return self.__UATMM_structure_Edge

    @UATMM_structure_Edge.setter
    def UATMM_structure_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UATMM_structure_Edge__UATMM_structure_Edge", None)
        self.__UATMM_structure_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UATMM_structure_AttackTree5"):
                opp_val = getattr(old_value, "UATMM_structure_AttackTree5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UATMM_structure_AttackTree5"):
                opp_val = getattr(value, "UATMM_structure_AttackTree5", None)
                if opp_val is None:
                    setattr(value, "UATMM_structure_AttackTree5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UATMM_structure_Edge18(self):
        return self.__UATMM_structure_Edge18

    @UATMM_structure_Edge18.setter
    def UATMM_structure_Edge18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UATMM_structure_Edge__UATMM_structure_Edge18", None)
        self.__UATMM_structure_Edge18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UATMM_structure_Node19"):
                opp_val = getattr(old_value, "UATMM_structure_Node19", None)
                if opp_val == self:
                    setattr(old_value, "UATMM_structure_Node19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UATMM_structure_Node19"):
                opp_val = getattr(value, "UATMM_structure_Node19", None)
                setattr(value, "UATMM_structure_Node19", self)

    @property
    def UATMM_structure_Edge15(self):
        return self.__UATMM_structure_Edge15

    @UATMM_structure_Edge15.setter
    def UATMM_structure_Edge15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UATMM_structure_Edge__UATMM_structure_Edge15", None)
        self.__UATMM_structure_Edge15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UATMM_structure_Node16"):
                opp_val = getattr(old_value, "UATMM_structure_Node16", None)
                if opp_val == self:
                    setattr(old_value, "UATMM_structure_Node16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UATMM_structure_Node16"):
                opp_val = getattr(value, "UATMM_structure_Node16", None)
                setattr(value, "UATMM_structure_Node16", self)

class UATMM_structure_Node:

    def __init__(self, id: str, label: str, nature: str, role: str, UATMM_structure_Node: "UATMM_structure_AttackTree" = None, UATMM_structure_Node3: "UATMM_structure_AttackTree" = None, gate: "UATMM_structure_Connector" = None, Node: "UATMM_structure_Node" = None, parents: set["UATMM_structure_Node"] = None, Node13: "UATMM_structure_Node" = None, children: set["UATMM_structure_Node"] = None, UATMM_structure_Node16: "UATMM_structure_Edge" = None, UATMM_structure_Node19: "UATMM_structure_Edge" = None, Node21: "UATMM_structure_Connector" = None):
        self.id = id
        self.label = label
        self.nature = nature
        self.role = role
        self.UATMM_structure_Node = UATMM_structure_Node
        self.UATMM_structure_Node3 = UATMM_structure_Node3
        self.gate = gate
        self.Node = Node
        self.parents = parents if parents is not None else set()
        self.Node13 = Node13
        self.children = children if children is not None else set()
        self.UATMM_structure_Node16 = UATMM_structure_Node16
        self.UATMM_structure_Node19 = UATMM_structure_Node19
        self.Node21 = Node21
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def nature(self) -> str:
        return self.__nature

    @nature.setter
    def nature(self, nature: str):
        self.__nature = nature

    @property
    def gate(self):
        return self.__gate

    @gate.setter
    def gate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UATMM_structure_Node__gate", None)
        self.__gate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Connector"):
                opp_val = getattr(old_value, "Connector", None)
                if opp_val == self:
                    setattr(old_value, "Connector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Connector"):
                opp_val = getattr(value, "Connector", None)
                setattr(value, "Connector", self)

    @property
    def parents(self):
        return self.__parents

    @parents.setter
    def parents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UATMM_structure_Node__parents", None)
        self.__parents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    if opp_val == self:
                        setattr(item, "Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node"):
                    opp_val = getattr(item, "Node", None)
                    
                    setattr(item, "Node", self)
                    

    @property
    def Node13(self):
        return self.__Node13

    @Node13.setter
    def Node13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UATMM_structure_Node__Node13", None)
        self.__Node13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "children"):
                opp_val = getattr(old_value, "children", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "children"):
                opp_val = getattr(value, "children", None)
                if opp_val is None:
                    setattr(value, "children", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UATMM_structure_Node16(self):
        return self.__UATMM_structure_Node16

    @UATMM_structure_Node16.setter
    def UATMM_structure_Node16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UATMM_structure_Node__UATMM_structure_Node16", None)
        self.__UATMM_structure_Node16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UATMM_structure_Edge15"):
                opp_val = getattr(old_value, "UATMM_structure_Edge15", None)
                if opp_val == self:
                    setattr(old_value, "UATMM_structure_Edge15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UATMM_structure_Edge15"):
                opp_val = getattr(value, "UATMM_structure_Edge15", None)
                setattr(value, "UATMM_structure_Edge15", self)

    @property
    def UATMM_structure_Node3(self):
        return self.__UATMM_structure_Node3

    @UATMM_structure_Node3.setter
    def UATMM_structure_Node3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UATMM_structure_Node__UATMM_structure_Node3", None)
        self.__UATMM_structure_Node3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UATMM_structure_AttackTree2"):
                opp_val = getattr(old_value, "UATMM_structure_AttackTree2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UATMM_structure_AttackTree2"):
                opp_val = getattr(value, "UATMM_structure_AttackTree2", None)
                if opp_val is None:
                    setattr(value, "UATMM_structure_AttackTree2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Node(self):
        return self.__Node

    @Node.setter
    def Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UATMM_structure_Node__Node", None)
        self.__Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parents"):
                opp_val = getattr(old_value, "parents", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parents"):
                opp_val = getattr(value, "parents", None)
                if opp_val is None:
                    setattr(value, "parents", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def UATMM_structure_Node(self):
        return self.__UATMM_structure_Node

    @UATMM_structure_Node.setter
    def UATMM_structure_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UATMM_structure_Node__UATMM_structure_Node", None)
        self.__UATMM_structure_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UATMM_structure_AttackTree"):
                opp_val = getattr(old_value, "UATMM_structure_AttackTree", None)
                if opp_val == self:
                    setattr(old_value, "UATMM_structure_AttackTree", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UATMM_structure_AttackTree"):
                opp_val = getattr(value, "UATMM_structure_AttackTree", None)
                setattr(value, "UATMM_structure_AttackTree", self)

    @property
    def UATMM_structure_Node19(self):
        return self.__UATMM_structure_Node19

    @UATMM_structure_Node19.setter
    def UATMM_structure_Node19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UATMM_structure_Node__UATMM_structure_Node19", None)
        self.__UATMM_structure_Node19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UATMM_structure_Edge18"):
                opp_val = getattr(old_value, "UATMM_structure_Edge18", None)
                if opp_val == self:
                    setattr(old_value, "UATMM_structure_Edge18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UATMM_structure_Edge18"):
                opp_val = getattr(value, "UATMM_structure_Edge18", None)
                setattr(value, "UATMM_structure_Edge18", self)

    @property
    def Node21(self):
        return self.__Node21

    @Node21.setter
    def Node21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UATMM_structure_Node__Node21", None)
        self.__Node21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "connector"):
                opp_val = getattr(old_value, "connector", None)
                if opp_val == self:
                    setattr(old_value, "connector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "connector"):
                opp_val = getattr(value, "connector", None)
                setattr(value, "connector", self)

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UATMM_structure_Node__children", None)
        self.__children = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Node13"):
                    opp_val = getattr(item, "Node13", None)
                    
                    if opp_val == self:
                        setattr(item, "Node13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Node13"):
                    opp_val = getattr(item, "Node13", None)
                    
                    setattr(item, "Node13", self)
                    

class UATMM_structure_AttackTree:

    pass