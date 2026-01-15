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

# Enumerations
StateType: Enumeration = Enumeration(
    name="StateType",
    literals={
            EnumerationLiteral(name="NORMAL"),
			EnumerationLiteral(name="CONDITIONAL"),
			EnumerationLiteral(name="REFERENCE"),
			EnumerationLiteral(name="TEXTUAL")
    }
)

TransitionType: Enumeration = Enumeration(
    name="TransitionType",
    literals={
            EnumerationLiteral(name="WEAKABORT"),
			EnumerationLiteral(name="STRONGABORT"),
			EnumerationLiteral(name="NORMALTERMINATION")
    }
)

# Classes
synccharts_Assignment = Class(name="synccharts::Assignment")
Effect = Class(name="Effect")
synccharts_Action = Class(name="synccharts::Action")
Annotatable = Class(name="Annotatable")
synccharts_Effect = Class(name="synccharts::Effect", is_abstract=True)
synccharts_Expression = Class(name="synccharts::Expression")
synccharts_Transition = Class(name="synccharts::Transition")
synccharts_Variable = Class(name="synccharts::Variable")
synccharts_Emission = Class(name="synccharts::Emission")
synccharts_Signal = Class(name="synccharts::Signal")
synccharts_Region = Class(name="synccharts::Region")
Scope = Class(name="Scope")
synccharts_State = Class(name="synccharts::State")
synccharts_Substitution = Class(name="synccharts::Substitution")
synccharts_Scope = Class(name="synccharts::Scope", is_abstract=True)
Action = Class(name="Action")
synccharts_EObject = Class(name="synccharts::EObject")
synccharts_TextualCode = Class(name="synccharts::TextualCode")
synccharts_TextEffect = Class(name="synccharts::TextEffect")
TextualCode = Class(name="TextualCode")

# synccharts_Assignment class attributes and methods

# Effect class attributes and methods

# synccharts_Action class attributes and methods
synccharts_Action_delay: Property = Property(name="delay", type=IntegerType)
synccharts_Action_isImmediate: Property = Property(name="isImmediate", type=BooleanType)
synccharts_Action_label: Property = Property(name="label", type=StringType)
synccharts_Action.attributes={synccharts_Action_delay, synccharts_Action_isImmediate, synccharts_Action_label}

# Annotatable class attributes and methods

# synccharts_Effect class attributes and methods

# synccharts_Expression class attributes and methods

# synccharts_Transition class attributes and methods
synccharts_Transition_priority: Property = Property(name="priority", type=IntegerType)
synccharts_Transition_type: Property = Property(name="type", type=StringType)
synccharts_Transition_isHistory: Property = Property(name="isHistory", type=BooleanType)
synccharts_Transition.attributes={synccharts_Transition_type, synccharts_Transition_isHistory, synccharts_Transition_priority}

# synccharts_Variable class attributes and methods

# synccharts_Emission class attributes and methods

# synccharts_Signal class attributes and methods

# synccharts_Region class attributes and methods

# Scope class attributes and methods

# synccharts_State class attributes and methods
synccharts_State_type: Property = Property(name="type", type=StringType)
synccharts_State_isInitial: Property = Property(name="isInitial", type=BooleanType)
synccharts_State_isFinal: Property = Property(name="isFinal", type=BooleanType)
synccharts_State.attributes={synccharts_State_type, synccharts_State_isFinal, synccharts_State_isInitial}

# synccharts_Substitution class attributes and methods
synccharts_Substitution_formal: Property = Property(name="formal", type=StringType)
synccharts_Substitution_actual: Property = Property(name="actual", type=StringType)
synccharts_Substitution.attributes={synccharts_Substitution_formal, synccharts_Substitution_actual}

# synccharts_Scope class attributes and methods
synccharts_Scope_id: Property = Property(name="id", type=StringType)
synccharts_Scope_label: Property = Property(name="label", type=StringType)
synccharts_Scope_interfaceDeclaration: Property = Property(name="interfaceDeclaration", type=StringType)
synccharts_Scope.attributes={synccharts_Scope_id, synccharts_Scope_interfaceDeclaration, synccharts_Scope_label}

# Action class attributes and methods

# synccharts_EObject class attributes and methods

# synccharts_TextualCode class attributes and methods

# synccharts_TextEffect class attributes and methods

# TextualCode class attributes and methods

# Relationships
effects0: BinaryAssociation = BinaryAssociation(
    name="effects0",
    ends={
        Property(name="synccharts_Effect", type=synccharts_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="synccharts_Action", type=synccharts_Effect, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trigger1: BinaryAssociation = BinaryAssociation(
    name="trigger1",
    ends={
        Property(name="synccharts_Expression", type=synccharts_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="synccharts_Action2", type=synccharts_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outgoingTransitions18: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions18",
    ends={
        Property(name="Transition", type=synccharts_State, multiplicity=Multiplicity(1, 1)),
        Property(name="sourceState", type=synccharts_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable3: BinaryAssociation = BinaryAssociation(
    name="variable3",
    ends={
        Property(name="synccharts_Variable", type=synccharts_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="synccharts_Assignment", type=synccharts_Variable, multiplicity=Multiplicity(1, 1))
    }
)
expression4: BinaryAssociation = BinaryAssociation(
    name="expression4",
    ends={
        Property(name="synccharts_Expression6", type=synccharts_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="synccharts_Assignment5", type=synccharts_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
signal7: BinaryAssociation = BinaryAssociation(
    name="signal7",
    ends={
        Property(name="synccharts_Signal", type=synccharts_Emission, multiplicity=Multiplicity(1, 1)),
        Property(name="synccharts_Emission", type=synccharts_Signal, multiplicity=Multiplicity(1, 1))
    }
)
newValue8: BinaryAssociation = BinaryAssociation(
    name="newValue8",
    ends={
        Property(name="synccharts_Expression10", type=synccharts_Emission, multiplicity=Multiplicity(1, 1)),
        Property(name="synccharts_Emission9", type=synccharts_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
states11: BinaryAssociation = BinaryAssociation(
    name="states11",
    ends={
        Property(name="State", type=synccharts_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="parentRegion", type=synccharts_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentState12: BinaryAssociation = BinaryAssociation(
    name="parentState12",
    ends={
        Property(name="State13", type=synccharts_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="regions", type=synccharts_State, multiplicity=Multiplicity(0, 1))
    }
)
parentScope14: BinaryAssociation = BinaryAssociation(
    name="parentScope14",
    ends={
        Property(name="Scope", type=synccharts_Substitution, multiplicity=Multiplicity(1, 1)),
        Property(name="renamings", type=synccharts_Scope, multiplicity=Multiplicity(1, 1))
    }
)
regions15: BinaryAssociation = BinaryAssociation(
    name="regions15",
    ends={
        Property(name="Region", type=synccharts_State, multiplicity=Multiplicity(1, 1)),
        Property(name="parentState", type=synccharts_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentRegion16: BinaryAssociation = BinaryAssociation(
    name="parentRegion16",
    ends={
        Property(name="Region17", type=synccharts_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=synccharts_Region, multiplicity=Multiplicity(1, 1))
    }
)
variables27: BinaryAssociation = BinaryAssociation(
    name="variables27",
    ends={
        Property(name="synccharts_Variable29", type=synccharts_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="synccharts_Scope28", type=synccharts_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
suspensionTrigger30: BinaryAssociation = BinaryAssociation(
    name="suspensionTrigger30",
    ends={
        Property(name="synccharts_Action32", type=synccharts_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="synccharts_Scope31", type=synccharts_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exitActions33: BinaryAssociation = BinaryAssociation(
    name="exitActions33",
    ends={
        Property(name="synccharts_Action35", type=synccharts_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="synccharts_Scope34", type=synccharts_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransitions19: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions19",
    ends={
        Property(name="Transition20", type=synccharts_State, multiplicity=Multiplicity(1, 1)),
        Property(name="targetState", type=synccharts_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
targetState21: BinaryAssociation = BinaryAssociation(
    name="targetState21",
    ends={
        Property(name="State22", type=synccharts_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=synccharts_State, multiplicity=Multiplicity(1, 1))
    }
)
sourceState23: BinaryAssociation = BinaryAssociation(
    name="sourceState23",
    ends={
        Property(name="State24", type=synccharts_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=synccharts_State, multiplicity=Multiplicity(1, 1))
    }
)
signals25: BinaryAssociation = BinaryAssociation(
    name="signals25",
    ends={
        Property(name="synccharts_Signal26", type=synccharts_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="synccharts_Scope", type=synccharts_Signal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerActions36: BinaryAssociation = BinaryAssociation(
    name="innerActions36",
    ends={
        Property(name="synccharts_Action38", type=synccharts_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="synccharts_Scope37", type=synccharts_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entryActions39: BinaryAssociation = BinaryAssociation(
    name="entryActions39",
    ends={
        Property(name="synccharts_Action41", type=synccharts_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="synccharts_Scope40", type=synccharts_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyReference42: BinaryAssociation = BinaryAssociation(
    name="bodyReference42",
    ends={
        Property(name="synccharts_EObject", type=synccharts_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="synccharts_Scope43", type=synccharts_EObject, multiplicity=Multiplicity(0, 1))
    }
)
bodyContents44: BinaryAssociation = BinaryAssociation(
    name="bodyContents44",
    ends={
        Property(name="synccharts_EObject46", type=synccharts_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="synccharts_Scope45", type=synccharts_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyText47: BinaryAssociation = BinaryAssociation(
    name="bodyText47",
    ends={
        Property(name="synccharts_TextualCode", type=synccharts_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="synccharts_Scope48", type=synccharts_TextualCode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
renamings49: BinaryAssociation = BinaryAssociation(
    name="renamings49",
    ends={
        Property(name="Substitution", type=synccharts_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="parentScope", type=synccharts_Substitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_synccharts_Assignment_Effect = Generalization(general=Effect, specific=synccharts_Assignment)
gen_synccharts_Action_Annotatable = Generalization(general=Annotatable, specific=synccharts_Action)
gen_synccharts_Emission_Effect = Generalization(general=Effect, specific=synccharts_Emission)
gen_synccharts_Region_Scope = Generalization(general=Scope, specific=synccharts_Region)
gen_synccharts_State_Scope = Generalization(general=Scope, specific=synccharts_State)
gen_synccharts_Transition_Action = Generalization(general=Action, specific=synccharts_Transition)
gen_synccharts_Scope_Annotatable = Generalization(general=Annotatable, specific=synccharts_Scope)
gen_synccharts_TextEffect_TextualCode = Generalization(general=TextualCode, specific=synccharts_TextEffect)
gen_synccharts_TextEffect_Effect = Generalization(general=Effect, specific=synccharts_TextEffect)

# Domain Model
domain_model = DomainModel(
    name="synccharts",
    types={synccharts_Assignment, Effect, synccharts_Action, Annotatable, synccharts_Effect, synccharts_Expression, synccharts_Transition, synccharts_Variable, synccharts_Emission, synccharts_Signal, synccharts_Region, Scope, synccharts_State, synccharts_Substitution, synccharts_Scope, Action, synccharts_EObject, synccharts_TextualCode, synccharts_TextEffect, TextualCode, StateType, TransitionType},
    associations={effects0, trigger1, outgoingTransitions18, variable3, expression4, signal7, newValue8, states11, parentState12, parentScope14, regions15, parentRegion16, variables27, suspensionTrigger30, exitActions33, incomingTransitions19, targetState21, sourceState23, signals25, innerActions36, entryActions39, bodyReference42, bodyContents44, bodyText47, renamings49},
    generalizations={gen_synccharts_Assignment_Effect, gen_synccharts_Action_Annotatable, gen_synccharts_Emission_Effect, gen_synccharts_Region_Scope, gen_synccharts_State_Scope, gen_synccharts_Transition_Action, gen_synccharts_Scope_Annotatable, gen_synccharts_TextEffect_TextualCode, gen_synccharts_TextEffect_Effect},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)