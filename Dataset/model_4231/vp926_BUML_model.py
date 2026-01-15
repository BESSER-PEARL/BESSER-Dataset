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
employee_Employee = Class(name="employee::Employee")
employee_Company = Class(name="employee::Company")
NamedEntity = Class(name="NamedEntity")
employee_Department = Class(name="employee::Department")
employee_RichDepartment = Class(name="employee::RichDepartment")
Department = Class(name="Department")
employee_PoorDepartment = Class(name="employee::PoorDepartment")
employee_NamedEntity = Class(name="employee::NamedEntity")

# employee_Employee class attributes and methods
employee_Employee_wage: Property = Property(name="wage", type=IntegerType)
employee_Employee.attributes={employee_Employee_wage}

# employee_Company class attributes and methods

# NamedEntity class attributes and methods

# employee_Department class attributes and methods

# employee_RichDepartment class attributes and methods

# Department class attributes and methods

# employee_PoorDepartment class attributes and methods

# employee_NamedEntity class attributes and methods
employee_NamedEntity_name: Property = Property(name="name", type=StringType)
employee_NamedEntity.attributes={employee_NamedEntity_name}

# Relationships
employees1: BinaryAssociation = BinaryAssociation(
    name="employees1",
    ends={
        Property(name="employee_Employee", type=employee_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Department2", type=employee_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
departments0: BinaryAssociation = BinaryAssociation(
    name="departments0",
    ends={
        Property(name="employee_Department", type=employee_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Company", type=employee_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_employee_Employee_NamedEntity = Generalization(general=NamedEntity, specific=employee_Employee)
gen_employee_Company_NamedEntity = Generalization(general=NamedEntity, specific=employee_Company)
gen_employee_RichDepartment_Department = Generalization(general=Department, specific=employee_RichDepartment)
gen_employee_PoorDepartment_Department = Generalization(general=Department, specific=employee_PoorDepartment)
gen_employee_Department_NamedEntity = Generalization(general=NamedEntity, specific=employee_Department)

# Domain Model
domain_model = DomainModel(
    name="employee",
    types={employee_Employee, employee_Company, NamedEntity, employee_Department, employee_RichDepartment, Department, employee_PoorDepartment, employee_NamedEntity},
    associations={employees1, departments0},
    generalizations={gen_employee_Employee_NamedEntity, gen_employee_Company_NamedEntity, gen_employee_RichDepartment_Department, gen_employee_PoorDepartment_Department, gen_employee_Department_NamedEntity},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)