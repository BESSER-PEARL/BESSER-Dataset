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
mydsl_A = Class(name="mydsl::A")
W = Class(name="W")
mydsl_B = Class(name="mydsl::B")
mydsl_C = Class(name="mydsl::C")
mydsl_L = Class(name="mydsl::L")
mydsl_D = Class(name="mydsl::D")
mydsl_W = Class(name="mydsl::W")

# mydsl_A class attributes and methods

# W class attributes and methods

# mydsl_B class attributes and methods

# mydsl_C class attributes and methods

# mydsl_L class attributes and methods

# mydsl_D class attributes and methods

# mydsl_W class attributes and methods
mydsl_W_name: Property = Property(name="name", type=StringType)
mydsl_W.attributes={mydsl_W_name}

# Relationships
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="mydsl_B", type=mydsl_A, multiplicity=Multiplicity(1, 1)),
        Property(name="mydsl_A", type=mydsl_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cs1: BinaryAssociation = BinaryAssociation(
    name="cs1",
    ends={
        Property(name="mydsl_C", type=mydsl_A, multiplicity=Multiplicity(1, 1)),
        Property(name="mydsl_A2", type=mydsl_C, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ls3: BinaryAssociation = BinaryAssociation(
    name="ls3",
    ends={
        Property(name="mydsl_L", type=mydsl_B, multiplicity=Multiplicity(1, 1)),
        Property(name="mydsl_B4", type=mydsl_L, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dd5: BinaryAssociation = BinaryAssociation(
    name="dd5",
    ends={
        Property(name="mydsl_D", type=mydsl_B, multiplicity=Multiplicity(1, 1)),
        Property(name="mydsl_B6", type=mydsl_D, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c7: BinaryAssociation = BinaryAssociation(
    name="c7",
    ends={
        Property(name="mydsl_C9", type=mydsl_L, multiplicity=Multiplicity(1, 1)),
        Property(name="mydsl_L8", type=mydsl_C, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_mydsl_A_W = Generalization(general=W, specific=mydsl_A)
gen_mydsl_B_W = Generalization(general=W, specific=mydsl_B)
gen_mydsl_C_W = Generalization(general=W, specific=mydsl_C)
gen_mydsl_L_W = Generalization(general=W, specific=mydsl_L)
gen_mydsl_D_W = Generalization(general=W, specific=mydsl_D)

# Domain Model
domain_model = DomainModel(
    name="mydsl",
    types={mydsl_A, W, mydsl_B, mydsl_C, mydsl_L, mydsl_D, mydsl_W},
    associations={bs0, cs1, ls3, dd5, c7},
    generalizations={gen_mydsl_A_W, gen_mydsl_B_W, gen_mydsl_C_W, gen_mydsl_L_W, gen_mydsl_D_W},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)