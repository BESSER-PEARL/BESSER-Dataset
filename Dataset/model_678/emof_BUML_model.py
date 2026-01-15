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
emof_DataType = Class(name="emof::DataType")
emof_Element = Class(name="emof::Element", is_abstract=True)
Object = Class(name="Object")
emof_Class = Class(name="emof::Class")
Type = Class(name="Type")
emof_Property = Class(name="emof::Property")
emof_Operation = Class(name="emof::Operation")
emof_NamedElement = Class(name="emof::NamedElement", is_abstract=True)
emof_Extent = Class(name="emof::Extent")
emof_Object = Class(name="emof::Object")
MultiplicityElement = Class(name="MultiplicityElement")
TypedElement = Class(name="TypedElement")
emof_Tag = Class(name="emof::Tag")
emof_Comment = Class(name="emof::Comment")
Element = Class(name="Element")
emof_Enumeration = Class(name="emof::Enumeration")
DataType = Class(name="DataType")
emof_EnumerationLiteral = Class(name="emof::EnumerationLiteral")
emof_Parameter = Class(name="emof::Parameter")
emof_Type = Class(name="emof::Type", is_abstract=True)
emof_MultiplicityElement = Class(name="emof::MultiplicityElement", is_abstract=True)
emof_Package = Class(name="emof::Package")
NamedElement = Class(name="NamedElement")
emof_TypedElement = Class(name="emof::TypedElement", is_abstract=True)
emof_PrimitiveType = Class(name="emof::PrimitiveType")
emof_URIExtent = Class(name="emof::URIExtent")
Extent = Class(name="Extent")

# emof_DataType class attributes and methods

# emof_Element class attributes and methods

# Object class attributes and methods

# emof_Class class attributes and methods
emof_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
emof_Class.attributes={emof_Class_isAbstract}

# Type class attributes and methods

# emof_Property class attributes and methods
emof_Property_isDerived: Property = Property(name="isDerived", type=StringType)
emof_Property_isComposite: Property = Property(name="isComposite", type=StringType)
emof_Property_isId: Property = Property(name="isId", type=StringType)
emof_Property_default: Property = Property(name="default", type=StringType)
emof_Property_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
emof_Property.attributes={emof_Property_isDerived, emof_Property_isComposite, emof_Property_isId, emof_Property_default, emof_Property_isReadOnly}

# emof_Operation class attributes and methods

# emof_NamedElement class attributes and methods
emof_NamedElement_name: Property = Property(name="name", type=StringType)
emof_NamedElement.attributes={emof_NamedElement_name}

# emof_Extent class attributes and methods

# emof_Object class attributes and methods

# MultiplicityElement class attributes and methods

# TypedElement class attributes and methods

# emof_Tag class attributes and methods
emof_Tag_value: Property = Property(name="value", type=StringType)
emof_Tag_name: Property = Property(name="name", type=StringType)
emof_Tag.attributes={emof_Tag_name, emof_Tag_value}

# emof_Comment class attributes and methods

# Element class attributes and methods

# emof_Enumeration class attributes and methods

# DataType class attributes and methods

# emof_EnumerationLiteral class attributes and methods

# emof_Parameter class attributes and methods

# emof_Type class attributes and methods

# emof_MultiplicityElement class attributes and methods
emof_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
emof_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
emof_MultiplicityElement_lower: Property = Property(name="lower", type=StringType)
emof_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
emof_MultiplicityElement.attributes={emof_MultiplicityElement_isUnique, emof_MultiplicityElement_isOrdered, emof_MultiplicityElement_upper, emof_MultiplicityElement_lower}

# emof_Package class attributes and methods
emof_Package_uri: Property = Property(name="uri", type=StringType)
emof_Package.attributes={emof_Package_uri}

# NamedElement class attributes and methods

# emof_TypedElement class attributes and methods

# emof_PrimitiveType class attributes and methods

# emof_URIExtent class attributes and methods

# Extent class attributes and methods

# Relationships
ownedOperation1: BinaryAssociation = BinaryAssociation(
    name="ownedOperation1",
    ends={
        Property(name="Operation", type=emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class2", type=emof_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass4: BinaryAssociation = BinaryAssociation(
    name="superClass4",
    ends={
        Property(name="emof_Class", type=emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Class3", type=emof_Class, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute0: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute0",
    ends={
        Property(name="Property", type=emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class", type=emof_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLiteral8: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral8",
    ends={
        Property(name="EnumerationLiteral", type=emof_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=emof_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tag5: BinaryAssociation = BinaryAssociation(
    name="tag5",
    ends={
        Property(name="Tag", type=emof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="element", type=emof_Tag, multiplicity=Multiplicity(0, 9999))
    }
)
ownedComment6: BinaryAssociation = BinaryAssociation(
    name="ownedComment6",
    ends={
        Property(name="emof_Comment", type=emof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Element", type=emof_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element7: BinaryAssociation = BinaryAssociation(
    name="element7",
    ends={
        Property(name="Element", type=emof_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="tag", type=emof_Element, multiplicity=Multiplicity(0, 9999))
    }
)
ownedType12: BinaryAssociation = BinaryAssociation(
    name="ownedType12",
    ends={
        Property(name="package", type=emof_Type, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Type", type=emof_Package, multiplicity=Multiplicity(1, 1))
    }
)
nestedPackage14: BinaryAssociation = BinaryAssociation(
    name="nestedPackage14",
    ends={
        Property(name="emof_Package", type=emof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Package13", type=emof_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package15: BinaryAssociation = BinaryAssociation(
    name="package15",
    ends={
        Property(name="Package", type=emof_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType", type=emof_Package, multiplicity=Multiplicity(1, 1))
    }
)
class9: BinaryAssociation = BinaryAssociation(
    name="class9",
    ends={
        Property(name="Class", type=emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=emof_Class, multiplicity=Multiplicity(1, 1))
    }
)
ownedParameter10: BinaryAssociation = BinaryAssociation(
    name="ownedParameter10",
    ends={
        Property(name="Parameter", type=emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=emof_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException11: BinaryAssociation = BinaryAssociation(
    name="raisedException11",
    ends={
        Property(name="emof_Type", type=emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Operation", type=emof_Type, multiplicity=Multiplicity(0, 9999))
    }
)
type23: BinaryAssociation = BinaryAssociation(
    name="type23",
    ends={
        Property(name="emof_Type24", type=emof_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_TypedElement", type=emof_Type, multiplicity=Multiplicity(0, 1))
    }
)
operation16: BinaryAssociation = BinaryAssociation(
    name="operation16",
    ends={
        Property(name="Operation17", type=emof_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameter", type=emof_Operation, multiplicity=Multiplicity(0, 1))
    }
)
enumeration18: BinaryAssociation = BinaryAssociation(
    name="enumeration18",
    ends={
        Property(name="Enumeration", type=emof_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=emof_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
class19: BinaryAssociation = BinaryAssociation(
    name="class19",
    ends={
        Property(name="Class20", type=emof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute", type=emof_Class, multiplicity=Multiplicity(1, 1))
    }
)
opposite22: BinaryAssociation = BinaryAssociation(
    name="opposite22",
    ends={
        Property(name="emof_Property", type=emof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Property21", type=emof_Property, multiplicity=Multiplicity(0, 1))
    }
)
annotatedElement25: BinaryAssociation = BinaryAssociation(
    name="annotatedElement25",
    ends={
        Property(name="emof_NamedElement", type=emof_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Comment26", type=emof_NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_emof_DataType_Type = Generalization(general=Type, specific=emof_DataType)
gen_emof_Element_Object = Generalization(general=Object, specific=emof_Element)
gen_emof_Class_Type = Generalization(general=Type, specific=emof_Class)
gen_emof_NamedElement_Element = Generalization(general=Element, specific=emof_NamedElement)
gen_emof_Extent_Object = Generalization(general=Object, specific=emof_Extent)
gen_emof_Operation_MultiplicityElement = Generalization(general=MultiplicityElement, specific=emof_Operation)
gen_emof_Operation_TypedElement = Generalization(general=TypedElement, specific=emof_Operation)
gen_emof_Tag_Element = Generalization(general=Element, specific=emof_Tag)
gen_emof_Enumeration_DataType = Generalization(general=DataType, specific=emof_Enumeration)
gen_emof_Type_NamedElement = Generalization(general=NamedElement, specific=emof_Type)
gen_emof_Package_NamedElement = Generalization(general=NamedElement, specific=emof_Package)
gen_emof_TypedElement_NamedElement = Generalization(general=NamedElement, specific=emof_TypedElement)
gen_emof_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=emof_Parameter)
gen_emof_Parameter_TypedElement = Generalization(general=TypedElement, specific=emof_Parameter)
gen_emof_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=emof_EnumerationLiteral)
gen_emof_Property_MultiplicityElement = Generalization(general=MultiplicityElement, specific=emof_Property)
gen_emof_Property_TypedElement = Generalization(general=TypedElement, specific=emof_Property)
gen_emof_PrimitiveType_DataType = Generalization(general=DataType, specific=emof_PrimitiveType)
gen_emof_URIExtent_Extent = Generalization(general=Extent, specific=emof_URIExtent)
gen_emof_Comment_Element = Generalization(general=Element, specific=emof_Comment)

# Domain Model
domain_model = DomainModel(
    name="emof",
    types={emof_DataType, emof_Element, Object, emof_Class, Type, emof_Property, emof_Operation, emof_NamedElement, emof_Extent, emof_Object, MultiplicityElement, TypedElement, emof_Tag, emof_Comment, Element, emof_Enumeration, DataType, emof_EnumerationLiteral, emof_Parameter, emof_Type, emof_MultiplicityElement, emof_Package, NamedElement, emof_TypedElement, emof_PrimitiveType, emof_URIExtent, Extent},
    associations={ownedOperation1, superClass4, ownedAttribute0, ownedLiteral8, tag5, ownedComment6, element7, ownedType12, nestedPackage14, package15, class9, ownedParameter10, raisedException11, type23, operation16, enumeration18, class19, opposite22, annotatedElement25},
    generalizations={gen_emof_DataType_Type, gen_emof_Element_Object, gen_emof_Class_Type, gen_emof_NamedElement_Element, gen_emof_Extent_Object, gen_emof_Operation_MultiplicityElement, gen_emof_Operation_TypedElement, gen_emof_Tag_Element, gen_emof_Enumeration_DataType, gen_emof_Type_NamedElement, gen_emof_Package_NamedElement, gen_emof_TypedElement_NamedElement, gen_emof_Parameter_MultiplicityElement, gen_emof_Parameter_TypedElement, gen_emof_EnumerationLiteral_NamedElement, gen_emof_Property_MultiplicityElement, gen_emof_Property_TypedElement, gen_emof_PrimitiveType_DataType, gen_emof_URIExtent_Extent, gen_emof_Comment_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)