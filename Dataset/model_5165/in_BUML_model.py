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
in_RootContainer = Class(name="in::RootContainer")
in_RootIn = Class(name="in::RootIn", is_abstract=True)
in_A = Class(name="in::A")
RootIn = Class(name="RootIn")
in_B = Class(name="in::B")

# in_RootContainer class attributes and methods

# in_RootIn class attributes and methods

# in_A class attributes and methods
in_A_name: Property = Property(name="name", type=StringType)
in_A.attributes={in_A_name}

# RootIn class attributes and methods

# in_B class attributes and methods
in_B_name: Property = Property(name="name", type=StringType)
in_B.attributes={in_B_name}

# Relationships
elements4: BinaryAssociation = BinaryAssociation(
    name="elements4",
    ends={
        Property(name="in_RootIn", type=in_RootContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="in_RootContainer", type=in_RootIn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refB0: BinaryAssociation = BinaryAssociation(
    name="refB0",
    ends={
        Property(name="in_B", type=in_A, multiplicity=Multiplicity(1, 1)),
        Property(name="in_A", type=in_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refA1: BinaryAssociation = BinaryAssociation(
    name="refA1",
    ends={
        Property(name="in_A3", type=in_B, multiplicity=Multiplicity(1, 1)),
        Property(name="in_B2", type=in_A, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_in_RootContainer_RootIn = Generalization(general=RootIn, specific=in_RootContainer)
gen_in_A_RootIn = Generalization(general=RootIn, specific=in_A)
gen_in_B_RootIn = Generalization(general=RootIn, specific=in_B)

# Domain Model
domain_model = DomainModel(
    name="in",
    types={in_RootContainer, in_RootIn, in_A, RootIn, in_B},
    associations={elements4, refB0, refA1},
    generalizations={gen_in_RootContainer_RootIn, gen_in_A_RootIn, gen_in_B_RootIn},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)