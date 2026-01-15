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
B = Class(name="B")
foo_B = Class(name="foo::B", is_abstract=True)
J = Class(name="J")
foo_J = Class(name="foo::J")
foo_A = Class(name="foo::A")

# B class attributes and methods

# foo_B class attributes and methods

# J class attributes and methods

# foo_J class attributes and methods

# foo_A class attributes and methods
foo_A_fooA: Property = Property(name="fooA", type=StringType)
foo_A.attributes={foo_A_fooA}

# Relationships
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="B", type=foo_A, multiplicity=Multiplicity(1, 1)),
        Property(name="foo_A", type=B, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_foo_B_J = Generalization(general=J, specific=foo_B)

# Domain Model
domain_model = DomainModel(
    name="ecore",
    types={B, foo_B, J, foo_J, foo_A},
    associations={b0},
    generalizations={gen_foo_B_J},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)