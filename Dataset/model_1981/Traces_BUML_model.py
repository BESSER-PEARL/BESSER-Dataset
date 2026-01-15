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
Traces_Trace = Class(name="Traces::Trace")
Traces_EObject = Class(name="Traces::EObject")

# Traces_Trace class attributes and methods
Traces_Trace_name: Property = Property(name="name", type=StringType)
Traces_Trace.attributes={Traces_Trace_name}

# Traces_EObject class attributes and methods

# Relationships
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="Traces_EObject", type=Traces_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="Traces_Trace", type=Traces_EObject, multiplicity=Multiplicity(1, 1))
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="Traces_EObject3", type=Traces_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="Traces_Trace2", type=Traces_EObject, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Traces",
    types={Traces_Trace, Traces_EObject},
    associations={source0, target1},
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