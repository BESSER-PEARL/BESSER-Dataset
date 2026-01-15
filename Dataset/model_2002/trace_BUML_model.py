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
trace_Value = Class(name="trace::Value")
trace_Assignment = Class(name="trace::Assignment")
Step = Class(name="Step")
trace_ArrayValue = Class(name="trace::ArrayValue")
Value = Class(name="Value")
trace_FunctionReturn = Class(name="trace::FunctionReturn")
trace_Location = Class(name="trace::Location")
trace_LocationOnly = Class(name="trace::LocationOnly")
trace_NameToValueMap = Class(name="trace::NameToValueMap")
trace_Failure = Class(name="trace::Failure")
trace_FunctionCall = Class(name="trace::FunctionCall")
trace_Step = Class(name="trace::Step")
trace_StructValue = Class(name="trace::StructValue")
trace_SimpleValue = Class(name="trace::SimpleValue")
trace_UnionValue = Class(name="trace::UnionValue")
StructValue = Class(name="StructValue")
trace_Output = Class(name="trace::Output")
trace_Trace = Class(name="trace::Trace")

# trace_Value class attributes and methods
trace_Value_type: Property = Property(name="type", type=StringType)
trace_Value_m_getValue: Method = Method(name="getValue", parameters={Parameter(name='expression')}, type=Value)
trace_Value_m_getChildrenCount: Method = Method(name="getChildrenCount", parameters={}, type=StringType)
trace_Value_m_getUserFriendlyRepresentation: Method = Method(name="getUserFriendlyRepresentation", parameters={Parameter(name='abridged')}, type=StringType)
trace_Value_m_compare: Method = Method(name="compare", parameters={Parameter(name='old'), Parameter(name='parentPath')})
trace_Value_m_listChildren: Method = Method(name="listChildren", parameters={Parameter(name='requestedExpression')})
trace_Value.attributes={trace_Value_type}
trace_Value.methods={trace_Value_m_listChildren, trace_Value_m_compare, trace_Value_m_getUserFriendlyRepresentation, trace_Value_m_getChildrenCount, trace_Value_m_getValue}

# trace_Assignment class attributes and methods
trace_Assignment_id: Property = Property(name="id", type=StringType)
trace_Assignment_displayName: Property = Property(name="displayName", type=StringType)
trace_Assignment_baseName: Property = Property(name="baseName", type=StringType)
trace_Assignment_assignmentType: Property = Property(name="assignmentType", type=StringType)
trace_Assignment_m_getValue: Method = Method(name="getValue", parameters={Parameter(name='expression')}, type=Value)
trace_Assignment_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
trace_Assignment.attributes={trace_Assignment_id, trace_Assignment_displayName, trace_Assignment_assignmentType, trace_Assignment_baseName}
trace_Assignment.methods={trace_Assignment_m_getType, trace_Assignment_m_getValue}

# Step class attributes and methods

# trace_ArrayValue class attributes and methods

# Value class attributes and methods

# trace_FunctionReturn class attributes and methods
trace_FunctionReturn_id: Property = Property(name="id", type=StringType)
trace_FunctionReturn_displayName: Property = Property(name="displayName", type=StringType)
trace_FunctionReturn.attributes={trace_FunctionReturn_displayName, trace_FunctionReturn_id}

# trace_Location class attributes and methods
trace_Location_file: Property = Property(name="file", type=StringType)
trace_Location_function: Property = Property(name="function", type=StringType)
trace_Location_line: Property = Property(name="line", type=StringType)
trace_Location.attributes={trace_Location_line, trace_Location_function, trace_Location_file}

# trace_LocationOnly class attributes and methods

# trace_NameToValueMap class attributes and methods
trace_NameToValueMap_key: Property = Property(name="key", type=StringType)
trace_NameToValueMap.attributes={trace_NameToValueMap_key}

# trace_Failure class attributes and methods
trace_Failure_reason: Property = Property(name="reason", type=StringType)
trace_Failure.attributes={trace_Failure_reason}

# trace_FunctionCall class attributes and methods
trace_FunctionCall_id: Property = Property(name="id", type=StringType)
trace_FunctionCall_displayName: Property = Property(name="displayName", type=StringType)
trace_FunctionCall.attributes={trace_FunctionCall_displayName, trace_FunctionCall_id}

# trace_Step class attributes and methods
trace_Step_number: Property = Property(name="number", type=StringType)
trace_Step_thread: Property = Property(name="thread", type=StringType)
trace_Step_hidden: Property = Property(name="hidden", type=StringType)
trace_Step_m_interpret: Method = Method(name="interpret", parameters={Parameter(name='context')}, type=StringType)
trace_Step.attributes={trace_Step_number, trace_Step_hidden, trace_Step_thread}
trace_Step.methods={trace_Step_m_interpret}

# trace_StructValue class attributes and methods

# trace_SimpleValue class attributes and methods
trace_SimpleValue_value: Property = Property(name="value", type=StringType)
trace_SimpleValue.attributes={trace_SimpleValue_value}

# trace_UnionValue class attributes and methods

# StructValue class attributes and methods

# trace_Output class attributes and methods
trace_Output_text: Property = Property(name="text", type=StringType)
trace_Output.attributes={trace_Output_text}

# trace_Trace class attributes and methods

# Relationships
values0: BinaryAssociation = BinaryAssociation(
    name="values0",
    ends={
        Property(name="trace_Value", type=trace_ArrayValue, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_ArrayValue", type=trace_Value, multiplicity=Multiplicity(0, 9999))
    }
)
value1: BinaryAssociation = BinaryAssociation(
    name="value1",
    ends={
        Property(name="trace_Value2", type=trace_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Assignment", type=trace_Value, multiplicity=Multiplicity(1, 1))
    }
)
value3: BinaryAssociation = BinaryAssociation(
    name="value3",
    ends={
        Property(name="trace_Value4", type=trace_NameToValueMap, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_NameToValueMap", type=trace_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
location5: BinaryAssociation = BinaryAssociation(
    name="location5",
    ends={
        Property(name="trace_Location", type=trace_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Step", type=trace_Location, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values6: BinaryAssociation = BinaryAssociation(
    name="values6",
    ends={
        Property(name="trace_NameToValueMap7", type=trace_StructValue, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_StructValue", type=trace_NameToValueMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
steps8: BinaryAssociation = BinaryAssociation(
    name="steps8",
    ends={
        Property(name="trace_Step9", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace", type=trace_Step, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_trace_Assignment_Step = Generalization(general=Step, specific=trace_Assignment)
gen_trace_ArrayValue_Value = Generalization(general=Value, specific=trace_ArrayValue)
gen_trace_FunctionReturn_Step = Generalization(general=Step, specific=trace_FunctionReturn)
gen_trace_LocationOnly_Step = Generalization(general=Step, specific=trace_LocationOnly)
gen_trace_Failure_Step = Generalization(general=Step, specific=trace_Failure)
gen_trace_FunctionCall_Step = Generalization(general=Step, specific=trace_FunctionCall)
gen_trace_StructValue_Value = Generalization(general=Value, specific=trace_StructValue)
gen_trace_SimpleValue_Value = Generalization(general=Value, specific=trace_SimpleValue)
gen_trace_UnionValue_StructValue = Generalization(general=StructValue, specific=trace_UnionValue)
gen_trace_Output_Step = Generalization(general=Step, specific=trace_Output)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_Value, trace_Assignment, Step, trace_ArrayValue, Value, trace_FunctionReturn, trace_Location, trace_LocationOnly, trace_NameToValueMap, trace_Failure, trace_FunctionCall, trace_Step, trace_StructValue, trace_SimpleValue, trace_UnionValue, StructValue, trace_Output, trace_Trace},
    associations={values0, value1, value3, location5, values6, steps8},
    generalizations={gen_trace_Assignment_Step, gen_trace_ArrayValue_Value, gen_trace_FunctionReturn_Step, gen_trace_LocationOnly_Step, gen_trace_Failure_Step, gen_trace_FunctionCall_Step, gen_trace_StructValue_Value, gen_trace_SimpleValue_Value, gen_trace_UnionValue_StructValue, gen_trace_Output_Step},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)