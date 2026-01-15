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
company_Employee = Class(name="company::Employee")
company_Department = Class(name="company::Department")
company_Division = Class(name="company::Division")
company_Student = Class(name="company::Student")
company_Freelance = Class(name="company::Freelance")
Employee = Class(name="Employee")
company_Company = Class(name="company::Company")

# company_Employee class attributes and methods
company_Employee_name: Property = Property(name="name", type=StringType)
company_Employee_age: Property = Property(name="age", type=StringType)
company_Employee_salary: Property = Property(name="salary", type=StringType)
company_Employee.attributes={company_Employee_age, company_Employee_name, company_Employee_salary}

# company_Department class attributes and methods
company_Department_name: Property = Property(name="name", type=StringType)
company_Department_biggestNumberOfStudentsOrFreelancers: Property = Property(name="biggestNumberOfStudentsOrFreelancers", type=StringType)
company_Department_maxJuniors: Property = Property(name="maxJuniors", type=StringType)
company_Department_budget: Property = Property(name="budget", type=StringType)
company_Department_m_calcExpenses: Method = Method(name="calcExpenses", parameters={}, type=StringType)
company_Department_m_sumBudget: Method = Method(name="sumBudget", parameters={}, type=StringType)
company_Department.attributes={company_Department_maxJuniors, company_Department_budget, company_Department_biggestNumberOfStudentsOrFreelancers, company_Department_name}
company_Department.methods={company_Department_m_sumBudget, company_Department_m_calcExpenses}

# company_Division class attributes and methods
company_Division_budget: Property = Property(name="budget", type=StringType)
company_Division_name: Property = Property(name="name", type=StringType)
company_Division_numberEmployeesOfTheMonth: Property = Property(name="numberEmployeesOfTheMonth", type=StringType)
company_Division.attributes={company_Division_name, company_Division_numberEmployeesOfTheMonth, company_Division_budget}

# company_Student class attributes and methods

# company_Freelance class attributes and methods
company_Freelance_assignment: Property = Property(name="assignment", type=StringType)
company_Freelance.attributes={company_Freelance_assignment}

# Employee class attributes and methods

# company_Company class attributes and methods
company_Company_eotmDelta: Property = Property(name="eotmDelta", type=StringType)
company_Company_name: Property = Property(name="name", type=StringType)
company_Company.attributes={company_Company_eotmDelta, company_Company_name}

# Relationships
managed1: BinaryAssociation = BinaryAssociation(
    name="managed1",
    ends={
        Property(name="Department2", type=company_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="boss", type=company_Department, multiplicity=Multiplicity(0, 1))
    }
)
employer0: BinaryAssociation = BinaryAssociation(
    name="employer0",
    ends={
        Property(name="Department", type=company_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="employee", type=company_Department, multiplicity=Multiplicity(0, 1))
    }
)
directed3: BinaryAssociation = BinaryAssociation(
    name="directed3",
    ends={
        Property(name="Division", type=company_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="director", type=company_Division, multiplicity=Multiplicity(0, 1))
    }
)
secretary5: BinaryAssociation = BinaryAssociation(
    name="secretary5",
    ends={
        Property(name="company_Employee", type=company_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Employee4", type=company_Employee, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
intern6: BinaryAssociation = BinaryAssociation(
    name="intern6",
    ends={
        Property(name="company_Student", type=company_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Employee7", type=company_Student, multiplicity=Multiplicity(0, 1))
    }
)
employee8: BinaryAssociation = BinaryAssociation(
    name="employee8",
    ends={
        Property(name="Employee", type=company_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="employer", type=company_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boss9: BinaryAssociation = BinaryAssociation(
    name="boss9",
    ends={
        Property(name="Employee10", type=company_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="managed", type=company_Employee, multiplicity=Multiplicity(0, 1))
    }
)
subDepartment12: BinaryAssociation = BinaryAssociation(
    name="subDepartment12",
    ends={
        Property(name="Department13", type=company_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="parentDepartment", type=company_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentDepartment15: BinaryAssociation = BinaryAssociation(
    name="parentDepartment15",
    ends={
        Property(name="Department16", type=company_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="subDepartment", type=company_Department, multiplicity=Multiplicity(0, 1))
    }
)
employeeOfTheMonth17: BinaryAssociation = BinaryAssociation(
    name="employeeOfTheMonth17",
    ends={
        Property(name="company_Employee18", type=company_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Department", type=company_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
department19: BinaryAssociation = BinaryAssociation(
    name="department19",
    ends={
        Property(name="company_Department20", type=company_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Division", type=company_Department, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
director21: BinaryAssociation = BinaryAssociation(
    name="director21",
    ends={
        Property(name="Employee22", type=company_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="directed", type=company_Employee, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
employeesOfTheMonth23: BinaryAssociation = BinaryAssociation(
    name="employeesOfTheMonth23",
    ends={
        Property(name="company_Employee25", type=company_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Division24", type=company_Employee, multiplicity=Multiplicity(0, 9999))
    }
)
company26: BinaryAssociation = BinaryAssociation(
    name="company26",
    ends={
        Property(name="Company", type=company_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="division", type=company_Company, multiplicity=Multiplicity(0, 1))
    }
)
division27: BinaryAssociation = BinaryAssociation(
    name="division27",
    ends={
        Property(name="Division28", type=company_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company", type=company_Division, multiplicity=Multiplicity(0, 1))
    }
)
divisionDirector29: BinaryAssociation = BinaryAssociation(
    name="divisionDirector29",
    ends={
        Property(name="company_Employee30", type=company_Company, multiplicity=Multiplicity(1, 1)),
        Property(name="company_Company", type=company_Employee, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_company_Freelance_Employee = Generalization(general=Employee, specific=company_Freelance)
gen_company_Student_Employee = Generalization(general=Employee, specific=company_Student)

# Domain Model
domain_model = DomainModel(
    name="company",
    types={company_Employee, company_Department, company_Division, company_Student, company_Freelance, Employee, company_Company},
    associations={managed1, employer0, directed3, secretary5, intern6, employee8, boss9, subDepartment12, parentDepartment15, employeeOfTheMonth17, department19, director21, employeesOfTheMonth23, company26, division27, divisionDirector29},
    generalizations={gen_company_Freelance_Employee, gen_company_Student_Employee},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)