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

# Enumerations
Gender: Enumeration = Enumeration(
    name="Gender",
    literals={
            EnumerationLiteral(name="MALE"),
			EnumerationLiteral(name="FEMALE"),
			EnumerationLiteral(name="UNKNOWN")
    }
)

# Classes
test_TestModel = Class(name="test::TestModel")
test_AddressModel = Class(name="test::AddressModel")
test_ConfigurationModel = Class(name="test::ConfigurationModel")

# test_TestModel class attributes and methods
test_TestModel_gender: Property = Property(name="gender", type=StringType)
test_TestModel_name: Property = Property(name="name", type=StringType)
test_TestModel_birthDate: Property = Property(name="birthDate", type=DateType)
test_TestModel_overdrawAccount: Property = Property(name="overdrawAccount", type=StringType)
test_TestModel_childCount: Property = Property(name="childCount", type=StringType)
test_TestModel_age: Property = Property(name="age", type=IntegerType)
test_TestModel_accountBalance: Property = Property(name="accountBalance", type=StringType)
test_TestModel_isSelectable: Property = Property(name="isSelectable", type=StringType)
test_TestModel.attributes={test_TestModel_accountBalance, test_TestModel_isSelectable, test_TestModel_childCount, test_TestModel_age, test_TestModel_name, test_TestModel_overdrawAccount, test_TestModel_gender, test_TestModel_birthDate}

# test_AddressModel class attributes and methods
test_AddressModel_zipCode: Property = Property(name="zipCode", type=StringType)
test_AddressModel_validFrom: Property = Property(name="validFrom", type=DateType)
test_AddressModel_validTo: Property = Property(name="validTo", type=DateType)
test_AddressModel_differentPostAddress: Property = Property(name="differentPostAddress", type=BooleanType)
test_AddressModel_street: Property = Property(name="street", type=StringType)
test_AddressModel_houseNumber: Property = Property(name="houseNumber", type=StringType)
test_AddressModel.attributes={test_AddressModel_validFrom, test_AddressModel_houseNumber, test_AddressModel_zipCode, test_AddressModel_street, test_AddressModel_validTo, test_AddressModel_differentPostAddress}

# test_ConfigurationModel class attributes and methods

# Relationships
address0: BinaryAssociation = BinaryAssociation(
    name="address0",
    ends={
        Property(name="test_AddressModel", type=test_TestModel, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestModel", type=test_AddressModel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
testModels1: BinaryAssociation = BinaryAssociation(
    name="testModels1",
    ends={
        Property(name="test_TestModel2", type=test_ConfigurationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="test_ConfigurationModel", type=test_TestModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
testModel3: BinaryAssociation = BinaryAssociation(
    name="testModel3",
    ends={
        Property(name="test_TestModel5", type=test_ConfigurationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="test_ConfigurationModel4", type=test_TestModel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_TestModel, test_AddressModel, test_ConfigurationModel, Gender},
    associations={address0, testModels1, testModel3},
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