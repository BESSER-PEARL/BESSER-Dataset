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
Operation = Class(name="Operation")
Class_ = Class(name="Class")
EMOF_Comment = Class(name="EMOF::Comment")
Element = Class(name="Element")
EMOF_Class = Class(name="EMOF::Class")
Type = Class(name="Type")
Property_ = Class(name="Property")
Comment = Class(name="Comment")
NamedElement = Class(name="NamedElement")
EMOF_DataType = Class(name="EMOF::DataType")
EMOF_Element = Class(name="EMOF::Element", is_abstract=True)
Object = Class(name="Object")
Package = Class(name="Package")
EMOF_Enumeration = Class(name="EMOF::Enumeration")
DataType = Class(name="DataType")
EnumerationLiteral = Class(name="EnumerationLiteral")
EMOF_EnumerationLiteral = Class(name="EMOF::EnumerationLiteral")
Enumeration_ = Class(name="Enumeration")
EMOF_Extent = Class(name="EMOF::Extent")
EMOF_Factory = Class(name="EMOF::Factory")
Parameter_ = Class(name="Parameter")
EMOF_MultiplicityElement = Class(name="EMOF::MultiplicityElement", is_abstract=True)
EMOF_NamedElement = Class(name="EMOF::NamedElement", is_abstract=True)
EMOF_Object = Class(name="EMOF::Object")
EMOF_Operation = Class(name="EMOF::Operation")
TypedElement = Class(name="TypedElement")
MultiplicityElement = Class(name="MultiplicityElement")
EMOF_PrimitiveType = Class(name="EMOF::PrimitiveType")
EMOF_Property = Class(name="EMOF::Property")
EMOF_Package = Class(name="EMOF::Package")
EMOF_Parameter = Class(name="EMOF::Parameter")
EMOF_ReflectiveSequence = Class(name="EMOF::ReflectiveSequence")
ReflectiveCollection = Class(name="ReflectiveCollection")
EMOF_ReflectiveCollection = Class(name="EMOF::ReflectiveCollection")
EMOF_TypedElement = Class(name="EMOF::TypedElement", is_abstract=True)
EMOF_Tag = Class(name="EMOF::Tag")
EMOF_Type = Class(name="EMOF::Type", is_abstract=True)
EMOF_URIExtent = Class(name="EMOF::URIExtent")
Extent = Class(name="Extent")

# Operation class attributes and methods

# Class class attributes and methods

# EMOF_Comment class attributes and methods
EMOF_Comment_body: Property = Property(name="body", type=StringType)
EMOF_Comment.attributes={EMOF_Comment_body}

# Element class attributes and methods

# EMOF_Class class attributes and methods
EMOF_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
EMOF_Class.attributes={EMOF_Class_isAbstract}

# Type class attributes and methods

# Property class attributes and methods

# Comment class attributes and methods

# NamedElement class attributes and methods

# EMOF_DataType class attributes and methods

# EMOF_Element class attributes and methods
EMOF_Element_m_set: Method = Method(name="set", parameters={Parameter(name='property'), Parameter(name='object')})
EMOF_Element_m_unset: Method = Method(name="unset", parameters={Parameter(name='property')})
EMOF_Element_m_container: Method = Method(name="container", parameters={}, type=StringType)
EMOF_Element_m_equals: Method = Method(name="equals", parameters={Parameter(name='object')}, type=StringType)
EMOF_Element_m_get: Method = Method(name="get", parameters={Parameter(name='property')}, type=StringType)
EMOF_Element_m_getMetaClass: Method = Method(name="getMetaClass", parameters={}, type=StringType)
EMOF_Element_m_isSet: Method = Method(name="isSet", parameters={Parameter(name='property')}, type=StringType)
EMOF_Element.methods={EMOF_Element_m_container, EMOF_Element_m_set, EMOF_Element_m_equals, EMOF_Element_m_unset, EMOF_Element_m_get, EMOF_Element_m_isSet, EMOF_Element_m_getMetaClass}

# Object class attributes and methods

# Package class attributes and methods

# EMOF_Enumeration class attributes and methods

# DataType class attributes and methods

# EnumerationLiteral class attributes and methods

# EMOF_EnumerationLiteral class attributes and methods

# Enumeration class attributes and methods

# EMOF_Extent class attributes and methods
EMOF_Extent_m_elements: Method = Method(name="elements", parameters={}, type=StringType)
EMOF_Extent_m_useContainment: Method = Method(name="useContainment", parameters={}, type=StringType)
EMOF_Extent.methods={EMOF_Extent_m_elements, EMOF_Extent_m_useContainment}

# EMOF_Factory class attributes and methods
EMOF_Factory_m_create: Method = Method(name="create", parameters={Parameter(name='metaClass')}, type=StringType)
EMOF_Factory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='string'), Parameter(name='dataType')}, type=StringType)
EMOF_Factory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='dataType'), Parameter(name='object')}, type=StringType)
EMOF_Factory.methods={EMOF_Factory_m_create, EMOF_Factory_m_convertToString, EMOF_Factory_m_createFromString}

# Parameter class attributes and methods

# EMOF_MultiplicityElement class attributes and methods
EMOF_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
EMOF_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
EMOF_MultiplicityElement_lower: Property = Property(name="lower", type=StringType)
EMOF_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
EMOF_MultiplicityElement.attributes={EMOF_MultiplicityElement_isUnique, EMOF_MultiplicityElement_upper, EMOF_MultiplicityElement_isOrdered, EMOF_MultiplicityElement_lower}

# EMOF_NamedElement class attributes and methods
EMOF_NamedElement_name: Property = Property(name="name", type=StringType)
EMOF_NamedElement.attributes={EMOF_NamedElement_name}

# EMOF_Object class attributes and methods

# EMOF_Operation class attributes and methods

# TypedElement class attributes and methods

# MultiplicityElement class attributes and methods

# EMOF_PrimitiveType class attributes and methods

# EMOF_Property class attributes and methods
EMOF_Property_default: Property = Property(name="default", type=StringType)
EMOF_Property_isComposite: Property = Property(name="isComposite", type=StringType)
EMOF_Property_isDerived: Property = Property(name="isDerived", type=StringType)
EMOF_Property_isID: Property = Property(name="isID", type=StringType)
EMOF_Property_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
EMOF_Property.attributes={EMOF_Property_isComposite, EMOF_Property_isID, EMOF_Property_default, EMOF_Property_isReadOnly, EMOF_Property_isDerived}

# EMOF_Package class attributes and methods
EMOF_Package_uri: Property = Property(name="uri", type=StringType)
EMOF_Package.attributes={EMOF_Package_uri}

# EMOF_Parameter class attributes and methods

# EMOF_ReflectiveSequence class attributes and methods
EMOF_ReflectiveSequence_m_add: Method = Method(name="add", parameters={Parameter(name='object'), Parameter(name='index')})
EMOF_ReflectiveSequence_m_get: Method = Method(name="get", parameters={Parameter(name='index')}, type=StringType)
EMOF_ReflectiveSequence_m_remove: Method = Method(name="remove", parameters={Parameter(name='index')}, type=StringType)
EMOF_ReflectiveSequence_m_set: Method = Method(name="set", parameters={Parameter(name='object'), Parameter(name='index')}, type=StringType)
EMOF_ReflectiveSequence.methods={EMOF_ReflectiveSequence_m_set, EMOF_ReflectiveSequence_m_get, EMOF_ReflectiveSequence_m_add, EMOF_ReflectiveSequence_m_remove}

# ReflectiveCollection class attributes and methods

# EMOF_ReflectiveCollection class attributes and methods
EMOF_ReflectiveCollection_m_size: Method = Method(name="size", parameters={}, type=StringType)
EMOF_ReflectiveCollection_m_add: Method = Method(name="add", parameters={Parameter(name='object')}, type=StringType)
EMOF_ReflectiveCollection_m_addAll: Method = Method(name="addAll", parameters={Parameter(name='objects')}, type=StringType)
EMOF_ReflectiveCollection_m_clear: Method = Method(name="clear", parameters={})
EMOF_ReflectiveCollection_m_remove: Method = Method(name="remove", parameters={Parameter(name='object')}, type=StringType)
EMOF_ReflectiveCollection.methods={EMOF_ReflectiveCollection_m_size, EMOF_ReflectiveCollection_m_remove, EMOF_ReflectiveCollection_m_add, EMOF_ReflectiveCollection_m_addAll, EMOF_ReflectiveCollection_m_clear}

# EMOF_TypedElement class attributes and methods

# EMOF_Tag class attributes and methods
EMOF_Tag_name: Property = Property(name="name", type=StringType)
EMOF_Tag_value: Property = Property(name="value", type=StringType)
EMOF_Tag.attributes={EMOF_Tag_value, EMOF_Tag_name}

# EMOF_Type class attributes and methods
EMOF_Type_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=StringType)
EMOF_Type.methods={EMOF_Type_m_isInstance}

# EMOF_URIExtent class attributes and methods
EMOF_URIExtent_m_contextURI: Method = Method(name="contextURI", parameters={}, type=StringType)
EMOF_URIExtent_m_element: Method = Method(name="element", parameters={Parameter(name='uri')}, type=StringType)
EMOF_URIExtent_m_uri: Method = Method(name="uri", parameters={Parameter(name='element')}, type=StringType)
EMOF_URIExtent.methods={EMOF_URIExtent_m_uri, EMOF_URIExtent_m_element, EMOF_URIExtent_m_contextURI}

# Extent class attributes and methods

# Relationships
ownedOperation1: BinaryAssociation = BinaryAssociation(
    name="ownedOperation1",
    ends={
        Property(name="Operation", type=EMOF_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Class2", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass3: BinaryAssociation = BinaryAssociation(
    name="superClass3",
    ends={
        Property(name="Class", type=EMOF_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Class4", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute0: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute0",
    ends={
        Property(name="Property", type=EMOF_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Class", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedComment6: BinaryAssociation = BinaryAssociation(
    name="ownedComment6",
    ends={
        Property(name="Comment", type=EMOF_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Element", type=Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotatedElement5: BinaryAssociation = BinaryAssociation(
    name="annotatedElement5",
    ends={
        Property(name="NamedElement", type=EMOF_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Comment", type=NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
ownedLiteral7: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral7",
    ends={
        Property(name="EnumerationLiteral", type=EMOF_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Enumeration", type=EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration8: BinaryAssociation = BinaryAssociation(
    name="enumeration8",
    ends={
        Property(name="Enumeration", type=EMOF_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_EnumerationLiteral", type=Enumeration_, multiplicity=Multiplicity(0, 1))
    }
)
class10: BinaryAssociation = BinaryAssociation(
    name="class10",
    ends={
        Property(name="Class11", type=EMOF_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Operation", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameter12: BinaryAssociation = BinaryAssociation(
    name="ownedParameter12",
    ends={
        Property(name="Parameter", type=EMOF_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Operation13", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException14: BinaryAssociation = BinaryAssociation(
    name="raisedException14",
    ends={
        Property(name="Type", type=EMOF_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Operation15", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
package9: BinaryAssociation = BinaryAssociation(
    name="package9",
    ends={
        Property(name="Package", type=EMOF_Factory, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Factory", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
class26: BinaryAssociation = BinaryAssociation(
    name="class26",
    ends={
        Property(name="Class27", type=EMOF_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Property", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
nestedPackage16: BinaryAssociation = BinaryAssociation(
    name="nestedPackage16",
    ends={
        Property(name="Package17", type=EMOF_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Package", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestingPackage18: BinaryAssociation = BinaryAssociation(
    name="nestingPackage18",
    ends={
        Property(name="Package20", type=EMOF_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Package19", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
ownedType21: BinaryAssociation = BinaryAssociation(
    name="ownedType21",
    ends={
        Property(name="Type23", type=EMOF_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Package22", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation24: BinaryAssociation = BinaryAssociation(
    name="operation24",
    ends={
        Property(name="Operation25", type=EMOF_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Parameter", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
opposite28: BinaryAssociation = BinaryAssociation(
    name="opposite28",
    ends={
        Property(name="Property30", type=EMOF_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Property29", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
package32: BinaryAssociation = BinaryAssociation(
    name="package32",
    ends={
        Property(name="Package33", type=EMOF_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Type", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
type34: BinaryAssociation = BinaryAssociation(
    name="type34",
    ends={
        Property(name="Type35", type=EMOF_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_TypedElement", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
element31: BinaryAssociation = BinaryAssociation(
    name="element31",
    ends={
        Property(name="Element", type=EMOF_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="EMOF_Tag", type=Element, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_EMOF_Comment_Element = Generalization(general=Element, specific=EMOF_Comment)
gen_EMOF_Class_Type = Generalization(general=Type, specific=EMOF_Class)
gen_EMOF_DataType_Type = Generalization(general=Type, specific=EMOF_DataType)
gen_EMOF_Element_Object = Generalization(general=Object, specific=EMOF_Element)
gen_EMOF_Enumeration_DataType = Generalization(general=DataType, specific=EMOF_Enumeration)
gen_EMOF_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=EMOF_EnumerationLiteral)
gen_EMOF_Extent_Object = Generalization(general=Object, specific=EMOF_Extent)
gen_EMOF_Factory_Element = Generalization(general=Element, specific=EMOF_Factory)
gen_EMOF_NamedElement_Element = Generalization(general=Element, specific=EMOF_NamedElement)
gen_EMOF_Operation_TypedElement = Generalization(general=TypedElement, specific=EMOF_Operation)
gen_EMOF_Operation_MultiplicityElement = Generalization(general=MultiplicityElement, specific=EMOF_Operation)
gen_EMOF_PrimitiveType_DataType = Generalization(general=DataType, specific=EMOF_PrimitiveType)
gen_EMOF_Property_TypedElement = Generalization(general=TypedElement, specific=EMOF_Property)
gen_EMOF_Property_MultiplicityElement = Generalization(general=MultiplicityElement, specific=EMOF_Property)
gen_EMOF_Package_NamedElement = Generalization(general=NamedElement, specific=EMOF_Package)
gen_EMOF_Parameter_TypedElement = Generalization(general=TypedElement, specific=EMOF_Parameter)
gen_EMOF_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=EMOF_Parameter)
gen_EMOF_ReflectiveSequence_ReflectiveCollection = Generalization(general=ReflectiveCollection, specific=EMOF_ReflectiveSequence)
gen_EMOF_ReflectiveCollection_Object = Generalization(general=Object, specific=EMOF_ReflectiveCollection)
gen_EMOF_TypedElement_NamedElement = Generalization(general=NamedElement, specific=EMOF_TypedElement)
gen_EMOF_Tag_Element = Generalization(general=Element, specific=EMOF_Tag)
gen_EMOF_Type_NamedElement = Generalization(general=NamedElement, specific=EMOF_Type)
gen_EMOF_URIExtent_Extent = Generalization(general=Extent, specific=EMOF_URIExtent)

# Domain Model
domain_model = DomainModel(
    name="EMOF",
    types={Operation, Class_, EMOF_Comment, Element, EMOF_Class, Type, Property_, Comment, NamedElement, EMOF_DataType, EMOF_Element, Object, Package, EMOF_Enumeration, DataType, EnumerationLiteral, EMOF_EnumerationLiteral, Enumeration_, EMOF_Extent, EMOF_Factory, Parameter_, EMOF_MultiplicityElement, EMOF_NamedElement, EMOF_Object, EMOF_Operation, TypedElement, MultiplicityElement, EMOF_PrimitiveType, EMOF_Property, EMOF_Package, EMOF_Parameter, EMOF_ReflectiveSequence, ReflectiveCollection, EMOF_ReflectiveCollection, EMOF_TypedElement, EMOF_Tag, EMOF_Type, EMOF_URIExtent, Extent},
    associations={ownedOperation1, superClass3, ownedAttribute0, ownedComment6, annotatedElement5, ownedLiteral7, enumeration8, class10, ownedParameter12, raisedException14, package9, class26, nestedPackage16, nestingPackage18, ownedType21, operation24, opposite28, package32, type34, element31},
    generalizations={gen_EMOF_Comment_Element, gen_EMOF_Class_Type, gen_EMOF_DataType_Type, gen_EMOF_Element_Object, gen_EMOF_Enumeration_DataType, gen_EMOF_EnumerationLiteral_NamedElement, gen_EMOF_Extent_Object, gen_EMOF_Factory_Element, gen_EMOF_NamedElement_Element, gen_EMOF_Operation_TypedElement, gen_EMOF_Operation_MultiplicityElement, gen_EMOF_PrimitiveType_DataType, gen_EMOF_Property_TypedElement, gen_EMOF_Property_MultiplicityElement, gen_EMOF_Package_NamedElement, gen_EMOF_Parameter_TypedElement, gen_EMOF_Parameter_MultiplicityElement, gen_EMOF_ReflectiveSequence_ReflectiveCollection, gen_EMOF_ReflectiveCollection_Object, gen_EMOF_TypedElement_NamedElement, gen_EMOF_Tag_Element, gen_EMOF_Type_NamedElement, gen_EMOF_URIExtent_Extent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)