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
Employee = Class(name="Employee")
Salary = Class(name="Salary")
Login = Class(name="Login")
Admin = Class(name="Admin")
EmployeeRequest = Class(name="EmployeeRequest")
Attendence = Class(name="Attendence")
payslip = Class(name="payslip")
Loan = Class(name="Loan")

# Employee class attributes and methods
Employee_emp_id: Property = Property(name="emp_id", type=IntegerType)
Employee_emp_name: Property = Property(name="emp_name", type=StringType)
Employee_emp_email: Property = Property(name="emp_email", type=StringType)
Employee.attributes={Employee_emp_id, Employee_emp_name, Employee_emp_email}

# Salary class attributes and methods
Salary_emp_id: Property = Property(name="emp_id", type=IntegerType)
Salary_emp_name: Property = Property(name="emp_name", type=StringType)
Salary_basic_salary: Property = Property(name="basic_salary", type=StringType)
Salary.attributes={Salary_emp_id, Salary_basic_salary, Salary_emp_name}

# Login class attributes and methods
Login_username: Property = Property(name="username", type=StringType)
Login_password: Property = Property(name="password", type=IntegerType)
Login.attributes={Login_password, Login_username}

# Admin class attributes and methods
Admin_adminEmail: Property = Property(name="adminEmail", type=StringType)
Admin_password: Property = Property(name="password", type=IntegerType)
Admin.attributes={Admin_password, Admin_adminEmail}

# EmployeeRequest class attributes and methods

# Attendence class attributes and methods
Attendence_emp_id: Property = Property(name="emp_id", type=IntegerType)
Attendence_emp_name: Property = Property(name="emp_name", type=StringType)
Attendence_Basic_salary: Property = Property(name="Basic_salary", type=IntegerType)
Attendence.attributes={Attendence_emp_name, Attendence_Basic_salary, Attendence_emp_id}

# payslip class attributes and methods
payslip_emp_id: Property = Property(name="emp_id", type=IntegerType)
payslip_emp_name: Property = Property(name="emp_name", type=StringType)
payslip.attributes={payslip_emp_id, payslip_emp_name}

# Loan class attributes and methods
Loan_emp_id: Property = Property(name="emp_id", type=IntegerType)
Loan_emp_name: Property = Property(name="emp_name", type=StringType)
Loan_loan_purpose: Property = Property(name="loan_purpose", type=StringType)
Loan_loan_interst: Property = Property(name="loan_interst", type=IntegerType)
Loan_loan_type: Property = Property(name="loan_type", type=StringType)
Loan_amount: Property = Property(name="amount", type=StringType)
Loan.attributes={Loan_loan_purpose, Loan_loan_type, Loan_emp_name, Loan_amount, Loan_loan_interst, Loan_emp_id}

# Relationships
Attendence_Employee: BinaryAssociation = BinaryAssociation(
    name="Attendence_Employee",
    ends={
        Property(name="employee0", type=Employee, multiplicity=Multiplicity(0, 1)),
        Property(name="attendence1", type=Attendence, multiplicity=Multiplicity(0, 1))
    }
)
Employee_Salary: BinaryAssociation = BinaryAssociation(
    name="Employee_Salary",
    ends={
        Property(name="salary2", type=Salary, multiplicity=Multiplicity(0, 1)),
        Property(name="employee3", type=Employee, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_4_8_wP53EeeLEbIzy5aHfg",
    types={Employee, Salary, Login, Admin, EmployeeRequest, Attendence, payslip, Loan},
    associations={Attendence_Employee, Employee_Salary},
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