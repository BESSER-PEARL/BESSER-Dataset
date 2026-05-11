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
testPackage_TestElementA = Class(name="testPackage_TestElementA")
testPackage_Container = Class(name="testPackage_Container")
testPackage_TestElementB = Class(name="testPackage_TestElementB")
TestElementA = Class(name="TestElementA")

# testPackage_TestElementA class attributes and methods
testPackage_TestElementA_name: Property = Property(name="name", type=StringType)
testPackage_TestElementA_multi: Property = Property(name="multi", type=IntegerType)
testPackage_TestElementA.attributes={testPackage_TestElementA_multi, testPackage_TestElementA_name}

# testPackage_Container class attributes and methods

# testPackage_TestElementB class attributes and methods

# TestElementA class attributes and methods

# Relationships
content0: BinaryAssociation = BinaryAssociation(
    name="content0",
    ends={
        Property(name="testPackage_TestElementA", type=testPackage_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="testPackage_Container", type=testPackage_TestElementA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref1: BinaryAssociation = BinaryAssociation(
    name="ref1",
    ends={
        Property(name="testPackage_TestElementA2", type=testPackage_TestElementB, multiplicity=Multiplicity(1, 1)),
        Property(name="testPackage_TestElementB", type=testPackage_TestElementA, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_testPackage_TestElementB_TestElementA = Generalization(general=TestElementA, specific=testPackage_TestElementB)

# Domain Model
domain_model = DomainModel(
    name="testPackage",
    types={testPackage_TestElementA, testPackage_Container, testPackage_TestElementB, TestElementA},
    associations={content0, ref1},
    generalizations={gen_testPackage_TestElementB_TestElementA},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)