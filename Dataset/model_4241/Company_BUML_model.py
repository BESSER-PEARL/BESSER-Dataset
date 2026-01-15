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
company_Dept = Class(name="company::Dept")
company_Subunit = Class(name="company::Subunit")
company_Person = Class(name="company::Person")
company_Employee = Class(name="company::Employee")

# company_Company class attributes and methods

# company_Dept class attributes and methods
company_Dept_name: Property = Property(name="name", type=StringType)
company_Dept.attributes={company_Dept_name}

# company_Subunit class attributes and methods

# company_Person class attributes and methods
company_Person_name: Property = Property(name="name", type=StringType)
company_Person_address: Property = Property(name="address", type=StringType)
company_Person.attributes={company_Person_name, company_Person_address}

# company_Employee class attributes and methods
company_Employee_salary: Property = Property(name="salary", type=FloatType)
company_Employee.attributes={company_Employee_salary}

# Relationships
depts0: BinaryAssociation = BinaryAssociation(
    name="depts0",
    ends={
        Property(name="company_Dept", type=company_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Company", type=company_Dept, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subunits3: BinaryAssociation = BinaryAssociation(
    name="subunits3",
    ends={
        Property(name="company_Subunit", type=company_Dept, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Dept4", type=company_Subunit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
person5: BinaryAssociation = BinaryAssociation(
    name="person5",
    ends={
        Property(name="company_Person", type=company_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Employee6", type=company_Person, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pu7: BinaryAssociation = BinaryAssociation(
    name="pu7",
    ends={
        Property(name="company_Employee9", type=company_Subunit, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Subunit8", type=company_Employee, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
du10: BinaryAssociation = BinaryAssociation(
    name="du10",
    ends={
        Property(name="company_Dept12", type=company_Subunit, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Subunit11", type=company_Dept, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
manager1: BinaryAssociation = BinaryAssociation(
    name="manager1",
    ends={
        Property(name="company_Employee", type=company_Dept, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Dept2", type=company_Employee, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="company",
    types={company_Company, company_Dept, company_Subunit, company_Person, company_Employee},
    associations={depts0, subunits3, person5, pu7, du10, manager1},
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