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
            EnumerationLiteral(name="male"),
			EnumerationLiteral(name="female")
    }
)

# Classes
company_Person = Class(name="company::Person")
company_Company = Class(name="company::Company")

# company_Person class attributes and methods
company_Person_name: Property = Property(name="name", type=StringType)
company_Person_lastname: Property = Property(name="lastname", type=StringType)
company_Person_gender: Property = Property(name="gender", type=StringType)
company_Person_age: Property = Property(name="age", type=IntegerType)
company_Person_isUnemployed: Property = Property(name="isUnemployed", type=BooleanType)
company_Person_salary: Property = Property(name="salary", type=IntegerType)
company_Person.attributes={company_Person_age, company_Person_gender, company_Person_name, company_Person_isUnemployed, company_Person_lastname, company_Person_salary}

# company_Company class attributes and methods
company_Company_name: Property = Property(name="name", type=StringType)
company_Company_numberOfManager: Property = Property(name="numberOfManager", type=IntegerType)
company_Company.attributes={company_Company_name, company_Company_numberOfManager}

# Relationships
managerCompanies0: BinaryAssociation = BinaryAssociation(
    name="managerCompanies0",
    ends={
        Property(name="Company", type=company_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="manager", type=company_Company, multiplicity=Multiplicity(0, 1))
    }
)
manager1: BinaryAssociation = BinaryAssociation(
    name="manager1",
    ends={
        Property(name="Person", type=company_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="managerCompanies", type=company_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="company",
    types={company_Person, company_Company, Gender},
    associations={managerCompanies0, manager1},
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