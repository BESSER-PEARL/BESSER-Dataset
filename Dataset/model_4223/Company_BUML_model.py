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
company_Department = Class(name="company::Department")
company_Employee = Class(name="company::Employee")

# company_Company class attributes and methods
company_Company_name: Property = Property(name="name", type=StringType)
company_Company.attributes={company_Company_name}

# company_Department class attributes and methods
company_Department_name: Property = Property(name="name", type=StringType)
company_Department.attributes={company_Department_name}

# company_Employee class attributes and methods
company_Employee_name: Property = Property(name="name", type=StringType)
company_Employee_address: Property = Property(name="address", type=StringType)
company_Employee_salary: Property = Property(name="salary", type=FloatType)
company_Employee.attributes={company_Employee_name, company_Employee_address, company_Employee_salary}

# Relationships
depts0: BinaryAssociation = BinaryAssociation(
    name="depts0",
    ends={
        Property(name="company_Department", type=company_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Company", type=company_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manager1: BinaryAssociation = BinaryAssociation(
    name="manager1",
    ends={
        Property(name="company_Employee", type=company_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Department2", type=company_Employee, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subdepts4: BinaryAssociation = BinaryAssociation(
    name="subdepts4",
    ends={
        Property(name="company_Department5", type=company_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Department3", type=company_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees6: BinaryAssociation = BinaryAssociation(
    name="employees6",
    ends={
        Property(name="company_Employee8", type=company_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Department7", type=company_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mentor10: BinaryAssociation = BinaryAssociation(
    name="mentor10",
    ends={
        Property(name="company_Employee11", type=company_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Employee9", type=company_Employee, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="company",
    types={company_Company, company_Department, company_Employee},
    associations={depts0, manager1, subdepts4, employees6, mentor10},
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