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
astransast_AAS = Class(name="astransast::AAS")
astransast_BAS = Class(name="astransast::BAS")

# astransast_AAS class attributes and methods

# astransast_BAS class attributes and methods

# Relationships
nonc0: BinaryAssociation = BinaryAssociation(
    name="nonc0",
    ends={
        Property(name="astransast_BAS", type=astransast_AAS, multiplicity=Multiplicity(1, 1)),
        Property(name="astransast_AAS", type=astransast_BAS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
c1: BinaryAssociation = BinaryAssociation(
    name="c1",
    ends={
        Property(name="astransast_BAS3", type=astransast_AAS, multiplicity=Multiplicity(1, 1)),
        Property(name="astransast_AAS2", type=astransast_BAS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
b5: BinaryAssociation = BinaryAssociation(
    name="b5",
    ends={
        Property(name="astransast_BAS6", type=astransast_BAS, multiplicity=Multiplicity(1, 1)),
        Property(name="astransast_BAS4", type=astransast_BAS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="astransast",
    types={astransast_AAS, astransast_BAS},
    associations={nonc0, c1, b5},
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