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
tracelinks_TraceLink = Class(name="tracelinks::TraceLink")
tracelinks_TraceLinkEnd = Class(name="tracelinks::TraceLinkEnd")
tracelinks_TraceLinksModel = Class(name="tracelinks::TraceLinksModel")

# tracelinks_TraceLink class attributes and methods

# tracelinks_TraceLinkEnd class attributes and methods
tracelinks_TraceLinkEnd_id: Property = Property(name="id", type=StringType)
tracelinks_TraceLinkEnd_version: Property = Property(name="version", type=StringType)
tracelinks_TraceLinkEnd.attributes={tracelinks_TraceLinkEnd_version, tracelinks_TraceLinkEnd_id}

# tracelinks_TraceLinksModel class attributes and methods

# Relationships
traceLinks0: BinaryAssociation = BinaryAssociation(
    name="traceLinks0",
    ends={
        Property(name="tracelinks_TraceLink", type=tracelinks_TraceLinksModel, multiplicity=Multiplicity(1, 1)),
        Property(name="tracelinks_TraceLinksModel", type=tracelinks_TraceLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from1: BinaryAssociation = BinaryAssociation(
    name="from1",
    ends={
        Property(name="tracelinks_TraceLinkEnd", type=tracelinks_TraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="tracelinks_TraceLink2", type=tracelinks_TraceLinkEnd, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
to3: BinaryAssociation = BinaryAssociation(
    name="to3",
    ends={
        Property(name="tracelinks_TraceLinkEnd5", type=tracelinks_TraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="tracelinks_TraceLink4", type=tracelinks_TraceLinkEnd, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="tracelinks",
    types={tracelinks_TraceLink, tracelinks_TraceLinkEnd, tracelinks_TraceLinksModel},
    associations={traceLinks0, from1, to3},
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