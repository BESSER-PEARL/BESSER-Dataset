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
trace_TraceElement = Class(name="trace::TraceElement")

# trace_Trace class attributes and methods

# trace_TraceElement class attributes and methods
trace_TraceElement_event: Property = Property(name="event", type=StringType)
trace_TraceElement_timestamp: Property = Property(name="timestamp", type=IntegerType)
trace_TraceElement.attributes={trace_TraceElement_timestamp, trace_TraceElement_event}

# Relationships
traceElements0: BinaryAssociation = BinaryAssociation(
    name="traceElements0",
    ends={
        Property(name="trace_TraceElement", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace", type=trace_TraceElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_Trace, trace_TraceElement},
    associations={traceElements0},
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