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
UML_PackageableElement = Class(name="UML::PackageableElement")
Element = Class(name="Element")
UML_Package = Class(name="UML::Package")
PackageableElement = Class(name="PackageableElement")
UML_Model = Class(name="UML::Model")
Package = Class(name="Package")
UML_TypedElement = Class(name="UML::TypedElement")
UML_LiteralInteger = Class(name="UML::LiteralInteger")
UML_LiteralUnlimitedNatural = Class(name="UML::LiteralUnlimitedNatural")
UML_PrimitiveType = Class(name="UML::PrimitiveType")
UML_Attribute = Class(name="UML::Attribute")
TypedElement = Class(name="TypedElement")
UML_Property = Class(name="UML::Property")
Attribute = Class(name="Attribute")
UML_Element = Class(name="UML::Element", is_abstract=True)
UML_Generalization = Class(name="UML::Generalization")
UML_TemplateBinding = Class(name="UML::TemplateBinding")
Class_ = Class(name="Class")
UML_EnumerationLiteral = Class(name="UML::EnumerationLiteral")
UML_Enumeration = Class(name="UML::Enumeration")
UML_Association = Class(name="UML::Association")
UML_Interface = Class(name="UML::Interface")
UML_Parameter = Class(name="UML::Parameter")
UML_Operation = Class(name="UML::Operation")
UML_Class = Class(name="UML::Class")
UML_TemplateParameterSubstitution = Class(name="UML::TemplateParameterSubstitution")

# UML_PackageableElement class attributes and methods

# Element class attributes and methods

# UML_Package class attributes and methods

# PackageableElement class attributes and methods

# UML_Model class attributes and methods

# Package class attributes and methods

# UML_TypedElement class attributes and methods

# UML_LiteralInteger class attributes and methods

# UML_LiteralUnlimitedNatural class attributes and methods
UML_LiteralUnlimitedNatural_value: Property = Property(name="value", type=IntegerType)
UML_LiteralUnlimitedNatural.attributes={UML_LiteralUnlimitedNatural_value}

# UML_PrimitiveType class attributes and methods

# UML_Attribute class attributes and methods

# TypedElement class attributes and methods

# UML_Property class attributes and methods
UML_Property_isStatic: Property = Property(name="isStatic", type=BooleanType)
UML_Property.attributes={UML_Property_isStatic}

# Attribute class attributes and methods

# UML_Element class attributes and methods
UML_Element_visibility: Property = Property(name="visibility", type=StringType)
UML_Element_name: Property = Property(name="name", type=StringType)
UML_Element.attributes={UML_Element_visibility, UML_Element_name}

# UML_Generalization class attributes and methods

# UML_TemplateBinding class attributes and methods

# Class class attributes and methods

# UML_EnumerationLiteral class attributes and methods

# UML_Enumeration class attributes and methods

# UML_Association class attributes and methods

# UML_Interface class attributes and methods

# UML_Parameter class attributes and methods
UML_Parameter_direction: Property = Property(name="direction", type=StringType)
UML_Parameter.attributes={UML_Parameter_direction}

# UML_Operation class attributes and methods

# UML_Class class attributes and methods

# UML_TemplateParameterSubstitution class attributes and methods

# Relationships
packagedElement0: BinaryAssociation = BinaryAssociation(
    name="packagedElement0",
    ends={
        Property(name="UML_Package", type=UML_PackageableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_PackageableElement", type=UML_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="UML_Package2", type=UML_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_TypedElement", type=UML_Package, multiplicity=Multiplicity(0, 1))
    }
)
lowerValue3: BinaryAssociation = BinaryAssociation(
    name="lowerValue3",
    ends={
        Property(name="UML_LiteralInteger", type=UML_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_TypedElement4", type=UML_LiteralInteger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
upperValue5: BinaryAssociation = BinaryAssociation(
    name="upperValue5",
    ends={
        Property(name="UML_LiteralUnlimitedNatural", type=UML_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_TypedElement6", type=UML_LiteralUnlimitedNatural, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
class20: BinaryAssociation = BinaryAssociation(
    name="class20",
    ends={
        Property(name="UML_Class", type=UML_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Operation21", type=UML_Class, multiplicity=Multiplicity(0, 1))
    }
)
interface22: BinaryAssociation = BinaryAssociation(
    name="interface22",
    ends={
        Property(name="UML_Interface24", type=UML_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Operation23", type=UML_Interface, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute25: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute25",
    ends={
        Property(name="UML_Attribute", type=UML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Class26", type=UML_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation27: BinaryAssociation = BinaryAssociation(
    name="ownedOperation27",
    ends={
        Property(name="UML_Operation29", type=UML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Class28", type=UML_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generalization30: BinaryAssociation = BinaryAssociation(
    name="generalization30",
    ends={
        Property(name="UML_Generalization", type=UML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Class31", type=UML_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
templateBinding32: BinaryAssociation = BinaryAssociation(
    name="templateBinding32",
    ends={
        Property(name="UML_TemplateBinding", type=UML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Class33", type=UML_TemplateBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedClassifier35: BinaryAssociation = BinaryAssociation(
    name="nestedClassifier35",
    ends={
        Property(name="UML_Class36", type=UML_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Class34", type=UML_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifier37: BinaryAssociation = BinaryAssociation(
    name="classifier37",
    ends={
        Property(name="UML_Enumeration", type=UML_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_EnumerationLiteral", type=UML_Enumeration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration38: BinaryAssociation = BinaryAssociation(
    name="enumeration38",
    ends={
        Property(name="UML_Enumeration40", type=UML_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_EnumerationLiteral39", type=UML_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
ownedLiteral41: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral41",
    ends={
        Property(name="UML_EnumerationLiteral43", type=UML_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Enumeration42", type=UML_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
association7: BinaryAssociation = BinaryAssociation(
    name="association7",
    ends={
        Property(name="UML_Association", type=UML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Property", type=UML_Association, multiplicity=Multiplicity(0, 1))
    }
)
qualifier9: BinaryAssociation = BinaryAssociation(
    name="qualifier9",
    ends={
        Property(name="UML_Property10", type=UML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Property8", type=UML_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningAssociation11: BinaryAssociation = BinaryAssociation(
    name="owningAssociation11",
    ends={
        Property(name="UML_Association13", type=UML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Property12", type=UML_Association, multiplicity=Multiplicity(0, 1))
    }
)
associationEnd14: BinaryAssociation = BinaryAssociation(
    name="associationEnd14",
    ends={
        Property(name="UML_Association16", type=UML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Property15", type=UML_Association, multiplicity=Multiplicity(0, 1))
    }
)
interface17: BinaryAssociation = BinaryAssociation(
    name="interface17",
    ends={
        Property(name="UML_Interface", type=UML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Property18", type=UML_Interface, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameter19: BinaryAssociation = BinaryAssociation(
    name="ownedParameter19",
    ends={
        Property(name="UML_Parameter", type=UML_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Operation", type=UML_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterSubstitution61: BinaryAssociation = BinaryAssociation(
    name="parameterSubstitution61",
    ends={
        Property(name="UML_TemplateParameterSubstitution63", type=UML_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_TemplateBinding62", type=UML_TemplateParameterSubstitution, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
boundElement64: BinaryAssociation = BinaryAssociation(
    name="boundElement64",
    ends={
        Property(name="UML_Package66", type=UML_TemplateBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_TemplateBinding65", type=UML_Package, multiplicity=Multiplicity(0, 1))
    }
)
general44: BinaryAssociation = BinaryAssociation(
    name="general44",
    ends={
        Property(name="UML_Class46", type=UML_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Generalization45", type=UML_Class, multiplicity=Multiplicity(0, 1))
    }
)
specific47: BinaryAssociation = BinaryAssociation(
    name="specific47",
    ends={
        Property(name="UML_Class49", type=UML_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Generalization48", type=UML_Class, multiplicity=Multiplicity(0, 1))
    }
)
memberEnd50: BinaryAssociation = BinaryAssociation(
    name="memberEnd50",
    ends={
        Property(name="UML_Property52", type=UML_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Association51", type=UML_Property, multiplicity=Multiplicity(0, 9999))
    }
)
ownedEnd53: BinaryAssociation = BinaryAssociation(
    name="ownedEnd53",
    ends={
        Property(name="UML_Property55", type=UML_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_Association54", type=UML_Property, multiplicity=Multiplicity(0, 9999))
    }
)
actual56: BinaryAssociation = BinaryAssociation(
    name="actual56",
    ends={
        Property(name="UML_Package57", type=UML_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_TemplateParameterSubstitution", type=UML_Package, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
templateBinding58: BinaryAssociation = BinaryAssociation(
    name="templateBinding58",
    ends={
        Property(name="UML_TemplateBinding60", type=UML_TemplateParameterSubstitution, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_TemplateParameterSubstitution59", type=UML_TemplateBinding, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_UML_PackageableElement_Element = Generalization(general=Element, specific=UML_PackageableElement)
gen_UML_Package_PackageableElement = Generalization(general=PackageableElement, specific=UML_Package)
gen_UML_Model_Package = Generalization(general=Package, specific=UML_Model)
gen_UML_TypedElement_Element = Generalization(general=Element, specific=UML_TypedElement)
gen_UML_PrimitiveType_Package = Generalization(general=Package, specific=UML_PrimitiveType)
gen_UML_LiteralInteger_Package = Generalization(general=Package, specific=UML_LiteralInteger)
gen_UML_LiteralUnlimitedNatural_Package = Generalization(general=Package, specific=UML_LiteralUnlimitedNatural)
gen_UML_Attribute_TypedElement = Generalization(general=TypedElement, specific=UML_Attribute)
gen_UML_Property_Attribute = Generalization(general=Attribute, specific=UML_Property)
gen_UML_Class_Package = Generalization(general=Package, specific=UML_Class)
gen_UML_Interface_Class = Generalization(general=Class_, specific=UML_Interface)
gen_UML_EnumerationLiteral_Package = Generalization(general=Package, specific=UML_EnumerationLiteral)
gen_UML_Enumeration_Class = Generalization(general=Class_, specific=UML_Enumeration)
gen_UML_Parameter_TypedElement = Generalization(general=TypedElement, specific=UML_Parameter)
gen_UML_Operation_Package = Generalization(general=Package, specific=UML_Operation)
gen_UML_Generalization_Element = Generalization(general=Element, specific=UML_Generalization)
gen_UML_Association_Package = Generalization(general=Package, specific=UML_Association)
gen_UML_TemplateParameterSubstitution_Element = Generalization(general=Element, specific=UML_TemplateParameterSubstitution)
gen_UML_TemplateBinding_Element = Generalization(general=Element, specific=UML_TemplateBinding)

# Domain Model
domain_model = DomainModel(
    name="UML",
    types={UML_PackageableElement, Element, UML_Package, PackageableElement, UML_Model, Package, UML_TypedElement, UML_LiteralInteger, UML_LiteralUnlimitedNatural, UML_PrimitiveType, UML_Attribute, TypedElement, UML_Property, Attribute, UML_Element, UML_Generalization, UML_TemplateBinding, Class_, UML_EnumerationLiteral, UML_Enumeration, UML_Association, UML_Interface, UML_Parameter, UML_Operation, UML_Class, UML_TemplateParameterSubstitution},
    associations={packagedElement0, type1, lowerValue3, upperValue5, class20, interface22, ownedAttribute25, ownedOperation27, generalization30, templateBinding32, nestedClassifier35, classifier37, enumeration38, ownedLiteral41, association7, qualifier9, owningAssociation11, associationEnd14, interface17, ownedParameter19, parameterSubstitution61, boundElement64, general44, specific47, memberEnd50, ownedEnd53, actual56, templateBinding58},
    generalizations={gen_UML_PackageableElement_Element, gen_UML_Package_PackageableElement, gen_UML_Model_Package, gen_UML_TypedElement_Element, gen_UML_PrimitiveType_Package, gen_UML_LiteralInteger_Package, gen_UML_LiteralUnlimitedNatural_Package, gen_UML_Attribute_TypedElement, gen_UML_Property_Attribute, gen_UML_Class_Package, gen_UML_Interface_Class, gen_UML_EnumerationLiteral_Package, gen_UML_Enumeration_Class, gen_UML_Parameter_TypedElement, gen_UML_Operation_Package, gen_UML_Generalization_Element, gen_UML_Association_Package, gen_UML_TemplateParameterSubstitution_Element, gen_UML_TemplateBinding_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)