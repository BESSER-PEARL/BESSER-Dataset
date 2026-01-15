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
ParameterDirectionKind: Enumeration = Enumeration(
    name="ParameterDirectionKind",
    literals={
            EnumerationLiteral(name="in"),
			EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="out"),
			EnumerationLiteral(name="return")
    }
)

# Classes
UML2_Pin = Class(name="UML2::Pin")
UML2_ConnectorEnd = Class(name="UML2::ConnectorEnd")
MultiplicityElement = Class(name="MultiplicityElement")
UML2_Property = Class(name="UML2::Property")
StructuralFeature = Class(name="StructuralFeature")
UML2_InputPin = Class(name="UML2::InputPin")
Pin = Class(name="Pin")
UML2_Parameter = Class(name="UML2::Parameter")
UML2_Operation = Class(name="UML2::Operation")
UML2_Variable = Class(name="UML2::Variable")
UML2_MultiplicityElement = Class(name="UML2::MultiplicityElement")
UML2_OutputPin = Class(name="UML2::OutputPin")
UML2_StructuralFeature = Class(name="UML2::StructuralFeature")
UML2_ValuePin = Class(name="UML2::ValuePin")
InputPin = Class(name="InputPin")
UML2_ExtensionEnd = Class(name="UML2::ExtensionEnd")
Property_ = Class(name="Property")
UML2_Port = Class(name="UML2::Port")

# UML2_Pin class attributes and methods

# UML2_ConnectorEnd class attributes and methods

# MultiplicityElement class attributes and methods

# UML2_Property class attributes and methods

# StructuralFeature class attributes and methods

# UML2_InputPin class attributes and methods

# Pin class attributes and methods

# UML2_Parameter class attributes and methods
UML2_Parameter_direction: Property = Property(name="direction", type=StringType)
UML2_Parameter.attributes={UML2_Parameter_direction}

# UML2_Operation class attributes and methods

# UML2_Variable class attributes and methods

# UML2_MultiplicityElement class attributes and methods
UML2_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=BooleanType)
UML2_MultiplicityElement.attributes={UML2_MultiplicityElement_isUnique}

# UML2_OutputPin class attributes and methods

# UML2_StructuralFeature class attributes and methods

# UML2_ValuePin class attributes and methods

# InputPin class attributes and methods

# UML2_ExtensionEnd class attributes and methods

# Property class attributes and methods

# UML2_Port class attributes and methods

# Relationships
ownedParameter0: BinaryAssociation = BinaryAssociation(
    name="ownedParameter0",
    ends={
        Property(name="UML2_Parameter", type=UML2_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Operation", type=UML2_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_UML2_Pin_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2_Pin)
gen_UML2_ConnectorEnd_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2_ConnectorEnd)
gen_UML2_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=UML2_Property)
gen_UML2_InputPin_Pin = Generalization(general=Pin, specific=UML2_InputPin)
gen_UML2_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2_Parameter)
gen_UML2_Operation_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2_Operation)
gen_UML2_Variable_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2_Variable)
gen_UML2_OutputPin_Pin = Generalization(general=Pin, specific=UML2_OutputPin)
gen_UML2_StructuralFeature_MultiplicityElement = Generalization(general=MultiplicityElement, specific=UML2_StructuralFeature)
gen_UML2_ValuePin_InputPin = Generalization(general=InputPin, specific=UML2_ValuePin)
gen_UML2_ExtensionEnd_Property = Generalization(general=Property_, specific=UML2_ExtensionEnd)
gen_UML2_Port_Property = Generalization(general=Property_, specific=UML2_Port)

# Domain Model
domain_model = DomainModel(
    name="UML2",
    types={UML2_Pin, UML2_ConnectorEnd, MultiplicityElement, UML2_Property, StructuralFeature, UML2_InputPin, Pin, UML2_Parameter, UML2_Operation, UML2_Variable, UML2_MultiplicityElement, UML2_OutputPin, UML2_StructuralFeature, UML2_ValuePin, InputPin, UML2_ExtensionEnd, Property_, UML2_Port, ParameterDirectionKind},
    associations={ownedParameter0},
    generalizations={gen_UML2_Pin_MultiplicityElement, gen_UML2_ConnectorEnd_MultiplicityElement, gen_UML2_Property_StructuralFeature, gen_UML2_InputPin_Pin, gen_UML2_Parameter_MultiplicityElement, gen_UML2_Operation_MultiplicityElement, gen_UML2_Variable_MultiplicityElement, gen_UML2_OutputPin_Pin, gen_UML2_StructuralFeature_MultiplicityElement, gen_UML2_ValuePin_InputPin, gen_UML2_ExtensionEnd_Property, gen_UML2_Port_Property},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)