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
test_A = Class(name="test::A")
test_B = Class(name="test::B")
A = Class(name="A")
test_C = Class(name="test::C")
test_D = Class(name="test::D")
test_OptionTestClass = Class(name="test::OptionTestClass")

# test_A class attributes and methods
test_A_m_op1: Method = Method(name="op1", parameters={}, type=StringType)
test_A.methods={test_A_m_op1}

# test_B class attributes and methods

# A class attributes and methods

# test_C class attributes and methods

# test_D class attributes and methods
test_D_attr1: Property = Property(name="attr1", type=StringType)
test_D.attributes={test_D_attr1}

# test_OptionTestClass class attributes and methods
test_OptionTestClass_attribute: Property = Property(name="attribute", type=StringType)
test_OptionTestClass_attribute2: Property = Property(name="attribute2", type=StringType)
test_OptionTestClass.attributes={test_OptionTestClass_attribute2, test_OptionTestClass_attribute}

# Generalizations
gen_test_B_A = Generalization(general=A, specific=test_B)
gen_test_C_A = Generalization(general=A, specific=test_C)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_A, test_B, A, test_C, test_D, test_OptionTestClass},
    associations={},
    generalizations={gen_test_B_A, gen_test_C_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)