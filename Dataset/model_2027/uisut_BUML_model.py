####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
uisut_ApplicationSystem = Class(name="uisut::ApplicationSystem")
uisut_AbstractState = Class(name="uisut::AbstractState", is_abstract=True)
uisut_UITransition = Class(name="uisut::UITransition")
uisut_UISUT = Class(name="uisut::UISUT")
UISUTElement = Class(name="UISUTElement")
uisut_UIStatemachine = Class(name="uisut::UIStatemachine")
uisut_UIState = Class(name="uisut::UIState")
AbstractState = Class(name="AbstractState")
uisut_UIControl = Class(name="uisut::UIControl")
uisut_UIDataVariable = Class(name="uisut::UIDataVariable")
uisut_UITrigger = Class(name="uisut::UITrigger", is_abstract=True)
uisut_UICondition = Class(name="uisut::UICondition")
uisut_Action = Class(name="uisut::Action")
uisut_UserTrigger = Class(name="uisut::UserTrigger")
UITrigger = Class(name="UITrigger")
uisut_ComponentTrigger = Class(name="uisut::ComponentTrigger")
uisut_UISUTElement = Class(name="uisut::UISUTElement", is_abstract=True)
uisut_InitialState = Class(name="uisut::InitialState")
uisut_FinalState = Class(name="uisut::FinalState")

# uisut_ApplicationSystem class attributes and methods

# uisut_AbstractState class attributes and methods

# uisut_UITransition class attributes and methods
uisut_UITransition_triggerStr: Property = Property(name="triggerStr", type=StringType)
uisut_UITransition_guardStr: Property = Property(name="guardStr", type=StringType)
uisut_UITransition_scriptStr: Property = Property(name="scriptStr", type=StringType)
uisut_UITransition_actionStr: Property = Property(name="actionStr", type=StringType)
uisut_UITransition.attributes={uisut_UITransition_scriptStr, uisut_UITransition_guardStr, uisut_UITransition_actionStr, uisut_UITransition_triggerStr}

# uisut_UISUT class attributes and methods

# UISUTElement class attributes and methods

# uisut_UIStatemachine class attributes and methods

# uisut_UIState class attributes and methods
uisut_UIState_isInitial: Property = Property(name="isInitial", type=BooleanType)
uisut_UIState_pic: Property = Property(name="pic", type=StringType)
uisut_UIState.attributes={uisut_UIState_pic, uisut_UIState_isInitial}

# AbstractState class attributes and methods

# uisut_UIControl class attributes and methods
uisut_UIControl_valueExpression: Property = Property(name="valueExpression", type=StringType)
uisut_UIControl_variableName: Property = Property(name="variableName", type=StringType)
uisut_UIControl.attributes={uisut_UIControl_valueExpression, uisut_UIControl_variableName}

# uisut_UIDataVariable class attributes and methods
uisut_UIDataVariable_constraintRE: Property = Property(name="constraintRE", type=StringType)
uisut_UIDataVariable.attributes={uisut_UIDataVariable_constraintRE}

# uisut_UITrigger class attributes and methods

# uisut_UICondition class attributes and methods

# uisut_Action class attributes and methods

# uisut_UserTrigger class attributes and methods

# UITrigger class attributes and methods

# uisut_ComponentTrigger class attributes and methods

# uisut_UISUTElement class attributes and methods
uisut_UISUTElement_name: Property = Property(name="name", type=StringType)
uisut_UISUTElement_description: Property = Property(name="description", type=StringType)
uisut_UISUTElement_id: Property = Property(name="id", type=StringType)
uisut_UISUTElement.attributes={uisut_UISUTElement_description, uisut_UISUTElement_name, uisut_UISUTElement_id}

# uisut_InitialState class attributes and methods

# uisut_FinalState class attributes and methods

# Relationships
itsSTM0: BinaryAssociation = BinaryAssociation(
    name="itsSTM0",
    ends={
        Property(name="uisut_UISUT", type=uisut_UIStatemachine, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="uisut_UIStatemachine", type=uisut_UISUT, multiplicity=Multiplicity(1, 1))
    }
)
itsUISUT1: BinaryAssociation = BinaryAssociation(
    name="itsUISUT1",
    ends={
        Property(name="uisut_UISUT2", type=uisut_ApplicationSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="uisut_ApplicationSystem", type=uisut_UISUT, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
itsState3: BinaryAssociation = BinaryAssociation(
    name="itsState3",
    ends={
        Property(name="uisut_AbstractState", type=uisut_UIStatemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="uisut_UIStatemachine4", type=uisut_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itsTransition5: BinaryAssociation = BinaryAssociation(
    name="itsTransition5",
    ends={
        Property(name="uisut_UITransition", type=uisut_UIStatemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="uisut_UIStatemachine6", type=uisut_UITransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itsUIControl9: BinaryAssociation = BinaryAssociation(
    name="itsUIControl9",
    ends={
        Property(name="uisut_UIControl", type=uisut_UIState, multiplicity=Multiplicity(1, 1)),
        Property(name="uisut_UIState", type=uisut_UIControl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
addedDataVariable10: BinaryAssociation = BinaryAssociation(
    name="addedDataVariable10",
    ends={
        Property(name="uisut_UIDataVariable12", type=uisut_UIState, multiplicity=Multiplicity(1, 1)),
        Property(name="uisut_UIState11", type=uisut_UIDataVariable, multiplicity=Multiplicity(0, 9999))
    }
)
deletedDataVariable13: BinaryAssociation = BinaryAssociation(
    name="deletedDataVariable13",
    ends={
        Property(name="uisut_UIDataVariable15", type=uisut_UIState, multiplicity=Multiplicity(1, 1)),
        Property(name="uisut_UIState14", type=uisut_UIDataVariable, multiplicity=Multiplicity(0, 9999))
    }
)
itsDataVariable7: BinaryAssociation = BinaryAssociation(
    name="itsDataVariable7",
    ends={
        Property(name="uisut_UIDataVariable", type=uisut_UIStatemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="uisut_UIStatemachine8", type=uisut_UIDataVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
itsSrcState17: BinaryAssociation = BinaryAssociation(
    name="itsSrcState17",
    ends={
        Property(name="AbstractState18", type=uisut_UITransition, multiplicity=Multiplicity(1, 1)),
        Property(name="itsOutTransition", type=uisut_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
itsTrigger19: BinaryAssociation = BinaryAssociation(
    name="itsTrigger19",
    ends={
        Property(name="uisut_UITrigger", type=uisut_UITransition, multiplicity=Multiplicity(1, 1)),
        Property(name="uisut_UITransition20", type=uisut_UITrigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
itsCondition21: BinaryAssociation = BinaryAssociation(
    name="itsCondition21",
    ends={
        Property(name="uisut_UICondition", type=uisut_UITransition, multiplicity=Multiplicity(1, 1)),
        Property(name="uisut_UITransition22", type=uisut_UICondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
itsAction23: BinaryAssociation = BinaryAssociation(
    name="itsAction23",
    ends={
        Property(name="uisut_Action", type=uisut_UITransition, multiplicity=Multiplicity(1, 1)),
        Property(name="uisut_UITransition24", type=uisut_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
itsTrgtState16: BinaryAssociation = BinaryAssociation(
    name="itsTrgtState16",
    ends={
        Property(name="AbstractState", type=uisut_UITransition, multiplicity=Multiplicity(1, 1)),
        Property(name="itsInTransition", type=uisut_AbstractState, multiplicity=Multiplicity(1, 1))
    }
)
itsInputDaa28: BinaryAssociation = BinaryAssociation(
    name="itsInputDaa28",
    ends={
        Property(name="uisut_UIDataVariable30", type=uisut_UIControl, multiplicity=Multiplicity(1, 1)),
        Property(name="uisut_UIControl29", type=uisut_UIDataVariable, multiplicity=Multiplicity(0, 1))
    }
)
guardedDataVariable25: BinaryAssociation = BinaryAssociation(
    name="guardedDataVariable25",
    ends={
        Property(name="uisut_UIDataVariable27", type=uisut_UITransition, multiplicity=Multiplicity(1, 1)),
        Property(name="uisut_UITransition26", type=uisut_UIDataVariable, multiplicity=Multiplicity(0, 9999))
    }
)
itsOutputData31: BinaryAssociation = BinaryAssociation(
    name="itsOutputData31",
    ends={
        Property(name="uisut_UIDataVariable33", type=uisut_UIControl, multiplicity=Multiplicity(1, 1)),
        Property(name="uisut_UIControl32", type=uisut_UIDataVariable, multiplicity=Multiplicity(0, 1))
    }
)
itsOutTransition35: BinaryAssociation = BinaryAssociation(
    name="itsOutTransition35",
    ends={
        Property(name="UITransition36", type=uisut_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="itsSrcState", type=uisut_UITransition, multiplicity=Multiplicity(0, 9999))
    }
)
itsInTransition34: BinaryAssociation = BinaryAssociation(
    name="itsInTransition34",
    ends={
        Property(name="UITransition", type=uisut_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="itsTrgtState", type=uisut_UITransition, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_uisut_ApplicationSystem_UISUTElement = Generalization(general=UISUTElement, specific=uisut_ApplicationSystem)
gen_uisut_UIStatemachine_UISUTElement = Generalization(general=UISUTElement, specific=uisut_UIStatemachine)
gen_uisut_UISUT_UISUTElement = Generalization(general=UISUTElement, specific=uisut_UISUT)
gen_uisut_UIState_AbstractState = Generalization(general=AbstractState, specific=uisut_UIState)
gen_uisut_UITransition_UISUTElement = Generalization(general=UISUTElement, specific=uisut_UITransition)
gen_uisut_UITrigger_UISUTElement = Generalization(general=UISUTElement, specific=uisut_UITrigger)
gen_uisut_UserTrigger_UITrigger = Generalization(general=UITrigger, specific=uisut_UserTrigger)
gen_uisut_ComponentTrigger_UITrigger = Generalization(general=UITrigger, specific=uisut_ComponentTrigger)
gen_uisut_UICondition_UISUTElement = Generalization(general=UISUTElement, specific=uisut_UICondition)
gen_uisut_Action_UISUTElement = Generalization(general=UISUTElement, specific=uisut_Action)
gen_uisut_UIControl_UISUTElement = Generalization(general=UISUTElement, specific=uisut_UIControl)
gen_uisut_UIDataVariable_UISUTElement = Generalization(general=UISUTElement, specific=uisut_UIDataVariable)
gen_uisut_InitialState_AbstractState = Generalization(general=AbstractState, specific=uisut_InitialState)
gen_uisut_FinalState_AbstractState = Generalization(general=AbstractState, specific=uisut_FinalState)
gen_uisut_AbstractState_UISUTElement = Generalization(general=UISUTElement, specific=uisut_AbstractState)

# Domain Model
domain_model = DomainModel(
    name="uisut",
    types={uisut_ApplicationSystem, uisut_AbstractState, uisut_UITransition, uisut_UISUT, UISUTElement, uisut_UIStatemachine, uisut_UIState, AbstractState, uisut_UIControl, uisut_UIDataVariable, uisut_UITrigger, uisut_UICondition, uisut_Action, uisut_UserTrigger, UITrigger, uisut_ComponentTrigger, uisut_UISUTElement, uisut_InitialState, uisut_FinalState},
    associations={itsSTM0, itsUISUT1, itsState3, itsTransition5, itsUIControl9, addedDataVariable10, deletedDataVariable13, itsDataVariable7, itsSrcState17, itsTrigger19, itsCondition21, itsAction23, itsTrgtState16, itsInputDaa28, guardedDataVariable25, itsOutputData31, itsOutTransition35, itsInTransition34},
    generalizations={gen_uisut_ApplicationSystem_UISUTElement, gen_uisut_UIStatemachine_UISUTElement, gen_uisut_UISUT_UISUTElement, gen_uisut_UIState_AbstractState, gen_uisut_UITransition_UISUTElement, gen_uisut_UITrigger_UISUTElement, gen_uisut_UserTrigger_UITrigger, gen_uisut_ComponentTrigger_UITrigger, gen_uisut_UICondition_UISUTElement, gen_uisut_Action_UISUTElement, gen_uisut_UIControl_UISUTElement, gen_uisut_UIDataVariable_UISUTElement, gen_uisut_InitialState_AbstractState, gen_uisut_FinalState_AbstractState, gen_uisut_AbstractState_UISUTElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)