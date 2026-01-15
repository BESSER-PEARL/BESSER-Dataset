from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class EdgeType(Enum):
    IS_A_TYPE = "IS_A_TYPE"
    AKO_TYPE = "AKO_TYPE"
    ROLE_CONSTRAINT_TYPE = "ROLE_CONSTRAINT_TYPE"


############################################
# Definition of Classes
############################################

class Node:

    pass
class model_AssociationNode(Node):

    def __init__(self, associationTypeConstraint: str):
        self.associationTypeConstraint = associationTypeConstraint
        
    @property
    def associationTypeConstraint(self) -> str:
        return self.__associationTypeConstraint

    @associationTypeConstraint.setter
    def associationTypeConstraint(self, associationTypeConstraint: str):
        self.__associationTypeConstraint = associationTypeConstraint

class model_TypeNode(Node):

    def __init__(self, topicType: str):
        self.topicType = topicType
        
    @property
    def topicType(self) -> str:
        return self.__topicType

    @topicType.setter
    def topicType(self, topicType: str):
        self.__topicType = topicType

class model_Edge:

    def __init__(self, type: str, model_Edge: "model_Diagram" = None, model_Edge4: "model_BendPoint" = None, model_Edge6: "model_Node" = None, model_Edge9: "model_Node" = None):
        self.type = type
        self.model_Edge = model_Edge
        self.model_Edge4 = model_Edge4
        self.model_Edge6 = model_Edge6
        self.model_Edge9 = model_Edge9
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def model_Edge(self):
        return self.__model_Edge

    @model_Edge.setter
    def model_Edge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Edge__model_Edge", None)
        self.__model_Edge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Diagram2"):
                opp_val = getattr(old_value, "model_Diagram2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Diagram2"):
                opp_val = getattr(value, "model_Diagram2", None)
                if opp_val is None:
                    setattr(value, "model_Diagram2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Edge6(self):
        return self.__model_Edge6

    @model_Edge6.setter
    def model_Edge6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Edge__model_Edge6", None)
        self.__model_Edge6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Node7"):
                opp_val = getattr(old_value, "model_Node7", None)
                if opp_val == self:
                    setattr(old_value, "model_Node7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Node7"):
                opp_val = getattr(value, "model_Node7", None)
                setattr(value, "model_Node7", self)

    @property
    def model_Edge9(self):
        return self.__model_Edge9

    @model_Edge9.setter
    def model_Edge9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Edge__model_Edge9", None)
        self.__model_Edge9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Node10"):
                opp_val = getattr(old_value, "model_Node10", None)
                if opp_val == self:
                    setattr(old_value, "model_Node10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Node10"):
                opp_val = getattr(value, "model_Node10", None)
                setattr(value, "model_Node10", self)

    @property
    def model_Edge4(self):
        return self.__model_Edge4

    @model_Edge4.setter
    def model_Edge4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Edge__model_Edge4", None)
        self.__model_Edge4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_BendPoint"):
                opp_val = getattr(old_value, "model_BendPoint", None)
                if opp_val == self:
                    setattr(old_value, "model_BendPoint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_BendPoint"):
                opp_val = getattr(value, "model_BendPoint", None)
                setattr(value, "model_BendPoint", self)

class model_Node:

    def __init__(self, posY: int, posX: int, model_Node: "model_Diagram" = None, model_Node7: "model_Edge" = None, model_Node10: "model_Edge" = None):
        self.posY = posY
        self.posX = posX
        self.model_Node = model_Node
        self.model_Node7 = model_Node7
        self.model_Node10 = model_Node10
        
    @property
    def posX(self) -> int:
        return self.__posX

    @posX.setter
    def posX(self, posX: int):
        self.__posX = posX

    @property
    def posY(self) -> int:
        return self.__posY

    @posY.setter
    def posY(self, posY: int):
        self.__posY = posY

    @property
    def model_Node(self):
        return self.__model_Node

    @model_Node.setter
    def model_Node(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Node__model_Node", None)
        self.__model_Node = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Diagram"):
                opp_val = getattr(old_value, "model_Diagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Diagram"):
                opp_val = getattr(value, "model_Diagram", None)
                if opp_val is None:
                    setattr(value, "model_Diagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Node7(self):
        return self.__model_Node7

    @model_Node7.setter
    def model_Node7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Node__model_Node7", None)
        self.__model_Node7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Edge6"):
                opp_val = getattr(old_value, "model_Edge6", None)
                if opp_val == self:
                    setattr(old_value, "model_Edge6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Edge6"):
                opp_val = getattr(value, "model_Edge6", None)
                setattr(value, "model_Edge6", self)

    @property
    def model_Node10(self):
        return self.__model_Node10

    @model_Node10.setter
    def model_Node10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Node__model_Node10", None)
        self.__model_Node10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Edge9"):
                opp_val = getattr(old_value, "model_Edge9", None)
                if opp_val == self:
                    setattr(old_value, "model_Edge9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Edge9"):
                opp_val = getattr(value, "model_Edge9", None)
                setattr(value, "model_Edge9", self)

class model_BendPoint:

    def __init__(self, posX: int, posY: int, model_BendPoint: "model_Edge" = None):
        self.posX = posX
        self.posY = posY
        self.model_BendPoint = model_BendPoint
        
    @property
    def posX(self) -> int:
        return self.__posX

    @posX.setter
    def posX(self, posX: int):
        self.__posX = posX

    @property
    def posY(self) -> int:
        return self.__posY

    @posY.setter
    def posY(self, posY: int):
        self.__posY = posY

    @property
    def model_BendPoint(self):
        return self.__model_BendPoint

    @model_BendPoint.setter
    def model_BendPoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_BendPoint__model_BendPoint", None)
        self.__model_BendPoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Edge4"):
                opp_val = getattr(old_value, "model_Edge4", None)
                if opp_val == self:
                    setattr(old_value, "model_Edge4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Edge4"):
                opp_val = getattr(value, "model_Edge4", None)
                setattr(value, "model_Edge4", self)

class model_Diagram:

    def __init__(self, topicMapSchema: str, model_Diagram: set["model_Node"] = None, model_Diagram2: set["model_Edge"] = None):
        self.topicMapSchema = topicMapSchema
        self.model_Diagram = model_Diagram if model_Diagram is not None else set()
        self.model_Diagram2 = model_Diagram2 if model_Diagram2 is not None else set()
        
    @property
    def topicMapSchema(self) -> str:
        return self.__topicMapSchema

    @topicMapSchema.setter
    def topicMapSchema(self, topicMapSchema: str):
        self.__topicMapSchema = topicMapSchema

    @property
    def model_Diagram(self):
        return self.__model_Diagram

    @model_Diagram.setter
    def model_Diagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Diagram__model_Diagram", None)
        self.__model_Diagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Node"):
                    opp_val = getattr(item, "model_Node", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Node", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Node"):
                    opp_val = getattr(item, "model_Node", None)
                    
                    setattr(item, "model_Node", self)
                    

    @property
    def model_Diagram2(self):
        return self.__model_Diagram2

    @model_Diagram2.setter
    def model_Diagram2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Diagram__model_Diagram2", None)
        self.__model_Diagram2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Edge"):
                    opp_val = getattr(item, "model_Edge", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Edge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Edge"):
                    opp_val = getattr(item, "model_Edge", None)
                    
                    setattr(item, "model_Edge", self)
                    
