from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ToolInfoConstants(Enum):
    toolName = "toolName"
    toolVersion = "toolVersion"
    uri = "uri"
class ServerType(Enum):
    InfiniteServer = "InfiniteServer"
    OneServer = "OneServer"
    LoadDependent = "LoadDependent"
    MarkingDependent = "MarkingDependent"
class TransitionKind(Enum):
    Immediate = "Immediate"
    Exponential = "Exponential"
    Deterministic = "Deterministic"


############################################
# Definition of Classes
############################################

class pnextensions_pnutils_PnUtils:

    def __init__(self):
        
        pass
    def layout(self, pnextensions_petriNet):
        # TODO: Implement layout method
        pass

class pnextensions_pnutils_ToolInfoUtils:

    def __init__(self):
        
        pass
    def deleteToolInfoEntryByGrammarUri(self, pnextensions_uri, pnextensions_pnObject) :
        # TODO: Implement deleteToolInfoEntryByGrammarUri method
        pass

    def setTransitionServerType(self, pnextensions_transition, pnextensions_serverType, pnextensions_value):
        # TODO: Implement setTransitionServerType method
        pass

    def isTransitionKind(self, pnextensions_transition, pnextensions_transitionKind) :
        # TODO: Implement isTransitionKind method
        pass

    def isEObjectValidTransition(self, pnextensions_eObject) :
        # TODO: Implement isEObjectValidTransition method
        pass

    def isTransitionServerType(self, pnextensions_serverType, pnextensions_transition) :
        # TODO: Implement isTransitionServerType method
        pass

    def setToolInfoEntryByGrammarUri(self, pnextensions_pnObject, pnextensions_value, pnextensions_uri):
        # TODO: Implement setToolInfoEntryByGrammarUri method
        pass

    def getTransitionRate(self, pnextensions_transition) :
        # TODO: Implement getTransitionRate method
        pass

    def setTransitionKind(self, pnextensions_transitionKind, pnextensions_value, pnextensions_transition):
        # TODO: Implement setTransitionKind method
        pass

    def isEObjectValidPnObject(self, pnextensions_eObject) :
        # TODO: Implement isEObjectValidPnObject method
        pass

    def getToolInfoEntryByGrammarUri(self, pnextensions_uri, pnextensions_pnObject) :
        # TODO: Implement getToolInfoEntryByGrammarUri method
        pass

class pnextensions_pnutils_DataTypeUtils:

    def __init__(self):
        
        pass
    def createLongString(self, pnextensions_string) :
        # TODO: Implement createLongString method
        pass

    def createURI(self, pnextensions_stringUri) :
        # TODO: Implement createURI method
        pass
