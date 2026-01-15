from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Lqn2umlTrace_TraceLink:

    def __init__(self, sources: str, targets: str, description: str, Lqn2umlTrace_TraceLink: "Lqn2umlTrace_Trace" = None):
        self.sources = sources
        self.targets = targets
        self.description = description
        self.Lqn2umlTrace_TraceLink = Lqn2umlTrace_TraceLink
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def targets(self) -> str:
        return self.__targets

    @targets.setter
    def targets(self, targets: str):
        self.__targets = targets

    @property
    def sources(self) -> str:
        return self.__sources

    @sources.setter
    def sources(self, sources: str):
        self.__sources = sources

    @property
    def Lqn2umlTrace_TraceLink(self):
        return self.__Lqn2umlTrace_TraceLink

    @Lqn2umlTrace_TraceLink.setter
    def Lqn2umlTrace_TraceLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Lqn2umlTrace_TraceLink__Lqn2umlTrace_TraceLink", None)
        self.__Lqn2umlTrace_TraceLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Lqn2umlTrace_Trace"):
                opp_val = getattr(old_value, "Lqn2umlTrace_Trace", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Lqn2umlTrace_Trace"):
                opp_val = getattr(value, "Lqn2umlTrace_Trace", None)
                if opp_val is None:
                    setattr(value, "Lqn2umlTrace_Trace", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Lqn2umlTrace_Trace:

    pass