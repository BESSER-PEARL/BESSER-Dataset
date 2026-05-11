from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Classifier:

    pass
class dscDiagramModel_ShallowHistory(Classifier):

    pass
class dscDiagramModel_DeepHistory(Classifier):

    pass
class dscDiagramModel_StartPoint(Classifier):

    pass
class Relationship:

    pass
class dscDiagramModel_Transition(Relationship):

    def __init__(self, transitionID: str, eventID: str, guardID: str, actionID: str, showProperties: bool, showTransitionID: bool, triggeredByEvent: bool):
        self.transitionID = transitionID
        self.eventID = eventID
        self.guardID = guardID
        self.actionID = actionID
        self.showProperties = showProperties
        self.showTransitionID = showTransitionID
        self.triggeredByEvent = triggeredByEvent
        
        pass
    @property
    def triggeredByEvent(self):
        return self.__triggeredByEvent

    @triggeredByEvent.setter
    def triggeredByEvent(self, triggeredByEvent: bool):
        self.__triggeredByEvent = triggeredByEvent


    @property
    def guardID(self):
        return self.__guardID

    @guardID.setter
    def guardID(self, guardID: str):
        self.__guardID = guardID


    @property
    def transitionID(self):
        return self.__transitionID

    @transitionID.setter
    def transitionID(self, transitionID: str):
        self.__transitionID = transitionID


    @property
    def showTransitionID(self):
        return self.__showTransitionID

    @showTransitionID.setter
    def showTransitionID(self, showTransitionID: bool):
        self.__showTransitionID = showTransitionID


    @property
    def showProperties(self):
        return self.__showProperties

    @showProperties.setter
    def showProperties(self, showProperties: bool):
        self.__showProperties = showProperties


    @property
    def actionID(self):
        return self.__actionID

    @actionID.setter
    def actionID(self, actionID: str):
        self.__actionID = actionID


    @property
    def eventID(self):
        return self.__eventID

    @eventID.setter
    def eventID(self, eventID: str):
        self.__eventID = eventID


class dscDiagramModel_AnchorNoteToItem(Relationship):

    pass
class Container:

    pass
class dscDiagramModel_DSCState(Container):

    def __init__(self, Variables: str, isSimple: bool, compositeState: "dscDiagramModel_StartPoint" = None, compositeState7: "dscDiagramModel_ShallowHistory" = None, compositeState9: "dscDiagramModel_DeepHistory" = None, DSCState: "dscDiagramModel_StartPoint" = None, DSCState2: "dscDiagramModel_ShallowHistory" = None, DSCState4: "dscDiagramModel_DeepHistory" = None):
        self.Variables = Variables
        self.isSimple = isSimple
        self.compositeState = compositeState
        self.compositeState7 = compositeState7
        self.compositeState9 = compositeState9
        self.DSCState = DSCState
        self.DSCState2 = DSCState2
        self.DSCState4 = DSCState4
        
        pass
    @property
    def Variables(self):
        return self.__Variables

    @Variables.setter
    def Variables(self, Variables: str):
        self.__Variables = Variables


    @property
    def isSimple(self):
        return self.__isSimple

    @isSimple.setter
    def isSimple(self, isSimple: bool):
        self.__isSimple = isSimple


    @property
    def DSCState4(self):
        return self.__DSCState4

    @DSCState4.setter
    def DSCState4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dscDiagramModel_DSCState__DSCState4", None)
        self.__DSCState4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "deepHistory"):
                opp_val = getattr(old_value, "deepHistory", None)
                if opp_val == self:
                    setattr(old_value, "deepHistory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "deepHistory"):
                opp_val = getattr(value, "deepHistory", None)
                setattr(value, "deepHistory", self)

    @property
    def compositeState9(self):
        return self.__compositeState9

    @compositeState9.setter
    def compositeState9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dscDiagramModel_DSCState__compositeState9", None)
        self.__compositeState9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DeepHistory"):
                opp_val = getattr(old_value, "DeepHistory", None)
                if opp_val == self:
                    setattr(old_value, "DeepHistory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DeepHistory"):
                opp_val = getattr(value, "DeepHistory", None)
                setattr(value, "DeepHistory", self)

    @property
    def DSCState(self):
        return self.__DSCState

    @DSCState.setter
    def DSCState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dscDiagramModel_DSCState__DSCState", None)
        self.__DSCState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "startPoint"):
                opp_val = getattr(old_value, "startPoint", None)
                if opp_val == self:
                    setattr(old_value, "startPoint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "startPoint"):
                opp_val = getattr(value, "startPoint", None)
                setattr(value, "startPoint", self)

    @property
    def compositeState(self):
        return self.__compositeState

    @compositeState.setter
    def compositeState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dscDiagramModel_DSCState__compositeState", None)
        self.__compositeState = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StartPoint"):
                opp_val = getattr(old_value, "StartPoint", None)
                if opp_val == self:
                    setattr(old_value, "StartPoint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StartPoint"):
                opp_val = getattr(value, "StartPoint", None)
                setattr(value, "StartPoint", self)

    @property
    def DSCState2(self):
        return self.__DSCState2

    @DSCState2.setter
    def DSCState2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dscDiagramModel_DSCState__DSCState2", None)
        self.__DSCState2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shallowHistory"):
                opp_val = getattr(old_value, "shallowHistory", None)
                if opp_val == self:
                    setattr(old_value, "shallowHistory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shallowHistory"):
                opp_val = getattr(value, "shallowHistory", None)
                setattr(value, "shallowHistory", self)

    @property
    def compositeState7(self):
        return self.__compositeState7

    @compositeState7.setter
    def compositeState7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dscDiagramModel_DSCState__compositeState7", None)
        self.__compositeState7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ShallowHistory"):
                opp_val = getattr(old_value, "ShallowHistory", None)
                if opp_val == self:
                    setattr(old_value, "ShallowHistory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ShallowHistory"):
                opp_val = getattr(value, "ShallowHistory", None)
                setattr(value, "ShallowHistory", self)

class GenericDiagram:

    pass
class dscDiagramModel_DSCDiagram(GenericDiagram):

    def __init__(self, eventFile: str, guardFile: str, actionFile: str, diagramVariables: str, functionFile: str):
        self.eventFile = eventFile
        self.guardFile = guardFile
        self.actionFile = actionFile
        self.diagramVariables = diagramVariables
        self.functionFile = functionFile
        
        pass
    @property
    def guardFile(self):
        return self.__guardFile

    @guardFile.setter
    def guardFile(self, guardFile: str):
        self.__guardFile = guardFile


    @property
    def actionFile(self):
        return self.__actionFile

    @actionFile.setter
    def actionFile(self, actionFile: str):
        self.__actionFile = actionFile


    @property
    def functionFile(self):
        return self.__functionFile

    @functionFile.setter
    def functionFile(self, functionFile: str):
        self.__functionFile = functionFile


    @property
    def eventFile(self):
        return self.__eventFile

    @eventFile.setter
    def eventFile(self, eventFile: str):
        self.__eventFile = eventFile


    @property
    def diagramVariables(self):
        return self.__diagramVariables

    @diagramVariables.setter
    def diagramVariables(self, diagramVariables: str):
        self.__diagramVariables = diagramVariables

