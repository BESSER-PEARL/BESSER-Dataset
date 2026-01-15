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
bug1312_Root = Class(name="bug1312::Root")
bug1312_B = Class(name="bug1312::B")
bug1312_C = Class(name="bug1312::C")

# bug1312_Root class attributes and methods

# bug1312_B class attributes and methods

# bug1312_C class attributes and methods

# Relationships
blist0: BinaryAssociation = BinaryAssociation(
    name="blist0",
    ends={
        Property(name="bug1312_B", type=bug1312_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="bug1312_Root", type=bug1312_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clist1: BinaryAssociation = BinaryAssociation(
    name="clist1",
    ends={
        Property(name="bug1312_C", type=bug1312_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="bug1312_Root2", type=bug1312_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="bug1312",
    types={bug1312_Root, bug1312_B, bug1312_C},
    associations={blist0, clist1},
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