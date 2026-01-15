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
ModeType: Enumeration = Enumeration(
    name="ModeType",
    literals={
            EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="OUT"),
			EnumerationLiteral(name="INOUT")
    }
)

TypeType: Enumeration = Enumeration(
    name="TypeType",
    literals={
            EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="REFERENCE"),
			EnumerationLiteral(name="DATETIME"),
			EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="PERFORMER")
    }
)

# Classes
xpdl_DeclaredTypeType = Class(name="xpdl::DeclaredTypeType")
xpdl_SchemaTypeType = Class(name="xpdl::SchemaTypeType")
xpdl_ExternalReferenceType = Class(name="xpdl::ExternalReferenceType")
xpdl_BasicTypeType = Class(name="xpdl::BasicTypeType")
XpdlTypeType = Class(name="XpdlTypeType")
xpdl_DataTypeType = Class(name="xpdl::DataTypeType")
xpdl_Extensible = Class(name="xpdl::Extensible", is_abstract=True)
xpdl_ExternalPackages = Class(name="xpdl::ExternalPackages")
xpdl_ExtendedAttributesType = Class(name="xpdl::ExtendedAttributesType")
xpdl_ExtendedAttributeType = Class(name="xpdl::ExtendedAttributeType")
ExtendedAnnotationType = Class(name="ExtendedAnnotationType")
xpdl_FormalParameterType = Class(name="xpdl::FormalParameterType")
xpdl_ExternalPackage = Class(name="xpdl::ExternalPackage")
Extensible = Class(name="Extensible")
xpdl_FormalParametersType = Class(name="xpdl::FormalParametersType")
xpdl_XSDSchema = Class(name="xpdl::XSDSchema")
xpdl_ScriptType = Class(name="xpdl::ScriptType")
xpdl_TypeDeclarationsType = Class(name="xpdl::TypeDeclarationsType")
xpdl_TypeDeclarationType = Class(name="xpdl::TypeDeclarationType")
xpdl_extensions_ExtendedAnnotationType = Class(name="xpdl::extensions::ExtendedAnnotationType")
XSDAnnotation = Class(name="XSDAnnotation")
xpdl_XpdlTypeType = Class(name="xpdl::XpdlTypeType", is_abstract=True)

# xpdl_DeclaredTypeType class attributes and methods
xpdl_DeclaredTypeType_id: Property = Property(name="id", type=StringType)
xpdl_DeclaredTypeType.attributes={xpdl_DeclaredTypeType_id}

# xpdl_SchemaTypeType class attributes and methods

# xpdl_ExternalReferenceType class attributes and methods
xpdl_ExternalReferenceType_location: Property = Property(name="location", type=StringType)
xpdl_ExternalReferenceType_namespace: Property = Property(name="namespace", type=StringType)
xpdl_ExternalReferenceType_xref: Property = Property(name="xref", type=StringType)
xpdl_ExternalReferenceType_m_getSchema: Method = Method(name="getSchema", parameters={}, type=StringType)
xpdl_ExternalReferenceType.attributes={xpdl_ExternalReferenceType_xref, xpdl_ExternalReferenceType_location, xpdl_ExternalReferenceType_namespace}
xpdl_ExternalReferenceType.methods={xpdl_ExternalReferenceType_m_getSchema}

# xpdl_BasicTypeType class attributes and methods
xpdl_BasicTypeType_type: Property = Property(name="type", type=StringType)
xpdl_BasicTypeType.attributes={xpdl_BasicTypeType_type}

# XpdlTypeType class attributes and methods

# xpdl_DataTypeType class attributes and methods
xpdl_DataTypeType_carnotType: Property = Property(name="carnotType", type=StringType)
xpdl_DataTypeType_m_getDataType: Method = Method(name="getDataType", parameters={}, type=XpdlTypeType)
xpdl_DataTypeType.attributes={xpdl_DataTypeType_carnotType}
xpdl_DataTypeType.methods={xpdl_DataTypeType_m_getDataType}

# xpdl_Extensible class attributes and methods

# xpdl_ExternalPackages class attributes and methods
xpdl_ExternalPackages_m_getExternalPackage: Method = Method(name="getExternalPackage", parameters={Parameter(name='packageId')}, type=StringType)
xpdl_ExternalPackages.methods={xpdl_ExternalPackages_m_getExternalPackage}

# xpdl_ExtendedAttributesType class attributes and methods

# xpdl_ExtendedAttributeType class attributes and methods
xpdl_ExtendedAttributeType_name: Property = Property(name="name", type=StringType)
xpdl_ExtendedAttributeType_value: Property = Property(name="value", type=StringType)
xpdl_ExtendedAttributeType_mixed: Property = Property(name="mixed", type=StringType)
xpdl_ExtendedAttributeType_group: Property = Property(name="group", type=StringType)
xpdl_ExtendedAttributeType_any: Property = Property(name="any", type=StringType)
xpdl_ExtendedAttributeType.attributes={xpdl_ExtendedAttributeType_name, xpdl_ExtendedAttributeType_any, xpdl_ExtendedAttributeType_group, xpdl_ExtendedAttributeType_value, xpdl_ExtendedAttributeType_mixed}

# ExtendedAnnotationType class attributes and methods

# xpdl_FormalParameterType class attributes and methods
xpdl_FormalParameterType_description: Property = Property(name="description", type=StringType)
xpdl_FormalParameterType_id: Property = Property(name="id", type=StringType)
xpdl_FormalParameterType_mode: Property = Property(name="mode", type=StringType)
xpdl_FormalParameterType_name: Property = Property(name="name", type=StringType)
xpdl_FormalParameterType.attributes={xpdl_FormalParameterType_mode, xpdl_FormalParameterType_name, xpdl_FormalParameterType_description, xpdl_FormalParameterType_id}

# xpdl_ExternalPackage class attributes and methods
xpdl_ExternalPackage_href: Property = Property(name="href", type=StringType)
xpdl_ExternalPackage_id: Property = Property(name="id", type=StringType)
xpdl_ExternalPackage_name: Property = Property(name="name", type=StringType)
xpdl_ExternalPackage.attributes={xpdl_ExternalPackage_name, xpdl_ExternalPackage_id, xpdl_ExternalPackage_href}

# Extensible class attributes and methods

# xpdl_FormalParametersType class attributes and methods
xpdl_FormalParametersType_m_addFormalParameter: Method = Method(name="addFormalParameter", parameters={Parameter(name='parameter')})
xpdl_FormalParametersType_m_getFormalParameter: Method = Method(name="getFormalParameter", parameters={Parameter(name='parameterId')}, type=StringType)
xpdl_FormalParametersType.methods={xpdl_FormalParametersType_m_getFormalParameter, xpdl_FormalParametersType_m_addFormalParameter}

# xpdl_XSDSchema class attributes and methods

# xpdl_ScriptType class attributes and methods
xpdl_ScriptType_grammar: Property = Property(name="grammar", type=StringType)
xpdl_ScriptType_type: Property = Property(name="type", type=StringType)
xpdl_ScriptType_version: Property = Property(name="version", type=StringType)
xpdl_ScriptType.attributes={xpdl_ScriptType_version, xpdl_ScriptType_type, xpdl_ScriptType_grammar}

# xpdl_TypeDeclarationsType class attributes and methods
xpdl_TypeDeclarationsType_m_getTypeDeclaration: Method = Method(name="getTypeDeclaration", parameters={Parameter(name='typeId')}, type=StringType)
xpdl_TypeDeclarationsType.methods={xpdl_TypeDeclarationsType_m_getTypeDeclaration}

# xpdl_TypeDeclarationType class attributes and methods
xpdl_TypeDeclarationType_description: Property = Property(name="description", type=StringType)
xpdl_TypeDeclarationType_id: Property = Property(name="id", type=StringType)
xpdl_TypeDeclarationType_name: Property = Property(name="name", type=StringType)
xpdl_TypeDeclarationType_m_getDataType: Method = Method(name="getDataType", parameters={}, type=XpdlTypeType)
xpdl_TypeDeclarationType_m_getSchema: Method = Method(name="getSchema", parameters={}, type=StringType)
xpdl_TypeDeclarationType.attributes={xpdl_TypeDeclarationType_name, xpdl_TypeDeclarationType_id, xpdl_TypeDeclarationType_description}
xpdl_TypeDeclarationType.methods={xpdl_TypeDeclarationType_m_getSchema, xpdl_TypeDeclarationType_m_getDataType}

# xpdl_extensions_ExtendedAnnotationType class attributes and methods

# XSDAnnotation class attributes and methods

# xpdl_XpdlTypeType class attributes and methods

# Relationships
declaredType1: BinaryAssociation = BinaryAssociation(
    name="declaredType1",
    ends={
        Property(name="xpdl_DeclaredTypeType", type=xpdl_DataTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl_DataTypeType2", type=xpdl_DeclaredTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schemaType3: BinaryAssociation = BinaryAssociation(
    name="schemaType3",
    ends={
        Property(name="xpdl_SchemaTypeType", type=xpdl_DataTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl_DataTypeType4", type=xpdl_SchemaTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
externalReference5: BinaryAssociation = BinaryAssociation(
    name="externalReference5",
    ends={
        Property(name="xpdl_ExternalReferenceType", type=xpdl_DataTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl_DataTypeType6", type=xpdl_ExternalReferenceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
basicType0: BinaryAssociation = BinaryAssociation(
    name="basicType0",
    ends={
        Property(name="xpdl_BasicTypeType", type=xpdl_DataTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl_DataTypeType", type=xpdl_BasicTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedAttributes10: BinaryAssociation = BinaryAssociation(
    name="extendedAttributes10",
    ends={
        Property(name="xpdl_ExtendedAttributesType11", type=xpdl_Extensible, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl_Extensible", type=xpdl_ExtendedAttributesType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedAttribute7: BinaryAssociation = BinaryAssociation(
    name="extendedAttribute7",
    ends={
        Property(name="xpdl_ExtendedAttributeType", type=xpdl_ExtendedAttributesType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl_ExtendedAttributesType", type=xpdl_ExtendedAttributeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendedAnnotation8: BinaryAssociation = BinaryAssociation(
    name="extendedAnnotation8",
    ends={
        Property(name="ExtendedAnnotationType", type=xpdl_ExtendedAttributeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl_ExtendedAttributeType9", type=ExtendedAnnotationType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameter13: BinaryAssociation = BinaryAssociation(
    name="formalParameter13",
    ends={
        Property(name="xpdl_FormalParameterType", type=xpdl_FormalParametersType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl_FormalParametersType", type=xpdl_FormalParameterType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataType14: BinaryAssociation = BinaryAssociation(
    name="dataType14",
    ends={
        Property(name="xpdl_DataTypeType16", type=xpdl_FormalParameterType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl_FormalParameterType15", type=xpdl_DataTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
externalPackage12: BinaryAssociation = BinaryAssociation(
    name="externalPackage12",
    ends={
        Property(name="xpdl_ExternalPackage", type=xpdl_ExternalPackages, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl_ExternalPackages", type=xpdl_ExternalPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeDeclaration19: BinaryAssociation = BinaryAssociation(
    name="typeDeclaration19",
    ends={
        Property(name="xpdl_TypeDeclarationsType", type=xpdl_TypeDeclarationType, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="xpdl_TypeDeclarationType", type=xpdl_TypeDeclarationsType, multiplicity=Multiplicity(1, 1))
    }
)
basicType20: BinaryAssociation = BinaryAssociation(
    name="basicType20",
    ends={
        Property(name="xpdl_BasicTypeType22", type=xpdl_TypeDeclarationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl_TypeDeclarationType21", type=xpdl_BasicTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaredType23: BinaryAssociation = BinaryAssociation(
    name="declaredType23",
    ends={
        Property(name="xpdl_DeclaredTypeType25", type=xpdl_TypeDeclarationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl_TypeDeclarationType24", type=xpdl_DeclaredTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schemaType26: BinaryAssociation = BinaryAssociation(
    name="schemaType26",
    ends={
        Property(name="xpdl_SchemaTypeType28", type=xpdl_TypeDeclarationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl_TypeDeclarationType27", type=xpdl_SchemaTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schema17: BinaryAssociation = BinaryAssociation(
    name="schema17",
    ends={
        Property(name="xpdl_XSDSchema", type=xpdl_SchemaTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl_SchemaTypeType18", type=xpdl_XSDSchema, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
externalReference29: BinaryAssociation = BinaryAssociation(
    name="externalReference29",
    ends={
        Property(name="xpdl_ExternalReferenceType31", type=xpdl_TypeDeclarationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl_TypeDeclarationType30", type=xpdl_ExternalReferenceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_xpdl_BasicTypeType_XpdlTypeType = Generalization(general=XpdlTypeType, specific=xpdl_BasicTypeType)
gen_xpdl_DeclaredTypeType_XpdlTypeType = Generalization(general=XpdlTypeType, specific=xpdl_DeclaredTypeType)
gen_xpdl_ExternalPackage_Extensible = Generalization(general=Extensible, specific=xpdl_ExternalPackage)
gen_xpdl_ExternalReferenceType_XpdlTypeType = Generalization(general=XpdlTypeType, specific=xpdl_ExternalReferenceType)
gen_xpdl_TypeDeclarationType_Extensible = Generalization(general=Extensible, specific=xpdl_TypeDeclarationType)
gen_xpdl_SchemaTypeType_XpdlTypeType = Generalization(general=XpdlTypeType, specific=xpdl_SchemaTypeType)
gen_xpdl_extensions_ExtendedAnnotationType_XSDAnnotation = Generalization(general=XSDAnnotation, specific=xpdl_extensions_ExtendedAnnotationType)

# Domain Model
domain_model = DomainModel(
    name="xpdl",
    types={xpdl_DeclaredTypeType, xpdl_SchemaTypeType, xpdl_ExternalReferenceType, xpdl_BasicTypeType, XpdlTypeType, xpdl_DataTypeType, xpdl_Extensible, xpdl_ExternalPackages, xpdl_ExtendedAttributesType, xpdl_ExtendedAttributeType, ExtendedAnnotationType, xpdl_FormalParameterType, xpdl_ExternalPackage, Extensible, xpdl_FormalParametersType, xpdl_XSDSchema, xpdl_ScriptType, xpdl_TypeDeclarationsType, xpdl_TypeDeclarationType, xpdl_extensions_ExtendedAnnotationType, XSDAnnotation, xpdl_XpdlTypeType, ModeType, TypeType},
    associations={declaredType1, schemaType3, externalReference5, basicType0, extendedAttributes10, extendedAttribute7, extendedAnnotation8, formalParameter13, dataType14, externalPackage12, typeDeclaration19, basicType20, declaredType23, schemaType26, schema17, externalReference29},
    generalizations={gen_xpdl_BasicTypeType_XpdlTypeType, gen_xpdl_DeclaredTypeType_XpdlTypeType, gen_xpdl_ExternalPackage_Extensible, gen_xpdl_ExternalReferenceType_XpdlTypeType, gen_xpdl_TypeDeclarationType_Extensible, gen_xpdl_SchemaTypeType_XpdlTypeType, gen_xpdl_extensions_ExtendedAnnotationType_XSDAnnotation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)