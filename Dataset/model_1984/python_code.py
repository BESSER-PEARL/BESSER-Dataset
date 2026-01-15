from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class trace_EObject:

    pass
class trace_TraceLink:

    def __init__(self, name: str, similarity: int, requiredSimilarity: int, rationale: str, similarityMethod: int, targetValue: str, sourceValue: str, trace_TraceLink: "trace_Trace" = None, trace_TraceLink7: "trace_EObject" = None, trace_TraceLink10: "trace_EObject" = None):
        self.name = name
        self.similarity = similarity
        self.requiredSimilarity = requiredSimilarity
        self.rationale = rationale
        self.similarityMethod = similarityMethod
        self.targetValue = targetValue
        self.sourceValue = sourceValue
        self.trace_TraceLink = trace_TraceLink
        self.trace_TraceLink7 = trace_TraceLink7
        self.trace_TraceLink10 = trace_TraceLink10
        
    @property
    def similarity(self) -> int:
        return self.__similarity

    @similarity.setter
    def similarity(self, similarity: int):
        self.__similarity = similarity

    @property
    def rationale(self) -> str:
        return self.__rationale

    @rationale.setter
    def rationale(self, rationale: str):
        self.__rationale = rationale

    @property
    def requiredSimilarity(self) -> int:
        return self.__requiredSimilarity

    @requiredSimilarity.setter
    def requiredSimilarity(self, requiredSimilarity: int):
        self.__requiredSimilarity = requiredSimilarity

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def sourceValue(self) -> str:
        return self.__sourceValue

    @sourceValue.setter
    def sourceValue(self, sourceValue: str):
        self.__sourceValue = sourceValue

    @property
    def similarityMethod(self) -> int:
        return self.__similarityMethod

    @similarityMethod.setter
    def similarityMethod(self, similarityMethod: int):
        self.__similarityMethod = similarityMethod

    @property
    def targetValue(self) -> str:
        return self.__targetValue

    @targetValue.setter
    def targetValue(self, targetValue: str):
        self.__targetValue = targetValue

    @property
    def trace_TraceLink(self):
        return self.__trace_TraceLink

    @trace_TraceLink.setter
    def trace_TraceLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLink__trace_TraceLink", None)
        self.__trace_TraceLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_Trace"):
                opp_val = getattr(old_value, "trace_Trace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_Trace"):
                opp_val = getattr(value, "trace_Trace", None)
                if opp_val is None:
                    setattr(value, "trace_Trace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trace_TraceLink10(self):
        return self.__trace_TraceLink10

    @trace_TraceLink10.setter
    def trace_TraceLink10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLink__trace_TraceLink10", None)
        self.__trace_TraceLink10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_EObject11"):
                opp_val = getattr(old_value, "trace_EObject11", None)
                if opp_val == self:
                    setattr(old_value, "trace_EObject11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_EObject11"):
                opp_val = getattr(value, "trace_EObject11", None)
                setattr(value, "trace_EObject11", self)

    @property
    def trace_TraceLink7(self):
        return self.__trace_TraceLink7

    @trace_TraceLink7.setter
    def trace_TraceLink7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_TraceLink__trace_TraceLink7", None)
        self.__trace_TraceLink7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_EObject8"):
                opp_val = getattr(old_value, "trace_EObject8", None)
                if opp_val == self:
                    setattr(old_value, "trace_EObject8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_EObject8"):
                opp_val = getattr(value, "trace_EObject8", None)
                setattr(value, "trace_EObject8", self)

    def sameAs(self, tracelink: str) -> bool:
        # TODO: Implement sameAs method
        pass

class trace_Trace:

    def __init__(self, trace_Trace: set["trace_TraceLink"] = None, trace_Trace2: "trace_EObject" = None, trace_Trace4: "trace_EObject" = None):
        self.trace_Trace = trace_Trace if trace_Trace is not None else set()
        self.trace_Trace2 = trace_Trace2
        self.trace_Trace4 = trace_Trace4
        
    @property
    def trace_Trace(self):
        return self.__trace_Trace

    @trace_Trace.setter
    def trace_Trace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__trace_Trace", None)
        self.__trace_Trace = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_TraceLink"):
                    opp_val = getattr(item, "trace_TraceLink", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_TraceLink", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_TraceLink"):
                    opp_val = getattr(item, "trace_TraceLink", None)
                    
                    setattr(item, "trace_TraceLink", self)
                    

    @property
    def trace_Trace4(self):
        return self.__trace_Trace4

    @trace_Trace4.setter
    def trace_Trace4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__trace_Trace4", None)
        self.__trace_Trace4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trace_EObject5"):
                opp_val = getattr(old_value, "trace_EObject5", None)
                if opp_val == self:
                    setattr(old_value, "trace_EObject5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trace_EObject5"):
                opp_val = getattr(value, "trace_EObject5", None)
                setattr(value, "trace_EObject5", self)

    @property
    def trace_Trace2(self):
        return self.__trace_Trace2

    @trace_Trace2.setter
    def trace_Trace2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_Trace__trace_Trace2", None)
        self.__trace_Trace2 = value
        
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

    def getAllMappedObjects(self) -> str:
        # TODO: Implement getAllMappedObjects method
        pass
