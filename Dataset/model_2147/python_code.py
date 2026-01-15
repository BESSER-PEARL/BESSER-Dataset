from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class DirectionType(Enum):
    None = "None"
    To = "To"
    From = "From"
    Both = "Both"
class ActivityType(Enum):
    EventIntermediateLink = "EventIntermediateLink"
    EventIntermediateMultiple = "EventIntermediateMultiple"
    EventIntermediateCancel = "EventIntermediateCancel"
    EventEndEmpty = "EventEndEmpty"
    EventEndMessage = "EventEndMessage"
    EventEndError = "EventEndError"
    EventEndCompensation = "EventEndCompensation"
    EventEndTerminate = "EventEndTerminate"
    EventEndLink = "EventEndLink"
    EventEndMultiple = "EventEndMultiple"
    EventEndCancel = "EventEndCancel"
    GatewayDataBasedExclusive = "GatewayDataBasedExclusive"
    GatewayEventBasedExclusive = "GatewayEventBasedExclusive"
    Task = "Task"
    SubProcess = "SubProcess"
    EventStartEmpty = "EventStartEmpty"
    EventStartMessage = "EventStartMessage"
    EventStartRule = "EventStartRule"
    EventStartTimer = "EventStartTimer"
    EventStartLink = "EventStartLink"
    EventStartMultiple = "EventStartMultiple"
    EventIntermediateEmpty = "EventIntermediateEmpty"
    EventIntermediateMessage = "EventIntermediateMessage"
    EventIntermediateTimer = "EventIntermediateTimer"
    EventIntermediateError = "EventIntermediateError"
    EventIntermediateCompensation = "EventIntermediateCompensation"
    EventIntermediateRule = "EventIntermediateRule"
    GatewayDataBasedInclusive = "GatewayDataBasedInclusive"
    GatewayParallel = "GatewayParallel"
    GatewayComplex = "GatewayComplex"
    EventStartSignal = "EventStartSignal"
    EventIntermediateSignal = "EventIntermediateSignal"
    EventEndSignal = "EventEndSignal"
class SequenceFlowConditionType(Enum):
    None = "None"
    Expression = "Expression"
    Default = "Default"


############################################
# Definition of Classes
############################################

class Activity:

    pass
class Graph:

    pass
class bpmn_NamedBpmnObject:

    def __init__(self, documentation: str, name: str, ncname: str):
        self.documentation = documentation
        self.name = name
        self.ncname = ncname
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def documentation(self) -> str:
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation

    @property
    def ncname(self) -> str:
        return self.__ncname

    @ncname.setter
    def ncname(self, ncname: str):
        self.__ncname = ncname

class Artifact:

    pass
class bpmn_TextAnnotation(Artifact):

    pass
class bpmn_DataObject(Artifact):

    pass
class ArtifactsContainer:

    pass
class AssociationTarget:

    pass
class bpmn_Vertex(AssociationTarget):

    pass
class bpmn_Graph(ArtifactsContainer, AssociationTarget):

    pass
class EModelElement:

    pass
class bpmn_Identifiable(EModelElement):

    def __init__(self, iD: str):
        self.iD = iD
        
    @property
    def iD(self) -> str:
        return self.__iD

    @iD.setter
    def iD(self, iD: str):
        self.__iD = iD

class bpmn_Association(EModelElement):

    def __init__(self, direction: str, associations: "bpmn_Artifact" = None, associations10: "bpmn_AssociationTarget" = None, Association: "bpmn_Artifact" = None, Association12: "bpmn_AssociationTarget" = None):
        self.direction = direction
        self.associations = associations
        self.associations10 = associations10
        self.Association = Association
        self.Association12 = Association12
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def associations(self):
        return self.__associations

    @associations.setter
    def associations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_Association__associations", None)
        self.__associations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Artifact8"):
                opp_val = getattr(old_value, "Artifact8", None)
                if opp_val == self:
                    setattr(old_value, "Artifact8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Artifact8"):
                opp_val = getattr(value, "Artifact8", None)
                setattr(value, "Artifact8", self)

    @property
    def associations10(self):
        return self.__associations10

    @associations10.setter
    def associations10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_Association__associations10", None)
        self.__associations10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AssociationTarget"):
                opp_val = getattr(old_value, "AssociationTarget", None)
                if opp_val == self:
                    setattr(old_value, "AssociationTarget", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssociationTarget"):
                opp_val = getattr(value, "AssociationTarget", None)
                setattr(value, "AssociationTarget", self)

    @property
    def Association12(self):
        return self.__Association12

    @Association12.setter
    def Association12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_Association__Association12", None)
        self.__Association12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target"):
                opp_val = getattr(old_value, "target", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target"):
                opp_val = getattr(value, "target", None)
                if opp_val is None:
                    setattr(value, "target", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Association(self):
        return self.__Association

    @Association.setter
    def Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_Association__Association", None)
        self.__Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedBpmnObject:

    pass
class bpmn_ArtifactsContainer(NamedBpmnObject):

    pass
class bpmn_SequenceEdge(NamedBpmnObject, AssociationTarget):

    def __init__(self, conditionType: str, isDefault: str, SequenceEdge: "bpmn_Graph" = None, outgoingEdges: "bpmn_Vertex" = None, incomingEdges: "bpmn_Vertex" = None, sequenceEdges: "bpmn_Graph" = None, SequenceEdge48: "bpmn_Vertex" = None, SequenceEdge51: "bpmn_Vertex" = None):
        self.conditionType = conditionType
        self.isDefault = isDefault
        self.SequenceEdge = SequenceEdge
        self.outgoingEdges = outgoingEdges
        self.incomingEdges = incomingEdges
        self.sequenceEdges = sequenceEdges
        self.SequenceEdge48 = SequenceEdge48
        self.SequenceEdge51 = SequenceEdge51
        
    @property
    def conditionType(self) -> str:
        return self.__conditionType

    @conditionType.setter
    def conditionType(self, conditionType: str):
        self.__conditionType = conditionType

    @property
    def isDefault(self) -> str:
        return self.__isDefault

    @isDefault.setter
    def isDefault(self, isDefault: str):
        self.__isDefault = isDefault

    @property
    def SequenceEdge51(self):
        return self.__SequenceEdge51

    @SequenceEdge51.setter
    def SequenceEdge51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_SequenceEdge__SequenceEdge51", None)
        self.__SequenceEdge51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target50"):
                opp_val = getattr(old_value, "target50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target50"):
                opp_val = getattr(value, "target50", None)
                if opp_val is None:
                    setattr(value, "target50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def incomingEdges(self):
        return self.__incomingEdges

    @incomingEdges.setter
    def incomingEdges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_SequenceEdge__incomingEdges", None)
        self.__incomingEdges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex42"):
                opp_val = getattr(old_value, "Vertex42", None)
                if opp_val == self:
                    setattr(old_value, "Vertex42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex42"):
                opp_val = getattr(value, "Vertex42", None)
                setattr(value, "Vertex42", self)

    @property
    def sequenceEdges(self):
        return self.__sequenceEdges

    @sequenceEdges.setter
    def sequenceEdges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_SequenceEdge__sequenceEdges", None)
        self.__sequenceEdges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph"):
                opp_val = getattr(old_value, "Graph", None)
                if opp_val == self:
                    setattr(old_value, "Graph", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph"):
                opp_val = getattr(value, "Graph", None)
                setattr(value, "Graph", self)

    @property
    def SequenceEdge48(self):
        return self.__SequenceEdge48

    @SequenceEdge48.setter
    def SequenceEdge48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_SequenceEdge__SequenceEdge48", None)
        self.__SequenceEdge48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source47"):
                opp_val = getattr(old_value, "source47", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source47"):
                opp_val = getattr(value, "source47", None)
                if opp_val is None:
                    setattr(value, "source47", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def outgoingEdges(self):
        return self.__outgoingEdges

    @outgoingEdges.setter
    def outgoingEdges(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_SequenceEdge__outgoingEdges", None)
        self.__outgoingEdges = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Vertex40"):
                opp_val = getattr(old_value, "Vertex40", None)
                if opp_val == self:
                    setattr(old_value, "Vertex40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex40"):
                opp_val = getattr(value, "Vertex40", None)
                setattr(value, "Vertex40", self)

    @property
    def SequenceEdge(self):
        return self.__SequenceEdge

    @SequenceEdge.setter
    def SequenceEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_SequenceEdge__SequenceEdge", None)
        self.__SequenceEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph18"):
                opp_val = getattr(old_value, "graph18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph18"):
                opp_val = getattr(value, "graph18", None)
                if opp_val is None:
                    setattr(value, "graph18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bpmn_MessagingEdge(NamedBpmnObject, AssociationTarget):

    pass
class Identifiable:

    pass
class bpmn_MessageVertex(NamedBpmnObject, Identifiable):

    def __init__(self, orderedMessages: str, target26: set["bpmn_MessagingEdge"] = None, source29: set["bpmn_MessagingEdge"] = None, MessageVertex: "bpmn_MessagingEdge" = None, MessageVertex33: "bpmn_MessagingEdge" = None):
        self.orderedMessages = orderedMessages
        self.target26 = target26 if target26 is not None else set()
        self.source29 = source29 if source29 is not None else set()
        self.MessageVertex = MessageVertex
        self.MessageVertex33 = MessageVertex33
        
    @property
    def orderedMessages(self) -> str:
        return self.__orderedMessages

    @orderedMessages.setter
    def orderedMessages(self, orderedMessages: str):
        self.__orderedMessages = orderedMessages

    @property
    def MessageVertex(self):
        return self.__MessageVertex

    @MessageVertex.setter
    def MessageVertex(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_MessageVertex__MessageVertex", None)
        self.__MessageVertex = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outgoingMessages"):
                opp_val = getattr(old_value, "outgoingMessages", None)
                if opp_val == self:
                    setattr(old_value, "outgoingMessages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outgoingMessages"):
                opp_val = getattr(value, "outgoingMessages", None)
                setattr(value, "outgoingMessages", self)

    @property
    def MessageVertex33(self):
        return self.__MessageVertex33

    @MessageVertex33.setter
    def MessageVertex33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_MessageVertex__MessageVertex33", None)
        self.__MessageVertex33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "incomingMessages"):
                opp_val = getattr(old_value, "incomingMessages", None)
                if opp_val == self:
                    setattr(old_value, "incomingMessages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "incomingMessages"):
                opp_val = getattr(value, "incomingMessages", None)
                setattr(value, "incomingMessages", self)

    @property
    def source29(self):
        return self.__source29

    @source29.setter
    def source29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_MessageVertex__source29", None)
        self.__source29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessagingEdge30"):
                    opp_val = getattr(item, "MessagingEdge30", None)
                    
                    if opp_val == self:
                        setattr(item, "MessagingEdge30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessagingEdge30"):
                    opp_val = getattr(item, "MessagingEdge30", None)
                    
                    setattr(item, "MessagingEdge30", self)
                    

    @property
    def target26(self):
        return self.__target26

    @target26.setter
    def target26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_MessageVertex__target26", None)
        self.__target26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessagingEdge27"):
                    opp_val = getattr(item, "MessagingEdge27", None)
                    
                    if opp_val == self:
                        setattr(item, "MessagingEdge27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessagingEdge27"):
                    opp_val = getattr(item, "MessagingEdge27", None)
                    
                    setattr(item, "MessagingEdge27", self)
                    

class bpmn_BpmnDiagram(ArtifactsContainer, Identifiable):

    def __init__(self, author: str, title: str, bpmnDiagram: set["bpmn_Pool"] = None, bpmnDiagram15: set["bpmn_MessagingEdge"] = None, BpmnDiagram38: "bpmn_Pool" = None, BpmnDiagram: "bpmn_MessagingEdge" = None):
        self.author = author
        self.title = title
        self.bpmnDiagram = bpmnDiagram if bpmnDiagram is not None else set()
        self.bpmnDiagram15 = bpmnDiagram15 if bpmnDiagram15 is not None else set()
        self.BpmnDiagram38 = BpmnDiagram38
        self.BpmnDiagram = BpmnDiagram
        
    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def bpmnDiagram15(self):
        return self.__bpmnDiagram15

    @bpmnDiagram15.setter
    def bpmnDiagram15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_BpmnDiagram__bpmnDiagram15", None)
        self.__bpmnDiagram15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessagingEdge"):
                    opp_val = getattr(item, "MessagingEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "MessagingEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessagingEdge"):
                    opp_val = getattr(item, "MessagingEdge", None)
                    
                    setattr(item, "MessagingEdge", self)
                    

    @property
    def bpmnDiagram(self):
        return self.__bpmnDiagram

    @bpmnDiagram.setter
    def bpmnDiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_BpmnDiagram__bpmnDiagram", None)
        self.__bpmnDiagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Pool"):
                    opp_val = getattr(item, "Pool", None)
                    
                    if opp_val == self:
                        setattr(item, "Pool", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Pool"):
                    opp_val = getattr(item, "Pool", None)
                    
                    setattr(item, "Pool", self)
                    

    @property
    def BpmnDiagram38(self):
        return self.__BpmnDiagram38

    @BpmnDiagram38.setter
    def BpmnDiagram38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_BpmnDiagram__BpmnDiagram38", None)
        self.__BpmnDiagram38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pools"):
                opp_val = getattr(old_value, "pools", None)
                if opp_val == self:
                    setattr(old_value, "pools", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pools"):
                opp_val = getattr(value, "pools", None)
                setattr(value, "pools", self)

    @property
    def BpmnDiagram(self):
        return self.__BpmnDiagram

    @BpmnDiagram.setter
    def BpmnDiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_BpmnDiagram__BpmnDiagram", None)
        self.__BpmnDiagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "messages"):
                opp_val = getattr(old_value, "messages", None)
                if opp_val == self:
                    setattr(old_value, "messages", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "messages"):
                opp_val = getattr(value, "messages", None)
                setattr(value, "messages", self)

class bpmn_Artifact(NamedBpmnObject, Identifiable):

    pass
class bpmn_AssociationTarget(Identifiable):

    pass
class bpmn_SubProcess(Activity, Graph):

    def __init__(self, isTransaction: str, adhoc: str, SubProcess: "bpmn_Activity" = None, eventHandlerFor: set["bpmn_Activity"] = None):
        self.isTransaction = isTransaction
        self.adhoc = adhoc
        self.SubProcess = SubProcess
        self.eventHandlerFor = eventHandlerFor if eventHandlerFor is not None else set()
        
    @property
    def isTransaction(self) -> str:
        return self.__isTransaction

    @isTransaction.setter
    def isTransaction(self, isTransaction: str):
        self.__isTransaction = isTransaction

    @property
    def adhoc(self) -> str:
        return self.__adhoc

    @adhoc.setter
    def adhoc(self, adhoc: str):
        self.__adhoc = adhoc

    @property
    def eventHandlerFor(self):
        return self.__eventHandlerFor

    @eventHandlerFor.setter
    def eventHandlerFor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_SubProcess__eventHandlerFor", None)
        self.__eventHandlerFor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Activity45"):
                    opp_val = getattr(item, "Activity45", None)
                    
                    if opp_val == self:
                        setattr(item, "Activity45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Activity45"):
                    opp_val = getattr(item, "Activity45", None)
                    
                    setattr(item, "Activity45", self)
                    

    @property
    def SubProcess(self):
        return self.__SubProcess

    @SubProcess.setter
    def SubProcess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_SubProcess__SubProcess", None)
        self.__SubProcess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eventHandlers"):
                opp_val = getattr(old_value, "eventHandlers", None)
                if opp_val == self:
                    setattr(old_value, "eventHandlers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eventHandlers"):
                opp_val = getattr(value, "eventHandlers", None)
                setattr(value, "eventHandlers", self)

class bpmn_Lane(NamedBpmnObject, AssociationTarget):

    pass
class bpmn_Group(Artifact):

    pass
class MessageVertex:

    pass
class bpmn_Pool(Graph, MessageVertex):

    pass
class Vertex:

    pass
class bpmn_Activity(Vertex, MessageVertex):

    def __init__(self, activityType: str, looping: str, activities: set["bpmn_Group"] = None, activities2: set["bpmn_Lane"] = None, eventHandlers: "bpmn_SubProcess" = None, Activity: "bpmn_Group" = None, Activity21: "bpmn_Lane" = None, Activity45: "bpmn_SubProcess" = None):
        self.activityType = activityType
        self.looping = looping
        self.activities = activities if activities is not None else set()
        self.activities2 = activities2 if activities2 is not None else set()
        self.eventHandlers = eventHandlers
        self.Activity = Activity
        self.Activity21 = Activity21
        self.Activity45 = Activity45
        
    @property
    def activityType(self) -> str:
        return self.__activityType

    @activityType.setter
    def activityType(self, activityType: str):
        self.__activityType = activityType

    @property
    def looping(self) -> str:
        return self.__looping

    @looping.setter
    def looping(self, looping: str):
        self.__looping = looping

    @property
    def Activity21(self):
        return self.__Activity21

    @Activity21.setter
    def Activity21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_Activity__Activity21", None)
        self.__Activity21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lanes"):
                opp_val = getattr(old_value, "lanes", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lanes"):
                opp_val = getattr(value, "lanes", None)
                if opp_val is None:
                    setattr(value, "lanes", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eventHandlers(self):
        return self.__eventHandlers

    @eventHandlers.setter
    def eventHandlers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_Activity__eventHandlers", None)
        self.__eventHandlers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SubProcess"):
                opp_val = getattr(old_value, "SubProcess", None)
                if opp_val == self:
                    setattr(old_value, "SubProcess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SubProcess"):
                opp_val = getattr(value, "SubProcess", None)
                setattr(value, "SubProcess", self)

    @property
    def activities2(self):
        return self.__activities2

    @activities2.setter
    def activities2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_Activity__activities2", None)
        self.__activities2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Lane"):
                    opp_val = getattr(item, "Lane", None)
                    
                    if opp_val == self:
                        setattr(item, "Lane", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Lane"):
                    opp_val = getattr(item, "Lane", None)
                    
                    setattr(item, "Lane", self)
                    

    @property
    def Activity45(self):
        return self.__Activity45

    @Activity45.setter
    def Activity45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_Activity__Activity45", None)
        self.__Activity45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eventHandlerFor"):
                opp_val = getattr(old_value, "eventHandlerFor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eventHandlerFor"):
                opp_val = getattr(value, "eventHandlerFor", None)
                if opp_val is None:
                    setattr(value, "eventHandlerFor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Activity(self):
        return self.__Activity

    @Activity.setter
    def Activity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_Activity__Activity", None)
        self.__Activity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "groups"):
                opp_val = getattr(old_value, "groups", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "groups"):
                opp_val = getattr(value, "groups", None)
                if opp_val is None:
                    setattr(value, "groups", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def activities(self):
        return self.__activities

    @activities.setter
    def activities(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_Activity__activities", None)
        self.__activities = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Group"):
                    opp_val = getattr(item, "Group", None)
                    
                    if opp_val == self:
                        setattr(item, "Group", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Group"):
                    opp_val = getattr(item, "Group", None)
                    
                    setattr(item, "Group", self)
                    
