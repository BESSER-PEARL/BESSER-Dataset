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
traces_Trace = Class(name="traces::Trace")
traces_EObject = Class(name="traces::EObject")
traces_TraceRepository = Class(name="traces::TraceRepository")

# traces_Trace class attributes and methods
traces_Trace_Role: Property = Property(name="Role", type=StringType)
traces_Trace.attributes={traces_Trace_Role}

# traces_EObject class attributes and methods

# traces_TraceRepository class attributes and methods

# Relationships
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="traces_EObject", type=traces_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_Trace", type=traces_EObject, multiplicity=Multiplicity(1, 1))
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="traces_EObject3", type=traces_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_Trace2", type=traces_EObject, multiplicity=Multiplicity(1, 1))
    }
)
Traces4: BinaryAssociation = BinaryAssociation(
    name="Traces4",
    ends={
        Property(name="traces_Trace5", type=traces_TraceRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="traces_TraceRepository", type=traces_Trace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="traces",
    types={traces_Trace, traces_EObject, traces_TraceRepository},
    associations={source0, target1, Traces4},
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