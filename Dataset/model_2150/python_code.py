from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ActivityType(Enum):
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
    GatewayDataBasedInclusive = "GatewayDataBasedInclusive"
    GatewayParallel = "GatewayParallel"
    GatewayComplex = "GatewayComplex"
class DirectionType(Enum):
    None = "None"
    To = "To"
    From = "From"
    Both = "Both"
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

    def __init__(self, ncname: str, documentation: str, name: str):
        self.ncname = ncname
        self.documentation = documentation
        self.name = name
        
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

class IdentifiableNode:

    pass
class bpmn_Vertex(IdentifiableNode):

    pass
class Artifact:

    pass
class bpmn_DataObject(Artifact):

    pass
class bpmn_TextAnnotation(Artifact):

    pass
class ArtifactsContainer:

    pass
class bpmn_Graph(IdentifiableNode, ArtifactsContainer):

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

    def __init__(self, direction: str, Association: "bpmn_Artifact" = None, associations: "bpmn_Artifact" = None, associations14: "bpmn_IdentifiableNode" = None, Association25: "bpmn_IdentifiableNode" = None):
        self.direction = direction
        self.Association = Association
        self.associations = associations
        self.associations14 = associations14
        self.Association25 = Association25
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

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
            if hasattr(old_value, "source8"):
                opp_val = getattr(old_value, "source8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source8"):
                opp_val = getattr(value, "source8", None)
                if opp_val is None:
                    setattr(value, "source8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "Artifact12"):
                opp_val = getattr(old_value, "Artifact12", None)
                if opp_val == self:
                    setattr(old_value, "Artifact12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Artifact12"):
                opp_val = getattr(value, "Artifact12", None)
                setattr(value, "Artifact12", self)

    @property
    def associations14(self):
        return self.__associations14

    @associations14.setter
    def associations14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_Association__associations14", None)
        self.__associations14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IdentifiableNode"):
                opp_val = getattr(old_value, "IdentifiableNode", None)
                if opp_val == self:
                    setattr(old_value, "IdentifiableNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IdentifiableNode"):
                opp_val = getattr(value, "IdentifiableNode", None)
                setattr(value, "IdentifiableNode", self)

    @property
    def Association25(self):
        return self.__Association25

    @Association25.setter
    def Association25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_Association__Association25", None)
        self.__Association25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "target24"):
                opp_val = getattr(old_value, "target24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "target24"):
                opp_val = getattr(value, "target24", None)
                if opp_val is None:
                    setattr(value, "target24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Identifiable:

    pass
class bpmn_IdentifiableNode(Identifiable):

    pass
class bpmn_BpmnDiagram(Identifiable, ArtifactsContainer):

    def __init__(self, author: str, title: str, bpmnDiagram: set["bpmn_Pool"] = None, bpmnDiagram17: set["bpmn_MessagingEdge"] = None, BpmnDiagram: "bpmn_MessagingEdge" = None, BpmnDiagram38: "bpmn_Pool" = None):
        self.author = author
        self.title = title
        self.bpmnDiagram = bpmnDiagram if bpmnDiagram is not None else set()
        self.bpmnDiagram17 = bpmnDiagram17 if bpmnDiagram17 is not None else set()
        self.BpmnDiagram = BpmnDiagram
        self.BpmnDiagram38 = BpmnDiagram38
        
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
    def bpmnDiagram17(self):
        return self.__bpmnDiagram17

    @bpmnDiagram17.setter
    def bpmnDiagram17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_BpmnDiagram__bpmnDiagram17", None)
        self.__bpmnDiagram17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessagingEdge18"):
                    opp_val = getattr(item, "MessagingEdge18", None)
                    
                    if opp_val == self:
                        setattr(item, "MessagingEdge18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessagingEdge18"):
                    opp_val = getattr(item, "MessagingEdge18", None)
                    
                    setattr(item, "MessagingEdge18", self)
                    

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
                    

class Vertex:

    pass
class bpmn_SubProcess(Activity, Graph):

    def __init__(self, isTransaction: str, SubProcess: "bpmn_Activity" = None, eventHandlerFor: set["bpmn_Activity"] = None):
        self.isTransaction = isTransaction
        self.SubProcess = SubProcess
        self.eventHandlerFor = eventHandlerFor if eventHandlerFor is not None else set()
        
    @property
    def isTransaction(self) -> str:
        return self.__isTransaction

    @isTransaction.setter
    def isTransaction(self, isTransaction: str):
        self.__isTransaction = isTransaction

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

class bpmn_Group(Artifact):

    pass
class NamedBpmnObject:

    pass
class bpmn_Artifact(Identifiable, NamedBpmnObject):

    pass
class bpmn_MessagingEdge(Identifiable, NamedBpmnObject):

    pass
class bpmn_Activity(NamedBpmnObject, Vertex):

    def __init__(self, orderedMessages: str, activityType: str, looping: str, target: set["bpmn_MessagingEdge"] = None, source: set["bpmn_MessagingEdge"] = None, activities: set["bpmn_Group"] = None, eventHandlers: "bpmn_SubProcess" = None, activities6: "bpmn_Lane" = None, Activity: "bpmn_Group" = None, Activity27: "bpmn_Lane" = None, Activity32: "bpmn_MessagingEdge" = None, Activity34: "bpmn_MessagingEdge" = None, Activity45: "bpmn_SubProcess" = None):
        self.orderedMessages = orderedMessages
        self.activityType = activityType
        self.looping = looping
        self.target = target if target is not None else set()
        self.source = source if source is not None else set()
        self.activities = activities if activities is not None else set()
        self.eventHandlers = eventHandlers
        self.activities6 = activities6
        self.Activity = Activity
        self.Activity27 = Activity27
        self.Activity32 = Activity32
        self.Activity34 = Activity34
        self.Activity45 = Activity45
        
    @property
    def activityType(self) -> str:
        return self.__activityType

    @activityType.setter
    def activityType(self, activityType: str):
        self.__activityType = activityType

    @property
    def orderedMessages(self) -> str:
        return self.__orderedMessages

    @orderedMessages.setter
    def orderedMessages(self, orderedMessages: str):
        self.__orderedMessages = orderedMessages

    @property
    def looping(self) -> str:
        return self.__looping

    @looping.setter
    def looping(self, looping: str):
        self.__looping = looping

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
    def activities6(self):
        return self.__activities6

    @activities6.setter
    def activities6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_Activity__activities6", None)
        self.__activities6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Lane"):
                opp_val = getattr(old_value, "Lane", None)
                if opp_val == self:
                    setattr(old_value, "Lane", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Lane"):
                opp_val = getattr(value, "Lane", None)
                setattr(value, "Lane", self)

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_Activity__source", None)
        self.__source = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MessagingEdge2"):
                    opp_val = getattr(item, "MessagingEdge2", None)
                    
                    if opp_val == self:
                        setattr(item, "MessagingEdge2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MessagingEdge2"):
                    opp_val = getattr(item, "MessagingEdge2", None)
                    
                    setattr(item, "MessagingEdge2", self)
                    

    @property
    def Activity27(self):
        return self.__Activity27

    @Activity27.setter
    def Activity27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_Activity__Activity27", None)
        self.__Activity27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lane"):
                opp_val = getattr(old_value, "lane", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lane"):
                opp_val = getattr(value, "lane", None)
                if opp_val is None:
                    setattr(value, "lane", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Activity34(self):
        return self.__Activity34

    @Activity34.setter
    def Activity34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_Activity__Activity34", None)
        self.__Activity34 = value
        
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
    def Activity32(self):
        return self.__Activity32

    @Activity32.setter
    def Activity32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_Activity__Activity32", None)
        self.__Activity32 = value
        
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
                    

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_Activity__target", None)
        self.__target = value if value is not None else set()
        
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
                    

class bpmn_Pool(NamedBpmnObject, Graph):

    pass
class bpmn_Lane(Identifiable, NamedBpmnObject):

    pass
class bpmn_ArtifactsContainer(NamedBpmnObject):

    pass
class bpmn_SequenceEdge(Identifiable, NamedBpmnObject):

    def __init__(self, conditionType: str, isDefault: str, SequenceEdge: "bpmn_Graph" = None, sequenceEdges: "bpmn_Graph" = None, outgoingEdges: "bpmn_Vertex" = None, incomingEdges: "bpmn_Vertex" = None, SequenceEdge48: "bpmn_Vertex" = None, SequenceEdge51: "bpmn_Vertex" = None):
        self.conditionType = conditionType
        self.isDefault = isDefault
        self.SequenceEdge = SequenceEdge
        self.sequenceEdges = sequenceEdges
        self.outgoingEdges = outgoingEdges
        self.incomingEdges = incomingEdges
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
    def SequenceEdge(self):
        return self.__SequenceEdge

    @SequenceEdge.setter
    def SequenceEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bpmn_SequenceEdge__SequenceEdge", None)
        self.__SequenceEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "graph21"):
                opp_val = getattr(old_value, "graph21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "graph21"):
                opp_val = getattr(value, "graph21", None)
                if opp_val is None:
                    setattr(value, "graph21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "Vertex41"):
                opp_val = getattr(old_value, "Vertex41", None)
                if opp_val == self:
                    setattr(old_value, "Vertex41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex41"):
                opp_val = getattr(value, "Vertex41", None)
                setattr(value, "Vertex41", self)

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
            if hasattr(old_value, "Vertex43"):
                opp_val = getattr(old_value, "Vertex43", None)
                if opp_val == self:
                    setattr(old_value, "Vertex43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Vertex43"):
                opp_val = getattr(value, "Vertex43", None)
                setattr(value, "Vertex43", self)

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
