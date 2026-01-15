from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

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
    def runtimeObject(self) -> str:
        return self.__runtimeObject

    @runtimeObject.setter
    def runtimeObject(self, runtimeObject: str):
        self.__runtimeObject = runtimeObject

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

class trace_TargetElement(TraceElement):

    pass
class trace_TraceLinkSet:

    def __init__(self, linkSet: set["trace_TracedRule"] = None, defaultFor: set["trace_SourceElement"] = None, defaultFor3: set["trace_SourceElementList"] = None, TraceLinkSet: "trace_TracedRule" = None, TraceLinkSet22: "trace_SourceElement" = None, TraceLinkSet32: "trace_SourceElementList" = None):
        self.linkSet = linkSet if linkSet is not None else set()
        self.defaultFor = defaultFor if defaultFor is not None else set()
        self.defaultFor3 = defaultFor3 if defaultFor3 is not None else set()
        self.TraceLinkSet = TraceLinkSet
        self.TraceLinkSet22 = TraceLinkSet22
        self.TraceLinkSet32 = TraceLinkSet32
        
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
    def TraceLinkSet32(self):
        return self.__TraceLinkSet32

    @TraceLinkSet32.setter
    def TraceLinkSet32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLinkSet__TraceLinkSet32", None)
        self.__TraceLinkSet32 = value
        
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
    def TraceLinkSet22(self):
        return self.__TraceLinkSet22

    @TraceLinkSet22.setter
    def TraceLinkSet22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLinkSet__TraceLinkSet22", None)
        self.__TraceLinkSet22 = value
        
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

    def getLinksByRule(self, rule: str, create: bool) -> str:
        # TODO: Implement getLinksByRule method
        pass

    def getDefaultSourceElements(self, sourceElements: str) -> str:
        # TODO: Implement getDefaultSourceElements method
        pass

    def getDefaultSourceElement(self, sourceElement: str) -> str:
        # TODO: Implement getDefaultSourceElement method
        pass

    def clear(self):
        # TODO: Implement clear method
        pass

class trace_TraceLink:

    def __init__(self, overridden: bool, TraceLink: "trace_TracedRule" = None, sourceOf: set["trace_SourceElement"] = None, TraceLink18: "trace_SourceElement" = None, TraceLink26: "trace_TargetElement" = None, targetOf: set["trace_TargetElement"] = None, links: "trace_TracedRule" = None):
        self.overridden = overridden
        self.TraceLink = TraceLink
        self.sourceOf = sourceOf if sourceOf is not None else set()
        self.TraceLink18 = TraceLink18
        self.TraceLink26 = TraceLink26
        self.targetOf = targetOf if targetOf is not None else set()
        self.links = links
        
    @property
    def overridden(self) -> bool:
        return self.__overridden

    @overridden.setter
    def overridden(self, overridden: bool):
        self.__overridden = overridden

    @property
    def TraceLink18(self):
        return self.__TraceLink18

    @TraceLink18.setter
    def TraceLink18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLink__TraceLink18", None)
        self.__TraceLink18 = value
        
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

    @property
    def TraceLink26(self):
        return self.__TraceLink26

    @TraceLink26.setter
    def TraceLink26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLink__TraceLink26", None)
        self.__TraceLink26 = value
        
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

    def getTargetElement(self, name: str) -> str:
        # TODO: Implement getTargetElement method
        pass

    def getSourceElement(self, create: bool, name: str) -> str:
        # TODO: Implement getSourceElement method
        pass

class trace_SourceElementList:

    def __init__(self, SourceElementList: "trace_TraceLinkSet" = None, SourceElementList10: "trace_TracedRule" = None, trace_SourceElementList: set["trace_SourceElement"] = None, defaultSourceElementLists: "trace_TraceLinkSet" = None, uniqueSourceElementLists: "trace_TracedRule" = None):
        self.SourceElementList = SourceElementList
        self.SourceElementList10 = SourceElementList10
        self.trace_SourceElementList = trace_SourceElementList if trace_SourceElementList is not None else set()
        self.defaultSourceElementLists = defaultSourceElementLists
        self.uniqueSourceElementLists = uniqueSourceElementLists
        
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
            if hasattr(old_value, "TracedRule34"):
                opp_val = getattr(old_value, "TracedRule34", None)
                if opp_val == self:
                    setattr(old_value, "TracedRule34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TracedRule34"):
                opp_val = getattr(value, "TracedRule34", None)
                setattr(value, "TracedRule34", self)

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
            if hasattr(old_value, "TraceLinkSet32"):
                opp_val = getattr(old_value, "TraceLinkSet32", None)
                if opp_val == self:
                    setattr(old_value, "TraceLinkSet32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TraceLinkSet32"):
                opp_val = getattr(value, "TraceLinkSet32", None)
                setattr(value, "TraceLinkSet32", self)

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
                    

    def getSourceObjects(self) -> str:
        # TODO: Implement getSourceObjects method
        pass

class trace_SourceElement(TraceElement):

    def __init__(self, mapsToSelf: bool, SourceElement: "trace_TraceLinkSet" = None, SourceElement7: "trace_TracedRule" = None, SourceElement12: "trace_TraceLink" = None, sourceElements: "trace_TraceLink" = None, mapsTo: set["trace_TargetElement"] = None, defaultSourceElements: "trace_TraceLinkSet" = None, uniqueSourceElements: "trace_TracedRule" = None, SourceElement29: "trace_TargetElement" = None, trace_SourceElement: "trace_SourceElementList" = None):
        self.mapsToSelf = mapsToSelf
        self.SourceElement = SourceElement
        self.SourceElement7 = SourceElement7
        self.SourceElement12 = SourceElement12
        self.sourceElements = sourceElements
        self.mapsTo = mapsTo if mapsTo is not None else set()
        self.defaultSourceElements = defaultSourceElements
        self.uniqueSourceElements = uniqueSourceElements
        self.SourceElement29 = SourceElement29
        self.trace_SourceElement = trace_SourceElement
        
    @property
    def mapsToSelf(self) -> bool:
        return self.__mapsToSelf

    @mapsToSelf.setter
    def mapsToSelf(self, mapsToSelf: bool):
        self.__mapsToSelf = mapsToSelf

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
                if hasattr(item, "TargetElement20"):
                    opp_val = getattr(item, "TargetElement20", None)
                    
                    if opp_val == self:
                        setattr(item, "TargetElement20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TargetElement20"):
                    opp_val = getattr(item, "TargetElement20", None)
                    
                    setattr(item, "TargetElement20", self)
                    

    @property
    def SourceElement29(self):
        return self.__SourceElement29

    @SourceElement29.setter
    def SourceElement29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_SourceElement__SourceElement29", None)
        self.__SourceElement29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mapsTo28"):
                opp_val = getattr(old_value, "mapsTo28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mapsTo28"):
                opp_val = getattr(value, "mapsTo28", None)
                if opp_val is None:
                    setattr(value, "mapsTo28", set([self]))
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
            if hasattr(old_value, "TraceLink18"):
                opp_val = getattr(old_value, "TraceLink18", None)
                if opp_val == self:
                    setattr(old_value, "TraceLink18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TraceLink18"):
                opp_val = getattr(value, "TraceLink18", None)
                setattr(value, "TraceLink18", self)

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
            if hasattr(old_value, "TracedRule24"):
                opp_val = getattr(old_value, "TracedRule24", None)
                if opp_val == self:
                    setattr(old_value, "TracedRule24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TracedRule24"):
                opp_val = getattr(value, "TracedRule24", None)
                setattr(value, "TracedRule24", self)

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
    def defaultSourceElements(self):
        return self.__defaultSourceElements

    @defaultSourceElements.setter
    def defaultSourceElements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_SourceElement__defaultSourceElements", None)
        self.__defaultSourceElements = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TraceLinkSet22"):
                opp_val = getattr(old_value, "TraceLinkSet22", None)
                if opp_val == self:
                    setattr(old_value, "TraceLinkSet22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TraceLinkSet22"):
                opp_val = getattr(value, "TraceLinkSet22", None)
                setattr(value, "TraceLinkSet22", self)

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

class trace_TracedRule:

    def __init__(self, rule: str, TracedRule: "trace_TraceLinkSet" = None, rule: set["trace_TraceLink"] = None, rules: "trace_TraceLinkSet" = None, uniqueFor: set["trace_SourceElement"] = None, uniqueFor9: set["trace_SourceElementList"] = None, TracedRule24: "trace_SourceElement" = None, TracedRule34: "trace_SourceElementList" = None, TracedRule15: "trace_TraceLink" = None):
        self.rule = rule
        self.TracedRule = TracedRule
        self.rule = rule if rule is not None else set()
        self.rules = rules
        self.uniqueFor = uniqueFor if uniqueFor is not None else set()
        self.uniqueFor9 = uniqueFor9 if uniqueFor9 is not None else set()
        self.TracedRule24 = TracedRule24
        self.TracedRule34 = TracedRule34
        self.TracedRule15 = TracedRule15
        
    @property
    def rule(self) -> str:
        return self.__rule

    @rule.setter
    def rule(self, rule: str):
        self.__rule = rule

    @property
    def TracedRule24(self):
        return self.__TracedRule24

    @TracedRule24.setter
    def TracedRule24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TracedRule__TracedRule24", None)
        self.__TracedRule24 = value
        
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
    def TracedRule34(self):
        return self.__TracedRule34

    @TracedRule34.setter
    def TracedRule34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TracedRule__TracedRule34", None)
        self.__TracedRule34 = value
        
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

    def getUniqueSourceElements(self, sourceElements: str) -> str:
        # TODO: Implement getUniqueSourceElements method
        pass

    def getUniqueSourceElement(self, sourceElement: str) -> str:
        # TODO: Implement getUniqueSourceElement method
        pass
