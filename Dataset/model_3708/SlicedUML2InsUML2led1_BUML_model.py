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
UML2_LinkEndCreationData = Class(name="UML2::LinkEndCreationData")
LinkEndData = Class(name="LinkEndData")
UML2_CommunicationPath = Class(name="UML2::CommunicationPath")
Association = Class(name="Association")
UML2_ExtensionEnd = Class(name="UML2::ExtensionEnd")
Property_ = Class(name="Property")
UML2_LinkEndData = Class(name="UML2::LinkEndData")
UML2_Property = Class(name="UML2::Property")
UML2_Port = Class(name="UML2::Port")
UML2_AssociationClass = Class(name="UML2::AssociationClass")
UML2_Association = Class(name="UML2::Association")
UML2_Extension = Class(name="UML2::Extension")

# UML2_LinkEndCreationData class attributes and methods

# LinkEndData class attributes and methods

# UML2_CommunicationPath class attributes and methods

# Association class attributes and methods

# UML2_ExtensionEnd class attributes and methods

# Property class attributes and methods

# UML2_LinkEndData class attributes and methods

# UML2_Property class attributes and methods

# UML2_Port class attributes and methods

# UML2_AssociationClass class attributes and methods

# UML2_Association class attributes and methods

# UML2_Extension class attributes and methods

# Relationships
end0: BinaryAssociation = BinaryAssociation(
    name="end0",
    ends={
        Property(name="UML2_Property", type=UML2_LinkEndData, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_LinkEndData", type=UML2_Property, multiplicity=Multiplicity(1, 1))
    }
)
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="UML2_Association", type=UML2_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Property2", type=UML2_Association, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_UML2_LinkEndCreationData_LinkEndData = Generalization(general=LinkEndData, specific=UML2_LinkEndCreationData)
gen_UML2_CommunicationPath_Association = Generalization(general=Association, specific=UML2_CommunicationPath)
gen_UML2_ExtensionEnd_Property = Generalization(general=Property_, specific=UML2_ExtensionEnd)
gen_UML2_Port_Property = Generalization(general=Property_, specific=UML2_Port)
gen_UML2_AssociationClass_Association = Generalization(general=Association, specific=UML2_AssociationClass)
gen_UML2_Extension_Association = Generalization(general=Association, specific=UML2_Extension)

# Domain Model
domain_model = DomainModel(
    name="UML2",
    types={UML2_LinkEndCreationData, LinkEndData, UML2_CommunicationPath, Association, UML2_ExtensionEnd, Property_, UML2_LinkEndData, UML2_Property, UML2_Port, UML2_AssociationClass, UML2_Association, UML2_Extension},
    associations={end0, association1},
    generalizations={gen_UML2_LinkEndCreationData_LinkEndData, gen_UML2_CommunicationPath_Association, gen_UML2_ExtensionEnd_Property, gen_UML2_Port_Property, gen_UML2_AssociationClass_Association, gen_UML2_Extension_Association},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)