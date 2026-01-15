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
testModel_AClass = Class(name="testModel::AClass")
testModel_BClass = Class(name="testModel::BClass")
AClass = Class(name="AClass")
testModel_CClass = Class(name="testModel::CClass")
BClass = Class(name="BClass")
testModel_EObject = Class(name="testModel::EObject")

# testModel_AClass class attributes and methods
testModel_AClass_AClassAttr1: Property = Property(name="AClassAttr1", type=BooleanType)
testModel_AClass_AClassAttr2: Property = Property(name="AClassAttr2", type=StringType)
testModel_AClass.attributes={testModel_AClass_AClassAttr1, testModel_AClass_AClassAttr2}

# testModel_BClass class attributes and methods
testModel_BClass_BClassAttr1: Property = Property(name="BClassAttr1", type=BooleanType)
testModel_BClass_BClassAttr2: Property = Property(name="BClassAttr2", type=StringType)
testModel_BClass.attributes={testModel_BClass_BClassAttr2, testModel_BClass_BClassAttr1}

# AClass class attributes and methods

# testModel_CClass class attributes and methods
testModel_CClass_CClassAttr1: Property = Property(name="CClassAttr1", type=BooleanType)
testModel_CClass_CClassAttr2: Property = Property(name="CClassAttr2", type=StringType)
testModel_CClass.attributes={testModel_CClass_CClassAttr2, testModel_CClass_CClassAttr1}

# BClass class attributes and methods

# testModel_EObject class attributes and methods

# Relationships
AClassRef10: BinaryAssociation = BinaryAssociation(
    name="AClassRef10",
    ends={
        Property(name="testModel_BClass", type=testModel_AClass, multiplicity=Multiplicity(1, 1)),
        Property(name="testModel_AClass", type=testModel_BClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
BClassRef11: BinaryAssociation = BinaryAssociation(
    name="BClassRef11",
    ends={
        Property(name="testModel_CClass", type=testModel_BClass, multiplicity=Multiplicity(1, 1)),
        Property(name="testModel_BClass2", type=testModel_CClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
CClassRef13: BinaryAssociation = BinaryAssociation(
    name="CClassRef13",
    ends={
        Property(name="testModel_EObject", type=testModel_CClass, multiplicity=Multiplicity(1, 1)),
        Property(name="testModel_CClass4", type=testModel_EObject, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_testModel_BClass_AClass = Generalization(general=AClass, specific=testModel_BClass)
gen_testModel_CClass_BClass = Generalization(general=BClass, specific=testModel_CClass)

# Domain Model
domain_model = DomainModel(
    name="testModel",
    types={testModel_AClass, testModel_BClass, AClass, testModel_CClass, BClass, testModel_EObject},
    associations={AClassRef10, BClassRef11, CClassRef13},
    generalizations={gen_testModel_BClass_AClass, gen_testModel_CClass_BClass},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)