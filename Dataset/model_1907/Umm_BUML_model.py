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
ConstraintKind: Enumeration = Enumeration(
    name="ConstraintKind",
    literals={
            EnumerationLiteral(name="facet"),
			EnumerationLiteral(name="payload"),
			EnumerationLiteral(name="document"),
			EnumerationLiteral(name="invariant"),
			EnumerationLiteral(name="abie"),
			EnumerationLiteral(name="bdt"),
			EnumerationLiteral(name="dependency")
    }
)

MultiplicityKind: Enumeration = Enumeration(
    name="MultiplicityKind",
    literals={
            EnumerationLiteral(name="Optional"),
			EnumerationLiteral(name="One"),
			EnumerationLiteral(name="OneOrMore"),
			EnumerationLiteral(name="ZeroOrMore")
    }
)

# Classes
umm_BIELibrary = Class(name="umm_BIELibrary")
umm_BDTLibrary = Class(name="umm_BDTLibrary")
umm_InfEnvelope = Class(name="umm_InfEnvelope")
umm_MA = Class(name="umm_MA")
ContextRef = Class(name="ContextRef")
umm_MAProperty = Class(name="umm_MAProperty")
umm_Constraint = Class(name="umm_Constraint")
umm_Library = Class(name="umm_Library")
umm_DocLibrary = Class(name="umm_DocLibrary")
Library = Class(name="Library")
OclRef = Class(name="OclRef")
umm_ABIEProperty = Class(name="umm_ABIEProperty")
umm_ABIE = Class(name="umm_ABIE")
umm_ASMA = Class(name="umm_ASMA")
MAProperty = Class(name="MAProperty")
umm_ASNONE = Class(name="umm_ASNONE")
umm_ContextRef = Class(name="umm_ContextRef")
umm_TC_Constraint = Class(name="umm_TC_Constraint")
umm_OclInvariant = Class(name="umm_OclInvariant")
umm_ASBIE = Class(name="umm_ASBIE")
ABIEProperty = Class(name="ABIEProperty")
umm_BBIE = Class(name="umm_BBIE")
umm_ENUMLibrary = Class(name="umm_ENUMLibrary")
umm_BDT = Class(name="umm_BDT")
umm_ENUM = Class(name="umm_ENUM")
ENUM = Class(name="ENUM")
umm_Primitive = Class(name="umm_Primitive")
AssembledBase = Class(name="AssembledBase")
umm_BDTProperty = Class(name="umm_BDTProperty")
umm_Assembled = Class(name="umm_Assembled")
umm_Original = Class(name="umm_Original")
umm_AssembledBase = Class(name="umm_AssembledBase")
umm_Content = Class(name="umm_Content")
BDTProperty = Class(name="BDTProperty")
umm_Supplement = Class(name="umm_Supplement")
umm_ACC = Class(name="umm_ACC")
umm_ACCProperty = Class(name="umm_ACCProperty")
umm_ASCC = Class(name="umm_ASCC")
ACCProperty = Class(name="ACCProperty")
umm_Subset = Class(name="umm_Subset")
umm_CodelistEntry = Class(name="umm_CodelistEntry")
umm_CCLibrary = Class(name="umm_CCLibrary")
umm_CDTLibrary = Class(name="umm_CDTLibrary")
umm_BCC = Class(name="umm_BCC")
umm_CDT = Class(name="umm_CDT")
umm_PrimitiveLibrary = Class(name="umm_PrimitiveLibrary")
umm_OclExpression = Class(name="umm_OclExpression")
umm_OclValue = Class(name="umm_OclValue")
OclExpression = Class(name="OclExpression")
umm_OclReference = Class(name="umm_OclReference")
OclValue = Class(name="OclValue")
umm_OclPathSelfHead = Class(name="umm_OclPathSelfHead")
OclReference = Class(name="OclReference")
umm_OclPathTail = Class(name="umm_OclPathTail")
umm_OclPathFeatureHead = Class(name="umm_OclPathFeatureHead")
umm_OclRef = Class(name="umm_OclRef")
umm_CDTProperty = Class(name="umm_CDTProperty")
umm_CDT_Content = Class(name="umm_CDT_Content")
CDTProperty = Class(name="CDTProperty")
umm_CDT_Supplement = Class(name="umm_CDT_Supplement")
umm_OclBooleanFalse = Class(name="umm_OclBooleanFalse")
OclBooleanLiteral = Class(name="OclBooleanLiteral")
umm_OclImplies = Class(name="umm_OclImplies")
umm_OclAnd = Class(name="umm_OclAnd")
umm_OclOr = Class(name="umm_OclOr")
umm_OclXor = Class(name="umm_OclXor")
umm_OclEqual = Class(name="umm_OclEqual")
umm_OclFunctionCall = Class(name="umm_OclFunctionCall")
umm_OclForAll = Class(name="umm_OclForAll")
OclFunctionCall = Class(name="OclFunctionCall")
umm_OclIsEmpty = Class(name="umm_OclIsEmpty")
umm_OclNotEmpty = Class(name="umm_OclNotEmpty")
umm_OclSize = Class(name="umm_OclSize")
umm_OclLiteral = Class(name="umm_OclLiteral")
umm_OclEnumerationLiteral = Class(name="umm_OclEnumerationLiteral")
OclLiteral = Class(name="OclLiteral")
umm_OclIntegerLiteral = Class(name="umm_OclIntegerLiteral")
umm_OclStringLiteral = Class(name="umm_OclStringLiteral")
umm_OclBooleanLiteral = Class(name="umm_OclBooleanLiteral")
umm_OclArrow = Class(name="umm_OclArrow")
umm_OclBooleanTrue = Class(name="umm_OclBooleanTrue")
umm_OclLess = Class(name="umm_OclLess")
umm_OclLessOrEqual = Class(name="umm_OclLessOrEqual")
umm_OclMore = Class(name="umm_OclMore")
umm_OclMoreOrEqual = Class(name="umm_OclMoreOrEqual")

# umm_BIELibrary class attributes and methods
umm_BIELibrary_businessTerm: Property = Property(name="businessTerm", type=StringType)
umm_BIELibrary_copyright: Property = Property(name="copyright", type=StringType)
umm_BIELibrary_owner: Property = Property(name="owner", type=StringType)
umm_BIELibrary_reference: Property = Property(name="reference", type=StringType)
umm_BIELibrary_uniqueIdentifier: Property = Property(name="uniqueIdentifier", type=StringType)
umm_BIELibrary_versionIdentifier: Property = Property(name="versionIdentifier", type=StringType)
umm_BIELibrary_baseURN: Property = Property(name="baseURN", type=StringType)
umm_BIELibrary_namespacePrefix: Property = Property(name="namespacePrefix", type=StringType)
umm_BIELibrary.attributes={umm_BIELibrary_namespacePrefix, umm_BIELibrary_uniqueIdentifier, umm_BIELibrary_copyright, umm_BIELibrary_baseURN, umm_BIELibrary_owner, umm_BIELibrary_reference, umm_BIELibrary_businessTerm, umm_BIELibrary_versionIdentifier}

# umm_BDTLibrary class attributes and methods
umm_BDTLibrary_businessTerm: Property = Property(name="businessTerm", type=StringType)
umm_BDTLibrary_copyright: Property = Property(name="copyright", type=StringType)
umm_BDTLibrary_owner: Property = Property(name="owner", type=StringType)
umm_BDTLibrary_reference: Property = Property(name="reference", type=StringType)
umm_BDTLibrary_uniqueIdentifier: Property = Property(name="uniqueIdentifier", type=StringType)
umm_BDTLibrary_versionIdentifier: Property = Property(name="versionIdentifier", type=StringType)
umm_BDTLibrary_baseURN: Property = Property(name="baseURN", type=StringType)
umm_BDTLibrary_namespacePrefix: Property = Property(name="namespacePrefix", type=StringType)
umm_BDTLibrary.attributes={umm_BDTLibrary_owner, umm_BDTLibrary_namespacePrefix, umm_BDTLibrary_baseURN, umm_BDTLibrary_businessTerm, umm_BDTLibrary_copyright, umm_BDTLibrary_uniqueIdentifier, umm_BDTLibrary_reference, umm_BDTLibrary_versionIdentifier}

# umm_InfEnvelope class attributes and methods
umm_InfEnvelope_name: Property = Property(name="name", type=StringType)
umm_InfEnvelope.attributes={umm_InfEnvelope_name}

# umm_MA class attributes and methods

# ContextRef class attributes and methods

# umm_MAProperty class attributes and methods

# umm_Constraint class attributes and methods

# umm_Library class attributes and methods
umm_Library_name: Property = Property(name="name", type=StringType)
umm_Library.attributes={umm_Library_name}

# umm_DocLibrary class attributes and methods
umm_DocLibrary_namespacePrefix: Property = Property(name="namespacePrefix", type=StringType)
umm_DocLibrary_businessTerm: Property = Property(name="businessTerm", type=StringType)
umm_DocLibrary_copyright: Property = Property(name="copyright", type=StringType)
umm_DocLibrary_owner: Property = Property(name="owner", type=StringType)
umm_DocLibrary_reference: Property = Property(name="reference", type=StringType)
umm_DocLibrary_uniqueIdentifier: Property = Property(name="uniqueIdentifier", type=StringType)
umm_DocLibrary_versionIdentifier: Property = Property(name="versionIdentifier", type=StringType)
umm_DocLibrary_baseURN: Property = Property(name="baseURN", type=StringType)
umm_DocLibrary.attributes={umm_DocLibrary_owner, umm_DocLibrary_reference, umm_DocLibrary_copyright, umm_DocLibrary_namespacePrefix, umm_DocLibrary_versionIdentifier, umm_DocLibrary_baseURN, umm_DocLibrary_uniqueIdentifier, umm_DocLibrary_businessTerm}

# Library class attributes and methods

# OclRef class attributes and methods

# umm_ABIEProperty class attributes and methods
umm_ABIEProperty_businessTerm: Property = Property(name="businessTerm", type=StringType)
umm_ABIEProperty_definition: Property = Property(name="definition", type=StringType)
umm_ABIEProperty_dictionary: Property = Property(name="dictionary", type=StringType)
umm_ABIEProperty_uniqueIdentifier: Property = Property(name="uniqueIdentifier", type=StringType)
umm_ABIEProperty_versionIdentifier: Property = Property(name="versionIdentifier", type=StringType)
umm_ABIEProperty_sequencingKey: Property = Property(name="sequencingKey", type=StringType)
umm_ABIEProperty.attributes={umm_ABIEProperty_businessTerm, umm_ABIEProperty_dictionary, umm_ABIEProperty_definition, umm_ABIEProperty_versionIdentifier, umm_ABIEProperty_sequencingKey, umm_ABIEProperty_uniqueIdentifier}

# umm_ABIE class attributes and methods
umm_ABIE_businessTerm: Property = Property(name="businessTerm", type=StringType)
umm_ABIE_definition: Property = Property(name="definition", type=StringType)
umm_ABIE_dictionary: Property = Property(name="dictionary", type=StringType)
umm_ABIE_uniqueIdentifier: Property = Property(name="uniqueIdentifier", type=StringType)
umm_ABIE_versionIdentifier: Property = Property(name="versionIdentifier", type=StringType)
umm_ABIE.attributes={umm_ABIE_dictionary, umm_ABIE_businessTerm, umm_ABIE_definition, umm_ABIE_versionIdentifier, umm_ABIE_uniqueIdentifier}

# umm_ASMA class attributes and methods

# MAProperty class attributes and methods

# umm_ASNONE class attributes and methods

# umm_ContextRef class attributes and methods
umm_ContextRef_name: Property = Property(name="name", type=StringType)
umm_ContextRef.attributes={umm_ContextRef_name}

# umm_TC_Constraint class attributes and methods
umm_TC_Constraint_kind: Property = Property(name="kind", type=StringType)
umm_TC_Constraint_listIdentifier: Property = Property(name="listIdentifier", type=StringType)
umm_TC_Constraint_responsibleAgency: Property = Property(name="responsibleAgency", type=StringType)
umm_TC_Constraint.attributes={umm_TC_Constraint_kind, umm_TC_Constraint_listIdentifier, umm_TC_Constraint_responsibleAgency}

# umm_OclInvariant class attributes and methods

# umm_ASBIE class attributes and methods

# ABIEProperty class attributes and methods

# umm_BBIE class attributes and methods
umm_BBIE_restriction: Property = Property(name="restriction", type=StringType)
umm_BBIE_fixedValue: Property = Property(name="fixedValue", type=StringType)
umm_BBIE.attributes={umm_BBIE_restriction, umm_BBIE_fixedValue}

# umm_ENUMLibrary class attributes and methods
umm_ENUMLibrary_businessTerm: Property = Property(name="businessTerm", type=StringType)
umm_ENUMLibrary_copyright: Property = Property(name="copyright", type=StringType)
umm_ENUMLibrary_owner: Property = Property(name="owner", type=StringType)
umm_ENUMLibrary_reference: Property = Property(name="reference", type=StringType)
umm_ENUMLibrary_uniqueIdentifier: Property = Property(name="uniqueIdentifier", type=StringType)
umm_ENUMLibrary_versionIdentifier: Property = Property(name="versionIdentifier", type=StringType)
umm_ENUMLibrary_baseURN: Property = Property(name="baseURN", type=StringType)
umm_ENUMLibrary_namespacePrefix: Property = Property(name="namespacePrefix", type=StringType)
umm_ENUMLibrary.attributes={umm_ENUMLibrary_owner, umm_ENUMLibrary_reference, umm_ENUMLibrary_copyright, umm_ENUMLibrary_businessTerm, umm_ENUMLibrary_baseURN, umm_ENUMLibrary_uniqueIdentifier, umm_ENUMLibrary_namespacePrefix, umm_ENUMLibrary_versionIdentifier}

# umm_BDT class attributes and methods
umm_BDT_businessTerm: Property = Property(name="businessTerm", type=StringType)
umm_BDT_definition: Property = Property(name="definition", type=StringType)
umm_BDT_dictionary: Property = Property(name="dictionary", type=StringType)
umm_BDT_uniqueIdentifier: Property = Property(name="uniqueIdentifier", type=StringType)
umm_BDT_versionIdentifier: Property = Property(name="versionIdentifier", type=StringType)
umm_BDT.attributes={umm_BDT_uniqueIdentifier, umm_BDT_businessTerm, umm_BDT_dictionary, umm_BDT_definition, umm_BDT_versionIdentifier}

# umm_ENUM class attributes and methods
umm_ENUM_name: Property = Property(name="name", type=StringType)
umm_ENUM_businessTerm: Property = Property(name="businessTerm", type=StringType)
umm_ENUM_definition: Property = Property(name="definition", type=StringType)
umm_ENUM_codeListAgencyIdentifier: Property = Property(name="codeListAgencyIdentifier", type=StringType)
umm_ENUM_codeListName: Property = Property(name="codeListName", type=StringType)
umm_ENUM_codeListIdentifier: Property = Property(name="codeListIdentifier", type=StringType)
umm_ENUM_dictionary: Property = Property(name="dictionary", type=StringType)
umm_ENUM_uniqueIdentifier: Property = Property(name="uniqueIdentifier", type=StringType)
umm_ENUM_versionIdentifier: Property = Property(name="versionIdentifier", type=StringType)
umm_ENUM.attributes={umm_ENUM_definition, umm_ENUM_codeListIdentifier, umm_ENUM_name, umm_ENUM_dictionary, umm_ENUM_uniqueIdentifier, umm_ENUM_codeListName, umm_ENUM_versionIdentifier, umm_ENUM_businessTerm, umm_ENUM_codeListAgencyIdentifier}

# ENUM class attributes and methods

# umm_Primitive class attributes and methods

# AssembledBase class attributes and methods

# umm_BDTProperty class attributes and methods
umm_BDTProperty_pattern: Property = Property(name="pattern", type=StringType)
umm_BDTProperty_minLength: Property = Property(name="minLength", type=IntegerType)
umm_BDTProperty_maxLength: Property = Property(name="maxLength", type=IntegerType)
umm_BDTProperty_length: Property = Property(name="length", type=IntegerType)
umm_BDTProperty_businessTerm: Property = Property(name="businessTerm", type=StringType)
umm_BDTProperty_definition: Property = Property(name="definition", type=StringType)
umm_BDTProperty_dictionary: Property = Property(name="dictionary", type=StringType)
umm_BDTProperty_uniqueIdentifier: Property = Property(name="uniqueIdentifier", type=StringType)
umm_BDTProperty_versionIdentifier: Property = Property(name="versionIdentifier", type=StringType)
umm_BDTProperty.attributes={umm_BDTProperty_definition, umm_BDTProperty_length, umm_BDTProperty_pattern, umm_BDTProperty_maxLength, umm_BDTProperty_versionIdentifier, umm_BDTProperty_businessTerm, umm_BDTProperty_minLength, umm_BDTProperty_dictionary, umm_BDTProperty_uniqueIdentifier}

# umm_Assembled class attributes and methods

# umm_Original class attributes and methods

# umm_AssembledBase class attributes and methods

# umm_Content class attributes and methods
umm_Content_maxInclusive: Property = Property(name="maxInclusive", type=IntegerType)
umm_Content_maxExclusive: Property = Property(name="maxExclusive", type=IntegerType)
umm_Content_minInclusive: Property = Property(name="minInclusive", type=IntegerType)
umm_Content_minExclusive: Property = Property(name="minExclusive", type=IntegerType)
umm_Content_fractionalDigits: Property = Property(name="fractionalDigits", type=IntegerType)
umm_Content_totalDigits: Property = Property(name="totalDigits", type=IntegerType)
umm_Content.attributes={umm_Content_minExclusive, umm_Content_fractionalDigits, umm_Content_totalDigits, umm_Content_maxInclusive, umm_Content_minInclusive, umm_Content_maxExclusive}

# BDTProperty class attributes and methods

# umm_Supplement class attributes and methods
umm_Supplement_restriction: Property = Property(name="restriction", type=StringType)
umm_Supplement_fixedValue: Property = Property(name="fixedValue", type=StringType)
umm_Supplement_defaultValue: Property = Property(name="defaultValue", type=StringType)
umm_Supplement.attributes={umm_Supplement_defaultValue, umm_Supplement_restriction, umm_Supplement_fixedValue}

# umm_ACC class attributes and methods
umm_ACC_name: Property = Property(name="name", type=StringType)
umm_ACC_businessTerm: Property = Property(name="businessTerm", type=StringType)
umm_ACC_definition: Property = Property(name="definition", type=StringType)
umm_ACC_dictionary: Property = Property(name="dictionary", type=StringType)
umm_ACC_uniqueIdentifier: Property = Property(name="uniqueIdentifier", type=StringType)
umm_ACC_versionIdentifier: Property = Property(name="versionIdentifier", type=StringType)
umm_ACC.attributes={umm_ACC_definition, umm_ACC_name, umm_ACC_uniqueIdentifier, umm_ACC_dictionary, umm_ACC_versionIdentifier, umm_ACC_businessTerm}

# umm_ACCProperty class attributes and methods
umm_ACCProperty_multiplicity: Property = Property(name="multiplicity", type=StringType)
umm_ACCProperty_name: Property = Property(name="name", type=StringType)
umm_ACCProperty_businessTerm: Property = Property(name="businessTerm", type=StringType)
umm_ACCProperty_definition: Property = Property(name="definition", type=StringType)
umm_ACCProperty_dictionary: Property = Property(name="dictionary", type=StringType)
umm_ACCProperty_uniqueIdentifier: Property = Property(name="uniqueIdentifier", type=StringType)
umm_ACCProperty_versionIdentifier: Property = Property(name="versionIdentifier", type=StringType)
umm_ACCProperty_sequencingKey: Property = Property(name="sequencingKey", type=StringType)
umm_ACCProperty.attributes={umm_ACCProperty_dictionary, umm_ACCProperty_sequencingKey, umm_ACCProperty_multiplicity, umm_ACCProperty_versionIdentifier, umm_ACCProperty_uniqueIdentifier, umm_ACCProperty_name, umm_ACCProperty_definition, umm_ACCProperty_businessTerm}

# umm_ASCC class attributes and methods

# ACCProperty class attributes and methods

# umm_Subset class attributes and methods

# umm_CodelistEntry class attributes and methods
umm_CodelistEntry_name: Property = Property(name="name", type=StringType)
umm_CodelistEntry_description: Property = Property(name="description", type=StringType)
umm_CodelistEntry.attributes={umm_CodelistEntry_description, umm_CodelistEntry_name}

# umm_CCLibrary class attributes and methods
umm_CCLibrary_versionIdentifier: Property = Property(name="versionIdentifier", type=StringType)
umm_CCLibrary_baseURN: Property = Property(name="baseURN", type=StringType)
umm_CCLibrary_namespacePrefix: Property = Property(name="namespacePrefix", type=StringType)
umm_CCLibrary_businessTerm: Property = Property(name="businessTerm", type=StringType)
umm_CCLibrary_copyright: Property = Property(name="copyright", type=StringType)
umm_CCLibrary_owner: Property = Property(name="owner", type=StringType)
umm_CCLibrary_reference: Property = Property(name="reference", type=StringType)
umm_CCLibrary_uniqueIdentifier: Property = Property(name="uniqueIdentifier", type=StringType)
umm_CCLibrary.attributes={umm_CCLibrary_versionIdentifier, umm_CCLibrary_copyright, umm_CCLibrary_uniqueIdentifier, umm_CCLibrary_businessTerm, umm_CCLibrary_namespacePrefix, umm_CCLibrary_owner, umm_CCLibrary_baseURN, umm_CCLibrary_reference}

# umm_CDTLibrary class attributes and methods
umm_CDTLibrary_businessTerm: Property = Property(name="businessTerm", type=StringType)
umm_CDTLibrary_copyright: Property = Property(name="copyright", type=StringType)
umm_CDTLibrary_owner: Property = Property(name="owner", type=StringType)
umm_CDTLibrary_reference: Property = Property(name="reference", type=StringType)
umm_CDTLibrary_uniqueIdentifier: Property = Property(name="uniqueIdentifier", type=StringType)
umm_CDTLibrary_versionIdentifier: Property = Property(name="versionIdentifier", type=StringType)
umm_CDTLibrary_baseURN: Property = Property(name="baseURN", type=StringType)
umm_CDTLibrary_namespacePrefix: Property = Property(name="namespacePrefix", type=StringType)
umm_CDTLibrary.attributes={umm_CDTLibrary_namespacePrefix, umm_CDTLibrary_copyright, umm_CDTLibrary_baseURN, umm_CDTLibrary_owner, umm_CDTLibrary_businessTerm, umm_CDTLibrary_uniqueIdentifier, umm_CDTLibrary_versionIdentifier, umm_CDTLibrary_reference}

# umm_BCC class attributes and methods
umm_BCC_restriction: Property = Property(name="restriction", type=StringType)
umm_BCC_fixedValue: Property = Property(name="fixedValue", type=StringType)
umm_BCC.attributes={umm_BCC_fixedValue, umm_BCC_restriction}

# umm_CDT class attributes and methods
umm_CDT_name: Property = Property(name="name", type=StringType)
umm_CDT_businessTerm: Property = Property(name="businessTerm", type=StringType)
umm_CDT_definition: Property = Property(name="definition", type=StringType)
umm_CDT_dictionary: Property = Property(name="dictionary", type=StringType)
umm_CDT_uniqueIdentifier: Property = Property(name="uniqueIdentifier", type=StringType)
umm_CDT_versionIdentifier: Property = Property(name="versionIdentifier", type=StringType)
umm_CDT.attributes={umm_CDT_businessTerm, umm_CDT_definition, umm_CDT_dictionary, umm_CDT_versionIdentifier, umm_CDT_name, umm_CDT_uniqueIdentifier}

# umm_PrimitiveLibrary class attributes and methods

# umm_OclExpression class attributes and methods

# umm_OclValue class attributes and methods

# OclExpression class attributes and methods

# umm_OclReference class attributes and methods

# OclValue class attributes and methods

# umm_OclPathSelfHead class attributes and methods

# OclReference class attributes and methods

# umm_OclPathTail class attributes and methods

# umm_OclPathFeatureHead class attributes and methods

# umm_OclRef class attributes and methods
umm_OclRef_name: Property = Property(name="name", type=StringType)
umm_OclRef_multiplicity: Property = Property(name="multiplicity", type=StringType)
umm_OclRef.attributes={umm_OclRef_name, umm_OclRef_multiplicity}

# umm_CDTProperty class attributes and methods
umm_CDTProperty_multiplicity: Property = Property(name="multiplicity", type=StringType)
umm_CDTProperty_name: Property = Property(name="name", type=StringType)
umm_CDTProperty_businessTerm: Property = Property(name="businessTerm", type=StringType)
umm_CDTProperty_definition: Property = Property(name="definition", type=StringType)
umm_CDTProperty_dictionary: Property = Property(name="dictionary", type=StringType)
umm_CDTProperty_uniqueIdentifier: Property = Property(name="uniqueIdentifier", type=StringType)
umm_CDTProperty_versionIdentifier: Property = Property(name="versionIdentifier", type=StringType)
umm_CDTProperty.attributes={umm_CDTProperty_uniqueIdentifier, umm_CDTProperty_definition, umm_CDTProperty_dictionary, umm_CDTProperty_multiplicity, umm_CDTProperty_name, umm_CDTProperty_versionIdentifier, umm_CDTProperty_businessTerm}

# umm_CDT_Content class attributes and methods

# CDTProperty class attributes and methods

# umm_CDT_Supplement class attributes and methods
umm_CDT_Supplement_fixedValue: Property = Property(name="fixedValue", type=StringType)
umm_CDT_Supplement_defaultValue: Property = Property(name="defaultValue", type=StringType)
umm_CDT_Supplement_restriction: Property = Property(name="restriction", type=StringType)
umm_CDT_Supplement.attributes={umm_CDT_Supplement_defaultValue, umm_CDT_Supplement_restriction, umm_CDT_Supplement_fixedValue}

# umm_OclBooleanFalse class attributes and methods

# OclBooleanLiteral class attributes and methods

# umm_OclImplies class attributes and methods

# umm_OclAnd class attributes and methods

# umm_OclOr class attributes and methods

# umm_OclXor class attributes and methods

# umm_OclEqual class attributes and methods

# umm_OclFunctionCall class attributes and methods

# umm_OclForAll class attributes and methods

# OclFunctionCall class attributes and methods

# umm_OclIsEmpty class attributes and methods

# umm_OclNotEmpty class attributes and methods

# umm_OclSize class attributes and methods

# umm_OclLiteral class attributes and methods

# umm_OclEnumerationLiteral class attributes and methods
umm_OclEnumerationLiteral_value: Property = Property(name="value", type=StringType)
umm_OclEnumerationLiteral.attributes={umm_OclEnumerationLiteral_value}

# OclLiteral class attributes and methods

# umm_OclIntegerLiteral class attributes and methods
umm_OclIntegerLiteral_value: Property = Property(name="value", type=IntegerType)
umm_OclIntegerLiteral.attributes={umm_OclIntegerLiteral_value}

# umm_OclStringLiteral class attributes and methods
umm_OclStringLiteral_value: Property = Property(name="value", type=StringType)
umm_OclStringLiteral.attributes={umm_OclStringLiteral_value}

# umm_OclBooleanLiteral class attributes and methods

# umm_OclArrow class attributes and methods

# umm_OclBooleanTrue class attributes and methods

# umm_OclLess class attributes and methods

# umm_OclLessOrEqual class attributes and methods

# umm_OclMore class attributes and methods

# umm_OclMoreOrEqual class attributes and methods

# Relationships
bieLibrary0: BinaryAssociation = BinaryAssociation(
    name="bieLibrary0",
    ends={
        Property(name="umm_BIELibrary", type=umm_DocLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_DocLibrary", type=umm_BIELibrary, multiplicity=Multiplicity(0, 1))
    }
)
bdtLibrary1: BinaryAssociation = BinaryAssociation(
    name="bdtLibrary1",
    ends={
        Property(name="umm_BDTLibrary", type=umm_DocLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_DocLibrary2", type=umm_BDTLibrary, multiplicity=Multiplicity(0, 1))
    }
)
envelopes3: BinaryAssociation = BinaryAssociation(
    name="envelopes3",
    ends={
        Property(name="umm_InfEnvelope", type=umm_DocLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_DocLibrary4", type=umm_InfEnvelope, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assemblies5: BinaryAssociation = BinaryAssociation(
    name="assemblies5",
    ends={
        Property(name="umm_MA", type=umm_InfEnvelope, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_InfEnvelope6", type=umm_MA, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties7: BinaryAssociation = BinaryAssociation(
    name="properties7",
    ends={
        Property(name="umm_MAProperty", type=umm_MA, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_MA8", type=umm_MAProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints9: BinaryAssociation = BinaryAssociation(
    name="constraints9",
    ends={
        Property(name="umm_Constraint", type=umm_MA, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_MA10", type=umm_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bdtLibrary19: BinaryAssociation = BinaryAssociation(
    name="bdtLibrary19",
    ends={
        Property(name="umm_BDTLibrary21", type=umm_BIELibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_BIELibrary20", type=umm_BDTLibrary, multiplicity=Multiplicity(0, 1))
    }
)
abies22: BinaryAssociation = BinaryAssociation(
    name="abies22",
    ends={
        Property(name="umm_ABIE24", type=umm_BIELibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_BIELibrary23", type=umm_ABIE, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties25: BinaryAssociation = BinaryAssociation(
    name="properties25",
    ends={
        Property(name="umm_ABIEProperty", type=umm_ABIE, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_ABIE26", type=umm_ABIEProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="umm_ABIE", type=umm_MAProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_MAProperty12", type=umm_ABIE, multiplicity=Multiplicity(0, 1))
    }
)
context13: BinaryAssociation = BinaryAssociation(
    name="context13",
    ends={
        Property(name="umm_ContextRef", type=umm_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_Constraint14", type=umm_ContextRef, multiplicity=Multiplicity(0, 1))
    }
)
type15: BinaryAssociation = BinaryAssociation(
    name="type15",
    ends={
        Property(name="umm_TC_Constraint", type=umm_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_Constraint16", type=umm_TC_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invariants17: BinaryAssociation = BinaryAssociation(
    name="invariants17",
    ends={
        Property(name="umm_OclInvariant", type=umm_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_Constraint18", type=umm_OclInvariant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bdts36: BinaryAssociation = BinaryAssociation(
    name="bdts36",
    ends={
        Property(name="umm_BDT38", type=umm_BDTLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_BDTLibrary37", type=umm_BDT, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints27: BinaryAssociation = BinaryAssociation(
    name="constraints27",
    ends={
        Property(name="umm_Constraint29", type=umm_ABIE, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_ABIE28", type=umm_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
or_31: BinaryAssociation = BinaryAssociation(
    name="or_31",
    ends={
        Property(name="umm_ABIEProperty32", type=umm_ABIEProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_ABIEProperty30", type=umm_ABIEProperty, multiplicity=Multiplicity(0, 9999))
    }
)
type33: BinaryAssociation = BinaryAssociation(
    name="type33",
    ends={
        Property(name="umm_ABIE34", type=umm_ASBIE, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_ASBIE", type=umm_ABIE, multiplicity=Multiplicity(0, 1))
    }
)
type35: BinaryAssociation = BinaryAssociation(
    name="type35",
    ends={
        Property(name="umm_BDT", type=umm_BBIE, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_BBIE", type=umm_BDT, multiplicity=Multiplicity(0, 1))
    }
)
enums43: BinaryAssociation = BinaryAssociation(
    name="enums43",
    ends={
        Property(name="umm_ENUM", type=umm_ENUMLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_ENUMLibrary", type=umm_ENUM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties39: BinaryAssociation = BinaryAssociation(
    name="properties39",
    ends={
        Property(name="umm_BDTProperty", type=umm_BDT, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_BDT40", type=umm_BDTProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type41: BinaryAssociation = BinaryAssociation(
    name="type41",
    ends={
        Property(name="umm_AssembledBase", type=umm_BDTProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_BDTProperty42", type=umm_AssembledBase, multiplicity=Multiplicity(0, 1))
    }
)
accs52: BinaryAssociation = BinaryAssociation(
    name="accs52",
    ends={
        Property(name="umm_ACC", type=umm_CCLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_CCLibrary", type=umm_ACC, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties53: BinaryAssociation = BinaryAssociation(
    name="properties53",
    ends={
        Property(name="umm_ACCProperty", type=umm_ACC, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_ACC54", type=umm_ACCProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints55: BinaryAssociation = BinaryAssociation(
    name="constraints55",
    ends={
        Property(name="umm_Constraint57", type=umm_ACC, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_ACC56", type=umm_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type58: BinaryAssociation = BinaryAssociation(
    name="type58",
    ends={
        Property(name="umm_ACC59", type=umm_ASCC, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_ASCC", type=umm_ACC, multiplicity=Multiplicity(0, 1))
    }
)
originals44: BinaryAssociation = BinaryAssociation(
    name="originals44",
    ends={
        Property(name="umm_Original", type=umm_Assembled, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_Assembled", type=umm_Original, multiplicity=Multiplicity(0, 9999))
    }
)
subsets45: BinaryAssociation = BinaryAssociation(
    name="subsets45",
    ends={
        Property(name="umm_Subset", type=umm_Assembled, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_Assembled46", type=umm_Subset, multiplicity=Multiplicity(0, 9999))
    }
)
codes47: BinaryAssociation = BinaryAssociation(
    name="codes47",
    ends={
        Property(name="umm_CodelistEntry", type=umm_Original, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_Original48", type=umm_CodelistEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
codes49: BinaryAssociation = BinaryAssociation(
    name="codes49",
    ends={
        Property(name="umm_CodelistEntry51", type=umm_Subset, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_Subset50", type=umm_CodelistEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type60: BinaryAssociation = BinaryAssociation(
    name="type60",
    ends={
        Property(name="umm_CDT", type=umm_BCC, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_BCC", type=umm_CDT, multiplicity=Multiplicity(0, 1))
    }
)
types67: BinaryAssociation = BinaryAssociation(
    name="types67",
    ends={
        Property(name="umm_Primitive68", type=umm_PrimitiveLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_PrimitiveLibrary", type=umm_Primitive, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression69: BinaryAssociation = BinaryAssociation(
    name="expression69",
    ends={
        Property(name="umm_OclExpression", type=umm_OclInvariant, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclInvariant70", type=umm_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
path71: BinaryAssociation = BinaryAssociation(
    name="path71",
    ends={
        Property(name="umm_OclPathTail", type=umm_OclPathSelfHead, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclPathSelfHead", type=umm_OclPathTail, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature72: BinaryAssociation = BinaryAssociation(
    name="feature72",
    ends={
        Property(name="umm_OclRef", type=umm_OclPathFeatureHead, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclPathFeatureHead", type=umm_OclRef, multiplicity=Multiplicity(0, 1))
    }
)
tail73: BinaryAssociation = BinaryAssociation(
    name="tail73",
    ends={
        Property(name="umm_OclPathTail75", type=umm_OclPathFeatureHead, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclPathFeatureHead74", type=umm_OclPathTail, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature76: BinaryAssociation = BinaryAssociation(
    name="feature76",
    ends={
        Property(name="umm_OclRef78", type=umm_OclPathTail, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclPathTail77", type=umm_OclRef, multiplicity=Multiplicity(0, 1))
    }
)
cdts61: BinaryAssociation = BinaryAssociation(
    name="cdts61",
    ends={
        Property(name="umm_CDT62", type=umm_CDTLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_CDTLibrary", type=umm_CDT, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tail80: BinaryAssociation = BinaryAssociation(
    name="tail80",
    ends={
        Property(name="umm_OclPathTail81", type=umm_OclPathTail, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclPathTail79", type=umm_OclPathTail, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties63: BinaryAssociation = BinaryAssociation(
    name="properties63",
    ends={
        Property(name="umm_CDTProperty", type=umm_CDT, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_CDT64", type=umm_CDTProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type65: BinaryAssociation = BinaryAssociation(
    name="type65",
    ends={
        Property(name="umm_Primitive", type=umm_CDTProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_CDTProperty66", type=umm_Primitive, multiplicity=Multiplicity(0, 1))
    }
)
left84: BinaryAssociation = BinaryAssociation(
    name="left84",
    ends={
        Property(name="umm_OclExpression85", type=umm_OclImplies, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclImplies", type=umm_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right86: BinaryAssociation = BinaryAssociation(
    name="right86",
    ends={
        Property(name="umm_OclExpression88", type=umm_OclImplies, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclImplies87", type=umm_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left89: BinaryAssociation = BinaryAssociation(
    name="left89",
    ends={
        Property(name="umm_OclExpression90", type=umm_OclAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclAnd", type=umm_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right91: BinaryAssociation = BinaryAssociation(
    name="right91",
    ends={
        Property(name="umm_OclExpression93", type=umm_OclAnd, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclAnd92", type=umm_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left94: BinaryAssociation = BinaryAssociation(
    name="left94",
    ends={
        Property(name="umm_OclExpression95", type=umm_OclOr, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclOr", type=umm_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right96: BinaryAssociation = BinaryAssociation(
    name="right96",
    ends={
        Property(name="umm_OclExpression98", type=umm_OclOr, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclOr97", type=umm_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left99: BinaryAssociation = BinaryAssociation(
    name="left99",
    ends={
        Property(name="umm_OclExpression100", type=umm_OclXor, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclXor", type=umm_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right101: BinaryAssociation = BinaryAssociation(
    name="right101",
    ends={
        Property(name="umm_OclExpression103", type=umm_OclXor, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclXor102", type=umm_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left104: BinaryAssociation = BinaryAssociation(
    name="left104",
    ends={
        Property(name="umm_OclExpression105", type=umm_OclEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclEqual", type=umm_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right106: BinaryAssociation = BinaryAssociation(
    name="right106",
    ends={
        Property(name="umm_OclExpression108", type=umm_OclEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclEqual107", type=umm_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body82: BinaryAssociation = BinaryAssociation(
    name="body82",
    ends={
        Property(name="umm_OclExpression83", type=umm_OclForAll, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclForAll", type=umm_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left124: BinaryAssociation = BinaryAssociation(
    name="left124",
    ends={
        Property(name="umm_OclExpression125", type=umm_OclMoreOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclMoreOrEqual", type=umm_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right126: BinaryAssociation = BinaryAssociation(
    name="right126",
    ends={
        Property(name="umm_OclExpression128", type=umm_OclMoreOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclMoreOrEqual127", type=umm_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left129: BinaryAssociation = BinaryAssociation(
    name="left129",
    ends={
        Property(name="umm_OclValue", type=umm_OclArrow, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclArrow", type=umm_OclValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right130: BinaryAssociation = BinaryAssociation(
    name="right130",
    ends={
        Property(name="umm_OclFunctionCall", type=umm_OclArrow, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclArrow131", type=umm_OclFunctionCall, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left109: BinaryAssociation = BinaryAssociation(
    name="left109",
    ends={
        Property(name="umm_OclExpression110", type=umm_OclLess, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclLess", type=umm_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right111: BinaryAssociation = BinaryAssociation(
    name="right111",
    ends={
        Property(name="umm_OclExpression113", type=umm_OclLess, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclLess112", type=umm_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left114: BinaryAssociation = BinaryAssociation(
    name="left114",
    ends={
        Property(name="umm_OclExpression115", type=umm_OclLessOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclLessOrEqual", type=umm_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right116: BinaryAssociation = BinaryAssociation(
    name="right116",
    ends={
        Property(name="umm_OclExpression118", type=umm_OclLessOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclLessOrEqual117", type=umm_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left119: BinaryAssociation = BinaryAssociation(
    name="left119",
    ends={
        Property(name="umm_OclExpression120", type=umm_OclMore, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclMore", type=umm_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right121: BinaryAssociation = BinaryAssociation(
    name="right121",
    ends={
        Property(name="umm_OclExpression123", type=umm_OclMore, multiplicity=Multiplicity(1, 1)),
        Property(name="umm_OclMore122", type=umm_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_umm_MA_ContextRef = Generalization(general=ContextRef, specific=umm_MA)
gen_umm_DocLibrary_Library = Generalization(general=Library, specific=umm_DocLibrary)
gen_umm_BIELibrary_Library = Generalization(general=Library, specific=umm_BIELibrary)
gen_umm_ABIE_ContextRef = Generalization(general=ContextRef, specific=umm_ABIE)
gen_umm_MAProperty_OclRef = Generalization(general=OclRef, specific=umm_MAProperty)
gen_umm_ASMA_MAProperty = Generalization(general=MAProperty, specific=umm_ASMA)
gen_umm_ASNONE_MAProperty = Generalization(general=MAProperty, specific=umm_ASNONE)
gen_umm_BDTLibrary_Library = Generalization(general=Library, specific=umm_BDTLibrary)
gen_umm_BDT_ContextRef = Generalization(general=ContextRef, specific=umm_BDT)
gen_umm_ABIEProperty_OclRef = Generalization(general=OclRef, specific=umm_ABIEProperty)
gen_umm_ASBIE_ABIEProperty = Generalization(general=ABIEProperty, specific=umm_ASBIE)
gen_umm_BBIE_ABIEProperty = Generalization(general=ABIEProperty, specific=umm_BBIE)
gen_umm_ENUMLibrary_Library = Generalization(general=Library, specific=umm_ENUMLibrary)
gen_umm_AssembledBase_ENUM = Generalization(general=ENUM, specific=umm_AssembledBase)
gen_umm_Primitive_AssembledBase = Generalization(general=AssembledBase, specific=umm_Primitive)
gen_umm_Assembled_AssembledBase = Generalization(general=AssembledBase, specific=umm_Assembled)
gen_umm_BDTProperty_OclRef = Generalization(general=OclRef, specific=umm_BDTProperty)
gen_umm_Content_BDTProperty = Generalization(general=BDTProperty, specific=umm_Content)
gen_umm_Supplement_BDTProperty = Generalization(general=BDTProperty, specific=umm_Supplement)
gen_umm_ASCC_ACCProperty = Generalization(general=ACCProperty, specific=umm_ASCC)
gen_umm_Original_ENUM = Generalization(general=ENUM, specific=umm_Original)
gen_umm_Subset_ENUM = Generalization(general=ENUM, specific=umm_Subset)
gen_umm_CCLibrary_Library = Generalization(general=Library, specific=umm_CCLibrary)
gen_umm_CDTLibrary_Library = Generalization(general=Library, specific=umm_CDTLibrary)
gen_umm_BCC_ACCProperty = Generalization(general=ACCProperty, specific=umm_BCC)
gen_umm_PrimitiveLibrary_Library = Generalization(general=Library, specific=umm_PrimitiveLibrary)
gen_umm_OclValue_OclExpression = Generalization(general=OclExpression, specific=umm_OclValue)
gen_umm_OclReference_OclValue = Generalization(general=OclValue, specific=umm_OclReference)
gen_umm_OclPathSelfHead_OclReference = Generalization(general=OclReference, specific=umm_OclPathSelfHead)
gen_umm_OclPathFeatureHead_OclReference = Generalization(general=OclReference, specific=umm_OclPathFeatureHead)
gen_umm_CDT_Content_CDTProperty = Generalization(general=CDTProperty, specific=umm_CDT_Content)
gen_umm_CDT_Supplement_CDTProperty = Generalization(general=CDTProperty, specific=umm_CDT_Supplement)
gen_umm_OclBooleanFalse_OclBooleanLiteral = Generalization(general=OclBooleanLiteral, specific=umm_OclBooleanFalse)
gen_umm_OclImplies_OclExpression = Generalization(general=OclExpression, specific=umm_OclImplies)
gen_umm_OclAnd_OclExpression = Generalization(general=OclExpression, specific=umm_OclAnd)
gen_umm_OclOr_OclExpression = Generalization(general=OclExpression, specific=umm_OclOr)
gen_umm_OclXor_OclExpression = Generalization(general=OclExpression, specific=umm_OclXor)
gen_umm_OclEqual_OclExpression = Generalization(general=OclExpression, specific=umm_OclEqual)
gen_umm_OclForAll_OclFunctionCall = Generalization(general=OclFunctionCall, specific=umm_OclForAll)
gen_umm_OclIsEmpty_OclFunctionCall = Generalization(general=OclFunctionCall, specific=umm_OclIsEmpty)
gen_umm_OclNotEmpty_OclFunctionCall = Generalization(general=OclFunctionCall, specific=umm_OclNotEmpty)
gen_umm_OclSize_OclFunctionCall = Generalization(general=OclFunctionCall, specific=umm_OclSize)
gen_umm_OclLiteral_OclValue = Generalization(general=OclValue, specific=umm_OclLiteral)
gen_umm_OclEnumerationLiteral_OclLiteral = Generalization(general=OclLiteral, specific=umm_OclEnumerationLiteral)
gen_umm_OclIntegerLiteral_OclLiteral = Generalization(general=OclLiteral, specific=umm_OclIntegerLiteral)
gen_umm_OclStringLiteral_OclLiteral = Generalization(general=OclLiteral, specific=umm_OclStringLiteral)
gen_umm_OclBooleanLiteral_OclLiteral = Generalization(general=OclLiteral, specific=umm_OclBooleanLiteral)
gen_umm_OclArrow_OclExpression = Generalization(general=OclExpression, specific=umm_OclArrow)
gen_umm_OclBooleanTrue_OclBooleanLiteral = Generalization(general=OclBooleanLiteral, specific=umm_OclBooleanTrue)
gen_umm_OclLess_OclExpression = Generalization(general=OclExpression, specific=umm_OclLess)
gen_umm_OclLessOrEqual_OclExpression = Generalization(general=OclExpression, specific=umm_OclLessOrEqual)
gen_umm_OclMore_OclExpression = Generalization(general=OclExpression, specific=umm_OclMore)
gen_umm_OclMoreOrEqual_OclExpression = Generalization(general=OclExpression, specific=umm_OclMoreOrEqual)

# Domain Model
domain_model = DomainModel(
    name="umm",
    types={umm_BIELibrary, umm_BDTLibrary, umm_InfEnvelope, umm_MA, ContextRef, umm_MAProperty, umm_Constraint, umm_Library, umm_DocLibrary, Library, OclRef, umm_ABIEProperty, umm_ABIE, umm_ASMA, MAProperty, umm_ASNONE, umm_ContextRef, umm_TC_Constraint, umm_OclInvariant, umm_ASBIE, ABIEProperty, umm_BBIE, umm_ENUMLibrary, umm_BDT, umm_ENUM, ENUM, umm_Primitive, AssembledBase, umm_BDTProperty, umm_Assembled, umm_Original, umm_AssembledBase, umm_Content, BDTProperty, umm_Supplement, umm_ACC, umm_ACCProperty, umm_ASCC, ACCProperty, umm_Subset, umm_CodelistEntry, umm_CCLibrary, umm_CDTLibrary, umm_BCC, umm_CDT, umm_PrimitiveLibrary, umm_OclExpression, umm_OclValue, OclExpression, umm_OclReference, OclValue, umm_OclPathSelfHead, OclReference, umm_OclPathTail, umm_OclPathFeatureHead, umm_OclRef, umm_CDTProperty, umm_CDT_Content, CDTProperty, umm_CDT_Supplement, umm_OclBooleanFalse, OclBooleanLiteral, umm_OclImplies, umm_OclAnd, umm_OclOr, umm_OclXor, umm_OclEqual, umm_OclFunctionCall, umm_OclForAll, OclFunctionCall, umm_OclIsEmpty, umm_OclNotEmpty, umm_OclSize, umm_OclLiteral, umm_OclEnumerationLiteral, OclLiteral, umm_OclIntegerLiteral, umm_OclStringLiteral, umm_OclBooleanLiteral, umm_OclArrow, umm_OclBooleanTrue, umm_OclLess, umm_OclLessOrEqual, umm_OclMore, umm_OclMoreOrEqual, ConstraintKind, MultiplicityKind},
    associations={bieLibrary0, bdtLibrary1, envelopes3, assemblies5, properties7, constraints9, bdtLibrary19, abies22, properties25, type11, context13, type15, invariants17, bdts36, constraints27, or_31, type33, type35, enums43, properties39, type41, accs52, properties53, constraints55, type58, originals44, subsets45, codes47, codes49, type60, types67, expression69, path71, feature72, tail73, feature76, cdts61, tail80, properties63, type65, left84, right86, left89, right91, left94, right96, left99, right101, left104, right106, body82, left124, right126, left129, right130, left109, right111, left114, right116, left119, right121},
    generalizations={gen_umm_MA_ContextRef, gen_umm_DocLibrary_Library, gen_umm_BIELibrary_Library, gen_umm_ABIE_ContextRef, gen_umm_MAProperty_OclRef, gen_umm_ASMA_MAProperty, gen_umm_ASNONE_MAProperty, gen_umm_BDTLibrary_Library, gen_umm_BDT_ContextRef, gen_umm_ABIEProperty_OclRef, gen_umm_ASBIE_ABIEProperty, gen_umm_BBIE_ABIEProperty, gen_umm_ENUMLibrary_Library, gen_umm_AssembledBase_ENUM, gen_umm_Primitive_AssembledBase, gen_umm_Assembled_AssembledBase, gen_umm_BDTProperty_OclRef, gen_umm_Content_BDTProperty, gen_umm_Supplement_BDTProperty, gen_umm_ASCC_ACCProperty, gen_umm_Original_ENUM, gen_umm_Subset_ENUM, gen_umm_CCLibrary_Library, gen_umm_CDTLibrary_Library, gen_umm_BCC_ACCProperty, gen_umm_PrimitiveLibrary_Library, gen_umm_OclValue_OclExpression, gen_umm_OclReference_OclValue, gen_umm_OclPathSelfHead_OclReference, gen_umm_OclPathFeatureHead_OclReference, gen_umm_CDT_Content_CDTProperty, gen_umm_CDT_Supplement_CDTProperty, gen_umm_OclBooleanFalse_OclBooleanLiteral, gen_umm_OclImplies_OclExpression, gen_umm_OclAnd_OclExpression, gen_umm_OclOr_OclExpression, gen_umm_OclXor_OclExpression, gen_umm_OclEqual_OclExpression, gen_umm_OclForAll_OclFunctionCall, gen_umm_OclIsEmpty_OclFunctionCall, gen_umm_OclNotEmpty_OclFunctionCall, gen_umm_OclSize_OclFunctionCall, gen_umm_OclLiteral_OclValue, gen_umm_OclEnumerationLiteral_OclLiteral, gen_umm_OclIntegerLiteral_OclLiteral, gen_umm_OclStringLiteral_OclLiteral, gen_umm_OclBooleanLiteral_OclLiteral, gen_umm_OclArrow_OclExpression, gen_umm_OclBooleanTrue_OclBooleanLiteral, gen_umm_OclLess_OclExpression, gen_umm_OclLessOrEqual_OclExpression, gen_umm_OclMore_OclExpression, gen_umm_OclMoreOrEqual_OclExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)