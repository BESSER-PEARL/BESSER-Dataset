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

# Enumerations
model_EmployeeType: Enumeration = Enumeration(
    name="model_EmployeeType",
    literals={
            
    }
)

# Classes
model_Call = Class(name="model_Call")
model_CallCenterEmployee = Class(name="model_CallCenterEmployee")
model_Director = Class(name="model_Director")
model_Operator = Class(name="model_Operator")
model_Supervisor = Class(name="model_Supervisor")
genmymodelreverse_java_util_logging_Logger = Class(name="genmymodelreverse_java_util_logging_Logger")

# model_Call class attributes and methods
model_Call_LOGGER: Property = Property(name="LOGGER", type=genmymodelreverse_java_util_logging_Logger)
model_Call_number: Property = Property(name="number", type=IntegerType)
model_Call_MIN: Property = Property(name="MIN", type=IntegerType)
model_Call_MAX: Property = Property(name="MAX", type=IntegerType)
model_Call.attributes={model_Call_LOGGER, model_Call_MIN, model_Call_number, model_Call_MAX}

# model_CallCenterEmployee class attributes and methods
model_CallCenterEmployee_LOGGER: Property = Property(name="LOGGER", type=genmymodelreverse_java_util_logging_Logger)
model_CallCenterEmployee_name: Property = Property(name="name", type=StringType)
model_CallCenterEmployee_employeeType: Property = Property(name="employeeType", type=model_EmployeeType)
model_CallCenterEmployee_callsAnswered: Property = Property(name="callsAnswered", type=IntegerType)
model_CallCenterEmployee.attributes={model_CallCenterEmployee_name, model_CallCenterEmployee_employeeType, model_CallCenterEmployee_callsAnswered, model_CallCenterEmployee_LOGGER}

# model_Director class attributes and methods

# model_Operator class attributes and methods

# model_Supervisor class attributes and methods

# genmymodelreverse_java_util_logging_Logger class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="c41050a2_846f_44fa_b4ba_cb48e68c6f3b",
    types={model_Call, model_CallCenterEmployee, model_Director, model_Operator, model_Supervisor, genmymodelreverse_java_util_logging_Logger, model_EmployeeType},
    associations={},
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