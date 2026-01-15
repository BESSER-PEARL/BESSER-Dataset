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
oo_remove_empty_A = Class(name="oo::remove::empty::A")
oo_remove_empty_B = Class(name="oo::remove::empty::B")
oo_remove_empty_C = Class(name="oo::remove::empty::C")
B = Class(name="B")

# oo_remove_empty_A class attributes and methods

# oo_remove_empty_B class attributes and methods

# oo_remove_empty_C class attributes and methods

# B class attributes and methods

# Relationships
refToB0: BinaryAssociation = BinaryAssociation(
    name="refToB0",
    ends={
        Property(name="oo_remove_empty_B", type=oo_remove_empty_A, multiplicity=Multiplicity(1, 1)),
        Property(name="oo_remove_empty_A", type=oo_remove_empty_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_oo_remove_empty_C_B = Generalization(general=B, specific=oo_remove_empty_C)

# Domain Model
domain_model = DomainModel(
    name="oo_remove_empty",
    types={oo_remove_empty_A, oo_remove_empty_B, oo_remove_empty_C, B},
    associations={refToB0},
    generalizations={gen_oo_remove_empty_C_B},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)