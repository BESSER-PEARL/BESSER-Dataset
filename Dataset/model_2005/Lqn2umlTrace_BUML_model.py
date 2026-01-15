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
Lqn2umlTrace_Trace = Class(name="Lqn2umlTrace::Trace")
Lqn2umlTrace_TraceLink = Class(name="Lqn2umlTrace::TraceLink")

# Lqn2umlTrace_Trace class attributes and methods

# Lqn2umlTrace_TraceLink class attributes and methods
Lqn2umlTrace_TraceLink_sources: Property = Property(name="sources", type=StringType)
Lqn2umlTrace_TraceLink_targets: Property = Property(name="targets", type=StringType)
Lqn2umlTrace_TraceLink_description: Property = Property(name="description", type=StringType)
Lqn2umlTrace_TraceLink.attributes={Lqn2umlTrace_TraceLink_description, Lqn2umlTrace_TraceLink_sources, Lqn2umlTrace_TraceLink_targets}

# Relationships
links0: BinaryAssociation = BinaryAssociation(
    name="links0",
    ends={
        Property(name="Lqn2umlTrace_TraceLink", type=Lqn2umlTrace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="Lqn2umlTrace_Trace", type=Lqn2umlTrace_TraceLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Lqn2umlTrace",
    types={Lqn2umlTrace_Trace, Lqn2umlTrace_TraceLink},
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