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
_101companies_Company = Class(name="::101companies::Company")
_101companies_Department = Class(name="::101companies::Department")
_101companies_Employee = Class(name="::101companies::Employee")

# _101companies_Company class attributes and methods
_101companies_Company_name: Property = Property(name="name", type=StringType)
_101companies_Company_totalSalary: Property = Property(name="totalSalary", type=FloatType)
_101companies_Company.attributes={_101companies_Company_name, _101companies_Company_totalSalary}

# _101companies_Department class attributes and methods
_101companies_Department_name: Property = Property(name="name", type=StringType)
_101companies_Department_totalSalary: Property = Property(name="totalSalary", type=FloatType)
_101companies_Department.attributes={_101companies_Department_name, _101companies_Department_totalSalary}

# _101companies_Employee class attributes and methods
_101companies_Employee_name: Property = Property(name="name", type=StringType)
_101companies_Employee_address: Property = Property(name="address", type=StringType)
_101companies_Employee_salary: Property = Property(name="salary", type=FloatType)
_101companies_Employee.attributes={_101companies_Employee_salary, _101companies_Employee_address, _101companies_Employee_name}

# Relationships
employees3: BinaryAssociation = BinaryAssociation(
    name="employees3",
    ends={
        Property(name="_101companies_Employee5", type=_101companies_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="_101companies_Department4", type=_101companies_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
departments0: BinaryAssociation = BinaryAssociation(
    name="departments0",
    ends={
        Property(name="_101companies_Department", type=_101companies_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="_101companies_Company", type=_101companies_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manager1: BinaryAssociation = BinaryAssociation(
    name="manager1",
    ends={
        Property(name="_101companies_Employee", type=_101companies_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="_101companies_Department2", type=_101companies_Employee, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subdepartments7: BinaryAssociation = BinaryAssociation(
    name="subdepartments7",
    ends={
        Property(name="_101companies_Department8", type=_101companies_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="_101companies_Department6", type=_101companies_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="_101companies",
    types={_101companies_Company, _101companies_Department, _101companies_Employee},
    associations={employees3, departments0, manager1, subdepartments7},
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