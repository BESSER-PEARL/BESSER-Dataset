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
DatabaseProperties: Enumeration = Enumeration(
    name="DatabaseProperties",
    literals={
            EnumerationLiteral(name="Password"),
			EnumerationLiteral(name="ServerName"),
			EnumerationLiteral(name="DatasourceName"),
			EnumerationLiteral(name="FileFieldName"),
			EnumerationLiteral(name="Schema"),
			EnumerationLiteral(name="SID"),
			EnumerationLiteral(name="SqlSynthax"),
			EnumerationLiteral(name="StringQuote"),
			EnumerationLiteral(name="NullChar"),
			EnumerationLiteral(name="DatabaseType"),
			EnumerationLiteral(name="DriverClass"),
			EnumerationLiteral(name="URL"),
			EnumerationLiteral(name="Port"),
			EnumerationLiteral(name="Username")
    }
)

FileFormat: Enumeration = Enumeration(
    name="FileFormat",
    literals={
            EnumerationLiteral(name="UNIX"),
			EnumerationLiteral(name="MAC"),
			EnumerationLiteral(name="WINDOWS")
    }
)

FieldSeparator: Enumeration = Enumeration(
    name="FieldSeparator",
    literals={
            EnumerationLiteral(name="Tabulation"),
			EnumerationLiteral(name="Semicolon"),
			EnumerationLiteral(name="Comma"),
			EnumerationLiteral(name="Space"),
			EnumerationLiteral(name="Alt_65"),
			EnumerationLiteral(name="Custom_ANSI"),
			EnumerationLiteral(name="Custom_UTF8"),
			EnumerationLiteral(name="Custom_RegExp")
    }
)

Escape: Enumeration = Enumeration(
    name="Escape",
    literals={
            EnumerationLiteral(name="Delimited"),
			EnumerationLiteral(name="CSV")
    }
)

RowSeparator: Enumeration = Enumeration(
    name="RowSeparator",
    literals={
            EnumerationLiteral(name="Custom_String"),
			EnumerationLiteral(name="Standart_EOL")
    }
)

# Classes
connection_Metadata = Class(name="connection_Metadata")
connection_MetadataColumn = Class(name="connection_MetadataColumn")
connection_AbstractMetadataObject = Class(name="connection_AbstractMetadataObject", is_abstract=True)
AbstractMetadataObject = Class(name="AbstractMetadataObject")
connection_Connection = Class(name="connection_Connection")
connection_MetadataTable = Class(name="connection_MetadataTable")
connection_QueriesConnection = Class(name="connection_QueriesConnection")
connection_FileConnection = Class(name="connection_FileConnection", is_abstract=True)
Connection = Class(name="Connection")
connection_Concept = Class(name="connection_Concept")
connection_DelimitedFileConnection = Class(name="connection_DelimitedFileConnection")
FileConnection = Class(name="FileConnection")
connection_PositionalFileConnection = Class(name="connection_PositionalFileConnection")
connection_EbcdicConnection = Class(name="connection_EbcdicConnection")
connection_MDMConnection = Class(name="connection_MDMConnection")
connection_DatabaseConnection = Class(name="connection_DatabaseConnection")
connection_SAPFunctionUnit = Class(name="connection_SAPFunctionUnit")
connection_CDCConnection = Class(name="connection_CDCConnection")
connection_SAPConnection = Class(name="connection_SAPConnection")
connection_SAPTestInputParameterTable = Class(name="connection_SAPTestInputParameterTable")
connection_SAPFunctionParameterColumn = Class(name="connection_SAPFunctionParameterColumn")
connection_InputSAPFunctionParameterTable = Class(name="connection_InputSAPFunctionParameterTable")
connection_OutputSAPFunctionParameterTable = Class(name="connection_OutputSAPFunctionParameterTable")
connection_RegexpFileConnection = Class(name="connection_RegexpFileConnection")
connection_XmlFileConnection = Class(name="connection_XmlFileConnection")
connection_XmlXPathLoopDescriptor = Class(name="connection_XmlXPathLoopDescriptor")
connection_SchemaTarget = Class(name="connection_SchemaTarget")
connection_SAPFunctionParameterTable = Class(name="connection_SAPFunctionParameterTable")
SAPFunctionParameterTable = Class(name="SAPFunctionParameterTable")
connection_GenericSchemaConnection = Class(name="connection_GenericSchemaConnection")
connection_LDAPSchemaConnection = Class(name="connection_LDAPSchemaConnection")
connection_Query = Class(name="connection_Query")
connection_LdifFileConnection = Class(name="connection_LdifFileConnection")
connection_FileExcelConnection = Class(name="connection_FileExcelConnection")
connection_WSDLSchemaConnection = Class(name="connection_WSDLSchemaConnection")
connection_SalesforceSchemaConnection = Class(name="connection_SalesforceSchemaConnection")
connection_SubscriberTable = Class(name="connection_SubscriberTable")
MetadataTable = Class(name="MetadataTable")
connection_ConceptTarget = Class(name="connection_ConceptTarget")
connection_CDCType = Class(name="connection_CDCType")
connection_HL7Connection = Class(name="connection_HL7Connection")

# connection_Metadata class attributes and methods

# connection_MetadataColumn class attributes and methods
connection_MetadataColumn_sourceType: Property = Property(name="sourceType", type=StringType)
connection_MetadataColumn_defaultValue: Property = Property(name="defaultValue", type=StringType)
connection_MetadataColumn_talendType: Property = Property(name="talendType", type=StringType)
connection_MetadataColumn_key: Property = Property(name="key", type=BooleanType)
connection_MetadataColumn_nullable: Property = Property(name="nullable", type=BooleanType)
connection_MetadataColumn_length: Property = Property(name="length", type=IntegerType)
connection_MetadataColumn_precision: Property = Property(name="precision", type=IntegerType)
connection_MetadataColumn_originalField: Property = Property(name="originalField", type=StringType)
connection_MetadataColumn_pattern: Property = Property(name="pattern", type=StringType)
connection_MetadataColumn_displayField: Property = Property(name="displayField", type=StringType)
connection_MetadataColumn.attributes={connection_MetadataColumn_precision, connection_MetadataColumn_defaultValue, connection_MetadataColumn_sourceType, connection_MetadataColumn_key, connection_MetadataColumn_pattern, connection_MetadataColumn_talendType, connection_MetadataColumn_originalField, connection_MetadataColumn_displayField, connection_MetadataColumn_nullable, connection_MetadataColumn_length}

# connection_AbstractMetadataObject class attributes and methods
connection_AbstractMetadataObject_properties: Property = Property(name="properties", type=StringType)
connection_AbstractMetadataObject_id: Property = Property(name="id", type=StringType)
connection_AbstractMetadataObject_comment: Property = Property(name="comment", type=StringType)
connection_AbstractMetadataObject_label: Property = Property(name="label", type=StringType)
connection_AbstractMetadataObject_readOnly: Property = Property(name="readOnly", type=BooleanType)
connection_AbstractMetadataObject_synchronised: Property = Property(name="synchronised", type=BooleanType)
connection_AbstractMetadataObject_divergency: Property = Property(name="divergency", type=BooleanType)
connection_AbstractMetadataObject.attributes={connection_AbstractMetadataObject_readOnly, connection_AbstractMetadataObject_id, connection_AbstractMetadataObject_label, connection_AbstractMetadataObject_properties, connection_AbstractMetadataObject_comment, connection_AbstractMetadataObject_synchronised, connection_AbstractMetadataObject_divergency}

# AbstractMetadataObject class attributes and methods

# connection_Connection class attributes and methods
connection_Connection_ContextMode: Property = Property(name="ContextMode", type=BooleanType)
connection_Connection_ContextId: Property = Property(name="ContextId", type=StringType)
connection_Connection_version: Property = Property(name="version", type=StringType)
connection_Connection.attributes={connection_Connection_version, connection_Connection_ContextId, connection_Connection_ContextMode}

# connection_MetadataTable class attributes and methods
connection_MetadataTable_sourceName: Property = Property(name="sourceName", type=StringType)
connection_MetadataTable_tableType: Property = Property(name="tableType", type=StringType)
connection_MetadataTable_attachedCDC: Property = Property(name="attachedCDC", type=BooleanType)
connection_MetadataTable_activatedCDC: Property = Property(name="activatedCDC", type=BooleanType)
connection_MetadataTable.attributes={connection_MetadataTable_sourceName, connection_MetadataTable_attachedCDC, connection_MetadataTable_tableType, connection_MetadataTable_activatedCDC}

# connection_QueriesConnection class attributes and methods

# connection_FileConnection class attributes and methods
connection_FileConnection_Server: Property = Property(name="Server", type=StringType)
connection_FileConnection_FilePath: Property = Property(name="FilePath", type=StringType)
connection_FileConnection_Format: Property = Property(name="Format", type=StringType)
connection_FileConnection_Encoding: Property = Property(name="Encoding", type=StringType)
connection_FileConnection_FieldSeparatorValue: Property = Property(name="FieldSeparatorValue", type=StringType)
connection_FileConnection_RowSeparatorType: Property = Property(name="RowSeparatorType", type=StringType)
connection_FileConnection_RowSeparatorValue: Property = Property(name="RowSeparatorValue", type=StringType)
connection_FileConnection_TextIdentifier: Property = Property(name="TextIdentifier", type=StringType)
connection_FileConnection_UseHeader: Property = Property(name="UseHeader", type=BooleanType)
connection_FileConnection_HeaderValue: Property = Property(name="HeaderValue", type=StringType)
connection_FileConnection_UseFooter: Property = Property(name="UseFooter", type=BooleanType)
connection_FileConnection_FooterValue: Property = Property(name="FooterValue", type=StringType)
connection_FileConnection_UseLimit: Property = Property(name="UseLimit", type=BooleanType)
connection_FileConnection_LimitValue: Property = Property(name="LimitValue", type=StringType)
connection_FileConnection_FirstLineCaption: Property = Property(name="FirstLineCaption", type=BooleanType)
connection_FileConnection_RemoveEmptyRow: Property = Property(name="RemoveEmptyRow", type=BooleanType)
connection_FileConnection_EscapeType: Property = Property(name="EscapeType", type=StringType)
connection_FileConnection_EscapeChar: Property = Property(name="EscapeChar", type=StringType)
connection_FileConnection_TextEnclosure: Property = Property(name="TextEnclosure", type=StringType)
connection_FileConnection_CsvOption: Property = Property(name="CsvOption", type=BooleanType)
connection_FileConnection.attributes={connection_FileConnection_FooterValue, connection_FileConnection_UseFooter, connection_FileConnection_UseHeader, connection_FileConnection_HeaderValue, connection_FileConnection_FirstLineCaption, connection_FileConnection_EscapeChar, connection_FileConnection_Encoding, connection_FileConnection_TextIdentifier, connection_FileConnection_EscapeType, connection_FileConnection_RemoveEmptyRow, connection_FileConnection_FilePath, connection_FileConnection_Server, connection_FileConnection_FieldSeparatorValue, connection_FileConnection_CsvOption, connection_FileConnection_TextEnclosure, connection_FileConnection_Format, connection_FileConnection_RowSeparatorType, connection_FileConnection_LimitValue, connection_FileConnection_UseLimit, connection_FileConnection_RowSeparatorValue}

# Connection class attributes and methods

# connection_Concept class attributes and methods
connection_Concept_LoopExpression: Property = Property(name="LoopExpression", type=StringType)
connection_Concept_LoopLimit: Property = Property(name="LoopLimit", type=StringType)
connection_Concept.attributes={connection_Concept_LoopExpression, connection_Concept_LoopLimit}

# connection_DelimitedFileConnection class attributes and methods
connection_DelimitedFileConnection_FieldSeparatorType: Property = Property(name="FieldSeparatorType", type=StringType)
connection_DelimitedFileConnection_splitRecord: Property = Property(name="splitRecord", type=BooleanType)
connection_DelimitedFileConnection.attributes={connection_DelimitedFileConnection_FieldSeparatorType, connection_DelimitedFileConnection_splitRecord}

# FileConnection class attributes and methods

# connection_PositionalFileConnection class attributes and methods

# connection_EbcdicConnection class attributes and methods
connection_EbcdicConnection_MidFile: Property = Property(name="MidFile", type=StringType)
connection_EbcdicConnection_DataFile: Property = Property(name="DataFile", type=StringType)
connection_EbcdicConnection.attributes={connection_EbcdicConnection_DataFile, connection_EbcdicConnection_MidFile}

# connection_MDMConnection class attributes and methods
connection_MDMConnection_Username: Property = Property(name="Username", type=StringType)
connection_MDMConnection_Password: Property = Property(name="Password", type=StringType)
connection_MDMConnection_Port: Property = Property(name="Port", type=StringType)
connection_MDMConnection_Server: Property = Property(name="Server", type=StringType)
connection_MDMConnection_Universe: Property = Property(name="Universe", type=StringType)
connection_MDMConnection_Datamodel: Property = Property(name="Datamodel", type=StringType)
connection_MDMConnection_Datacluster: Property = Property(name="Datacluster", type=StringType)
connection_MDMConnection.attributes={connection_MDMConnection_Port, connection_MDMConnection_Server, connection_MDMConnection_Datamodel, connection_MDMConnection_Universe, connection_MDMConnection_Password, connection_MDMConnection_Username, connection_MDMConnection_Datacluster}

# connection_DatabaseConnection class attributes and methods
connection_DatabaseConnection_SID: Property = Property(name="SID", type=StringType)
connection_DatabaseConnection_DatabaseType: Property = Property(name="DatabaseType", type=StringType)
connection_DatabaseConnection_SqlSynthax: Property = Property(name="SqlSynthax", type=StringType)
connection_DatabaseConnection_DriverJarPath: Property = Property(name="DriverJarPath", type=StringType)
connection_DatabaseConnection_StringQuote: Property = Property(name="StringQuote", type=StringType)
connection_DatabaseConnection_DriverClass: Property = Property(name="DriverClass", type=StringType)
connection_DatabaseConnection_URL: Property = Property(name="URL", type=StringType)
connection_DatabaseConnection_dbVersionString: Property = Property(name="dbVersionString", type=StringType)
connection_DatabaseConnection_Port: Property = Property(name="Port", type=StringType)
connection_DatabaseConnection_Username: Property = Property(name="Username", type=StringType)
connection_DatabaseConnection_Password: Property = Property(name="Password", type=StringType)
connection_DatabaseConnection_ServerName: Property = Property(name="ServerName", type=StringType)
connection_DatabaseConnection_DatasourceName: Property = Property(name="DatasourceName", type=StringType)
connection_DatabaseConnection_FileFieldName: Property = Property(name="FileFieldName", type=StringType)
connection_DatabaseConnection_Schema: Property = Property(name="Schema", type=StringType)
connection_DatabaseConnection_NullChar: Property = Property(name="NullChar", type=StringType)
connection_DatabaseConnection_DbmsId: Property = Property(name="DbmsId", type=StringType)
connection_DatabaseConnection_ProductId: Property = Property(name="ProductId", type=StringType)
connection_DatabaseConnection_DBRootPath: Property = Property(name="DBRootPath", type=StringType)
connection_DatabaseConnection_AdditionalParams: Property = Property(name="AdditionalParams", type=StringType)
connection_DatabaseConnection_StandardSQL: Property = Property(name="StandardSQL", type=BooleanType)
connection_DatabaseConnection_SystemSQL: Property = Property(name="SystemSQL", type=BooleanType)
connection_DatabaseConnection_cdcTypeMode: Property = Property(name="cdcTypeMode", type=StringType)
connection_DatabaseConnection_SQLMode: Property = Property(name="SQLMode", type=BooleanType)
connection_DatabaseConnection.attributes={connection_DatabaseConnection_NullChar, connection_DatabaseConnection_StringQuote, connection_DatabaseConnection_ProductId, connection_DatabaseConnection_Password, connection_DatabaseConnection_DatabaseType, connection_DatabaseConnection_Port, connection_DatabaseConnection_SQLMode, connection_DatabaseConnection_ServerName, connection_DatabaseConnection_DriverJarPath, connection_DatabaseConnection_AdditionalParams, connection_DatabaseConnection_DatasourceName, connection_DatabaseConnection_SqlSynthax, connection_DatabaseConnection_StandardSQL, connection_DatabaseConnection_URL, connection_DatabaseConnection_SID, connection_DatabaseConnection_DbmsId, connection_DatabaseConnection_DBRootPath, connection_DatabaseConnection_Schema, connection_DatabaseConnection_FileFieldName, connection_DatabaseConnection_SystemSQL, connection_DatabaseConnection_dbVersionString, connection_DatabaseConnection_DriverClass, connection_DatabaseConnection_Username, connection_DatabaseConnection_cdcTypeMode}

# connection_SAPFunctionUnit class attributes and methods
connection_SAPFunctionUnit_Name: Property = Property(name="Name", type=StringType)
connection_SAPFunctionUnit_OutputType: Property = Property(name="OutputType", type=StringType)
connection_SAPFunctionUnit_OutputTableName: Property = Property(name="OutputTableName", type=StringType)
connection_SAPFunctionUnit_Document: Property = Property(name="Document", type=StringType)
connection_SAPFunctionUnit.attributes={connection_SAPFunctionUnit_Name, connection_SAPFunctionUnit_Document, connection_SAPFunctionUnit_OutputType, connection_SAPFunctionUnit_OutputTableName}

# connection_CDCConnection class attributes and methods

# connection_SAPConnection class attributes and methods
connection_SAPConnection_Client: Property = Property(name="Client", type=StringType)
connection_SAPConnection_SystemNumber: Property = Property(name="SystemNumber", type=StringType)
connection_SAPConnection_Language: Property = Property(name="Language", type=StringType)
connection_SAPConnection_currentFucntion: Property = Property(name="currentFucntion", type=StringType)
connection_SAPConnection_Host: Property = Property(name="Host", type=StringType)
connection_SAPConnection_Username: Property = Property(name="Username", type=StringType)
connection_SAPConnection_Password: Property = Property(name="Password", type=StringType)
connection_SAPConnection.attributes={connection_SAPConnection_currentFucntion, connection_SAPConnection_Client, connection_SAPConnection_Username, connection_SAPConnection_Password, connection_SAPConnection_Language, connection_SAPConnection_Host, connection_SAPConnection_SystemNumber}

# connection_SAPTestInputParameterTable class attributes and methods

# connection_SAPFunctionParameterColumn class attributes and methods
connection_SAPFunctionParameterColumn_Name: Property = Property(name="Name", type=StringType)
connection_SAPFunctionParameterColumn_ParameterType: Property = Property(name="ParameterType", type=StringType)
connection_SAPFunctionParameterColumn_StructureOrTableName: Property = Property(name="StructureOrTableName", type=StringType)
connection_SAPFunctionParameterColumn_DataType: Property = Property(name="DataType", type=StringType)
connection_SAPFunctionParameterColumn_Length: Property = Property(name="Length", type=StringType)
connection_SAPFunctionParameterColumn_Description: Property = Property(name="Description", type=StringType)
connection_SAPFunctionParameterColumn_Value: Property = Property(name="Value", type=StringType)
connection_SAPFunctionParameterColumn.attributes={connection_SAPFunctionParameterColumn_Name, connection_SAPFunctionParameterColumn_Length, connection_SAPFunctionParameterColumn_Value, connection_SAPFunctionParameterColumn_Description, connection_SAPFunctionParameterColumn_StructureOrTableName, connection_SAPFunctionParameterColumn_ParameterType, connection_SAPFunctionParameterColumn_DataType}

# connection_InputSAPFunctionParameterTable class attributes and methods

# connection_OutputSAPFunctionParameterTable class attributes and methods

# connection_RegexpFileConnection class attributes and methods
connection_RegexpFileConnection_FieldSeparatorType: Property = Property(name="FieldSeparatorType", type=StringType)
connection_RegexpFileConnection.attributes={connection_RegexpFileConnection_FieldSeparatorType}

# connection_XmlFileConnection class attributes and methods
connection_XmlFileConnection_XsdFilePath: Property = Property(name="XsdFilePath", type=StringType)
connection_XmlFileConnection_XmlFilePath: Property = Property(name="XmlFilePath", type=StringType)
connection_XmlFileConnection_Guess: Property = Property(name="Guess", type=BooleanType)
connection_XmlFileConnection_MaskXPattern: Property = Property(name="MaskXPattern", type=StringType)
connection_XmlFileConnection_Encoding: Property = Property(name="Encoding", type=StringType)
connection_XmlFileConnection.attributes={connection_XmlFileConnection_XsdFilePath, connection_XmlFileConnection_XmlFilePath, connection_XmlFileConnection_MaskXPattern, connection_XmlFileConnection_Encoding, connection_XmlFileConnection_Guess}

# connection_XmlXPathLoopDescriptor class attributes and methods
connection_XmlXPathLoopDescriptor_LimitBoucle: Property = Property(name="LimitBoucle", type=StringType)
connection_XmlXPathLoopDescriptor_AbsoluteXPathQuery: Property = Property(name="AbsoluteXPathQuery", type=StringType)
connection_XmlXPathLoopDescriptor.attributes={connection_XmlXPathLoopDescriptor_AbsoluteXPathQuery, connection_XmlXPathLoopDescriptor_LimitBoucle}

# connection_SchemaTarget class attributes and methods
connection_SchemaTarget_RelativeXPathQuery: Property = Property(name="RelativeXPathQuery", type=StringType)
connection_SchemaTarget_TagName: Property = Property(name="TagName", type=StringType)
connection_SchemaTarget.attributes={connection_SchemaTarget_TagName, connection_SchemaTarget_RelativeXPathQuery}

# connection_SAPFunctionParameterTable class attributes and methods

# SAPFunctionParameterTable class attributes and methods

# connection_GenericSchemaConnection class attributes and methods
connection_GenericSchemaConnection_mappingTypeUsed: Property = Property(name="mappingTypeUsed", type=BooleanType)
connection_GenericSchemaConnection_mappingTypeId: Property = Property(name="mappingTypeId", type=StringType)
connection_GenericSchemaConnection.attributes={connection_GenericSchemaConnection_mappingTypeUsed, connection_GenericSchemaConnection_mappingTypeId}

# connection_LDAPSchemaConnection class attributes and methods
connection_LDAPSchemaConnection_Host: Property = Property(name="Host", type=StringType)
connection_LDAPSchemaConnection_Port: Property = Property(name="Port", type=StringType)
connection_LDAPSchemaConnection_Protocol: Property = Property(name="Protocol", type=StringType)
connection_LDAPSchemaConnection_ReturnAttributes: Property = Property(name="ReturnAttributes", type=StringType)
connection_LDAPSchemaConnection_SelectedDN: Property = Property(name="SelectedDN", type=StringType)
connection_LDAPSchemaConnection_Filter: Property = Property(name="Filter", type=StringType)
connection_LDAPSchemaConnection_Separator: Property = Property(name="Separator", type=StringType)
connection_LDAPSchemaConnection_UseAdvanced: Property = Property(name="UseAdvanced", type=BooleanType)
connection_LDAPSchemaConnection_StorePath: Property = Property(name="StorePath", type=StringType)
connection_LDAPSchemaConnection_UseLimit: Property = Property(name="UseLimit", type=BooleanType)
connection_LDAPSchemaConnection_UseAuthen: Property = Property(name="UseAuthen", type=BooleanType)
connection_LDAPSchemaConnection_BindPrincipal: Property = Property(name="BindPrincipal", type=StringType)
connection_LDAPSchemaConnection_BindPassword: Property = Property(name="BindPassword", type=StringType)
connection_LDAPSchemaConnection_LimitValue: Property = Property(name="LimitValue", type=IntegerType)
connection_LDAPSchemaConnection_EncryptionMethodName: Property = Property(name="EncryptionMethodName", type=StringType)
connection_LDAPSchemaConnection_Value: Property = Property(name="Value", type=StringType)
connection_LDAPSchemaConnection_SavePassword: Property = Property(name="SavePassword", type=BooleanType)
connection_LDAPSchemaConnection_Aliases: Property = Property(name="Aliases", type=StringType)
connection_LDAPSchemaConnection_Referrals: Property = Property(name="Referrals", type=StringType)
connection_LDAPSchemaConnection_CountLimit: Property = Property(name="CountLimit", type=StringType)
connection_LDAPSchemaConnection_TimeOutLimit: Property = Property(name="TimeOutLimit", type=StringType)
connection_LDAPSchemaConnection_BaseDNs: Property = Property(name="BaseDNs", type=StringType)
connection_LDAPSchemaConnection_GetBaseDNsFromRoot: Property = Property(name="GetBaseDNsFromRoot", type=BooleanType)
connection_LDAPSchemaConnection.attributes={connection_LDAPSchemaConnection_LimitValue, connection_LDAPSchemaConnection_ReturnAttributes, connection_LDAPSchemaConnection_EncryptionMethodName, connection_LDAPSchemaConnection_BindPassword, connection_LDAPSchemaConnection_UseAuthen, connection_LDAPSchemaConnection_Filter, connection_LDAPSchemaConnection_Referrals, connection_LDAPSchemaConnection_GetBaseDNsFromRoot, connection_LDAPSchemaConnection_Aliases, connection_LDAPSchemaConnection_CountLimit, connection_LDAPSchemaConnection_Port, connection_LDAPSchemaConnection_BaseDNs, connection_LDAPSchemaConnection_TimeOutLimit, connection_LDAPSchemaConnection_Protocol, connection_LDAPSchemaConnection_UseAdvanced, connection_LDAPSchemaConnection_Value, connection_LDAPSchemaConnection_SavePassword, connection_LDAPSchemaConnection_SelectedDN, connection_LDAPSchemaConnection_BindPrincipal, connection_LDAPSchemaConnection_Host, connection_LDAPSchemaConnection_UseLimit, connection_LDAPSchemaConnection_Separator, connection_LDAPSchemaConnection_StorePath}

# connection_Query class attributes and methods
connection_Query_value: Property = Property(name="value", type=StringType)
connection_Query_contextMode: Property = Property(name="contextMode", type=BooleanType)
connection_Query.attributes={connection_Query_contextMode, connection_Query_value}

# connection_LdifFileConnection class attributes and methods
connection_LdifFileConnection_value: Property = Property(name="value", type=StringType)
connection_LdifFileConnection_FilePath: Property = Property(name="FilePath", type=StringType)
connection_LdifFileConnection_LimitEntry: Property = Property(name="LimitEntry", type=IntegerType)
connection_LdifFileConnection_UseLimit: Property = Property(name="UseLimit", type=BooleanType)
connection_LdifFileConnection_Server: Property = Property(name="Server", type=StringType)
connection_LdifFileConnection.attributes={connection_LdifFileConnection_value, connection_LdifFileConnection_LimitEntry, connection_LdifFileConnection_Server, connection_LdifFileConnection_UseLimit, connection_LdifFileConnection_FilePath}

# connection_FileExcelConnection class attributes and methods
connection_FileExcelConnection_firstColumn: Property = Property(name="firstColumn", type=StringType)
connection_FileExcelConnection_lastColumn: Property = Property(name="lastColumn", type=StringType)
connection_FileExcelConnection_thousandSeparator: Property = Property(name="thousandSeparator", type=StringType)
connection_FileExcelConnection_decimalSeparator: Property = Property(name="decimalSeparator", type=StringType)
connection_FileExcelConnection_advancedSpearator: Property = Property(name="advancedSpearator", type=BooleanType)
connection_FileExcelConnection_selectAllSheets: Property = Property(name="selectAllSheets", type=BooleanType)
connection_FileExcelConnection_sheetList: Property = Property(name="sheetList", type=StringType)
connection_FileExcelConnection_SheetName: Property = Property(name="SheetName", type=StringType)
connection_FileExcelConnection_sheetColumns: Property = Property(name="sheetColumns", type=StringType)
connection_FileExcelConnection.attributes={connection_FileExcelConnection_advancedSpearator, connection_FileExcelConnection_thousandSeparator, connection_FileExcelConnection_decimalSeparator, connection_FileExcelConnection_lastColumn, connection_FileExcelConnection_SheetName, connection_FileExcelConnection_selectAllSheets, connection_FileExcelConnection_sheetList, connection_FileExcelConnection_sheetColumns, connection_FileExcelConnection_firstColumn}

# connection_WSDLSchemaConnection class attributes and methods
connection_WSDLSchemaConnection_WSDL: Property = Property(name="WSDL", type=StringType)
connection_WSDLSchemaConnection_needAuth: Property = Property(name="needAuth", type=BooleanType)
connection_WSDLSchemaConnection_methodName: Property = Property(name="methodName", type=StringType)
connection_WSDLSchemaConnection_parameters: Property = Property(name="parameters", type=StringType)
connection_WSDLSchemaConnection_UserName: Property = Property(name="UserName", type=StringType)
connection_WSDLSchemaConnection_Password: Property = Property(name="Password", type=StringType)
connection_WSDLSchemaConnection_useProxy: Property = Property(name="useProxy", type=BooleanType)
connection_WSDLSchemaConnection_proxyHost: Property = Property(name="proxyHost", type=StringType)
connection_WSDLSchemaConnection_proxyPort: Property = Property(name="proxyPort", type=StringType)
connection_WSDLSchemaConnection_proxyUser: Property = Property(name="proxyUser", type=StringType)
connection_WSDLSchemaConnection_proxyPassword: Property = Property(name="proxyPassword", type=StringType)
connection_WSDLSchemaConnection_Value: Property = Property(name="Value", type=StringType)
connection_WSDLSchemaConnection_EndpointURI: Property = Property(name="EndpointURI", type=StringType)
connection_WSDLSchemaConnection_Encoding: Property = Property(name="Encoding", type=StringType)
connection_WSDLSchemaConnection_timeOut: Property = Property(name="timeOut", type=IntegerType)
connection_WSDLSchemaConnection.attributes={connection_WSDLSchemaConnection_methodName, connection_WSDLSchemaConnection_proxyHost, connection_WSDLSchemaConnection_parameters, connection_WSDLSchemaConnection_proxyPort, connection_WSDLSchemaConnection_timeOut, connection_WSDLSchemaConnection_Password, connection_WSDLSchemaConnection_proxyPassword, connection_WSDLSchemaConnection_EndpointURI, connection_WSDLSchemaConnection_needAuth, connection_WSDLSchemaConnection_WSDL, connection_WSDLSchemaConnection_UserName, connection_WSDLSchemaConnection_Encoding, connection_WSDLSchemaConnection_Value, connection_WSDLSchemaConnection_useProxy, connection_WSDLSchemaConnection_proxyUser}

# connection_SalesforceSchemaConnection class attributes and methods
connection_SalesforceSchemaConnection_webServiceUrl: Property = Property(name="webServiceUrl", type=StringType)
connection_SalesforceSchemaConnection_userName: Property = Property(name="userName", type=StringType)
connection_SalesforceSchemaConnection_password: Property = Property(name="password", type=StringType)
connection_SalesforceSchemaConnection_moduleName: Property = Property(name="moduleName", type=StringType)
connection_SalesforceSchemaConnection_queryCondition: Property = Property(name="queryCondition", type=StringType)
connection_SalesforceSchemaConnection_useCustomModuleName: Property = Property(name="useCustomModuleName", type=BooleanType)
connection_SalesforceSchemaConnection_useProxy: Property = Property(name="useProxy", type=BooleanType)
connection_SalesforceSchemaConnection_proxyHost: Property = Property(name="proxyHost", type=StringType)
connection_SalesforceSchemaConnection_proxyPort: Property = Property(name="proxyPort", type=StringType)
connection_SalesforceSchemaConnection_proxyUsername: Property = Property(name="proxyUsername", type=StringType)
connection_SalesforceSchemaConnection_proxyPassword: Property = Property(name="proxyPassword", type=StringType)
connection_SalesforceSchemaConnection_batchSize: Property = Property(name="batchSize", type=StringType)
connection_SalesforceSchemaConnection_useHttpProxy: Property = Property(name="useHttpProxy", type=BooleanType)
connection_SalesforceSchemaConnection_useAlphbet: Property = Property(name="useAlphbet", type=BooleanType)
connection_SalesforceSchemaConnection_timeOut: Property = Property(name="timeOut", type=StringType)
connection_SalesforceSchemaConnection.attributes={connection_SalesforceSchemaConnection_proxyPassword, connection_SalesforceSchemaConnection_webServiceUrl, connection_SalesforceSchemaConnection_useProxy, connection_SalesforceSchemaConnection_proxyHost, connection_SalesforceSchemaConnection_useAlphbet, connection_SalesforceSchemaConnection_password, connection_SalesforceSchemaConnection_userName, connection_SalesforceSchemaConnection_moduleName, connection_SalesforceSchemaConnection_proxyPort, connection_SalesforceSchemaConnection_useHttpProxy, connection_SalesforceSchemaConnection_queryCondition, connection_SalesforceSchemaConnection_useCustomModuleName, connection_SalesforceSchemaConnection_batchSize, connection_SalesforceSchemaConnection_proxyUsername, connection_SalesforceSchemaConnection_timeOut}

# connection_SubscriberTable class attributes and methods
connection_SubscriberTable_system: Property = Property(name="system", type=BooleanType)
connection_SubscriberTable.attributes={connection_SubscriberTable_system}

# MetadataTable class attributes and methods

# connection_ConceptTarget class attributes and methods
connection_ConceptTarget_targetName: Property = Property(name="targetName", type=StringType)
connection_ConceptTarget_RelativeLoopExpression: Property = Property(name="RelativeLoopExpression", type=StringType)
connection_ConceptTarget.attributes={connection_ConceptTarget_RelativeLoopExpression, connection_ConceptTarget_targetName}

# connection_CDCType class attributes and methods
connection_CDCType_linkDB: Property = Property(name="linkDB", type=StringType)
connection_CDCType_journalName: Property = Property(name="journalName", type=StringType)
connection_CDCType.attributes={connection_CDCType_journalName, connection_CDCType_linkDB}

# connection_HL7Connection class attributes and methods
connection_HL7Connection_StartChar: Property = Property(name="StartChar", type=StringType)
connection_HL7Connection_EndChar: Property = Property(name="EndChar", type=StringType)
connection_HL7Connection.attributes={connection_HL7Connection_StartChar, connection_HL7Connection_EndChar}

# Relationships
table4: BinaryAssociation = BinaryAssociation(
    name="table4",
    ends={
        Property(name="MetadataTable5", type=connection_MetadataColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=connection_MetadataTable, multiplicity=Multiplicity(0, 1))
    }
)
connections0: BinaryAssociation = BinaryAssociation(
    name="connections0",
    ends={
        Property(name="connection_Connection", type=connection_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_Metadata", type=connection_Connection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables1: BinaryAssociation = BinaryAssociation(
    name="tables1",
    ends={
        Property(name="MetadataTable", type=connection_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection", type=connection_MetadataTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
queries2: BinaryAssociation = BinaryAssociation(
    name="queries2",
    ends={
        Property(name="QueriesConnection", type=connection_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection3", type=connection_QueriesConnection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columns6: BinaryAssociation = BinaryAssociation(
    name="columns6",
    ends={
        Property(name="MetadataColumn", type=connection_MetadataTable, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=connection_MetadataColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connection7: BinaryAssociation = BinaryAssociation(
    name="connection7",
    ends={
        Property(name="Connection", type=connection_MetadataTable, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=connection_Connection, multiplicity=Multiplicity(0, 1))
    }
)
schemas8: BinaryAssociation = BinaryAssociation(
    name="schemas8",
    ends={
        Property(name="connection_Concept", type=connection_MDMConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_MDMConnection", type=connection_Concept, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Funtions11: BinaryAssociation = BinaryAssociation(
    name="Funtions11",
    ends={
        Property(name="SAPFunctionUnit", type=connection_SAPConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection12", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cdcConns9: BinaryAssociation = BinaryAssociation(
    name="cdcConns9",
    ends={
        Property(name="CDCConnection", type=connection_DatabaseConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection10", type=connection_CDCConnection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connection17: BinaryAssociation = BinaryAssociation(
    name="connection17",
    ends={
        Property(name="SAPConnection", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="Funtions", type=connection_SAPConnection, multiplicity=Multiplicity(0, 1))
    }
)
tables18: BinaryAssociation = BinaryAssociation(
    name="tables18",
    ends={
        Property(name="connection_MetadataTable20", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_SAPFunctionUnit19", type=connection_MetadataTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
TestInputParameterTable21: BinaryAssociation = BinaryAssociation(
    name="TestInputParameterTable21",
    ends={
        Property(name="SAPTestInputParameterTable", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="functionUnit22", type=connection_SAPTestInputParameterTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
InputParameterTable13: BinaryAssociation = BinaryAssociation(
    name="InputParameterTable13",
    ends={
        Property(name="InputSAPFunctionParameterTable", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="functionUnit", type=connection_InputSAPFunctionParameterTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
OutputParameterTable14: BinaryAssociation = BinaryAssociation(
    name="OutputParameterTable14",
    ends={
        Property(name="OutputSAPFunctionParameterTable", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="functionUnit15", type=connection_OutputSAPFunctionParameterTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
MetadataTable16: BinaryAssociation = BinaryAssociation(
    name="MetadataTable16",
    ends={
        Property(name="connection_MetadataTable", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_SAPFunctionUnit", type=connection_MetadataTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schema30: BinaryAssociation = BinaryAssociation(
    name="schema30",
    ends={
        Property(name="XmlXPathLoopDescriptor", type=connection_XmlFileConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection31", type=connection_XmlXPathLoopDescriptor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schema32: BinaryAssociation = BinaryAssociation(
    name="schema32",
    ends={
        Property(name="XmlXPathLoopDescriptor33", type=connection_SchemaTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="schemaTargets", type=connection_XmlXPathLoopDescriptor, multiplicity=Multiplicity(0, 1))
    }
)
connection34: BinaryAssociation = BinaryAssociation(
    name="connection34",
    ends={
        Property(name="Connection35", type=connection_QueriesConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="queries", type=connection_Connection, multiplicity=Multiplicity(0, 1))
    }
)
ParameterTable23: BinaryAssociation = BinaryAssociation(
    name="ParameterTable23",
    ends={
        Property(name="SAPFunctionParameterTable", type=connection_SAPFunctionParameterColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="columns24", type=connection_SAPFunctionParameterTable, multiplicity=Multiplicity(0, 1))
    }
)
columns25: BinaryAssociation = BinaryAssociation(
    name="columns25",
    ends={
        Property(name="SAPFunctionParameterColumn", type=connection_SAPFunctionParameterTable, multiplicity=Multiplicity(1, 1)),
        Property(name="ParameterTable", type=connection_SAPFunctionParameterColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionUnit26: BinaryAssociation = BinaryAssociation(
    name="functionUnit26",
    ends={
        Property(name="SAPFunctionUnit27", type=connection_InputSAPFunctionParameterTable, multiplicity=Multiplicity(1, 1)),
        Property(name="InputParameterTable", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(0, 1))
    }
)
functionUnit28: BinaryAssociation = BinaryAssociation(
    name="functionUnit28",
    ends={
        Property(name="SAPFunctionUnit29", type=connection_OutputSAPFunctionParameterTable, multiplicity=Multiplicity(1, 1)),
        Property(name="OutputParameterTable", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(0, 1))
    }
)
connection40: BinaryAssociation = BinaryAssociation(
    name="connection40",
    ends={
        Property(name="XmlFileConnection", type=connection_XmlXPathLoopDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=connection_XmlFileConnection, multiplicity=Multiplicity(0, 1))
    }
)
schemaTargets41: BinaryAssociation = BinaryAssociation(
    name="schemaTargets41",
    ends={
        Property(name="SchemaTarget", type=connection_XmlXPathLoopDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="schema42", type=connection_SchemaTarget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
query36: BinaryAssociation = BinaryAssociation(
    name="query36",
    ends={
        Property(name="Query", type=connection_QueriesConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="queries37", type=connection_Query, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
queries38: BinaryAssociation = BinaryAssociation(
    name="queries38",
    ends={
        Property(name="QueriesConnection39", type=connection_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="query", type=connection_QueriesConnection, multiplicity=Multiplicity(0, 1))
    }
)
cdcTypes44: BinaryAssociation = BinaryAssociation(
    name="cdcTypes44",
    ends={
        Property(name="connection_CDCType", type=connection_CDCConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_CDCConnection", type=connection_CDCType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subscribers45: BinaryAssociation = BinaryAssociation(
    name="subscribers45",
    ends={
        Property(name="connection_SubscriberTable", type=connection_CDCType, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_CDCType46", type=connection_SubscriberTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cdcConnection47: BinaryAssociation = BinaryAssociation(
    name="cdcConnection47",
    ends={
        Property(name="connection_CDCConnection49", type=connection_CDCType, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_CDCType48", type=connection_CDCConnection, multiplicity=Multiplicity(0, 1))
    }
)
functionUnit50: BinaryAssociation = BinaryAssociation(
    name="functionUnit50",
    ends={
        Property(name="SAPFunctionUnit51", type=connection_SAPTestInputParameterTable, multiplicity=Multiplicity(1, 1)),
        Property(name="TestInputParameterTable", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(0, 1))
    }
)
connection43: BinaryAssociation = BinaryAssociation(
    name="connection43",
    ends={
        Property(name="DatabaseConnection", type=connection_CDCConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="cdcConns", type=connection_DatabaseConnection, multiplicity=Multiplicity(0, 1))
    }
)
conceptTargets52: BinaryAssociation = BinaryAssociation(
    name="conceptTargets52",
    ends={
        Property(name="ConceptTarget", type=connection_Concept, multiplicity=Multiplicity(1, 1)),
        Property(name="schema53", type=connection_ConceptTarget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schema54: BinaryAssociation = BinaryAssociation(
    name="schema54",
    ends={
        Property(name="Concept", type=connection_ConceptTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="conceptTargets", type=connection_Concept, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_connection_MetadataColumn_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_MetadataColumn)
gen_connection_MetadataTable_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_MetadataTable)
gen_connection_Metadata_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_Metadata)
gen_connection_Connection_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_Connection)
gen_connection_FileConnection_Connection = Generalization(general=Connection, specific=connection_FileConnection)
gen_connection_DelimitedFileConnection_FileConnection = Generalization(general=FileConnection, specific=connection_DelimitedFileConnection)
gen_connection_PositionalFileConnection_FileConnection = Generalization(general=FileConnection, specific=connection_PositionalFileConnection)
gen_connection_EbcdicConnection_FileConnection = Generalization(general=FileConnection, specific=connection_EbcdicConnection)
gen_connection_MDMConnection_Connection = Generalization(general=Connection, specific=connection_MDMConnection)
gen_connection_DatabaseConnection_Connection = Generalization(general=Connection, specific=connection_DatabaseConnection)
gen_connection_SAPFunctionUnit_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_SAPFunctionUnit)
gen_connection_SAPConnection_Connection = Generalization(general=Connection, specific=connection_SAPConnection)
gen_connection_SAPFunctionParameterColumn_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_SAPFunctionParameterColumn)
gen_connection_RegexpFileConnection_FileConnection = Generalization(general=FileConnection, specific=connection_RegexpFileConnection)
gen_connection_XmlFileConnection_Connection = Generalization(general=Connection, specific=connection_XmlFileConnection)
gen_connection_SAPFunctionParameterTable_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_SAPFunctionParameterTable)
gen_connection_InputSAPFunctionParameterTable_SAPFunctionParameterTable = Generalization(general=SAPFunctionParameterTable, specific=connection_InputSAPFunctionParameterTable)
gen_connection_OutputSAPFunctionParameterTable_SAPFunctionParameterTable = Generalization(general=SAPFunctionParameterTable, specific=connection_OutputSAPFunctionParameterTable)
gen_connection_GenericSchemaConnection_Connection = Generalization(general=Connection, specific=connection_GenericSchemaConnection)
gen_connection_LDAPSchemaConnection_Connection = Generalization(general=Connection, specific=connection_LDAPSchemaConnection)
gen_connection_Query_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_Query)
gen_connection_LdifFileConnection_Connection = Generalization(general=Connection, specific=connection_LdifFileConnection)
gen_connection_FileExcelConnection_FileConnection = Generalization(general=FileConnection, specific=connection_FileExcelConnection)
gen_connection_WSDLSchemaConnection_Connection = Generalization(general=Connection, specific=connection_WSDLSchemaConnection)
gen_connection_SalesforceSchemaConnection_Connection = Generalization(general=Connection, specific=connection_SalesforceSchemaConnection)
gen_connection_CDCType_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_CDCType)
gen_connection_SubscriberTable_MetadataTable = Generalization(general=MetadataTable, specific=connection_SubscriberTable)
gen_connection_SAPTestInputParameterTable_SAPFunctionParameterTable = Generalization(general=SAPFunctionParameterTable, specific=connection_SAPTestInputParameterTable)
gen_connection_Concept_MetadataTable = Generalization(general=MetadataTable, specific=connection_Concept)
gen_connection_HL7Connection_FileConnection = Generalization(general=FileConnection, specific=connection_HL7Connection)

# Domain Model
domain_model = DomainModel(
    name="connection",
    types={connection_Metadata, connection_MetadataColumn, connection_AbstractMetadataObject, AbstractMetadataObject, connection_Connection, connection_MetadataTable, connection_QueriesConnection, connection_FileConnection, Connection, connection_Concept, connection_DelimitedFileConnection, FileConnection, connection_PositionalFileConnection, connection_EbcdicConnection, connection_MDMConnection, connection_DatabaseConnection, connection_SAPFunctionUnit, connection_CDCConnection, connection_SAPConnection, connection_SAPTestInputParameterTable, connection_SAPFunctionParameterColumn, connection_InputSAPFunctionParameterTable, connection_OutputSAPFunctionParameterTable, connection_RegexpFileConnection, connection_XmlFileConnection, connection_XmlXPathLoopDescriptor, connection_SchemaTarget, connection_SAPFunctionParameterTable, SAPFunctionParameterTable, connection_GenericSchemaConnection, connection_LDAPSchemaConnection, connection_Query, connection_LdifFileConnection, connection_FileExcelConnection, connection_WSDLSchemaConnection, connection_SalesforceSchemaConnection, connection_SubscriberTable, MetadataTable, connection_ConceptTarget, connection_CDCType, connection_HL7Connection, DatabaseProperties, FileFormat, FieldSeparator, Escape, RowSeparator},
    associations={table4, connections0, tables1, queries2, columns6, connection7, schemas8, Funtions11, cdcConns9, connection17, tables18, TestInputParameterTable21, InputParameterTable13, OutputParameterTable14, MetadataTable16, schema30, schema32, connection34, ParameterTable23, columns25, functionUnit26, functionUnit28, connection40, schemaTargets41, query36, queries38, cdcTypes44, subscribers45, cdcConnection47, functionUnit50, connection43, conceptTargets52, schema54},
    generalizations={gen_connection_MetadataColumn_AbstractMetadataObject, gen_connection_MetadataTable_AbstractMetadataObject, gen_connection_Metadata_AbstractMetadataObject, gen_connection_Connection_AbstractMetadataObject, gen_connection_FileConnection_Connection, gen_connection_DelimitedFileConnection_FileConnection, gen_connection_PositionalFileConnection_FileConnection, gen_connection_EbcdicConnection_FileConnection, gen_connection_MDMConnection_Connection, gen_connection_DatabaseConnection_Connection, gen_connection_SAPFunctionUnit_AbstractMetadataObject, gen_connection_SAPConnection_Connection, gen_connection_SAPFunctionParameterColumn_AbstractMetadataObject, gen_connection_RegexpFileConnection_FileConnection, gen_connection_XmlFileConnection_Connection, gen_connection_SAPFunctionParameterTable_AbstractMetadataObject, gen_connection_InputSAPFunctionParameterTable_SAPFunctionParameterTable, gen_connection_OutputSAPFunctionParameterTable_SAPFunctionParameterTable, gen_connection_GenericSchemaConnection_Connection, gen_connection_LDAPSchemaConnection_Connection, gen_connection_Query_AbstractMetadataObject, gen_connection_LdifFileConnection_Connection, gen_connection_FileExcelConnection_FileConnection, gen_connection_WSDLSchemaConnection_Connection, gen_connection_SalesforceSchemaConnection_Connection, gen_connection_CDCType_AbstractMetadataObject, gen_connection_SubscriberTable_MetadataTable, gen_connection_SAPTestInputParameterTable_SAPFunctionParameterTable, gen_connection_Concept_MetadataTable, gen_connection_HL7Connection_FileConnection},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)