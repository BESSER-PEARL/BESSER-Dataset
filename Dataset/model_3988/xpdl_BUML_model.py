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
MIOrderingType: Enumeration = Enumeration(
    name="MIOrderingType",
    literals={
            EnumerationLiteral(name="Sequential"),
			EnumerationLiteral(name="Parallel")
    }
)

ModeType: Enumeration = Enumeration(
    name="ModeType",
    literals={
            EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="OUT"),
			EnumerationLiteral(name="INOUT")
    }
)

TestTimeType: Enumeration = Enumeration(
    name="TestTimeType",
    literals={
            EnumerationLiteral(name="Before"),
			EnumerationLiteral(name="After")
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

LoopTypeType: Enumeration = Enumeration(
    name="LoopTypeType",
    literals={
            EnumerationLiteral(name="Standard"),
			EnumerationLiteral(name="MultiInstance")
    }
)

MIFlowConditionType: Enumeration = Enumeration(
    name="MIFlowConditionType",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="One"),
			EnumerationLiteral(name="All"),
			EnumerationLiteral(name="Complex")
    }
)

# Classes
xpdl2_BasicTypeType = Class(name="xpdl2::BasicTypeType")
XpdlTypeType = Class(name="XpdlTypeType")
xpdl2_DataTypeType = Class(name="xpdl2::DataTypeType")
xpdl2_DeclaredTypeType = Class(name="xpdl2::DeclaredTypeType")
xpdl2_SchemaTypeType = Class(name="xpdl2::SchemaTypeType")
xpdl2_ExternalReferenceType = Class(name="xpdl2::ExternalReferenceType")
xpdl2_ExtendedAttributesType = Class(name="xpdl2::ExtendedAttributesType")
xpdl2_ExtendedAttributeType = Class(name="xpdl2::ExtendedAttributeType")
ExtendedAnnotationType = Class(name="ExtendedAnnotationType")
xpdl2_ExpressionType = Class(name="xpdl2::ExpressionType")
xpdl2_FormalParametersType = Class(name="xpdl2::FormalParametersType")
xpdl2_FormalParameterType = Class(name="xpdl2::FormalParameterType")
xpdl2_Extensible = Class(name="xpdl2::Extensible", is_abstract=True)
xpdl2_ExternalPackages = Class(name="xpdl2::ExternalPackages")
xpdl2_ExternalPackage = Class(name="xpdl2::ExternalPackage")
Extensible = Class(name="Extensible")
LoopDataRefType = Class(name="LoopDataRefType")
xpdl2_LoopStandardType = Class(name="xpdl2::LoopStandardType")
xpdl2_LoopType = Class(name="xpdl2::LoopType")
xpdl2_LoopMultiInstanceType = Class(name="xpdl2::LoopMultiInstanceType")
xpdl2_TypeDeclarationsType = Class(name="xpdl2::TypeDeclarationsType")
xpdl2_TypeDeclarationType = Class(name="xpdl2::TypeDeclarationType")
xpdl2_XSDSchema = Class(name="xpdl2::XSDSchema")
xpdl2_ScriptType = Class(name="xpdl2::ScriptType")
xpdl2_XpdlTypeType = Class(name="xpdl2::XpdlTypeType", is_abstract=True)
xpdl2_extensions_ExtendedAnnotationType = Class(name="xpdl2::extensions::ExtendedAnnotationType")
XSDAnnotation = Class(name="XSDAnnotation")
xpdl2_extensions_LoopDataRefType = Class(name="xpdl2::extensions::LoopDataRefType")

# xpdl2_BasicTypeType class attributes and methods
xpdl2_BasicTypeType_type: Property = Property(name="type", type=StringType)
xpdl2_BasicTypeType.attributes={xpdl2_BasicTypeType_type}

# XpdlTypeType class attributes and methods

# xpdl2_DataTypeType class attributes and methods
xpdl2_DataTypeType_carnotType: Property = Property(name="carnotType", type=StringType)
xpdl2_DataTypeType_m_getDataType: Method = Method(name="getDataType", parameters={}, type=XpdlTypeType)
xpdl2_DataTypeType.attributes={xpdl2_DataTypeType_carnotType}
xpdl2_DataTypeType.methods={xpdl2_DataTypeType_m_getDataType}

# xpdl2_DeclaredTypeType class attributes and methods
xpdl2_DeclaredTypeType_id: Property = Property(name="id", type=StringType)
xpdl2_DeclaredTypeType.attributes={xpdl2_DeclaredTypeType_id}

# xpdl2_SchemaTypeType class attributes and methods

# xpdl2_ExternalReferenceType class attributes and methods
xpdl2_ExternalReferenceType_location: Property = Property(name="location", type=StringType)
xpdl2_ExternalReferenceType_namespace: Property = Property(name="namespace", type=StringType)
xpdl2_ExternalReferenceType_xref: Property = Property(name="xref", type=StringType)
xpdl2_ExternalReferenceType_uuid: Property = Property(name="uuid", type=StringType)
xpdl2_ExternalReferenceType_m_getSchema: Method = Method(name="getSchema", parameters={}, type=StringType)
xpdl2_ExternalReferenceType.attributes={xpdl2_ExternalReferenceType_uuid, xpdl2_ExternalReferenceType_namespace, xpdl2_ExternalReferenceType_xref, xpdl2_ExternalReferenceType_location}
xpdl2_ExternalReferenceType.methods={xpdl2_ExternalReferenceType_m_getSchema}

# xpdl2_ExtendedAttributesType class attributes and methods

# xpdl2_ExtendedAttributeType class attributes and methods
xpdl2_ExtendedAttributeType_mixed: Property = Property(name="mixed", type=StringType)
xpdl2_ExtendedAttributeType_group: Property = Property(name="group", type=StringType)
xpdl2_ExtendedAttributeType_any: Property = Property(name="any", type=StringType)
xpdl2_ExtendedAttributeType_name: Property = Property(name="name", type=StringType)
xpdl2_ExtendedAttributeType_value: Property = Property(name="value", type=StringType)
xpdl2_ExtendedAttributeType.attributes={xpdl2_ExtendedAttributeType_name, xpdl2_ExtendedAttributeType_value, xpdl2_ExtendedAttributeType_mixed, xpdl2_ExtendedAttributeType_group, xpdl2_ExtendedAttributeType_any}

# ExtendedAnnotationType class attributes and methods

# xpdl2_ExpressionType class attributes and methods
xpdl2_ExpressionType_scriptGrammar: Property = Property(name="scriptGrammar", type=StringType)
xpdl2_ExpressionType_scriptType: Property = Property(name="scriptType", type=StringType)
xpdl2_ExpressionType_scriptVersion: Property = Property(name="scriptVersion", type=StringType)
xpdl2_ExpressionType_mixed: Property = Property(name="mixed", type=StringType)
xpdl2_ExpressionType_group: Property = Property(name="group", type=StringType)
xpdl2_ExpressionType_any: Property = Property(name="any", type=StringType)
xpdl2_ExpressionType.attributes={xpdl2_ExpressionType_scriptType, xpdl2_ExpressionType_group, xpdl2_ExpressionType_mixed, xpdl2_ExpressionType_scriptVersion, xpdl2_ExpressionType_scriptGrammar, xpdl2_ExpressionType_any}

# xpdl2_FormalParametersType class attributes and methods
xpdl2_FormalParametersType_m_addFormalParameter: Method = Method(name="addFormalParameter", parameters={Parameter(name='parameter')})
xpdl2_FormalParametersType_m_getFormalParameter: Method = Method(name="getFormalParameter", parameters={Parameter(name='parameterId')}, type=StringType)
xpdl2_FormalParametersType.methods={xpdl2_FormalParametersType_m_addFormalParameter, xpdl2_FormalParametersType_m_getFormalParameter}

# xpdl2_FormalParameterType class attributes and methods
xpdl2_FormalParameterType_description: Property = Property(name="description", type=StringType)
xpdl2_FormalParameterType_id: Property = Property(name="id", type=StringType)
xpdl2_FormalParameterType_mode: Property = Property(name="mode", type=StringType)
xpdl2_FormalParameterType_name: Property = Property(name="name", type=StringType)
xpdl2_FormalParameterType.attributes={xpdl2_FormalParameterType_name, xpdl2_FormalParameterType_description, xpdl2_FormalParameterType_id, xpdl2_FormalParameterType_mode}

# xpdl2_Extensible class attributes and methods

# xpdl2_ExternalPackages class attributes and methods
xpdl2_ExternalPackages_m_getExternalPackage: Method = Method(name="getExternalPackage", parameters={Parameter(name='packageId')}, type=StringType)
xpdl2_ExternalPackages.methods={xpdl2_ExternalPackages_m_getExternalPackage}

# xpdl2_ExternalPackage class attributes and methods
xpdl2_ExternalPackage_href: Property = Property(name="href", type=StringType)
xpdl2_ExternalPackage_id: Property = Property(name="id", type=StringType)
xpdl2_ExternalPackage_name: Property = Property(name="name", type=StringType)
xpdl2_ExternalPackage.attributes={xpdl2_ExternalPackage_href, xpdl2_ExternalPackage_id, xpdl2_ExternalPackage_name}

# Extensible class attributes and methods

# LoopDataRefType class attributes and methods

# xpdl2_LoopStandardType class attributes and methods
xpdl2_LoopStandardType_loopMaximum: Property = Property(name="loopMaximum", type=StringType)
xpdl2_LoopStandardType_testTime: Property = Property(name="testTime", type=StringType)
xpdl2_LoopStandardType.attributes={xpdl2_LoopStandardType_testTime, xpdl2_LoopStandardType_loopMaximum}

# xpdl2_LoopType class attributes and methods
xpdl2_LoopType_loopType: Property = Property(name="loopType", type=StringType)
xpdl2_LoopType.attributes={xpdl2_LoopType_loopType}

# xpdl2_LoopMultiInstanceType class attributes and methods
xpdl2_LoopMultiInstanceType_mIFlowCondition: Property = Property(name="mIFlowCondition", type=StringType)
xpdl2_LoopMultiInstanceType_mIOrdering: Property = Property(name="mIOrdering", type=StringType)
xpdl2_LoopMultiInstanceType.attributes={xpdl2_LoopMultiInstanceType_mIFlowCondition, xpdl2_LoopMultiInstanceType_mIOrdering}

# xpdl2_TypeDeclarationsType class attributes and methods
xpdl2_TypeDeclarationsType_m_getTypeDeclaration: Method = Method(name="getTypeDeclaration", parameters={Parameter(name='typeId')}, type=StringType)
xpdl2_TypeDeclarationsType.methods={xpdl2_TypeDeclarationsType_m_getTypeDeclaration}

# xpdl2_TypeDeclarationType class attributes and methods
xpdl2_TypeDeclarationType_description: Property = Property(name="description", type=StringType)
xpdl2_TypeDeclarationType_id: Property = Property(name="id", type=StringType)
xpdl2_TypeDeclarationType_name: Property = Property(name="name", type=StringType)
xpdl2_TypeDeclarationType_m_getDataType: Method = Method(name="getDataType", parameters={}, type=XpdlTypeType)
xpdl2_TypeDeclarationType_m_getSchema: Method = Method(name="getSchema", parameters={}, type=StringType)
xpdl2_TypeDeclarationType.attributes={xpdl2_TypeDeclarationType_description, xpdl2_TypeDeclarationType_id, xpdl2_TypeDeclarationType_name}
xpdl2_TypeDeclarationType.methods={xpdl2_TypeDeclarationType_m_getSchema, xpdl2_TypeDeclarationType_m_getDataType}

# xpdl2_XSDSchema class attributes and methods

# xpdl2_ScriptType class attributes and methods
xpdl2_ScriptType_type: Property = Property(name="type", type=StringType)
xpdl2_ScriptType_version: Property = Property(name="version", type=StringType)
xpdl2_ScriptType_grammar: Property = Property(name="grammar", type=StringType)
xpdl2_ScriptType.attributes={xpdl2_ScriptType_version, xpdl2_ScriptType_type, xpdl2_ScriptType_grammar}

# xpdl2_XpdlTypeType class attributes and methods

# xpdl2_extensions_ExtendedAnnotationType class attributes and methods

# XSDAnnotation class attributes and methods

# xpdl2_extensions_LoopDataRefType class attributes and methods
xpdl2_extensions_LoopDataRefType_inputItemRef: Property = Property(name="inputItemRef", type=StringType)
xpdl2_extensions_LoopDataRefType_outputItemRef: Property = Property(name="outputItemRef", type=StringType)
xpdl2_extensions_LoopDataRefType_loopCounterRef: Property = Property(name="loopCounterRef", type=StringType)
xpdl2_extensions_LoopDataRefType.attributes={xpdl2_extensions_LoopDataRefType_outputItemRef, xpdl2_extensions_LoopDataRefType_loopCounterRef, xpdl2_extensions_LoopDataRefType_inputItemRef}

# Relationships
basicType0: BinaryAssociation = BinaryAssociation(
    name="basicType0",
    ends={
        Property(name="xpdl2_BasicTypeType", type=xpdl2_DataTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl2_DataTypeType", type=xpdl2_BasicTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaredType1: BinaryAssociation = BinaryAssociation(
    name="declaredType1",
    ends={
        Property(name="xpdl2_DeclaredTypeType", type=xpdl2_DataTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl2_DataTypeType2", type=xpdl2_DeclaredTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schemaType3: BinaryAssociation = BinaryAssociation(
    name="schemaType3",
    ends={
        Property(name="xpdl2_SchemaTypeType", type=xpdl2_DataTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl2_DataTypeType4", type=xpdl2_SchemaTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
externalReference5: BinaryAssociation = BinaryAssociation(
    name="externalReference5",
    ends={
        Property(name="xpdl2_ExternalReferenceType", type=xpdl2_DataTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl2_DataTypeType6", type=xpdl2_ExternalReferenceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedAttribute7: BinaryAssociation = BinaryAssociation(
    name="extendedAttribute7",
    ends={
        Property(name="xpdl2_ExtendedAttributeType", type=xpdl2_ExtendedAttributesType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl2_ExtendedAttributesType", type=xpdl2_ExtendedAttributeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendedAnnotation8: BinaryAssociation = BinaryAssociation(
    name="extendedAnnotation8",
    ends={
        Property(name="ExtendedAnnotationType", type=xpdl2_ExtendedAttributeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl2_ExtendedAttributeType9", type=ExtendedAnnotationType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameter13: BinaryAssociation = BinaryAssociation(
    name="formalParameter13",
    ends={
        Property(name="xpdl2_FormalParameterType", type=xpdl2_FormalParametersType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl2_FormalParametersType", type=xpdl2_FormalParameterType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extendedAttributes10: BinaryAssociation = BinaryAssociation(
    name="extendedAttributes10",
    ends={
        Property(name="xpdl2_ExtendedAttributesType11", type=xpdl2_Extensible, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl2_Extensible", type=xpdl2_ExtendedAttributesType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
externalPackage12: BinaryAssociation = BinaryAssociation(
    name="externalPackage12",
    ends={
        Property(name="xpdl2_ExternalPackage", type=xpdl2_ExternalPackages, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl2_ExternalPackages", type=xpdl2_ExternalPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mICondition17: BinaryAssociation = BinaryAssociation(
    name="mICondition17",
    ends={
        Property(name="xpdl2_ExpressionType", type=xpdl2_LoopMultiInstanceType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl2_LoopMultiInstanceType", type=xpdl2_ExpressionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
complexMIFlowCondition18: BinaryAssociation = BinaryAssociation(
    name="complexMIFlowCondition18",
    ends={
        Property(name="xpdl2_ExpressionType20", type=xpdl2_LoopMultiInstanceType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl2_LoopMultiInstanceType19", type=xpdl2_ExpressionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loopDataRef21: BinaryAssociation = BinaryAssociation(
    name="loopDataRef21",
    ends={
        Property(name="LoopDataRefType", type=xpdl2_LoopMultiInstanceType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl2_LoopMultiInstanceType22", type=LoopDataRefType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loopCondition23: BinaryAssociation = BinaryAssociation(
    name="loopCondition23",
    ends={
        Property(name="xpdl2_ExpressionType24", type=xpdl2_LoopStandardType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl2_LoopStandardType", type=xpdl2_ExpressionType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dataType14: BinaryAssociation = BinaryAssociation(
    name="dataType14",
    ends={
        Property(name="xpdl2_DataTypeType16", type=xpdl2_FormalParameterType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl2_FormalParameterType15", type=xpdl2_DataTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeDeclaration32: BinaryAssociation = BinaryAssociation(
    name="typeDeclaration32",
    ends={
        Property(name="xpdl2_TypeDeclarationType", type=xpdl2_TypeDeclarationsType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl2_TypeDeclarationsType", type=xpdl2_TypeDeclarationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
basicType33: BinaryAssociation = BinaryAssociation(
    name="basicType33",
    ends={
        Property(name="xpdl2_BasicTypeType35", type=xpdl2_TypeDeclarationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl2_TypeDeclarationType34", type=xpdl2_BasicTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaredType36: BinaryAssociation = BinaryAssociation(
    name="declaredType36",
    ends={
        Property(name="xpdl2_DeclaredTypeType38", type=xpdl2_TypeDeclarationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl2_TypeDeclarationType37", type=xpdl2_DeclaredTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schemaType39: BinaryAssociation = BinaryAssociation(
    name="schemaType39",
    ends={
        Property(name="xpdl2_SchemaTypeType41", type=xpdl2_TypeDeclarationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl2_TypeDeclarationType40", type=xpdl2_SchemaTypeType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loopStandard25: BinaryAssociation = BinaryAssociation(
    name="loopStandard25",
    ends={
        Property(name="xpdl2_LoopStandardType26", type=xpdl2_LoopType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl2_LoopType", type=xpdl2_LoopStandardType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loopMultiInstance27: BinaryAssociation = BinaryAssociation(
    name="loopMultiInstance27",
    ends={
        Property(name="xpdl2_LoopMultiInstanceType29", type=xpdl2_LoopType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl2_LoopType28", type=xpdl2_LoopMultiInstanceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schema30: BinaryAssociation = BinaryAssociation(
    name="schema30",
    ends={
        Property(name="xpdl2_XSDSchema", type=xpdl2_SchemaTypeType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl2_SchemaTypeType31", type=xpdl2_XSDSchema, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
externalReference42: BinaryAssociation = BinaryAssociation(
    name="externalReference42",
    ends={
        Property(name="xpdl2_ExternalReferenceType44", type=xpdl2_TypeDeclarationType, multiplicity=Multiplicity(1, 1)),
        Property(name="xpdl2_TypeDeclarationType43", type=xpdl2_ExternalReferenceType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_xpdl2_BasicTypeType_XpdlTypeType = Generalization(general=XpdlTypeType, specific=xpdl2_BasicTypeType)
gen_xpdl2_DeclaredTypeType_XpdlTypeType = Generalization(general=XpdlTypeType, specific=xpdl2_DeclaredTypeType)
gen_xpdl2_ExternalReferenceType_XpdlTypeType = Generalization(general=XpdlTypeType, specific=xpdl2_ExternalReferenceType)
gen_xpdl2_ExternalPackage_Extensible = Generalization(general=Extensible, specific=xpdl2_ExternalPackage)
gen_xpdl2_TypeDeclarationType_Extensible = Generalization(general=Extensible, specific=xpdl2_TypeDeclarationType)
gen_xpdl2_SchemaTypeType_XpdlTypeType = Generalization(general=XpdlTypeType, specific=xpdl2_SchemaTypeType)
gen_xpdl2_extensions_ExtendedAnnotationType_XSDAnnotation = Generalization(general=XSDAnnotation, specific=xpdl2_extensions_ExtendedAnnotationType)

# Domain Model
domain_model = DomainModel(
    name="xpdl2",
    types={xpdl2_BasicTypeType, XpdlTypeType, xpdl2_DataTypeType, xpdl2_DeclaredTypeType, xpdl2_SchemaTypeType, xpdl2_ExternalReferenceType, xpdl2_ExtendedAttributesType, xpdl2_ExtendedAttributeType, ExtendedAnnotationType, xpdl2_ExpressionType, xpdl2_FormalParametersType, xpdl2_FormalParameterType, xpdl2_Extensible, xpdl2_ExternalPackages, xpdl2_ExternalPackage, Extensible, LoopDataRefType, xpdl2_LoopStandardType, xpdl2_LoopType, xpdl2_LoopMultiInstanceType, xpdl2_TypeDeclarationsType, xpdl2_TypeDeclarationType, xpdl2_XSDSchema, xpdl2_ScriptType, xpdl2_XpdlTypeType, xpdl2_extensions_ExtendedAnnotationType, XSDAnnotation, xpdl2_extensions_LoopDataRefType, MIOrderingType, ModeType, TestTimeType, TypeType, LoopTypeType, MIFlowConditionType},
    associations={basicType0, declaredType1, schemaType3, externalReference5, extendedAttribute7, extendedAnnotation8, formalParameter13, extendedAttributes10, externalPackage12, mICondition17, complexMIFlowCondition18, loopDataRef21, loopCondition23, dataType14, typeDeclaration32, basicType33, declaredType36, schemaType39, loopStandard25, loopMultiInstance27, schema30, externalReference42},
    generalizations={gen_xpdl2_BasicTypeType_XpdlTypeType, gen_xpdl2_DeclaredTypeType_XpdlTypeType, gen_xpdl2_ExternalReferenceType_XpdlTypeType, gen_xpdl2_ExternalPackage_Extensible, gen_xpdl2_TypeDeclarationType_Extensible, gen_xpdl2_SchemaTypeType_XpdlTypeType, gen_xpdl2_extensions_ExtendedAnnotationType_XSDAnnotation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)