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
ParameterStyle: Enumeration = Enumeration(
    name="ParameterStyle",
    literals={
            EnumerationLiteral(name="DB2SQL"),
			EnumerationLiteral(name="GENERAL"),
			EnumerationLiteral(name="GENERAL_WITH_NULLS"),
			EnumerationLiteral(name="DB2GENRL"),
			EnumerationLiteral(name="DB2DARI"),
			EnumerationLiteral(name="JAVA"),
			EnumerationLiteral(name="SQL")
    }
)

ParentDeleteDRIRuleType: Enumeration = Enumeration(
    name="ParentDeleteDRIRuleType",
    literals={
            EnumerationLiteral(name="NO_ACTION"),
			EnumerationLiteral(name="RESTRICT"),
			EnumerationLiteral(name="CASCADE"),
			EnumerationLiteral(name="SET_NULL"),
			EnumerationLiteral(name="SET_DEFAULT")
    }
)

CheckOption: Enumeration = Enumeration(
    name="CheckOption",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="CASCADE"),
			EnumerationLiteral(name="LOCAL")
    }
)

LanguageType: Enumeration = Enumeration(
    name="LanguageType",
    literals={
            EnumerationLiteral(name="REXX"),
			EnumerationLiteral(name="RPG"),
			EnumerationLiteral(name="RPGLE"),
			EnumerationLiteral(name="PLSQL"),
			EnumerationLiteral(name="SQL"),
			EnumerationLiteral(name="JAVA"),
			EnumerationLiteral(name="C"),
			EnumerationLiteral(name="OLE"),
			EnumerationLiteral(name="ASSEMBLY"),
			EnumerationLiteral(name="COBOL"),
			EnumerationLiteral(name="PLI"),
			EnumerationLiteral(name="CPLUSPLUS"),
			EnumerationLiteral(name="CL"),
			EnumerationLiteral(name="COBOLLE"),
			EnumerationLiteral(name="FORTRAN")
    }
)

ParentUpdateDRIRuleType: Enumeration = Enumeration(
    name="ParentUpdateDRIRuleType",
    literals={
            EnumerationLiteral(name="NO_ACTION"),
			EnumerationLiteral(name="RESTRICT"),
			EnumerationLiteral(name="CASCADE"),
			EnumerationLiteral(name="SET_NULL"),
			EnumerationLiteral(name="SET_DEFAULT")
    }
)

ProcedureType: Enumeration = Enumeration(
    name="ProcedureType",
    literals={
            EnumerationLiteral(name="PROCEDURE"),
			EnumerationLiteral(name="FUNCTION")
    }
)

TableSpaceType: Enumeration = Enumeration(
    name="TableSpaceType",
    literals={
            EnumerationLiteral(name="REGULAR"),
			EnumerationLiteral(name="LOB"),
			EnumerationLiteral(name="SYSTEM_TEMPORARY"),
			EnumerationLiteral(name="USER_TEMPORARY"),
			EnumerationLiteral(name="PERMANENT"),
			EnumerationLiteral(name="TEMPORARY"),
			EnumerationLiteral(name="LONG"),
			EnumerationLiteral(name="LARGE")
    }
)

PercentFreeTerminology: Enumeration = Enumeration(
    name="PercentFreeTerminology",
    literals={
            EnumerationLiteral(name="PERCENT_FREE"),
			EnumerationLiteral(name="FILL_FACTOR"),
			EnumerationLiteral(name="THRESHOLD")
    }
)

LengthUnit: Enumeration = Enumeration(
    name="LengthUnit",
    literals={
            EnumerationLiteral(name="DECIMAL"),
			EnumerationLiteral(name="BIT"),
			EnumerationLiteral(name="BYTE"),
			EnumerationLiteral(name="DOUBLE_BYTE")
    }
)

# Classes
dbdefinition_DatabaseVendorDefinition = Class(name="dbdefinition_DatabaseVendorDefinition")
dbdefinition_PredefinedDataTypeDefinition = Class(name="dbdefinition_PredefinedDataTypeDefinition")
dbdefinition_UserDefinedTypeDefinition = Class(name="dbdefinition_UserDefinedTypeDefinition")
dbdefinition_QueryDefinition = Class(name="dbdefinition_QueryDefinition")
dbdefinition_SQLSyntaxDefinition = Class(name="dbdefinition_SQLSyntaxDefinition")
dbdefinition_NicknameDefinition = Class(name="dbdefinition_NicknameDefinition")
dbdefinition_TableSpaceDefinition = Class(name="dbdefinition_TableSpaceDefinition")
dbdefinition_StoredProcedureDefinition = Class(name="dbdefinition_StoredProcedureDefinition")
dbdefinition_TriggerDefinition = Class(name="dbdefinition_TriggerDefinition")
dbdefinition_ColumnDefinition = Class(name="dbdefinition_ColumnDefinition")
dbdefinition_ConstraintDefinition = Class(name="dbdefinition_ConstraintDefinition")
dbdefinition_ExtendedDefinition = Class(name="dbdefinition_ExtendedDefinition")
dbdefinition_IndexDefinition = Class(name="dbdefinition_IndexDefinition")
dbdefinition_TableDefinition = Class(name="dbdefinition_TableDefinition")
dbdefinition_SequenceDefinition = Class(name="dbdefinition_SequenceDefinition")
dbdefinition_SchemaDefinition = Class(name="dbdefinition_SchemaDefinition")
dbdefinition_ViewDefinition = Class(name="dbdefinition_ViewDefinition")
dbdefinition_DebuggerDefinition = Class(name="dbdefinition_DebuggerDefinition")
dbdefinition_PrivilegedElementDefinition = Class(name="dbdefinition_PrivilegedElementDefinition")
dbdefinition_ConstructedDataTypeDefinition = Class(name="dbdefinition_ConstructedDataTypeDefinition")
dbdefinition_FieldQualifierDefinition = Class(name="dbdefinition_FieldQualifierDefinition")
dbdefinition_PrivilegeDefinition = Class(name="dbdefinition_PrivilegeDefinition")

# dbdefinition_DatabaseVendorDefinition class attributes and methods
dbdefinition_DatabaseVendorDefinition_domainSupported: Property = Property(name="domainSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_SQLStatementSupported: Property = Property(name="SQLStatementSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_nicknameSupported: Property = Property(name="nicknameSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_quotedDMLSupported: Property = Property(name="quotedDMLSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_quotedDDLSupported: Property = Property(name="quotedDDLSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_xmlSupported: Property = Property(name="xmlSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_mQTIndexSupported: Property = Property(name="mQTIndexSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_eventSupported: Property = Property(name="eventSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_sqlUDFSupported: Property = Property(name="sqlUDFSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_storedProcedureSupported: Property = Property(name="storedProcedureSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_packageSupported: Property = Property(name="packageSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_authorizationIdentifierSupported: Property = Property(name="authorizationIdentifierSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_vendor: Property = Property(name="vendor", type=StringType)
dbdefinition_DatabaseVendorDefinition_version: Property = Property(name="version", type=StringType)
dbdefinition_DatabaseVendorDefinition_constraintsSupported: Property = Property(name="constraintsSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_maximumIdentifierLength: Property = Property(name="maximumIdentifierLength", type=IntegerType)
dbdefinition_DatabaseVendorDefinition_triggerSupported: Property = Property(name="triggerSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_snapshotViewSupported: Property = Property(name="snapshotViewSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_joinSupported: Property = Property(name="joinSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_viewTriggerSupported: Property = Property(name="viewTriggerSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_tablespacesSupported: Property = Property(name="tablespacesSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_maximumCommentLength: Property = Property(name="maximumCommentLength", type=IntegerType)
dbdefinition_DatabaseVendorDefinition_sequenceSupported: Property = Property(name="sequenceSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_mQTSupported: Property = Property(name="mQTSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_schemaSupported: Property = Property(name="schemaSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_aliasSupported: Property = Property(name="aliasSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_synonymSupported: Property = Property(name="synonymSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_userDefinedTypeSupported: Property = Property(name="userDefinedTypeSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_roleSupported: Property = Property(name="roleSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_groupSupported: Property = Property(name="groupSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_userSupported: Property = Property(name="userSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_roleAuthorizationSupported: Property = Property(name="roleAuthorizationSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_constructedDataTypeSupported: Property = Property(name="constructedDataTypeSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition_uDFSupported: Property = Property(name="uDFSupported", type=BooleanType)
dbdefinition_DatabaseVendorDefinition.attributes={dbdefinition_DatabaseVendorDefinition_joinSupported, dbdefinition_DatabaseVendorDefinition_mQTSupported, dbdefinition_DatabaseVendorDefinition_packageSupported, dbdefinition_DatabaseVendorDefinition_triggerSupported, dbdefinition_DatabaseVendorDefinition_constraintsSupported, dbdefinition_DatabaseVendorDefinition_schemaSupported, dbdefinition_DatabaseVendorDefinition_version, dbdefinition_DatabaseVendorDefinition_SQLStatementSupported, dbdefinition_DatabaseVendorDefinition_nicknameSupported, dbdefinition_DatabaseVendorDefinition_roleAuthorizationSupported, dbdefinition_DatabaseVendorDefinition_constructedDataTypeSupported, dbdefinition_DatabaseVendorDefinition_viewTriggerSupported, dbdefinition_DatabaseVendorDefinition_groupSupported, dbdefinition_DatabaseVendorDefinition_authorizationIdentifierSupported, dbdefinition_DatabaseVendorDefinition_snapshotViewSupported, dbdefinition_DatabaseVendorDefinition_quotedDDLSupported, dbdefinition_DatabaseVendorDefinition_roleSupported, dbdefinition_DatabaseVendorDefinition_aliasSupported, dbdefinition_DatabaseVendorDefinition_eventSupported, dbdefinition_DatabaseVendorDefinition_quotedDMLSupported, dbdefinition_DatabaseVendorDefinition_xmlSupported, dbdefinition_DatabaseVendorDefinition_storedProcedureSupported, dbdefinition_DatabaseVendorDefinition_sequenceSupported, dbdefinition_DatabaseVendorDefinition_tablespacesSupported, dbdefinition_DatabaseVendorDefinition_uDFSupported, dbdefinition_DatabaseVendorDefinition_domainSupported, dbdefinition_DatabaseVendorDefinition_mQTIndexSupported, dbdefinition_DatabaseVendorDefinition_userSupported, dbdefinition_DatabaseVendorDefinition_maximumCommentLength, dbdefinition_DatabaseVendorDefinition_userDefinedTypeSupported, dbdefinition_DatabaseVendorDefinition_maximumIdentifierLength, dbdefinition_DatabaseVendorDefinition_synonymSupported, dbdefinition_DatabaseVendorDefinition_vendor, dbdefinition_DatabaseVendorDefinition_sqlUDFSupported}

# dbdefinition_PredefinedDataTypeDefinition class attributes and methods
dbdefinition_PredefinedDataTypeDefinition_maximumScale: Property = Property(name="maximumScale", type=IntegerType)
dbdefinition_PredefinedDataTypeDefinition_minimumScale: Property = Property(name="minimumScale", type=IntegerType)
dbdefinition_PredefinedDataTypeDefinition_defaultValueTypes: Property = Property(name="defaultValueTypes", type=StringType)
dbdefinition_PredefinedDataTypeDefinition_primitiveType: Property = Property(name="primitiveType", type=StringType)
dbdefinition_PredefinedDataTypeDefinition_name: Property = Property(name="name", type=StringType)
dbdefinition_PredefinedDataTypeDefinition_jdbcEnumType: Property = Property(name="jdbcEnumType", type=IntegerType)
dbdefinition_PredefinedDataTypeDefinition_characterSet: Property = Property(name="characterSet", type=StringType)
dbdefinition_PredefinedDataTypeDefinition_encodingScheme: Property = Property(name="encodingScheme", type=StringType)
dbdefinition_PredefinedDataTypeDefinition_characterSetSuffix: Property = Property(name="characterSetSuffix", type=StringType)
dbdefinition_PredefinedDataTypeDefinition_encodingSchemeSuffix: Property = Property(name="encodingSchemeSuffix", type=StringType)
dbdefinition_PredefinedDataTypeDefinition_javaClassName: Property = Property(name="javaClassName", type=StringType)
dbdefinition_PredefinedDataTypeDefinition_defaultLength: Property = Property(name="defaultLength", type=IntegerType)
dbdefinition_PredefinedDataTypeDefinition_lengthSupported: Property = Property(name="lengthSupported", type=BooleanType)
dbdefinition_PredefinedDataTypeDefinition_scaleSupported: Property = Property(name="scaleSupported", type=BooleanType)
dbdefinition_PredefinedDataTypeDefinition_precisionSupported: Property = Property(name="precisionSupported", type=BooleanType)
dbdefinition_PredefinedDataTypeDefinition_keyConstraintSupported: Property = Property(name="keyConstraintSupported", type=BooleanType)
dbdefinition_PredefinedDataTypeDefinition_identitySupported: Property = Property(name="identitySupported", type=BooleanType)
dbdefinition_PredefinedDataTypeDefinition_multipleColumnsSupported: Property = Property(name="multipleColumnsSupported", type=BooleanType)
dbdefinition_PredefinedDataTypeDefinition_nullableSupported: Property = Property(name="nullableSupported", type=BooleanType)
dbdefinition_PredefinedDataTypeDefinition_defaultSupported: Property = Property(name="defaultSupported", type=BooleanType)
dbdefinition_PredefinedDataTypeDefinition_clusteringSupported: Property = Property(name="clusteringSupported", type=BooleanType)
dbdefinition_PredefinedDataTypeDefinition_fillFactorSupported: Property = Property(name="fillFactorSupported", type=BooleanType)
dbdefinition_PredefinedDataTypeDefinition_bitDataSupported: Property = Property(name="bitDataSupported", type=BooleanType)
dbdefinition_PredefinedDataTypeDefinition_maximumValue: Property = Property(name="maximumValue", type=StringType)
dbdefinition_PredefinedDataTypeDefinition_minimumValue: Property = Property(name="minimumValue", type=StringType)
dbdefinition_PredefinedDataTypeDefinition_maximumLength: Property = Property(name="maximumLength", type=IntegerType)
dbdefinition_PredefinedDataTypeDefinition_maximumPrecision: Property = Property(name="maximumPrecision", type=IntegerType)
dbdefinition_PredefinedDataTypeDefinition_defaultPrecision: Property = Property(name="defaultPrecision", type=IntegerType)
dbdefinition_PredefinedDataTypeDefinition_defaultScale: Property = Property(name="defaultScale", type=IntegerType)
dbdefinition_PredefinedDataTypeDefinition_cutoffPrecision: Property = Property(name="cutoffPrecision", type=IntegerType)
dbdefinition_PredefinedDataTypeDefinition_lengthUnit: Property = Property(name="lengthUnit", type=StringType)
dbdefinition_PredefinedDataTypeDefinition_orderingSupported: Property = Property(name="orderingSupported", type=BooleanType)
dbdefinition_PredefinedDataTypeDefinition_groupingSupported: Property = Property(name="groupingSupported", type=BooleanType)
dbdefinition_PredefinedDataTypeDefinition_displayName: Property = Property(name="displayName", type=StringType)
dbdefinition_PredefinedDataTypeDefinition_displayNameSupported: Property = Property(name="displayNameSupported", type=BooleanType)
dbdefinition_PredefinedDataTypeDefinition_leadingFieldQualifierSupported: Property = Property(name="leadingFieldQualifierSupported", type=BooleanType)
dbdefinition_PredefinedDataTypeDefinition_trailingFieldQualifierSupported: Property = Property(name="trailingFieldQualifierSupported", type=BooleanType)
dbdefinition_PredefinedDataTypeDefinition_fieldQualifierSeparator: Property = Property(name="fieldQualifierSeparator", type=StringType)
dbdefinition_PredefinedDataTypeDefinition_largeValueSpecifierSupported: Property = Property(name="largeValueSpecifierSupported", type=BooleanType)
dbdefinition_PredefinedDataTypeDefinition_largeValueSpecifierName: Property = Property(name="largeValueSpecifierName", type=StringType)
dbdefinition_PredefinedDataTypeDefinition_largeValueSpecifierLength: Property = Property(name="largeValueSpecifierLength", type=IntegerType)
dbdefinition_PredefinedDataTypeDefinition_lengthSemanticSupported: Property = Property(name="lengthSemanticSupported", type=BooleanType)
dbdefinition_PredefinedDataTypeDefinition_lengthSemantic: Property = Property(name="lengthSemantic", type=StringType)
dbdefinition_PredefinedDataTypeDefinition_languageType: Property = Property(name="languageType", type=StringType)
dbdefinition_PredefinedDataTypeDefinition.attributes={dbdefinition_PredefinedDataTypeDefinition_characterSet, dbdefinition_PredefinedDataTypeDefinition_minimumValue, dbdefinition_PredefinedDataTypeDefinition_languageType, dbdefinition_PredefinedDataTypeDefinition_precisionSupported, dbdefinition_PredefinedDataTypeDefinition_fillFactorSupported, dbdefinition_PredefinedDataTypeDefinition_identitySupported, dbdefinition_PredefinedDataTypeDefinition_defaultLength, dbdefinition_PredefinedDataTypeDefinition_characterSetSuffix, dbdefinition_PredefinedDataTypeDefinition_maximumPrecision, dbdefinition_PredefinedDataTypeDefinition_multipleColumnsSupported, dbdefinition_PredefinedDataTypeDefinition_maximumValue, dbdefinition_PredefinedDataTypeDefinition_defaultPrecision, dbdefinition_PredefinedDataTypeDefinition_largeValueSpecifierName, dbdefinition_PredefinedDataTypeDefinition_groupingSupported, dbdefinition_PredefinedDataTypeDefinition_fieldQualifierSeparator, dbdefinition_PredefinedDataTypeDefinition_encodingScheme, dbdefinition_PredefinedDataTypeDefinition_orderingSupported, dbdefinition_PredefinedDataTypeDefinition_javaClassName, dbdefinition_PredefinedDataTypeDefinition_clusteringSupported, dbdefinition_PredefinedDataTypeDefinition_bitDataSupported, dbdefinition_PredefinedDataTypeDefinition_maximumScale, dbdefinition_PredefinedDataTypeDefinition_largeValueSpecifierSupported, dbdefinition_PredefinedDataTypeDefinition_nullableSupported, dbdefinition_PredefinedDataTypeDefinition_name, dbdefinition_PredefinedDataTypeDefinition_lengthSemantic, dbdefinition_PredefinedDataTypeDefinition_defaultScale, dbdefinition_PredefinedDataTypeDefinition_defaultSupported, dbdefinition_PredefinedDataTypeDefinition_lengthSemanticSupported, dbdefinition_PredefinedDataTypeDefinition_keyConstraintSupported, dbdefinition_PredefinedDataTypeDefinition_lengthSupported, dbdefinition_PredefinedDataTypeDefinition_lengthUnit, dbdefinition_PredefinedDataTypeDefinition_displayNameSupported, dbdefinition_PredefinedDataTypeDefinition_encodingSchemeSuffix, dbdefinition_PredefinedDataTypeDefinition_trailingFieldQualifierSupported, dbdefinition_PredefinedDataTypeDefinition_leadingFieldQualifierSupported, dbdefinition_PredefinedDataTypeDefinition_defaultValueTypes, dbdefinition_PredefinedDataTypeDefinition_jdbcEnumType, dbdefinition_PredefinedDataTypeDefinition_maximumLength, dbdefinition_PredefinedDataTypeDefinition_primitiveType, dbdefinition_PredefinedDataTypeDefinition_cutoffPrecision, dbdefinition_PredefinedDataTypeDefinition_largeValueSpecifierLength, dbdefinition_PredefinedDataTypeDefinition_scaleSupported, dbdefinition_PredefinedDataTypeDefinition_minimumScale, dbdefinition_PredefinedDataTypeDefinition_displayName}

# dbdefinition_UserDefinedTypeDefinition class attributes and methods
dbdefinition_UserDefinedTypeDefinition_defaultValueSupported: Property = Property(name="defaultValueSupported", type=BooleanType)
dbdefinition_UserDefinedTypeDefinition_distinctTypeSupported: Property = Property(name="distinctTypeSupported", type=BooleanType)
dbdefinition_UserDefinedTypeDefinition_structuredTypeSupported: Property = Property(name="structuredTypeSupported", type=BooleanType)
dbdefinition_UserDefinedTypeDefinition_maximumIdentifierLength: Property = Property(name="maximumIdentifierLength", type=IntegerType)
dbdefinition_UserDefinedTypeDefinition.attributes={dbdefinition_UserDefinedTypeDefinition_defaultValueSupported, dbdefinition_UserDefinedTypeDefinition_structuredTypeSupported, dbdefinition_UserDefinedTypeDefinition_maximumIdentifierLength, dbdefinition_UserDefinedTypeDefinition_distinctTypeSupported}

# dbdefinition_QueryDefinition class attributes and methods
dbdefinition_QueryDefinition_identifierQuoteString: Property = Property(name="identifierQuoteString", type=StringType)
dbdefinition_QueryDefinition_hostVariableMarker: Property = Property(name="hostVariableMarker", type=StringType)
dbdefinition_QueryDefinition_hostVariableMarkerSupported: Property = Property(name="hostVariableMarkerSupported", type=BooleanType)
dbdefinition_QueryDefinition_castExpressionSupported: Property = Property(name="castExpressionSupported", type=BooleanType)
dbdefinition_QueryDefinition_defaultKeywordForInsertValueSupported: Property = Property(name="defaultKeywordForInsertValueSupported", type=BooleanType)
dbdefinition_QueryDefinition_extendedGroupingSupported: Property = Property(name="extendedGroupingSupported", type=BooleanType)
dbdefinition_QueryDefinition_tableAliasInDeleteSupported: Property = Property(name="tableAliasInDeleteSupported", type=BooleanType)
dbdefinition_QueryDefinition.attributes={dbdefinition_QueryDefinition_extendedGroupingSupported, dbdefinition_QueryDefinition_defaultKeywordForInsertValueSupported, dbdefinition_QueryDefinition_identifierQuoteString, dbdefinition_QueryDefinition_castExpressionSupported, dbdefinition_QueryDefinition_hostVariableMarkerSupported, dbdefinition_QueryDefinition_hostVariableMarker, dbdefinition_QueryDefinition_tableAliasInDeleteSupported}

# dbdefinition_SQLSyntaxDefinition class attributes and methods
dbdefinition_SQLSyntaxDefinition_keywords: Property = Property(name="keywords", type=StringType)
dbdefinition_SQLSyntaxDefinition_operators: Property = Property(name="operators", type=StringType)
dbdefinition_SQLSyntaxDefinition_terminationCharacter: Property = Property(name="terminationCharacter", type=StringType)
dbdefinition_SQLSyntaxDefinition.attributes={dbdefinition_SQLSyntaxDefinition_operators, dbdefinition_SQLSyntaxDefinition_terminationCharacter, dbdefinition_SQLSyntaxDefinition_keywords}

# dbdefinition_NicknameDefinition class attributes and methods
dbdefinition_NicknameDefinition_constraintSupported: Property = Property(name="constraintSupported", type=BooleanType)
dbdefinition_NicknameDefinition_indexSupported: Property = Property(name="indexSupported", type=BooleanType)
dbdefinition_NicknameDefinition_maximumIdentifierLength: Property = Property(name="maximumIdentifierLength", type=IntegerType)
dbdefinition_NicknameDefinition.attributes={dbdefinition_NicknameDefinition_indexSupported, dbdefinition_NicknameDefinition_maximumIdentifierLength, dbdefinition_NicknameDefinition_constraintSupported}

# dbdefinition_TableSpaceDefinition class attributes and methods
dbdefinition_TableSpaceDefinition_typeSupported: Property = Property(name="typeSupported", type=BooleanType)
dbdefinition_TableSpaceDefinition_extentSizeSupported: Property = Property(name="extentSizeSupported", type=BooleanType)
dbdefinition_TableSpaceDefinition_prefetchSizeSupported: Property = Property(name="prefetchSizeSupported", type=BooleanType)
dbdefinition_TableSpaceDefinition_managedBySupported: Property = Property(name="managedBySupported", type=BooleanType)
dbdefinition_TableSpaceDefinition_pageSizeSupported: Property = Property(name="pageSizeSupported", type=BooleanType)
dbdefinition_TableSpaceDefinition_bufferPoolSupported: Property = Property(name="bufferPoolSupported", type=BooleanType)
dbdefinition_TableSpaceDefinition_defaultSupported: Property = Property(name="defaultSupported", type=BooleanType)
dbdefinition_TableSpaceDefinition_containerMaximumSizeSupported: Property = Property(name="containerMaximumSizeSupported", type=BooleanType)
dbdefinition_TableSpaceDefinition_containerInitialSizeSupported: Property = Property(name="containerInitialSizeSupported", type=BooleanType)
dbdefinition_TableSpaceDefinition_containerExtentSizeSupported: Property = Property(name="containerExtentSizeSupported", type=BooleanType)
dbdefinition_TableSpaceDefinition_tableSpaceType: Property = Property(name="tableSpaceType", type=StringType)
dbdefinition_TableSpaceDefinition_maximumIdentifierLength: Property = Property(name="maximumIdentifierLength", type=IntegerType)
dbdefinition_TableSpaceDefinition.attributes={dbdefinition_TableSpaceDefinition_containerInitialSizeSupported, dbdefinition_TableSpaceDefinition_tableSpaceType, dbdefinition_TableSpaceDefinition_maximumIdentifierLength, dbdefinition_TableSpaceDefinition_pageSizeSupported, dbdefinition_TableSpaceDefinition_prefetchSizeSupported, dbdefinition_TableSpaceDefinition_containerExtentSizeSupported, dbdefinition_TableSpaceDefinition_defaultSupported, dbdefinition_TableSpaceDefinition_typeSupported, dbdefinition_TableSpaceDefinition_bufferPoolSupported, dbdefinition_TableSpaceDefinition_containerMaximumSizeSupported, dbdefinition_TableSpaceDefinition_extentSizeSupported, dbdefinition_TableSpaceDefinition_managedBySupported}

# dbdefinition_StoredProcedureDefinition class attributes and methods
dbdefinition_StoredProcedureDefinition_nullInputActionSupported: Property = Property(name="nullInputActionSupported", type=BooleanType)
dbdefinition_StoredProcedureDefinition_packageGenerationSupported: Property = Property(name="packageGenerationSupported", type=BooleanType)
dbdefinition_StoredProcedureDefinition_determininsticSupported: Property = Property(name="determininsticSupported", type=BooleanType)
dbdefinition_StoredProcedureDefinition_returnedNullSupported: Property = Property(name="returnedNullSupported", type=BooleanType)
dbdefinition_StoredProcedureDefinition_returnedTypeDeclarationConstraintSupported: Property = Property(name="returnedTypeDeclarationConstraintSupported", type=BooleanType)
dbdefinition_StoredProcedureDefinition_parameterInitValueSupported: Property = Property(name="parameterInitValueSupported", type=BooleanType)
dbdefinition_StoredProcedureDefinition_parameterStyleSupported: Property = Property(name="parameterStyleSupported", type=BooleanType)
dbdefinition_StoredProcedureDefinition_returnTypeSupported: Property = Property(name="returnTypeSupported", type=BooleanType)
dbdefinition_StoredProcedureDefinition_parameterDeclarationConstraintSupported: Property = Property(name="parameterDeclarationConstraintSupported", type=BooleanType)
dbdefinition_StoredProcedureDefinition_maximumActionBodyLength: Property = Property(name="maximumActionBodyLength", type=IntegerType)
dbdefinition_StoredProcedureDefinition_parameterStyle: Property = Property(name="parameterStyle", type=StringType)
dbdefinition_StoredProcedureDefinition_languageType: Property = Property(name="languageType", type=StringType)
dbdefinition_StoredProcedureDefinition_functionLanguageType: Property = Property(name="functionLanguageType", type=StringType)
dbdefinition_StoredProcedureDefinition_procedureType: Property = Property(name="procedureType", type=StringType)
dbdefinition_StoredProcedureDefinition_maximumIdentifierLength: Property = Property(name="maximumIdentifierLength", type=IntegerType)
dbdefinition_StoredProcedureDefinition.attributes={dbdefinition_StoredProcedureDefinition_functionLanguageType, dbdefinition_StoredProcedureDefinition_returnedTypeDeclarationConstraintSupported, dbdefinition_StoredProcedureDefinition_packageGenerationSupported, dbdefinition_StoredProcedureDefinition_parameterStyleSupported, dbdefinition_StoredProcedureDefinition_maximumIdentifierLength, dbdefinition_StoredProcedureDefinition_languageType, dbdefinition_StoredProcedureDefinition_returnedNullSupported, dbdefinition_StoredProcedureDefinition_maximumActionBodyLength, dbdefinition_StoredProcedureDefinition_determininsticSupported, dbdefinition_StoredProcedureDefinition_procedureType, dbdefinition_StoredProcedureDefinition_parameterInitValueSupported, dbdefinition_StoredProcedureDefinition_parameterStyle, dbdefinition_StoredProcedureDefinition_returnTypeSupported, dbdefinition_StoredProcedureDefinition_nullInputActionSupported, dbdefinition_StoredProcedureDefinition_parameterDeclarationConstraintSupported}

# dbdefinition_TriggerDefinition class attributes and methods
dbdefinition_TriggerDefinition_maximumReferencePartLength: Property = Property(name="maximumReferencePartLength", type=IntegerType)
dbdefinition_TriggerDefinition_maximumActionBodyLength: Property = Property(name="maximumActionBodyLength", type=IntegerType)
dbdefinition_TriggerDefinition_typeSupported: Property = Property(name="typeSupported", type=BooleanType)
dbdefinition_TriggerDefinition_whenClauseSupported: Property = Property(name="whenClauseSupported", type=BooleanType)
dbdefinition_TriggerDefinition_granularitySupported: Property = Property(name="granularitySupported", type=BooleanType)
dbdefinition_TriggerDefinition_referencesClauseSupported: Property = Property(name="referencesClauseSupported", type=BooleanType)
dbdefinition_TriggerDefinition_perColumnUpdateTriggerSupported: Property = Property(name="perColumnUpdateTriggerSupported", type=BooleanType)
dbdefinition_TriggerDefinition_insteadOfTriggerSupported: Property = Property(name="insteadOfTriggerSupported", type=BooleanType)
dbdefinition_TriggerDefinition_rowTriggerReferenceSupported: Property = Property(name="rowTriggerReferenceSupported", type=BooleanType)
dbdefinition_TriggerDefinition_tableTriggerReferenceSupported: Property = Property(name="tableTriggerReferenceSupported", type=BooleanType)
dbdefinition_TriggerDefinition_maximumIdentifierLength: Property = Property(name="maximumIdentifierLength", type=IntegerType)
dbdefinition_TriggerDefinition.attributes={dbdefinition_TriggerDefinition_typeSupported, dbdefinition_TriggerDefinition_referencesClauseSupported, dbdefinition_TriggerDefinition_maximumActionBodyLength, dbdefinition_TriggerDefinition_rowTriggerReferenceSupported, dbdefinition_TriggerDefinition_maximumIdentifierLength, dbdefinition_TriggerDefinition_perColumnUpdateTriggerSupported, dbdefinition_TriggerDefinition_tableTriggerReferenceSupported, dbdefinition_TriggerDefinition_whenClauseSupported, dbdefinition_TriggerDefinition_maximumReferencePartLength, dbdefinition_TriggerDefinition_granularitySupported, dbdefinition_TriggerDefinition_insteadOfTriggerSupported}

# dbdefinition_ColumnDefinition class attributes and methods
dbdefinition_ColumnDefinition_identityStartValueSupported: Property = Property(name="identityStartValueSupported", type=BooleanType)
dbdefinition_ColumnDefinition_identityIncrementSupported: Property = Property(name="identityIncrementSupported", type=BooleanType)
dbdefinition_ColumnDefinition_identityMinimumSupported: Property = Property(name="identityMinimumSupported", type=BooleanType)
dbdefinition_ColumnDefinition_identityMaximumSupported: Property = Property(name="identityMaximumSupported", type=BooleanType)
dbdefinition_ColumnDefinition_identityCycleSupported: Property = Property(name="identityCycleSupported", type=BooleanType)
dbdefinition_ColumnDefinition_maximumIdentifierLength: Property = Property(name="maximumIdentifierLength", type=IntegerType)
dbdefinition_ColumnDefinition_identitySupported: Property = Property(name="identitySupported", type=BooleanType)
dbdefinition_ColumnDefinition_computedSupported: Property = Property(name="computedSupported", type=BooleanType)
dbdefinition_ColumnDefinition.attributes={dbdefinition_ColumnDefinition_computedSupported, dbdefinition_ColumnDefinition_identityCycleSupported, dbdefinition_ColumnDefinition_identitySupported, dbdefinition_ColumnDefinition_maximumIdentifierLength, dbdefinition_ColumnDefinition_identityIncrementSupported, dbdefinition_ColumnDefinition_identityMinimumSupported, dbdefinition_ColumnDefinition_identityStartValueSupported, dbdefinition_ColumnDefinition_identityMaximumSupported}

# dbdefinition_ConstraintDefinition class attributes and methods
dbdefinition_ConstraintDefinition_deferrableConstraintSupported: Property = Property(name="deferrableConstraintSupported", type=BooleanType)
dbdefinition_ConstraintDefinition_informationalConstraintSupported: Property = Property(name="informationalConstraintSupported", type=BooleanType)
dbdefinition_ConstraintDefinition_clusteredPrimaryKeySupported: Property = Property(name="clusteredPrimaryKeySupported", type=BooleanType)
dbdefinition_ConstraintDefinition_clusteredUniqueConstraintSupported: Property = Property(name="clusteredUniqueConstraintSupported", type=BooleanType)
dbdefinition_ConstraintDefinition_primaryKeyNullable: Property = Property(name="primaryKeyNullable", type=BooleanType)
dbdefinition_ConstraintDefinition_uniqueKeyNullable: Property = Property(name="uniqueKeyNullable", type=BooleanType)
dbdefinition_ConstraintDefinition_maximumCheckExpressionLength: Property = Property(name="maximumCheckExpressionLength", type=IntegerType)
dbdefinition_ConstraintDefinition_parentUpdateDRIRuleType: Property = Property(name="parentUpdateDRIRuleType", type=StringType)
dbdefinition_ConstraintDefinition_parentDeleteDRIRuleType: Property = Property(name="parentDeleteDRIRuleType", type=StringType)
dbdefinition_ConstraintDefinition_checkOption: Property = Property(name="checkOption", type=StringType)
dbdefinition_ConstraintDefinition_maximumPrimaryKeyIdentifierLength: Property = Property(name="maximumPrimaryKeyIdentifierLength", type=IntegerType)
dbdefinition_ConstraintDefinition_maximumForeignKeyIdentifierLength: Property = Property(name="maximumForeignKeyIdentifierLength", type=IntegerType)
dbdefinition_ConstraintDefinition_maximumCheckConstraintIdentifierLength: Property = Property(name="maximumCheckConstraintIdentifierLength", type=IntegerType)
dbdefinition_ConstraintDefinition.attributes={dbdefinition_ConstraintDefinition_maximumPrimaryKeyIdentifierLength, dbdefinition_ConstraintDefinition_primaryKeyNullable, dbdefinition_ConstraintDefinition_maximumCheckConstraintIdentifierLength, dbdefinition_ConstraintDefinition_clusteredUniqueConstraintSupported, dbdefinition_ConstraintDefinition_parentUpdateDRIRuleType, dbdefinition_ConstraintDefinition_deferrableConstraintSupported, dbdefinition_ConstraintDefinition_informationalConstraintSupported, dbdefinition_ConstraintDefinition_parentDeleteDRIRuleType, dbdefinition_ConstraintDefinition_maximumForeignKeyIdentifierLength, dbdefinition_ConstraintDefinition_uniqueKeyNullable, dbdefinition_ConstraintDefinition_checkOption, dbdefinition_ConstraintDefinition_clusteredPrimaryKeySupported, dbdefinition_ConstraintDefinition_maximumCheckExpressionLength}

# dbdefinition_ExtendedDefinition class attributes and methods
dbdefinition_ExtendedDefinition_name: Property = Property(name="name", type=StringType)
dbdefinition_ExtendedDefinition_value: Property = Property(name="value", type=StringType)
dbdefinition_ExtendedDefinition.attributes={dbdefinition_ExtendedDefinition_name, dbdefinition_ExtendedDefinition_value}

# dbdefinition_IndexDefinition class attributes and methods
dbdefinition_IndexDefinition_percentFreeTerminology: Property = Property(name="percentFreeTerminology", type=StringType)
dbdefinition_IndexDefinition_percentFreeChangeable: Property = Property(name="percentFreeChangeable", type=BooleanType)
dbdefinition_IndexDefinition_clusteringSupported: Property = Property(name="clusteringSupported", type=BooleanType)
dbdefinition_IndexDefinition_clusterChangeable: Property = Property(name="clusterChangeable", type=BooleanType)
dbdefinition_IndexDefinition_fillFactorSupported: Property = Property(name="fillFactorSupported", type=BooleanType)
dbdefinition_IndexDefinition_includedColumnsSupported: Property = Property(name="includedColumnsSupported", type=BooleanType)
dbdefinition_IndexDefinition_maximumIdentifierLength: Property = Property(name="maximumIdentifierLength", type=IntegerType)
dbdefinition_IndexDefinition.attributes={dbdefinition_IndexDefinition_clusteringSupported, dbdefinition_IndexDefinition_percentFreeChangeable, dbdefinition_IndexDefinition_maximumIdentifierLength, dbdefinition_IndexDefinition_clusterChangeable, dbdefinition_IndexDefinition_percentFreeTerminology, dbdefinition_IndexDefinition_fillFactorSupported, dbdefinition_IndexDefinition_includedColumnsSupported}

# dbdefinition_TableDefinition class attributes and methods
dbdefinition_TableDefinition_maximumIdentifierLength: Property = Property(name="maximumIdentifierLength", type=IntegerType)
dbdefinition_TableDefinition_auditSupported: Property = Property(name="auditSupported", type=BooleanType)
dbdefinition_TableDefinition_dataCaptureSupported: Property = Property(name="dataCaptureSupported", type=BooleanType)
dbdefinition_TableDefinition_editProcSupported: Property = Property(name="editProcSupported", type=BooleanType)
dbdefinition_TableDefinition_encodingSupported: Property = Property(name="encodingSupported", type=BooleanType)
dbdefinition_TableDefinition_validProcSupported: Property = Property(name="validProcSupported", type=BooleanType)
dbdefinition_TableDefinition.attributes={dbdefinition_TableDefinition_validProcSupported, dbdefinition_TableDefinition_editProcSupported, dbdefinition_TableDefinition_auditSupported, dbdefinition_TableDefinition_encodingSupported, dbdefinition_TableDefinition_dataCaptureSupported, dbdefinition_TableDefinition_maximumIdentifierLength}

# dbdefinition_SequenceDefinition class attributes and methods
dbdefinition_SequenceDefinition_typeEnumerationSupported: Property = Property(name="typeEnumerationSupported", type=BooleanType)
dbdefinition_SequenceDefinition_cacheSupported: Property = Property(name="cacheSupported", type=BooleanType)
dbdefinition_SequenceDefinition_orderSupported: Property = Property(name="orderSupported", type=BooleanType)
dbdefinition_SequenceDefinition_noMaximumValueString: Property = Property(name="noMaximumValueString", type=StringType)
dbdefinition_SequenceDefinition_noMinimumValueString: Property = Property(name="noMinimumValueString", type=StringType)
dbdefinition_SequenceDefinition_noCacheString: Property = Property(name="noCacheString", type=StringType)
dbdefinition_SequenceDefinition_cacheDefaultValue: Property = Property(name="cacheDefaultValue", type=IntegerType)
dbdefinition_SequenceDefinition.attributes={dbdefinition_SequenceDefinition_typeEnumerationSupported, dbdefinition_SequenceDefinition_noCacheString, dbdefinition_SequenceDefinition_noMaximumValueString, dbdefinition_SequenceDefinition_cacheSupported, dbdefinition_SequenceDefinition_noMinimumValueString, dbdefinition_SequenceDefinition_cacheDefaultValue, dbdefinition_SequenceDefinition_orderSupported}

# dbdefinition_SchemaDefinition class attributes and methods
dbdefinition_SchemaDefinition_maximumIdentifierLength: Property = Property(name="maximumIdentifierLength", type=IntegerType)
dbdefinition_SchemaDefinition.attributes={dbdefinition_SchemaDefinition_maximumIdentifierLength}

# dbdefinition_ViewDefinition class attributes and methods
dbdefinition_ViewDefinition_maximumIdentifierLength: Property = Property(name="maximumIdentifierLength", type=IntegerType)
dbdefinition_ViewDefinition_indexSupported: Property = Property(name="indexSupported", type=BooleanType)
dbdefinition_ViewDefinition_checkOptionSupported: Property = Property(name="checkOptionSupported", type=BooleanType)
dbdefinition_ViewDefinition_checkOptionLevelsSupported: Property = Property(name="checkOptionLevelsSupported", type=BooleanType)
dbdefinition_ViewDefinition.attributes={dbdefinition_ViewDefinition_indexSupported, dbdefinition_ViewDefinition_checkOptionLevelsSupported, dbdefinition_ViewDefinition_checkOptionSupported, dbdefinition_ViewDefinition_maximumIdentifierLength}

# dbdefinition_DebuggerDefinition class attributes and methods
dbdefinition_DebuggerDefinition_conditionSupported: Property = Property(name="conditionSupported", type=BooleanType)
dbdefinition_DebuggerDefinition.attributes={dbdefinition_DebuggerDefinition_conditionSupported}

# dbdefinition_PrivilegedElementDefinition class attributes and methods
dbdefinition_PrivilegedElementDefinition_name: Property = Property(name="name", type=StringType)
dbdefinition_PrivilegedElementDefinition.attributes={dbdefinition_PrivilegedElementDefinition_name}

# dbdefinition_ConstructedDataTypeDefinition class attributes and methods
dbdefinition_ConstructedDataTypeDefinition_arrayDatatypeSupported: Property = Property(name="arrayDatatypeSupported", type=BooleanType)
dbdefinition_ConstructedDataTypeDefinition_multisetDatatypeSupported: Property = Property(name="multisetDatatypeSupported", type=BooleanType)
dbdefinition_ConstructedDataTypeDefinition_rowDatatypeSupported: Property = Property(name="rowDatatypeSupported", type=BooleanType)
dbdefinition_ConstructedDataTypeDefinition_referenceDatatypeSupported: Property = Property(name="referenceDatatypeSupported", type=BooleanType)
dbdefinition_ConstructedDataTypeDefinition_cursorDatatypeSupported: Property = Property(name="cursorDatatypeSupported", type=BooleanType)
dbdefinition_ConstructedDataTypeDefinition.attributes={dbdefinition_ConstructedDataTypeDefinition_arrayDatatypeSupported, dbdefinition_ConstructedDataTypeDefinition_cursorDatatypeSupported, dbdefinition_ConstructedDataTypeDefinition_referenceDatatypeSupported, dbdefinition_ConstructedDataTypeDefinition_multisetDatatypeSupported, dbdefinition_ConstructedDataTypeDefinition_rowDatatypeSupported}

# dbdefinition_FieldQualifierDefinition class attributes and methods
dbdefinition_FieldQualifierDefinition_name: Property = Property(name="name", type=StringType)
dbdefinition_FieldQualifierDefinition_maximumPrecision: Property = Property(name="maximumPrecision", type=IntegerType)
dbdefinition_FieldQualifierDefinition_defaultPrecision: Property = Property(name="defaultPrecision", type=IntegerType)
dbdefinition_FieldQualifierDefinition_precisionSupported: Property = Property(name="precisionSupported", type=BooleanType)
dbdefinition_FieldQualifierDefinition_maximumScale: Property = Property(name="maximumScale", type=IntegerType)
dbdefinition_FieldQualifierDefinition_defaultScale: Property = Property(name="defaultScale", type=IntegerType)
dbdefinition_FieldQualifierDefinition_scaleSupported: Property = Property(name="scaleSupported", type=BooleanType)
dbdefinition_FieldQualifierDefinition.attributes={dbdefinition_FieldQualifierDefinition_defaultScale, dbdefinition_FieldQualifierDefinition_scaleSupported, dbdefinition_FieldQualifierDefinition_precisionSupported, dbdefinition_FieldQualifierDefinition_maximumPrecision, dbdefinition_FieldQualifierDefinition_name, dbdefinition_FieldQualifierDefinition_defaultPrecision, dbdefinition_FieldQualifierDefinition_maximumScale}

# dbdefinition_PrivilegeDefinition class attributes and methods
dbdefinition_PrivilegeDefinition_name: Property = Property(name="name", type=StringType)
dbdefinition_PrivilegeDefinition.attributes={dbdefinition_PrivilegeDefinition_name}

# Relationships
udtDefinition19: BinaryAssociation = BinaryAssociation(
    name="udtDefinition19",
    ends={
        Property(name="dbdefinition_UserDefinedTypeDefinition", type=dbdefinition_DatabaseVendorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_DatabaseVendorDefinition20", type=dbdefinition_UserDefinedTypeDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
queryDefinition21: BinaryAssociation = BinaryAssociation(
    name="queryDefinition21",
    ends={
        Property(name="dbdefinition_QueryDefinition", type=dbdefinition_DatabaseVendorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_DatabaseVendorDefinition22", type=dbdefinition_QueryDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
SQLSyntaxDefinition23: BinaryAssociation = BinaryAssociation(
    name="SQLSyntaxDefinition23",
    ends={
        Property(name="dbdefinition_SQLSyntaxDefinition", type=dbdefinition_DatabaseVendorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_DatabaseVendorDefinition24", type=dbdefinition_SQLSyntaxDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nicknameDefinition25: BinaryAssociation = BinaryAssociation(
    name="nicknameDefinition25",
    ends={
        Property(name="dbdefinition_NicknameDefinition", type=dbdefinition_DatabaseVendorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_DatabaseVendorDefinition26", type=dbdefinition_NicknameDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
predefinedDataTypeDefinitions0: BinaryAssociation = BinaryAssociation(
    name="predefinedDataTypeDefinitions0",
    ends={
        Property(name="dbdefinition_PredefinedDataTypeDefinition", type=dbdefinition_DatabaseVendorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_DatabaseVendorDefinition", type=dbdefinition_PredefinedDataTypeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tableSpaceDefinition1: BinaryAssociation = BinaryAssociation(
    name="tableSpaceDefinition1",
    ends={
        Property(name="dbdefinition_TableSpaceDefinition", type=dbdefinition_DatabaseVendorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_DatabaseVendorDefinition2", type=dbdefinition_TableSpaceDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
storedProcedureDefinition3: BinaryAssociation = BinaryAssociation(
    name="storedProcedureDefinition3",
    ends={
        Property(name="dbdefinition_StoredProcedureDefinition", type=dbdefinition_DatabaseVendorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_DatabaseVendorDefinition4", type=dbdefinition_StoredProcedureDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
triggerDefinition5: BinaryAssociation = BinaryAssociation(
    name="triggerDefinition5",
    ends={
        Property(name="dbdefinition_TriggerDefinition", type=dbdefinition_DatabaseVendorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_DatabaseVendorDefinition6", type=dbdefinition_TriggerDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
columnDefinition7: BinaryAssociation = BinaryAssociation(
    name="columnDefinition7",
    ends={
        Property(name="dbdefinition_ColumnDefinition", type=dbdefinition_DatabaseVendorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_DatabaseVendorDefinition8", type=dbdefinition_ColumnDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constraintDefinition9: BinaryAssociation = BinaryAssociation(
    name="constraintDefinition9",
    ends={
        Property(name="dbdefinition_ConstraintDefinition", type=dbdefinition_DatabaseVendorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_DatabaseVendorDefinition10", type=dbdefinition_ConstraintDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extendedDefinitions11: BinaryAssociation = BinaryAssociation(
    name="extendedDefinitions11",
    ends={
        Property(name="dbdefinition_ExtendedDefinition", type=dbdefinition_DatabaseVendorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_DatabaseVendorDefinition12", type=dbdefinition_ExtendedDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
indexDefinition13: BinaryAssociation = BinaryAssociation(
    name="indexDefinition13",
    ends={
        Property(name="dbdefinition_IndexDefinition", type=dbdefinition_DatabaseVendorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_DatabaseVendorDefinition14", type=dbdefinition_IndexDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tableDefinition15: BinaryAssociation = BinaryAssociation(
    name="tableDefinition15",
    ends={
        Property(name="dbdefinition_TableDefinition", type=dbdefinition_DatabaseVendorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_DatabaseVendorDefinition16", type=dbdefinition_TableDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sequenceDefinition17: BinaryAssociation = BinaryAssociation(
    name="sequenceDefinition17",
    ends={
        Property(name="dbdefinition_SequenceDefinition", type=dbdefinition_DatabaseVendorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_DatabaseVendorDefinition18", type=dbdefinition_SequenceDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
schemaDefinition27: BinaryAssociation = BinaryAssociation(
    name="schemaDefinition27",
    ends={
        Property(name="dbdefinition_SchemaDefinition", type=dbdefinition_DatabaseVendorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_DatabaseVendorDefinition28", type=dbdefinition_SchemaDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
viewDefinition29: BinaryAssociation = BinaryAssociation(
    name="viewDefinition29",
    ends={
        Property(name="dbdefinition_ViewDefinition", type=dbdefinition_DatabaseVendorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_DatabaseVendorDefinition30", type=dbdefinition_ViewDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
debuggerDefinition31: BinaryAssociation = BinaryAssociation(
    name="debuggerDefinition31",
    ends={
        Property(name="dbdefinition_DebuggerDefinition", type=dbdefinition_DatabaseVendorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_DatabaseVendorDefinition32", type=dbdefinition_DebuggerDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
privilegedElementDefinitions33: BinaryAssociation = BinaryAssociation(
    name="privilegedElementDefinitions33",
    ends={
        Property(name="dbdefinition_PrivilegedElementDefinition", type=dbdefinition_DatabaseVendorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_DatabaseVendorDefinition34", type=dbdefinition_PrivilegedElementDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constructedDataTypeDefinition35: BinaryAssociation = BinaryAssociation(
    name="constructedDataTypeDefinition35",
    ends={
        Property(name="dbdefinition_ConstructedDataTypeDefinition", type=dbdefinition_DatabaseVendorDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_DatabaseVendorDefinition36", type=dbdefinition_ConstructedDataTypeDefinition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leadingFieldQualifierDefinition37: BinaryAssociation = BinaryAssociation(
    name="leadingFieldQualifierDefinition37",
    ends={
        Property(name="dbdefinition_FieldQualifierDefinition", type=dbdefinition_PredefinedDataTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_PredefinedDataTypeDefinition38", type=dbdefinition_FieldQualifierDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trailingFieldQualifierDefinition39: BinaryAssociation = BinaryAssociation(
    name="trailingFieldQualifierDefinition39",
    ends={
        Property(name="dbdefinition_FieldQualifierDefinition41", type=dbdefinition_PredefinedDataTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_PredefinedDataTypeDefinition40", type=dbdefinition_FieldQualifierDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultTrailingFieldQualifierDefinition42: BinaryAssociation = BinaryAssociation(
    name="defaultTrailingFieldQualifierDefinition42",
    ends={
        Property(name="dbdefinition_FieldQualifierDefinition44", type=dbdefinition_PredefinedDataTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_PredefinedDataTypeDefinition43", type=dbdefinition_FieldQualifierDefinition, multiplicity=Multiplicity(0, 1))
    }
)
defaultLeadingFieldQualifierDefinition45: BinaryAssociation = BinaryAssociation(
    name="defaultLeadingFieldQualifierDefinition45",
    ends={
        Property(name="dbdefinition_FieldQualifierDefinition47", type=dbdefinition_PredefinedDataTypeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_PredefinedDataTypeDefinition46", type=dbdefinition_FieldQualifierDefinition, multiplicity=Multiplicity(0, 1))
    }
)
predefinedDataTypeDefinitions48: BinaryAssociation = BinaryAssociation(
    name="predefinedDataTypeDefinitions48",
    ends={
        Property(name="dbdefinition_PredefinedDataTypeDefinition50", type=dbdefinition_StoredProcedureDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_StoredProcedureDefinition49", type=dbdefinition_PredefinedDataTypeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identityColumnDataTypeDefinitions51: BinaryAssociation = BinaryAssociation(
    name="identityColumnDataTypeDefinitions51",
    ends={
        Property(name="dbdefinition_PredefinedDataTypeDefinition53", type=dbdefinition_ColumnDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_ColumnDefinition52", type=dbdefinition_PredefinedDataTypeDefinition, multiplicity=Multiplicity(1, 9999))
    }
)
predefinedDataTypeDefinitions54: BinaryAssociation = BinaryAssociation(
    name="predefinedDataTypeDefinitions54",
    ends={
        Property(name="dbdefinition_PredefinedDataTypeDefinition56", type=dbdefinition_SequenceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_SequenceDefinition55", type=dbdefinition_PredefinedDataTypeDefinition, multiplicity=Multiplicity(1, 9999))
    }
)
defaultDataTypeDefinition57: BinaryAssociation = BinaryAssociation(
    name="defaultDataTypeDefinition57",
    ends={
        Property(name="dbdefinition_PredefinedDataTypeDefinition59", type=dbdefinition_SequenceDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_SequenceDefinition58", type=dbdefinition_PredefinedDataTypeDefinition, multiplicity=Multiplicity(1, 1))
    }
)
validTrailingFieldQualifierDefinitions61: BinaryAssociation = BinaryAssociation(
    name="validTrailingFieldQualifierDefinitions61",
    ends={
        Property(name="dbdefinition_FieldQualifierDefinition62", type=dbdefinition_FieldQualifierDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_FieldQualifierDefinition60", type=dbdefinition_FieldQualifierDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
privilegeDefinitions63: BinaryAssociation = BinaryAssociation(
    name="privilegeDefinitions63",
    ends={
        Property(name="dbdefinition_PrivilegeDefinition", type=dbdefinition_PrivilegedElementDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_PrivilegedElementDefinition64", type=dbdefinition_PrivilegeDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionElementDefinitions65: BinaryAssociation = BinaryAssociation(
    name="actionElementDefinitions65",
    ends={
        Property(name="dbdefinition_PrivilegedElementDefinition67", type=dbdefinition_PrivilegeDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="dbdefinition_PrivilegeDefinition66", type=dbdefinition_PrivilegedElementDefinition, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="dbdefinition",
    types={dbdefinition_DatabaseVendorDefinition, dbdefinition_PredefinedDataTypeDefinition, dbdefinition_UserDefinedTypeDefinition, dbdefinition_QueryDefinition, dbdefinition_SQLSyntaxDefinition, dbdefinition_NicknameDefinition, dbdefinition_TableSpaceDefinition, dbdefinition_StoredProcedureDefinition, dbdefinition_TriggerDefinition, dbdefinition_ColumnDefinition, dbdefinition_ConstraintDefinition, dbdefinition_ExtendedDefinition, dbdefinition_IndexDefinition, dbdefinition_TableDefinition, dbdefinition_SequenceDefinition, dbdefinition_SchemaDefinition, dbdefinition_ViewDefinition, dbdefinition_DebuggerDefinition, dbdefinition_PrivilegedElementDefinition, dbdefinition_ConstructedDataTypeDefinition, dbdefinition_FieldQualifierDefinition, dbdefinition_PrivilegeDefinition, ParameterStyle, ParentDeleteDRIRuleType, CheckOption, LanguageType, ParentUpdateDRIRuleType, ProcedureType, TableSpaceType, PercentFreeTerminology, LengthUnit},
    associations={udtDefinition19, queryDefinition21, SQLSyntaxDefinition23, nicknameDefinition25, predefinedDataTypeDefinitions0, tableSpaceDefinition1, storedProcedureDefinition3, triggerDefinition5, columnDefinition7, constraintDefinition9, extendedDefinitions11, indexDefinition13, tableDefinition15, sequenceDefinition17, schemaDefinition27, viewDefinition29, debuggerDefinition31, privilegedElementDefinitions33, constructedDataTypeDefinition35, leadingFieldQualifierDefinition37, trailingFieldQualifierDefinition39, defaultTrailingFieldQualifierDefinition42, defaultLeadingFieldQualifierDefinition45, predefinedDataTypeDefinitions48, identityColumnDataTypeDefinitions51, predefinedDataTypeDefinitions54, defaultDataTypeDefinition57, validTrailingFieldQualifierDefinitions61, privilegeDefinitions63, actionElementDefinitions65},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)