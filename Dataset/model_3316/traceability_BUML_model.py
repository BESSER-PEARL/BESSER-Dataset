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
traceability_Traceability = Class(name="traceability::Traceability")
traceability_Trace = Class(name="traceability::Trace")
traceability_EObject = Class(name="traceability::EObject")

# traceability_Traceability class attributes and methods
traceability_Traceability_id: Property = Property(name="id", type=StringType)
traceability_Traceability.attributes={traceability_Traceability_id}

# traceability_Trace class attributes and methods
traceability_Trace_id: Property = Property(name="id", type=StringType)
traceability_Trace_objects: Property = Property(name="objects", type=StringType)
traceability_Trace.attributes={traceability_Trace_id, traceability_Trace_objects}

# traceability_EObject class attributes and methods

# Relationships
traces0: BinaryAssociation = BinaryAssociation(
    name="traces0",
    ends={
        Property(name="traceability_Trace", type=traceability_Traceability, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_Traceability", type=traceability_Trace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params3: BinaryAssociation = BinaryAssociation(
    name="params3",
    ends={
        Property(name="traceability_EObject5", type=traceability_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_Trace4", type=traceability_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
targets1: BinaryAssociation = BinaryAssociation(
    name="targets1",
    ends={
        Property(name="traceability_EObject", type=traceability_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traceability_Trace2", type=traceability_EObject, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="traceability",
    types={traceability_Traceability, traceability_Trace, traceability_EObject},
    associations={traces0, params3, targets1},
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