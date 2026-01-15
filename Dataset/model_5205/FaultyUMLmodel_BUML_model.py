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
FaultyUMLmodel_D = Class(name="FaultyUMLmodel::D")
FaultyUMLmodel_A = Class(name="FaultyUMLmodel::A")
FaultyUMLmodel_B = Class(name="FaultyUMLmodel::B")
FaultyUMLmodel_C = Class(name="FaultyUMLmodel::C")

# FaultyUMLmodel_D class attributes and methods
FaultyUMLmodel_D_z: Property = Property(name="z", type=BooleanType)
FaultyUMLmodel_D.attributes={FaultyUMLmodel_D_z}

# FaultyUMLmodel_A class attributes and methods
FaultyUMLmodel_A_v: Property = Property(name="v", type=IntegerType)
FaultyUMLmodel_A_w: Property = Property(name="w", type=BooleanType)
FaultyUMLmodel_A.attributes={FaultyUMLmodel_A_w, FaultyUMLmodel_A_v}

# FaultyUMLmodel_B class attributes and methods
FaultyUMLmodel_B_x: Property = Property(name="x", type=IntegerType)
FaultyUMLmodel_B_y: Property = Property(name="y", type=IntegerType)
FaultyUMLmodel_B.attributes={FaultyUMLmodel_B_x, FaultyUMLmodel_B_y}

# FaultyUMLmodel_C class attributes and methods
FaultyUMLmodel_C_u: Property = Property(name="u", type=IntegerType)
FaultyUMLmodel_C.attributes={FaultyUMLmodel_C_u}

# Domain Model
domain_model = DomainModel(
    name="FaultyUMLmodel",
    types={FaultyUMLmodel_D, FaultyUMLmodel_A, FaultyUMLmodel_B, FaultyUMLmodel_C},
    associations={},
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