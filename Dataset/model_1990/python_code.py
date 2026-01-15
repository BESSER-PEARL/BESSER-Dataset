from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class trace_EObject:

    pass
class trace_InputElement:

    pass
class trace_OutputFile:

    def __init__(self, fileName: str, outlet: str, trace_OutputFile: "trace_Trace" = None, trace_OutputFile2: set["trace_InputElement"] = None, trace_OutputFile4: "trace_EObject" = None):
        self.fileName = fileName
        self.outlet = outlet
        self.trace_OutputFile = trace_OutputFile
        self.trace_OutputFile2 = trace_OutputFile2 if trace_OutputFile2 is not None else set()
        self.trace_OutputFile4 = trace_OutputFile4
        
    @property
    def outlet(self) -> str:
        return self.__outlet

    @outlet.setter
    def outlet(self, outlet: str):
        self.__outlet = outlet

    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def trace_OutputFile4(self):
        return self.__trace_OutputFile4

    @trace_OutputFile4.setter
    def trace_OutputFile4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_OutputFile__trace_OutputFile4", None)
        self.__trace_OutputFile4 = value
        
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

    @property
    def trace_OutputFile(self):
        return self.__trace_OutputFile

    @trace_OutputFile.setter
    def trace_OutputFile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_OutputFile__trace_OutputFile", None)
        self.__trace_OutputFile = value
        
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
    def trace_OutputFile2(self):
        return self.__trace_OutputFile2

    @trace_OutputFile2.setter
    def trace_OutputFile2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_OutputFile__trace_OutputFile2", None)
        self.__trace_OutputFile2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "trace_InputElement"):
                    opp_val = getattr(item, "trace_InputElement", None)
                    
                    if opp_val == self:
                        setattr(item, "trace_InputElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "trace_InputElement"):
                    opp_val = getattr(item, "trace_InputElement", None)
                    
                    setattr(item, "trace_InputElement", self)
                    

class trace_Trace:

    pass
class trace_EStructuralFeature:

    pass