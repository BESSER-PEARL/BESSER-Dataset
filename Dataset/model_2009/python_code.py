from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class trace_TraceElement(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class TraceElement:

    pass
class trace_Trace(TraceElement):

    pass
class trace_ModuleElement(TraceElement):

    def __init__(self, module_id: str, ModuleElement: "trace_ExecutionContext" = None, for: set["trace_ExecutionContext"] = None, traces: set["trace_Trace"] = None, ModuleElement11: "trace_Trace" = None):
        self.module_id = module_id
        self.ModuleElement = ModuleElement
        self.for = for if for is not None else set()
        self.traces = traces if traces is not None else set()
        self.ModuleElement11 = ModuleElement11
        
    @property
    def module_id(self) -> str:
        return self.__module_id

    @module_id.setter
    def module_id(self, module_id: str):
        self.__module_id = module_id

    @property
    def ModuleElement(self):
        return self.__ModuleElement

    @ModuleElement.setter
    def ModuleElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ModuleElement__ModuleElement", None)
        self.__ModuleElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executionContexts"):
                opp_val = getattr(old_value, "executionContexts", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executionContexts"):
                opp_val = getattr(value, "executionContexts", None)
                if opp_val is None:
                    setattr(value, "executionContexts", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ModuleElement11(self):
        return self.__ModuleElement11

    @ModuleElement11.setter
    def ModuleElement11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ModuleElement__ModuleElement11", None)
        self.__ModuleElement11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces10"):
                opp_val = getattr(old_value, "traces10", None)
                if opp_val == self:
                    setattr(old_value, "traces10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces10"):
                opp_val = getattr(value, "traces10", None)
                setattr(value, "traces10", self)

    @property
    def for(self):
        return self.__for

    @for.setter
    def for(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ModuleElement__for", None)
        self.__for = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExecutionContext"):
                    opp_val = getattr(item, "ExecutionContext", None)
                    
                    if opp_val == self:
                        setattr(item, "ExecutionContext", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExecutionContext"):
                    opp_val = getattr(item, "ExecutionContext", None)
                    
                    setattr(item, "ExecutionContext", self)
                    

    @property
    def traces(self):
        return self.__traces

    @traces.setter
    def traces(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ModuleElement__traces", None)
        self.__traces = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Trace6"):
                    opp_val = getattr(item, "Trace6", None)
                    
                    if opp_val == self:
                        setattr(item, "Trace6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Trace6"):
                    opp_val = getattr(item, "Trace6", None)
                    
                    setattr(item, "Trace6", self)
                    

class trace_Property(TraceElement):

    def __init__(self, name: str, Property: "trace_Trace" = None, Property22: "trace_ModelElement" = None, owns: "trace_ModelElement" = None, accesses: set["trace_Trace"] = None):
        self.name = name
        self.Property = Property
        self.Property22 = Property22
        self.owns = owns
        self.accesses = accesses if accesses is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def owns(self):
        return self.__owns

    @owns.setter
    def owns(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Property__owns", None)
        self.__owns = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElement24"):
                opp_val = getattr(old_value, "ModelElement24", None)
                if opp_val == self:
                    setattr(old_value, "ModelElement24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElement24"):
                opp_val = getattr(value, "ModelElement24", None)
                setattr(value, "ModelElement24", self)

    @property
    def Property22(self):
        return self.__Property22

    @Property22.setter
    def Property22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Property__Property22", None)
        self.__Property22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modelElement"):
                opp_val = getattr(old_value, "modelElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modelElement"):
                opp_val = getattr(value, "modelElement", None)
                if opp_val is None:
                    setattr(value, "modelElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Property(self):
        return self.__Property

    @Property.setter
    def Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Property__Property", None)
        self.__Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces16"):
                opp_val = getattr(old_value, "traces16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces16"):
                opp_val = getattr(value, "traces16", None)
                if opp_val is None:
                    setattr(value, "traces16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def accesses(self):
        return self.__accesses

    @accesses.setter
    def accesses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Property__accesses", None)
        self.__accesses = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Trace26"):
                    opp_val = getattr(item, "Trace26", None)
                    
                    if opp_val == self:
                        setattr(item, "Trace26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Trace26"):
                    opp_val = getattr(item, "Trace26", None)
                    
                    setattr(item, "Trace26", self)
                    

class trace_ModelElement(TraceElement):

    def __init__(self, element_id: str, ModelElement: "trace_ExecutionContext" = None, involves: set["trace_ExecutionContext"] = None, reaches: set["trace_Trace"] = None, modelElement: set["trace_Property"] = None, ModelElement24: "trace_Property" = None, ModelElement14: "trace_Trace" = None):
        self.element_id = element_id
        self.ModelElement = ModelElement
        self.involves = involves if involves is not None else set()
        self.reaches = reaches if reaches is not None else set()
        self.modelElement = modelElement if modelElement is not None else set()
        self.ModelElement24 = ModelElement24
        self.ModelElement14 = ModelElement14
        
    @property
    def element_id(self) -> str:
        return self.__element_id

    @element_id.setter
    def element_id(self, element_id: str):
        self.__element_id = element_id

    @property
    def involves(self):
        return self.__involves

    @involves.setter
    def involves(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ModelElement__involves", None)
        self.__involves = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExecutionContext18"):
                    opp_val = getattr(item, "ExecutionContext18", None)
                    
                    if opp_val == self:
                        setattr(item, "ExecutionContext18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExecutionContext18"):
                    opp_val = getattr(item, "ExecutionContext18", None)
                    
                    setattr(item, "ExecutionContext18", self)
                    

    @property
    def ModelElement24(self):
        return self.__ModelElement24

    @ModelElement24.setter
    def ModelElement24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ModelElement__ModelElement24", None)
        self.__ModelElement24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owns"):
                opp_val = getattr(old_value, "owns", None)
                if opp_val == self:
                    setattr(old_value, "owns", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owns"):
                opp_val = getattr(value, "owns", None)
                setattr(value, "owns", self)

    @property
    def ModelElement14(self):
        return self.__ModelElement14

    @ModelElement14.setter
    def ModelElement14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ModelElement__ModelElement14", None)
        self.__ModelElement14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "traces13"):
                opp_val = getattr(old_value, "traces13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "traces13"):
                opp_val = getattr(value, "traces13", None)
                if opp_val is None:
                    setattr(value, "traces13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def reaches(self):
        return self.__reaches

    @reaches.setter
    def reaches(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ModelElement__reaches", None)
        self.__reaches = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Trace20"):
                    opp_val = getattr(item, "Trace20", None)
                    
                    if opp_val == self:
                        setattr(item, "Trace20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Trace20"):
                    opp_val = getattr(item, "Trace20", None)
                    
                    setattr(item, "Trace20", self)
                    

    @property
    def ModelElement(self):
        return self.__ModelElement

    @ModelElement.setter
    def ModelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ModelElement__ModelElement", None)
        self.__ModelElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "executionContext3"):
                opp_val = getattr(old_value, "executionContext3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "executionContext3"):
                opp_val = getattr(value, "executionContext3", None)
                if opp_val is None:
                    setattr(value, "executionContext3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def modelElement(self):
        return self.__modelElement

    @modelElement.setter
    def modelElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ModelElement__modelElement", None)
        self.__modelElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Property22"):
                    opp_val = getattr(item, "Property22", None)
                    
                    if opp_val == self:
                        setattr(item, "Property22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Property22"):
                    opp_val = getattr(item, "Property22", None)
                    
                    setattr(item, "Property22", self)
                    

class trace_ExecutionContext(TraceElement):

    def __init__(self, scriptId: str, modelsIds: str, executionContexts: set["trace_ModuleElement"] = None, executionContext: set["trace_Trace"] = None, executionContext3: set["trace_ModelElement"] = None, ExecutionContext18: "trace_ModelElement" = None, ExecutionContext: "trace_ModuleElement" = None, ExecutionContext8: "trace_Trace" = None):
        self.scriptId = scriptId
        self.modelsIds = modelsIds
        self.executionContexts = executionContexts if executionContexts is not None else set()
        self.executionContext = executionContext if executionContext is not None else set()
        self.executionContext3 = executionContext3 if executionContext3 is not None else set()
        self.ExecutionContext18 = ExecutionContext18
        self.ExecutionContext = ExecutionContext
        self.ExecutionContext8 = ExecutionContext8
        
    @property
    def scriptId(self) -> str:
        return self.__scriptId

    @scriptId.setter
    def scriptId(self, scriptId: str):
        self.__scriptId = scriptId

    @property
    def modelsIds(self) -> str:
        return self.__modelsIds

    @modelsIds.setter
    def modelsIds(self, modelsIds: str):
        self.__modelsIds = modelsIds

    @property
    def ExecutionContext18(self):
        return self.__ExecutionContext18

    @ExecutionContext18.setter
    def ExecutionContext18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ExecutionContext__ExecutionContext18", None)
        self.__ExecutionContext18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "involves"):
                opp_val = getattr(old_value, "involves", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "involves"):
                opp_val = getattr(value, "involves", None)
                if opp_val is None:
                    setattr(value, "involves", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def executionContext(self):
        return self.__executionContext

    @executionContext.setter
    def executionContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ExecutionContext__executionContext", None)
        self.__executionContext = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Trace"):
                    opp_val = getattr(item, "Trace", None)
                    
                    if opp_val == self:
                        setattr(item, "Trace", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Trace"):
                    opp_val = getattr(item, "Trace", None)
                    
                    setattr(item, "Trace", self)
                    

    @property
    def executionContext3(self):
        return self.__executionContext3

    @executionContext3.setter
    def executionContext3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ExecutionContext__executionContext3", None)
        self.__executionContext3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModelElement"):
                    opp_val = getattr(item, "ModelElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ModelElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModelElement"):
                    opp_val = getattr(item, "ModelElement", None)
                    
                    setattr(item, "ModelElement", self)
                    

    @property
    def executionContexts(self):
        return self.__executionContexts

    @executionContexts.setter
    def executionContexts(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ExecutionContext__executionContexts", None)
        self.__executionContexts = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ModuleElement"):
                    opp_val = getattr(item, "ModuleElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ModuleElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ModuleElement"):
                    opp_val = getattr(item, "ModuleElement", None)
                    
                    setattr(item, "ModuleElement", self)
                    

    @property
    def ExecutionContext8(self):
        return self.__ExecutionContext8

    @ExecutionContext8.setter
    def ExecutionContext8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ExecutionContext__ExecutionContext8", None)
        self.__ExecutionContext8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contains"):
                opp_val = getattr(old_value, "contains", None)
                if opp_val == self:
                    setattr(old_value, "contains", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contains"):
                opp_val = getattr(value, "contains", None)
                setattr(value, "contains", self)

    @property
    def ExecutionContext(self):
        return self.__ExecutionContext

    @ExecutionContext.setter
    def ExecutionContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_ExecutionContext__ExecutionContext", None)
        self.__ExecutionContext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "for"):
                opp_val = getattr(old_value, "for", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "for"):
                opp_val = getattr(value, "for", None)
                if opp_val is None:
                    setattr(value, "for", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
