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
AggregationKind: Enumeration = Enumeration(
    name="AggregationKind",
    literals={
            EnumerationLiteral(name="composite"),
			EnumerationLiteral(name="none"),
			EnumerationLiteral(name="shared")
    }
)

# Classes
UML2WithID_Port = Class(name="UML2WithID::Port")
Property_ = Class(name="Property")
UML2WithID_ExtensionEnd = Class(name="UML2WithID::ExtensionEnd")
UML2WithID_CommunicationPath = Class(name="UML2WithID::CommunicationPath")
Association = Class(name="Association")
Element = Class(name="Element")
UML2WithID_Association = Class(name="UML2WithID::Association")
UML2WithID_Property = Class(name="UML2WithID::Property")
UML2WithID_AssociationClass = Class(name="UML2WithID::AssociationClass")
UML2WithID_Extension = Class(name="UML2WithID::Extension")
UML2WithID_Element = Class(name="UML2WithID::Element", is_abstract=True)

# UML2WithID_Port class attributes and methods

# Property class attributes and methods

# UML2WithID_ExtensionEnd class attributes and methods

# UML2WithID_CommunicationPath class attributes and methods

# Association class attributes and methods

# Element class attributes and methods

# UML2WithID_Association class attributes and methods

# UML2WithID_Property class attributes and methods
UML2WithID_Property_aggregation: Property = Property(name="aggregation", type=StringType)
UML2WithID_Property.attributes={UML2WithID_Property_aggregation}

# UML2WithID_AssociationClass class attributes and methods

# UML2WithID_Extension class attributes and methods

# UML2WithID_Element class attributes and methods
UML2WithID_Element_ID: Property = Property(name="ID", type=StringType)
UML2WithID_Element.attributes={UML2WithID_Element_ID}

# Relationships
memberEnd0: BinaryAssociation = BinaryAssociation(
    name="memberEnd0",
    ends={
        Property(name="UML2WithID_Property", type=UML2WithID_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Association", type=UML2WithID_Property, multiplicity=Multiplicity(2, 9999))
    }
)

# Generalizations
gen_UML2WithID_Property_Element = Generalization(general=Element, specific=UML2WithID_Property)
gen_UML2WithID_Port_Property = Generalization(general=Property_, specific=UML2WithID_Port)
gen_UML2WithID_Port_Element = Generalization(general=Element, specific=UML2WithID_Port)
gen_UML2WithID_ExtensionEnd_Property = Generalization(general=Property_, specific=UML2WithID_ExtensionEnd)
gen_UML2WithID_ExtensionEnd_Element = Generalization(general=Element, specific=UML2WithID_ExtensionEnd)
gen_UML2WithID_CommunicationPath_Association = Generalization(general=Association, specific=UML2WithID_CommunicationPath)
gen_UML2WithID_CommunicationPath_Element = Generalization(general=Element, specific=UML2WithID_CommunicationPath)
gen_UML2WithID_Association_Element = Generalization(general=Element, specific=UML2WithID_Association)
gen_UML2WithID_AssociationClass_Association = Generalization(general=Association, specific=UML2WithID_AssociationClass)
gen_UML2WithID_AssociationClass_Element = Generalization(general=Element, specific=UML2WithID_AssociationClass)
gen_UML2WithID_Extension_Association = Generalization(general=Association, specific=UML2WithID_Extension)
gen_UML2WithID_Extension_Element = Generalization(general=Element, specific=UML2WithID_Extension)

# Domain Model
domain_model = DomainModel(
    name="UML2WithID",
    types={UML2WithID_Port, Property_, UML2WithID_ExtensionEnd, UML2WithID_CommunicationPath, Association, Element, UML2WithID_Association, UML2WithID_Property, UML2WithID_AssociationClass, UML2WithID_Extension, UML2WithID_Element, AggregationKind},
    associations={memberEnd0},
    generalizations={gen_UML2WithID_Property_Element, gen_UML2WithID_Port_Property, gen_UML2WithID_Port_Element, gen_UML2WithID_ExtensionEnd_Property, gen_UML2WithID_ExtensionEnd_Element, gen_UML2WithID_CommunicationPath_Association, gen_UML2WithID_CommunicationPath_Element, gen_UML2WithID_Association_Element, gen_UML2WithID_AssociationClass_Association, gen_UML2WithID_AssociationClass_Element, gen_UML2WithID_Extension_Association, gen_UML2WithID_Extension_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)