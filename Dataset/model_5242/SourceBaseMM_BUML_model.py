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
sbase_X = Class(name="sbase::X")
SElement = Class(name="SElement")
sbase_Y = Class(name="sbase::Y")
sbase_Z = Class(name="sbase::Z")
sbase_SRoot = Class(name="sbase::SRoot")
sbase_SElement = Class(name="sbase::SElement")
sbase_EObject = Class(name="sbase::EObject")

# sbase_X class attributes and methods
sbase_X_name: Property = Property(name="name", type=StringType)
sbase_X.attributes={sbase_X_name}

# SElement class attributes and methods

# sbase_Y class attributes and methods
sbase_Y_name: Property = Property(name="name", type=StringType)
sbase_Y.attributes={sbase_Y_name}

# sbase_Z class attributes and methods

# sbase_SRoot class attributes and methods

# sbase_SElement class attributes and methods

# sbase_EObject class attributes and methods

# Relationships
ownsY0: BinaryAssociation = BinaryAssociation(
    name="ownsY0",
    ends={
        Property(name="Y", type=sbase_X, multiplicity=Multiplicity(1, 1)),
        Property(name="toX", type=sbase_Y, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownsZ1: BinaryAssociation = BinaryAssociation(
    name="ownsZ1",
    ends={
        Property(name="Z", type=sbase_Y, multiplicity=Multiplicity(1, 1)),
        Property(name="toY", type=sbase_Z, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toX2: BinaryAssociation = BinaryAssociation(
    name="toX2",
    ends={
        Property(name="X", type=sbase_Y, multiplicity=Multiplicity(1, 1)),
        Property(name="ownsY", type=sbase_X, multiplicity=Multiplicity(0, 1))
    }
)
toY3: BinaryAssociation = BinaryAssociation(
    name="toY3",
    ends={
        Property(name="Y4", type=sbase_Z, multiplicity=Multiplicity(1, 1)),
        Property(name="ownsZ", type=sbase_Y, multiplicity=Multiplicity(0, 1))
    }
)
ownedX5: BinaryAssociation = BinaryAssociation(
    name="ownedX5",
    ends={
        Property(name="sbase_X", type=sbase_SRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="sbase_SRoot", type=sbase_X, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ast6: BinaryAssociation = BinaryAssociation(
    name="ast6",
    ends={
        Property(name="sbase_EObject", type=sbase_SElement, multiplicity=Multiplicity(1, 1)),
        Property(name="sbase_SElement", type=sbase_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_sbase_X_SElement = Generalization(general=SElement, specific=sbase_X)
gen_sbase_Y_SElement = Generalization(general=SElement, specific=sbase_Y)
gen_sbase_Z_SElement = Generalization(general=SElement, specific=sbase_Z)
gen_sbase_SRoot_SElement = Generalization(general=SElement, specific=sbase_SRoot)

# Domain Model
domain_model = DomainModel(
    name="sbase",
    types={sbase_X, SElement, sbase_Y, sbase_Z, sbase_SRoot, sbase_SElement, sbase_EObject},
    associations={ownsY0, ownsZ1, toX2, toY3, ownedX5, ast6},
    generalizations={gen_sbase_X_SElement, gen_sbase_Y_SElement, gen_sbase_Z_SElement, gen_sbase_SRoot_SElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)