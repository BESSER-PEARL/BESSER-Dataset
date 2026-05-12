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
AppProcessor = Class(name="AppProcessor")
SetExpressCheckoutProcessor = Class(name="SetExpressCheckoutProcessor")
GetExpressCheckoutDetailsProcessor = Class(name="GetExpressCheckoutDetailsProcessor")
DoExpressCheckoutDetailsProcessor = Class(name="DoExpressCheckoutDetailsProcessor")
IAppProcessor_Interface = Class(name="IAppProcessor_Interface")
SetExpressCheckoutAdapter = Class(name="SetExpressCheckoutAdapter")
GetExpressCheckoutDetailsAdapter = Class(name="GetExpressCheckoutDetailsAdapter")
DoExpressCheckoutDetailsAdapter = Class(name="DoExpressCheckoutDetailsAdapter")
User_Actor = Class(name="User_Actor")

# AppProcessor class attributes and methods

# SetExpressCheckoutProcessor class attributes and methods

# GetExpressCheckoutDetailsProcessor class attributes and methods

# DoExpressCheckoutDetailsProcessor class attributes and methods

# IAppProcessor_Interface class attributes and methods

# SetExpressCheckoutAdapter class attributes and methods

# GetExpressCheckoutDetailsAdapter class attributes and methods

# DoExpressCheckoutDetailsAdapter class attributes and methods

# User_Actor class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_6529e21a_c1e9_43de_94ff_1907893396c1",
    types={AppProcessor, SetExpressCheckoutProcessor, GetExpressCheckoutDetailsProcessor, DoExpressCheckoutDetailsProcessor, IAppProcessor_Interface, SetExpressCheckoutAdapter, GetExpressCheckoutDetailsAdapter, DoExpressCheckoutDetailsAdapter, User_Actor},
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