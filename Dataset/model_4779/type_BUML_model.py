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
RelationType: Enumeration = Enumeration(
    name="RelationType",
    literals={
            EnumerationLiteral(name="One2One"),
			EnumerationLiteral(name="One2Many"),
			EnumerationLiteral(name="Many2Many")
    }
)

Containment: Enumeration = Enumeration(
    name="Containment",
    literals={
            EnumerationLiteral(name="Source"),
			EnumerationLiteral(name="Target"),
			EnumerationLiteral(name="Non")
    }
)

# Classes
Categorized = Class(name="Categorized")
type_References = Class(name="type::References")
Relationship = Class(name="Relationship")
type_Generalization = Class(name="type::Generalization")
type_TypeGroup = Class(name="type::TypeGroup")
type_TypeElement = Class(name="type::TypeElement")
type_Relationship = Class(name="type::Relationship")
type_PrimitivesGroup = Class(name="type::PrimitivesGroup")
type_Primitive = Class(name="type::Primitive")
type_Operation = Class(name="type::Operation")
Secured = Class(name="Secured")
type_Parameter = Class(name="type::Parameter")
type_ReturnValue = Class(name="type::ReturnValue")
TypeElement = Class(name="TypeElement")
type_TypePointer = Class(name="type::TypePointer")
type_PackagePointer = Class(name="type::PackagePointer")
type_Assosiation = Class(name="type::Assosiation")
type_Link = Class(name="type::Link")
type_Attribute = Class(name="type::Attribute")
TypePointer = Class(name="TypePointer")
type_Type = Class(name="type::Type")
type_TypeReference = Class(name="type::TypeReference")
type_Enumerator = Class(name="type::Enumerator")
type_EnumAttribute = Class(name="type::EnumAttribute")
type_MethodPointer = Class(name="type::MethodPointer")
type_AttributePointer = Class(name="type::AttributePointer")

# Categorized class attributes and methods

# type_References class attributes and methods

# Relationship class attributes and methods

# type_Generalization class attributes and methods

# type_TypeGroup class attributes and methods
type_TypeGroup_uid: Property = Property(name="uid", type=StringType)
type_TypeGroup_name: Property = Property(name="name", type=StringType)
type_TypeGroup.attributes={type_TypeGroup_name, type_TypeGroup_uid}

# type_TypeElement class attributes and methods
type_TypeElement_uid: Property = Property(name="uid", type=StringType)
type_TypeElement_name: Property = Property(name="name", type=StringType)
type_TypeElement.attributes={type_TypeElement_name, type_TypeElement_uid}

# type_Relationship class attributes and methods
type_Relationship_uid: Property = Property(name="uid", type=StringType)
type_Relationship.attributes={type_Relationship_uid}

# type_PrimitivesGroup class attributes and methods

# type_Primitive class attributes and methods

# type_Operation class attributes and methods
type_Operation_uid: Property = Property(name="uid", type=StringType)
type_Operation_name: Property = Property(name="name", type=StringType)
type_Operation.attributes={type_Operation_uid, type_Operation_name}

# Secured class attributes and methods

# type_Parameter class attributes and methods
type_Parameter_uid: Property = Property(name="uid", type=StringType)
type_Parameter_name: Property = Property(name="name", type=StringType)
type_Parameter_order: Property = Property(name="order", type=IntegerType)
type_Parameter.attributes={type_Parameter_uid, type_Parameter_name, type_Parameter_order}

# type_ReturnValue class attributes and methods
type_ReturnValue_uid: Property = Property(name="uid", type=StringType)
type_ReturnValue.attributes={type_ReturnValue_uid}

# TypeElement class attributes and methods

# type_TypePointer class attributes and methods

# type_PackagePointer class attributes and methods

# type_Assosiation class attributes and methods
type_Assosiation_type: Property = Property(name="type", type=StringType)
type_Assosiation_containment: Property = Property(name="containment", type=StringType)
type_Assosiation_internal: Property = Property(name="internal", type=BooleanType)
type_Assosiation_sourceOperation: Property = Property(name="sourceOperation", type=StringType)
type_Assosiation_targetOperation: Property = Property(name="targetOperation", type=StringType)
type_Assosiation.attributes={type_Assosiation_containment, type_Assosiation_internal, type_Assosiation_type, type_Assosiation_sourceOperation, type_Assosiation_targetOperation}

# type_Link class attributes and methods
type_Link_uid: Property = Property(name="uid", type=StringType)
type_Link.attributes={type_Link_uid}

# type_Attribute class attributes and methods
type_Attribute_uid: Property = Property(name="uid", type=StringType)
type_Attribute_name: Property = Property(name="name", type=StringType)
type_Attribute_pk: Property = Property(name="pk", type=BooleanType)
type_Attribute.attributes={type_Attribute_pk, type_Attribute_uid, type_Attribute_name}

# TypePointer class attributes and methods

# type_Type class attributes and methods

# type_TypeReference class attributes and methods

# type_Enumerator class attributes and methods

# type_EnumAttribute class attributes and methods
type_EnumAttribute_uid: Property = Property(name="uid", type=StringType)
type_EnumAttribute_name: Property = Property(name="name", type=StringType)
type_EnumAttribute_value: Property = Property(name="value", type=StringType)
type_EnumAttribute.attributes={type_EnumAttribute_name, type_EnumAttribute_value, type_EnumAttribute_uid}

# type_MethodPointer class attributes and methods

# type_AttributePointer class attributes and methods

# Relationships
source4: BinaryAssociation = BinaryAssociation(
    name="source4",
    ends={
        Property(name="type_TypeElement6", type=type_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="type_Relationship5", type=type_TypeElement, multiplicity=Multiplicity(0, 1))
    }
)
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="type_TypeElement9", type=type_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="type_Relationship8", type=type_TypeElement, multiplicity=Multiplicity(0, 1))
    }
)
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="type_TypeElement", type=type_TypeGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="type_TypeGroup", type=type_TypeElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationships1: BinaryAssociation = BinaryAssociation(
    name="relationships1",
    ends={
        Property(name="type_Relationship", type=type_TypeGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="type_TypeGroup2", type=type_Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primitives3: BinaryAssociation = BinaryAssociation(
    name="primitives3",
    ends={
        Property(name="type_Primitive", type=type_PrimitivesGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="type_PrimitivesGroup", type=type_Primitive, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters23: BinaryAssociation = BinaryAssociation(
    name="parameters23",
    ends={
        Property(name="type_Parameter", type=type_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="type_Operation", type=type_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnValue24: BinaryAssociation = BinaryAssociation(
    name="returnValue24",
    ends={
        Property(name="type_ReturnValue", type=type_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="type_Operation25", type=type_ReturnValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef10: BinaryAssociation = BinaryAssociation(
    name="typeRef10",
    ends={
        Property(name="type_TypeElement11", type=type_TypePointer, multiplicity=Multiplicity(1, 1)),
        Property(name="type_TypePointer", type=type_TypeElement, multiplicity=Multiplicity(0, 1))
    }
)
packageRef12: BinaryAssociation = BinaryAssociation(
    name="packageRef12",
    ends={
        Property(name="type_TypeGroup13", type=type_PackagePointer, multiplicity=Multiplicity(1, 1)),
        Property(name="type_PackagePointer", type=type_TypeGroup, multiplicity=Multiplicity(0, 1))
    }
)
links14: BinaryAssociation = BinaryAssociation(
    name="links14",
    ends={
        Property(name="type_Link", type=type_Assosiation, multiplicity=Multiplicity(1, 1)),
        Property(name="type_Assosiation", type=type_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
many2manyHelper15: BinaryAssociation = BinaryAssociation(
    name="many2manyHelper15",
    ends={
        Property(name="type_TypePointer17", type=type_Assosiation, multiplicity=Multiplicity(1, 1)),
        Property(name="type_Assosiation16", type=type_TypePointer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
masterField18: BinaryAssociation = BinaryAssociation(
    name="masterField18",
    ends={
        Property(name="type_Attribute", type=type_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="type_Link19", type=type_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
detailField20: BinaryAssociation = BinaryAssociation(
    name="detailField20",
    ends={
        Property(name="type_Attribute22", type=type_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="type_Link21", type=type_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
attributes26: BinaryAssociation = BinaryAssociation(
    name="attributes26",
    ends={
        Property(name="type_Attribute27", type=type_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="type_Type", type=type_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations28: BinaryAssociation = BinaryAssociation(
    name="operations28",
    ends={
        Property(name="type_Operation30", type=type_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="type_Type29", type=type_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values31: BinaryAssociation = BinaryAssociation(
    name="values31",
    ends={
        Property(name="type_EnumAttribute", type=type_Enumerator, multiplicity=Multiplicity(1, 1)),
        Property(name="type_Enumerator", type=type_EnumAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodRef32: BinaryAssociation = BinaryAssociation(
    name="methodRef32",
    ends={
        Property(name="type_Operation33", type=type_MethodPointer, multiplicity=Multiplicity(1, 1)),
        Property(name="type_MethodPointer", type=type_Operation, multiplicity=Multiplicity(0, 1))
    }
)
attributeRef34: BinaryAssociation = BinaryAssociation(
    name="attributeRef34",
    ends={
        Property(name="type_Attribute35", type=type_AttributePointer, multiplicity=Multiplicity(1, 1)),
        Property(name="type_AttributePointer", type=type_Attribute, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_type_Relationship_Categorized = Generalization(general=Categorized, specific=type_Relationship)
gen_type_References_Relationship = Generalization(general=Relationship, specific=type_References)
gen_type_Generalization_Relationship = Generalization(general=Relationship, specific=type_Generalization)
gen_type_Operation_Secured = Generalization(general=Secured, specific=type_Operation)
gen_type_Operation_Categorized = Generalization(general=Categorized, specific=type_Operation)
gen_type_Primitive_TypeElement = Generalization(general=TypeElement, specific=type_Primitive)
gen_type_Assosiation_Relationship = Generalization(general=Relationship, specific=type_Assosiation)
gen_type_Attribute_TypePointer = Generalization(general=TypePointer, specific=type_Attribute)
gen_type_Attribute_Categorized = Generalization(general=Categorized, specific=type_Attribute)
gen_type_Type_TypeElement = Generalization(general=TypeElement, specific=type_Type)
gen_type_Type_Categorized = Generalization(general=Categorized, specific=type_Type)
gen_type_TypeReference_TypeElement = Generalization(general=TypeElement, specific=type_TypeReference)
gen_type_TypeReference_TypePointer = Generalization(general=TypePointer, specific=type_TypeReference)
gen_type_Parameter_TypePointer = Generalization(general=TypePointer, specific=type_Parameter)
gen_type_ReturnValue_TypePointer = Generalization(general=TypePointer, specific=type_ReturnValue)
gen_type_Enumerator_TypeElement = Generalization(general=TypeElement, specific=type_Enumerator)
gen_type_Enumerator_Categorized = Generalization(general=Categorized, specific=type_Enumerator)
gen_type_EnumAttribute_Categorized = Generalization(general=Categorized, specific=type_EnumAttribute)

# Domain Model
domain_model = DomainModel(
    name="type",
    types={Categorized, type_References, Relationship, type_Generalization, type_TypeGroup, type_TypeElement, type_Relationship, type_PrimitivesGroup, type_Primitive, type_Operation, Secured, type_Parameter, type_ReturnValue, TypeElement, type_TypePointer, type_PackagePointer, type_Assosiation, type_Link, type_Attribute, TypePointer, type_Type, type_TypeReference, type_Enumerator, type_EnumAttribute, type_MethodPointer, type_AttributePointer, RelationType, Containment},
    associations={source4, target7, types0, relationships1, primitives3, parameters23, returnValue24, typeRef10, packageRef12, links14, many2manyHelper15, masterField18, detailField20, attributes26, operations28, values31, methodRef32, attributeRef34},
    generalizations={gen_type_Relationship_Categorized, gen_type_References_Relationship, gen_type_Generalization_Relationship, gen_type_Operation_Secured, gen_type_Operation_Categorized, gen_type_Primitive_TypeElement, gen_type_Assosiation_Relationship, gen_type_Attribute_TypePointer, gen_type_Attribute_Categorized, gen_type_Type_TypeElement, gen_type_Type_Categorized, gen_type_TypeReference_TypeElement, gen_type_TypeReference_TypePointer, gen_type_Parameter_TypePointer, gen_type_ReturnValue_TypePointer, gen_type_Enumerator_TypeElement, gen_type_Enumerator_Categorized, gen_type_EnumAttribute_Categorized},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)