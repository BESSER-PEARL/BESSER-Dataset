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
Operator: Enumeration = Enumeration(
    name="Operator",
    literals={
            EnumerationLiteral(name="add"),
			EnumerationLiteral(name="sub"),
			EnumerationLiteral(name="eq"),
			EnumerationLiteral(name="mul"),
			EnumerationLiteral(name="gt"),
			EnumerationLiteral(name="lt"),
			EnumerationLiteral(name="lte"),
			EnumerationLiteral(name="gte"),
			EnumerationLiteral(name="div"),
			EnumerationLiteral(name="and"),
			EnumerationLiteral(name="neq"),
			EnumerationLiteral(name="or"),
			EnumerationLiteral(name="not")
    }
)

# Classes
State = Class(name="State")
SimplStateMachine_StateMachine = Class(name="SimplStateMachine::StateMachine")
CompositeState = Class(name="CompositeState")
SimplStateMachine_Transition = Class(name="SimplStateMachine::Transition")
SimplStateMachine_Event = Class(name="SimplStateMachine::Event")
SimplStateMachine_Variable = Class(name="SimplStateMachine::Variable", is_abstract=True)
SimplStateMachine_State = Class(name="SimplStateMachine::State")
SimplStateMachine_CompositeState = Class(name="SimplStateMachine::CompositeState")
SimplStateMachine_Operation = Class(name="SimplStateMachine::Operation")
SimplStateMachine_InitialState = Class(name="SimplStateMachine::InitialState")
SimplStateMachine_Expression = Class(name="SimplStateMachine::Expression")
SimplStateMachine_ExpressionElement = Class(name="SimplStateMachine::ExpressionElement", is_abstract=True)
ExpressionElement = Class(name="ExpressionElement")
SimplStateMachine_Data = Class(name="SimplStateMachine::Data", is_abstract=True)
SimplStateMachine_BooleanData = Class(name="SimplStateMachine::BooleanData")
Data = Class(name="Data")
SimplStateMachine_IntegerData = Class(name="SimplStateMachine::IntegerData")
SimplStateMachine_BooleanVariable = Class(name="SimplStateMachine::BooleanVariable")
Variable = Class(name="Variable")
SimplStateMachine_IntegerVariable = Class(name="SimplStateMachine::IntegerVariable")
SimplStateMachine_Assignment = Class(name="SimplStateMachine::Assignment")
SimplStateMachine_VariableReference = Class(name="SimplStateMachine::VariableReference")

# State class attributes and methods

# SimplStateMachine_StateMachine class attributes and methods

# CompositeState class attributes and methods

# SimplStateMachine_Transition class attributes and methods

# SimplStateMachine_Event class attributes and methods
SimplStateMachine_Event_name: Property = Property(name="name", type=StringType)
SimplStateMachine_Event.attributes={SimplStateMachine_Event_name}

# SimplStateMachine_Variable class attributes and methods
SimplStateMachine_Variable_name: Property = Property(name="name", type=StringType)
SimplStateMachine_Variable.attributes={SimplStateMachine_Variable_name}

# SimplStateMachine_State class attributes and methods
SimplStateMachine_State_name: Property = Property(name="name", type=StringType)
SimplStateMachine_State_isActive: Property = Property(name="isActive", type=BooleanType)
SimplStateMachine_State.attributes={SimplStateMachine_State_isActive, SimplStateMachine_State_name}

# SimplStateMachine_CompositeState class attributes and methods
SimplStateMachine_CompositeState_m_activeSubTree: Method = Method(name="activeSubTree", parameters={}, type=BooleanType)
SimplStateMachine_CompositeState_m_unactiveSubTree: Method = Method(name="unactiveSubTree", parameters={}, type=BooleanType)
SimplStateMachine_CompositeState.methods={SimplStateMachine_CompositeState_m_unactiveSubTree, SimplStateMachine_CompositeState_m_activeSubTree}

# SimplStateMachine_Operation class attributes and methods

# SimplStateMachine_InitialState class attributes and methods

# SimplStateMachine_Expression class attributes and methods
SimplStateMachine_Expression__name: Property = Property(name="_name", type=StringType)
SimplStateMachine_Expression_operator: Property = Property(name="operator", type=StringType)
SimplStateMachine_Expression.attributes={SimplStateMachine_Expression_operator, SimplStateMachine_Expression__name}

# SimplStateMachine_ExpressionElement class attributes and methods

# ExpressionElement class attributes and methods

# SimplStateMachine_Data class attributes and methods

# SimplStateMachine_BooleanData class attributes and methods
SimplStateMachine_BooleanData_value: Property = Property(name="value", type=BooleanType)
SimplStateMachine_BooleanData.attributes={SimplStateMachine_BooleanData_value}

# Data class attributes and methods

# SimplStateMachine_IntegerData class attributes and methods
SimplStateMachine_IntegerData_value: Property = Property(name="value", type=IntegerType)
SimplStateMachine_IntegerData.attributes={SimplStateMachine_IntegerData_value}

# SimplStateMachine_BooleanVariable class attributes and methods

# Variable class attributes and methods

# SimplStateMachine_IntegerVariable class attributes and methods

# SimplStateMachine_Assignment class attributes and methods
SimplStateMachine_Assignment__name: Property = Property(name="_name", type=StringType)
SimplStateMachine_Assignment.attributes={SimplStateMachine_Assignment__name}

# SimplStateMachine_VariableReference class attributes and methods
SimplStateMachine_VariableReference__name: Property = Property(name="_name", type=StringType)
SimplStateMachine_VariableReference.attributes={SimplStateMachine_VariableReference__name}

# Relationships
transitions0: BinaryAssociation = BinaryAssociation(
    name="transitions0",
    ends={
        Property(name="SimplStateMachine_Transition", type=SimplStateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachine_StateMachine", type=SimplStateMachine_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
events1: BinaryAssociation = BinaryAssociation(
    name="events1",
    ends={
        Property(name="SimplStateMachine_Event", type=SimplStateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachine_StateMachine2", type=SimplStateMachine_Event, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variables3: BinaryAssociation = BinaryAssociation(
    name="variables3",
    ends={
        Property(name="SimplStateMachine_Variable", type=SimplStateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachine_StateMachine4", type=SimplStateMachine_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container5: BinaryAssociation = BinaryAssociation(
    name="container5",
    ends={
        Property(name="CompositeState", type=SimplStateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=SimplStateMachine_CompositeState, multiplicity=Multiplicity(0, 1))
    }
)
operation6: BinaryAssociation = BinaryAssociation(
    name="operation6",
    ends={
        Property(name="SimplStateMachine_Operation", type=SimplStateMachine_State, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachine_State", type=SimplStateMachine_Operation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
states7: BinaryAssociation = BinaryAssociation(
    name="states7",
    ends={
        Property(name="State", type=SimplStateMachine_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=SimplStateMachine_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initialState8: BinaryAssociation = BinaryAssociation(
    name="initialState8",
    ends={
        Property(name="SimplStateMachine_InitialState", type=SimplStateMachine_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachine_CompositeState", type=SimplStateMachine_InitialState, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referencedState9: BinaryAssociation = BinaryAssociation(
    name="referencedState9",
    ends={
        Property(name="SimplStateMachine_State11", type=SimplStateMachine_InitialState, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachine_InitialState10", type=SimplStateMachine_State, multiplicity=Multiplicity(1, 1))
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="SimplStateMachine_State14", type=SimplStateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachine_Transition13", type=SimplStateMachine_State, multiplicity=Multiplicity(1, 1))
    }
)
target15: BinaryAssociation = BinaryAssociation(
    name="target15",
    ends={
        Property(name="SimplStateMachine_State17", type=SimplStateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachine_Transition16", type=SimplStateMachine_State, multiplicity=Multiplicity(1, 1))
    }
)
event18: BinaryAssociation = BinaryAssociation(
    name="event18",
    ends={
        Property(name="SimplStateMachine_Event20", type=SimplStateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachine_Transition19", type=SimplStateMachine_Event, multiplicity=Multiplicity(1, 1))
    }
)
guard21: BinaryAssociation = BinaryAssociation(
    name="guard21",
    ends={
        Property(name="SimplStateMachine_Expression", type=SimplStateMachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachine_Transition22", type=SimplStateMachine_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left23: BinaryAssociation = BinaryAssociation(
    name="left23",
    ends={
        Property(name="SimplStateMachine_ExpressionElement", type=SimplStateMachine_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachine_Expression24", type=SimplStateMachine_ExpressionElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right25: BinaryAssociation = BinaryAssociation(
    name="right25",
    ends={
        Property(name="SimplStateMachine_ExpressionElement27", type=SimplStateMachine_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachine_Expression26", type=SimplStateMachine_ExpressionElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value28: BinaryAssociation = BinaryAssociation(
    name="value28",
    ends={
        Property(name="SimplStateMachine_Data", type=SimplStateMachine_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachine_Variable29", type=SimplStateMachine_Data, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contents30: BinaryAssociation = BinaryAssociation(
    name="contents30",
    ends={
        Property(name="SimplStateMachine_Assignment", type=SimplStateMachine_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachine_Operation31", type=SimplStateMachine_Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression32: BinaryAssociation = BinaryAssociation(
    name="expression32",
    ends={
        Property(name="SimplStateMachine_ExpressionElement34", type=SimplStateMachine_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachine_Assignment33", type=SimplStateMachine_ExpressionElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable35: BinaryAssociation = BinaryAssociation(
    name="variable35",
    ends={
        Property(name="SimplStateMachine_Variable37", type=SimplStateMachine_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachine_Assignment36", type=SimplStateMachine_Variable, multiplicity=Multiplicity(1, 1))
    }
)
variable38: BinaryAssociation = BinaryAssociation(
    name="variable38",
    ends={
        Property(name="SimplStateMachine_Variable39", type=SimplStateMachine_VariableReference, multiplicity=Multiplicity(1, 1)),
        Property(name="SimplStateMachine_VariableReference", type=SimplStateMachine_Variable, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SimplStateMachine_CompositeState_State = Generalization(general=State, specific=SimplStateMachine_CompositeState)
gen_SimplStateMachine_StateMachine_CompositeState = Generalization(general=CompositeState, specific=SimplStateMachine_StateMachine)
gen_SimplStateMachine_Expression_ExpressionElement = Generalization(general=ExpressionElement, specific=SimplStateMachine_Expression)
gen_SimplStateMachine_Data_ExpressionElement = Generalization(general=ExpressionElement, specific=SimplStateMachine_Data)
gen_SimplStateMachine_BooleanData_Data = Generalization(general=Data, specific=SimplStateMachine_BooleanData)
gen_SimplStateMachine_IntegerData_Data = Generalization(general=Data, specific=SimplStateMachine_IntegerData)
gen_SimplStateMachine_BooleanVariable_Variable = Generalization(general=Variable, specific=SimplStateMachine_BooleanVariable)
gen_SimplStateMachine_IntegerVariable_Variable = Generalization(general=Variable, specific=SimplStateMachine_IntegerVariable)
gen_SimplStateMachine_VariableReference_ExpressionElement = Generalization(general=ExpressionElement, specific=SimplStateMachine_VariableReference)

# Domain Model
domain_model = DomainModel(
    name="SimplStateMachine",
    types={State, SimplStateMachine_StateMachine, CompositeState, SimplStateMachine_Transition, SimplStateMachine_Event, SimplStateMachine_Variable, SimplStateMachine_State, SimplStateMachine_CompositeState, SimplStateMachine_Operation, SimplStateMachine_InitialState, SimplStateMachine_Expression, SimplStateMachine_ExpressionElement, ExpressionElement, SimplStateMachine_Data, SimplStateMachine_BooleanData, Data, SimplStateMachine_IntegerData, SimplStateMachine_BooleanVariable, Variable, SimplStateMachine_IntegerVariable, SimplStateMachine_Assignment, SimplStateMachine_VariableReference, Operator},
    associations={transitions0, events1, variables3, container5, operation6, states7, initialState8, referencedState9, source12, target15, event18, guard21, left23, right25, value28, contents30, expression32, variable35, variable38},
    generalizations={gen_SimplStateMachine_CompositeState_State, gen_SimplStateMachine_StateMachine_CompositeState, gen_SimplStateMachine_Expression_ExpressionElement, gen_SimplStateMachine_Data_ExpressionElement, gen_SimplStateMachine_BooleanData_Data, gen_SimplStateMachine_IntegerData_Data, gen_SimplStateMachine_BooleanVariable_Variable, gen_SimplStateMachine_IntegerVariable_Variable, gen_SimplStateMachine_VariableReference_ExpressionElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)