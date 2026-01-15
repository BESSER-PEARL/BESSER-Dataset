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
model_User = Class(name="model::User")
model_Service = Class(name="model::Service")
model_App = Class(name="model::App")
model_Param = Class(name="model::Param")

# model_User class attributes and methods
model_User_name: Property = Property(name="name", type=StringType)
model_User_password: Property = Property(name="password", type=StringType)
model_User.attributes={model_User_name, model_User_password}

# model_Service class attributes and methods
model_Service_name: Property = Property(name="name", type=StringType)
model_Service_methodName: Property = Property(name="methodName", type=StringType)
model_Service_acceptedParams: Property = Property(name="acceptedParams", type=StringType)
model_Service.attributes={model_Service_name, model_Service_acceptedParams, model_Service_methodName}

# model_App class attributes and methods
model_App_m_authFailure: Method = Method(name="authFailure", parameters={})
model_App_m_result: Method = Method(name="result", parameters={Parameter(name='result')})
model_App_m_auth: Method = Method(name="auth", parameters={Parameter(name='login'), Parameter(name='password')})
model_App_m_service: Method = Method(name="service", parameters={Parameter(name='params'), Parameter(name='token'), Parameter(name='service')})
model_App_m_authSuccess: Method = Method(name="authSuccess", parameters={Parameter(name='token')})
model_App.methods={model_App_m_result, model_App_m_service, model_App_m_authSuccess, model_App_m_authFailure, model_App_m_auth}

# model_Param class attributes and methods
model_Param_name: Property = Property(name="name", type=StringType)
model_Param_value: Property = Property(name="value", type=StringType)
model_Param.attributes={model_Param_name, model_Param_value}

# Relationships
allowedUsers0: BinaryAssociation = BinaryAssociation(
    name="allowedUsers0",
    ends={
        Property(name="model_User", type=model_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Service", type=model_User, multiplicity=Multiplicity(0, 9999))
    }
)
users1: BinaryAssociation = BinaryAssociation(
    name="users1",
    ends={
        Property(name="model_User2", type=model_App, multiplicity=Multiplicity(1, 1)),
        Property(name="model_App", type=model_User, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
services3: BinaryAssociation = BinaryAssociation(
    name="services3",
    ends={
        Property(name="model_Service5", type=model_App, multiplicity=Multiplicity(1, 1)),
        Property(name="model_App4", type=model_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_User, model_Service, model_App, model_Param},
    associations={allowedUsers0, users1, services3},
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