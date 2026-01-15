from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class tracelinks_TraceLinksModel:

    pass
class tracelinks_TraceLinkEnd:

    def __init__(self, id: str, version: str, tracelinks_TraceLinkEnd: "tracelinks_TraceLink" = None, tracelinks_TraceLinkEnd5: "tracelinks_TraceLink" = None):
        self.id = id
        self.version = version
        self.tracelinks_TraceLinkEnd = tracelinks_TraceLinkEnd
        self.tracelinks_TraceLinkEnd5 = tracelinks_TraceLinkEnd5
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def tracelinks_TraceLinkEnd(self):
        return self.__tracelinks_TraceLinkEnd

    @tracelinks_TraceLinkEnd.setter
    def tracelinks_TraceLinkEnd(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracelinks_TraceLinkEnd__tracelinks_TraceLinkEnd", None)
        self.__tracelinks_TraceLinkEnd = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracelinks_TraceLink2"):
                opp_val = getattr(old_value, "tracelinks_TraceLink2", None)
                if opp_val == self:
                    setattr(old_value, "tracelinks_TraceLink2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracelinks_TraceLink2"):
                opp_val = getattr(value, "tracelinks_TraceLink2", None)
                setattr(value, "tracelinks_TraceLink2", self)

    @property
    def tracelinks_TraceLinkEnd5(self):
        return self.__tracelinks_TraceLinkEnd5

    @tracelinks_TraceLinkEnd5.setter
    def tracelinks_TraceLinkEnd5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tracelinks_TraceLinkEnd__tracelinks_TraceLinkEnd5", None)
        self.__tracelinks_TraceLinkEnd5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracelinks_TraceLink4"):
                opp_val = getattr(old_value, "tracelinks_TraceLink4", None)
                if opp_val == self:
                    setattr(old_value, "tracelinks_TraceLink4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracelinks_TraceLink4"):
                opp_val = getattr(value, "tracelinks_TraceLink4", None)
                setattr(value, "tracelinks_TraceLink4", self)

class tracelinks_TraceLink:

    pass