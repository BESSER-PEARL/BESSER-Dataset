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
trace_Trace = Class(name="trace::Trace")
trace_TraceLink = Class(name="trace::TraceLink")
trace_EObject = Class(name="trace::EObject")

# trace_Trace class attributes and methods
trace_Trace_m_getAllMappedObjects: Method = Method(name="getAllMappedObjects", parameters={}, type=StringType)
trace_Trace.methods={trace_Trace_m_getAllMappedObjects}

# trace_TraceLink class attributes and methods
trace_TraceLink_name: Property = Property(name="name", type=StringType)
trace_TraceLink_similarity: Property = Property(name="similarity", type=IntegerType)
trace_TraceLink_requiredSimilarity: Property = Property(name="requiredSimilarity", type=IntegerType)
trace_TraceLink_rationale: Property = Property(name="rationale", type=StringType)
trace_TraceLink_similarityMethod: Property = Property(name="similarityMethod", type=IntegerType)
trace_TraceLink_targetValue: Property = Property(name="targetValue", type=StringType)
trace_TraceLink_sourceValue: Property = Property(name="sourceValue", type=StringType)
trace_TraceLink_m_sameAs: Method = Method(name="sameAs", parameters={Parameter(name='tracelink')}, type=BooleanType)
trace_TraceLink.attributes={trace_TraceLink_similarity, trace_TraceLink_rationale, trace_TraceLink_requiredSimilarity, trace_TraceLink_name, trace_TraceLink_sourceValue, trace_TraceLink_similarityMethod, trace_TraceLink_targetValue}
trace_TraceLink.methods={trace_TraceLink_m_sameAs}

# trace_EObject class attributes and methods

# Relationships
traces0: BinaryAssociation = BinaryAssociation(
    name="traces0",
    ends={
        Property(name="trace_TraceLink", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace", type=trace_TraceLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceModel1: BinaryAssociation = BinaryAssociation(
    name="sourceModel1",
    ends={
        Property(name="trace_EObject", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace2", type=trace_EObject, multiplicity=Multiplicity(0, 1))
    }
)
targetModel3: BinaryAssociation = BinaryAssociation(
    name="targetModel3",
    ends={
        Property(name="trace_EObject5", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace4", type=trace_EObject, multiplicity=Multiplicity(0, 1))
    }
)
source6: BinaryAssociation = BinaryAssociation(
    name="source6",
    ends={
        Property(name="trace_EObject8", type=trace_TraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TraceLink7", type=trace_EObject, multiplicity=Multiplicity(0, 1))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="trace_EObject11", type=trace_TraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TraceLink10", type=trace_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_Trace, trace_TraceLink, trace_EObject},
    associations={traces0, sourceModel1, targetModel3, source6, target9},
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