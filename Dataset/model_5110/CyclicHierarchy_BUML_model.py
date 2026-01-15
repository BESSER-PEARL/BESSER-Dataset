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
SuperType = Class(name="SuperType")
SubType = Class(name="SubType")
testPackage_SuperType = Class(name="testPackage::SuperType")
testPackage_SubSubType = Class(name="testPackage::SubSubType")
testPackage_SubType = Class(name="testPackage::SubType")

# SuperType class attributes and methods

# SubType class attributes and methods

# testPackage_SuperType class attributes and methods

# testPackage_SubSubType class attributes and methods

# testPackage_SubType class attributes and methods

# Relationships
knownDerived0: BinaryAssociation = BinaryAssociation(
    name="knownDerived0",
    ends={
        Property(name="testPackage_SubSubType", type=testPackage_SuperType, multiplicity=Multiplicity(1, 1)),
        Property(name="testPackage_SuperType", type=testPackage_SubSubType, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_testPackage_SubType_SuperType = Generalization(general=SuperType, specific=testPackage_SubType)
gen_testPackage_SubSubType_SubType = Generalization(general=SubType, specific=testPackage_SubSubType)

# Domain Model
domain_model = DomainModel(
    name="testPackage",
    types={SuperType, SubType, testPackage_SuperType, testPackage_SubSubType, testPackage_SubType},
    associations={knownDerived0},
    generalizations={gen_testPackage_SubType_SuperType, gen_testPackage_SubSubType_SubType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)