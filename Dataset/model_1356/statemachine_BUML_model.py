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
ActionKind: Enumeration = Enumeration(
    name="ActionKind",
    literals={
            EnumerationLiteral(name="ENTRY"),
			EnumerationLiteral(name="EXIT")
    }
)

# Classes
statemachine_Named = Class(name="statemachine::Named")
statemachine_GAbstractState = Class(name="statemachine::GAbstractState", is_abstract=True)
statemachine_GAbstractAction = Class(name="statemachine::GAbstractAction", is_abstract=True)
statemachine_GState = Class(name="statemachine::GState")
Named = Class(name="Named")
GAbstractState = Class(name="GAbstractState")
statemachine_Transition = Class(name="statemachine::Transition")
statemachine_Value = Class(name="statemachine::Value", is_abstract=True)
statemachine_GCompositeState = Class(name="statemachine::GCompositeState")
GState = Class(name="GState")
statemachine_GStartState = Class(name="statemachine::GStartState")
statemachine_GStopState = Class(name="statemachine::GStopState")
statemachine_GStatemachine = Class(name="statemachine::GStatemachine")
GCompositeState = Class(name="GCompositeState")
ConstantValue = Class(name="ConstantValue")
statemachine_NumberValue = Class(name="statemachine::NumberValue", is_abstract=True)
statemachine_Parameter = Class(name="statemachine::Parameter")
statemachine_CallAction = Class(name="statemachine::CallAction")
GAbstractAction = Class(name="GAbstractAction")
statemachine_Call = Class(name="statemachine::Call")
statemachine_GetParameter = Class(name="statemachine::GetParameter")
Value = Class(name="Value")
statemachine_ConstantValue = Class(name="statemachine::ConstantValue", is_abstract=True)
statemachine_StringValue = Class(name="statemachine::StringValue")
statemachine_BooleanValue = Class(name="statemachine::BooleanValue")
statemachine_LongValue = Class(name="statemachine::LongValue")
NumberValue = Class(name="NumberValue")

# statemachine_Named class attributes and methods
statemachine_Named_name: Property = Property(name="name", type=StringType)
statemachine_Named_comment: Property = Property(name="comment", type=StringType)
statemachine_Named.attributes={statemachine_Named_comment, statemachine_Named_name}

# statemachine_GAbstractState class attributes and methods

# statemachine_GAbstractAction class attributes and methods
statemachine_GAbstractAction_kind: Property = Property(name="kind", type=StringType)
statemachine_GAbstractAction.attributes={statemachine_GAbstractAction_kind}

# statemachine_GState class attributes and methods

# Named class attributes and methods

# GAbstractState class attributes and methods

# statemachine_Transition class attributes and methods
statemachine_Transition_preserveTimers: Property = Property(name="preserveTimers", type=BooleanType)
statemachine_Transition.attributes={statemachine_Transition_preserveTimers}

# statemachine_Value class attributes and methods

# statemachine_GCompositeState class attributes and methods

# GState class attributes and methods

# statemachine_GStartState class attributes and methods

# statemachine_GStopState class attributes and methods

# statemachine_GStatemachine class attributes and methods
statemachine_GStatemachine_package: Property = Property(name="package", type=StringType)
statemachine_GStatemachine.attributes={statemachine_GStatemachine_package}

# GCompositeState class attributes and methods

# ConstantValue class attributes and methods

# statemachine_NumberValue class attributes and methods

# statemachine_Parameter class attributes and methods

# statemachine_CallAction class attributes and methods

# GAbstractAction class attributes and methods

# statemachine_Call class attributes and methods
statemachine_Call_actionId: Property = Property(name="actionId", type=StringType)
statemachine_Call.attributes={statemachine_Call_actionId}

# statemachine_GetParameter class attributes and methods

# Value class attributes and methods

# statemachine_ConstantValue class attributes and methods
statemachine_ConstantValue_value: Property = Property(name="value", type=StringType)
statemachine_ConstantValue.attributes={statemachine_ConstantValue_value}

# statemachine_StringValue class attributes and methods

# statemachine_BooleanValue class attributes and methods

# statemachine_LongValue class attributes and methods

# NumberValue class attributes and methods

# Relationships
to3: BinaryAssociation = BinaryAssociation(
    name="to3",
    ends={
        Property(name="statemachine_GAbstractState5", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition4", type=statemachine_GAbstractState, multiplicity=Multiplicity(0, 1))
    }
)
actions0: BinaryAssociation = BinaryAssociation(
    name="actions0",
    ends={
        Property(name="statemachine_GAbstractAction", type=statemachine_GAbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_GAbstractState", type=statemachine_GAbstractAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from1: BinaryAssociation = BinaryAssociation(
    name="from1",
    ends={
        Property(name="statemachine_GAbstractState2", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition", type=statemachine_GAbstractState, multiplicity=Multiplicity(0, 1))
    }
)
guard6: BinaryAssociation = BinaryAssociation(
    name="guard6",
    ends={
        Property(name="statemachine_Value", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition7", type=statemachine_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
delay8: BinaryAssociation = BinaryAssociation(
    name="delay8",
    ends={
        Property(name="statemachine_Value10", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition9", type=statemachine_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
signals11: BinaryAssociation = BinaryAssociation(
    name="signals11",
    ends={
        Property(name="statemachine_Value13", type=statemachine_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_Transition12", type=statemachine_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states14: BinaryAssociation = BinaryAssociation(
    name="states14",
    ends={
        Property(name="statemachine_GAbstractState15", type=statemachine_GCompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_GCompositeState", type=statemachine_GAbstractState, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transitions16: BinaryAssociation = BinaryAssociation(
    name="transitions16",
    ends={
        Property(name="statemachine_Transition18", type=statemachine_GCompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_GCompositeState17", type=statemachine_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter19: BinaryAssociation = BinaryAssociation(
    name="parameter19",
    ends={
        Property(name="statemachine_Parameter", type=statemachine_GStatemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_GStatemachine", type=statemachine_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
call20: BinaryAssociation = BinaryAssociation(
    name="call20",
    ends={
        Property(name="statemachine_Call", type=statemachine_CallAction, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_CallAction", type=statemachine_Call, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter21: BinaryAssociation = BinaryAssociation(
    name="parameter21",
    ends={
        Property(name="statemachine_Parameter22", type=statemachine_GetParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="statemachine_GetParameter", type=statemachine_Parameter, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_statemachine_GState_Named = Generalization(general=Named, specific=statemachine_GState)
gen_statemachine_GState_GAbstractState = Generalization(general=GAbstractState, specific=statemachine_GState)
gen_statemachine_Transition_Named = Generalization(general=Named, specific=statemachine_Transition)
gen_statemachine_GCompositeState_GState = Generalization(general=GState, specific=statemachine_GCompositeState)
gen_statemachine_GStartState_GAbstractState = Generalization(general=GAbstractState, specific=statemachine_GStartState)
gen_statemachine_GStopState_GAbstractState = Generalization(general=GAbstractState, specific=statemachine_GStopState)
gen_statemachine_GStatemachine_GCompositeState = Generalization(general=GCompositeState, specific=statemachine_GStatemachine)
gen_statemachine_StringValue_ConstantValue = Generalization(general=ConstantValue, specific=statemachine_StringValue)
gen_statemachine_NumberValue_ConstantValue = Generalization(general=ConstantValue, specific=statemachine_NumberValue)
gen_statemachine_CallAction_GAbstractAction = Generalization(general=GAbstractAction, specific=statemachine_CallAction)
gen_statemachine_Parameter_Named = Generalization(general=Named, specific=statemachine_Parameter)
gen_statemachine_GetParameter_Value = Generalization(general=Value, specific=statemachine_GetParameter)
gen_statemachine_Call_Value = Generalization(general=Value, specific=statemachine_Call)
gen_statemachine_ConstantValue_Value = Generalization(general=Value, specific=statemachine_ConstantValue)
gen_statemachine_BooleanValue_ConstantValue = Generalization(general=ConstantValue, specific=statemachine_BooleanValue)
gen_statemachine_LongValue_NumberValue = Generalization(general=NumberValue, specific=statemachine_LongValue)

# Domain Model
domain_model = DomainModel(
    name="statemachine",
    types={statemachine_Named, statemachine_GAbstractState, statemachine_GAbstractAction, statemachine_GState, Named, GAbstractState, statemachine_Transition, statemachine_Value, statemachine_GCompositeState, GState, statemachine_GStartState, statemachine_GStopState, statemachine_GStatemachine, GCompositeState, ConstantValue, statemachine_NumberValue, statemachine_Parameter, statemachine_CallAction, GAbstractAction, statemachine_Call, statemachine_GetParameter, Value, statemachine_ConstantValue, statemachine_StringValue, statemachine_BooleanValue, statemachine_LongValue, NumberValue, ActionKind},
    associations={to3, actions0, from1, guard6, delay8, signals11, states14, transitions16, parameter19, call20, parameter21},
    generalizations={gen_statemachine_GState_Named, gen_statemachine_GState_GAbstractState, gen_statemachine_Transition_Named, gen_statemachine_GCompositeState_GState, gen_statemachine_GStartState_GAbstractState, gen_statemachine_GStopState_GAbstractState, gen_statemachine_GStatemachine_GCompositeState, gen_statemachine_StringValue_ConstantValue, gen_statemachine_NumberValue_ConstantValue, gen_statemachine_CallAction_GAbstractAction, gen_statemachine_Parameter_Named, gen_statemachine_GetParameter_Value, gen_statemachine_Call_Value, gen_statemachine_ConstantValue_Value, gen_statemachine_BooleanValue_ConstantValue, gen_statemachine_LongValue_NumberValue},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)