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
hExample_6_LHS_B = Class(name="hExample::6::LHS::B")
hExample_6_LHS_model = Class(name="hExample::6::LHS::model")
hExample_6_LHS_A = Class(name="hExample::6::LHS::A")
hExample_6_LHS_C = Class(name="hExample::6::LHS::C")

# hExample_6_LHS_B class attributes and methods
hExample_6_LHS_B_name: Property = Property(name="name", type=StringType)
hExample_6_LHS_B.attributes={hExample_6_LHS_B_name}

# hExample_6_LHS_model class attributes and methods

# hExample_6_LHS_A class attributes and methods
hExample_6_LHS_A_name: Property = Property(name="name", type=StringType)
hExample_6_LHS_A.attributes={hExample_6_LHS_A_name}

# hExample_6_LHS_C class attributes and methods
hExample_6_LHS_C_name: Property = Property(name="name", type=StringType)
hExample_6_LHS_C.attributes={hExample_6_LHS_C_name}

# Relationships
containsA0: BinaryAssociation = BinaryAssociation(
    name="containsA0",
    ends={
        Property(name="hExample_6_LHS_A", type=hExample_6_LHS_model, multiplicity=Multiplicity(1, 1)),
        Property(name="hExample_6_LHS_model", type=hExample_6_LHS_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsB1: BinaryAssociation = BinaryAssociation(
    name="containsB1",
    ends={
        Property(name="hExample_6_LHS_B", type=hExample_6_LHS_model, multiplicity=Multiplicity(1, 1)),
        Property(name="hExample_6_LHS_model2", type=hExample_6_LHS_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsC3: BinaryAssociation = BinaryAssociation(
    name="containsC3",
    ends={
        Property(name="hExample_6_LHS_C", type=hExample_6_LHS_model, multiplicity=Multiplicity(1, 1)),
        Property(name="hExample_6_LHS_model4", type=hExample_6_LHS_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refB5: BinaryAssociation = BinaryAssociation(
    name="refB5",
    ends={
        Property(name="hExample_6_LHS_B7", type=hExample_6_LHS_A, multiplicity=Multiplicity(1, 1)),
        Property(name="hExample_6_LHS_A6", type=hExample_6_LHS_B, multiplicity=Multiplicity(0, 1))
    }
)
contC8: BinaryAssociation = BinaryAssociation(
    name="contC8",
    ends={
        Property(name="hExample_6_LHS_C10", type=hExample_6_LHS_A, multiplicity=Multiplicity(1, 1)),
        Property(name="hExample_6_LHS_A9", type=hExample_6_LHS_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="hExample_6_LHS",
    types={hExample_6_LHS_B, hExample_6_LHS_model, hExample_6_LHS_A, hExample_6_LHS_C},
    associations={containsA0, containsB1, containsC3, refB5, contC8},
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