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
Trace_Trace = Class(name="Trace::Trace")
Trace_TraceLink = Class(name="Trace::TraceLink")

# Trace_Trace class attributes and methods
Trace_Trace_description: Property = Property(name="description", type=StringType)
Trace_Trace.attributes={Trace_Trace_description}

# Trace_TraceLink class attributes and methods
Trace_TraceLink_targetType: Property = Property(name="targetType", type=StringType)
Trace_TraceLink_description: Property = Property(name="description", type=StringType)
Trace_TraceLink_sourceName: Property = Property(name="sourceName", type=StringType)
Trace_TraceLink_sourceType: Property = Property(name="sourceType", type=StringType)
Trace_TraceLink_targetName: Property = Property(name="targetName", type=StringType)
Trace_TraceLink.attributes={Trace_TraceLink_description, Trace_TraceLink_sourceType, Trace_TraceLink_sourceName, Trace_TraceLink_targetType, Trace_TraceLink_targetName}

# Relationships
links0: BinaryAssociation = BinaryAssociation(
    name="links0",
    ends={
        Property(name="Trace_TraceLink", type=Trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="Trace_Trace", type=Trace_TraceLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Trace",
    types={Trace_Trace, Trace_TraceLink},
    associations={links0},
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