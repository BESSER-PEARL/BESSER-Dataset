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
MultipleInheritance_Model = Class(name="MultipleInheritance::Model")
MultipleInheritance_Object = Class(name="MultipleInheritance::Object", is_abstract=True)
MultipleInheritance_A = Class(name="MultipleInheritance::A")
Object = Class(name="Object")
MultipleInheritance_D = Class(name="MultipleInheritance::D")
MultipleInheritance_B = Class(name="MultipleInheritance::B")
MultipleInheritance_C = Class(name="MultipleInheritance::C")
A = Class(name="A")
B = Class(name="B")

# MultipleInheritance_Model class attributes and methods

# MultipleInheritance_Object class attributes and methods

# MultipleInheritance_A class attributes and methods

# Object class attributes and methods

# MultipleInheritance_D class attributes and methods

# MultipleInheritance_B class attributes and methods

# MultipleInheritance_C class attributes and methods

# A class attributes and methods

# B class attributes and methods

# Relationships
objects0: BinaryAssociation = BinaryAssociation(
    name="objects0",
    ends={
        Property(name="MultipleInheritance_Object", type=MultipleInheritance_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="MultipleInheritance_Model", type=MultipleInheritance_Object, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fieldOfA1: BinaryAssociation = BinaryAssociation(
    name="fieldOfA1",
    ends={
        Property(name="MultipleInheritance_D", type=MultipleInheritance_A, multiplicity=Multiplicity(1, 1)),
        Property(name="MultipleInheritance_A", type=MultipleInheritance_D, multiplicity=Multiplicity(1, 1))
    }
)
fieldOfB2: BinaryAssociation = BinaryAssociation(
    name="fieldOfB2",
    ends={
        Property(name="MultipleInheritance_D3", type=MultipleInheritance_B, multiplicity=Multiplicity(1, 1)),
        Property(name="MultipleInheritance_B", type=MultipleInheritance_D, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_MultipleInheritance_A_Object = Generalization(general=Object, specific=MultipleInheritance_A)
gen_MultipleInheritance_B_Object = Generalization(general=Object, specific=MultipleInheritance_B)
gen_MultipleInheritance_C_A = Generalization(general=A, specific=MultipleInheritance_C)
gen_MultipleInheritance_C_B = Generalization(general=B, specific=MultipleInheritance_C)
gen_MultipleInheritance_D_Object = Generalization(general=Object, specific=MultipleInheritance_D)

# Domain Model
domain_model = DomainModel(
    name="MultipleInheritance",
    types={MultipleInheritance_Model, MultipleInheritance_Object, MultipleInheritance_A, Object, MultipleInheritance_D, MultipleInheritance_B, MultipleInheritance_C, A, B},
    associations={objects0, fieldOfA1, fieldOfB2},
    generalizations={gen_MultipleInheritance_A_Object, gen_MultipleInheritance_B_Object, gen_MultipleInheritance_C_A, gen_MultipleInheritance_C_B, gen_MultipleInheritance_D_Object},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)