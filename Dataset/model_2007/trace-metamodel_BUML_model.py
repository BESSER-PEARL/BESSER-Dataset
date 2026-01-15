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
ParamterKindEnum: Enumeration = Enumeration(
    name="ParamterKindEnum",
    literals={
            EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="INOUT"),
			EnumerationLiteral(name="OUT"),
			EnumerationLiteral(name="RETURN")
    }
)

# Classes
trace_Trace = Class(name="trace::Trace")
trace_Step = Class(name="trace::Step", is_abstract=True)
trace_ModelState = Class(name="trace::ModelState")
trace_ObjectState = Class(name="trace::ObjectState")
trace_TracedObject = Class(name="trace::TracedObject")
trace_Value = Class(name="trace::Value", is_abstract=True)
trace_ParameterValue = Class(name="trace::ParameterValue")
trace_BigStep = Class(name="trace::BigStep")
trace_RefValue = Class(name="trace::RefValue")
Value = Class(name="Value")
trace_LiteralValue = Class(name="trace::LiteralValue")
trace_SmallStep = Class(name="trace::SmallStep")
Step = Class(name="Step")

# trace_Trace class attributes and methods

# trace_Step class attributes and methods

# trace_ModelState class attributes and methods

# trace_ObjectState class attributes and methods

# trace_TracedObject class attributes and methods

# trace_Value class attributes and methods

# trace_ParameterValue class attributes and methods
trace_ParameterValue_DirectionKind: Property = Property(name="DirectionKind", type=StringType)
trace_ParameterValue.attributes={trace_ParameterValue_DirectionKind}

# trace_BigStep class attributes and methods

# trace_RefValue class attributes and methods

# Value class attributes and methods

# trace_LiteralValue class attributes and methods

# trace_SmallStep class attributes and methods

# Step class attributes and methods

# Relationships
steps0: BinaryAssociation = BinaryAssociation(
    name="steps0",
    ends={
        Property(name="trace_Step", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace", type=trace_Step, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelstate1: BinaryAssociation = BinaryAssociation(
    name="modelstate1",
    ends={
        Property(name="trace_ModelState", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace2", type=trace_ModelState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectstates3: BinaryAssociation = BinaryAssociation(
    name="objectstates3",
    ends={
        Property(name="trace_ObjectState", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace4", type=trace_ObjectState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tracedobject5: BinaryAssociation = BinaryAssociation(
    name="tracedobject5",
    ends={
        Property(name="trace_TracedObject", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace6", type=trace_TracedObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values7: BinaryAssociation = BinaryAssociation(
    name="values7",
    ends={
        Property(name="trace_Value", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace8", type=trace_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state9: BinaryAssociation = BinaryAssociation(
    name="state9",
    ends={
        Property(name="trace_ModelState11", type=trace_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Step10", type=trace_ModelState, multiplicity=Multiplicity(0, 1))
    }
)
parametervalue12: BinaryAssociation = BinaryAssociation(
    name="parametervalue12",
    ends={
        Property(name="trace_ParameterValue", type=trace_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Step13", type=trace_ParameterValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent14: BinaryAssociation = BinaryAssociation(
    name="parent14",
    ends={
        Property(name="BigStep", type=trace_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=trace_BigStep, multiplicity=Multiplicity(0, 1))
    }
)
value15: BinaryAssociation = BinaryAssociation(
    name="value15",
    ends={
        Property(name="trace_Value17", type=trace_ObjectState, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_ObjectState16", type=trace_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tracedobject18: BinaryAssociation = BinaryAssociation(
    name="tracedobject18",
    ends={
        Property(name="TracedObject", type=trace_ObjectState, multiplicity=Multiplicity(1, 1)),
        Property(name="objectstates", type=trace_TracedObject, multiplicity=Multiplicity(1, 1))
    }
)
objectstate19: BinaryAssociation = BinaryAssociation(
    name="objectstate19",
    ends={
        Property(name="trace_TracedObject20", type=trace_RefValue, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_RefValue", type=trace_TracedObject, multiplicity=Multiplicity(0, 1))
    }
)
objectstates21: BinaryAssociation = BinaryAssociation(
    name="objectstates21",
    ends={
        Property(name="trace_ObjectState23", type=trace_ModelState, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_ModelState22", type=trace_ObjectState, multiplicity=Multiplicity(0, 9999))
    }
)
children24: BinaryAssociation = BinaryAssociation(
    name="children24",
    ends={
        Property(name="Step", type=trace_BigStep, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=trace_Step, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objectstates25: BinaryAssociation = BinaryAssociation(
    name="objectstates25",
    ends={
        Property(name="ObjectState", type=trace_TracedObject, multiplicity=Multiplicity(1, 1)),
        Property(name="tracedobject", type=trace_ObjectState, multiplicity=Multiplicity(1, 9999))
    }
)
value26: BinaryAssociation = BinaryAssociation(
    name="value26",
    ends={
        Property(name="trace_Value28", type=trace_ParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_ParameterValue27", type=trace_Value, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_trace_RefValue_Value = Generalization(general=Value, specific=trace_RefValue)
gen_trace_LiteralValue_Value = Generalization(general=Value, specific=trace_LiteralValue)
gen_trace_SmallStep_Step = Generalization(general=Step, specific=trace_SmallStep)
gen_trace_BigStep_Step = Generalization(general=Step, specific=trace_BigStep)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_Trace, trace_Step, trace_ModelState, trace_ObjectState, trace_TracedObject, trace_Value, trace_ParameterValue, trace_BigStep, trace_RefValue, Value, trace_LiteralValue, trace_SmallStep, Step, ParamterKindEnum},
    associations={steps0, modelstate1, objectstates3, tracedobject5, values7, state9, parametervalue12, parent14, value15, tracedobject18, objectstate19, objectstates21, children24, objectstates25, value26},
    generalizations={gen_trace_RefValue_Value, gen_trace_LiteralValue_Value, gen_trace_SmallStep_Step, gen_trace_BigStep_Step},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)