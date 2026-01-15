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
company_TestClass = Class(name="company::TestClass")

# company_Department class attributes and methods
company_Department_number: Property = Property(name="number", type=IntegerType)
company_Department.attributes={company_Department_number}

# company_Employee class attributes and methods
company_Employee_firstName: Property = Property(name="firstName", type=StringType)
company_Employee_lastName: Property = Property(name="lastName", type=StringType)
company_Employee_age: Property = Property(name="age", type=IntegerType)
company_Employee.attributes={company_Employee_age, company_Employee_lastName, company_Employee_firstName}

# company_Company class attributes and methods
company_Company_name: Property = Property(name="name", type=StringType)
company_Company.attributes={company_Company_name}

# company_TestClass class attributes and methods
company_TestClass_stringAttribute1: Property = Property(name="stringAttribute1", type=StringType)
company_TestClass_stringAttribute2: Property = Property(name="stringAttribute2", type=StringType)
company_TestClass_intAttribute1: Property = Property(name="intAttribute1", type=IntegerType)
company_TestClass_intAttribute2: Property = Property(name="intAttribute2", type=IntegerType)
company_TestClass.attributes={company_TestClass_stringAttribute2, company_TestClass_intAttribute1, company_TestClass_stringAttribute1, company_TestClass_intAttribute2}

# Relationships
employees0: BinaryAssociation = BinaryAssociation(
    name="employees0",
    ends={
        Property(name="company_Employee", type=company_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Department", type=company_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
departments1: BinaryAssociation = BinaryAssociation(
    name="departments1",
    ends={
        Property(name="company_Department2", type=company_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Company", type=company_Department, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="company",
    types={company_Department, company_Employee, company_Company, company_TestClass},
    associations={employees0, departments1},
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