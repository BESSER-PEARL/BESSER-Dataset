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
SimpleTrace_EObject = Class(name="SimpleTrace::EObject")
SimpleTrace_Trace = Class(name="SimpleTrace::Trace")
SimpleTrace_TraceLink = Class(name="SimpleTrace::TraceLink")

# SimpleTrace_EObject class attributes and methods

# SimpleTrace_Trace class attributes and methods

# SimpleTrace_TraceLink class attributes and methods
SimpleTrace_TraceLink_description: Property = Property(name="description", type=StringType)
SimpleTrace_TraceLink.attributes={SimpleTrace_TraceLink_description}

# Relationships
links0: BinaryAssociation = BinaryAssociation(
    name="links0",
    ends={
        Property(name="SimpleTrace_TraceLink", type=SimpleTrace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleTrace_Trace", type=SimpleTrace_TraceLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sources1: BinaryAssociation = BinaryAssociation(
    name="sources1",
    ends={
        Property(name="SimpleTrace_EObject", type=SimpleTrace_TraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleTrace_TraceLink2", type=SimpleTrace_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
targets3: BinaryAssociation = BinaryAssociation(
    name="targets3",
    ends={
        Property(name="SimpleTrace_EObject5", type=SimpleTrace_TraceLink, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleTrace_TraceLink4", type=SimpleTrace_EObject, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="SimpleTrace",
    types={SimpleTrace_EObject, SimpleTrace_Trace, SimpleTrace_TraceLink},
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