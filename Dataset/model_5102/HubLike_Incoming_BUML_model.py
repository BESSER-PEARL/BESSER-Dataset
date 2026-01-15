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
testPackage_Class5 = Class(name="testPackage::Class5")
testPackage_HubClass = Class(name="testPackage::HubClass")
testPackage_Class1 = Class(name="testPackage::Class1")
testPackage_Class2 = Class(name="testPackage::Class2")
testPackage_Class3 = Class(name="testPackage::Class3")
testPackage_Class4 = Class(name="testPackage::Class4")

# testPackage_Class5 class attributes and methods

# testPackage_HubClass class attributes and methods

# testPackage_Class1 class attributes and methods

# testPackage_Class2 class attributes and methods

# testPackage_Class3 class attributes and methods

# testPackage_Class4 class attributes and methods

# Relationships
testReference7: BinaryAssociation = BinaryAssociation(
    name="testReference7",
    ends={
        Property(name="testPackage_HubClass8", type=testPackage_Class5, multiplicity=Multiplicity(1, 1)),
        Property(name="testPackage_Class5", type=testPackage_HubClass, multiplicity=Multiplicity(0, 1))
    }
)
testReference0: BinaryAssociation = BinaryAssociation(
    name="testReference0",
    ends={
        Property(name="testPackage_HubClass", type=testPackage_Class1, multiplicity=Multiplicity(1, 1)),
        Property(name="testPackage_Class1", type=testPackage_HubClass, multiplicity=Multiplicity(0, 1))
    }
)
testReference1: BinaryAssociation = BinaryAssociation(
    name="testReference1",
    ends={
        Property(name="testPackage_HubClass2", type=testPackage_Class2, multiplicity=Multiplicity(1, 1)),
        Property(name="testPackage_Class2", type=testPackage_HubClass, multiplicity=Multiplicity(0, 1))
    }
)
testReference3: BinaryAssociation = BinaryAssociation(
    name="testReference3",
    ends={
        Property(name="testPackage_HubClass4", type=testPackage_Class3, multiplicity=Multiplicity(1, 1)),
        Property(name="testPackage_Class3", type=testPackage_HubClass, multiplicity=Multiplicity(0, 1))
    }
)
testReference5: BinaryAssociation = BinaryAssociation(
    name="testReference5",
    ends={
        Property(name="testPackage_HubClass6", type=testPackage_Class4, multiplicity=Multiplicity(1, 1)),
        Property(name="testPackage_Class4", type=testPackage_HubClass, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="testPackage",
    types={testPackage_Class5, testPackage_HubClass, testPackage_Class1, testPackage_Class2, testPackage_Class3, testPackage_Class4},
    associations={testReference7, testReference0, testReference1, testReference3, testReference5},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)