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
test_Adown = Class(name="test::Adown")
E = Class(name="E")
test_B = Class(name="test::B")
test_C = Class(name="test::C")
test_D = Class(name="test::D")
test_E = Class(name="test::E")
test_F = Class(name="test::F")

# test_Adown class attributes and methods
test_Adown_newAttribute: Property = Property(name="newAttribute", type=StringType)
test_Adown.attributes={test_Adown_newAttribute}

# E class attributes and methods

# test_B class attributes and methods
test_B_newAttribute: Property = Property(name="newAttribute", type=StringType)
test_B.attributes={test_B_newAttribute}

# test_C class attributes and methods
test_C_newAttribute: Property = Property(name="newAttribute", type=StringType)
test_C.attributes={test_C_newAttribute}

# test_D class attributes and methods
test_D_newAttribute: Property = Property(name="newAttribute", type=StringType)
test_D.attributes={test_D_newAttribute}

# test_E class attributes and methods
test_E_newAttribute2: Property = Property(name="newAttribute2", type=StringType)
test_E.attributes={test_E_newAttribute2}

# test_F class attributes and methods

# Relationships
a4: BinaryAssociation = BinaryAssociation(
    name="a4",
    ends={
        Property(name="Adown", type=test_C, multiplicity=Multiplicity(1, 1)),
        Property(name="c", type=test_Adown, multiplicity=Multiplicity(0, 1))
    }
)
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="test_B", type=test_Adown, multiplicity=Multiplicity(1, 1)),
        Property(name="test_Adown", type=test_B, multiplicity=Multiplicity(0, 1))
    }
)
c1: BinaryAssociation = BinaryAssociation(
    name="c1",
    ends={
        Property(name="C", type=test_Adown, multiplicity=Multiplicity(1, 1)),
        Property(name="a", type=test_C, multiplicity=Multiplicity(0, 1))
    }
)
d2: BinaryAssociation = BinaryAssociation(
    name="d2",
    ends={
        Property(name="test_D", type=test_Adown, multiplicity=Multiplicity(1, 1)),
        Property(name="test_Adown3", type=test_D, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_test_Adown_E = Generalization(general=E, specific=test_Adown)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_Adown, E, test_B, test_C, test_D, test_E, test_F},
    associations={a4, b0, c1, d2},
    generalizations={gen_test_Adown_E},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)