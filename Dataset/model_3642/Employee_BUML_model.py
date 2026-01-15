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
employee_Company = Class(name="employee::Company")
employee_Employee = Class(name="employee::Employee")
employee_Department = Class(name="employee::Department")

# employee_Company class attributes and methods
employee_Company_name: Property = Property(name="name", type=StringType)
employee_Company.attributes={employee_Company_name}

# employee_Employee class attributes and methods
employee_Employee_empID: Property = Property(name="empID", type=IntegerType)
employee_Employee_name: Property = Property(name="name", type=StringType)
employee_Employee_isManager: Property = Property(name="isManager", type=BooleanType)
employee_Employee_m_allReports: Method = Method(name="allReports", parameters={}, type=StringType)
employee_Employee_m_reportingChain: Method = Method(name="reportingChain", parameters={}, type=StringType)
employee_Employee_m_reportsTo: Method = Method(name="reportsTo", parameters={Parameter(name='mgr')}, type=BooleanType)
employee_Employee.attributes={employee_Employee_name, employee_Employee_isManager, employee_Employee_empID}
employee_Employee.methods={employee_Employee_m_allReports, employee_Employee_m_reportingChain, employee_Employee_m_reportsTo}

# employee_Department class attributes and methods
employee_Department_deptID: Property = Property(name="deptID", type=IntegerType)
employee_Department_name: Property = Property(name="name", type=StringType)
employee_Department.attributes={employee_Department_deptID, employee_Department_name}

# Relationships
employees0: BinaryAssociation = BinaryAssociation(
    name="employees0",
    ends={
        Property(name="Employee", type=employee_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company", type=employee_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees4: BinaryAssociation = BinaryAssociation(
    name="employees4",
    ends={
        Property(name="Employee5", type=employee_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="department", type=employee_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
company6: BinaryAssociation = BinaryAssociation(
    name="company6",
    ends={
        Property(name="Company", type=employee_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="departments", type=employee_Company, multiplicity=Multiplicity(0, 1))
    }
)
departments1: BinaryAssociation = BinaryAssociation(
    name="departments1",
    ends={
        Property(name="Department", type=employee_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company2", type=employee_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manager3: BinaryAssociation = BinaryAssociation(
    name="manager3",
    ends={
        Property(name="employee_Employee", type=employee_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="employee_Department", type=employee_Employee, multiplicity=Multiplicity(0, 1))
    }
)
department7: BinaryAssociation = BinaryAssociation(
    name="department7",
    ends={
        Property(name="Department8", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employees", type=employee_Department, multiplicity=Multiplicity(0, 1))
    }
)
manager10: BinaryAssociation = BinaryAssociation(
    name="manager10",
    ends={
        Property(name="Employee11", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="directReports", type=employee_Employee, multiplicity=Multiplicity(0, 1))
    }
)
directReports13: BinaryAssociation = BinaryAssociation(
    name="directReports13",
    ends={
        Property(name="Employee14", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="manager", type=employee_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
company15: BinaryAssociation = BinaryAssociation(
    name="company15",
    ends={
        Property(name="Company17", type=employee_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employees16", type=employee_Company, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="employee",
    types={employee_Company, employee_Employee, employee_Department},
    associations={employees0, employees4, company6, departments1, manager3, department7, manager10, directReports13, company15},
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