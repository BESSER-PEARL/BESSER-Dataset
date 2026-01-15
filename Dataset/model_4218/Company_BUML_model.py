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
company_Company = Class(name="company::Company")
company_Department = Class(name="company::Department")

# company_Employee class attributes and methods
company_Employee_name: Property = Property(name="name", type=StringType)
company_Employee.attributes={company_Employee_name}

# company_Company class attributes and methods
company_Company_name: Property = Property(name="name", type=StringType)
company_Company.attributes={company_Company_name}

# company_Department class attributes and methods
company_Department_number: Property = Property(name="number", type=IntegerType)
company_Department.attributes={company_Department_number}

# Relationships
department0: BinaryAssociation = BinaryAssociation(
    name="department0",
    ends={
        Property(name="company_Department", type=company_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Company", type=company_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees1: BinaryAssociation = BinaryAssociation(
    name="employees1",
    ends={
        Property(name="company_Employee", type=company_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Department2", type=company_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="company",
    types={company_Employee, company_Company, company_Department},
    associations={department0, employees1},
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