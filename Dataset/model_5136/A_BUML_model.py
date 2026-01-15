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
a_B = Class(name="a::B")
SuperStuff = Class(name="SuperStuff")
SuperStuff2 = Class(name="SuperStuff2")
a_Root = Class(name="a::Root")
a_A = Class(name="a::A")

# a_B class attributes and methods
a_B_name: Property = Property(name="name", type=StringType)
a_B.attributes={a_B_name}

# SuperStuff class attributes and methods

# SuperStuff2 class attributes and methods

# a_Root class attributes and methods
a_Root_visible: Property = Property(name="visible", type=BooleanType)
a_Root.attributes={a_Root_visible}

# a_A class attributes and methods

# Relationships
a1: BinaryAssociation = BinaryAssociation(
    name="a1",
    ends={
        Property(name="a_A3", type=a_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="a_Root2", type=a_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
b4: BinaryAssociation = BinaryAssociation(
    name="b4",
    ends={
        Property(name="a_B", type=a_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="a_Root5", type=a_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tob6: BinaryAssociation = BinaryAssociation(
    name="tob6",
    ends={
        Property(name="a_B8", type=a_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a_A7", type=a_B, multiplicity=Multiplicity(0, 1))
    }
)
refa0: BinaryAssociation = BinaryAssociation(
    name="refa0",
    ends={
        Property(name="a_A", type=a_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="a_Root", type=a_A, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_a_A_SuperStuff = Generalization(general=SuperStuff, specific=a_A)
gen_a_A_SuperStuff2 = Generalization(general=SuperStuff2, specific=a_A)

# Domain Model
domain_model = DomainModel(
    name="a",
    types={a_B, SuperStuff, SuperStuff2, a_Root, a_A},
    associations={a1, b4, tob6, refa0},
    generalizations={gen_a_A_SuperStuff, gen_a_A_SuperStuff2},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)