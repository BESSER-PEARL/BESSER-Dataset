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
UML2_ExtensionEnd = Class(name="UML2::ExtensionEnd")
Property_ = Class(name="Property")
UML2_Association = Class(name="UML2::Association")
UML2_Property = Class(name="UML2::Property")
UML2_Extension = Class(name="UML2::Extension")
Association = Class(name="Association")
UML2_AssociationClass = Class(name="UML2::AssociationClass")
UML2_CommunicationPath = Class(name="UML2::CommunicationPath")
UML2_Port = Class(name="UML2::Port")

# UML2_ExtensionEnd class attributes and methods

# Property class attributes and methods

# UML2_Association class attributes and methods

# UML2_Property class attributes and methods

# UML2_Extension class attributes and methods

# Association class attributes and methods

# UML2_AssociationClass class attributes and methods

# UML2_CommunicationPath class attributes and methods

# UML2_Port class attributes and methods

# Relationships
ownedEnd0: BinaryAssociation = BinaryAssociation(
    name="ownedEnd0",
    ends={
        Property(name="UML2_Property", type=UML2_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Association", type=UML2_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memberEnd1: BinaryAssociation = BinaryAssociation(
    name="memberEnd1",
    ends={
        Property(name="UML2_Property3", type=UML2_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Association2", type=UML2_Property, multiplicity=Multiplicity(2, 9999))
    }
)

# Generalizations
gen_UML2_ExtensionEnd_Property = Generalization(general=Property_, specific=UML2_ExtensionEnd)
gen_UML2_Extension_Association = Generalization(general=Association, specific=UML2_Extension)
gen_UML2_AssociationClass_Association = Generalization(general=Association, specific=UML2_AssociationClass)
gen_UML2_CommunicationPath_Association = Generalization(general=Association, specific=UML2_CommunicationPath)
gen_UML2_Port_Property = Generalization(general=Property_, specific=UML2_Port)

# Domain Model
domain_model = DomainModel(
    name="UML2",
    types={UML2_ExtensionEnd, Property_, UML2_Association, UML2_Property, UML2_Extension, Association, UML2_AssociationClass, UML2_CommunicationPath, UML2_Port},
    associations={ownedEnd0, memberEnd1},
    generalizations={gen_UML2_ExtensionEnd_Property, gen_UML2_Extension_Association, gen_UML2_AssociationClass_Association, gen_UML2_CommunicationPath_Association, gen_UML2_Port_Property},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)