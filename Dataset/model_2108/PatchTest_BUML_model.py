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
test_PatchTestModel = Class(name="test::PatchTestModel")
test_SomeTestClass = Class(name="test::SomeTestClass")
test_SomeTestClassWithID = Class(name="test::SomeTestClassWithID")
SomeTestClass = Class(name="SomeTestClass")

# test_PatchTestModel class attributes and methods
test_PatchTestModel_id: Property = Property(name="id", type=StringType)
test_PatchTestModel_oneAttribute: Property = Property(name="oneAttribute", type=StringType)
test_PatchTestModel_multiAttribute: Property = Property(name="multiAttribute", type=StringType)
test_PatchTestModel.attributes={test_PatchTestModel_multiAttribute, test_PatchTestModel_oneAttribute, test_PatchTestModel_id}

# test_SomeTestClass class attributes and methods
test_SomeTestClass_attribute: Property = Property(name="attribute", type=StringType)
test_SomeTestClass.attributes={test_SomeTestClass_attribute}

# test_SomeTestClassWithID class attributes and methods
test_SomeTestClassWithID_id: Property = Property(name="id", type=StringType)
test_SomeTestClassWithID.attributes={test_SomeTestClassWithID_id}

# SomeTestClass class attributes and methods

# Relationships
oneNonContainmentReference0: BinaryAssociation = BinaryAssociation(
    name="oneNonContainmentReference0",
    ends={
        Property(name="test_SomeTestClass", type=test_PatchTestModel, multiplicity=Multiplicity(1, 1)),
        Property(name="test_PatchTestModel", type=test_SomeTestClass, multiplicity=Multiplicity(0, 1))
    }
)
multiNonContainmentReferences1: BinaryAssociation = BinaryAssociation(
    name="multiNonContainmentReferences1",
    ends={
        Property(name="test_SomeTestClass3", type=test_PatchTestModel, multiplicity=Multiplicity(1, 1)),
        Property(name="test_PatchTestModel2", type=test_SomeTestClass, multiplicity=Multiplicity(0, 9999))
    }
)
oneContainmentReference4: BinaryAssociation = BinaryAssociation(
    name="oneContainmentReference4",
    ends={
        Property(name="test_SomeTestClass6", type=test_PatchTestModel, multiplicity=Multiplicity(1, 1)),
        Property(name="test_PatchTestModel5", type=test_SomeTestClass, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiContainmentReference7: BinaryAssociation = BinaryAssociation(
    name="multiContainmentReference7",
    ends={
        Property(name="test_SomeTestClass9", type=test_PatchTestModel, multiplicity=Multiplicity(1, 1)),
        Property(name="test_PatchTestModel8", type=test_SomeTestClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_test_SomeTestClassWithID_SomeTestClass = Generalization(general=SomeTestClass, specific=test_SomeTestClassWithID)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_PatchTestModel, test_SomeTestClass, test_SomeTestClassWithID, SomeTestClass},
    associations={oneNonContainmentReference0, multiNonContainmentReferences1, oneContainmentReference4, multiContainmentReference7},
    generalizations={gen_test_SomeTestClassWithID_SomeTestClass},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)