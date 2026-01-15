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
companies_employee = Class(name="companies::employee")
companies_company = Class(name="companies::company")
CSTrace = Class(name="CSTrace")
companies_department = Class(name="companies::department")
companies_department_manager = Class(name="companies::department::manager")
companies_department_employees = Class(name="companies::department::employees")
companies_CSTrace = Class(name="companies::CSTrace", is_abstract=True)
companies_Visitable = Class(name="companies::Visitable")

# companies_employee class attributes and methods
companies_employee_name: Property = Property(name="name", type=StringType)
companies_employee_address: Property = Property(name="address", type=StringType)
companies_employee_salary: Property = Property(name="salary", type=FloatType)
companies_employee_mentor: Property = Property(name="mentor", type=StringType)
companies_employee.attributes={companies_employee_name, companies_employee_address, companies_employee_mentor, companies_employee_salary}

# companies_company class attributes and methods
companies_company_name: Property = Property(name="name", type=StringType)
companies_company.attributes={companies_company_name}

# CSTrace class attributes and methods

# companies_department class attributes and methods
companies_department_name: Property = Property(name="name", type=StringType)
companies_department.attributes={companies_department_name}

# companies_department_manager class attributes and methods

# companies_department_employees class attributes and methods

# companies_CSTrace class attributes and methods

# companies_Visitable class attributes and methods

# Relationships
department_employees3: BinaryAssociation = BinaryAssociation(
    name="department_employees3",
    ends={
        Property(name="companies_department4", type=companies_department_employees, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="companies_department_employees", type=companies_department, multiplicity=Multiplicity(1, 1))
    }
)
deparment6: BinaryAssociation = BinaryAssociation(
    name="deparment6",
    ends={
        Property(name="companies_department7", type=companies_department, multiplicity=Multiplicity(1, 1)),
        Property(name="companies_department5", type=companies_department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employee8: BinaryAssociation = BinaryAssociation(
    name="employee8",
    ends={
        Property(name="companies_employee", type=companies_department_manager, multiplicity=Multiplicity(1, 1)),
        Property(name="companies_department_manager9", type=companies_employee, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
deparment0: BinaryAssociation = BinaryAssociation(
    name="deparment0",
    ends={
        Property(name="companies_department", type=companies_company, multiplicity=Multiplicity(1, 1)),
        Property(name="companies_company", type=companies_department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
department_manager1: BinaryAssociation = BinaryAssociation(
    name="department_manager1",
    ends={
        Property(name="companies_department_manager", type=companies_department, multiplicity=Multiplicity(1, 1)),
        Property(name="companies_department2", type=companies_department_manager, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
employee10: BinaryAssociation = BinaryAssociation(
    name="employee10",
    ends={
        Property(name="companies_employee12", type=companies_department_employees, multiplicity=Multiplicity(1, 1)),
        Property(name="companies_department_employees11", type=companies_employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ast13: BinaryAssociation = BinaryAssociation(
    name="ast13",
    ends={
        Property(name="companies_Visitable", type=companies_CSTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="companies_CSTrace", type=companies_Visitable, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_companies_department_manager_CSTrace = Generalization(general=CSTrace, specific=companies_department_manager)
gen_companies_company_CSTrace = Generalization(general=CSTrace, specific=companies_company)
gen_companies_department_CSTrace = Generalization(general=CSTrace, specific=companies_department)
gen_companies_department_employees_CSTrace = Generalization(general=CSTrace, specific=companies_department_employees)
gen_companies_employee_CSTrace = Generalization(general=CSTrace, specific=companies_employee)

# Domain Model
domain_model = DomainModel(
    name="companies",
    types={companies_employee, companies_company, CSTrace, companies_department, companies_department_manager, companies_department_employees, companies_CSTrace, companies_Visitable},
    associations={department_employees3, deparment6, employee8, deparment0, department_manager1, employee10, ast13},
    generalizations={gen_companies_department_manager_CSTrace, gen_companies_company_CSTrace, gen_companies_department_CSTrace, gen_companies_department_employees_CSTrace, gen_companies_employee_CSTrace},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)