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
jointPackage_Ecore2Maude_JointMM = Class(name="jointPackage::Ecore2Maude::JointMM")
jointPackage_Ecore2Maude_SrcEStringToStringMapEntry = Class(name="jointPackage::Ecore2Maude::SrcEStringToStringMapEntry")
jointPackage_Ecore2Maude_TrgEqualCond = Class(name="jointPackage::Ecore2Maude::TrgEqualCond")
jointPackage_Ecore2Maude_SrcEAttribute = Class(name="jointPackage::Ecore2Maude::SrcEAttribute")
SrcEStructuralFeature = Class(name="SrcEStructuralFeature")
jointPackage_Ecore2Maude_SrcEDataType = Class(name="jointPackage::Ecore2Maude::SrcEDataType")
jointPackage_Ecore2Maude_SrcEClassifier = Class(name="jointPackage::Ecore2Maude::SrcEClassifier", is_abstract=True)
SrcENamedElement = Class(name="SrcENamedElement")
jointPackage_Ecore2Maude_SrcEOperation = Class(name="jointPackage::Ecore2Maude::SrcEOperation")
jointPackage_Ecore2Maude_SrcEReference = Class(name="jointPackage::Ecore2Maude::SrcEReference")
jointPackage_Ecore2Maude_SrcEStructuralFeature = Class(name="jointPackage::Ecore2Maude::SrcEStructuralFeature", is_abstract=True)
jointPackage_Ecore2Maude_SrcEClass = Class(name="jointPackage::Ecore2Maude::SrcEClass")
SrcEClassifier = Class(name="SrcEClassifier")
jointPackage_Ecore2Maude_SrcEParameter = Class(name="jointPackage::Ecore2Maude::SrcEParameter")
jointPackage_Ecore2Maude_SrcEPackage = Class(name="jointPackage::Ecore2Maude::SrcEPackage")
jointPackage_Ecore2Maude_SrcEEnum = Class(name="jointPackage::Ecore2Maude::SrcEEnum")
SrcEDataType = Class(name="SrcEDataType")
jointPackage_Ecore2Maude_SrcEEnumLiteral = Class(name="jointPackage::Ecore2Maude::SrcEEnumLiteral")
jointPackage_Ecore2Maude_SrcENamedElement = Class(name="jointPackage::Ecore2Maude::SrcENamedElement", is_abstract=True)
SrcETypedElement = Class(name="SrcETypedElement")
jointPackage_Ecore2Maude_SrcETypedElement = Class(name="jointPackage::Ecore2Maude::SrcETypedElement", is_abstract=True)
jointPackage_Ecore2Maude_TrgMembershipCond = Class(name="jointPackage::Ecore2Maude::TrgMembershipCond")
TrgEquationalCond = Class(name="TrgEquationalCond")
jointPackage_Ecore2Maude_TrgBooleanCond = Class(name="jointPackage::Ecore2Maude::TrgBooleanCond")
jointPackage_Ecore2Maude_TrgMatchingCond = Class(name="jointPackage::Ecore2Maude::TrgMatchingCond")
jointPackage_Ecore2Maude_TrgMaudeSpec = Class(name="jointPackage::Ecore2Maude::TrgMaudeSpec")
jointPackage_Ecore2Maude_TrgMaudeTopEl = Class(name="jointPackage::Ecore2Maude::TrgMaudeTopEl", is_abstract=True)
jointPackage_Ecore2Maude_TrgMembership = Class(name="jointPackage::Ecore2Maude::TrgMembership")
TrgStatement = Class(name="TrgStatement")
jointPackage_Ecore2Maude_TrgTerm = Class(name="jointPackage::Ecore2Maude::TrgTerm", is_abstract=True)
jointPackage_Ecore2Maude_TrgSort = Class(name="jointPackage::Ecore2Maude::TrgSort")
jointPackage_Ecore2Maude_TrgEquation = Class(name="jointPackage::Ecore2Maude::TrgEquation")
jointPackage_Ecore2Maude_TrgRule = Class(name="jointPackage::Ecore2Maude::TrgRule")
TrgMaudeTopEl = Class(name="TrgMaudeTopEl")
jointPackage_Ecore2Maude_TrgModElement = Class(name="jointPackage::Ecore2Maude::TrgModElement", is_abstract=True)
jointPackage_Ecore2Maude_TrgFTheory = Class(name="jointPackage::Ecore2Maude::TrgFTheory")
TrgTheory = Class(name="TrgTheory")
jointPackage_Ecore2Maude_TrgSTheory = Class(name="jointPackage::Ecore2Maude::TrgSTheory")
jointPackage_Ecore2Maude_TrgModExpression = Class(name="jointPackage::Ecore2Maude::TrgModExpression", is_abstract=True)
jointPackage_Ecore2Maude_TrgInstModExp = Class(name="jointPackage::Ecore2Maude::TrgInstModExp")
TrgModExpression = Class(name="TrgModExpression")
jointPackage_Ecore2Maude_TrgView = Class(name="jointPackage::Ecore2Maude::TrgView")
jointPackage_Ecore2Maude_TrgRenModExp = Class(name="jointPackage::Ecore2Maude::TrgRenModExp")
jointPackage_Ecore2Maude_TrgRenMapping = Class(name="jointPackage::Ecore2Maude::TrgRenMapping", is_abstract=True)
jointPackage_Ecore2Maude_TrgCompModExp = Class(name="jointPackage::Ecore2Maude::TrgCompModExp")
jointPackage_Ecore2Maude_TrgModuleIdModExp = Class(name="jointPackage::Ecore2Maude::TrgModuleIdModExp")
jointPackage_Ecore2Maude_TrgModule = Class(name="jointPackage::Ecore2Maude::TrgModule", is_abstract=True)
jointPackage_Ecore2Maude_TrgTheoryIdModExp = Class(name="jointPackage::Ecore2Maude::TrgTheoryIdModExp")
jointPackage_Ecore2Maude_TrgTheory = Class(name="jointPackage::Ecore2Maude::TrgTheory", is_abstract=True)
jointPackage_Ecore2Maude_TrgParameter = Class(name="jointPackage::Ecore2Maude::TrgParameter")
jointPackage_Ecore2Maude_TrgKind = Class(name="jointPackage::Ecore2Maude::TrgKind")
jointPackage_Ecore2Maude_TrgFModule = Class(name="jointPackage::Ecore2Maude::TrgFModule")
TrgModule = Class(name="TrgModule")
jointPackage_Ecore2Maude_TrgSModule = Class(name="jointPackage::Ecore2Maude::TrgSModule")
jointPackage_Ecore2Maude_TrgModImportation = Class(name="jointPackage::Ecore2Maude::TrgModImportation")
TrgModElement = Class(name="TrgModElement")
jointPackage_Ecore2Maude_TrgType = Class(name="jointPackage::Ecore2Maude::TrgType", is_abstract=True)
TrgType = Class(name="TrgType")
jointPackage_Ecore2Maude_TrgSubsortRel = Class(name="jointPackage::Ecore2Maude::TrgSubsortRel")
jointPackage_Ecore2Maude_TrgConstant = Class(name="jointPackage::Ecore2Maude::TrgConstant")
TrgTerm = Class(name="TrgTerm")
jointPackage_Ecore2Maude_TrgRecTerm = Class(name="jointPackage::Ecore2Maude::TrgRecTerm")
jointPackage_Ecore2Maude_TrgVariable = Class(name="jointPackage::Ecore2Maude::TrgVariable")
jointPackage_Ecore2Maude_TrgOperation = Class(name="jointPackage::Ecore2Maude::TrgOperation")
jointPackage_Ecore2Maude_TrgStatement = Class(name="jointPackage::Ecore2Maude::TrgStatement", is_abstract=True)
jointPackage_Ecore2Maude_TrgCondition = Class(name="jointPackage::Ecore2Maude::TrgCondition", is_abstract=True)
jointPackage_Ecore2Maude_TrgEquationalCond = Class(name="jointPackage::Ecore2Maude::TrgEquationalCond", is_abstract=True)
TrgCondition = Class(name="TrgCondition")
jointPackage_Ecore2Maude_TrgRewriteCond = Class(name="jointPackage::Ecore2Maude::TrgRewriteCond")
jointPackage_Ecore2Maude_TrgOpMapping = Class(name="jointPackage::Ecore2Maude::TrgOpMapping")
jointPackage_Ecore2Maude_TrgLabelMapping = Class(name="jointPackage::Ecore2Maude::TrgLabelMapping")
jointPackage_Ecore2Maude_TrgViewMapping = Class(name="jointPackage::Ecore2Maude::TrgViewMapping", is_abstract=True)
TrgViewMapping = Class(name="TrgViewMapping")
jointPackage_Ecore2Maude_TrgTermMapping = Class(name="jointPackage::Ecore2Maude::TrgTermMapping")
jointPackage_Ecore2Maude_TrgSortMapping = Class(name="jointPackage::Ecore2Maude::TrgSortMapping")
TrgRenMapping = Class(name="TrgRenMapping")
jointPackage_Ecore2Maude_TrgOpTypedMapping = Class(name="jointPackage::Ecore2Maude::TrgOpTypedMapping")

# jointPackage_Ecore2Maude_JointMM class attributes and methods

# jointPackage_Ecore2Maude_SrcEStringToStringMapEntry class attributes and methods
jointPackage_Ecore2Maude_SrcEStringToStringMapEntry_key: Property = Property(name="key", type=StringType)
jointPackage_Ecore2Maude_SrcEStringToStringMapEntry_value: Property = Property(name="value", type=StringType)
jointPackage_Ecore2Maude_SrcEStringToStringMapEntry.attributes={jointPackage_Ecore2Maude_SrcEStringToStringMapEntry_key, jointPackage_Ecore2Maude_SrcEStringToStringMapEntry_value}

# jointPackage_Ecore2Maude_TrgEqualCond class attributes and methods

# jointPackage_Ecore2Maude_SrcEAttribute class attributes and methods
jointPackage_Ecore2Maude_SrcEAttribute_iD: Property = Property(name="iD", type=BooleanType)
jointPackage_Ecore2Maude_SrcEAttribute.attributes={jointPackage_Ecore2Maude_SrcEAttribute_iD}

# SrcEStructuralFeature class attributes and methods

# jointPackage_Ecore2Maude_SrcEDataType class attributes and methods
jointPackage_Ecore2Maude_SrcEDataType_serializable: Property = Property(name="serializable", type=BooleanType)
jointPackage_Ecore2Maude_SrcEDataType.attributes={jointPackage_Ecore2Maude_SrcEDataType_serializable}

# jointPackage_Ecore2Maude_SrcEClassifier class attributes and methods
jointPackage_Ecore2Maude_SrcEClassifier_instanceClassName: Property = Property(name="instanceClassName", type=StringType)
jointPackage_Ecore2Maude_SrcEClassifier_instanceTypeName: Property = Property(name="instanceTypeName", type=StringType)
jointPackage_Ecore2Maude_SrcEClassifier_m_getClassifierID: Method = Method(name="getClassifierID", parameters={}, type=IntegerType)
jointPackage_Ecore2Maude_SrcEClassifier.attributes={jointPackage_Ecore2Maude_SrcEClassifier_instanceTypeName, jointPackage_Ecore2Maude_SrcEClassifier_instanceClassName}
jointPackage_Ecore2Maude_SrcEClassifier.methods={jointPackage_Ecore2Maude_SrcEClassifier_m_getClassifierID}

# SrcENamedElement class attributes and methods

# jointPackage_Ecore2Maude_SrcEOperation class attributes and methods

# jointPackage_Ecore2Maude_SrcEReference class attributes and methods
jointPackage_Ecore2Maude_SrcEReference_containment: Property = Property(name="containment", type=BooleanType)
jointPackage_Ecore2Maude_SrcEReference_container: Property = Property(name="container", type=BooleanType)
jointPackage_Ecore2Maude_SrcEReference_resolveProxies: Property = Property(name="resolveProxies", type=BooleanType)
jointPackage_Ecore2Maude_SrcEReference.attributes={jointPackage_Ecore2Maude_SrcEReference_container, jointPackage_Ecore2Maude_SrcEReference_resolveProxies, jointPackage_Ecore2Maude_SrcEReference_containment}

# jointPackage_Ecore2Maude_SrcEStructuralFeature class attributes and methods
jointPackage_Ecore2Maude_SrcEStructuralFeature_changeable: Property = Property(name="changeable", type=BooleanType)
jointPackage_Ecore2Maude_SrcEStructuralFeature_volatile: Property = Property(name="volatile", type=BooleanType)
jointPackage_Ecore2Maude_SrcEStructuralFeature_transient: Property = Property(name="transient", type=BooleanType)
jointPackage_Ecore2Maude_SrcEStructuralFeature_defaultValueLiteral: Property = Property(name="defaultValueLiteral", type=StringType)
jointPackage_Ecore2Maude_SrcEStructuralFeature_unsettable: Property = Property(name="unsettable", type=BooleanType)
jointPackage_Ecore2Maude_SrcEStructuralFeature_derived: Property = Property(name="derived", type=BooleanType)
jointPackage_Ecore2Maude_SrcEStructuralFeature_m_getFeatureID: Method = Method(name="getFeatureID", parameters={}, type=IntegerType)
jointPackage_Ecore2Maude_SrcEStructuralFeature.attributes={jointPackage_Ecore2Maude_SrcEStructuralFeature_transient, jointPackage_Ecore2Maude_SrcEStructuralFeature_changeable, jointPackage_Ecore2Maude_SrcEStructuralFeature_derived, jointPackage_Ecore2Maude_SrcEStructuralFeature_defaultValueLiteral, jointPackage_Ecore2Maude_SrcEStructuralFeature_volatile, jointPackage_Ecore2Maude_SrcEStructuralFeature_unsettable}
jointPackage_Ecore2Maude_SrcEStructuralFeature.methods={jointPackage_Ecore2Maude_SrcEStructuralFeature_m_getFeatureID}

# jointPackage_Ecore2Maude_SrcEClass class attributes and methods
jointPackage_Ecore2Maude_SrcEClass_abstract: Property = Property(name="abstract", type=BooleanType)
jointPackage_Ecore2Maude_SrcEClass_interface: Property = Property(name="interface", type=BooleanType)
jointPackage_Ecore2Maude_SrcEClass_m_getFeatureCount: Method = Method(name="getFeatureCount", parameters={}, type=IntegerType)
jointPackage_Ecore2Maude_SrcEClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureID')}, type=SrcEStructuralFeature)
jointPackage_Ecore2Maude_SrcEClass_m_getFeatureID: Method = Method(name="getFeatureID", parameters={Parameter(name='feature')}, type=IntegerType)
jointPackage_Ecore2Maude_SrcEClass_m_getEStructuralFeature: Method = Method(name="getEStructuralFeature", parameters={Parameter(name='featureName')}, type=SrcEStructuralFeature)
jointPackage_Ecore2Maude_SrcEClass_m_isSuperTypeOf: Method = Method(name="isSuperTypeOf", parameters={Parameter(name='someClass')}, type=BooleanType)
jointPackage_Ecore2Maude_SrcEClass.attributes={jointPackage_Ecore2Maude_SrcEClass_abstract, jointPackage_Ecore2Maude_SrcEClass_interface}
jointPackage_Ecore2Maude_SrcEClass.methods={jointPackage_Ecore2Maude_SrcEClass_m_getFeatureID, jointPackage_Ecore2Maude_SrcEClass_m_isSuperTypeOf, jointPackage_Ecore2Maude_SrcEClass_m_getEStructuralFeature, jointPackage_Ecore2Maude_SrcEClass_m_getFeatureCount, jointPackage_Ecore2Maude_SrcEClass_m_getEStructuralFeature}

# SrcEClassifier class attributes and methods

# jointPackage_Ecore2Maude_SrcEParameter class attributes and methods

# jointPackage_Ecore2Maude_SrcEPackage class attributes and methods
jointPackage_Ecore2Maude_SrcEPackage_nsURI: Property = Property(name="nsURI", type=StringType)
jointPackage_Ecore2Maude_SrcEPackage_nsPrefix: Property = Property(name="nsPrefix", type=StringType)
jointPackage_Ecore2Maude_SrcEPackage_m_getEClassifier: Method = Method(name="getEClassifier", parameters={Parameter(name='name')}, type=SrcEClassifier)
jointPackage_Ecore2Maude_SrcEPackage.attributes={jointPackage_Ecore2Maude_SrcEPackage_nsPrefix, jointPackage_Ecore2Maude_SrcEPackage_nsURI}
jointPackage_Ecore2Maude_SrcEPackage.methods={jointPackage_Ecore2Maude_SrcEPackage_m_getEClassifier}

# jointPackage_Ecore2Maude_SrcEEnum class attributes and methods
jointPackage_Ecore2Maude_SrcEEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='name')}, type=StringType)
jointPackage_Ecore2Maude_SrcEEnum_m_getEEnumLiteral: Method = Method(name="getEEnumLiteral", parameters={Parameter(name='value')}, type=StringType)
jointPackage_Ecore2Maude_SrcEEnum_m_getEEnumLiteralByLiteral: Method = Method(name="getEEnumLiteralByLiteral", parameters={Parameter(name='literal')}, type=StringType)
jointPackage_Ecore2Maude_SrcEEnum.methods={jointPackage_Ecore2Maude_SrcEEnum_m_getEEnumLiteral, jointPackage_Ecore2Maude_SrcEEnum_m_getEEnumLiteral, jointPackage_Ecore2Maude_SrcEEnum_m_getEEnumLiteralByLiteral}

# SrcEDataType class attributes and methods

# jointPackage_Ecore2Maude_SrcEEnumLiteral class attributes and methods
jointPackage_Ecore2Maude_SrcEEnumLiteral_value: Property = Property(name="value", type=IntegerType)
jointPackage_Ecore2Maude_SrcEEnumLiteral_literal: Property = Property(name="literal", type=StringType)
jointPackage_Ecore2Maude_SrcEEnumLiteral.attributes={jointPackage_Ecore2Maude_SrcEEnumLiteral_value, jointPackage_Ecore2Maude_SrcEEnumLiteral_literal}

# jointPackage_Ecore2Maude_SrcENamedElement class attributes and methods
jointPackage_Ecore2Maude_SrcENamedElement_name: Property = Property(name="name", type=StringType)
jointPackage_Ecore2Maude_SrcENamedElement.attributes={jointPackage_Ecore2Maude_SrcENamedElement_name}

# SrcETypedElement class attributes and methods

# jointPackage_Ecore2Maude_SrcETypedElement class attributes and methods
jointPackage_Ecore2Maude_SrcETypedElement_ordered: Property = Property(name="ordered", type=BooleanType)
jointPackage_Ecore2Maude_SrcETypedElement_unique: Property = Property(name="unique", type=BooleanType)
jointPackage_Ecore2Maude_SrcETypedElement_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
jointPackage_Ecore2Maude_SrcETypedElement_upperBound: Property = Property(name="upperBound", type=IntegerType)
jointPackage_Ecore2Maude_SrcETypedElement_many: Property = Property(name="many", type=BooleanType)
jointPackage_Ecore2Maude_SrcETypedElement_required: Property = Property(name="required", type=BooleanType)
jointPackage_Ecore2Maude_SrcETypedElement.attributes={jointPackage_Ecore2Maude_SrcETypedElement_ordered, jointPackage_Ecore2Maude_SrcETypedElement_lowerBound, jointPackage_Ecore2Maude_SrcETypedElement_required, jointPackage_Ecore2Maude_SrcETypedElement_unique, jointPackage_Ecore2Maude_SrcETypedElement_many, jointPackage_Ecore2Maude_SrcETypedElement_upperBound}

# jointPackage_Ecore2Maude_TrgMembershipCond class attributes and methods

# TrgEquationalCond class attributes and methods

# jointPackage_Ecore2Maude_TrgBooleanCond class attributes and methods

# jointPackage_Ecore2Maude_TrgMatchingCond class attributes and methods

# jointPackage_Ecore2Maude_TrgMaudeSpec class attributes and methods

# jointPackage_Ecore2Maude_TrgMaudeTopEl class attributes and methods
jointPackage_Ecore2Maude_TrgMaudeTopEl_name: Property = Property(name="name", type=StringType)
jointPackage_Ecore2Maude_TrgMaudeTopEl.attributes={jointPackage_Ecore2Maude_TrgMaudeTopEl_name}

# jointPackage_Ecore2Maude_TrgMembership class attributes and methods

# TrgStatement class attributes and methods

# jointPackage_Ecore2Maude_TrgTerm class attributes and methods

# jointPackage_Ecore2Maude_TrgSort class attributes and methods

# jointPackage_Ecore2Maude_TrgEquation class attributes and methods

# jointPackage_Ecore2Maude_TrgRule class attributes and methods

# TrgMaudeTopEl class attributes and methods

# jointPackage_Ecore2Maude_TrgModElement class attributes and methods

# jointPackage_Ecore2Maude_TrgFTheory class attributes and methods

# TrgTheory class attributes and methods

# jointPackage_Ecore2Maude_TrgSTheory class attributes and methods

# jointPackage_Ecore2Maude_TrgModExpression class attributes and methods

# jointPackage_Ecore2Maude_TrgInstModExp class attributes and methods

# TrgModExpression class attributes and methods

# jointPackage_Ecore2Maude_TrgView class attributes and methods

# jointPackage_Ecore2Maude_TrgRenModExp class attributes and methods

# jointPackage_Ecore2Maude_TrgRenMapping class attributes and methods

# jointPackage_Ecore2Maude_TrgCompModExp class attributes and methods

# jointPackage_Ecore2Maude_TrgModuleIdModExp class attributes and methods

# jointPackage_Ecore2Maude_TrgModule class attributes and methods

# jointPackage_Ecore2Maude_TrgTheoryIdModExp class attributes and methods

# jointPackage_Ecore2Maude_TrgTheory class attributes and methods

# jointPackage_Ecore2Maude_TrgParameter class attributes and methods
jointPackage_Ecore2Maude_TrgParameter_label: Property = Property(name="label", type=StringType)
jointPackage_Ecore2Maude_TrgParameter.attributes={jointPackage_Ecore2Maude_TrgParameter_label}

# jointPackage_Ecore2Maude_TrgKind class attributes and methods

# jointPackage_Ecore2Maude_TrgFModule class attributes and methods

# TrgModule class attributes and methods

# jointPackage_Ecore2Maude_TrgSModule class attributes and methods

# jointPackage_Ecore2Maude_TrgModImportation class attributes and methods

# TrgModElement class attributes and methods

# jointPackage_Ecore2Maude_TrgType class attributes and methods
jointPackage_Ecore2Maude_TrgType_name: Property = Property(name="name", type=StringType)
jointPackage_Ecore2Maude_TrgType.attributes={jointPackage_Ecore2Maude_TrgType_name}

# TrgType class attributes and methods

# jointPackage_Ecore2Maude_TrgSubsortRel class attributes and methods

# jointPackage_Ecore2Maude_TrgConstant class attributes and methods
jointPackage_Ecore2Maude_TrgConstant_op: Property = Property(name="op", type=StringType)
jointPackage_Ecore2Maude_TrgConstant.attributes={jointPackage_Ecore2Maude_TrgConstant_op}

# TrgTerm class attributes and methods

# jointPackage_Ecore2Maude_TrgRecTerm class attributes and methods
jointPackage_Ecore2Maude_TrgRecTerm_op: Property = Property(name="op", type=StringType)
jointPackage_Ecore2Maude_TrgRecTerm.attributes={jointPackage_Ecore2Maude_TrgRecTerm_op}

# jointPackage_Ecore2Maude_TrgVariable class attributes and methods
jointPackage_Ecore2Maude_TrgVariable_name: Property = Property(name="name", type=StringType)
jointPackage_Ecore2Maude_TrgVariable.attributes={jointPackage_Ecore2Maude_TrgVariable_name}

# jointPackage_Ecore2Maude_TrgOperation class attributes and methods
jointPackage_Ecore2Maude_TrgOperation_name: Property = Property(name="name", type=StringType)
jointPackage_Ecore2Maude_TrgOperation_atts: Property = Property(name="atts", type=StringType)
jointPackage_Ecore2Maude_TrgOperation.attributes={jointPackage_Ecore2Maude_TrgOperation_name, jointPackage_Ecore2Maude_TrgOperation_atts}

# jointPackage_Ecore2Maude_TrgStatement class attributes and methods
jointPackage_Ecore2Maude_TrgStatement_label: Property = Property(name="label", type=StringType)
jointPackage_Ecore2Maude_TrgStatement_atts: Property = Property(name="atts", type=StringType)
jointPackage_Ecore2Maude_TrgStatement.attributes={jointPackage_Ecore2Maude_TrgStatement_atts, jointPackage_Ecore2Maude_TrgStatement_label}

# jointPackage_Ecore2Maude_TrgCondition class attributes and methods

# jointPackage_Ecore2Maude_TrgEquationalCond class attributes and methods

# TrgCondition class attributes and methods

# jointPackage_Ecore2Maude_TrgRewriteCond class attributes and methods

# jointPackage_Ecore2Maude_TrgOpMapping class attributes and methods
jointPackage_Ecore2Maude_TrgOpMapping_to: Property = Property(name="to", type=StringType)
jointPackage_Ecore2Maude_TrgOpMapping.attributes={jointPackage_Ecore2Maude_TrgOpMapping_to}

# jointPackage_Ecore2Maude_TrgLabelMapping class attributes and methods
jointPackage_Ecore2Maude_TrgLabelMapping_from: Property = Property(name="from", type=StringType)
jointPackage_Ecore2Maude_TrgLabelMapping_to: Property = Property(name="to", type=StringType)
jointPackage_Ecore2Maude_TrgLabelMapping.attributes={jointPackage_Ecore2Maude_TrgLabelMapping_from, jointPackage_Ecore2Maude_TrgLabelMapping_to}

# jointPackage_Ecore2Maude_TrgViewMapping class attributes and methods

# TrgViewMapping class attributes and methods

# jointPackage_Ecore2Maude_TrgTermMapping class attributes and methods

# jointPackage_Ecore2Maude_TrgSortMapping class attributes and methods
jointPackage_Ecore2Maude_TrgSortMapping_to: Property = Property(name="to", type=StringType)
jointPackage_Ecore2Maude_TrgSortMapping.attributes={jointPackage_Ecore2Maude_TrgSortMapping_to}

# TrgRenMapping class attributes and methods

# jointPackage_Ecore2Maude_TrgOpTypedMapping class attributes and methods
jointPackage_Ecore2Maude_TrgOpTypedMapping_to: Property = Property(name="to", type=StringType)
jointPackage_Ecore2Maude_TrgOpTypedMapping_atts: Property = Property(name="atts", type=StringType)
jointPackage_Ecore2Maude_TrgOpTypedMapping.attributes={jointPackage_Ecore2Maude_TrgOpTypedMapping_atts, jointPackage_Ecore2Maude_TrgOpTypedMapping_to}

# Relationships
sourceRoot0: BinaryAssociation = BinaryAssociation(
    name="sourceRoot0",
    ends={
        Property(name="jointPackage_Ecore2Maude_SrcEStringToStringMapEntry", type=jointPackage_Ecore2Maude_JointMM, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_JointMM", type=jointPackage_Ecore2Maude_SrcEStringToStringMapEntry, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetRoot1: BinaryAssociation = BinaryAssociation(
    name="targetRoot1",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgEqualCond", type=jointPackage_Ecore2Maude_JointMM, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_JointMM2", type=jointPackage_Ecore2Maude_TrgEqualCond, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
eStructuralFeatures31: BinaryAssociation = BinaryAssociation(
    name="eStructuralFeatures31",
    ends={
        Property(name="SrcEStructuralFeature", type=jointPackage_Ecore2Maude_SrcEClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass32", type=jointPackage_Ecore2Maude_SrcEStructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSuperTypes5: BinaryAssociation = BinaryAssociation(
    name="eSuperTypes5",
    ends={
        Property(name="jointPackage_Ecore2Maude_SrcEClass", type=jointPackage_Ecore2Maude_SrcEClass, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_SrcEClass4", type=jointPackage_Ecore2Maude_SrcEClass, multiplicity=Multiplicity(0, 9999))
    }
)
eOperations6: BinaryAssociation = BinaryAssociation(
    name="eOperations6",
    ends={
        Property(name="SrcEOperation", type=jointPackage_Ecore2Maude_SrcEClass, multiplicity=Multiplicity(1, 1)),
        Property(name="eContainingClass", type=jointPackage_Ecore2Maude_SrcEOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eAllAttributes7: BinaryAssociation = BinaryAssociation(
    name="eAllAttributes7",
    ends={
        Property(name="jointPackage_Ecore2Maude_SrcEAttribute9", type=jointPackage_Ecore2Maude_SrcEClass, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_SrcEClass8", type=jointPackage_Ecore2Maude_SrcEAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllReferences10: BinaryAssociation = BinaryAssociation(
    name="eAllReferences10",
    ends={
        Property(name="jointPackage_Ecore2Maude_SrcEReference", type=jointPackage_Ecore2Maude_SrcEClass, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_SrcEClass11", type=jointPackage_Ecore2Maude_SrcEReference, multiplicity=Multiplicity(0, 9999))
    }
)
eReferences12: BinaryAssociation = BinaryAssociation(
    name="eReferences12",
    ends={
        Property(name="jointPackage_Ecore2Maude_SrcEReference14", type=jointPackage_Ecore2Maude_SrcEClass, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_SrcEClass13", type=jointPackage_Ecore2Maude_SrcEReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributes15: BinaryAssociation = BinaryAssociation(
    name="eAttributes15",
    ends={
        Property(name="jointPackage_Ecore2Maude_SrcEAttribute17", type=jointPackage_Ecore2Maude_SrcEClass, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_SrcEClass16", type=jointPackage_Ecore2Maude_SrcEAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
eAllContainments18: BinaryAssociation = BinaryAssociation(
    name="eAllContainments18",
    ends={
        Property(name="jointPackage_Ecore2Maude_SrcEReference20", type=jointPackage_Ecore2Maude_SrcEClass, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_SrcEClass19", type=jointPackage_Ecore2Maude_SrcEReference, multiplicity=Multiplicity(0, 9999))
    }
)
eAllOperations21: BinaryAssociation = BinaryAssociation(
    name="eAllOperations21",
    ends={
        Property(name="jointPackage_Ecore2Maude_SrcEOperation", type=jointPackage_Ecore2Maude_SrcEClass, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_SrcEClass22", type=jointPackage_Ecore2Maude_SrcEOperation, multiplicity=Multiplicity(0, 9999))
    }
)
eAttributeType3: BinaryAssociation = BinaryAssociation(
    name="eAttributeType3",
    ends={
        Property(name="jointPackage_Ecore2Maude_SrcEDataType", type=jointPackage_Ecore2Maude_SrcEAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_SrcEAttribute", type=jointPackage_Ecore2Maude_SrcEDataType, multiplicity=Multiplicity(0, 1))
    }
)
eAllStructuralFeatures23: BinaryAssociation = BinaryAssociation(
    name="eAllStructuralFeatures23",
    ends={
        Property(name="jointPackage_Ecore2Maude_SrcEStructuralFeature", type=jointPackage_Ecore2Maude_SrcEClass, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_SrcEClass24", type=jointPackage_Ecore2Maude_SrcEStructuralFeature, multiplicity=Multiplicity(0, 9999))
    }
)
eAllSuperTypes26: BinaryAssociation = BinaryAssociation(
    name="eAllSuperTypes26",
    ends={
        Property(name="jointPackage_Ecore2Maude_SrcEClass27", type=jointPackage_Ecore2Maude_SrcEClass, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_SrcEClass25", type=jointPackage_Ecore2Maude_SrcEClass, multiplicity=Multiplicity(0, 9999))
    }
)
eIDAttribute28: BinaryAssociation = BinaryAssociation(
    name="eIDAttribute28",
    ends={
        Property(name="jointPackage_Ecore2Maude_SrcEAttribute30", type=jointPackage_Ecore2Maude_SrcEClass, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_SrcEClass29", type=jointPackage_Ecore2Maude_SrcEAttribute, multiplicity=Multiplicity(0, 1))
    }
)
eContainingClass36: BinaryAssociation = BinaryAssociation(
    name="eContainingClass36",
    ends={
        Property(name="eOperations", type=jointPackage_Ecore2Maude_SrcEClass, multiplicity=Multiplicity(0, 1)),
        Property(name="SrcEClass", type=jointPackage_Ecore2Maude_SrcEOperation, multiplicity=Multiplicity(1, 1))
    }
)
eParameters37: BinaryAssociation = BinaryAssociation(
    name="eParameters37",
    ends={
        Property(name="SrcEParameter", type=jointPackage_Ecore2Maude_SrcEOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="eOperation", type=jointPackage_Ecore2Maude_SrcEParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eExceptions38: BinaryAssociation = BinaryAssociation(
    name="eExceptions38",
    ends={
        Property(name="jointPackage_Ecore2Maude_SrcEClassifier", type=jointPackage_Ecore2Maude_SrcEOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_SrcEOperation39", type=jointPackage_Ecore2Maude_SrcEClassifier, multiplicity=Multiplicity(0, 9999))
    }
)
ePackage33: BinaryAssociation = BinaryAssociation(
    name="ePackage33",
    ends={
        Property(name="SrcEPackage", type=jointPackage_Ecore2Maude_SrcEClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="eClassifiers", type=jointPackage_Ecore2Maude_SrcEPackage, multiplicity=Multiplicity(0, 1))
    }
)
eLiterals34: BinaryAssociation = BinaryAssociation(
    name="eLiterals34",
    ends={
        Property(name="SrcEEnumLiteral", type=jointPackage_Ecore2Maude_SrcEEnum, multiplicity=Multiplicity(1, 1)),
        Property(name="eEnum", type=jointPackage_Ecore2Maude_SrcEEnumLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eEnum35: BinaryAssociation = BinaryAssociation(
    name="eEnum35",
    ends={
        Property(name="SrcEEnum", type=jointPackage_Ecore2Maude_SrcEEnumLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="eLiterals", type=jointPackage_Ecore2Maude_SrcEEnum, multiplicity=Multiplicity(0, 1))
    }
)
eContainingClass58: BinaryAssociation = BinaryAssociation(
    name="eContainingClass58",
    ends={
        Property(name="SrcEClass59", type=jointPackage_Ecore2Maude_SrcEStructuralFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="eStructuralFeatures", type=jointPackage_Ecore2Maude_SrcEClass, multiplicity=Multiplicity(0, 1))
    }
)
eClassifiers40: BinaryAssociation = BinaryAssociation(
    name="eClassifiers40",
    ends={
        Property(name="SrcEClassifier", type=jointPackage_Ecore2Maude_SrcEPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="ePackage", type=jointPackage_Ecore2Maude_SrcEClassifier, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSubpackages42: BinaryAssociation = BinaryAssociation(
    name="eSubpackages42",
    ends={
        Property(name="SrcEPackage43", type=jointPackage_Ecore2Maude_SrcEPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSuperPackage", type=jointPackage_Ecore2Maude_SrcEPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eSuperPackage45: BinaryAssociation = BinaryAssociation(
    name="eSuperPackage45",
    ends={
        Property(name="SrcEPackage46", type=jointPackage_Ecore2Maude_SrcEPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eSubpackages", type=jointPackage_Ecore2Maude_SrcEPackage, multiplicity=Multiplicity(0, 1))
    }
)
eOperation47: BinaryAssociation = BinaryAssociation(
    name="eOperation47",
    ends={
        Property(name="SrcEOperation48", type=jointPackage_Ecore2Maude_SrcEParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eParameters", type=jointPackage_Ecore2Maude_SrcEOperation, multiplicity=Multiplicity(0, 1))
    }
)
eOpposite50: BinaryAssociation = BinaryAssociation(
    name="eOpposite50",
    ends={
        Property(name="jointPackage_Ecore2Maude_SrcEReference51", type=jointPackage_Ecore2Maude_SrcEReference, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_SrcEReference49", type=jointPackage_Ecore2Maude_SrcEReference, multiplicity=Multiplicity(0, 1))
    }
)
eReferenceType52: BinaryAssociation = BinaryAssociation(
    name="eReferenceType52",
    ends={
        Property(name="jointPackage_Ecore2Maude_SrcEClass54", type=jointPackage_Ecore2Maude_SrcEReference, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_SrcEReference53", type=jointPackage_Ecore2Maude_SrcEClass, multiplicity=Multiplicity(0, 1))
    }
)
eKeys55: BinaryAssociation = BinaryAssociation(
    name="eKeys55",
    ends={
        Property(name="jointPackage_Ecore2Maude_SrcEAttribute57", type=jointPackage_Ecore2Maude_SrcEReference, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_SrcEReference56", type=jointPackage_Ecore2Maude_SrcEAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
rhs76: BinaryAssociation = BinaryAssociation(
    name="rhs76",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgRule77", type=jointPackage_Ecore2Maude_TrgTerm, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="jointPackage_Ecore2Maude_TrgTerm78", type=jointPackage_Ecore2Maude_TrgRule, multiplicity=Multiplicity(1, 1))
    }
)
rhs79: BinaryAssociation = BinaryAssociation(
    name="rhs79",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgSort80", type=jointPackage_Ecore2Maude_TrgMembershipCond, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgMembershipCond", type=jointPackage_Ecore2Maude_TrgSort, multiplicity=Multiplicity(1, 1))
    }
)
rhs81: BinaryAssociation = BinaryAssociation(
    name="rhs81",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgTerm82", type=jointPackage_Ecore2Maude_TrgMatchingCond, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgMatchingCond", type=jointPackage_Ecore2Maude_TrgTerm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs83: BinaryAssociation = BinaryAssociation(
    name="rhs83",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgTerm85", type=jointPackage_Ecore2Maude_TrgEqualCond, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgEqualCond84", type=jointPackage_Ecore2Maude_TrgTerm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
eType60: BinaryAssociation = BinaryAssociation(
    name="eType60",
    ends={
        Property(name="jointPackage_Ecore2Maude_SrcEClassifier61", type=jointPackage_Ecore2Maude_SrcETypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_SrcETypedElement", type=jointPackage_Ecore2Maude_SrcEClassifier, multiplicity=Multiplicity(0, 1))
    }
)
els62: BinaryAssociation = BinaryAssociation(
    name="els62",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgMaudeTopEl", type=jointPackage_Ecore2Maude_TrgMaudeSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgMaudeSpec", type=jointPackage_Ecore2Maude_TrgMaudeTopEl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
printableEls63: BinaryAssociation = BinaryAssociation(
    name="printableEls63",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgMaudeTopEl65", type=jointPackage_Ecore2Maude_TrgMaudeSpec, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgMaudeSpec64", type=jointPackage_Ecore2Maude_TrgMaudeTopEl, multiplicity=Multiplicity(0, 9999))
    }
)
term66: BinaryAssociation = BinaryAssociation(
    name="term66",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgTerm", type=jointPackage_Ecore2Maude_TrgMembership, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgMembership", type=jointPackage_Ecore2Maude_TrgTerm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sort67: BinaryAssociation = BinaryAssociation(
    name="sort67",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgSort", type=jointPackage_Ecore2Maude_TrgMembership, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgMembership68", type=jointPackage_Ecore2Maude_TrgSort, multiplicity=Multiplicity(1, 1))
    }
)
lhs69: BinaryAssociation = BinaryAssociation(
    name="lhs69",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgTerm70", type=jointPackage_Ecore2Maude_TrgEquation, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgEquation", type=jointPackage_Ecore2Maude_TrgTerm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs71: BinaryAssociation = BinaryAssociation(
    name="rhs71",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgTerm73", type=jointPackage_Ecore2Maude_TrgEquation, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgEquation72", type=jointPackage_Ecore2Maude_TrgTerm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs74: BinaryAssociation = BinaryAssociation(
    name="lhs74",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgTerm75", type=jointPackage_Ecore2Maude_TrgRule, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgRule", type=jointPackage_Ecore2Maude_TrgTerm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modExp97: BinaryAssociation = BinaryAssociation(
    name="modExp97",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgModExpression98", type=jointPackage_Ecore2Maude_TrgParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgParameter", type=jointPackage_Ecore2Maude_TrgModExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
els99: BinaryAssociation = BinaryAssociation(
    name="els99",
    ends={
        Property(name="TrgModElement", type=jointPackage_Ecore2Maude_TrgTheory, multiplicity=Multiplicity(1, 1)),
        Property(name="theory", type=jointPackage_Ecore2Maude_TrgModElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modExp86: BinaryAssociation = BinaryAssociation(
    name="modExp86",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgModExpression", type=jointPackage_Ecore2Maude_TrgInstModExp, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgInstModExp", type=jointPackage_Ecore2Maude_TrgModExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
views87: BinaryAssociation = BinaryAssociation(
    name="views87",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgView", type=jointPackage_Ecore2Maude_TrgInstModExp, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgInstModExp88", type=jointPackage_Ecore2Maude_TrgView, multiplicity=Multiplicity(1, 9999))
    }
)
modExp89: BinaryAssociation = BinaryAssociation(
    name="modExp89",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgModExpression90", type=jointPackage_Ecore2Maude_TrgRenModExp, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgRenModExp", type=jointPackage_Ecore2Maude_TrgModExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
renamings91: BinaryAssociation = BinaryAssociation(
    name="renamings91",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgRenMapping", type=jointPackage_Ecore2Maude_TrgRenModExp, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgRenModExp92", type=jointPackage_Ecore2Maude_TrgRenMapping, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
modExps93: BinaryAssociation = BinaryAssociation(
    name="modExps93",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgModExpression94", type=jointPackage_Ecore2Maude_TrgCompModExp, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgCompModExp", type=jointPackage_Ecore2Maude_TrgModExpression, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
module95: BinaryAssociation = BinaryAssociation(
    name="module95",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgModule", type=jointPackage_Ecore2Maude_TrgModuleIdModExp, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgModuleIdModExp", type=jointPackage_Ecore2Maude_TrgModule, multiplicity=Multiplicity(1, 1))
    }
)
supersortRels111: BinaryAssociation = BinaryAssociation(
    name="supersortRels111",
    ends={
        Property(name="TrgSubsortRel112", type=jointPackage_Ecore2Maude_TrgSort, multiplicity=Multiplicity(1, 1)),
        Property(name="subsorts", type=jointPackage_Ecore2Maude_TrgSubsortRel, multiplicity=Multiplicity(0, 9999))
    }
)
theory96: BinaryAssociation = BinaryAssociation(
    name="theory96",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgTheory", type=jointPackage_Ecore2Maude_TrgTheoryIdModExp, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgTheoryIdModExp", type=jointPackage_Ecore2Maude_TrgTheory, multiplicity=Multiplicity(1, 1))
    }
)
kind113: BinaryAssociation = BinaryAssociation(
    name="kind113",
    ends={
        Property(name="TrgKind", type=jointPackage_Ecore2Maude_TrgSort, multiplicity=Multiplicity(1, 1)),
        Property(name="sorts", type=jointPackage_Ecore2Maude_TrgKind, multiplicity=Multiplicity(1, 1))
    }
)
sorts114: BinaryAssociation = BinaryAssociation(
    name="sorts114",
    ends={
        Property(name="TrgSort", type=jointPackage_Ecore2Maude_TrgKind, multiplicity=Multiplicity(1, 1)),
        Property(name="kind", type=jointPackage_Ecore2Maude_TrgSort, multiplicity=Multiplicity(1, 9999))
    }
)
subsorts115: BinaryAssociation = BinaryAssociation(
    name="subsorts115",
    ends={
        Property(name="TrgSort116", type=jointPackage_Ecore2Maude_TrgSubsortRel, multiplicity=Multiplicity(1, 1)),
        Property(name="supersortRels", type=jointPackage_Ecore2Maude_TrgSort, multiplicity=Multiplicity(1, 9999))
    }
)
els100: BinaryAssociation = BinaryAssociation(
    name="els100",
    ends={
        Property(name="TrgModElement101", type=jointPackage_Ecore2Maude_TrgModule, multiplicity=Multiplicity(1, 1)),
        Property(name="module", type=jointPackage_Ecore2Maude_TrgModElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
params102: BinaryAssociation = BinaryAssociation(
    name="params102",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgParameter104", type=jointPackage_Ecore2Maude_TrgModule, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgModule103", type=jointPackage_Ecore2Maude_TrgParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module105: BinaryAssociation = BinaryAssociation(
    name="module105",
    ends={
        Property(name="TrgModule", type=jointPackage_Ecore2Maude_TrgModElement, multiplicity=Multiplicity(1, 1)),
        Property(name="els", type=jointPackage_Ecore2Maude_TrgModule, multiplicity=Multiplicity(0, 1))
    }
)
theory106: BinaryAssociation = BinaryAssociation(
    name="theory106",
    ends={
        Property(name="TrgTheory", type=jointPackage_Ecore2Maude_TrgModElement, multiplicity=Multiplicity(1, 1)),
        Property(name="els107", type=jointPackage_Ecore2Maude_TrgTheory, multiplicity=Multiplicity(0, 1))
    }
)
imports108: BinaryAssociation = BinaryAssociation(
    name="imports108",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgModExpression109", type=jointPackage_Ecore2Maude_TrgModImportation, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgModImportation", type=jointPackage_Ecore2Maude_TrgModExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subsortRels110: BinaryAssociation = BinaryAssociation(
    name="subsortRels110",
    ends={
        Property(name="TrgSubsortRel", type=jointPackage_Ecore2Maude_TrgSort, multiplicity=Multiplicity(1, 1)),
        Property(name="supersorts", type=jointPackage_Ecore2Maude_TrgSubsortRel, multiplicity=Multiplicity(0, 9999))
    }
)
type129: BinaryAssociation = BinaryAssociation(
    name="type129",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgType131", type=jointPackage_Ecore2Maude_TrgTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgTerm130", type=jointPackage_Ecore2Maude_TrgType, multiplicity=Multiplicity(1, 1))
    }
)
args132: BinaryAssociation = BinaryAssociation(
    name="args132",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgTerm133", type=jointPackage_Ecore2Maude_TrgRecTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgRecTerm", type=jointPackage_Ecore2Maude_TrgTerm, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
supersorts117: BinaryAssociation = BinaryAssociation(
    name="supersorts117",
    ends={
        Property(name="TrgSort118", type=jointPackage_Ecore2Maude_TrgSubsortRel, multiplicity=Multiplicity(1, 1)),
        Property(name="subsortRels", type=jointPackage_Ecore2Maude_TrgSort, multiplicity=Multiplicity(1, 9999))
    }
)
coarity119: BinaryAssociation = BinaryAssociation(
    name="coarity119",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgType", type=jointPackage_Ecore2Maude_TrgOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgOperation", type=jointPackage_Ecore2Maude_TrgType, multiplicity=Multiplicity(0, 1))
    }
)
arity120: BinaryAssociation = BinaryAssociation(
    name="arity120",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgType122", type=jointPackage_Ecore2Maude_TrgOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgOperation121", type=jointPackage_Ecore2Maude_TrgType, multiplicity=Multiplicity(0, 9999))
    }
)
conds123: BinaryAssociation = BinaryAssociation(
    name="conds123",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgCondition", type=jointPackage_Ecore2Maude_TrgStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgStatement", type=jointPackage_Ecore2Maude_TrgCondition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs124: BinaryAssociation = BinaryAssociation(
    name="lhs124",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgTerm126", type=jointPackage_Ecore2Maude_TrgCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgCondition125", type=jointPackage_Ecore2Maude_TrgTerm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs127: BinaryAssociation = BinaryAssociation(
    name="rhs127",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgTerm128", type=jointPackage_Ecore2Maude_TrgRewriteCond, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgRewriteCond", type=jointPackage_Ecore2Maude_TrgTerm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
from151: BinaryAssociation = BinaryAssociation(
    name="from151",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgOperation152", type=jointPackage_Ecore2Maude_TrgOpMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgOpMapping", type=jointPackage_Ecore2Maude_TrgOperation, multiplicity=Multiplicity(1, 1))
    }
)
from134: BinaryAssociation = BinaryAssociation(
    name="from134",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgModExpression136", type=jointPackage_Ecore2Maude_TrgView, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgView135", type=jointPackage_Ecore2Maude_TrgModExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
to137: BinaryAssociation = BinaryAssociation(
    name="to137",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgModExpression139", type=jointPackage_Ecore2Maude_TrgView, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgView138", type=jointPackage_Ecore2Maude_TrgModExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
els140: BinaryAssociation = BinaryAssociation(
    name="els140",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgViewMapping", type=jointPackage_Ecore2Maude_TrgView, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgView141", type=jointPackage_Ecore2Maude_TrgViewMapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from142: BinaryAssociation = BinaryAssociation(
    name="from142",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgTerm143", type=jointPackage_Ecore2Maude_TrgTermMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgTermMapping", type=jointPackage_Ecore2Maude_TrgTerm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
to144: BinaryAssociation = BinaryAssociation(
    name="to144",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgTerm146", type=jointPackage_Ecore2Maude_TrgTermMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgTermMapping145", type=jointPackage_Ecore2Maude_TrgTerm, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
from147: BinaryAssociation = BinaryAssociation(
    name="from147",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgSort148", type=jointPackage_Ecore2Maude_TrgSortMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgSortMapping", type=jointPackage_Ecore2Maude_TrgSort, multiplicity=Multiplicity(1, 1))
    }
)
from149: BinaryAssociation = BinaryAssociation(
    name="from149",
    ends={
        Property(name="jointPackage_Ecore2Maude_TrgOperation150", type=jointPackage_Ecore2Maude_TrgOpTypedMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="jointPackage_Ecore2Maude_TrgOpTypedMapping", type=jointPackage_Ecore2Maude_TrgOperation, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_jointPackage_Ecore2Maude_SrcEAttribute_SrcEStructuralFeature = Generalization(general=SrcEStructuralFeature, specific=jointPackage_Ecore2Maude_SrcEAttribute)
gen_jointPackage_Ecore2Maude_SrcEClassifier_SrcENamedElement = Generalization(general=SrcENamedElement, specific=jointPackage_Ecore2Maude_SrcEClassifier)
gen_jointPackage_Ecore2Maude_SrcEClass_SrcEClassifier = Generalization(general=SrcEClassifier, specific=jointPackage_Ecore2Maude_SrcEClass)
gen_jointPackage_Ecore2Maude_SrcEPackage_SrcENamedElement = Generalization(general=SrcENamedElement, specific=jointPackage_Ecore2Maude_SrcEPackage)
gen_jointPackage_Ecore2Maude_SrcEDataType_SrcEClassifier = Generalization(general=SrcEClassifier, specific=jointPackage_Ecore2Maude_SrcEDataType)
gen_jointPackage_Ecore2Maude_SrcEEnum_SrcEDataType = Generalization(general=SrcEDataType, specific=jointPackage_Ecore2Maude_SrcEEnum)
gen_jointPackage_Ecore2Maude_SrcEEnumLiteral_SrcENamedElement = Generalization(general=SrcENamedElement, specific=jointPackage_Ecore2Maude_SrcEEnumLiteral)
gen_jointPackage_Ecore2Maude_SrcEOperation_SrcETypedElement = Generalization(general=SrcETypedElement, specific=jointPackage_Ecore2Maude_SrcEOperation)
gen_jointPackage_Ecore2Maude_SrcETypedElement_SrcENamedElement = Generalization(general=SrcENamedElement, specific=jointPackage_Ecore2Maude_SrcETypedElement)
gen_jointPackage_Ecore2Maude_SrcEParameter_SrcETypedElement = Generalization(general=SrcETypedElement, specific=jointPackage_Ecore2Maude_SrcEParameter)
gen_jointPackage_Ecore2Maude_SrcEReference_SrcEStructuralFeature = Generalization(general=SrcEStructuralFeature, specific=jointPackage_Ecore2Maude_SrcEReference)
gen_jointPackage_Ecore2Maude_SrcEStructuralFeature_SrcETypedElement = Generalization(general=SrcETypedElement, specific=jointPackage_Ecore2Maude_SrcEStructuralFeature)
gen_jointPackage_Ecore2Maude_TrgMembershipCond_TrgEquationalCond = Generalization(general=TrgEquationalCond, specific=jointPackage_Ecore2Maude_TrgMembershipCond)
gen_jointPackage_Ecore2Maude_TrgBooleanCond_TrgEquationalCond = Generalization(general=TrgEquationalCond, specific=jointPackage_Ecore2Maude_TrgBooleanCond)
gen_jointPackage_Ecore2Maude_TrgMatchingCond_TrgEquationalCond = Generalization(general=TrgEquationalCond, specific=jointPackage_Ecore2Maude_TrgMatchingCond)
gen_jointPackage_Ecore2Maude_TrgEqualCond_TrgEquationalCond = Generalization(general=TrgEquationalCond, specific=jointPackage_Ecore2Maude_TrgEqualCond)
gen_jointPackage_Ecore2Maude_TrgMembership_TrgStatement = Generalization(general=TrgStatement, specific=jointPackage_Ecore2Maude_TrgMembership)
gen_jointPackage_Ecore2Maude_TrgEquation_TrgStatement = Generalization(general=TrgStatement, specific=jointPackage_Ecore2Maude_TrgEquation)
gen_jointPackage_Ecore2Maude_TrgRule_TrgStatement = Generalization(general=TrgStatement, specific=jointPackage_Ecore2Maude_TrgRule)
gen_jointPackage_Ecore2Maude_TrgTheory_TrgMaudeTopEl = Generalization(general=TrgMaudeTopEl, specific=jointPackage_Ecore2Maude_TrgTheory)
gen_jointPackage_Ecore2Maude_TrgFTheory_TrgTheory = Generalization(general=TrgTheory, specific=jointPackage_Ecore2Maude_TrgFTheory)
gen_jointPackage_Ecore2Maude_TrgSTheory_TrgTheory = Generalization(general=TrgTheory, specific=jointPackage_Ecore2Maude_TrgSTheory)
gen_jointPackage_Ecore2Maude_TrgModule_TrgMaudeTopEl = Generalization(general=TrgMaudeTopEl, specific=jointPackage_Ecore2Maude_TrgModule)
gen_jointPackage_Ecore2Maude_TrgInstModExp_TrgModExpression = Generalization(general=TrgModExpression, specific=jointPackage_Ecore2Maude_TrgInstModExp)
gen_jointPackage_Ecore2Maude_TrgRenModExp_TrgModExpression = Generalization(general=TrgModExpression, specific=jointPackage_Ecore2Maude_TrgRenModExp)
gen_jointPackage_Ecore2Maude_TrgCompModExp_TrgModExpression = Generalization(general=TrgModExpression, specific=jointPackage_Ecore2Maude_TrgCompModExp)
gen_jointPackage_Ecore2Maude_TrgModuleIdModExp_TrgModExpression = Generalization(general=TrgModExpression, specific=jointPackage_Ecore2Maude_TrgModuleIdModExp)
gen_jointPackage_Ecore2Maude_TrgTheoryIdModExp_TrgModExpression = Generalization(general=TrgModExpression, specific=jointPackage_Ecore2Maude_TrgTheoryIdModExp)
gen_jointPackage_Ecore2Maude_TrgParameter_TrgModExpression = Generalization(general=TrgModExpression, specific=jointPackage_Ecore2Maude_TrgParameter)
gen_jointPackage_Ecore2Maude_TrgKind_TrgType = Generalization(general=TrgType, specific=jointPackage_Ecore2Maude_TrgKind)
gen_jointPackage_Ecore2Maude_TrgSubsortRel_TrgModElement = Generalization(general=TrgModElement, specific=jointPackage_Ecore2Maude_TrgSubsortRel)
gen_jointPackage_Ecore2Maude_TrgFModule_TrgModule = Generalization(general=TrgModule, specific=jointPackage_Ecore2Maude_TrgFModule)
gen_jointPackage_Ecore2Maude_TrgSModule_TrgModule = Generalization(general=TrgModule, specific=jointPackage_Ecore2Maude_TrgSModule)
gen_jointPackage_Ecore2Maude_TrgModImportation_TrgModElement = Generalization(general=TrgModElement, specific=jointPackage_Ecore2Maude_TrgModImportation)
gen_jointPackage_Ecore2Maude_TrgSort_TrgType = Generalization(general=TrgType, specific=jointPackage_Ecore2Maude_TrgSort)
gen_jointPackage_Ecore2Maude_TrgSort_TrgModElement = Generalization(general=TrgModElement, specific=jointPackage_Ecore2Maude_TrgSort)
gen_jointPackage_Ecore2Maude_TrgConstant_TrgTerm = Generalization(general=TrgTerm, specific=jointPackage_Ecore2Maude_TrgConstant)
gen_jointPackage_Ecore2Maude_TrgRecTerm_TrgTerm = Generalization(general=TrgTerm, specific=jointPackage_Ecore2Maude_TrgRecTerm)
gen_jointPackage_Ecore2Maude_TrgVariable_TrgTerm = Generalization(general=TrgTerm, specific=jointPackage_Ecore2Maude_TrgVariable)
gen_jointPackage_Ecore2Maude_TrgOperation_TrgModElement = Generalization(general=TrgModElement, specific=jointPackage_Ecore2Maude_TrgOperation)
gen_jointPackage_Ecore2Maude_TrgStatement_TrgModElement = Generalization(general=TrgModElement, specific=jointPackage_Ecore2Maude_TrgStatement)
gen_jointPackage_Ecore2Maude_TrgEquationalCond_TrgCondition = Generalization(general=TrgCondition, specific=jointPackage_Ecore2Maude_TrgEquationalCond)
gen_jointPackage_Ecore2Maude_TrgRewriteCond_TrgCondition = Generalization(general=TrgCondition, specific=jointPackage_Ecore2Maude_TrgRewriteCond)
gen_jointPackage_Ecore2Maude_TrgOpMapping_TrgRenMapping = Generalization(general=TrgRenMapping, specific=jointPackage_Ecore2Maude_TrgOpMapping)
gen_jointPackage_Ecore2Maude_TrgLabelMapping_TrgRenMapping = Generalization(general=TrgRenMapping, specific=jointPackage_Ecore2Maude_TrgLabelMapping)
gen_jointPackage_Ecore2Maude_TrgView_TrgMaudeTopEl = Generalization(general=TrgMaudeTopEl, specific=jointPackage_Ecore2Maude_TrgView)
gen_jointPackage_Ecore2Maude_TrgRenMapping_TrgViewMapping = Generalization(general=TrgViewMapping, specific=jointPackage_Ecore2Maude_TrgRenMapping)
gen_jointPackage_Ecore2Maude_TrgTermMapping_TrgViewMapping = Generalization(general=TrgViewMapping, specific=jointPackage_Ecore2Maude_TrgTermMapping)
gen_jointPackage_Ecore2Maude_TrgSortMapping_TrgRenMapping = Generalization(general=TrgRenMapping, specific=jointPackage_Ecore2Maude_TrgSortMapping)
gen_jointPackage_Ecore2Maude_TrgOpTypedMapping_TrgRenMapping = Generalization(general=TrgRenMapping, specific=jointPackage_Ecore2Maude_TrgOpTypedMapping)

# Domain Model
domain_model = DomainModel(
    name="jointPackage_Ecore2Maude",
    types={jointPackage_Ecore2Maude_JointMM, jointPackage_Ecore2Maude_SrcEStringToStringMapEntry, jointPackage_Ecore2Maude_TrgEqualCond, jointPackage_Ecore2Maude_SrcEAttribute, SrcEStructuralFeature, jointPackage_Ecore2Maude_SrcEDataType, jointPackage_Ecore2Maude_SrcEClassifier, SrcENamedElement, jointPackage_Ecore2Maude_SrcEOperation, jointPackage_Ecore2Maude_SrcEReference, jointPackage_Ecore2Maude_SrcEStructuralFeature, jointPackage_Ecore2Maude_SrcEClass, SrcEClassifier, jointPackage_Ecore2Maude_SrcEParameter, jointPackage_Ecore2Maude_SrcEPackage, jointPackage_Ecore2Maude_SrcEEnum, SrcEDataType, jointPackage_Ecore2Maude_SrcEEnumLiteral, jointPackage_Ecore2Maude_SrcENamedElement, SrcETypedElement, jointPackage_Ecore2Maude_SrcETypedElement, jointPackage_Ecore2Maude_TrgMembershipCond, TrgEquationalCond, jointPackage_Ecore2Maude_TrgBooleanCond, jointPackage_Ecore2Maude_TrgMatchingCond, jointPackage_Ecore2Maude_TrgMaudeSpec, jointPackage_Ecore2Maude_TrgMaudeTopEl, jointPackage_Ecore2Maude_TrgMembership, TrgStatement, jointPackage_Ecore2Maude_TrgTerm, jointPackage_Ecore2Maude_TrgSort, jointPackage_Ecore2Maude_TrgEquation, jointPackage_Ecore2Maude_TrgRule, TrgMaudeTopEl, jointPackage_Ecore2Maude_TrgModElement, jointPackage_Ecore2Maude_TrgFTheory, TrgTheory, jointPackage_Ecore2Maude_TrgSTheory, jointPackage_Ecore2Maude_TrgModExpression, jointPackage_Ecore2Maude_TrgInstModExp, TrgModExpression, jointPackage_Ecore2Maude_TrgView, jointPackage_Ecore2Maude_TrgRenModExp, jointPackage_Ecore2Maude_TrgRenMapping, jointPackage_Ecore2Maude_TrgCompModExp, jointPackage_Ecore2Maude_TrgModuleIdModExp, jointPackage_Ecore2Maude_TrgModule, jointPackage_Ecore2Maude_TrgTheoryIdModExp, jointPackage_Ecore2Maude_TrgTheory, jointPackage_Ecore2Maude_TrgParameter, jointPackage_Ecore2Maude_TrgKind, jointPackage_Ecore2Maude_TrgFModule, TrgModule, jointPackage_Ecore2Maude_TrgSModule, jointPackage_Ecore2Maude_TrgModImportation, TrgModElement, jointPackage_Ecore2Maude_TrgType, TrgType, jointPackage_Ecore2Maude_TrgSubsortRel, jointPackage_Ecore2Maude_TrgConstant, TrgTerm, jointPackage_Ecore2Maude_TrgRecTerm, jointPackage_Ecore2Maude_TrgVariable, jointPackage_Ecore2Maude_TrgOperation, jointPackage_Ecore2Maude_TrgStatement, jointPackage_Ecore2Maude_TrgCondition, jointPackage_Ecore2Maude_TrgEquationalCond, TrgCondition, jointPackage_Ecore2Maude_TrgRewriteCond, jointPackage_Ecore2Maude_TrgOpMapping, jointPackage_Ecore2Maude_TrgLabelMapping, jointPackage_Ecore2Maude_TrgViewMapping, TrgViewMapping, jointPackage_Ecore2Maude_TrgTermMapping, jointPackage_Ecore2Maude_TrgSortMapping, TrgRenMapping, jointPackage_Ecore2Maude_TrgOpTypedMapping},
    associations={sourceRoot0, targetRoot1, eStructuralFeatures31, eSuperTypes5, eOperations6, eAllAttributes7, eAllReferences10, eReferences12, eAttributes15, eAllContainments18, eAllOperations21, eAttributeType3, eAllStructuralFeatures23, eAllSuperTypes26, eIDAttribute28, eContainingClass36, eParameters37, eExceptions38, ePackage33, eLiterals34, eEnum35, eContainingClass58, eClassifiers40, eSubpackages42, eSuperPackage45, eOperation47, eOpposite50, eReferenceType52, eKeys55, rhs76, rhs79, rhs81, rhs83, eType60, els62, printableEls63, term66, sort67, lhs69, rhs71, lhs74, modExp97, els99, modExp86, views87, modExp89, renamings91, modExps93, module95, supersortRels111, theory96, kind113, sorts114, subsorts115, els100, params102, module105, theory106, imports108, subsortRels110, type129, args132, supersorts117, coarity119, arity120, conds123, lhs124, rhs127, from151, from134, to137, els140, from142, to144, from147, from149},
    generalizations={gen_jointPackage_Ecore2Maude_SrcEAttribute_SrcEStructuralFeature, gen_jointPackage_Ecore2Maude_SrcEClassifier_SrcENamedElement, gen_jointPackage_Ecore2Maude_SrcEClass_SrcEClassifier, gen_jointPackage_Ecore2Maude_SrcEPackage_SrcENamedElement, gen_jointPackage_Ecore2Maude_SrcEDataType_SrcEClassifier, gen_jointPackage_Ecore2Maude_SrcEEnum_SrcEDataType, gen_jointPackage_Ecore2Maude_SrcEEnumLiteral_SrcENamedElement, gen_jointPackage_Ecore2Maude_SrcEOperation_SrcETypedElement, gen_jointPackage_Ecore2Maude_SrcETypedElement_SrcENamedElement, gen_jointPackage_Ecore2Maude_SrcEParameter_SrcETypedElement, gen_jointPackage_Ecore2Maude_SrcEReference_SrcEStructuralFeature, gen_jointPackage_Ecore2Maude_SrcEStructuralFeature_SrcETypedElement, gen_jointPackage_Ecore2Maude_TrgMembershipCond_TrgEquationalCond, gen_jointPackage_Ecore2Maude_TrgBooleanCond_TrgEquationalCond, gen_jointPackage_Ecore2Maude_TrgMatchingCond_TrgEquationalCond, gen_jointPackage_Ecore2Maude_TrgEqualCond_TrgEquationalCond, gen_jointPackage_Ecore2Maude_TrgMembership_TrgStatement, gen_jointPackage_Ecore2Maude_TrgEquation_TrgStatement, gen_jointPackage_Ecore2Maude_TrgRule_TrgStatement, gen_jointPackage_Ecore2Maude_TrgTheory_TrgMaudeTopEl, gen_jointPackage_Ecore2Maude_TrgFTheory_TrgTheory, gen_jointPackage_Ecore2Maude_TrgSTheory_TrgTheory, gen_jointPackage_Ecore2Maude_TrgModule_TrgMaudeTopEl, gen_jointPackage_Ecore2Maude_TrgInstModExp_TrgModExpression, gen_jointPackage_Ecore2Maude_TrgRenModExp_TrgModExpression, gen_jointPackage_Ecore2Maude_TrgCompModExp_TrgModExpression, gen_jointPackage_Ecore2Maude_TrgModuleIdModExp_TrgModExpression, gen_jointPackage_Ecore2Maude_TrgTheoryIdModExp_TrgModExpression, gen_jointPackage_Ecore2Maude_TrgParameter_TrgModExpression, gen_jointPackage_Ecore2Maude_TrgKind_TrgType, gen_jointPackage_Ecore2Maude_TrgSubsortRel_TrgModElement, gen_jointPackage_Ecore2Maude_TrgFModule_TrgModule, gen_jointPackage_Ecore2Maude_TrgSModule_TrgModule, gen_jointPackage_Ecore2Maude_TrgModImportation_TrgModElement, gen_jointPackage_Ecore2Maude_TrgSort_TrgType, gen_jointPackage_Ecore2Maude_TrgSort_TrgModElement, gen_jointPackage_Ecore2Maude_TrgConstant_TrgTerm, gen_jointPackage_Ecore2Maude_TrgRecTerm_TrgTerm, gen_jointPackage_Ecore2Maude_TrgVariable_TrgTerm, gen_jointPackage_Ecore2Maude_TrgOperation_TrgModElement, gen_jointPackage_Ecore2Maude_TrgStatement_TrgModElement, gen_jointPackage_Ecore2Maude_TrgEquationalCond_TrgCondition, gen_jointPackage_Ecore2Maude_TrgRewriteCond_TrgCondition, gen_jointPackage_Ecore2Maude_TrgOpMapping_TrgRenMapping, gen_jointPackage_Ecore2Maude_TrgLabelMapping_TrgRenMapping, gen_jointPackage_Ecore2Maude_TrgView_TrgMaudeTopEl, gen_jointPackage_Ecore2Maude_TrgRenMapping_TrgViewMapping, gen_jointPackage_Ecore2Maude_TrgTermMapping_TrgViewMapping, gen_jointPackage_Ecore2Maude_TrgSortMapping_TrgRenMapping, gen_jointPackage_Ecore2Maude_TrgOpTypedMapping_TrgRenMapping},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)