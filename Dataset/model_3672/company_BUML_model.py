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
company_Department = Class(name="company::Department")
company_Employee = Class(name="company::Employee")
company_Company = Class(name="company::Company")

# company_Department class attributes and methods
company_Department_name: Property = Property(name="name", type=StringType)
company_Department_budget: Property = Property(name="budget", type=IntegerType)
company_Department.attributes={company_Department_name, company_Department_budget}

# company_Employee class attributes and methods
company_Employee_name: Property = Property(name="name", type=StringType)
company_Employee.attributes={company_Employee_name}

# company_Company class attributes and methods

# Relationships
departments0: BinaryAssociation = BinaryAssociation(
    name="departments0",
    ends={
        Property(name="company_Department", type=company_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Company", type=company_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees1: BinaryAssociation = BinaryAssociation(
    name="employees1",
    ends={
        Property(name="company_Employee", type=company_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Company2", type=company_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees3: BinaryAssociation = BinaryAssociation(
    name="employees3",
    ends={
        Property(name="company_Employee5", type=company_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Department4", type=company_Employee, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="company",
    types={company_Department, company_Employee, company_Company},
    associations={departments0, employees1, employees3},
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