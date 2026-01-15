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
UmlTrace_TraceElement = Class(name="UmlTrace::TraceElement")
UmlTrace_Class = Class(name="UmlTrace::Class")
UmlTrace_EClass0 = Class(name="UmlTrace::EClass0")

# UmlTrace_TraceElement class attributes and methods

# UmlTrace_Class class attributes and methods

# UmlTrace_EClass0 class attributes and methods

# Relationships
source0: BinaryAssociation = BinaryAssociation(
    name="source0",
    ends={
        Property(name="UmlTrace_Class", type=UmlTrace_TraceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UmlTrace_TraceElement", type=UmlTrace_Class, multiplicity=Multiplicity(1, 1))
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="UmlTrace_Class3", type=UmlTrace_TraceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UmlTrace_TraceElement2", type=UmlTrace_Class, multiplicity=Multiplicity(1, 1))
    }
)
inheritedSource4: BinaryAssociation = BinaryAssociation(
    name="inheritedSource4",
    ends={
        Property(name="UmlTrace_Class6", type=UmlTrace_TraceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UmlTrace_TraceElement5", type=UmlTrace_Class, multiplicity=Multiplicity(0, 9999))
    }
)
inheritedTarget7: BinaryAssociation = BinaryAssociation(
    name="inheritedTarget7",
    ends={
        Property(name="UmlTrace_Class9", type=UmlTrace_TraceElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UmlTrace_TraceElement8", type=UmlTrace_Class, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="UmlTrace",
    types={UmlTrace_TraceElement, UmlTrace_Class, UmlTrace_EClass0},
    associations={source0, target1, inheritedSource4, inheritedTarget7},
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