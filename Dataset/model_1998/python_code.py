from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class trace_TraceLink:

    def __init__(self, overridden: bool, targetOf: set["trace_TargetElement"] = None, links: "trace_TracedRule" = None, appliedAt: set["trace_TraceProperty"] = None, TraceLink19: "trace_SourceElement" = None, TraceLink: "trace_TracedRule" = None, sourceOf: set["trace_SourceElement"] = None, TraceLink41: "trace_TraceProperty" = None, TraceLink27: "trace_TargetElement" = None):
        self.overridden = overridden
        self.targetOf = targetOf if targetOf is not None else set()
        self.links = links
        self.appliedAt = appliedAt if appliedAt is not None else set()
        self.TraceLink19 = TraceLink19
        self.TraceLink = TraceLink
        self.sourceOf = sourceOf if sourceOf is not None else set()
        self.TraceLink41 = TraceLink41
        self.TraceLink27 = TraceLink27
        
    @property
    def overridden(self) -> bool:
        return self.__overridden

    @overridden.setter
    def overridden(self, overridden: bool):
        self.__overridden = overridden

    @property
    def TraceLink41(self):
        return self.__TraceLink41

    @TraceLink41.setter
    def TraceLink41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLink__TraceLink41", None)
        self.__TraceLink41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "properties"):
                opp_val = getattr(old_value, "properties", None)
                if opp_val == self:
                    setattr(old_value, "properties", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "properties"):
                opp_val = getattr(value, "properties", None)
                setattr(value, "properties", self)

    @property
    def appliedAt(self):
        return self.__appliedAt

    @appliedAt.setter
    def appliedAt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLink__appliedAt", None)
        self.__appliedAt = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TraceProperty"):
                    opp_val = getattr(item, "TraceProperty", None)
                    
                    if opp_val == self:
                        setattr(item, "TraceProperty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TraceProperty"):
                    opp_val = getattr(item, "TraceProperty", None)
                    
                    setattr(item, "TraceProperty", self)
                    

    @property
    def TraceLink27(self):
        return self.__TraceLink27

    @TraceLink27.setter
    def TraceLink27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLink__TraceLink27", None)
        self.__TraceLink27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "targetElements"):
                opp_val = getattr(old_value, "targetElements", None)
                if opp_val == self:
                    setattr(old_value, "targetElements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "targetElements"):
                opp_val = getattr(value, "targetElements", None)
                setattr(value, "targetElements", self)

    @property
    def links(self):
        return self.__links

    @links.setter
    def links(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLink__links", None)
        self.__links = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TracedRule15"):
                opp_val = getattr(old_value, "TracedRule15", None)
                if opp_val == self:
                    setattr(old_value, "TracedRule15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TracedRule15"):
                opp_val = getattr(value, "TracedRule15", None)
                setattr(value, "TracedRule15", self)

    @property
    def TraceLink(self):
        return self.__TraceLink

    @TraceLink.setter
    def TraceLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLink__TraceLink", None)
        self.__TraceLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rule"):
                opp_val = getattr(old_value, "rule", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rule"):
                opp_val = getattr(value, "rule", None)
                if opp_val is None:
                    setattr(value, "rule", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def targetOf(self):
        return self.__targetOf

    @targetOf.setter
    def targetOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLink__targetOf", None)
        self.__targetOf = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TargetElement"):
                    opp_val = getattr(item, "TargetElement", None)
                    
                    if opp_val == self:
                        setattr(item, "TargetElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TargetElement"):
                    opp_val = getattr(item, "TargetElement", None)
                    
                    setattr(item, "TargetElement", self)
                    

    @property
    def sourceOf(self):
        return self.__sourceOf

    @sourceOf.setter
    def sourceOf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLink__sourceOf", None)
        self.__sourceOf = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SourceElement12"):
                    opp_val = getattr(item, "SourceElement12", None)
                    
                    if opp_val == self:
                        setattr(item, "SourceElement12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SourceElement12"):
                    opp_val = getattr(item, "SourceElement12", None)
                    
                    setattr(item, "SourceElement12", self)
                    

    @property
    def TraceLink19(self):
        return self.__TraceLink19

    @TraceLink19.setter
    def TraceLink19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLink__TraceLink19", None)
        self.__TraceLink19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceElements"):
                opp_val = getattr(old_value, "sourceElements", None)
                if opp_val == self:
                    setattr(old_value, "sourceElements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceElements"):
                opp_val = getattr(value, "sourceElements", None)
                setattr(value, "sourceElements", self)

    def getSourceElement(self, name: str, create: bool) -> str:
        # TODO: Implement getSourceElement method
        pass

    def getTargetElement(self, name: str) -> str:
        # TODO: Implement getTargetElement method
        pass

class trace_SourceElementList:

    def __init__(self, SourceElementList: "trace_TraceLinkSet" = None, SourceElementList10: "trace_TracedRule" = None, trace_SourceElementList: set["trace_SourceElement"] = None, defaultSourceElementLists: "trace_TraceLinkSet" = None, uniqueSourceElementLists: "trace_TracedRule" = None):
        self.SourceElementList = SourceElementList
        self.SourceElementList10 = SourceElementList10
        self.trace_SourceElementList = trace_SourceElementList if trace_SourceElementList is not None else set()
        self.defaultSourceElementLists = defaultSourceElementLists
        self.uniqueSourceElementLists = uniqueSourceElementLists
        
    @property
    def SourceElementList10(self):
        return self.__SourceElementList10

    @SourceElementList10.setter
    def SourceElementList10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_SourceElementList__SourceElementList10", None)
        self.__SourceElementList10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uniqueFor9"):
                opp_val = getattr(old_value, "uniqueFor9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uniqueFor9"):
                opp_val = getattr(value, "uniqueFor9", None)
                if opp_val is None:
                    setattr(value, "uniqueFor9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trace_SourceElementList(self):
        return self.__trace_SourceElementList

    @trace_SourceElementList.setter
    def trace_SourceElementList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_SourceElementList__trace_SourceElementList", None)
        self.__trace_SourceElementList = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_SourceElement"):
                    opp_val = getattr(item, "trace_SourceElement", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_SourceElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_SourceElement"):
                    opp_val = getattr(item, "trace_SourceElement", None)
                    
                    setattr(item, "trace_SourceElement", self)
                    

    @property
    def uniqueSourceElementLists(self):
        return self.__uniqueSourceElementLists

    @uniqueSourceElementLists.setter
    def uniqueSourceElementLists(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_SourceElementList__uniqueSourceElementLists", None)
        self.__uniqueSourceElementLists = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TracedRule35"):
                opp_val = getattr(old_value, "TracedRule35", None)
                if opp_val == self:
                    setattr(old_value, "TracedRule35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TracedRule35"):
                opp_val = getattr(value, "TracedRule35", None)
                setattr(value, "TracedRule35", self)

    @property
    def SourceElementList(self):
        return self.__SourceElementList

    @SourceElementList.setter
    def SourceElementList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_SourceElementList__SourceElementList", None)
        self.__SourceElementList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "defaultFor3"):
                opp_val = getattr(old_value, "defaultFor3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "defaultFor3"):
                opp_val = getattr(value, "defaultFor3", None)
                if opp_val is None:
                    setattr(value, "defaultFor3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def defaultSourceElementLists(self):
        return self.__defaultSourceElementLists

    @defaultSourceElementLists.setter
    def defaultSourceElementLists(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_SourceElementList__defaultSourceElementLists", None)
        self.__defaultSourceElementLists = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TraceLinkSet33"):
                opp_val = getattr(old_value, "TraceLinkSet33", None)
                if opp_val == self:
                    setattr(old_value, "TraceLinkSet33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TraceLinkSet33"):
                opp_val = getattr(value, "TraceLinkSet33", None)
                setattr(value, "TraceLinkSet33", self)

    def getSourceObjects(self) -> str:
        # TODO: Implement getSourceObjects method
        pass

class TraceElement:

    pass
class trace_EObject:

    pass
class trace_TraceElement(ABC):

    def __init__(self, name: str, runtimeObject: str, trace_TraceElement: "trace_EObject" = None):
        self.name = name
        self.runtimeObject = runtimeObject
        self.trace_TraceElement = trace_TraceElement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def runtimeObject(self) -> str:
        return self.__runtimeObject

    @runtimeObject.setter
    def runtimeObject(self, runtimeObject: str):
        self.__runtimeObject = runtimeObject

    @property
    def trace_TraceElement(self):
        return self.__trace_TraceElement

    @trace_TraceElement.setter
    def trace_TraceElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceElement__trace_TraceElement", None)
        self.__trace_TraceElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_EObject"):
                opp_val = getattr(old_value, "trace_EObject", None)
                if opp_val == self:
                    setattr(old_value, "trace_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_EObject"):
                opp_val = getattr(value, "trace_EObject", None)
                setattr(value, "trace_EObject", self)

class trace_TraceProperty:

    def __init__(self, propertyName: str, resolved: bool, TraceProperty: "trace_TraceLink" = None, trace_TraceProperty: "trace_TargetElement" = None, trace_TraceProperty38: set["trace_EObject"] = None, properties: "trace_TraceLink" = None):
        self.propertyName = propertyName
        self.resolved = resolved
        self.TraceProperty = TraceProperty
        self.trace_TraceProperty = trace_TraceProperty
        self.trace_TraceProperty38 = trace_TraceProperty38 if trace_TraceProperty38 is not None else set()
        self.properties = properties
        
    @property
    def resolved(self) -> bool:
        return self.__resolved

    @resolved.setter
    def resolved(self, resolved: bool):
        self.__resolved = resolved

    @property
    def propertyName(self) -> str:
        return self.__propertyName

    @propertyName.setter
    def propertyName(self, propertyName: str):
        self.__propertyName = propertyName

    @property
    def properties(self):
        return self.__properties

    @properties.setter
    def properties(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceProperty__properties", None)
        self.__properties = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TraceLink41"):
                opp_val = getattr(old_value, "TraceLink41", None)
                if opp_val == self:
                    setattr(old_value, "TraceLink41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TraceLink41"):
                opp_val = getattr(value, "TraceLink41", None)
                setattr(value, "TraceLink41", self)

    @property
    def trace_TraceProperty(self):
        return self.__trace_TraceProperty

    @trace_TraceProperty.setter
    def trace_TraceProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceProperty__trace_TraceProperty", None)
        self.__trace_TraceProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_TargetElement"):
                opp_val = getattr(old_value, "trace_TargetElement", None)
                if opp_val == self:
                    setattr(old_value, "trace_TargetElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_TargetElement"):
                opp_val = getattr(value, "trace_TargetElement", None)
                setattr(value, "trace_TargetElement", self)

    @property
    def trace_TraceProperty38(self):
        return self.__trace_TraceProperty38

    @trace_TraceProperty38.setter
    def trace_TraceProperty38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceProperty__trace_TraceProperty38", None)
        self.__trace_TraceProperty38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_EObject39"):
                    opp_val = getattr(item, "trace_EObject39", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_EObject39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_EObject39"):
                    opp_val = getattr(item, "trace_EObject39", None)
                    
                    setattr(item, "trace_EObject39", self)
                    

    @property
    def TraceProperty(self):
        return self.__TraceProperty

    @TraceProperty.setter
    def TraceProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceProperty__TraceProperty", None)
        self.__TraceProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appliedAt"):
                opp_val = getattr(old_value, "appliedAt", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appliedAt"):
                opp_val = getattr(value, "appliedAt", None)
                if opp_val is None:
                    setattr(value, "appliedAt", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def resolveBinding(self, traces: str):
        # TODO: Implement resolveBinding method
        pass

class trace_TargetElement(TraceElement):

    pass
class trace_SourceElement(TraceElement):

    def __init__(self, mapsToSelf: bool, SourceElement: "trace_TraceLinkSet" = None, sourceElements: "trace_TraceLink" = None, mapsTo: set["trace_TargetElement"] = None, defaultSourceElements: "trace_TraceLinkSet" = None, uniqueSourceElements: "trace_TracedRule" = None, SourceElement7: "trace_TracedRule" = None, SourceElement12: "trace_TraceLink" = None, SourceElement30: "trace_TargetElement" = None, trace_SourceElement: "trace_SourceElementList" = None):
        self.mapsToSelf = mapsToSelf
        self.SourceElement = SourceElement
        self.sourceElements = sourceElements
        self.mapsTo = mapsTo if mapsTo is not None else set()
        self.defaultSourceElements = defaultSourceElements
        self.uniqueSourceElements = uniqueSourceElements
        self.SourceElement7 = SourceElement7
        self.SourceElement12 = SourceElement12
        self.SourceElement30 = SourceElement30
        self.trace_SourceElement = trace_SourceElement
        
    @property
    def mapsToSelf(self) -> bool:
        return self.__mapsToSelf

    @mapsToSelf.setter
    def mapsToSelf(self, mapsToSelf: bool):
        self.__mapsToSelf = mapsToSelf

    @property
    def SourceElement(self):
        return self.__SourceElement

    @SourceElement.setter
    def SourceElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_SourceElement__SourceElement", None)
        self.__SourceElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "defaultFor"):
                opp_val = getattr(old_value, "defaultFor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "defaultFor"):
                opp_val = getattr(value, "defaultFor", None)
                if opp_val is None:
                    setattr(value, "defaultFor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trace_SourceElement(self):
        return self.__trace_SourceElement

    @trace_SourceElement.setter
    def trace_SourceElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_SourceElement__trace_SourceElement", None)
        self.__trace_SourceElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_SourceElementList"):
                opp_val = getattr(old_value, "trace_SourceElementList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_SourceElementList"):
                opp_val = getattr(value, "trace_SourceElementList", None)
                if opp_val is None:
                    setattr(value, "trace_SourceElementList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SourceElement12(self):
        return self.__SourceElement12

    @SourceElement12.setter
    def SourceElement12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_SourceElement__SourceElement12", None)
        self.__SourceElement12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sourceOf"):
                opp_val = getattr(old_value, "sourceOf", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sourceOf"):
                opp_val = getattr(value, "sourceOf", None)
                if opp_val is None:
                    setattr(value, "sourceOf", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def uniqueSourceElements(self):
        return self.__uniqueSourceElements

    @uniqueSourceElements.setter
    def uniqueSourceElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_SourceElement__uniqueSourceElements", None)
        self.__uniqueSourceElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TracedRule25"):
                opp_val = getattr(old_value, "TracedRule25", None)
                if opp_val == self:
                    setattr(old_value, "TracedRule25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TracedRule25"):
                opp_val = getattr(value, "TracedRule25", None)
                setattr(value, "TracedRule25", self)

    @property
    def defaultSourceElements(self):
        return self.__defaultSourceElements

    @defaultSourceElements.setter
    def defaultSourceElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_SourceElement__defaultSourceElements", None)
        self.__defaultSourceElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TraceLinkSet23"):
                opp_val = getattr(old_value, "TraceLinkSet23", None)
                if opp_val == self:
                    setattr(old_value, "TraceLinkSet23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TraceLinkSet23"):
                opp_val = getattr(value, "TraceLinkSet23", None)
                setattr(value, "TraceLinkSet23", self)

    @property
    def mapsTo(self):
        return self.__mapsTo

    @mapsTo.setter
    def mapsTo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_SourceElement__mapsTo", None)
        self.__mapsTo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TargetElement21"):
                    opp_val = getattr(item, "TargetElement21", None)
                    
                    if opp_val == self:
                        setattr(item, "TargetElement21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TargetElement21"):
                    opp_val = getattr(item, "TargetElement21", None)
                    
                    setattr(item, "TargetElement21", self)
                    

    @property
    def SourceElement7(self):
        return self.__SourceElement7

    @SourceElement7.setter
    def SourceElement7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_SourceElement__SourceElement7", None)
        self.__SourceElement7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uniqueFor"):
                opp_val = getattr(old_value, "uniqueFor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uniqueFor"):
                opp_val = getattr(value, "uniqueFor", None)
                if opp_val is None:
                    setattr(value, "uniqueFor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def sourceElements(self):
        return self.__sourceElements

    @sourceElements.setter
    def sourceElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_SourceElement__sourceElements", None)
        self.__sourceElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TraceLink19"):
                opp_val = getattr(old_value, "TraceLink19", None)
                if opp_val == self:
                    setattr(old_value, "TraceLink19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TraceLink19"):
                opp_val = getattr(value, "TraceLink19", None)
                setattr(value, "TraceLink19", self)

    @property
    def SourceElement30(self):
        return self.__SourceElement30

    @SourceElement30.setter
    def SourceElement30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_SourceElement__SourceElement30", None)
        self.__SourceElement30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mapsTo29"):
                opp_val = getattr(old_value, "mapsTo29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mapsTo29"):
                opp_val = getattr(value, "mapsTo29", None)
                if opp_val is None:
                    setattr(value, "mapsTo29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class trace_TracedRule:

    def __init__(self, rule: str, TracedRule: "trace_TraceLinkSet" = None, TracedRule15: "trace_TraceLink" = None, TracedRule25: "trace_SourceElement" = None, rule: set["trace_TraceLink"] = None, rules: "trace_TraceLinkSet" = None, uniqueFor: set["trace_SourceElement"] = None, uniqueFor9: set["trace_SourceElementList"] = None, TracedRule35: "trace_SourceElementList" = None):
        self.rule = rule
        self.TracedRule = TracedRule
        self.TracedRule15 = TracedRule15
        self.TracedRule25 = TracedRule25
        self.rule = rule if rule is not None else set()
        self.rules = rules
        self.uniqueFor = uniqueFor if uniqueFor is not None else set()
        self.uniqueFor9 = uniqueFor9 if uniqueFor9 is not None else set()
        self.TracedRule35 = TracedRule35
        
    @property
    def rule(self) -> str:
        return self.__rule

    @rule.setter
    def rule(self, rule: str):
        self.__rule = rule

    @property
    def rules(self):
        return self.__rules

    @rules.setter
    def rules(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TracedRule__rules", None)
        self.__rules = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TraceLinkSet"):
                opp_val = getattr(old_value, "TraceLinkSet", None)
                if opp_val == self:
                    setattr(old_value, "TraceLinkSet", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TraceLinkSet"):
                opp_val = getattr(value, "TraceLinkSet", None)
                setattr(value, "TraceLinkSet", self)

    @property
    def uniqueFor(self):
        return self.__uniqueFor

    @uniqueFor.setter
    def uniqueFor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TracedRule__uniqueFor", None)
        self.__uniqueFor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SourceElement7"):
                    opp_val = getattr(item, "SourceElement7", None)
                    
                    if opp_val == self:
                        setattr(item, "SourceElement7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SourceElement7"):
                    opp_val = getattr(item, "SourceElement7", None)
                    
                    setattr(item, "SourceElement7", self)
                    

    @property
    def TracedRule15(self):
        return self.__TracedRule15

    @TracedRule15.setter
    def TracedRule15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TracedRule__TracedRule15", None)
        self.__TracedRule15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "links"):
                opp_val = getattr(old_value, "links", None)
                if opp_val == self:
                    setattr(old_value, "links", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "links"):
                opp_val = getattr(value, "links", None)
                setattr(value, "links", self)

    @property
    def TracedRule25(self):
        return self.__TracedRule25

    @TracedRule25.setter
    def TracedRule25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TracedRule__TracedRule25", None)
        self.__TracedRule25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uniqueSourceElements"):
                opp_val = getattr(old_value, "uniqueSourceElements", None)
                if opp_val == self:
                    setattr(old_value, "uniqueSourceElements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uniqueSourceElements"):
                opp_val = getattr(value, "uniqueSourceElements", None)
                setattr(value, "uniqueSourceElements", self)

    @property
    def uniqueFor9(self):
        return self.__uniqueFor9

    @uniqueFor9.setter
    def uniqueFor9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TracedRule__uniqueFor9", None)
        self.__uniqueFor9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SourceElementList10"):
                    opp_val = getattr(item, "SourceElementList10", None)
                    
                    if opp_val == self:
                        setattr(item, "SourceElementList10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SourceElementList10"):
                    opp_val = getattr(item, "SourceElementList10", None)
                    
                    setattr(item, "SourceElementList10", self)
                    

    @property
    def TracedRule(self):
        return self.__TracedRule

    @TracedRule.setter
    def TracedRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TracedRule__TracedRule", None)
        self.__TracedRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "linkSet"):
                opp_val = getattr(old_value, "linkSet", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "linkSet"):
                opp_val = getattr(value, "linkSet", None)
                if opp_val is None:
                    setattr(value, "linkSet", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def TracedRule35(self):
        return self.__TracedRule35

    @TracedRule35.setter
    def TracedRule35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TracedRule__TracedRule35", None)
        self.__TracedRule35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "uniqueSourceElementLists"):
                opp_val = getattr(old_value, "uniqueSourceElementLists", None)
                if opp_val == self:
                    setattr(old_value, "uniqueSourceElementLists", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "uniqueSourceElementLists"):
                opp_val = getattr(value, "uniqueSourceElementLists", None)
                setattr(value, "uniqueSourceElementLists", self)

    @property
    def rule(self):
        return self.__rule

    @rule.setter
    def rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TracedRule__rule", None)
        self.__rule = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TraceLink"):
                    opp_val = getattr(item, "TraceLink", None)
                    
                    if opp_val == self:
                        setattr(item, "TraceLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TraceLink"):
                    opp_val = getattr(item, "TraceLink", None)
                    
                    setattr(item, "TraceLink", self)
                    

    def getUniqueSourceElements(self, sourceElements: str) -> str:
        # TODO: Implement getUniqueSourceElements method
        pass

    def getUniqueSourceElement(self, sourceElement: str) -> str:
        # TODO: Implement getUniqueSourceElement method
        pass

class trace_TraceLinkSet:

    def __init__(self, linkSet: set["trace_TracedRule"] = None, defaultFor: set["trace_SourceElement"] = None, TraceLinkSet23: "trace_SourceElement" = None, defaultFor3: set["trace_SourceElementList"] = None, TraceLinkSet: "trace_TracedRule" = None, TraceLinkSet33: "trace_SourceElementList" = None):
        self.linkSet = linkSet if linkSet is not None else set()
        self.defaultFor = defaultFor if defaultFor is not None else set()
        self.TraceLinkSet23 = TraceLinkSet23
        self.defaultFor3 = defaultFor3 if defaultFor3 is not None else set()
        self.TraceLinkSet = TraceLinkSet
        self.TraceLinkSet33 = TraceLinkSet33
        
    @property
    def defaultFor3(self):
        return self.__defaultFor3

    @defaultFor3.setter
    def defaultFor3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLinkSet__defaultFor3", None)
        self.__defaultFor3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SourceElementList"):
                    opp_val = getattr(item, "SourceElementList", None)
                    
                    if opp_val == self:
                        setattr(item, "SourceElementList", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SourceElementList"):
                    opp_val = getattr(item, "SourceElementList", None)
                    
                    setattr(item, "SourceElementList", self)
                    

    @property
    def defaultFor(self):
        return self.__defaultFor

    @defaultFor.setter
    def defaultFor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLinkSet__defaultFor", None)
        self.__defaultFor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SourceElement"):
                    opp_val = getattr(item, "SourceElement", None)
                    
                    if opp_val == self:
                        setattr(item, "SourceElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SourceElement"):
                    opp_val = getattr(item, "SourceElement", None)
                    
                    setattr(item, "SourceElement", self)
                    

    @property
    def linkSet(self):
        return self.__linkSet

    @linkSet.setter
    def linkSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLinkSet__linkSet", None)
        self.__linkSet = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TracedRule"):
                    opp_val = getattr(item, "TracedRule", None)
                    
                    if opp_val == self:
                        setattr(item, "TracedRule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TracedRule"):
                    opp_val = getattr(item, "TracedRule", None)
                    
                    setattr(item, "TracedRule", self)
                    

    @property
    def TraceLinkSet23(self):
        return self.__TraceLinkSet23

    @TraceLinkSet23.setter
    def TraceLinkSet23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLinkSet__TraceLinkSet23", None)
        self.__TraceLinkSet23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "defaultSourceElements"):
                opp_val = getattr(old_value, "defaultSourceElements", None)
                if opp_val == self:
                    setattr(old_value, "defaultSourceElements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "defaultSourceElements"):
                opp_val = getattr(value, "defaultSourceElements", None)
                setattr(value, "defaultSourceElements", self)

    @property
    def TraceLinkSet(self):
        return self.__TraceLinkSet

    @TraceLinkSet.setter
    def TraceLinkSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLinkSet__TraceLinkSet", None)
        self.__TraceLinkSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rules"):
                opp_val = getattr(old_value, "rules", None)
                if opp_val == self:
                    setattr(old_value, "rules", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rules"):
                opp_val = getattr(value, "rules", None)
                setattr(value, "rules", self)

    @property
    def TraceLinkSet33(self):
        return self.__TraceLinkSet33

    @TraceLinkSet33.setter
    def TraceLinkSet33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLinkSet__TraceLinkSet33", None)
        self.__TraceLinkSet33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "defaultSourceElementLists"):
                opp_val = getattr(old_value, "defaultSourceElementLists", None)
                if opp_val == self:
                    setattr(old_value, "defaultSourceElementLists", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "defaultSourceElementLists"):
                opp_val = getattr(value, "defaultSourceElementLists", None)
                setattr(value, "defaultSourceElementLists", self)

    def getLinksByRule(self, rule: str, create: bool) -> str:
        # TODO: Implement getLinksByRule method
        pass

    def getDefaultSourceElement(self, sourceElement: str) -> str:
        # TODO: Implement getDefaultSourceElement method
        pass

    def clear(self):
        # TODO: Implement clear method
        pass

    def getDefaultSourceElements(self, sourceElements: str) -> str:
        # TODO: Implement getDefaultSourceElements method
        pass
