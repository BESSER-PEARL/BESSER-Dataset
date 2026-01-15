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
abc_A = Class(name="abc::A")
NamedElement = Class(name="NamedElement")
abc_C = Class(name="abc::C")
abc_B = Class(name="abc::B")
abc_NamedElement = Class(name="abc::NamedElement", is_abstract=True)

# abc_A class attributes and methods

# NamedElement class attributes and methods

# abc_C class attributes and methods

# abc_B class attributes and methods

# abc_NamedElement class attributes and methods
abc_NamedElement_name: Property = Property(name="name", type=StringType)
abc_NamedElement.attributes={abc_NamedElement_name}

# Relationships
c0: BinaryAssociation = BinaryAssociation(
    name="c0",
    ends={
        Property(name="abc_C", type=abc_A, multiplicity=Multiplicity(1, 1)),
        Property(name="abc_A", type=abc_C, multiplicity=Multiplicity(0, 1))
    }
)
c1: BinaryAssociation = BinaryAssociation(
    name="c1",
    ends={
        Property(name="abc_C2", type=abc_B, multiplicity=Multiplicity(1, 1)),
        Property(name="abc_B", type=abc_C, multiplicity=Multiplicity(0, 1))
    }
)
a3: BinaryAssociation = BinaryAssociation(
    name="a3",
    ends={
        Property(name="abc_A5", type=abc_B, multiplicity=Multiplicity(1, 1)),
        Property(name="abc_B4", type=abc_A, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_abc_A_NamedElement = Generalization(general=NamedElement, specific=abc_A)
gen_abc_B_NamedElement = Generalization(general=NamedElement, specific=abc_B)
gen_abc_C_NamedElement = Generalization(general=NamedElement, specific=abc_C)

# Domain Model
domain_model = DomainModel(
    name="abc",
    types={abc_A, NamedElement, abc_C, abc_B, abc_NamedElement},
    associations={c0, c1, a3},
    generalizations={gen_abc_A_NamedElement, gen_abc_B_NamedElement, gen_abc_C_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)