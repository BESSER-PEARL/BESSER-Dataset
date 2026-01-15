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
testPackage_SuperSuperClass = Class(name="testPackage::SuperSuperClass")
testPackage_SuperClass = Class(name="testPackage::SuperClass")
SuperSuperClass = Class(name="SuperSuperClass")
testPackage_DerivedClass = Class(name="testPackage::DerivedClass")
SuperClass = Class(name="SuperClass")

# testPackage_SuperSuperClass class attributes and methods

# testPackage_SuperClass class attributes and methods

# SuperSuperClass class attributes and methods

# testPackage_DerivedClass class attributes and methods

# SuperClass class attributes and methods

# Generalizations
gen_testPackage_SuperClass_SuperSuperClass = Generalization(general=SuperSuperClass, specific=testPackage_SuperClass)
gen_testPackage_DerivedClass_SuperClass = Generalization(general=SuperClass, specific=testPackage_DerivedClass)
gen_testPackage_DerivedClass_SuperSuperClass = Generalization(general=SuperSuperClass, specific=testPackage_DerivedClass)

# Domain Model
domain_model = DomainModel(
    name="testPackage",
    types={testPackage_SuperSuperClass, testPackage_SuperClass, SuperSuperClass, testPackage_DerivedClass, SuperClass},
    associations={},
    generalizations={gen_testPackage_SuperClass_SuperSuperClass, gen_testPackage_DerivedClass_SuperClass, gen_testPackage_DerivedClass_SuperSuperClass},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)