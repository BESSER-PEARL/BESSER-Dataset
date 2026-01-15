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
MM1_D = Class(name="MM1::D")
MM1_B = Class(name="MM1::B")
A = Class(name="A")
MM1_C = Class(name="MM1::C")
MM1_ContainerMM1 = Class(name="MM1::ContainerMM1")
MM1_A = Class(name="MM1::A", is_abstract=True)

# MM1_D class attributes and methods

# MM1_B class attributes and methods
MM1_B_value: Property = Property(name="value", type=IntegerType)
MM1_B.attributes={MM1_B_value}

# A class attributes and methods

# MM1_C class attributes and methods
MM1_C_value: Property = Property(name="value", type=BooleanType)
MM1_C.attributes={MM1_C_value}

# MM1_ContainerMM1 class attributes and methods
MM1_ContainerMM1_aname: Property = Property(name="aname", type=IntegerType)
MM1_ContainerMM1.attributes={MM1_ContainerMM1_aname}

# MM1_A class attributes and methods
MM1_A_name: Property = Property(name="name", type=StringType)
MM1_A.attributes={MM1_A_name}

# Relationships
ds1: BinaryAssociation = BinaryAssociation(
    name="ds1",
    ends={
        Property(name="MM1_D", type=MM1_ContainerMM1, multiplicity=Multiplicity(1, 1)),
        Property(name="MM1_ContainerMM12", type=MM1_D, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
as0: BinaryAssociation = BinaryAssociation(
    name="as0",
    ends={
        Property(name="MM1_A", type=MM1_ContainerMM1, multiplicity=Multiplicity(1, 1)),
        Property(name="MM1_ContainerMM1", type=MM1_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_MM1_B_A = Generalization(general=A, specific=MM1_B)
gen_MM1_C_A = Generalization(general=A, specific=MM1_C)

# Domain Model
domain_model = DomainModel(
    name="MM1",
    types={MM1_D, MM1_B, A, MM1_C, MM1_ContainerMM1, MM1_A},
    associations={ds1, as0},
    generalizations={gen_MM1_B_A, gen_MM1_C_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)