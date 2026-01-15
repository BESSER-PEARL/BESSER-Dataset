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
ParameterType: Enumeration = Enumeration(
    name="ParameterType",
    literals={
            EnumerationLiteral(name="source"),
			EnumerationLiteral(name="target"),
			EnumerationLiteral(name="used")
    }
)

# Classes
traces_Trace = Class(name="traces::Trace")
traces_Model = Class(name="traces::Model")
traces_TraceRecord = Class(name="traces::TraceRecord")
traces_TraceElement = Class(name="traces::TraceElement")
traces_EObject = Class(name="traces::EObject")

# traces_Trace class attributes and methods
traces_Trace_timestamp: Property = Property(name="timestamp", type=StringType)
traces_Trace_ruleName: Property = Property(name="ruleName", type=StringType)
traces_Trace_ruleInfo: Property = Property(name="ruleInfo", type=StringType)
traces_Trace.attributes={traces_Trace_timestamp, traces_Trace_ruleName, traces_Trace_ruleInfo}

# traces_Model class attributes and methods
traces_Model_uriModel: Property = Property(name="uriModel", type=StringType)
traces_Model.attributes={traces_Model_uriModel}

# traces_TraceRecord class attributes and methods
traces_TraceRecord_name: Property = Property(name="name", type=StringType)
traces_TraceRecord.attributes={traces_TraceRecord_name}

# traces_TraceElement class attributes and methods
traces_TraceElement_traceType: Property = Property(name="traceType", type=StringType)
traces_TraceElement_value: Property = Property(name="value", type=StringType)
traces_TraceElement_typeName: Property = Property(name="typeName", type=StringType)
traces_TraceElement.attributes={traces_TraceElement_typeName, traces_TraceElement_traceType, traces_TraceElement_value}

# traces_EObject class attributes and methods

# Relationships
traces0: BinaryAssociation = BinaryAssociation(
    name="traces0",
    ends={
        Property(name="traces_Trace", type=traces_TraceRecord, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_TraceRecord", type=traces_Trace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
models1: BinaryAssociation = BinaryAssociation(
    name="models1",
    ends={
        Property(name="traces_Model", type=traces_TraceRecord, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_TraceRecord2", type=traces_Model, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elements3: BinaryAssociation = BinaryAssociation(
    name="elements3",
    ends={
        Property(name="traces_TraceElement", type=traces_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_Trace4", type=traces_TraceElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element5: BinaryAssociation = BinaryAssociation(
    name="element5",
    ends={
        Property(name="traces_EObject", type=traces_TraceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_TraceElement6", type=traces_EObject, multiplicity=Multiplicity(0, 1))
    }
)
modelRoot7: BinaryAssociation = BinaryAssociation(
    name="modelRoot7",
    ends={
        Property(name="traces_EObject9", type=traces_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_Model8", type=traces_EObject, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="traces",
    types={traces_Trace, traces_Model, traces_TraceRecord, traces_TraceElement, traces_EObject, ParameterType},
    associations={traces0, models1, elements3, element5, modelRoot7},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)