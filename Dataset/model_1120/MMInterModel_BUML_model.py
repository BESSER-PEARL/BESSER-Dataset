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
MMInterModel_Transition = Class(name="MMInterModel::Transition")
MMInterModel_State = Class(name="MMInterModel::State")
MMInterModel_Element = Class(name="MMInterModel::Element")
MMInterModel_Model = Class(name="MMInterModel::Model")
Element = Class(name="Element")
MMInterModel_Component = Class(name="MMInterModel::Component")
MMInterModel_Attribute = Class(name="MMInterModel::Attribute")
MMInterModel_Event = Class(name="MMInterModel::Event")
MMInterModel_StateConfiguration = Class(name="MMInterModel::StateConfiguration")
MMInterModel_StateMachine = Class(name="MMInterModel::StateMachine")
MMInterModel_StringEnumeration = Class(name="MMInterModel::StringEnumeration")
MMInterModel_Guard = Class(name="MMInterModel::Guard")

# MMInterModel_Transition class attributes and methods
MMInterModel_Transition_action: Property = Property(name="action", type=StringType)
MMInterModel_Transition_stateMachine: Property = Property(name="stateMachine", type=StringType)
MMInterModel_Transition.attributes={MMInterModel_Transition_action, MMInterModel_Transition_stateMachine}

# MMInterModel_State class attributes and methods
MMInterModel_State_duringBehaviour: Property = Property(name="duringBehaviour", type=StringType)
MMInterModel_State_entryBehaviour: Property = Property(name="entryBehaviour", type=StringType)
MMInterModel_State_exitBehaviour: Property = Property(name="exitBehaviour", type=StringType)
MMInterModel_State_stateMachine: Property = Property(name="stateMachine", type=StringType)
MMInterModel_State_stateConfiguration: Property = Property(name="stateConfiguration", type=StringType)
MMInterModel_State_stateNumber: Property = Property(name="stateNumber", type=IntegerType)
MMInterModel_State.attributes={MMInterModel_State_stateConfiguration, MMInterModel_State_stateNumber, MMInterModel_State_duringBehaviour, MMInterModel_State_exitBehaviour, MMInterModel_State_entryBehaviour, MMInterModel_State_stateMachine}

# MMInterModel_Element class attributes and methods
MMInterModel_Element_name: Property = Property(name="name", type=StringType)
MMInterModel_Element_id: Property = Property(name="id", type=StringType)
MMInterModel_Element.attributes={MMInterModel_Element_id, MMInterModel_Element_name}

# MMInterModel_Model class attributes and methods

# Element class attributes and methods

# MMInterModel_Component class attributes and methods
MMInterModel_Component_numberOfSpares: Property = Property(name="numberOfSpares", type=IntegerType)
MMInterModel_Component_model: Property = Property(name="model", type=StringType)
MMInterModel_Component.attributes={MMInterModel_Component_model, MMInterModel_Component_numberOfSpares}

# MMInterModel_Attribute class attributes and methods
MMInterModel_Attribute_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
MMInterModel_Attribute_upperBound: Property = Property(name="upperBound", type=IntegerType)
MMInterModel_Attribute_type: Property = Property(name="type", type=StringType)
MMInterModel_Attribute_isArray: Property = Property(name="isArray", type=BooleanType)
MMInterModel_Attribute_arraySize: Property = Property(name="arraySize", type=IntegerType)
MMInterModel_Attribute_defaultValue: Property = Property(name="defaultValue", type=StringType)
MMInterModel_Attribute_model: Property = Property(name="model", type=StringType)
MMInterModel_Attribute_component: Property = Property(name="component", type=StringType)
MMInterModel_Attribute.attributes={MMInterModel_Attribute_defaultValue, MMInterModel_Attribute_type, MMInterModel_Attribute_lowerBound, MMInterModel_Attribute_component, MMInterModel_Attribute_arraySize, MMInterModel_Attribute_isArray, MMInterModel_Attribute_upperBound, MMInterModel_Attribute_model}

# MMInterModel_Event class attributes and methods
MMInterModel_Event_type: Property = Property(name="type", type=StringType)
MMInterModel_Event_model: Property = Property(name="model", type=StringType)
MMInterModel_Event.attributes={MMInterModel_Event_model, MMInterModel_Event_type}

# MMInterModel_StateConfiguration class attributes and methods
MMInterModel_StateConfiguration_configOperator: Property = Property(name="configOperator", type=StringType)
MMInterModel_StateConfiguration_condition: Property = Property(name="condition", type=StringType)
MMInterModel_StateConfiguration_negation: Property = Property(name="negation", type=BooleanType)
MMInterModel_StateConfiguration_model: Property = Property(name="model", type=StringType)
MMInterModel_StateConfiguration.attributes={MMInterModel_StateConfiguration_configOperator, MMInterModel_StateConfiguration_negation, MMInterModel_StateConfiguration_condition, MMInterModel_StateConfiguration_model}

# MMInterModel_StateMachine class attributes and methods
MMInterModel_StateMachine_type: Property = Property(name="type", type=StringType)
MMInterModel_StateMachine_superState: Property = Property(name="superState", type=StringType)
MMInterModel_StateMachine_component: Property = Property(name="component", type=StringType)
MMInterModel_StateMachine.attributes={MMInterModel_StateMachine_superState, MMInterModel_StateMachine_component, MMInterModel_StateMachine_type}

# MMInterModel_StringEnumeration class attributes and methods
MMInterModel_StringEnumeration_attribute: Property = Property(name="attribute", type=StringType)
MMInterModel_StringEnumeration.attributes={MMInterModel_StringEnumeration_attribute}

# MMInterModel_Guard class attributes and methods
MMInterModel_Guard_specification: Property = Property(name="specification", type=StringType)
MMInterModel_Guard_transition: Property = Property(name="transition", type=StringType)
MMInterModel_Guard.attributes={MMInterModel_Guard_specification, MMInterModel_Guard_transition}

# Relationships
transitions15: BinaryAssociation = BinaryAssociation(
    name="transitions15",
    ends={
        Property(name="MMInterModel_Transition", type=MMInterModel_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="MMInterModel_StateMachine16", type=MMInterModel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states17: BinaryAssociation = BinaryAssociation(
    name="states17",
    ends={
        Property(name="MMInterModel_State", type=MMInterModel_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="MMInterModel_StateMachine18", type=MMInterModel_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState19: BinaryAssociation = BinaryAssociation(
    name="initialState19",
    ends={
        Property(name="MMInterModel_State21", type=MMInterModel_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="MMInterModel_StateMachine20", type=MMInterModel_State, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
components0: BinaryAssociation = BinaryAssociation(
    name="components0",
    ends={
        Property(name="MMInterModel_Component", type=MMInterModel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="MMInterModel_Model", type=MMInterModel_Component, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
globalVariables1: BinaryAssociation = BinaryAssociation(
    name="globalVariables1",
    ends={
        Property(name="MMInterModel_Attribute", type=MMInterModel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="MMInterModel_Model2", type=MMInterModel_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events3: BinaryAssociation = BinaryAssociation(
    name="events3",
    ends={
        Property(name="MMInterModel_Event", type=MMInterModel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="MMInterModel_Model4", type=MMInterModel_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateConfigurations5: BinaryAssociation = BinaryAssociation(
    name="stateConfigurations5",
    ends={
        Property(name="MMInterModel_StateConfiguration", type=MMInterModel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="MMInterModel_Model6", type=MMInterModel_StateConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
normalBehaviour7: BinaryAssociation = BinaryAssociation(
    name="normalBehaviour7",
    ends={
        Property(name="MMInterModel_StateMachine", type=MMInterModel_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="MMInterModel_Component8", type=MMInterModel_StateMachine, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localVariables9: BinaryAssociation = BinaryAssociation(
    name="localVariables9",
    ends={
        Property(name="MMInterModel_Attribute11", type=MMInterModel_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="MMInterModel_Component10", type=MMInterModel_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failurePatterns12: BinaryAssociation = BinaryAssociation(
    name="failurePatterns12",
    ends={
        Property(name="MMInterModel_StateMachine14", type=MMInterModel_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="MMInterModel_Component13", type=MMInterModel_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumerationLiterals42: BinaryAssociation = BinaryAssociation(
    name="enumerationLiterals42",
    ends={
        Property(name="MMInterModel_StringEnumeration", type=MMInterModel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="MMInterModel_Attribute43", type=MMInterModel_StringEnumeration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source22: BinaryAssociation = BinaryAssociation(
    name="source22",
    ends={
        Property(name="MMInterModel_State24", type=MMInterModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="MMInterModel_Transition23", type=MMInterModel_State, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target25: BinaryAssociation = BinaryAssociation(
    name="target25",
    ends={
        Property(name="MMInterModel_State27", type=MMInterModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="MMInterModel_Transition26", type=MMInterModel_State, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
event28: BinaryAssociation = BinaryAssociation(
    name="event28",
    ends={
        Property(name="MMInterModel_Event30", type=MMInterModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="MMInterModel_Transition29", type=MMInterModel_Event, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard31: BinaryAssociation = BinaryAssociation(
    name="guard31",
    ends={
        Property(name="MMInterModel_Guard", type=MMInterModel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="MMInterModel_Transition32", type=MMInterModel_Guard, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incomingTransitions33: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions33",
    ends={
        Property(name="MMInterModel_Transition35", type=MMInterModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="MMInterModel_State34", type=MMInterModel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingTransitions36: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions36",
    ends={
        Property(name="MMInterModel_Transition38", type=MMInterModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="MMInterModel_State37", type=MMInterModel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subMachines39: BinaryAssociation = BinaryAssociation(
    name="subMachines39",
    ends={
        Property(name="MMInterModel_StateMachine41", type=MMInterModel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="MMInterModel_State40", type=MMInterModel_StateMachine, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transitionsTriggeredByEvent44: BinaryAssociation = BinaryAssociation(
    name="transitionsTriggeredByEvent44",
    ends={
        Property(name="MMInterModel_Transition46", type=MMInterModel_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="MMInterModel_Event45", type=MMInterModel_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
configurationStates47: BinaryAssociation = BinaryAssociation(
    name="configurationStates47",
    ends={
        Property(name="MMInterModel_State49", type=MMInterModel_StateConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="MMInterModel_StateConfiguration48", type=MMInterModel_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subConfigurations51: BinaryAssociation = BinaryAssociation(
    name="subConfigurations51",
    ends={
        Property(name="MMInterModel_StateConfiguration52", type=MMInterModel_StateConfiguration, multiplicity=Multiplicity(1, 1)),
        Property(name="MMInterModel_StateConfiguration50", type=MMInterModel_StateConfiguration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_MMInterModel_StateMachine_Element = Generalization(general=Element, specific=MMInterModel_StateMachine)
gen_MMInterModel_Model_Element = Generalization(general=Element, specific=MMInterModel_Model)
gen_MMInterModel_Component_Element = Generalization(general=Element, specific=MMInterModel_Component)
gen_MMInterModel_Transition_Element = Generalization(general=Element, specific=MMInterModel_Transition)
gen_MMInterModel_State_Element = Generalization(general=Element, specific=MMInterModel_State)
gen_MMInterModel_Attribute_Element = Generalization(general=Element, specific=MMInterModel_Attribute)
gen_MMInterModel_StringEnumeration_Element = Generalization(general=Element, specific=MMInterModel_StringEnumeration)
gen_MMInterModel_Event_Element = Generalization(general=Element, specific=MMInterModel_Event)
gen_MMInterModel_StateConfiguration_Element = Generalization(general=Element, specific=MMInterModel_StateConfiguration)
gen_MMInterModel_Guard_Element = Generalization(general=Element, specific=MMInterModel_Guard)

# Domain Model
domain_model = DomainModel(
    name="MMInterModel",
    types={MMInterModel_Transition, MMInterModel_State, MMInterModel_Element, MMInterModel_Model, Element, MMInterModel_Component, MMInterModel_Attribute, MMInterModel_Event, MMInterModel_StateConfiguration, MMInterModel_StateMachine, MMInterModel_StringEnumeration, MMInterModel_Guard},
    associations={transitions15, states17, initialState19, components0, globalVariables1, events3, stateConfigurations5, normalBehaviour7, localVariables9, failurePatterns12, enumerationLiterals42, source22, target25, event28, guard31, incomingTransitions33, outgoingTransitions36, subMachines39, transitionsTriggeredByEvent44, configurationStates47, subConfigurations51},
    generalizations={gen_MMInterModel_StateMachine_Element, gen_MMInterModel_Model_Element, gen_MMInterModel_Component_Element, gen_MMInterModel_Transition_Element, gen_MMInterModel_State_Element, gen_MMInterModel_Attribute_Element, gen_MMInterModel_StringEnumeration_Element, gen_MMInterModel_Event_Element, gen_MMInterModel_StateConfiguration_Element, gen_MMInterModel_Guard_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)