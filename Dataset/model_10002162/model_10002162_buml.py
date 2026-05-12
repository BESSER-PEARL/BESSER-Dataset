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
AbstractWebpage = Class(name="AbstractWebpage", is_abstract=True)
LoginPage = Class(name="LoginPage")
RegisterPage = Class(name="RegisterPage")
AbstractHomePage = Class(name="AbstractHomePage", is_abstract=True)
AdminHomePage = Class(name="AdminHomePage")
ManagerHomePage = Class(name="ManagerHomePage")
UserHomePage = Class(name="UserHomePage")

# AbstractWebpage class attributes and methods

# LoginPage class attributes and methods

# RegisterPage class attributes and methods

# AbstractHomePage class attributes and methods

# AdminHomePage class attributes and methods

# ManagerHomePage class attributes and methods

# UserHomePage class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_tgNwcKDfEeiiNrO2ZqzvYA",
    types={AbstractWebpage, LoginPage, RegisterPage, AbstractHomePage, AdminHomePage, ManagerHomePage, UserHomePage},
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