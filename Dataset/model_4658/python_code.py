from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ParticipantBandKind(Enum):
    top_initiating = "top_initiating"
    middle_initiating = "middle_initiating"
    bottom_initiating = "bottom_initiating"
    top_non_initiating = "top_non_initiating"
    middle_non_initiating = "middle_non_initiating"
    bottom_non_initiating = "bottom_non_initiating"
class MessageVisibleKind(Enum):
    initiating = "initiating"
    non_initiating = "non_initiating"


############################################
# Definition of Classes
############################################

class LabeledShape:

    pass
class Plane:

    pass
class di_Font:

    pass
class Style:

    pass
class Label:

    pass
class di_DiagramElement:

    pass
class di_BaseElement:

    pass
class LabeledEdge:

    pass
class di_BPMNShape(LabeledShape):

    def __init__(self, isMessageVisible: bool, participantBandKind: str, isExpanded: bool, isHorizontal: bool, isMarkerVisible: bool, di_BPMNShape: "di_DocumentRoot" = None, di_BPMNShape41: "di_BPMNLabel" = None, di_BPMNShape44: "di_BaseElement" = None, di_BPMNShape48: "di_BPMNShape" = None, di_BPMNShape46: "di_BPMNShape" = None):
        self.isMessageVisible = isMessageVisible
        self.participantBandKind = participantBandKind
        self.isExpanded = isExpanded
        self.isHorizontal = isHorizontal
        self.isMarkerVisible = isMarkerVisible
        self.di_BPMNShape = di_BPMNShape
        self.di_BPMNShape41 = di_BPMNShape41
        self.di_BPMNShape44 = di_BPMNShape44
        self.di_BPMNShape48 = di_BPMNShape48
        self.di_BPMNShape46 = di_BPMNShape46
        
    @property
    def isMarkerVisible(self) -> bool:
        return self.__isMarkerVisible

    @isMarkerVisible.setter
    def isMarkerVisible(self, isMarkerVisible: bool):
        self.__isMarkerVisible = isMarkerVisible

    @property
    def isHorizontal(self) -> bool:
        return self.__isHorizontal

    @isHorizontal.setter
    def isHorizontal(self, isHorizontal: bool):
        self.__isHorizontal = isHorizontal

    @property
    def participantBandKind(self) -> str:
        return self.__participantBandKind

    @participantBandKind.setter
    def participantBandKind(self, participantBandKind: str):
        self.__participantBandKind = participantBandKind

    @property
    def isMessageVisible(self) -> bool:
        return self.__isMessageVisible

    @isMessageVisible.setter
    def isMessageVisible(self, isMessageVisible: bool):
        self.__isMessageVisible = isMessageVisible

    @property
    def isExpanded(self) -> bool:
        return self.__isExpanded

    @isExpanded.setter
    def isExpanded(self, isExpanded: bool):
        self.__isExpanded = isExpanded

    @property
    def di_BPMNShape48(self):
        return self.__di_BPMNShape48

    @di_BPMNShape48.setter
    def di_BPMNShape48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_BPMNShape__di_BPMNShape48", None)
        self.__di_BPMNShape48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_BPMNShape46"):
                opp_val = getattr(old_value, "di_BPMNShape46", None)
                if opp_val == self:
                    setattr(old_value, "di_BPMNShape46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_BPMNShape46"):
                opp_val = getattr(value, "di_BPMNShape46", None)
                setattr(value, "di_BPMNShape46", self)

    @property
    def di_BPMNShape46(self):
        return self.__di_BPMNShape46

    @di_BPMNShape46.setter
    def di_BPMNShape46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_BPMNShape__di_BPMNShape46", None)
        self.__di_BPMNShape46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_BPMNShape48"):
                opp_val = getattr(old_value, "di_BPMNShape48", None)
                if opp_val == self:
                    setattr(old_value, "di_BPMNShape48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_BPMNShape48"):
                opp_val = getattr(value, "di_BPMNShape48", None)
                setattr(value, "di_BPMNShape48", self)

    @property
    def di_BPMNShape(self):
        return self.__di_BPMNShape

    @di_BPMNShape.setter
    def di_BPMNShape(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_BPMNShape__di_BPMNShape", None)
        self.__di_BPMNShape = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_DocumentRoot15"):
                opp_val = getattr(old_value, "di_DocumentRoot15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_DocumentRoot15"):
                opp_val = getattr(value, "di_DocumentRoot15", None)
                if opp_val is None:
                    setattr(value, "di_DocumentRoot15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def di_BPMNShape41(self):
        return self.__di_BPMNShape41

    @di_BPMNShape41.setter
    def di_BPMNShape41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_BPMNShape__di_BPMNShape41", None)
        self.__di_BPMNShape41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_BPMNLabel42"):
                opp_val = getattr(old_value, "di_BPMNLabel42", None)
                if opp_val == self:
                    setattr(old_value, "di_BPMNLabel42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_BPMNLabel42"):
                opp_val = getattr(value, "di_BPMNLabel42", None)
                setattr(value, "di_BPMNLabel42", self)

    @property
    def di_BPMNShape44(self):
        return self.__di_BPMNShape44

    @di_BPMNShape44.setter
    def di_BPMNShape44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_BPMNShape__di_BPMNShape44", None)
        self.__di_BPMNShape44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_BaseElement45"):
                opp_val = getattr(old_value, "di_BaseElement45", None)
                if opp_val == self:
                    setattr(old_value, "di_BaseElement45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_BaseElement45"):
                opp_val = getattr(value, "di_BaseElement45", None)
                setattr(value, "di_BaseElement45", self)

class di_BPMNPlane(Plane):

    pass
class di_BPMNLabelStyle(Style):

    pass
class di_BPMNLabel(Label):

    pass
class di_BPMNEdge(LabeledEdge):

    def __init__(self, messageVisibleKind: str, di_BPMNEdge: "di_DocumentRoot" = None, di_BPMNEdge23: "di_BPMNLabel" = None, di_BPMNEdge26: "di_BaseElement" = None, di_BPMNEdge28: "di_DiagramElement" = None, di_BPMNEdge30: "di_DiagramElement" = None):
        self.messageVisibleKind = messageVisibleKind
        self.di_BPMNEdge = di_BPMNEdge
        self.di_BPMNEdge23 = di_BPMNEdge23
        self.di_BPMNEdge26 = di_BPMNEdge26
        self.di_BPMNEdge28 = di_BPMNEdge28
        self.di_BPMNEdge30 = di_BPMNEdge30
        
    @property
    def messageVisibleKind(self) -> str:
        return self.__messageVisibleKind

    @messageVisibleKind.setter
    def messageVisibleKind(self, messageVisibleKind: str):
        self.__messageVisibleKind = messageVisibleKind

    @property
    def di_BPMNEdge23(self):
        return self.__di_BPMNEdge23

    @di_BPMNEdge23.setter
    def di_BPMNEdge23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_BPMNEdge__di_BPMNEdge23", None)
        self.__di_BPMNEdge23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_BPMNLabel24"):
                opp_val = getattr(old_value, "di_BPMNLabel24", None)
                if opp_val == self:
                    setattr(old_value, "di_BPMNLabel24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_BPMNLabel24"):
                opp_val = getattr(value, "di_BPMNLabel24", None)
                setattr(value, "di_BPMNLabel24", self)

    @property
    def di_BPMNEdge(self):
        return self.__di_BPMNEdge

    @di_BPMNEdge.setter
    def di_BPMNEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_BPMNEdge__di_BPMNEdge", None)
        self.__di_BPMNEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_DocumentRoot7"):
                opp_val = getattr(old_value, "di_DocumentRoot7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_DocumentRoot7"):
                opp_val = getattr(value, "di_DocumentRoot7", None)
                if opp_val is None:
                    setattr(value, "di_DocumentRoot7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def di_BPMNEdge30(self):
        return self.__di_BPMNEdge30

    @di_BPMNEdge30.setter
    def di_BPMNEdge30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_BPMNEdge__di_BPMNEdge30", None)
        self.__di_BPMNEdge30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_DiagramElement31"):
                opp_val = getattr(old_value, "di_DiagramElement31", None)
                if opp_val == self:
                    setattr(old_value, "di_DiagramElement31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_DiagramElement31"):
                opp_val = getattr(value, "di_DiagramElement31", None)
                setattr(value, "di_DiagramElement31", self)

    @property
    def di_BPMNEdge28(self):
        return self.__di_BPMNEdge28

    @di_BPMNEdge28.setter
    def di_BPMNEdge28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_BPMNEdge__di_BPMNEdge28", None)
        self.__di_BPMNEdge28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_DiagramElement"):
                opp_val = getattr(old_value, "di_DiagramElement", None)
                if opp_val == self:
                    setattr(old_value, "di_DiagramElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_DiagramElement"):
                opp_val = getattr(value, "di_DiagramElement", None)
                setattr(value, "di_DiagramElement", self)

    @property
    def di_BPMNEdge26(self):
        return self.__di_BPMNEdge26

    @di_BPMNEdge26.setter
    def di_BPMNEdge26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_BPMNEdge__di_BPMNEdge26", None)
        self.__di_BPMNEdge26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_BaseElement"):
                opp_val = getattr(old_value, "di_BaseElement", None)
                if opp_val == self:
                    setattr(old_value, "di_BaseElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_BaseElement"):
                opp_val = getattr(value, "di_BaseElement", None)
                setattr(value, "di_BaseElement", self)

class Diagram:

    pass
class di_BPMNDiagram(Diagram):

    def __init__(self, version: str, phase: str, featureModel: str, location: str, di_BPMNDiagram: "di_DocumentRoot" = None, di_BPMNDiagram17: "di_BPMNPlane" = None, di_BPMNDiagram20: set["di_BPMNLabelStyle"] = None):
        self.version = version
        self.phase = phase
        self.featureModel = featureModel
        self.location = location
        self.di_BPMNDiagram = di_BPMNDiagram
        self.di_BPMNDiagram17 = di_BPMNDiagram17
        self.di_BPMNDiagram20 = di_BPMNDiagram20 if di_BPMNDiagram20 is not None else set()
        
    @property
    def featureModel(self) -> str:
        return self.__featureModel

    @featureModel.setter
    def featureModel(self, featureModel: str):
        self.__featureModel = featureModel

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def phase(self) -> str:
        return self.__phase

    @phase.setter
    def phase(self, phase: str):
        self.__phase = phase

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def di_BPMNDiagram17(self):
        return self.__di_BPMNDiagram17

    @di_BPMNDiagram17.setter
    def di_BPMNDiagram17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_BPMNDiagram__di_BPMNDiagram17", None)
        self.__di_BPMNDiagram17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_BPMNPlane18"):
                opp_val = getattr(old_value, "di_BPMNPlane18", None)
                if opp_val == self:
                    setattr(old_value, "di_BPMNPlane18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_BPMNPlane18"):
                opp_val = getattr(value, "di_BPMNPlane18", None)
                setattr(value, "di_BPMNPlane18", self)

    @property
    def di_BPMNDiagram20(self):
        return self.__di_BPMNDiagram20

    @di_BPMNDiagram20.setter
    def di_BPMNDiagram20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_BPMNDiagram__di_BPMNDiagram20", None)
        self.__di_BPMNDiagram20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_BPMNLabelStyle21"):
                    opp_val = getattr(item, "di_BPMNLabelStyle21", None)
                    
                    if opp_val == self:
                        setattr(item, "di_BPMNLabelStyle21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_BPMNLabelStyle21"):
                    opp_val = getattr(item, "di_BPMNLabelStyle21", None)
                    
                    setattr(item, "di_BPMNLabelStyle21", self)
                    

    @property
    def di_BPMNDiagram(self):
        return self.__di_BPMNDiagram

    @di_BPMNDiagram.setter
    def di_BPMNDiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_BPMNDiagram__di_BPMNDiagram", None)
        self.__di_BPMNDiagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "di_DocumentRoot5"):
                opp_val = getattr(old_value, "di_DocumentRoot5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "di_DocumentRoot5"):
                opp_val = getattr(value, "di_DocumentRoot5", None)
                if opp_val is None:
                    setattr(value, "di_DocumentRoot5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class di_DocumentRoot:

    def __init__(self, mixed: str, di_DocumentRoot: set["di_EStringToStringMapEntry"] = None, di_DocumentRoot2: set["di_EStringToStringMapEntry"] = None, di_DocumentRoot5: set["di_BPMNDiagram"] = None, di_DocumentRoot7: set["di_BPMNEdge"] = None, di_DocumentRoot9: set["di_BPMNLabel"] = None, di_DocumentRoot11: set["di_BPMNLabelStyle"] = None, di_DocumentRoot13: set["di_BPMNPlane"] = None, di_DocumentRoot15: set["di_BPMNShape"] = None):
        self.mixed = mixed
        self.di_DocumentRoot = di_DocumentRoot if di_DocumentRoot is not None else set()
        self.di_DocumentRoot2 = di_DocumentRoot2 if di_DocumentRoot2 is not None else set()
        self.di_DocumentRoot5 = di_DocumentRoot5 if di_DocumentRoot5 is not None else set()
        self.di_DocumentRoot7 = di_DocumentRoot7 if di_DocumentRoot7 is not None else set()
        self.di_DocumentRoot9 = di_DocumentRoot9 if di_DocumentRoot9 is not None else set()
        self.di_DocumentRoot11 = di_DocumentRoot11 if di_DocumentRoot11 is not None else set()
        self.di_DocumentRoot13 = di_DocumentRoot13 if di_DocumentRoot13 is not None else set()
        self.di_DocumentRoot15 = di_DocumentRoot15 if di_DocumentRoot15 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def di_DocumentRoot15(self):
        return self.__di_DocumentRoot15

    @di_DocumentRoot15.setter
    def di_DocumentRoot15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot15", None)
        self.__di_DocumentRoot15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_BPMNShape"):
                    opp_val = getattr(item, "di_BPMNShape", None)
                    
                    if opp_val == self:
                        setattr(item, "di_BPMNShape", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_BPMNShape"):
                    opp_val = getattr(item, "di_BPMNShape", None)
                    
                    setattr(item, "di_BPMNShape", self)
                    

    @property
    def di_DocumentRoot11(self):
        return self.__di_DocumentRoot11

    @di_DocumentRoot11.setter
    def di_DocumentRoot11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot11", None)
        self.__di_DocumentRoot11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_BPMNLabelStyle"):
                    opp_val = getattr(item, "di_BPMNLabelStyle", None)
                    
                    if opp_val == self:
                        setattr(item, "di_BPMNLabelStyle", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_BPMNLabelStyle"):
                    opp_val = getattr(item, "di_BPMNLabelStyle", None)
                    
                    setattr(item, "di_BPMNLabelStyle", self)
                    

    @property
    def di_DocumentRoot7(self):
        return self.__di_DocumentRoot7

    @di_DocumentRoot7.setter
    def di_DocumentRoot7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot7", None)
        self.__di_DocumentRoot7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_BPMNEdge"):
                    opp_val = getattr(item, "di_BPMNEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "di_BPMNEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_BPMNEdge"):
                    opp_val = getattr(item, "di_BPMNEdge", None)
                    
                    setattr(item, "di_BPMNEdge", self)
                    

    @property
    def di_DocumentRoot13(self):
        return self.__di_DocumentRoot13

    @di_DocumentRoot13.setter
    def di_DocumentRoot13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot13", None)
        self.__di_DocumentRoot13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_BPMNPlane"):
                    opp_val = getattr(item, "di_BPMNPlane", None)
                    
                    if opp_val == self:
                        setattr(item, "di_BPMNPlane", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_BPMNPlane"):
                    opp_val = getattr(item, "di_BPMNPlane", None)
                    
                    setattr(item, "di_BPMNPlane", self)
                    

    @property
    def di_DocumentRoot5(self):
        return self.__di_DocumentRoot5

    @di_DocumentRoot5.setter
    def di_DocumentRoot5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot5", None)
        self.__di_DocumentRoot5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_BPMNDiagram"):
                    opp_val = getattr(item, "di_BPMNDiagram", None)
                    
                    if opp_val == self:
                        setattr(item, "di_BPMNDiagram", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_BPMNDiagram"):
                    opp_val = getattr(item, "di_BPMNDiagram", None)
                    
                    setattr(item, "di_BPMNDiagram", self)
                    

    @property
    def di_DocumentRoot(self):
        return self.__di_DocumentRoot

    @di_DocumentRoot.setter
    def di_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot", None)
        self.__di_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_EStringToStringMapEntry"):
                    opp_val = getattr(item, "di_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "di_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_EStringToStringMapEntry"):
                    opp_val = getattr(item, "di_EStringToStringMapEntry", None)
                    
                    setattr(item, "di_EStringToStringMapEntry", self)
                    

    @property
    def di_DocumentRoot2(self):
        return self.__di_DocumentRoot2

    @di_DocumentRoot2.setter
    def di_DocumentRoot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot2", None)
        self.__di_DocumentRoot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "di_EStringToStringMapEntry3", None)
                    
                    if opp_val == self:
                        setattr(item, "di_EStringToStringMapEntry3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "di_EStringToStringMapEntry3", None)
                    
                    setattr(item, "di_EStringToStringMapEntry3", self)
                    

    @property
    def di_DocumentRoot9(self):
        return self.__di_DocumentRoot9

    @di_DocumentRoot9.setter
    def di_DocumentRoot9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_di_DocumentRoot__di_DocumentRoot9", None)
        self.__di_DocumentRoot9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "di_BPMNLabel"):
                    opp_val = getattr(item, "di_BPMNLabel", None)
                    
                    if opp_val == self:
                        setattr(item, "di_BPMNLabel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "di_BPMNLabel"):
                    opp_val = getattr(item, "di_BPMNLabel", None)
                    
                    setattr(item, "di_BPMNLabel", self)
                    

class di_EStringToStringMapEntry:

    pass