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
person_CompanyType = Class(name="person::CompanyType")
person_PersonType = Class(name="person::PersonType")
person_DocumentRoot = Class(name="person::DocumentRoot")
person_EStringToStringMapEntry = Class(name="person::EStringToStringMapEntry")

# person_CompanyType class attributes and methods

# person_PersonType class attributes and methods
person_PersonType_age: Property = Property(name="age", type=StringType)
person_PersonType_email: Property = Property(name="email", type=StringType)
person_PersonType_name: Property = Property(name="name", type=StringType)
person_PersonType_country: Property = Property(name="country", type=StringType)
person_PersonType.attributes={person_PersonType_age, person_PersonType_name, person_PersonType_country, person_PersonType_email}

# person_DocumentRoot class attributes and methods
person_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
person_DocumentRoot.attributes={person_DocumentRoot_mixed}

# person_EStringToStringMapEntry class attributes and methods

# Relationships
person0: BinaryAssociation = BinaryAssociation(
    name="person0",
    ends={
        Property(name="person_PersonType", type=person_CompanyType, multiplicity=Multiplicity(1, 1)),
        Property(name="person_CompanyType", type=person_PersonType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
xMLNSPrefixMap1: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap1",
    ends={
        Property(name="person_EStringToStringMapEntry", type=person_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="person_DocumentRoot", type=person_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation2: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation2",
    ends={
        Property(name="person_EStringToStringMapEntry4", type=person_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="person_DocumentRoot3", type=person_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
company5: BinaryAssociation = BinaryAssociation(
    name="company5",
    ends={
        Property(name="person_CompanyType7", type=person_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="person_DocumentRoot6", type=person_CompanyType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="person",
    types={person_CompanyType, person_PersonType, person_DocumentRoot, person_EStringToStringMapEntry},
    associations={person0, xMLNSPrefixMap1, xSISchemaLocation2, company5},
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