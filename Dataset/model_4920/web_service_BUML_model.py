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
web_service_Service = Class(name="web::service::Service")
web_service_MessageFormatter = Class(name="web::service::MessageFormatter")
web_service_FunctionProvider = Class(name="web::service::FunctionProvider")
web_service_DataRecogniser = Class(name="web::service::DataRecogniser")
web_service_GenericMessageFormatter = Class(name="web::service::GenericMessageFormatter")
MessageFormatter = Class(name="MessageFormatter")
web_service_GenericFunctionProvider = Class(name="web::service::GenericFunctionProvider")
FunctionProvider = Class(name="FunctionProvider")
web_service_GenericDataRecogniser = Class(name="web::service::GenericDataRecogniser")
DataRecogniser = Class(name="DataRecogniser")
web_service_Endpoint = Class(name="web::service::Endpoint")

# web_service_Service class attributes and methods

# web_service_MessageFormatter class attributes and methods
web_service_MessageFormatter_name: Property = Property(name="name", type=StringType)
web_service_MessageFormatter.attributes={web_service_MessageFormatter_name}

# web_service_FunctionProvider class attributes and methods
web_service_FunctionProvider_name: Property = Property(name="name", type=StringType)
web_service_FunctionProvider.attributes={web_service_FunctionProvider_name}

# web_service_DataRecogniser class attributes and methods
web_service_DataRecogniser_name: Property = Property(name="name", type=StringType)
web_service_DataRecogniser.attributes={web_service_DataRecogniser_name}

# web_service_GenericMessageFormatter class attributes and methods

# MessageFormatter class attributes and methods

# web_service_GenericFunctionProvider class attributes and methods

# FunctionProvider class attributes and methods

# web_service_GenericDataRecogniser class attributes and methods

# DataRecogniser class attributes and methods

# web_service_Endpoint class attributes and methods
web_service_Endpoint_name: Property = Property(name="name", type=StringType)
web_service_Endpoint.attributes={web_service_Endpoint_name}

# Relationships
formatters1: BinaryAssociation = BinaryAssociation(
    name="formatters1",
    ends={
        Property(name="web_service_MessageFormatter", type=web_service_Endpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="web_service_Endpoint2", type=web_service_MessageFormatter, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
functions3: BinaryAssociation = BinaryAssociation(
    name="functions3",
    ends={
        Property(name="web_service_FunctionProvider", type=web_service_Endpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="web_service_Endpoint4", type=web_service_FunctionProvider, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
recognisers5: BinaryAssociation = BinaryAssociation(
    name="recognisers5",
    ends={
        Property(name="web_service_DataRecogniser", type=web_service_Endpoint, multiplicity=Multiplicity(1, 1)),
        Property(name="web_service_Endpoint6", type=web_service_DataRecogniser, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endpoint0: BinaryAssociation = BinaryAssociation(
    name="endpoint0",
    ends={
        Property(name="web_service_Endpoint", type=web_service_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="web_service_Service", type=web_service_Endpoint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_web_service_GenericMessageFormatter_MessageFormatter = Generalization(general=MessageFormatter, specific=web_service_GenericMessageFormatter)
gen_web_service_GenericFunctionProvider_FunctionProvider = Generalization(general=FunctionProvider, specific=web_service_GenericFunctionProvider)
gen_web_service_GenericDataRecogniser_DataRecogniser = Generalization(general=DataRecogniser, specific=web_service_GenericDataRecogniser)

# Domain Model
domain_model = DomainModel(
    name="web_service",
    types={web_service_Service, web_service_MessageFormatter, web_service_FunctionProvider, web_service_DataRecogniser, web_service_GenericMessageFormatter, MessageFormatter, web_service_GenericFunctionProvider, FunctionProvider, web_service_GenericDataRecogniser, DataRecogniser, web_service_Endpoint},
    associations={formatters1, functions3, recognisers5, endpoint0},
    generalizations={gen_web_service_GenericMessageFormatter_MessageFormatter, gen_web_service_GenericFunctionProvider_FunctionProvider, gen_web_service_GenericDataRecogniser_DataRecogniser},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)