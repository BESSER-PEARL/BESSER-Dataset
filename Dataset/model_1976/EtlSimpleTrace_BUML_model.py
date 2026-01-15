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
EtlSimpleTrace_Trace = Class(name="EtlSimpleTrace::Trace")
EtlSimpleTrace_TraceLink = Class(name="EtlSimpleTrace::TraceLink")
EtlSimpleTrace_EObject = Class(name="EtlSimpleTrace::EObject")

# EtlSimpleTrace_Trace class attributes and methods

# EtlSimpleTrace_TraceLink class attributes and methods
EtlSimpleTrace_TraceLink_description: Property = Property(name="description", type=StringType)
EtlSimpleTrace_TraceLink.attributes={EtlSimpleTrace_TraceLink_description}

# EtlSimpleTrace_EObject class attributes and methods

# Relationships
links0: BinaryAssociation = BinaryAssociation(
    name="links0",
    ends={
        Property(name="EtlSimpleTrace_TraceLink", type=EtlSimpleTrace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="EtlSimpleTrace_Trace", type=EtlSimpleTrace_TraceLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sources1: BinaryAssociation = BinaryAssociation(
    name="sources1",
    ends={
        Property(name="EtlSimpleTrace_EObject", type=EtlSimpleTrace_TraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="EtlSimpleTrace_TraceLink2", type=EtlSimpleTrace_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
targets3: BinaryAssociation = BinaryAssociation(
    name="targets3",
    ends={
        Property(name="EtlSimpleTrace_EObject5", type=EtlSimpleTrace_TraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="EtlSimpleTrace_TraceLink4", type=EtlSimpleTrace_EObject, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="EtlSimpleTrace",
    types={EtlSimpleTrace_Trace, EtlSimpleTrace_TraceLink, EtlSimpleTrace_EObject},
    associations={links0, sources1, targets3},
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