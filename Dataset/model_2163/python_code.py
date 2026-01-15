from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class dsml_DModelElementBridge:

    def __init__(self, ecoreName: str, ecorePath: str, dsml_DModelElementBridge: "dsml_DSemanticBridge" = None):
        self.ecoreName = ecoreName
        self.ecorePath = ecorePath
        self.dsml_DModelElementBridge = dsml_DModelElementBridge
        
    @property
    def ecorePath(self) -> str:
        return self.__ecorePath

    @ecorePath.setter
    def ecorePath(self, ecorePath: str):
        self.__ecorePath = ecorePath

    @property
    def ecoreName(self) -> str:
        return self.__ecoreName

    @ecoreName.setter
    def ecoreName(self, ecoreName: str):
        self.__ecoreName = ecoreName

    @property
    def dsml_DModelElementBridge(self):
        return self.__dsml_DModelElementBridge

    @dsml_DModelElementBridge.setter
    def dsml_DModelElementBridge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_DModelElementBridge__dsml_DModelElementBridge", None)
        self.__dsml_DModelElementBridge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsml_DSemanticBridge46"):
                opp_val = getattr(old_value, "dsml_DSemanticBridge46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsml_DSemanticBridge46"):
                opp_val = getattr(value, "dsml_DSemanticBridge46", None)
                if opp_val is None:
                    setattr(value, "dsml_DSemanticBridge46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DModelElementBridge:

    pass
class dsml_DAttributeBridge(DModelElementBridge):

    pass
class dsml_DClassBridge(DModelElementBridge):

    pass
class dsml_EAttribute:

    pass
class dsml_EClass:

    pass
class dsml_DClassElement(ABC):

    pass
class dsml_DGraph:

    pass
class dsml_DSemanticBridge:

    pass
class dsml_Diagraph:

    pass
class DContainedEdge:

    pass
class dsml_DLabel:

    def __init__(self, name: str, dsml_DLabel: "dsml_DNode" = None, dsml_DLabel25: "dsml_DLink" = None, dsml_DLabel48: "dsml_DAttributeBridge" = None):
        self.name = name
        self.dsml_DLabel = dsml_DLabel
        self.dsml_DLabel25 = dsml_DLabel25
        self.dsml_DLabel48 = dsml_DLabel48
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dsml_DLabel(self):
        return self.__dsml_DLabel

    @dsml_DLabel.setter
    def dsml_DLabel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_DLabel__dsml_DLabel", None)
        self.__dsml_DLabel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsml_DNode17"):
                opp_val = getattr(old_value, "dsml_DNode17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsml_DNode17"):
                opp_val = getattr(value, "dsml_DNode17", None)
                if opp_val is None:
                    setattr(value, "dsml_DNode17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsml_DLabel48(self):
        return self.__dsml_DLabel48

    @dsml_DLabel48.setter
    def dsml_DLabel48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_DLabel__dsml_DLabel48", None)
        self.__dsml_DLabel48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsml_DAttributeBridge"):
                opp_val = getattr(old_value, "dsml_DAttributeBridge", None)
                if opp_val == self:
                    setattr(old_value, "dsml_DAttributeBridge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsml_DAttributeBridge"):
                opp_val = getattr(value, "dsml_DAttributeBridge", None)
                setattr(value, "dsml_DAttributeBridge", self)

    @property
    def dsml_DLabel25(self):
        return self.__dsml_DLabel25

    @dsml_DLabel25.setter
    def dsml_DLabel25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_DLabel__dsml_DLabel25", None)
        self.__dsml_DLabel25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsml_DLink24"):
                opp_val = getattr(old_value, "dsml_DLink24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsml_DLink24"):
                opp_val = getattr(value, "dsml_DLink24", None)
                if opp_val is None:
                    setattr(value, "dsml_DLink24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class DContainedElement:

    pass
class DClassElement:

    pass
class dsml_DLink(DContainedEdge, DClassElement):

    pass
class dsml_DContainment(DContainedEdge):

    def __init__(self, compartment: bool):
        self.compartment = compartment
        
    @property
    def compartment(self) -> bool:
        return self.__compartment

    @compartment.setter
    def compartment(self, compartment: bool):
        self.__compartment = compartment

class DEdge:

    pass
class dsml_DContainedEdge(DEdge, DContainedElement):

    pass
class dsml_DReference(DEdge):

    def __init__(self, nonGraphicalProperty: bool):
        self.nonGraphicalProperty = nonGraphicalProperty
        
    @property
    def nonGraphicalProperty(self) -> bool:
        return self.__nonGraphicalProperty

    @nonGraphicalProperty.setter
    def nonGraphicalProperty(self, nonGraphicalProperty: bool):
        self.__nonGraphicalProperty = nonGraphicalProperty

class dsml_EReference:

    pass
class DGraphElement:

    pass
class dsml_DContainedElement(DGraphElement):

    pass
class dsml_DNode(DGraphElement, DClassElement, DContainedElement):

    def __init__(self, pointOfView: bool, pointOfViewName: str, dsml_DNode5: "dsml_DEdge" = None, dsml_DNode: "dsml_DEdge" = None, dsml_DNode9: set["dsml_DEdge"] = None, DNode: "dsml_DNode" = None, childrenPointOfView: "dsml_DNode" = None, DNode15: "dsml_DNode" = None, parentPointOfView: set["dsml_DNode"] = None, dsml_DNode17: set["dsml_DLabel"] = None, dsml_DNode27: "dsml_DGraph" = None, dsml_DNode30: "dsml_DGraph" = None, dsml_DNode37: "dsml_DContainedElement" = None):
        self.pointOfView = pointOfView
        self.pointOfViewName = pointOfViewName
        self.dsml_DNode5 = dsml_DNode5
        self.dsml_DNode = dsml_DNode
        self.dsml_DNode9 = dsml_DNode9 if dsml_DNode9 is not None else set()
        self.DNode = DNode
        self.childrenPointOfView = childrenPointOfView
        self.DNode15 = DNode15
        self.parentPointOfView = parentPointOfView if parentPointOfView is not None else set()
        self.dsml_DNode17 = dsml_DNode17 if dsml_DNode17 is not None else set()
        self.dsml_DNode27 = dsml_DNode27
        self.dsml_DNode30 = dsml_DNode30
        self.dsml_DNode37 = dsml_DNode37
        
    @property
    def pointOfViewName(self) -> str:
        return self.__pointOfViewName

    @pointOfViewName.setter
    def pointOfViewName(self, pointOfViewName: str):
        self.__pointOfViewName = pointOfViewName

    @property
    def pointOfView(self) -> bool:
        return self.__pointOfView

    @pointOfView.setter
    def pointOfView(self, pointOfView: bool):
        self.__pointOfView = pointOfView

    @property
    def parentPointOfView(self):
        return self.__parentPointOfView

    @parentPointOfView.setter
    def parentPointOfView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_DNode__parentPointOfView", None)
        self.__parentPointOfView = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DNode15"):
                    opp_val = getattr(item, "DNode15", None)
                    
                    if opp_val == self:
                        setattr(item, "DNode15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DNode15"):
                    opp_val = getattr(item, "DNode15", None)
                    
                    setattr(item, "DNode15", self)
                    

    @property
    def dsml_DNode30(self):
        return self.__dsml_DNode30

    @dsml_DNode30.setter
    def dsml_DNode30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_DNode__dsml_DNode30", None)
        self.__dsml_DNode30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsml_DGraph29"):
                opp_val = getattr(old_value, "dsml_DGraph29", None)
                if opp_val == self:
                    setattr(old_value, "dsml_DGraph29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsml_DGraph29"):
                opp_val = getattr(value, "dsml_DGraph29", None)
                setattr(value, "dsml_DGraph29", self)

    @property
    def dsml_DNode27(self):
        return self.__dsml_DNode27

    @dsml_DNode27.setter
    def dsml_DNode27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_DNode__dsml_DNode27", None)
        self.__dsml_DNode27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsml_DGraph"):
                opp_val = getattr(old_value, "dsml_DGraph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsml_DGraph"):
                opp_val = getattr(value, "dsml_DGraph", None)
                if opp_val is None:
                    setattr(value, "dsml_DGraph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dsml_DNode9(self):
        return self.__dsml_DNode9

    @dsml_DNode9.setter
    def dsml_DNode9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_DNode__dsml_DNode9", None)
        self.__dsml_DNode9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsml_DEdge10"):
                    opp_val = getattr(item, "dsml_DEdge10", None)
                    
                    if opp_val == self:
                        setattr(item, "dsml_DEdge10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsml_DEdge10"):
                    opp_val = getattr(item, "dsml_DEdge10", None)
                    
                    setattr(item, "dsml_DEdge10", self)
                    

    @property
    def DNode(self):
        return self.__DNode

    @DNode.setter
    def DNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_DNode__DNode", None)
        self.__DNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "childrenPointOfView"):
                opp_val = getattr(old_value, "childrenPointOfView", None)
                if opp_val == self:
                    setattr(old_value, "childrenPointOfView", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "childrenPointOfView"):
                opp_val = getattr(value, "childrenPointOfView", None)
                setattr(value, "childrenPointOfView", self)

    @property
    def dsml_DNode5(self):
        return self.__dsml_DNode5

    @dsml_DNode5.setter
    def dsml_DNode5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_DNode__dsml_DNode5", None)
        self.__dsml_DNode5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsml_DEdge4"):
                opp_val = getattr(old_value, "dsml_DEdge4", None)
                if opp_val == self:
                    setattr(old_value, "dsml_DEdge4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsml_DEdge4"):
                opp_val = getattr(value, "dsml_DEdge4", None)
                setattr(value, "dsml_DEdge4", self)

    @property
    def dsml_DNode(self):
        return self.__dsml_DNode

    @dsml_DNode.setter
    def dsml_DNode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_DNode__dsml_DNode", None)
        self.__dsml_DNode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsml_DEdge"):
                opp_val = getattr(old_value, "dsml_DEdge", None)
                if opp_val == self:
                    setattr(old_value, "dsml_DEdge", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsml_DEdge"):
                opp_val = getattr(value, "dsml_DEdge", None)
                setattr(value, "dsml_DEdge", self)

    @property
    def dsml_DNode17(self):
        return self.__dsml_DNode17

    @dsml_DNode17.setter
    def dsml_DNode17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_DNode__dsml_DNode17", None)
        self.__dsml_DNode17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dsml_DLabel"):
                    opp_val = getattr(item, "dsml_DLabel", None)
                    
                    if opp_val == self:
                        setattr(item, "dsml_DLabel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dsml_DLabel"):
                    opp_val = getattr(item, "dsml_DLabel", None)
                    
                    setattr(item, "dsml_DLabel", self)
                    

    @property
    def DNode15(self):
        return self.__DNode15

    @DNode15.setter
    def DNode15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_DNode__DNode15", None)
        self.__DNode15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentPointOfView"):
                opp_val = getattr(old_value, "parentPointOfView", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentPointOfView"):
                opp_val = getattr(value, "parentPointOfView", None)
                if opp_val is None:
                    setattr(value, "parentPointOfView", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def childrenPointOfView(self):
        return self.__childrenPointOfView

    @childrenPointOfView.setter
    def childrenPointOfView(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_DNode__childrenPointOfView", None)
        self.__childrenPointOfView = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DNode"):
                opp_val = getattr(old_value, "DNode", None)
                if opp_val == self:
                    setattr(old_value, "DNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DNode"):
                opp_val = getattr(value, "DNode", None)
                setattr(value, "DNode", self)

    @property
    def dsml_DNode37(self):
        return self.__dsml_DNode37

    @dsml_DNode37.setter
    def dsml_DNode37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dsml_DNode__dsml_DNode37", None)
        self.__dsml_DNode37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dsml_DContainedElement"):
                opp_val = getattr(old_value, "dsml_DContainedElement", None)
                if opp_val == self:
                    setattr(old_value, "dsml_DContainedElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dsml_DContainedElement"):
                opp_val = getattr(value, "dsml_DContainedElement", None)
                setattr(value, "dsml_DContainedElement", self)

class dsml_DEdge(DGraphElement):

    pass
class dsml_DGraphElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class dsml_DReferenceBridge(DModelElementBridge):

    pass