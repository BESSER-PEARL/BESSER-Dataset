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
introduction_A = Class(name="introduction::A")
introduction_X = Class(name="introduction::X")
introduction_Y = Class(name="introduction::Y")
introduction_B = Class(name="introduction::B")
A = Class(name="A")
introduction_con = Class(name="introduction::con")

# introduction_A class attributes and methods
introduction_A_id: Property = Property(name="id", type=StringType)
introduction_A.attributes={introduction_A_id}

# introduction_X class attributes and methods
introduction_X_id: Property = Property(name="id", type=StringType)
introduction_X.attributes={introduction_X_id}

# introduction_Y class attributes and methods
introduction_Y_id: Property = Property(name="id", type=StringType)
introduction_Y_test: Property = Property(name="test", type=IntegerType)
introduction_Y.attributes={introduction_Y_id, introduction_Y_test}

# introduction_B class attributes and methods

# A class attributes and methods

# introduction_con class attributes and methods

# Relationships
xs0: BinaryAssociation = BinaryAssociation(
    name="xs0",
    ends={
        Property(name="introduction_X", type=introduction_A, multiplicity=Multiplicity(1, 1)),
        Property(name="introduction_A", type=introduction_X, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ys1: BinaryAssociation = BinaryAssociation(
    name="ys1",
    ends={
        Property(name="introduction_Y", type=introduction_A, multiplicity=Multiplicity(1, 1)),
        Property(name="introduction_A2", type=introduction_Y, multiplicity=Multiplicity(1, 4))
    }
)
a3: BinaryAssociation = BinaryAssociation(
    name="a3",
    ends={
        Property(name="introduction_A4", type=introduction_con, multiplicity=Multiplicity(1, 1)),
        Property(name="introduction_con", type=introduction_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
y5: BinaryAssociation = BinaryAssociation(
    name="y5",
    ends={
        Property(name="introduction_Y7", type=introduction_con, multiplicity=Multiplicity(1, 1)),
        Property(name="introduction_con6", type=introduction_Y, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_introduction_B_A = Generalization(general=A, specific=introduction_B)

# Domain Model
domain_model = DomainModel(
    name="introduction",
    types={introduction_A, introduction_X, introduction_Y, introduction_B, A, introduction_con},
    associations={xs0, ys1, a3, y5},
    generalizations={gen_introduction_B_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)