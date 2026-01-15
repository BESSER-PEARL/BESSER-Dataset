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
testPackage_FirstClass = Class(name="testPackage::FirstClass")
testPackage_SecondClass = Class(name="testPackage::SecondClass")
testPackage_FirstSubClass = Class(name="testPackage::FirstSubClass")
FirstClass = Class(name="FirstClass")
testPackage_SecondSubClass = Class(name="testPackage::SecondSubClass")
SecondClass = Class(name="SecondClass")

# testPackage_FirstClass class attributes and methods

# testPackage_SecondClass class attributes and methods

# testPackage_FirstSubClass class attributes and methods

# FirstClass class attributes and methods

# testPackage_SecondSubClass class attributes and methods

# SecondClass class attributes and methods

# Relationships
testReference0: BinaryAssociation = BinaryAssociation(
    name="testReference0",
    ends={
        Property(name="testPackage_SecondClass", type=testPackage_FirstClass, multiplicity=Multiplicity(1, 1)),
        Property(name="testPackage_FirstClass", type=testPackage_SecondClass, multiplicity=Multiplicity(0, 1))
    }
)
specializationReference1: BinaryAssociation = BinaryAssociation(
    name="specializationReference1",
    ends={
        Property(name="testPackage_SecondSubClass", type=testPackage_FirstSubClass, multiplicity=Multiplicity(1, 1)),
        Property(name="testPackage_FirstSubClass", type=testPackage_SecondSubClass, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_testPackage_FirstSubClass_FirstClass = Generalization(general=FirstClass, specific=testPackage_FirstSubClass)
gen_testPackage_SecondSubClass_SecondClass = Generalization(general=SecondClass, specific=testPackage_SecondSubClass)

# Domain Model
domain_model = DomainModel(
    name="testPackage",
    types={testPackage_FirstClass, testPackage_SecondClass, testPackage_FirstSubClass, FirstClass, testPackage_SecondSubClass, SecondClass},
    associations={testReference0, specializationReference1},
    generalizations={gen_testPackage_FirstSubClass_FirstClass, gen_testPackage_SecondSubClass_SecondClass},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)