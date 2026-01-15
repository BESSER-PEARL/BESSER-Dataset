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
test_ClassE = Class(name="test::ClassE")
ClassC = Class(name="ClassC")
test_ClassF = Class(name="test::ClassF")
test_Interface4 = Class(name="test::Interface4", is_abstract=True)
test_ClassA = Class(name="test::ClassA")
test_ClassC = Class(name="test::ClassC")
test_ClassB = Class(name="test::ClassB")
Itf1 = Class(name="Itf1")
ClassB = Class(name="ClassB")
test_Itf1 = Class(name="test::Itf1", is_abstract=True)
test_Itf2 = Class(name="test::Itf2", is_abstract=True)
test_Interface3 = Class(name="test::Interface3", is_abstract=True)
test_ClassD = Class(name="test::ClassD")
Interface3 = Class(name="Interface3")
Itf2 = Class(name="Itf2")

# test_ClassE class attributes and methods

# ClassC class attributes and methods

# test_ClassF class attributes and methods

# test_Interface4 class attributes and methods

# test_ClassA class attributes and methods

# test_ClassC class attributes and methods

# test_ClassB class attributes and methods

# Itf1 class attributes and methods

# ClassB class attributes and methods

# test_Itf1 class attributes and methods

# test_Itf2 class attributes and methods

# test_Interface3 class attributes and methods

# test_ClassD class attributes and methods

# Interface3 class attributes and methods

# Itf2 class attributes and methods

# Relationships
a1: BinaryAssociation = BinaryAssociation(
    name="a1",
    ends={
        Property(name="test_ClassA", type=test_ClassA, multiplicity=Multiplicity(1, 1)),
        Property(name="test_ClassA0", type=test_ClassA, multiplicity=Multiplicity(0, 1))
    }
)
cfghdtgh2: BinaryAssociation = BinaryAssociation(
    name="cfghdtgh2",
    ends={
        Property(name="test_ClassC", type=test_ClassA, multiplicity=Multiplicity(1, 1)),
        Property(name="test_ClassA3", type=test_ClassC, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_test_ClassE_ClassC = Generalization(general=ClassC, specific=test_ClassE)
gen_test_ClassE_Interface3 = Generalization(general=Interface3, specific=test_ClassE)
gen_test_ClassB_Itf1 = Generalization(general=Itf1, specific=test_ClassB)
gen_test_ClassC_ClassB = Generalization(general=ClassB, specific=test_ClassC)
gen_test_ClassD_Interface3 = Generalization(general=Interface3, specific=test_ClassD)
gen_test_ClassD_Itf1 = Generalization(general=Itf1, specific=test_ClassD)
gen_test_ClassD_Itf2 = Generalization(general=Itf2, specific=test_ClassD)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_ClassE, ClassC, test_ClassF, test_Interface4, test_ClassA, test_ClassC, test_ClassB, Itf1, ClassB, test_Itf1, test_Itf2, test_Interface3, test_ClassD, Interface3, Itf2},
    associations={a1, cfghdtgh2},
    generalizations={gen_test_ClassE_ClassC, gen_test_ClassE_Interface3, gen_test_ClassB_Itf1, gen_test_ClassC_ClassB, gen_test_ClassD_Interface3, gen_test_ClassD_Itf1, gen_test_ClassD_Itf2},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)