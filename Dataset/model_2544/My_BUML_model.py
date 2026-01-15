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
foo_B = Class(name="foo::B", is_abstract=True)
foo_A = Class(name="foo::A")
foo_F = Class(name="foo::F")
foo_C = Class(name="foo::C")
J = Class(name="J")
foo_H = Class(name="foo::H")
B = Class(name="B")
foo_D = Class(name="foo::D")
foo_E = Class(name="foo::E")
I = Class(name="I")
foo_I = Class(name="foo::I")
foo_J = Class(name="foo::J")

# foo_B class attributes and methods
foo_B_EAttribute0: Property = Property(name="EAttribute0", type=BooleanType)
foo_B.attributes={foo_B_EAttribute0}

# foo_A class attributes and methods
foo_A_fooA: Property = Property(name="fooA", type=BooleanType)
foo_A_fooo: Property = Property(name="fooo", type=StringType)
foo_A.attributes={foo_A_fooA, foo_A_fooo}

# foo_F class attributes and methods

# foo_C class attributes and methods
foo_C_EAttribute1: Property = Property(name="EAttribute1", type=FloatType)
foo_C.attributes={foo_C_EAttribute1}

# J class attributes and methods

# foo_H class attributes and methods
foo_H_EAttribute0: Property = Property(name="EAttribute0", type=StringType)
foo_H.attributes={foo_H_EAttribute0}

# B class attributes and methods

# foo_D class attributes and methods

# foo_E class attributes and methods

# I class attributes and methods

# foo_I class attributes and methods

# foo_J class attributes and methods

# Relationships
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="foo_B", type=foo_A, multiplicity=Multiplicity(1, 1)),
        Property(name="foo_A", type=foo_B, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
f3: BinaryAssociation = BinaryAssociation(
    name="f3",
    ends={
        Property(name="foo_F", type=foo_B, multiplicity=Multiplicity(1, 1)),
        Property(name="foo_B4", type=foo_F, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref1: BinaryAssociation = BinaryAssociation(
    name="ref1",
    ends={
        Property(name="foo_C", type=foo_A, multiplicity=Multiplicity(1, 1)),
        Property(name="foo_A2", type=foo_C, multiplicity=Multiplicity(0, 1))
    }
)
e5: BinaryAssociation = BinaryAssociation(
    name="e5",
    ends={
        Property(name="foo_E", type=foo_D, multiplicity=Multiplicity(1, 1)),
        Property(name="foo_D", type=foo_E, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_foo_B_J = Generalization(general=J, specific=foo_B)
gen_foo_C_B = Generalization(general=B, specific=foo_C)
gen_foo_D_B = Generalization(general=B, specific=foo_D)
gen_foo_F_I = Generalization(general=I, specific=foo_F)

# Domain Model
domain_model = DomainModel(
    name="foo",
    types={foo_B, foo_A, foo_F, foo_C, J, foo_H, B, foo_D, foo_E, I, foo_I, foo_J},
    associations={b0, f3, ref1, e5},
    generalizations={gen_foo_B_J, gen_foo_C_B, gen_foo_D_B, gen_foo_F_I},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)