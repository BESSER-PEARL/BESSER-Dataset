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
JvmVisibility: Enumeration = Enumeration(
    name="JvmVisibility",
    literals={
            EnumerationLiteral(name="DEFAULT"),
			EnumerationLiteral(name="PRIVATE"),
			EnumerationLiteral(name="PROTECTED"),
			EnumerationLiteral(name="PUBLIC")
    }
)

# Classes
types_JvmType = Class(name="types::JvmType", is_abstract=True)
JvmIdentifiableElement = Class(name="JvmIdentifiableElement")
types_JvmVoid = Class(name="types::JvmVoid")
JvmType = Class(name="JvmType")
types_JvmComponentType = Class(name="types::JvmComponentType", is_abstract=True)
types_JvmArrayType = Class(name="types::JvmArrayType")
types_JvmIdentifiableElement = Class(name="types::JvmIdentifiableElement", is_abstract=True)
types_JvmTypeReference = Class(name="types::JvmTypeReference", is_abstract=True)
types_JvmPrimitiveType = Class(name="types::JvmPrimitiveType")
JvmComponentType = Class(name="JvmComponentType")
types_JvmDeclaredType = Class(name="types::JvmDeclaredType", is_abstract=True)
JvmMember = Class(name="JvmMember")
types_JvmUpperBound = Class(name="types::JvmUpperBound")
JvmTypeConstraint = Class(name="JvmTypeConstraint")
types_JvmLowerBound = Class(name="types::JvmLowerBound")
types_JvmAnnotationType = Class(name="types::JvmAnnotationType")
JvmDeclaredType = Class(name="JvmDeclaredType")
types_JvmEnumerationType = Class(name="types::JvmEnumerationType")
types_JvmEnumerationLiteral = Class(name="types::JvmEnumerationLiteral")
JvmField = Class(name="JvmField")
types_JvmGenericType = Class(name="types::JvmGenericType")
JvmTypeParameterDeclarator = Class(name="JvmTypeParameterDeclarator")
types_JvmMember = Class(name="types::JvmMember", is_abstract=True)
types_JvmTypeParameter = Class(name="types::JvmTypeParameter")
JvmConstraintOwner = Class(name="JvmConstraintOwner")
types_JvmTypeParameterDeclarator = Class(name="types::JvmTypeParameterDeclarator", is_abstract=True)
types_JvmConstraintOwner = Class(name="types::JvmConstraintOwner", is_abstract=True)
types_JvmTypeConstraint = Class(name="types::JvmTypeConstraint", is_abstract=True)
types_JvmWildcardTypeReference = Class(name="types::JvmWildcardTypeReference")
types_JvmAnyTypeReference = Class(name="types::JvmAnyTypeReference")
types_JvmMultiTypeReference = Class(name="types::JvmMultiTypeReference")
JvmCompoundTypeReference = Class(name="JvmCompoundTypeReference")
JvmAnnotationTarget = Class(name="JvmAnnotationTarget")
types_JvmParameterizedTypeReference = Class(name="types::JvmParameterizedTypeReference")
JvmTypeReference = Class(name="JvmTypeReference")
types_JvmGenericArrayTypeReference = Class(name="types::JvmGenericArrayTypeReference")
types_JvmExecutable = Class(name="types::JvmExecutable", is_abstract=True)
types_JvmFormalParameter = Class(name="types::JvmFormalParameter")
types_JvmConstructor = Class(name="types::JvmConstructor")
JvmExecutable = Class(name="JvmExecutable")
types_JvmOperation = Class(name="types::JvmOperation")
types_JvmFeature = Class(name="types::JvmFeature", is_abstract=True)
types_JvmField = Class(name="types::JvmField")
JvmFeature = Class(name="JvmFeature")
types_JvmIntAnnotationValue = Class(name="types::JvmIntAnnotationValue")
JvmAnnotationValue = Class(name="JvmAnnotationValue")
types_JvmBooleanAnnotationValue = Class(name="types::JvmBooleanAnnotationValue")
types_JvmByteAnnotationValue = Class(name="types::JvmByteAnnotationValue")
types_JvmShortAnnotationValue = Class(name="types::JvmShortAnnotationValue")
types_JvmAnnotationValue = Class(name="types::JvmAnnotationValue", is_abstract=True)
types_JvmAnnotationTarget = Class(name="types::JvmAnnotationTarget", is_abstract=True)
types_JvmAnnotationReference = Class(name="types::JvmAnnotationReference")
types_JvmDelegateTypeReference = Class(name="types::JvmDelegateTypeReference")
types_JvmSpecializedTypeReference = Class(name="types::JvmSpecializedTypeReference", is_abstract=True)
types_JvmSynonymTypeReference = Class(name="types::JvmSynonymTypeReference")
types_JvmUnknownTypeReference = Class(name="types::JvmUnknownTypeReference")
types_JvmCompoundTypeReference = Class(name="types::JvmCompoundTypeReference", is_abstract=True)
types_JvmLongAnnotationValue = Class(name="types::JvmLongAnnotationValue")
types_JvmDoubleAnnotationValue = Class(name="types::JvmDoubleAnnotationValue")
types_JvmFloatAnnotationValue = Class(name="types::JvmFloatAnnotationValue")
types_JvmCharAnnotationValue = Class(name="types::JvmCharAnnotationValue")
types_JvmStringAnnotationValue = Class(name="types::JvmStringAnnotationValue")
types_JvmTypeAnnotationValue = Class(name="types::JvmTypeAnnotationValue")
types_JvmAnnotationAnnotationValue = Class(name="types::JvmAnnotationAnnotationValue")
types_JvmEnumAnnotationValue = Class(name="types::JvmEnumAnnotationValue")
types_JvmCustomAnnotationValue = Class(name="types::JvmCustomAnnotationValue")
types_EObject = Class(name="types::EObject")
types_JvmInnerTypeReference = Class(name="types::JvmInnerTypeReference")
JvmParameterizedTypeReference = Class(name="JvmParameterizedTypeReference")

# types_JvmType class attributes and methods

# JvmIdentifiableElement class attributes and methods

# types_JvmVoid class attributes and methods

# JvmType class attributes and methods

# types_JvmComponentType class attributes and methods

# types_JvmArrayType class attributes and methods
types_JvmArrayType_m_getDimensions: Method = Method(name="getDimensions", parameters={}, type=IntegerType)
types_JvmArrayType.methods={types_JvmArrayType_m_getDimensions}

# types_JvmIdentifiableElement class attributes and methods
types_JvmIdentifiableElement_m_getSimpleName: Method = Method(name="getSimpleName", parameters={}, type=StringType)
types_JvmIdentifiableElement_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={}, type=StringType)
types_JvmIdentifiableElement_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={Parameter(name='innerClassDelimiter')}, type=StringType)
types_JvmIdentifiableElement_m_getIdentifier: Method = Method(name="getIdentifier", parameters={}, type=StringType)
types_JvmIdentifiableElement.methods={types_JvmIdentifiableElement_m_getSimpleName, types_JvmIdentifiableElement_m_getQualifiedName, types_JvmIdentifiableElement_m_getQualifiedName, types_JvmIdentifiableElement_m_getIdentifier}

# types_JvmTypeReference class attributes and methods
types_JvmTypeReference_m_getType: Method = Method(name="getType", parameters={}, type=JvmType)
types_JvmTypeReference_m_getIdentifier: Method = Method(name="getIdentifier", parameters={}, type=StringType)
types_JvmTypeReference_m_getSimpleName: Method = Method(name="getSimpleName", parameters={}, type=StringType)
types_JvmTypeReference_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={}, type=StringType)
types_JvmTypeReference_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={Parameter(name='innerClassDelimiter')}, type=StringType)
types_JvmTypeReference_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor')})
types_JvmTypeReference_m_accept: Method = Method(name="accept", parameters={Parameter(name='visitor'), Parameter(name='parameter')})
types_JvmTypeReference.methods={types_JvmTypeReference_m_getQualifiedName, types_JvmTypeReference_m_getType, types_JvmTypeReference_m_accept, types_JvmTypeReference_m_getIdentifier, types_JvmTypeReference_m_getQualifiedName, types_JvmTypeReference_m_getSimpleName, types_JvmTypeReference_m_accept}

# types_JvmPrimitiveType class attributes and methods
types_JvmPrimitiveType_simpleName: Property = Property(name="simpleName", type=StringType)
types_JvmPrimitiveType.attributes={types_JvmPrimitiveType_simpleName}

# JvmComponentType class attributes and methods

# types_JvmDeclaredType class attributes and methods
types_JvmDeclaredType_abstract: Property = Property(name="abstract", type=BooleanType)
types_JvmDeclaredType_static: Property = Property(name="static", type=BooleanType)
types_JvmDeclaredType_final: Property = Property(name="final", type=BooleanType)
types_JvmDeclaredType_packageName: Property = Property(name="packageName", type=StringType)
types_JvmDeclaredType_m_getAllFeatures: Method = Method(name="getAllFeatures", parameters={})
types_JvmDeclaredType_m_getExtendedInterfaces: Method = Method(name="getExtendedInterfaces", parameters={})
types_JvmDeclaredType_m_getExtendedClass: Method = Method(name="getExtendedClass", parameters={}, type=StringType)
types_JvmDeclaredType_m_isInstantiateable: Method = Method(name="isInstantiateable", parameters={}, type=BooleanType)
types_JvmDeclaredType_m_findAllNestedTypesByName: Method = Method(name="findAllNestedTypesByName", parameters={Parameter(name='simpleName')})
types_JvmDeclaredType_m_isLocal: Method = Method(name="isLocal", parameters={}, type=BooleanType)
types_JvmDeclaredType_m_getDeclaredConstructors: Method = Method(name="getDeclaredConstructors", parameters={})
types_JvmDeclaredType_m_getAllNestedTypes: Method = Method(name="getAllNestedTypes", parameters={})
types_JvmDeclaredType_m_getDeclaredOperations: Method = Method(name="getDeclaredOperations", parameters={})
types_JvmDeclaredType_m_getDeclaredFields: Method = Method(name="getDeclaredFields", parameters={})
types_JvmDeclaredType_m_findAllFeaturesByName: Method = Method(name="findAllFeaturesByName", parameters={Parameter(name='simpleName')})
types_JvmDeclaredType.attributes={types_JvmDeclaredType_packageName, types_JvmDeclaredType_abstract, types_JvmDeclaredType_final, types_JvmDeclaredType_static}
types_JvmDeclaredType.methods={types_JvmDeclaredType_m_isInstantiateable, types_JvmDeclaredType_m_findAllFeaturesByName, types_JvmDeclaredType_m_getDeclaredFields, types_JvmDeclaredType_m_getDeclaredOperations, types_JvmDeclaredType_m_getDeclaredConstructors, types_JvmDeclaredType_m_getAllNestedTypes, types_JvmDeclaredType_m_getExtendedInterfaces, types_JvmDeclaredType_m_getExtendedClass, types_JvmDeclaredType_m_findAllNestedTypesByName, types_JvmDeclaredType_m_getAllFeatures, types_JvmDeclaredType_m_isLocal}

# JvmMember class attributes and methods

# types_JvmUpperBound class attributes and methods

# JvmTypeConstraint class attributes and methods

# types_JvmLowerBound class attributes and methods

# types_JvmAnnotationType class attributes and methods

# JvmDeclaredType class attributes and methods

# types_JvmEnumerationType class attributes and methods

# types_JvmEnumerationLiteral class attributes and methods
types_JvmEnumerationLiteral_m_getEnumType: Method = Method(name="getEnumType", parameters={}, type=StringType)
types_JvmEnumerationLiteral.methods={types_JvmEnumerationLiteral_m_getEnumType}

# JvmField class attributes and methods

# types_JvmGenericType class attributes and methods
types_JvmGenericType_interface: Property = Property(name="interface", type=BooleanType)
types_JvmGenericType_strictFloatingPoint: Property = Property(name="strictFloatingPoint", type=BooleanType)
types_JvmGenericType_anonymous: Property = Property(name="anonymous", type=BooleanType)
types_JvmGenericType.attributes={types_JvmGenericType_interface, types_JvmGenericType_strictFloatingPoint, types_JvmGenericType_anonymous}

# JvmTypeParameterDeclarator class attributes and methods

# types_JvmMember class attributes and methods
types_JvmMember_visibility: Property = Property(name="visibility", type=StringType)
types_JvmMember_simpleName: Property = Property(name="simpleName", type=StringType)
types_JvmMember_identifier: Property = Property(name="identifier", type=StringType)
types_JvmMember_deprecated: Property = Property(name="deprecated", type=BooleanType)
types_JvmMember_m_internalSetIdentifier: Method = Method(name="internalSetIdentifier", parameters={Parameter(name='identifier')})
types_JvmMember.attributes={types_JvmMember_visibility, types_JvmMember_simpleName, types_JvmMember_identifier, types_JvmMember_deprecated}
types_JvmMember.methods={types_JvmMember_m_internalSetIdentifier}

# types_JvmTypeParameter class attributes and methods
types_JvmTypeParameter_name: Property = Property(name="name", type=StringType)
types_JvmTypeParameter.attributes={types_JvmTypeParameter_name}

# JvmConstraintOwner class attributes and methods

# types_JvmTypeParameterDeclarator class attributes and methods

# types_JvmConstraintOwner class attributes and methods

# types_JvmTypeConstraint class attributes and methods
types_JvmTypeConstraint_m_getIdentifier: Method = Method(name="getIdentifier", parameters={}, type=StringType)
types_JvmTypeConstraint_m_getSimpleName: Method = Method(name="getSimpleName", parameters={}, type=StringType)
types_JvmTypeConstraint_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={}, type=StringType)
types_JvmTypeConstraint_m_getQualifiedName: Method = Method(name="getQualifiedName", parameters={Parameter(name='innerClassDelimiter')}, type=StringType)
types_JvmTypeConstraint.methods={types_JvmTypeConstraint_m_getQualifiedName, types_JvmTypeConstraint_m_getQualifiedName, types_JvmTypeConstraint_m_getIdentifier, types_JvmTypeConstraint_m_getSimpleName}

# types_JvmWildcardTypeReference class attributes and methods

# types_JvmAnyTypeReference class attributes and methods

# types_JvmMultiTypeReference class attributes and methods

# JvmCompoundTypeReference class attributes and methods

# JvmAnnotationTarget class attributes and methods

# types_JvmParameterizedTypeReference class attributes and methods

# JvmTypeReference class attributes and methods

# types_JvmGenericArrayTypeReference class attributes and methods
types_JvmGenericArrayTypeReference_m_getDimensions: Method = Method(name="getDimensions", parameters={}, type=IntegerType)
types_JvmGenericArrayTypeReference_m_getType: Method = Method(name="getType", parameters={}, type=StringType)
types_JvmGenericArrayTypeReference.methods={types_JvmGenericArrayTypeReference_m_getType, types_JvmGenericArrayTypeReference_m_getDimensions}

# types_JvmExecutable class attributes and methods
types_JvmExecutable_varArgs: Property = Property(name="varArgs", type=BooleanType)
types_JvmExecutable.attributes={types_JvmExecutable_varArgs}

# types_JvmFormalParameter class attributes and methods
types_JvmFormalParameter_name: Property = Property(name="name", type=StringType)
types_JvmFormalParameter.attributes={types_JvmFormalParameter_name}

# types_JvmConstructor class attributes and methods

# JvmExecutable class attributes and methods

# types_JvmOperation class attributes and methods
types_JvmOperation_static: Property = Property(name="static", type=BooleanType)
types_JvmOperation_final: Property = Property(name="final", type=BooleanType)
types_JvmOperation_abstract: Property = Property(name="abstract", type=BooleanType)
types_JvmOperation_synchronized: Property = Property(name="synchronized", type=BooleanType)
types_JvmOperation_default: Property = Property(name="default", type=BooleanType)
types_JvmOperation_native: Property = Property(name="native", type=BooleanType)
types_JvmOperation_strictFloatingPoint: Property = Property(name="strictFloatingPoint", type=BooleanType)
types_JvmOperation.attributes={types_JvmOperation_static, types_JvmOperation_native, types_JvmOperation_strictFloatingPoint, types_JvmOperation_synchronized, types_JvmOperation_abstract, types_JvmOperation_default, types_JvmOperation_final}

# types_JvmFeature class attributes and methods
types_JvmFeature_m_isStatic: Method = Method(name="isStatic", parameters={}, type=BooleanType)
types_JvmFeature.methods={types_JvmFeature_m_isStatic}

# types_JvmField class attributes and methods
types_JvmField_volatile: Property = Property(name="volatile", type=BooleanType)
types_JvmField_transient: Property = Property(name="transient", type=BooleanType)
types_JvmField_constant: Property = Property(name="constant", type=BooleanType)
types_JvmField_constantValue: Property = Property(name="constantValue", type=StringType)
types_JvmField_static: Property = Property(name="static", type=BooleanType)
types_JvmField_final: Property = Property(name="final", type=BooleanType)
types_JvmField_m_getConstantValueAsLong: Method = Method(name="getConstantValueAsLong", parameters={}, type=StringType)
types_JvmField_m_getConstantValueAsInt: Method = Method(name="getConstantValueAsInt", parameters={}, type=IntegerType)
types_JvmField_m_getConstantValueAsShort: Method = Method(name="getConstantValueAsShort", parameters={}, type=StringType)
types_JvmField_m_getConstantValueAsByte: Method = Method(name="getConstantValueAsByte", parameters={}, type=StringType)
types_JvmField_m_getConstantValueAsDouble: Method = Method(name="getConstantValueAsDouble", parameters={}, type=FloatType)
types_JvmField_m_getConstantValueAsFloat: Method = Method(name="getConstantValueAsFloat", parameters={}, type=FloatType)
types_JvmField_m_getConstantValueAsChar: Method = Method(name="getConstantValueAsChar", parameters={}, type=StringType)
types_JvmField_m_getConstantValueAsBoolean: Method = Method(name="getConstantValueAsBoolean", parameters={}, type=BooleanType)
types_JvmField_m_getConstantValueAsString: Method = Method(name="getConstantValueAsString", parameters={}, type=StringType)
types_JvmField.attributes={types_JvmField_static, types_JvmField_constantValue, types_JvmField_transient, types_JvmField_volatile, types_JvmField_final, types_JvmField_constant}
types_JvmField.methods={types_JvmField_m_getConstantValueAsByte, types_JvmField_m_getConstantValueAsString, types_JvmField_m_getConstantValueAsBoolean, types_JvmField_m_getConstantValueAsLong, types_JvmField_m_getConstantValueAsDouble, types_JvmField_m_getConstantValueAsShort, types_JvmField_m_getConstantValueAsInt, types_JvmField_m_getConstantValueAsChar, types_JvmField_m_getConstantValueAsFloat}

# JvmFeature class attributes and methods

# types_JvmIntAnnotationValue class attributes and methods
types_JvmIntAnnotationValue_values: Property = Property(name="values", type=IntegerType)
types_JvmIntAnnotationValue.attributes={types_JvmIntAnnotationValue_values}

# JvmAnnotationValue class attributes and methods

# types_JvmBooleanAnnotationValue class attributes and methods
types_JvmBooleanAnnotationValue_values: Property = Property(name="values", type=BooleanType)
types_JvmBooleanAnnotationValue.attributes={types_JvmBooleanAnnotationValue_values}

# types_JvmByteAnnotationValue class attributes and methods
types_JvmByteAnnotationValue_values: Property = Property(name="values", type=StringType)
types_JvmByteAnnotationValue.attributes={types_JvmByteAnnotationValue_values}

# types_JvmShortAnnotationValue class attributes and methods
types_JvmShortAnnotationValue_values: Property = Property(name="values", type=StringType)
types_JvmShortAnnotationValue.attributes={types_JvmShortAnnotationValue_values}

# types_JvmAnnotationValue class attributes and methods
types_JvmAnnotationValue_m_getValueName: Method = Method(name="getValueName", parameters={}, type=StringType)
types_JvmAnnotationValue.methods={types_JvmAnnotationValue_m_getValueName}

# types_JvmAnnotationTarget class attributes and methods

# types_JvmAnnotationReference class attributes and methods
types_JvmAnnotationReference_m_getValues: Method = Method(name="getValues", parameters={}, type=StringType)
types_JvmAnnotationReference.methods={types_JvmAnnotationReference_m_getValues}

# types_JvmDelegateTypeReference class attributes and methods

# types_JvmSpecializedTypeReference class attributes and methods

# types_JvmSynonymTypeReference class attributes and methods

# types_JvmUnknownTypeReference class attributes and methods
types_JvmUnknownTypeReference_qualifiedName: Property = Property(name="qualifiedName", type=StringType)
types_JvmUnknownTypeReference.attributes={types_JvmUnknownTypeReference_qualifiedName}

# types_JvmCompoundTypeReference class attributes and methods

# types_JvmLongAnnotationValue class attributes and methods
types_JvmLongAnnotationValue_values: Property = Property(name="values", type=StringType)
types_JvmLongAnnotationValue.attributes={types_JvmLongAnnotationValue_values}

# types_JvmDoubleAnnotationValue class attributes and methods
types_JvmDoubleAnnotationValue_values: Property = Property(name="values", type=FloatType)
types_JvmDoubleAnnotationValue.attributes={types_JvmDoubleAnnotationValue_values}

# types_JvmFloatAnnotationValue class attributes and methods
types_JvmFloatAnnotationValue_values: Property = Property(name="values", type=FloatType)
types_JvmFloatAnnotationValue.attributes={types_JvmFloatAnnotationValue_values}

# types_JvmCharAnnotationValue class attributes and methods
types_JvmCharAnnotationValue_values: Property = Property(name="values", type=StringType)
types_JvmCharAnnotationValue.attributes={types_JvmCharAnnotationValue_values}

# types_JvmStringAnnotationValue class attributes and methods
types_JvmStringAnnotationValue_values: Property = Property(name="values", type=StringType)
types_JvmStringAnnotationValue.attributes={types_JvmStringAnnotationValue_values}

# types_JvmTypeAnnotationValue class attributes and methods

# types_JvmAnnotationAnnotationValue class attributes and methods

# types_JvmEnumAnnotationValue class attributes and methods

# types_JvmCustomAnnotationValue class attributes and methods

# types_EObject class attributes and methods

# types_JvmInnerTypeReference class attributes and methods

# JvmParameterizedTypeReference class attributes and methods

# Relationships
arrayType0: BinaryAssociation = BinaryAssociation(
    name="arrayType0",
    ends={
        Property(name="JvmArrayType", type=types_JvmComponentType, multiplicity=Multiplicity(1, 1)),
        Property(name="componentType", type=types_JvmArrayType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
componentType1: BinaryAssociation = BinaryAssociation(
    name="componentType1",
    ends={
        Property(name="JvmComponentType", type=types_JvmArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="arrayType", type=types_JvmComponentType, multiplicity=Multiplicity(0, 1))
    }
)
owner9: BinaryAssociation = BinaryAssociation(
    name="owner9",
    ends={
        Property(name="JvmConstraintOwner", type=types_JvmTypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraints", type=types_JvmConstraintOwner, multiplicity=Multiplicity(0, 1))
    }
)
literals10: BinaryAssociation = BinaryAssociation(
    name="literals10",
    ends={
        Property(name="types_JvmEnumerationLiteral", type=types_JvmEnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmEnumerationType", type=types_JvmEnumerationLiteral, multiplicity=Multiplicity(0, 9999))
    }
)
superTypes2: BinaryAssociation = BinaryAssociation(
    name="superTypes2",
    ends={
        Property(name="types_JvmTypeReference", type=types_JvmDeclaredType, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmDeclaredType", type=types_JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members3: BinaryAssociation = BinaryAssociation(
    name="members3",
    ends={
        Property(name="JvmMember", type=types_JvmDeclaredType, multiplicity=Multiplicity(1, 1)),
        Property(name="declaringType", type=types_JvmMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarator4: BinaryAssociation = BinaryAssociation(
    name="declarator4",
    ends={
        Property(name="JvmTypeParameterDeclarator", type=types_JvmTypeParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="typeParameters", type=types_JvmTypeParameterDeclarator, multiplicity=Multiplicity(0, 1))
    }
)
typeParameters5: BinaryAssociation = BinaryAssociation(
    name="typeParameters5",
    ends={
        Property(name="JvmTypeParameter", type=types_JvmTypeParameterDeclarator, multiplicity=Multiplicity(1, 1)),
        Property(name="declarator", type=types_JvmTypeParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints6: BinaryAssociation = BinaryAssociation(
    name="constraints6",
    ends={
        Property(name="JvmTypeConstraint", type=types_JvmConstraintOwner, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=types_JvmTypeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeReference7: BinaryAssociation = BinaryAssociation(
    name="typeReference7",
    ends={
        Property(name="types_JvmTypeReference8", type=types_JvmTypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmTypeConstraint", type=types_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
componentType15: BinaryAssociation = BinaryAssociation(
    name="componentType15",
    ends={
        Property(name="types_JvmTypeReference16", type=types_JvmGenericArrayTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmGenericArrayTypeReference", type=types_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type17: BinaryAssociation = BinaryAssociation(
    name="type17",
    ends={
        Property(name="types_JvmType18", type=types_JvmAnyTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmAnyTypeReference", type=types_JvmType, multiplicity=Multiplicity(0, 1))
    }
)
declaringType19: BinaryAssociation = BinaryAssociation(
    name="declaringType19",
    ends={
        Property(name="JvmDeclaredType", type=types_JvmMember, multiplicity=Multiplicity(1, 1)),
        Property(name="members", type=types_JvmDeclaredType, multiplicity=Multiplicity(0, 1))
    }
)
arguments11: BinaryAssociation = BinaryAssociation(
    name="arguments11",
    ends={
        Property(name="types_JvmTypeReference12", type=types_JvmParameterizedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmParameterizedTypeReference", type=types_JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type13: BinaryAssociation = BinaryAssociation(
    name="type13",
    ends={
        Property(name="types_JvmType", type=types_JvmParameterizedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmParameterizedTypeReference14", type=types_JvmType, multiplicity=Multiplicity(0, 1))
    }
)
parameters23: BinaryAssociation = BinaryAssociation(
    name="parameters23",
    ends={
        Property(name="types_JvmFormalParameter", type=types_JvmExecutable, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmExecutable", type=types_JvmFormalParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exceptions24: BinaryAssociation = BinaryAssociation(
    name="exceptions24",
    ends={
        Property(name="types_JvmTypeReference26", type=types_JvmExecutable, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmExecutable25", type=types_JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
localClasses20: BinaryAssociation = BinaryAssociation(
    name="localClasses20",
    ends={
        Property(name="types_JvmGenericType", type=types_JvmFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmFeature", type=types_JvmGenericType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type21: BinaryAssociation = BinaryAssociation(
    name="type21",
    ends={
        Property(name="types_JvmTypeReference22", type=types_JvmField, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmField", type=types_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operation40: BinaryAssociation = BinaryAssociation(
    name="operation40",
    ends={
        Property(name="types_JvmOperation42", type=types_JvmAnnotationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmAnnotationValue41", type=types_JvmOperation, multiplicity=Multiplicity(0, 1))
    }
)
returnType27: BinaryAssociation = BinaryAssociation(
    name="returnType27",
    ends={
        Property(name="types_JvmTypeReference28", type=types_JvmOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmOperation", type=types_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue29: BinaryAssociation = BinaryAssociation(
    name="defaultValue29",
    ends={
        Property(name="types_JvmAnnotationValue", type=types_JvmOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmOperation30", type=types_JvmAnnotationValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterType31: BinaryAssociation = BinaryAssociation(
    name="parameterType31",
    ends={
        Property(name="types_JvmTypeReference33", type=types_JvmFormalParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmFormalParameter32", type=types_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations34: BinaryAssociation = BinaryAssociation(
    name="annotations34",
    ends={
        Property(name="types_JvmAnnotationReference", type=types_JvmAnnotationTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmAnnotationTarget", type=types_JvmAnnotationReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation35: BinaryAssociation = BinaryAssociation(
    name="annotation35",
    ends={
        Property(name="types_JvmAnnotationType", type=types_JvmAnnotationReference, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmAnnotationReference36", type=types_JvmAnnotationType, multiplicity=Multiplicity(0, 1))
    }
)
explicitValues37: BinaryAssociation = BinaryAssociation(
    name="explicitValues37",
    ends={
        Property(name="types_JvmAnnotationValue39", type=types_JvmAnnotationReference, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmAnnotationReference38", type=types_JvmAnnotationValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
delegate49: BinaryAssociation = BinaryAssociation(
    name="delegate49",
    ends={
        Property(name="types_JvmTypeReference50", type=types_JvmDelegateTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmDelegateTypeReference", type=types_JvmTypeReference, multiplicity=Multiplicity(0, 1))
    }
)
equivalent51: BinaryAssociation = BinaryAssociation(
    name="equivalent51",
    ends={
        Property(name="types_JvmTypeReference52", type=types_JvmSpecializedTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmSpecializedTypeReference", type=types_JvmTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values43: BinaryAssociation = BinaryAssociation(
    name="values43",
    ends={
        Property(name="types_JvmTypeReference44", type=types_JvmTypeAnnotationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmTypeAnnotationValue", type=types_JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values45: BinaryAssociation = BinaryAssociation(
    name="values45",
    ends={
        Property(name="types_JvmAnnotationReference46", type=types_JvmAnnotationAnnotationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmAnnotationAnnotationValue", type=types_JvmAnnotationReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values47: BinaryAssociation = BinaryAssociation(
    name="values47",
    ends={
        Property(name="types_JvmEnumerationLiteral48", type=types_JvmEnumAnnotationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmEnumAnnotationValue", type=types_JvmEnumerationLiteral, multiplicity=Multiplicity(0, 9999))
    }
)
type53: BinaryAssociation = BinaryAssociation(
    name="type53",
    ends={
        Property(name="types_JvmType54", type=types_JvmCompoundTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmCompoundTypeReference", type=types_JvmType, multiplicity=Multiplicity(0, 1))
    }
)
references55: BinaryAssociation = BinaryAssociation(
    name="references55",
    ends={
        Property(name="types_JvmTypeReference57", type=types_JvmCompoundTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmCompoundTypeReference56", type=types_JvmTypeReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values58: BinaryAssociation = BinaryAssociation(
    name="values58",
    ends={
        Property(name="types_EObject", type=types_JvmCustomAnnotationValue, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmCustomAnnotationValue", type=types_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
outer59: BinaryAssociation = BinaryAssociation(
    name="outer59",
    ends={
        Property(name="types_JvmParameterizedTypeReference60", type=types_JvmInnerTypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="types_JvmInnerTypeReference", type=types_JvmParameterizedTypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_types_JvmType_JvmIdentifiableElement = Generalization(general=JvmIdentifiableElement, specific=types_JvmType)
gen_types_JvmVoid_JvmType = Generalization(general=JvmType, specific=types_JvmVoid)
gen_types_JvmComponentType_JvmType = Generalization(general=JvmType, specific=types_JvmComponentType)
gen_types_JvmPrimitiveType_JvmComponentType = Generalization(general=JvmComponentType, specific=types_JvmPrimitiveType)
gen_types_JvmArrayType_JvmComponentType = Generalization(general=JvmComponentType, specific=types_JvmArrayType)
gen_types_JvmDeclaredType_JvmMember = Generalization(general=JvmMember, specific=types_JvmDeclaredType)
gen_types_JvmDeclaredType_JvmComponentType = Generalization(general=JvmComponentType, specific=types_JvmDeclaredType)
gen_types_JvmUpperBound_JvmTypeConstraint = Generalization(general=JvmTypeConstraint, specific=types_JvmUpperBound)
gen_types_JvmLowerBound_JvmTypeConstraint = Generalization(general=JvmTypeConstraint, specific=types_JvmLowerBound)
gen_types_JvmAnnotationType_JvmDeclaredType = Generalization(general=JvmDeclaredType, specific=types_JvmAnnotationType)
gen_types_JvmEnumerationType_JvmDeclaredType = Generalization(general=JvmDeclaredType, specific=types_JvmEnumerationType)
gen_types_JvmEnumerationLiteral_JvmField = Generalization(general=JvmField, specific=types_JvmEnumerationLiteral)
gen_types_JvmGenericType_JvmDeclaredType = Generalization(general=JvmDeclaredType, specific=types_JvmGenericType)
gen_types_JvmGenericType_JvmTypeParameterDeclarator = Generalization(general=JvmTypeParameterDeclarator, specific=types_JvmGenericType)
gen_types_JvmTypeParameter_JvmComponentType = Generalization(general=JvmComponentType, specific=types_JvmTypeParameter)
gen_types_JvmTypeParameter_JvmConstraintOwner = Generalization(general=JvmConstraintOwner, specific=types_JvmTypeParameter)
gen_types_JvmWildcardTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=types_JvmWildcardTypeReference)
gen_types_JvmWildcardTypeReference_JvmConstraintOwner = Generalization(general=JvmConstraintOwner, specific=types_JvmWildcardTypeReference)
gen_types_JvmAnyTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=types_JvmAnyTypeReference)
gen_types_JvmMultiTypeReference_JvmCompoundTypeReference = Generalization(general=JvmCompoundTypeReference, specific=types_JvmMultiTypeReference)
gen_types_JvmMember_JvmAnnotationTarget = Generalization(general=JvmAnnotationTarget, specific=types_JvmMember)
gen_types_JvmParameterizedTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=types_JvmParameterizedTypeReference)
gen_types_JvmGenericArrayTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=types_JvmGenericArrayTypeReference)
gen_types_JvmExecutable_JvmFeature = Generalization(general=JvmFeature, specific=types_JvmExecutable)
gen_types_JvmExecutable_JvmTypeParameterDeclarator = Generalization(general=JvmTypeParameterDeclarator, specific=types_JvmExecutable)
gen_types_JvmConstructor_JvmExecutable = Generalization(general=JvmExecutable, specific=types_JvmConstructor)
gen_types_JvmOperation_JvmExecutable = Generalization(general=JvmExecutable, specific=types_JvmOperation)
gen_types_JvmFeature_JvmMember = Generalization(general=JvmMember, specific=types_JvmFeature)
gen_types_JvmField_JvmFeature = Generalization(general=JvmFeature, specific=types_JvmField)
gen_types_JvmIntAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=types_JvmIntAnnotationValue)
gen_types_JvmBooleanAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=types_JvmBooleanAnnotationValue)
gen_types_JvmByteAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=types_JvmByteAnnotationValue)
gen_types_JvmShortAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=types_JvmShortAnnotationValue)
gen_types_JvmFormalParameter_JvmAnnotationTarget = Generalization(general=JvmAnnotationTarget, specific=types_JvmFormalParameter)
gen_types_JvmAnnotationTarget_JvmIdentifiableElement = Generalization(general=JvmIdentifiableElement, specific=types_JvmAnnotationTarget)
gen_types_JvmDelegateTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=types_JvmDelegateTypeReference)
gen_types_JvmSpecializedTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=types_JvmSpecializedTypeReference)
gen_types_JvmSynonymTypeReference_JvmCompoundTypeReference = Generalization(general=JvmCompoundTypeReference, specific=types_JvmSynonymTypeReference)
gen_types_JvmUnknownTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=types_JvmUnknownTypeReference)
gen_types_JvmCompoundTypeReference_JvmTypeReference = Generalization(general=JvmTypeReference, specific=types_JvmCompoundTypeReference)
gen_types_JvmLongAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=types_JvmLongAnnotationValue)
gen_types_JvmDoubleAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=types_JvmDoubleAnnotationValue)
gen_types_JvmFloatAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=types_JvmFloatAnnotationValue)
gen_types_JvmCharAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=types_JvmCharAnnotationValue)
gen_types_JvmStringAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=types_JvmStringAnnotationValue)
gen_types_JvmTypeAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=types_JvmTypeAnnotationValue)
gen_types_JvmAnnotationAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=types_JvmAnnotationAnnotationValue)
gen_types_JvmEnumAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=types_JvmEnumAnnotationValue)
gen_types_JvmCustomAnnotationValue_JvmAnnotationValue = Generalization(general=JvmAnnotationValue, specific=types_JvmCustomAnnotationValue)
gen_types_JvmInnerTypeReference_JvmParameterizedTypeReference = Generalization(general=JvmParameterizedTypeReference, specific=types_JvmInnerTypeReference)

# Domain Model
domain_model = DomainModel(
    name="types",
    types={types_JvmType, JvmIdentifiableElement, types_JvmVoid, JvmType, types_JvmComponentType, types_JvmArrayType, types_JvmIdentifiableElement, types_JvmTypeReference, types_JvmPrimitiveType, JvmComponentType, types_JvmDeclaredType, JvmMember, types_JvmUpperBound, JvmTypeConstraint, types_JvmLowerBound, types_JvmAnnotationType, JvmDeclaredType, types_JvmEnumerationType, types_JvmEnumerationLiteral, JvmField, types_JvmGenericType, JvmTypeParameterDeclarator, types_JvmMember, types_JvmTypeParameter, JvmConstraintOwner, types_JvmTypeParameterDeclarator, types_JvmConstraintOwner, types_JvmTypeConstraint, types_JvmWildcardTypeReference, types_JvmAnyTypeReference, types_JvmMultiTypeReference, JvmCompoundTypeReference, JvmAnnotationTarget, types_JvmParameterizedTypeReference, JvmTypeReference, types_JvmGenericArrayTypeReference, types_JvmExecutable, types_JvmFormalParameter, types_JvmConstructor, JvmExecutable, types_JvmOperation, types_JvmFeature, types_JvmField, JvmFeature, types_JvmIntAnnotationValue, JvmAnnotationValue, types_JvmBooleanAnnotationValue, types_JvmByteAnnotationValue, types_JvmShortAnnotationValue, types_JvmAnnotationValue, types_JvmAnnotationTarget, types_JvmAnnotationReference, types_JvmDelegateTypeReference, types_JvmSpecializedTypeReference, types_JvmSynonymTypeReference, types_JvmUnknownTypeReference, types_JvmCompoundTypeReference, types_JvmLongAnnotationValue, types_JvmDoubleAnnotationValue, types_JvmFloatAnnotationValue, types_JvmCharAnnotationValue, types_JvmStringAnnotationValue, types_JvmTypeAnnotationValue, types_JvmAnnotationAnnotationValue, types_JvmEnumAnnotationValue, types_JvmCustomAnnotationValue, types_EObject, types_JvmInnerTypeReference, JvmParameterizedTypeReference, JvmVisibility},
    associations={arrayType0, componentType1, owner9, literals10, superTypes2, members3, declarator4, typeParameters5, constraints6, typeReference7, componentType15, type17, declaringType19, arguments11, type13, parameters23, exceptions24, localClasses20, type21, operation40, returnType27, defaultValue29, parameterType31, annotations34, annotation35, explicitValues37, delegate49, equivalent51, values43, values45, values47, type53, references55, values58, outer59},
    generalizations={gen_types_JvmType_JvmIdentifiableElement, gen_types_JvmVoid_JvmType, gen_types_JvmComponentType_JvmType, gen_types_JvmPrimitiveType_JvmComponentType, gen_types_JvmArrayType_JvmComponentType, gen_types_JvmDeclaredType_JvmMember, gen_types_JvmDeclaredType_JvmComponentType, gen_types_JvmUpperBound_JvmTypeConstraint, gen_types_JvmLowerBound_JvmTypeConstraint, gen_types_JvmAnnotationType_JvmDeclaredType, gen_types_JvmEnumerationType_JvmDeclaredType, gen_types_JvmEnumerationLiteral_JvmField, gen_types_JvmGenericType_JvmDeclaredType, gen_types_JvmGenericType_JvmTypeParameterDeclarator, gen_types_JvmTypeParameter_JvmComponentType, gen_types_JvmTypeParameter_JvmConstraintOwner, gen_types_JvmWildcardTypeReference_JvmTypeReference, gen_types_JvmWildcardTypeReference_JvmConstraintOwner, gen_types_JvmAnyTypeReference_JvmTypeReference, gen_types_JvmMultiTypeReference_JvmCompoundTypeReference, gen_types_JvmMember_JvmAnnotationTarget, gen_types_JvmParameterizedTypeReference_JvmTypeReference, gen_types_JvmGenericArrayTypeReference_JvmTypeReference, gen_types_JvmExecutable_JvmFeature, gen_types_JvmExecutable_JvmTypeParameterDeclarator, gen_types_JvmConstructor_JvmExecutable, gen_types_JvmOperation_JvmExecutable, gen_types_JvmFeature_JvmMember, gen_types_JvmField_JvmFeature, gen_types_JvmIntAnnotationValue_JvmAnnotationValue, gen_types_JvmBooleanAnnotationValue_JvmAnnotationValue, gen_types_JvmByteAnnotationValue_JvmAnnotationValue, gen_types_JvmShortAnnotationValue_JvmAnnotationValue, gen_types_JvmFormalParameter_JvmAnnotationTarget, gen_types_JvmAnnotationTarget_JvmIdentifiableElement, gen_types_JvmDelegateTypeReference_JvmTypeReference, gen_types_JvmSpecializedTypeReference_JvmTypeReference, gen_types_JvmSynonymTypeReference_JvmCompoundTypeReference, gen_types_JvmUnknownTypeReference_JvmTypeReference, gen_types_JvmCompoundTypeReference_JvmTypeReference, gen_types_JvmLongAnnotationValue_JvmAnnotationValue, gen_types_JvmDoubleAnnotationValue_JvmAnnotationValue, gen_types_JvmFloatAnnotationValue_JvmAnnotationValue, gen_types_JvmCharAnnotationValue_JvmAnnotationValue, gen_types_JvmStringAnnotationValue_JvmAnnotationValue, gen_types_JvmTypeAnnotationValue_JvmAnnotationValue, gen_types_JvmAnnotationAnnotationValue_JvmAnnotationValue, gen_types_JvmEnumAnnotationValue_JvmAnnotationValue, gen_types_JvmCustomAnnotationValue_JvmAnnotationValue, gen_types_JvmInnerTypeReference_JvmParameterizedTypeReference},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)