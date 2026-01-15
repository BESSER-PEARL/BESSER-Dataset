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
CompanyLanguage_Admin = Class(name="CompanyLanguage::Admin")
CompanyLanguage_CEO = Class(name="CompanyLanguage::CEO")
CompanyLanguage_Employee = Class(name="CompanyLanguage::Employee")
CompanyLanguage_Company = Class(name="CompanyLanguage::Company")

# CompanyLanguage_Admin class attributes and methods
CompanyLanguage_Admin_name: Property = Property(name="name", type=StringType)
CompanyLanguage_Admin.attributes={CompanyLanguage_Admin_name}

# CompanyLanguage_CEO class attributes and methods
CompanyLanguage_CEO_name: Property = Property(name="name", type=StringType)
CompanyLanguage_CEO.attributes={CompanyLanguage_CEO_name}

# CompanyLanguage_Employee class attributes and methods
CompanyLanguage_Employee_name: Property = Property(name="name", type=StringType)
CompanyLanguage_Employee.attributes={CompanyLanguage_Employee_name}

# CompanyLanguage_Company class attributes and methods
CompanyLanguage_Company_name: Property = Property(name="name", type=StringType)
CompanyLanguage_Company.attributes={CompanyLanguage_Company_name}

# Relationships
ceo0: BinaryAssociation = BinaryAssociation(
    name="ceo0",
    ends={
        Property(name="CompanyLanguage_CEO", type=CompanyLanguage_Admin, multiplicity=Multiplicity(1, 1)),
        Property(name="CompanyLanguage_Admin", type=CompanyLanguage_CEO, multiplicity=Multiplicity(0, 1))
    }
)
employee1: BinaryAssociation = BinaryAssociation(
    name="employee1",
    ends={
        Property(name="CompanyLanguage_Employee", type=CompanyLanguage_CEO, multiplicity=Multiplicity(1, 1)),
        Property(name="CompanyLanguage_CEO2", type=CompanyLanguage_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
employee3: BinaryAssociation = BinaryAssociation(
    name="employee3",
    ends={
        Property(name="CompanyLanguage_Employee4", type=CompanyLanguage_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="CompanyLanguage_Company", type=CompanyLanguage_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ceo5: BinaryAssociation = BinaryAssociation(
    name="ceo5",
    ends={
        Property(name="CompanyLanguage_CEO7", type=CompanyLanguage_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="CompanyLanguage_Company6", type=CompanyLanguage_CEO, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
admin8: BinaryAssociation = BinaryAssociation(
    name="admin8",
    ends={
        Property(name="CompanyLanguage_Admin10", type=CompanyLanguage_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="CompanyLanguage_Company9", type=CompanyLanguage_Admin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="CompanyLanguage",
    types={CompanyLanguage_Admin, CompanyLanguage_CEO, CompanyLanguage_Employee, CompanyLanguage_Company},
    associations={ceo0, employee1, employee3, ceo5, admin8},
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