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
EDirectionKind: Enumeration = Enumeration(
    name="EDirectionKind",
    literals={
            EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="INOUT"),
			EnumerationLiteral(name="OUT")
    }
)

# Classes
trace_Trace = Class(name="trace::Trace")
trace_TraceRecord = Class(name="trace::TraceRecord")
trace_MappingOperationToTraceRecordMapEntry = Class(name="trace::MappingOperationToTraceRecordMapEntry")
trace_EMappingParameters = Class(name="trace::EMappingParameters")
trace_EMappingResults = Class(name="trace::EMappingResults")
trace_VarParameterValue = Class(name="trace::VarParameterValue")
trace_EValue = Class(name="trace::EValue")
MappingOperation = Class(name="MappingOperation")
trace_EObject = Class(name="trace::EObject")
trace_ObjectToTraceRecordMapEntry = Class(name="trace::ObjectToTraceRecordMapEntry")
trace_EMappingOperation = Class(name="trace::EMappingOperation")
trace_EMappingContext = Class(name="trace::EMappingContext")
trace_ETuplePartValue = Class(name="trace::ETuplePartValue")
EValue = Class(name="EValue")

# trace_Trace class attributes and methods
trace_Trace_m_getRecordBySource: Method = Method(name="getRecordBySource", parameters={Parameter(name='sourceObject'), Parameter(name='mapping')}, type=StringType)
trace_Trace_m_addRecordBySource: Method = Method(name="addRecordBySource", parameters={Parameter(name='sourceObject'), Parameter(name='trace'), Parameter(name='mapping')})
trace_Trace.methods={trace_Trace_m_addRecordBySource, trace_Trace_m_getRecordBySource}

# trace_TraceRecord class attributes and methods

# trace_MappingOperationToTraceRecordMapEntry class attributes and methods

# trace_EMappingParameters class attributes and methods

# trace_EMappingResults class attributes and methods

# trace_VarParameterValue class attributes and methods
trace_VarParameterValue_kind: Property = Property(name="kind", type=StringType)
trace_VarParameterValue_name: Property = Property(name="name", type=StringType)
trace_VarParameterValue_type: Property = Property(name="type", type=StringType)
trace_VarParameterValue.attributes={trace_VarParameterValue_type, trace_VarParameterValue_kind, trace_VarParameterValue_name}

# trace_EValue class attributes and methods
trace_EValue_primitiveValue: Property = Property(name="primitiveValue", type=StringType)
trace_EValue_oclObject: Property = Property(name="oclObject", type=StringType)
trace_EValue_collectionType: Property = Property(name="collectionType", type=StringType)
trace_EValue.attributes={trace_EValue_oclObject, trace_EValue_primitiveValue, trace_EValue_collectionType}

# MappingOperation class attributes and methods

# trace_EObject class attributes and methods

# trace_ObjectToTraceRecordMapEntry class attributes and methods
trace_ObjectToTraceRecordMapEntry_key: Property = Property(name="key", type=StringType)
trace_ObjectToTraceRecordMapEntry.attributes={trace_ObjectToTraceRecordMapEntry_key}

# trace_EMappingOperation class attributes and methods
trace_EMappingOperation_name: Property = Property(name="name", type=StringType)
trace_EMappingOperation_package: Property = Property(name="package", type=StringType)
trace_EMappingOperation_module: Property = Property(name="module", type=StringType)
trace_EMappingOperation.attributes={trace_EMappingOperation_package, trace_EMappingOperation_module, trace_EMappingOperation_name}

# trace_EMappingContext class attributes and methods

# trace_ETuplePartValue class attributes and methods
trace_ETuplePartValue_name: Property = Property(name="name", type=StringType)
trace_ETuplePartValue.attributes={trace_ETuplePartValue_name}

# EValue class attributes and methods

# Relationships
traceRecords0: BinaryAssociation = BinaryAssociation(
    name="traceRecords0",
    ends={
        Property(name="trace_TraceRecord", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace", type=trace_TraceRecord, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
traceRecordMap1: BinaryAssociation = BinaryAssociation(
    name="traceRecordMap1",
    ends={
        Property(name="trace_MappingOperationToTraceRecordMapEntry", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace2", type=trace_MappingOperationToTraceRecordMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters12: BinaryAssociation = BinaryAssociation(
    name="parameters12",
    ends={
        Property(name="trace_EMappingParameters", type=trace_TraceRecord, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TraceRecord13", type=trace_EMappingParameters, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result14: BinaryAssociation = BinaryAssociation(
    name="result14",
    ends={
        Property(name="trace_EMappingResults", type=trace_TraceRecord, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TraceRecord15", type=trace_EMappingResults, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value16: BinaryAssociation = BinaryAssociation(
    name="value16",
    ends={
        Property(name="trace_EValue", type=trace_VarParameterValue, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_VarParameterValue", type=trace_EValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value17: BinaryAssociation = BinaryAssociation(
    name="value17",
    ends={
        Property(name="trace_TraceRecord19", type=trace_MappingOperationToTraceRecordMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_MappingOperationToTraceRecordMapEntry18", type=trace_TraceRecord, multiplicity=Multiplicity(0, 9999))
    }
)
key20: BinaryAssociation = BinaryAssociation(
    name="key20",
    ends={
        Property(name="MappingOperation", type=trace_MappingOperationToTraceRecordMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_MappingOperationToTraceRecordMapEntry21", type=MappingOperation, multiplicity=Multiplicity(1, 1))
    }
)
runtimeMappingOperation22: BinaryAssociation = BinaryAssociation(
    name="runtimeMappingOperation22",
    ends={
        Property(name="MappingOperation24", type=trace_EMappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_EMappingOperation23", type=MappingOperation, multiplicity=Multiplicity(1, 1))
    }
)
modelElement25: BinaryAssociation = BinaryAssociation(
    name="modelElement25",
    ends={
        Property(name="trace_EObject", type=trace_EValue, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_EValue26", type=trace_EObject, multiplicity=Multiplicity(0, 1))
    }
)
sourceToTraceRecordMap3: BinaryAssociation = BinaryAssociation(
    name="sourceToTraceRecordMap3",
    ends={
        Property(name="trace_ObjectToTraceRecordMapEntry", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace4", type=trace_ObjectToTraceRecordMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targetToTraceRecordMap5: BinaryAssociation = BinaryAssociation(
    name="targetToTraceRecordMap5",
    ends={
        Property(name="trace_ObjectToTraceRecordMapEntry7", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace6", type=trace_ObjectToTraceRecordMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mappingOperation8: BinaryAssociation = BinaryAssociation(
    name="mappingOperation8",
    ends={
        Property(name="trace_EMappingOperation", type=trace_TraceRecord, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TraceRecord9", type=trace_EMappingOperation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context10: BinaryAssociation = BinaryAssociation(
    name="context10",
    ends={
        Property(name="trace_EMappingContext", type=trace_TraceRecord, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TraceRecord11", type=trace_EMappingContext, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value33: BinaryAssociation = BinaryAssociation(
    name="value33",
    ends={
        Property(name="trace_EValue34", type=trace_ETuplePartValue, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_ETuplePartValue", type=trace_EValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
context35: BinaryAssociation = BinaryAssociation(
    name="context35",
    ends={
        Property(name="trace_VarParameterValue37", type=trace_EMappingContext, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_EMappingContext36", type=trace_VarParameterValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters38: BinaryAssociation = BinaryAssociation(
    name="parameters38",
    ends={
        Property(name="trace_VarParameterValue40", type=trace_EMappingParameters, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_EMappingParameters39", type=trace_VarParameterValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result41: BinaryAssociation = BinaryAssociation(
    name="result41",
    ends={
        Property(name="trace_VarParameterValue43", type=trace_EMappingResults, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_EMappingResults42", type=trace_VarParameterValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value44: BinaryAssociation = BinaryAssociation(
    name="value44",
    ends={
        Property(name="trace_TraceRecord46", type=trace_ObjectToTraceRecordMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_ObjectToTraceRecordMapEntry45", type=trace_TraceRecord, multiplicity=Multiplicity(0, 9999))
    }
)
intermediateElement27: BinaryAssociation = BinaryAssociation(
    name="intermediateElement27",
    ends={
        Property(name="trace_EObject29", type=trace_EValue, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_EValue28", type=trace_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
collection31: BinaryAssociation = BinaryAssociation(
    name="collection31",
    ends={
        Property(name="trace_EValue32", type=trace_EValue, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_EValue30", type=trace_EValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_trace_ETuplePartValue_EValue = Generalization(general=EValue, specific=trace_ETuplePartValue)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_Trace, trace_TraceRecord, trace_MappingOperationToTraceRecordMapEntry, trace_EMappingParameters, trace_EMappingResults, trace_VarParameterValue, trace_EValue, MappingOperation, trace_EObject, trace_ObjectToTraceRecordMapEntry, trace_EMappingOperation, trace_EMappingContext, trace_ETuplePartValue, EValue, EDirectionKind},
    associations={traceRecords0, traceRecordMap1, parameters12, result14, value16, value17, key20, runtimeMappingOperation22, modelElement25, sourceToTraceRecordMap3, targetToTraceRecordMap5, mappingOperation8, context10, value33, context35, parameters38, result41, value44, intermediateElement27, collection31},
    generalizations={gen_trace_ETuplePartValue_EValue},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)