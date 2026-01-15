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
employee_NamedEntity = Class(name="employee::NamedEntity")
employee_Company = Class(name="employee::Company")
NamedEntity = Class(name="NamedEntity")
employee_Department = Class(name="employee::Department")
employee_Employee = Class(name="employee::Employee")

# employee_NamedEntity class attributes and methods
employee_NamedEntity_name: Property = Property(name="name", type=StringType)
employee_NamedEntity.attributes={employee_NamedEntity_name}

# employee_Company class attributes and methods

# NamedEntity class attributes and methods

# employee_Department class attributes and methods
employee_Department_isRich: Property = Property(name="isRich", type=BooleanType)
employee_Department.attributes={employee_Department_isRich}

# employee_Employee class attributes and methods
employee_Employee_wage: Property = Property(name="wage", type=IntegerType)
employee_Employee.attributes={employee_Employee_wage}

# Relationships
departments0: BinaryAssociation = BinaryAssociation(
    name="departments0",
    ends={
        Property(name="employee_Department", type=employee_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Company", type=employee_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees1: BinaryAssociation = BinaryAssociation(
    name="employees1",
    ends={
        Property(name="employee_Employee", type=employee_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Department2", type=employee_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_employee_Company_NamedEntity = Generalization(general=NamedEntity, specific=employee_Company)
gen_employee_Department_NamedEntity = Generalization(general=NamedEntity, specific=employee_Department)
gen_employee_Employee_NamedEntity = Generalization(general=NamedEntity, specific=employee_Employee)

# Domain Model
domain_model = DomainModel(
    name="employee",
    types={employee_NamedEntity, employee_Company, NamedEntity, employee_Department, employee_Employee},
    associations={departments0, employees1},
    generalizations={gen_employee_Company_NamedEntity, gen_employee_Department_NamedEntity, gen_employee_Employee_NamedEntity},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)