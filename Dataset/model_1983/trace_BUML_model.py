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
trace_EObject = Class(name="trace::EObject")

# trace_Trace class attributes and methods
trace_Trace_name: Property = Property(name="name", type=StringType)
trace_Trace.attributes={trace_Trace_name}

# trace_EObject class attributes and methods

# Relationships
target4: BinaryAssociation = BinaryAssociation(
    name="target4",
    ends={
        Property(name="trace_EObject6", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace5", type=trace_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
subTraces1: BinaryAssociation = BinaryAssociation(
    name="subTraces1",
    ends={
        Property(name="trace_Trace", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace0", type=trace_Trace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source2: BinaryAssociation = BinaryAssociation(
    name="source2",
    ends={
        Property(name="trace_EObject", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace3", type=trace_EObject, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_Trace, trace_EObject},
    associations={target4, subTraces1, source2},
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