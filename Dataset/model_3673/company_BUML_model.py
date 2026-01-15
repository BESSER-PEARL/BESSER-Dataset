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
company_Employee = Class(name="company::Employee")
company_PhonebookEntry = Class(name="company::PhonebookEntry")
company_Department = Class(name="company::Department")
company_Company = Class(name="company::Company")

# company_Employee class attributes and methods
company_Employee_name: Property = Property(name="name", type=StringType)
company_Employee.attributes={company_Employee_name}

# company_PhonebookEntry class attributes and methods

# company_Department class attributes and methods
company_Department_number: Property = Property(name="number", type=IntegerType)
company_Department.attributes={company_Department_number}

# company_Company class attributes and methods
company_Company_name: Property = Property(name="name", type=StringType)
company_Company.attributes={company_Company_name}

# Relationships
phonebookEntry0: BinaryAssociation = BinaryAssociation(
    name="phonebookEntry0",
    ends={
        Property(name="company_PhonebookEntry", type=company_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Employee", type=company_PhonebookEntry, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
employees1: BinaryAssociation = BinaryAssociation(
    name="employees1",
    ends={
        Property(name="company_Employee2", type=company_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Department", type=company_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manager3: BinaryAssociation = BinaryAssociation(
    name="manager3",
    ends={
        Property(name="company_Employee5", type=company_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Department4", type=company_Employee, multiplicity=Multiplicity(1, 1))
    }
)
departments6: BinaryAssociation = BinaryAssociation(
    name="departments6",
    ends={
        Property(name="company_Department7", type=company_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Company", type=company_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="company",
    types={company_Employee, company_PhonebookEntry, company_Department, company_Company},
    associations={phonebookEntry0, employees1, manager3, departments6},
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