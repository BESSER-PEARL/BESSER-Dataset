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

# trace_TraceLink class attributes and methods
trace_TraceLink_ruleName: Property = Property(name="ruleName", type=StringType)
trace_TraceLink.attributes={trace_TraceLink_ruleName}

# trace_EObject class attributes and methods

# Relationships
traceLinks0: BinaryAssociation = BinaryAssociation(
    name="traceLinks0",
    ends={
        Property(name="trace_TraceLink", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace", type=trace_TraceLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceElements1: BinaryAssociation = BinaryAssociation(
    name="sourceElements1",
    ends={
        Property(name="trace_EObject", type=trace_TraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TraceLink2", type=trace_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
targetElements3: BinaryAssociation = BinaryAssociation(
    name="targetElements3",
    ends={
        Property(name="trace_EObject5", type=trace_TraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_TraceLink4", type=trace_EObject, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_Trace, trace_TraceLink, trace_EObject},
    associations={traceLinks0, sourceElements1, targetElements3},
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