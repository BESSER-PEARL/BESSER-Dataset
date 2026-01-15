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
hExample_6_RHS_model = Class(name="hExample::6::RHS::model")
hExample_6_RHS_X = Class(name="hExample::6::RHS::X")
hExample_6_RHS_Y = Class(name="hExample::6::RHS::Y")
hExample_6_RHS_Z = Class(name="hExample::6::RHS::Z")

# hExample_6_RHS_model class attributes and methods

# hExample_6_RHS_X class attributes and methods
hExample_6_RHS_X_name: Property = Property(name="name", type=StringType)
hExample_6_RHS_X.attributes={hExample_6_RHS_X_name}

# hExample_6_RHS_Y class attributes and methods
hExample_6_RHS_Y_name: Property = Property(name="name", type=StringType)
hExample_6_RHS_Y.attributes={hExample_6_RHS_Y_name}

# hExample_6_RHS_Z class attributes and methods
hExample_6_RHS_Z_name: Property = Property(name="name", type=StringType)
hExample_6_RHS_Z.attributes={hExample_6_RHS_Z_name}

# Relationships
containsX0: BinaryAssociation = BinaryAssociation(
    name="containsX0",
    ends={
        Property(name="hExample_6_RHS_X", type=hExample_6_RHS_model, multiplicity=Multiplicity(1, 1)),
        Property(name="hExample_6_RHS_model", type=hExample_6_RHS_X, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsY1: BinaryAssociation = BinaryAssociation(
    name="containsY1",
    ends={
        Property(name="hExample_6_RHS_Y", type=hExample_6_RHS_model, multiplicity=Multiplicity(1, 1)),
        Property(name="hExample_6_RHS_model2", type=hExample_6_RHS_Y, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsZ3: BinaryAssociation = BinaryAssociation(
    name="containsZ3",
    ends={
        Property(name="hExample_6_RHS_Z", type=hExample_6_RHS_model, multiplicity=Multiplicity(1, 1)),
        Property(name="hExample_6_RHS_model4", type=hExample_6_RHS_Z, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refY5: BinaryAssociation = BinaryAssociation(
    name="refY5",
    ends={
        Property(name="hExample_6_RHS_Y7", type=hExample_6_RHS_X, multiplicity=Multiplicity(1, 1)),
        Property(name="hExample_6_RHS_X6", type=hExample_6_RHS_Y, multiplicity=Multiplicity(0, 1))
    }
)
contZ8: BinaryAssociation = BinaryAssociation(
    name="contZ8",
    ends={
        Property(name="hExample_6_RHS_Z10", type=hExample_6_RHS_X, multiplicity=Multiplicity(1, 1)),
        Property(name="hExample_6_RHS_X9", type=hExample_6_RHS_Z, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="hExample_6_RHS",
    types={hExample_6_RHS_model, hExample_6_RHS_X, hExample_6_RHS_Y, hExample_6_RHS_Z},
    associations={containsX0, containsY1, containsZ3, refY5, contZ8},
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