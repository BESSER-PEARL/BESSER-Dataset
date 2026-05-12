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
CoachBusWithEDataType_Employee = Class(name="CoachBusWithEDataType_Employee")
CoachBusWithEDataType_SecurityGuard = Class(name="CoachBusWithEDataType_SecurityGuard")
Employee = Class(name="Employee")
CoachBusWithEDataType_Manager = Class(name="CoachBusWithEDataType_Manager")

# CoachBusWithEDataType_Employee class attributes and methods
CoachBusWithEDataType_Employee_baseSalary: Property = Property(name="baseSalary", type=FloatType)
CoachBusWithEDataType_Employee.attributes={CoachBusWithEDataType_Employee_baseSalary}

# CoachBusWithEDataType_SecurityGuard class attributes and methods

# Employee class attributes and methods

# CoachBusWithEDataType_Manager class attributes and methods

# Generalizations
gen_CoachBusWithEDataType_SecurityGuard_Employee = Generalization(general=Employee, specific=CoachBusWithEDataType_SecurityGuard)
gen_CoachBusWithEDataType_Manager_Employee = Generalization(general=Employee, specific=CoachBusWithEDataType_Manager)


# OCL Constraints
BaseSalaryConstraint: Constraint = Constraint(
    name="BaseSalaryConstraint",
    context=CoachBusWithEDataType_Employee,
    expression="context Employee inv: self.baseSalary >=(0)",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="CoachBusWithEDataType",
    types={CoachBusWithEDataType_Employee, CoachBusWithEDataType_SecurityGuard, Employee, CoachBusWithEDataType_Manager},
    associations={},
    constraints={BaseSalaryConstraint},
    generalizations={gen_CoachBusWithEDataType_SecurityGuard_Employee, gen_CoachBusWithEDataType_Manager_Employee},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)