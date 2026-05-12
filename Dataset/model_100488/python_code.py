from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class UMLMetamodelFragment_Event:

    pass
class Event:

    pass
class UMLMetamodelFragment_Transition:

    pass
class CompositeState:

    pass
class UMLMetamodelFragment_StateVertex:

    pass
class Transition:

    pass
class Stereotype:

    pass
class Class:

    pass
class StateMachine:

    pass
class UMLMetamodelFragment_Dependency:

    pass
class UMLMetamodelFragment_Generalization_:

    pass
class Dependency:

    pass
class Generalization_:

    pass
class UMLMetamodelFragment_Class:

    pass
class StateVertex:

    pass
class UMLMetamodelFragment_PseudoState(StateVertex):

    pass
class UMLMetamodelFragment_State(StateVertex):

    pass
class State:

    pass
class UMLMetamodelFragment_SimpleState(State):

    pass
class UMLMetamodelFragment_CompositeState(State):

    pass
class UMLMetamodelFragment_FinalState(State):

    pass
class UMLMetamodelFragment_StateMachine:

    pass
class UMLMetamodelFragment_Stereotype:

    def __init__(self, baseClass: str, stereotype: "Dependency" = None):
        self.baseClass = baseClass
        self.stereotype = stereotype
        
        pass
    @property
    def baseClass(self):
        return self.__baseClass

    @baseClass.setter
    def baseClass(self, baseClass: str):
        self.__baseClass = baseClass


    @property
    def stereotype(self):
        return self.__stereotype

    @stereotype.setter
    def stereotype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UMLMetamodelFragment_Stereotype__stereotype", None)
        self.__stereotype = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Dependency9"):
                opp_val = getattr(old_value, "Dependency9", None)
                if opp_val == self:
                    setattr(old_value, "Dependency9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Dependency9"):
                opp_val = getattr(value, "Dependency9", None)
                setattr(value, "Dependency9", self)
