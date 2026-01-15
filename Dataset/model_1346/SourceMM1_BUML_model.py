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
source_X = Class(name="source::X")
SElement = Class(name="SElement")
source_Z = Class(name="source::Z")
source_Y1 = Class(name="source::Y1")
Y = Class(name="Y")
source_Y2 = Class(name="source::Y2")
source_Y = Class(name="source::Y", is_abstract=True)
source_SElement = Class(name="source::SElement")
source_EObject = Class(name="source::EObject")
source_PathElementCS = Class(name="source::PathElementCS")
source_PathNameCS = Class(name="source::PathNameCS")
source_SRoot = Class(name="source::SRoot")

# source_X class attributes and methods
source_X_isA1: Property = Property(name="isA1", type=BooleanType)
source_X_isA2: Property = Property(name="isA2", type=BooleanType)
source_X_name: Property = Property(name="name", type=StringType)
source_X.attributes={source_X_name, source_X_isA1, source_X_isA2}

# SElement class attributes and methods

# source_Z class attributes and methods

# source_Y1 class attributes and methods

# Y class attributes and methods

# source_Y2 class attributes and methods

# source_Y class attributes and methods
source_Y_name: Property = Property(name="name", type=StringType)
source_Y.attributes={source_Y_name}

# source_SElement class attributes and methods

# source_EObject class attributes and methods

# source_PathElementCS class attributes and methods
source_PathElementCS_name: Property = Property(name="name", type=StringType)
source_PathElementCS.attributes={source_PathElementCS_name}

# source_PathNameCS class attributes and methods

# source_SRoot class attributes and methods

# Relationships
ownsZ1: BinaryAssociation = BinaryAssociation(
    name="ownsZ1",
    ends={
        Property(name="Z", type=source_Y, multiplicity=Multiplicity(1, 1)),
        Property(name="toY", type=source_Z, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toX2: BinaryAssociation = BinaryAssociation(
    name="toX2",
    ends={
        Property(name="X", type=source_Y, multiplicity=Multiplicity(1, 1)),
        Property(name="ownsY", type=source_X, multiplicity=Multiplicity(0, 1))
    }
)
toY3: BinaryAssociation = BinaryAssociation(
    name="toY3",
    ends={
        Property(name="Y4", type=source_Z, multiplicity=Multiplicity(1, 1)),
        Property(name="ownsZ", type=source_Y, multiplicity=Multiplicity(0, 1))
    }
)
ownsY0: BinaryAssociation = BinaryAssociation(
    name="ownsY0",
    ends={
        Property(name="Y", type=source_X, multiplicity=Multiplicity(1, 1)),
        Property(name="toX", type=source_Y, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ast7: BinaryAssociation = BinaryAssociation(
    name="ast7",
    ends={
        Property(name="source_EObject", type=source_SElement, multiplicity=Multiplicity(1, 1)),
        Property(name="source_SElement", type=source_EObject, multiplicity=Multiplicity(0, 1))
    }
)
path8: BinaryAssociation = BinaryAssociation(
    name="path8",
    ends={
        Property(name="source_PathElementCS", type=source_PathNameCS, multiplicity=Multiplicity(1, 1)),
        Property(name="source_PathNameCS9", type=source_PathElementCS, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
refers5: BinaryAssociation = BinaryAssociation(
    name="refers5",
    ends={
        Property(name="source_PathNameCS", type=source_Z, multiplicity=Multiplicity(1, 1)),
        Property(name="source_Z", type=source_PathNameCS, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedX6: BinaryAssociation = BinaryAssociation(
    name="ownedX6",
    ends={
        Property(name="source_X", type=source_SRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="source_SRoot", type=source_X, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_source_X_SElement = Generalization(general=SElement, specific=source_X)
gen_source_Y_SElement = Generalization(general=SElement, specific=source_Y)
gen_source_Y1_Y = Generalization(general=Y, specific=source_Y1)
gen_source_Y2_Y = Generalization(general=Y, specific=source_Y2)
gen_source_Z_SElement = Generalization(general=SElement, specific=source_Z)
gen_source_PathNameCS_SElement = Generalization(general=SElement, specific=source_PathNameCS)
gen_source_PathElementCS_SElement = Generalization(general=SElement, specific=source_PathElementCS)
gen_source_SRoot_SElement = Generalization(general=SElement, specific=source_SRoot)

# Domain Model
domain_model = DomainModel(
    name="source",
    types={source_X, SElement, source_Z, source_Y1, Y, source_Y2, source_Y, source_SElement, source_EObject, source_PathElementCS, source_PathNameCS, source_SRoot},
    associations={ownsZ1, toX2, toY3, ownsY0, ast7, path8, refers5, ownedX6},
    generalizations={gen_source_X_SElement, gen_source_Y_SElement, gen_source_Y1_Y, gen_source_Y2_Y, gen_source_Z_SElement, gen_source_PathNameCS_SElement, gen_source_PathElementCS_SElement, gen_source_SRoot_SElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)