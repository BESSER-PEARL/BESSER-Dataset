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
ClassM = Class(name="ClassM")
ClassN = Class(name="ClassN")
ClassP = Class(name="ClassP")
InterfaceO_Interface = Class(name="InterfaceO_Interface")
ClassQ = Class(name="ClassQ")
ClassR = Class(name="ClassR")
ClassS = Class(name="ClassS")
ClassT = Class(name="ClassT")
ClassU = Class(name="ClassU")
ClassV = Class(name="ClassV")
MyClass = Class(name="MyClass")

# ClassM class attributes and methods

# ClassN class attributes and methods

# ClassP class attributes and methods

# InterfaceO_Interface class attributes and methods

# ClassQ class attributes and methods

# ClassR class attributes and methods

# ClassS class attributes and methods

# ClassT class attributes and methods

# ClassU class attributes and methods

# ClassV class attributes and methods

# MyClass class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_5c85815a_d7c3_42f1_a521_a40f1a9d9757",
    types={ClassM, ClassN, ClassP, InterfaceO_Interface, ClassQ, ClassR, ClassS, ClassT, ClassU, ClassV, MyClass},
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