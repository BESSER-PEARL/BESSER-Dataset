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
StateAttributeType: Enumeration = Enumeration(
    name="StateAttributeType",
    literals={
            EnumerationLiteral(name="null"),
			EnumerationLiteral(name="constant"),
			EnumerationLiteral(name="eventField"),
			EnumerationLiteral(name="location"),
			EnumerationLiteral(name="query")
    }
)

StateValueType: Enumeration = Enumeration(
    name="StateValueType",
    literals={
            EnumerationLiteral(name="string"),
			EnumerationLiteral(name="long"),
			EnumerationLiteral(name="eventField"),
			EnumerationLiteral(name="eventName"),
			EnumerationLiteral(name="delete"),
			EnumerationLiteral(name="query"),
			EnumerationLiteral(name="definedState"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="null")
    }
)

# Classes
statemachine_Statemachine = Class(name="statemachine::Statemachine")
Named = Class(name="Named")
statemachine_AbstractState = Class(name="statemachine::AbstractState", is_abstract=True)
statemachine_StateChange = Class(name="statemachine::StateChange")
statemachine_InitialState = Class(name="statemachine::InitialState")
AbstractState = Class(name="AbstractState")
statemachine_FinalState = Class(name="statemachine::FinalState")
statemachine_Named = Class(name="statemachine::Named")
statemachine_AbstractTransition = Class(name="statemachine::AbstractTransition", is_abstract=True)
statemachine_StateValue = Class(name="statemachine::StateValue")
statemachine_State = Class(name="statemachine::State")
statemachine_Transition = Class(name="statemachine::Transition")
AbstractTransition = Class(name="AbstractTransition")
statemachine_ConditionalTransition = Class(name="statemachine::ConditionalTransition")
statemachine_ConditionalState = Class(name="statemachine::ConditionalState")
statemachine_AbstractCondition = Class(name="statemachine::AbstractCondition")
statemachine_StateAttribute = Class(name="statemachine::StateAttribute")
statemachine_AttributeCondition = Class(name="statemachine::AttributeCondition")
statemachine_FieldCondition = Class(name="statemachine::FieldCondition")
AbstractCondition = Class(name="AbstractCondition")

# statemachine_Statemachine class attributes and methods
statemachine_Statemachine_associatedTree: Property = Property(name="associatedTree", type=StringType)
statemachine_Statemachine_associatedAttribute: Property = Property(name="associatedAttribute", type=StringType)
statemachine_Statemachine.attributes={statemachine_Statemachine_associatedTree, statemachine_Statemachine_associatedAttribute}

# Named class attributes and methods

# statemachine_AbstractState class attributes and methods

# statemachine_StateChange class attributes and methods

# statemachine_InitialState class attributes and methods

# AbstractState class attributes and methods

# statemachine_FinalState class attributes and methods

# statemachine_Named class attributes and methods
statemachine_Named_name: Property = Property(name="name", type=StringType)
statemachine_Named.attributes={statemachine_Named_name}

# statemachine_AbstractTransition class attributes and methods

# statemachine_StateValue class attributes and methods
statemachine_StateValue_type: Property = Property(name="type", type=StringType)
statemachine_StateValue_value: Property = Property(name="value", type=StringType)
statemachine_StateValue.attributes={statemachine_StateValue_type, statemachine_StateValue_value}

# statemachine_State class attributes and methods
statemachine_State_stateColor: Property = Property(name="stateColor", type=StringType)
statemachine_State.attributes={statemachine_State_stateColor}

# statemachine_Transition class attributes and methods

# AbstractTransition class attributes and methods

# statemachine_ConditionalTransition class attributes and methods

# statemachine_ConditionalState class attributes and methods
statemachine_ConditionalState_andExpression: Property = Property(name="andExpression", type=BooleanType)
statemachine_ConditionalState_conditionsOrganization: Property = Property(name="conditionsOrganization", type=StringType)
statemachine_ConditionalState.attributes={statemachine_ConditionalState_andExpression, statemachine_ConditionalState_conditionsOrganization}

# statemachine_AbstractCondition class attributes and methods
statemachine_AbstractCondition_isNotCondition: Property = Property(name="isNotCondition", type=BooleanType)
statemachine_AbstractCondition.attributes={statemachine_AbstractCondition_isNotCondition}

# statemachine_StateAttribute class attributes and methods
statemachine_StateAttribute_type: Property = Property(name="type", type=StringType)
statemachine_StateAttribute_value: Property = Property(name="value", type=StringType)
statemachine_StateAttribute.attributes={statemachine_StateAttribute_value, statemachine_StateAttribute_type}

# statemachine_AttributeCondition class attributes and methods

# statemachine_FieldCondition class attributes and methods
statemachine_FieldCondition_fieldName: Property = Property(name="fieldName", type=StringType)
statemachine_FieldCondition.attributes={statemachine_FieldCondition_fieldName}

# AbstractCondition class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="statemachine_AbstractState", type=statemachine_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Statemachine", type=statemachine_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state3: BinaryAssociation = BinaryAssociation(
    name="state3",
    ends={
        Property(name="statemachine_AbstractState5", type=statemachine_AbstractTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_AbstractTransition4", type=statemachine_AbstractState, multiplicity=Multiplicity(0, 1))
    }
)
stateChange6: BinaryAssociation = BinaryAssociation(
    name="stateChange6",
    ends={
        Property(name="statemachine_StateChange", type=statemachine_AbstractTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_AbstractTransition7", type=statemachine_StateChange, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="statemachine_AbstractTransition", type=statemachine_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_AbstractState2", type=statemachine_AbstractTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition10: BinaryAssociation = BinaryAssociation(
    name="condition10",
    ends={
        Property(name="statemachine_AbstractCondition", type=statemachine_ConditionalState, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_ConditionalState", type=statemachine_AbstractCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateAttribute11: BinaryAssociation = BinaryAssociation(
    name="stateAttribute11",
    ends={
        Property(name="statemachine_StateAttribute13", type=statemachine_StateChange, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateChange12", type=statemachine_StateAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateAttributeQuery9: BinaryAssociation = BinaryAssociation(
    name="stateAttributeQuery9",
    ends={
        Property(name="statemachine_StateAttribute", type=statemachine_StateAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateAttribute8", type=statemachine_StateAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateAttribute19: BinaryAssociation = BinaryAssociation(
    name="stateAttribute19",
    ends={
        Property(name="statemachine_StateAttribute20", type=statemachine_AttributeCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_AttributeCondition", type=statemachine_StateAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateValue14: BinaryAssociation = BinaryAssociation(
    name="stateValue14",
    ends={
        Property(name="statemachine_StateValue", type=statemachine_StateChange, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_StateChange15", type=statemachine_StateValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stateValue16: BinaryAssociation = BinaryAssociation(
    name="stateValue16",
    ends={
        Property(name="statemachine_StateValue18", type=statemachine_AbstractCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_AbstractCondition17", type=statemachine_StateValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_statemachine_Statemachine_Named = Generalization(general=Named, specific=statemachine_Statemachine)
gen_statemachine_InitialState_AbstractState = Generalization(general=AbstractState, specific=statemachine_InitialState)
gen_statemachine_FinalState_AbstractState = Generalization(general=AbstractState, specific=statemachine_FinalState)
gen_statemachine_AbstractState_Named = Generalization(general=Named, specific=statemachine_AbstractState)
gen_statemachine_AbstractTransition_Named = Generalization(general=Named, specific=statemachine_AbstractTransition)
gen_statemachine_State_AbstractState = Generalization(general=AbstractState, specific=statemachine_State)
gen_statemachine_Transition_AbstractTransition = Generalization(general=AbstractTransition, specific=statemachine_Transition)
gen_statemachine_ConditionalTransition_AbstractTransition = Generalization(general=AbstractTransition, specific=statemachine_ConditionalTransition)
gen_statemachine_ConditionalState_AbstractState = Generalization(general=AbstractState, specific=statemachine_ConditionalState)
gen_statemachine_AttributeCondition_AbstractCondition = Generalization(general=AbstractCondition, specific=statemachine_AttributeCondition)
gen_statemachine_FieldCondition_AbstractCondition = Generalization(general=AbstractCondition, specific=statemachine_FieldCondition)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_Statemachine, Named, statemachine_AbstractState, statemachine_StateChange, statemachine_InitialState, AbstractState, statemachine_FinalState, statemachine_Named, statemachine_AbstractTransition, statemachine_StateValue, statemachine_State, statemachine_Transition, AbstractTransition, statemachine_ConditionalTransition, statemachine_ConditionalState, statemachine_AbstractCondition, statemachine_StateAttribute, statemachine_AttributeCondition, statemachine_FieldCondition, AbstractCondition, StateAttributeType, StateValueType},
    associations={states0, state3, stateChange6, transitions1, condition10, stateAttribute11, stateAttributeQuery9, stateAttribute19, stateValue14, stateValue16},
    generalizations={gen_statemachine_Statemachine_Named, gen_statemachine_InitialState_AbstractState, gen_statemachine_FinalState_AbstractState, gen_statemachine_AbstractState_Named, gen_statemachine_AbstractTransition_Named, gen_statemachine_State_AbstractState, gen_statemachine_Transition_AbstractTransition, gen_statemachine_ConditionalTransition_AbstractTransition, gen_statemachine_ConditionalState_AbstractState, gen_statemachine_AttributeCondition_AbstractCondition, gen_statemachine_FieldCondition_AbstractCondition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)