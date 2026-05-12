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
CoachBusWithEDataType_SecurityGuard = Class(name="CoachBusWithEDataType_SecurityGuard")
CoachBusWithEDataType_Manager = Class(name="CoachBusWithEDataType_Manager")
Employee = Class(name="Employee")
CoachBusWithEDataType_Employee = Class(name="CoachBusWithEDataType_Employee")

# CoachBusWithEDataType_SecurityGuard class attributes and methods

# CoachBusWithEDataType_Manager class attributes and methods

# Employee class attributes and methods

# CoachBusWithEDataType_Employee class attributes and methods
CoachBusWithEDataType_Employee_id: Property = Property(name="id", type=IntegerType)
CoachBusWithEDataType_Employee.attributes={CoachBusWithEDataType_Employee_id}

# Generalizations
gen_CoachBusWithEDataType_SecurityGuard_Employee = Generalization(general=Employee, specific=CoachBusWithEDataType_SecurityGuard)
gen_CoachBusWithEDataType_Manager_Employee = Generalization(general=Employee, specific=CoachBusWithEDataType_Manager)


# OCL Constraints
UniqueEmployeeID: Constraint = Constraint(
    name="UniqueEmployeeID",
    context=CoachBusWithEDataType_Employee,
    expression="context Employee inv: CoachBusWithEDataType_Employee.allInstances()->isUnique(e : Employee | e.id)",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="CoachBusWithEDataType",
    types={CoachBusWithEDataType_SecurityGuard, CoachBusWithEDataType_Manager, Employee, CoachBusWithEDataType_Employee},
    associations={},
    constraints={UniqueEmployeeID},
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