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
generictest_Door = Class(name="generictest::Door")
generictest_ReffedClass = Class(name="generictest::ReffedClass")
GenericSuperClassBound = Class(name="GenericSuperClassBound")
generictest_NextGenSuperClass = Class(name="generictest::NextGenSuperClass")
generictest_TypeArgReferencedOnlyExternally = Class(name="generictest::TypeArgReferencedOnlyExternally")
generictest_GenRef = Class(name="generictest::GenRef")
generictest_TypeArgForRef = Class(name="generictest::TypeArgForRef")
generictest_NonGenericSuperclass = Class(name="generictest::NonGenericSuperclass")
SuperReffedClass = Class(name="SuperReffedClass")
generictest_SuperReffedClass = Class(name="generictest::SuperReffedClass")
generictest_GenericSuperClass = Class(name="generictest::GenericSuperClass")
generictest_GenericSuperClassBound = Class(name="generictest::GenericSuperClassBound")
generictest_TypeArgForGenericSuperClass = Class(name="generictest::TypeArgForGenericSuperClass")

# generictest_Door class attributes and methods

# generictest_ReffedClass class attributes and methods

# GenericSuperClassBound class attributes and methods

# generictest_NextGenSuperClass class attributes and methods

# generictest_TypeArgReferencedOnlyExternally class attributes and methods

# generictest_GenRef class attributes and methods

# generictest_TypeArgForRef class attributes and methods

# generictest_NonGenericSuperclass class attributes and methods

# SuperReffedClass class attributes and methods

# generictest_SuperReffedClass class attributes and methods

# generictest_GenericSuperClass class attributes and methods

# generictest_GenericSuperClassBound class attributes and methods

# generictest_TypeArgForGenericSuperClass class attributes and methods

# Relationships
reffedclass0: BinaryAssociation = BinaryAssociation(
    name="reffedclass0",
    ends={
        Property(name="generictest_ReffedClass", type=generictest_Door, multiplicity=Multiplicity(1, 1)),
        Property(name="generictest_Door", type=generictest_ReffedClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_generictest_TypeArgForGenericSuperClass_GenericSuperClassBound = Generalization(general=GenericSuperClassBound, specific=generictest_TypeArgForGenericSuperClass)
gen_generictest_ReffedClass_SuperReffedClass = Generalization(general=SuperReffedClass, specific=generictest_ReffedClass)

# Domain Model
domain_model = DomainModel(
    name="generictest",
    types={generictest_Door, generictest_ReffedClass, GenericSuperClassBound, generictest_NextGenSuperClass, generictest_TypeArgReferencedOnlyExternally, generictest_GenRef, generictest_TypeArgForRef, generictest_NonGenericSuperclass, SuperReffedClass, generictest_SuperReffedClass, generictest_GenericSuperClass, generictest_GenericSuperClassBound, generictest_TypeArgForGenericSuperClass},
    associations={reffedclass0},
    generalizations={gen_generictest_TypeArgForGenericSuperClass_GenericSuperClassBound, gen_generictest_ReffedClass_SuperReffedClass},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)