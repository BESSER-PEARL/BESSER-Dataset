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
company_Company = Class(name="company::Company")
NamedElement = Class(name="NamedElement")
company_Department = Class(name="company::Department")
company_Person = Class(name="company::Person")
company_NamedElement = Class(name="company::NamedElement")

# company_Company class attributes and methods

# NamedElement class attributes and methods

# company_Department class attributes and methods
company_Department_numberOfEmployees: Property = Property(name="numberOfEmployees", type=IntegerType)
company_Department_ageSumOfEmployees: Property = Property(name="ageSumOfEmployees", type=IntegerType)
company_Department.attributes={company_Department_ageSumOfEmployees, company_Department_numberOfEmployees}

# company_Person class attributes and methods
company_Person_firstName: Property = Property(name="firstName", type=StringType)
company_Person_fullName: Property = Property(name="fullName", type=StringType)
company_Person_age: Property = Property(name="age", type=IntegerType)
company_Person.attributes={company_Person_age, company_Person_fullName, company_Person_firstName}

# company_NamedElement class attributes and methods
company_NamedElement_name: Property = Property(name="name", type=StringType)
company_NamedElement.attributes={company_NamedElement_name}

# Relationships
department0: BinaryAssociation = BinaryAssociation(
    name="department0",
    ends={
        Property(name="company_Department", type=company_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Company", type=company_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employee1: BinaryAssociation = BinaryAssociation(
    name="employee1",
    ends={
        Property(name="company_Person", type=company_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Department2", type=company_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supervisor4: BinaryAssociation = BinaryAssociation(
    name="supervisor4",
    ends={
        Property(name="company_Person5", type=company_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Person3", type=company_Person, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_company_Company_NamedElement = Generalization(general=NamedElement, specific=company_Company)
gen_company_Department_NamedElement = Generalization(general=NamedElement, specific=company_Department)
gen_company_Person_NamedElement = Generalization(general=NamedElement, specific=company_Person)

# Domain Model
domain_model = DomainModel(
    name="company",
    types={company_Company, NamedElement, company_Department, company_Person, company_NamedElement},
    associations={department0, employee1, supervisor4},
    generalizations={gen_company_Company_NamedElement, gen_company_Department_NamedElement, gen_company_Person_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)