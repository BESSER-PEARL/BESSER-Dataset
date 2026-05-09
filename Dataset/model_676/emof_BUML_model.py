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
Enumeration_ = Class(name="Enumeration")
emof_Extent = Class(name="emof_Extent")
emof_MultiplicityElement = Class(name="emof_MultiplicityElement", is_abstract=True)
emof_Class = Class(name="emof_Class")
Type = Class(name="Type")
Property_ = Class(name="Property")
Operation = Class(name="Operation")
Class_ = Class(name="Class")
emof_Comment = Class(name="emof_Comment")
Element = Class(name="Element")
NamedElement = Class(name="NamedElement")
emof_DataType = Class(name="emof_DataType")
emof_Element = Class(name="emof_Element", is_abstract=True)
Object = Class(name="Object")
Comment = Class(name="Comment")
Tag = Class(name="Tag")
emof_Enumeration = Class(name="emof_Enumeration")
DataType = Class(name="DataType")
EnumerationLiteral = Class(name="EnumerationLiteral")
emof_EnumerationLiteral = Class(name="emof_EnumerationLiteral")
emof_NamedElement = Class(name="emof_NamedElement", is_abstract=True)
emof_Object = Class(name="emof_Object")
emof_Operation = Class(name="emof_Operation")
TypedElement = Class(name="TypedElement")
MultiplicityElement = Class(name="MultiplicityElement")
Parameter_ = Class(name="Parameter")
emof_Package = Class(name="emof_Package")
Package = Class(name="Package")
emof_Parameter = Class(name="emof_Parameter")
emof_PrimitiveType = Class(name="emof_PrimitiveType")
emof_Property = Class(name="emof_Property")
emof_Tag = Class(name="emof_Tag")
emof_Type = Class(name="emof_Type", is_abstract=True)
emof_TypedElement = Class(name="emof_TypedElement", is_abstract=True)
emof_URIExtent = Class(name="emof_URIExtent")
Extent = Class(name="Extent")

# Enumeration class attributes and methods

# emof_Extent class attributes and methods

# emof_MultiplicityElement class attributes and methods
emof_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
emof_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
emof_MultiplicityElement_lower: Property = Property(name="lower", type=StringType)
emof_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
emof_MultiplicityElement.attributes={emof_MultiplicityElement_isUnique, emof_MultiplicityElement_upper, emof_MultiplicityElement_lower, emof_MultiplicityElement_isOrdered}

# emof_Class class attributes and methods
emof_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
emof_Class.attributes={emof_Class_isAbstract}

# Type class attributes and methods

# Property class attributes and methods

# Operation class attributes and methods

# Class class attributes and methods

# emof_Comment class attributes and methods

# Element class attributes and methods

# NamedElement class attributes and methods

# emof_DataType class attributes and methods

# emof_Element class attributes and methods

# Object class attributes and methods

# Comment class attributes and methods

# Tag class attributes and methods

# emof_Enumeration class attributes and methods

# DataType class attributes and methods

# EnumerationLiteral class attributes and methods

# emof_EnumerationLiteral class attributes and methods

# emof_NamedElement class attributes and methods
emof_NamedElement_name: Property = Property(name="name", type=StringType)
emof_NamedElement.attributes={emof_NamedElement_name}

# emof_Object class attributes and methods

# emof_Operation class attributes and methods

# TypedElement class attributes and methods

# MultiplicityElement class attributes and methods

# Parameter class attributes and methods

# emof_Package class attributes and methods
emof_Package_uri: Property = Property(name="uri", type=StringType)
emof_Package.attributes={emof_Package_uri}

# Package class attributes and methods

# emof_Parameter class attributes and methods

# emof_PrimitiveType class attributes and methods

# emof_Property class attributes and methods
emof_Property_isDerived: Property = Property(name="isDerived", type=StringType)
emof_Property_isId: Property = Property(name="isId", type=StringType)
emof_Property_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
emof_Property_default: Property = Property(name="default", type=StringType)
emof_Property_isComposite: Property = Property(name="isComposite", type=StringType)
emof_Property.attributes={emof_Property_isComposite, emof_Property_isId, emof_Property_isDerived, emof_Property_default, emof_Property_isReadOnly}

# emof_Tag class attributes and methods
emof_Tag_name: Property = Property(name="name", type=StringType)
emof_Tag_value: Property = Property(name="value", type=StringType)
emof_Tag.attributes={emof_Tag_name, emof_Tag_value}

# emof_Type class attributes and methods

# emof_TypedElement class attributes and methods

# emof_URIExtent class attributes and methods

# Extent class attributes and methods

# Relationships
enumeration10: BinaryAssociation = BinaryAssociation(
    name="enumeration10",
    ends={
        Property(name="Enumeration", type=emof_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_EnumerationLiteral", type=Enumeration_, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute0: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute0",
    ends={
        Property(name="Property", type=emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Class", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation1: BinaryAssociation = BinaryAssociation(
    name="ownedOperation1",
    ends={
        Property(name="Operation", type=emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Class2", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass3: BinaryAssociation = BinaryAssociation(
    name="superClass3",
    ends={
        Property(name="Class", type=emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Class4", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
annotatedElement5: BinaryAssociation = BinaryAssociation(
    name="annotatedElement5",
    ends={
        Property(name="NamedElement", type=emof_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Comment", type=NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedComment6: BinaryAssociation = BinaryAssociation(
    name="ownedComment6",
    ends={
        Property(name="Comment", type=emof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Element", type=Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tag7: BinaryAssociation = BinaryAssociation(
    name="tag7",
    ends={
        Property(name="Tag", type=emof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Element8", type=Tag, multiplicity=Multiplicity(0, 9999))
    }
)
ownedLiteral9: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral9",
    ends={
        Property(name="EnumerationLiteral", type=emof_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Enumeration", type=EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opposite25: BinaryAssociation = BinaryAssociation(
    name="opposite25",
    ends={
        Property(name="Property27", type=emof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Property26", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
class_11: BinaryAssociation = BinaryAssociation(
    name="class_11",
    ends={
        Property(name="Class12", type=emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Operation", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
ownedParameter13: BinaryAssociation = BinaryAssociation(
    name="ownedParameter13",
    ends={
        Property(name="Parameter", type=emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Operation14", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException15: BinaryAssociation = BinaryAssociation(
    name="raisedException15",
    ends={
        Property(name="Type", type=emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Operation16", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
nestedPackage17: BinaryAssociation = BinaryAssociation(
    name="nestedPackage17",
    ends={
        Property(name="Package", type=emof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Package", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType18: BinaryAssociation = BinaryAssociation(
    name="ownedType18",
    ends={
        Property(name="Type20", type=emof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Package19", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation21: BinaryAssociation = BinaryAssociation(
    name="operation21",
    ends={
        Property(name="Operation22", type=emof_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Parameter", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
class_23: BinaryAssociation = BinaryAssociation(
    name="class_23",
    ends={
        Property(name="Class24", type=emof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Property", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
element28: BinaryAssociation = BinaryAssociation(
    name="element28",
    ends={
        Property(name="Element", type=emof_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Tag", type=Element, multiplicity=Multiplicity(0, 9999))
    }
)
package29: BinaryAssociation = BinaryAssociation(
    name="package29",
    ends={
        Property(name="Package30", type=emof_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Type", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
type31: BinaryAssociation = BinaryAssociation(
    name="type31",
    ends={
        Property(name="Type32", type=emof_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_TypedElement", type=Type, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_emof_Extent_Object = Generalization(general=Object, specific=emof_Extent)
gen_emof_Class_Type = Generalization(general=Type, specific=emof_Class)
gen_emof_Comment_Element = Generalization(general=Element, specific=emof_Comment)
gen_emof_DataType_Type = Generalization(general=Type, specific=emof_DataType)
gen_emof_Element_Object = Generalization(general=Object, specific=emof_Element)
gen_emof_Enumeration_DataType = Generalization(general=DataType, specific=emof_Enumeration)
gen_emof_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=emof_EnumerationLiteral)
gen_emof_NamedElement_Element = Generalization(general=Element, specific=emof_NamedElement)
gen_emof_Operation_TypedElement = Generalization(general=TypedElement, specific=emof_Operation)
gen_emof_Operation_MultiplicityElement = Generalization(general=MultiplicityElement, specific=emof_Operation)
gen_emof_Package_NamedElement = Generalization(general=NamedElement, specific=emof_Package)
gen_emof_Parameter_TypedElement = Generalization(general=TypedElement, specific=emof_Parameter)
gen_emof_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=emof_Parameter)
gen_emof_PrimitiveType_DataType = Generalization(general=DataType, specific=emof_PrimitiveType)
gen_emof_Property_TypedElement = Generalization(general=TypedElement, specific=emof_Property)
gen_emof_Property_MultiplicityElement = Generalization(general=MultiplicityElement, specific=emof_Property)
gen_emof_Tag_Element = Generalization(general=Element, specific=emof_Tag)
gen_emof_Type_NamedElement = Generalization(general=NamedElement, specific=emof_Type)
gen_emof_TypedElement_NamedElement = Generalization(general=NamedElement, specific=emof_TypedElement)
gen_emof_URIExtent_Extent = Generalization(general=Extent, specific=emof_URIExtent)

# Domain Model
domain_model = DomainModel(
    name="emof",
    types={Enumeration_, emof_Extent, emof_MultiplicityElement, emof_Class, Type, Property_, Operation, Class_, emof_Comment, Element, NamedElement, emof_DataType, emof_Element, Object, Comment, Tag, emof_Enumeration, DataType, EnumerationLiteral, emof_EnumerationLiteral, emof_NamedElement, emof_Object, emof_Operation, TypedElement, MultiplicityElement, Parameter_, emof_Package, Package, emof_Parameter, emof_PrimitiveType, emof_Property, emof_Tag, emof_Type, emof_TypedElement, emof_URIExtent, Extent},
    associations={enumeration10, ownedAttribute0, ownedOperation1, superClass3, annotatedElement5, ownedComment6, tag7, ownedLiteral9, opposite25, class_11, ownedParameter13, raisedException15, nestedPackage17, ownedType18, operation21, class_23, element28, package29, type31},
    generalizations={gen_emof_Extent_Object, gen_emof_Class_Type, gen_emof_Comment_Element, gen_emof_DataType_Type, gen_emof_Element_Object, gen_emof_Enumeration_DataType, gen_emof_EnumerationLiteral_NamedElement, gen_emof_NamedElement_Element, gen_emof_Operation_TypedElement, gen_emof_Operation_MultiplicityElement, gen_emof_Package_NamedElement, gen_emof_Parameter_TypedElement, gen_emof_Parameter_MultiplicityElement, gen_emof_PrimitiveType_DataType, gen_emof_Property_TypedElement, gen_emof_Property_MultiplicityElement, gen_emof_Tag_Element, gen_emof_Type_NamedElement, gen_emof_TypedElement_NamedElement, gen_emof_URIExtent_Extent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)