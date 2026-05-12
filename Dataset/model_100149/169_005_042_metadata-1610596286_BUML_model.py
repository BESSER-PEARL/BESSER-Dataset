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
            EnumerationLiteral(name="Space"),
			EnumerationLiteral(name="Alt_65"),
			EnumerationLiteral(name="Custom_ANSI"),
			EnumerationLiteral(name="Custom_UTF8"),
			EnumerationLiteral(name="Custom_RegExp"),
			EnumerationLiteral(name="Tabulation"),
			EnumerationLiteral(name="Semicolon"),
			EnumerationLiteral(name="Comma")
    }
)

MDMConnectionProtocol: Enumeration = Enumeration(
    name="MDMConnectionProtocol",
    literals={
            EnumerationLiteral(name="HTTP")
    }
)

MdmConceptType: Enumeration = Enumeration(
    name="MdmConceptType",
    literals={
            EnumerationLiteral(name="OUTPUT"),
			EnumerationLiteral(name="RECEIVE"),
			EnumerationLiteral(name="INPUT")
    }
)

LogicalOperator: Enumeration = Enumeration(
    name="LogicalOperator",
    literals={
            EnumerationLiteral(name="And"),
			EnumerationLiteral(name="Or")
    }
)

RuleType: Enumeration = Enumeration(
    name="RuleType",
    literals={
            EnumerationLiteral(name="REFERENCE"),
			EnumerationLiteral(name="BASIC"),
			EnumerationLiteral(name="CUSTOM")
    }
)

Function: Enumeration = Enumeration(
    name="Function",
    literals={
            EnumerationLiteral(name="Empty"),
			EnumerationLiteral(name="Lower_case"),
			EnumerationLiteral(name="Upper_case"),
			EnumerationLiteral(name="Lower_case_first"),
			EnumerationLiteral(name="Upper_case_first"),
			EnumerationLiteral(name="Length"),
			EnumerationLiteral(name="Match")
    }
)

Operator: Enumeration = Enumeration(
    name="Operator",
    literals={
            EnumerationLiteral(name="Lower"),
			EnumerationLiteral(name="Greater_or_equals"),
			EnumerationLiteral(name="Lower_or_equals"),
			EnumerationLiteral(name="Equals"),
			EnumerationLiteral(name="Not_equals"),
			EnumerationLiteral(name="Greater")
    }
)

DevelopmentStatus: Enumeration = Enumeration(
    name="DevelopmentStatus",
    literals={
            EnumerationLiteral(name="DRAFT"),
			EnumerationLiteral(name="PROD")
    }
)

# Classes
connection_Metadata = Class(name="connection_Metadata")
AbstractMetadataObject = Class(name="AbstractMetadataObject")
connection_Connection = Class(name="connection_Connection")
softwaredeployment_DataProvider = Class(name="softwaredeployment_DataProvider")
connection_QueriesConnection = Class(name="connection_QueriesConnection")
connection_MetadataColumn = Class(name="connection_MetadataColumn")
record_Field = Class(name="record_Field")
core_Class = Class(name="core_Class")
connection_MetadataTable = Class(name="connection_MetadataTable")
connection_AbstractMetadataObject = Class(name="connection_AbstractMetadataObject", is_abstract=True)
ModelElement = Class(name="ModelElement")
connection_DelimitedFileConnection = Class(name="connection_DelimitedFileConnection")
FileConnection = Class(name="FileConnection")
connection_PositionalFileConnection = Class(name="connection_PositionalFileConnection")
connection_EbcdicConnection = Class(name="connection_EbcdicConnection")
connection_AdditionalProperties = Class(name="connection_AdditionalProperties")
connection_FileConnection = Class(name="connection_FileConnection", is_abstract=True)
Connection = Class(name="Connection")
connection_DatabaseConnection = Class(name="connection_DatabaseConnection")
connection_MDMConnection = Class(name="connection_MDMConnection")
connection_Concept = Class(name="connection_Concept")
connection_CDCConnection = Class(name="connection_CDCConnection")
connection_InputSAPFunctionParameterTable = Class(name="connection_InputSAPFunctionParameterTable")
connection_OutputSAPFunctionParameterTable = Class(name="connection_OutputSAPFunctionParameterTable")
connection_SAPConnection = Class(name="connection_SAPConnection")
connection_SAPFunctionUnit = Class(name="connection_SAPFunctionUnit")
connection_SAPIDocUnit = Class(name="connection_SAPIDocUnit")
connection_AdditionalConnectionProperty = Class(name="connection_AdditionalConnectionProperty")
connection_SAPBWTable = Class(name="connection_SAPBWTable")
connection_SAPFunctionParameterColumn = Class(name="connection_SAPFunctionParameterColumn")
connection_SAPFunctionParameterTable = Class(name="connection_SAPFunctionParameterTable")
connection_SAPTestInputParameterTable = Class(name="connection_SAPTestInputParameterTable")
connection_SAPFunctionParamData = Class(name="connection_SAPFunctionParamData")
connection_SchemaTarget = Class(name="connection_SchemaTarget")
SAPFunctionParameterTable = Class(name="SAPFunctionParameterTable")
connection_RegexpFileConnection = Class(name="connection_RegexpFileConnection")
connection_XmlFileConnection = Class(name="connection_XmlFileConnection")
connection_XmlXPathLoopDescriptor = Class(name="connection_XmlXPathLoopDescriptor")
connection_XMLFileNode = Class(name="connection_XMLFileNode")
connection_GenericSchemaConnection = Class(name="connection_GenericSchemaConnection")
connection_LDAPSchemaConnection = Class(name="connection_LDAPSchemaConnection")
connection_Query = Class(name="connection_Query")
connection_LdifFileConnection = Class(name="connection_LdifFileConnection")
connection_FileExcelConnection = Class(name="connection_FileExcelConnection")
connection_WSDLSchemaConnection = Class(name="connection_WSDLSchemaConnection")
connection_CDCType = Class(name="connection_CDCType")
connection_WSDLParameter = Class(name="connection_WSDLParameter")
connection_SalesforceSchemaConnection = Class(name="connection_SalesforceSchemaConnection")
connection_SalesforceModuleUnit = Class(name="connection_SalesforceModuleUnit")
connection_HL7Connection = Class(name="connection_HL7Connection")
connection_HL7FileNode = Class(name="connection_HL7FileNode")
connection_SubscriberTable = Class(name="connection_SubscriberTable")
TdTable = Class(name="TdTable")
connection_ConceptTarget = Class(name="connection_ConceptTarget")
connection_FTPConnection = Class(name="connection_FTPConnection")
connection_HeaderFooterConnection = Class(name="connection_HeaderFooterConnection")
connection_GenericPackage = Class(name="connection_GenericPackage")
Package = Class(name="Package")
connection_ValidationRulesConnection = Class(name="connection_ValidationRulesConnection")
connection_BRMSConnection = Class(name="connection_BRMSConnection")
connection_EDIFACTConnection = Class(name="connection_EDIFACTConnection")
connection_EDIFACTColumn = Class(name="connection_EDIFACTColumn")
MetadataColumn = Class(name="MetadataColumn")
connection_ConditionType = Class(name="connection_ConditionType")
connection_InnerJoinMap = Class(name="connection_InnerJoinMap")
connection_SAPTable = Class(name="connection_SAPTable")
MetadataTable = Class(name="MetadataTable")
connection_SAPTableField = Class(name="connection_SAPTableField")
connection_SAPFunctionParameter = Class(name="connection_SAPFunctionParameter")
connection_relational_TdSqlDataType = Class(name="connection_relational_TdSqlDataType")
SQLSimpleType = Class(name="SQLSimpleType")
SAPTable = Class(name="SAPTable")
connection_SAPBWTableField = Class(name="connection_SAPBWTableField")
SAPTableField = Class(name="SAPTableField")
connection_relational_TdTable = Class(name="connection_relational_TdTable")
relational_Table = Class(name="relational_Table")
connection_relational_TdView = Class(name="connection_relational_TdView")
relational_View = Class(name="relational_View")
connection_relational_TdColumn = Class(name="connection_relational_TdColumn")
relational_TdSqlDataType = Class(name="relational_TdSqlDataType")
xml_connection_EObject = Class(name="xml_connection_EObject")
xml_TdXmlSchema = Class(name="xml_TdXmlSchema")
xml_TdXmlContent = Class(name="xml_TdXmlContent")
connection_xml_TdXmlContent = Class(name="connection_xml_TdXmlContent")
Content = Class(name="Content")
xml_TdXmlElementType = Class(name="xml_TdXmlElementType")
connection_xml_TdXmlSchema = Class(name="connection_xml_TdXmlSchema")
connection_relational_TdTrigger = Class(name="connection_relational_TdTrigger")
Trigger = Class(name="Trigger")
connection_relational_TdProcedure = Class(name="connection_relational_TdProcedure")
Procedure = Class(name="Procedure")
connection_relational_TdExpression = Class(name="connection_relational_TdExpression")
Expression = Class(name="Expression")
connection_softwaredeployment_TdDataManager = Class(name="connection_softwaredeployment_TdDataManager")
DataManager = Class(name="DataManager")
connection_softwaredeployment_TdSoftwareSystem = Class(name="connection_softwaredeployment_TdSoftwareSystem")
SoftwareSystem = Class(name="SoftwareSystem")
connection_softwaredeployment_TdMachine = Class(name="connection_softwaredeployment_TdMachine")
Machine = Class(name="Machine")
connection_xml_TdXmlElementType = Class(name="connection_xml_TdXmlElementType")
ElementType = Class(name="ElementType")
Schema = Class(name="Schema")

# connection_Metadata class attributes and methods

# AbstractMetadataObject class attributes and methods

# connection_Connection class attributes and methods
connection_Connection_version: Property = Property(name="version", type=StringType)
connection_Connection_ContextMode: Property = Property(name="ContextMode", type=BooleanType)
connection_Connection_ContextId: Property = Property(name="ContextId", type=StringType)
connection_Connection_contextName: Property = Property(name="contextName", type=StringType)
connection_Connection_m_getConnectionTypeName: Method = Method(name="getConnectionTypeName", parameters={}, type=StringType)
connection_Connection.attributes={connection_Connection_ContextId, connection_Connection_ContextMode, connection_Connection_version, connection_Connection_contextName}
connection_Connection.methods={connection_Connection_m_getConnectionTypeName}

# softwaredeployment_DataProvider class attributes and methods

# connection_QueriesConnection class attributes and methods

# connection_MetadataColumn class attributes and methods
connection_MetadataColumn_defaultValue: Property = Property(name="defaultValue", type=StringType)
connection_MetadataColumn_talendType: Property = Property(name="talendType", type=StringType)
connection_MetadataColumn_key: Property = Property(name="key", type=BooleanType)
connection_MetadataColumn_nullable: Property = Property(name="nullable", type=BooleanType)
connection_MetadataColumn_sourceType: Property = Property(name="sourceType", type=StringType)
connection_MetadataColumn_originalField: Property = Property(name="originalField", type=StringType)
connection_MetadataColumn_pattern: Property = Property(name="pattern", type=StringType)
connection_MetadataColumn_displayField: Property = Property(name="displayField", type=StringType)
connection_MetadataColumn_originalLength: Property = Property(name="originalLength", type=StringType)
connection_MetadataColumn_relatedEntity: Property = Property(name="relatedEntity", type=StringType)
connection_MetadataColumn_relationshipType: Property = Property(name="relationshipType", type=StringType)
connection_MetadataColumn.attributes={connection_MetadataColumn_defaultValue, connection_MetadataColumn_nullable, connection_MetadataColumn_talendType, connection_MetadataColumn_key, connection_MetadataColumn_pattern, connection_MetadataColumn_relationshipType, connection_MetadataColumn_originalLength, connection_MetadataColumn_originalField, connection_MetadataColumn_sourceType, connection_MetadataColumn_relatedEntity, connection_MetadataColumn_displayField}

# record_Field class attributes and methods

# core_Class class attributes and methods

# connection_MetadataTable class attributes and methods
connection_MetadataTable_sourceName: Property = Property(name="sourceName", type=StringType)
connection_MetadataTable_tableType: Property = Property(name="tableType", type=StringType)
connection_MetadataTable_attachedCDC: Property = Property(name="attachedCDC", type=BooleanType)
connection_MetadataTable_activatedCDC: Property = Property(name="activatedCDC", type=BooleanType)
connection_MetadataTable.attributes={connection_MetadataTable_sourceName, connection_MetadataTable_tableType, connection_MetadataTable_activatedCDC, connection_MetadataTable_attachedCDC}

# connection_AbstractMetadataObject class attributes and methods
connection_AbstractMetadataObject_divergency: Property = Property(name="divergency", type=BooleanType)
connection_AbstractMetadataObject_properties: Property = Property(name="properties", type=StringType)
connection_AbstractMetadataObject_id: Property = Property(name="id", type=StringType)
connection_AbstractMetadataObject_comment: Property = Property(name="comment", type=StringType)
connection_AbstractMetadataObject_label: Property = Property(name="label", type=StringType)
connection_AbstractMetadataObject_readOnly: Property = Property(name="readOnly", type=BooleanType)
connection_AbstractMetadataObject_synchronised: Property = Property(name="synchronised", type=BooleanType)
connection_AbstractMetadataObject.attributes={connection_AbstractMetadataObject_comment, connection_AbstractMetadataObject_properties, connection_AbstractMetadataObject_readOnly, connection_AbstractMetadataObject_label, connection_AbstractMetadataObject_id, connection_AbstractMetadataObject_divergency, connection_AbstractMetadataObject_synchronised}

# ModelElement class attributes and methods

# connection_DelimitedFileConnection class attributes and methods
connection_DelimitedFileConnection_FieldSeparatorType: Property = Property(name="FieldSeparatorType", type=StringType)
connection_DelimitedFileConnection_splitRecord: Property = Property(name="splitRecord", type=BooleanType)
connection_DelimitedFileConnection.attributes={connection_DelimitedFileConnection_splitRecord, connection_DelimitedFileConnection_FieldSeparatorType}

# FileConnection class attributes and methods

# connection_PositionalFileConnection class attributes and methods

# connection_EbcdicConnection class attributes and methods
connection_EbcdicConnection_MidFile: Property = Property(name="MidFile", type=StringType)
connection_EbcdicConnection_DataFile: Property = Property(name="DataFile", type=StringType)
connection_EbcdicConnection_CodePage: Property = Property(name="CodePage", type=StringType)
connection_EbcdicConnection_SourceFileStart: Property = Property(name="SourceFileStart", type=StringType)
connection_EbcdicConnection_SourceFileEnd: Property = Property(name="SourceFileEnd", type=StringType)
connection_EbcdicConnection.attributes={connection_EbcdicConnection_SourceFileEnd, connection_EbcdicConnection_SourceFileStart, connection_EbcdicConnection_MidFile, connection_EbcdicConnection_CodePage, connection_EbcdicConnection_DataFile}

# connection_AdditionalProperties class attributes and methods
connection_AdditionalProperties_key: Property = Property(name="key", type=StringType)
connection_AdditionalProperties_value: Property = Property(name="value", type=StringType)
connection_AdditionalProperties.attributes={connection_AdditionalProperties_value, connection_AdditionalProperties_key}

# connection_FileConnection class attributes and methods
connection_FileConnection_FirstLineCaption: Property = Property(name="FirstLineCaption", type=BooleanType)
connection_FileConnection_RemoveEmptyRow: Property = Property(name="RemoveEmptyRow", type=BooleanType)
connection_FileConnection_EscapeType: Property = Property(name="EscapeType", type=StringType)
connection_FileConnection_EscapeChar: Property = Property(name="EscapeChar", type=StringType)
connection_FileConnection_TextEnclosure: Property = Property(name="TextEnclosure", type=StringType)
connection_FileConnection_CsvOption: Property = Property(name="CsvOption", type=BooleanType)
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
connection_FileConnection.attributes={connection_FileConnection_RowSeparatorValue, connection_FileConnection_LimitValue, connection_FileConnection_FooterValue, connection_FileConnection_UseLimit, connection_FileConnection_UseHeader, connection_FileConnection_Format, connection_FileConnection_RemoveEmptyRow, connection_FileConnection_UseFooter, connection_FileConnection_Encoding, connection_FileConnection_Server, connection_FileConnection_FirstLineCaption, connection_FileConnection_RowSeparatorType, connection_FileConnection_FilePath, connection_FileConnection_EscapeType, connection_FileConnection_TextIdentifier, connection_FileConnection_HeaderValue, connection_FileConnection_FieldSeparatorValue, connection_FileConnection_CsvOption, connection_FileConnection_EscapeChar, connection_FileConnection_TextEnclosure}

# Connection class attributes and methods

# connection_DatabaseConnection class attributes and methods
connection_DatabaseConnection_DatabaseType: Property = Property(name="DatabaseType", type=StringType)
connection_DatabaseConnection_DBRootPath: Property = Property(name="DBRootPath", type=StringType)
connection_DatabaseConnection_AdditionalParams: Property = Property(name="AdditionalParams", type=StringType)
connection_DatabaseConnection_StandardSQL: Property = Property(name="StandardSQL", type=BooleanType)
connection_DatabaseConnection_SystemSQL: Property = Property(name="SystemSQL", type=BooleanType)
connection_DatabaseConnection_cdcTypeMode: Property = Property(name="cdcTypeMode", type=StringType)
connection_DatabaseConnection_SQLMode: Property = Property(name="SQLMode", type=BooleanType)
connection_DatabaseConnection_DriverJarPath: Property = Property(name="DriverJarPath", type=StringType)
connection_DatabaseConnection_DriverClass: Property = Property(name="DriverClass", type=StringType)
connection_DatabaseConnection_URL: Property = Property(name="URL", type=StringType)
connection_DatabaseConnection_dbVersionString: Property = Property(name="dbVersionString", type=StringType)
connection_DatabaseConnection_Port: Property = Property(name="Port", type=StringType)
connection_DatabaseConnection_Username: Property = Property(name="Username", type=StringType)
connection_DatabaseConnection_Password: Property = Property(name="Password", type=StringType)
connection_DatabaseConnection_ServerName: Property = Property(name="ServerName", type=StringType)
connection_DatabaseConnection_DatasourceName: Property = Property(name="DatasourceName", type=StringType)
connection_DatabaseConnection_FileFieldName: Property = Property(name="FileFieldName", type=StringType)
connection_DatabaseConnection_SID: Property = Property(name="SID", type=StringType)
connection_DatabaseConnection_SqlSynthax: Property = Property(name="SqlSynthax", type=StringType)
connection_DatabaseConnection_StringQuote: Property = Property(name="StringQuote", type=StringType)
connection_DatabaseConnection_NullChar: Property = Property(name="NullChar", type=StringType)
connection_DatabaseConnection_DbmsId: Property = Property(name="DbmsId", type=StringType)
connection_DatabaseConnection_ProductId: Property = Property(name="ProductId", type=StringType)
connection_DatabaseConnection_UiSchema: Property = Property(name="UiSchema", type=StringType)
connection_DatabaseConnection.attributes={connection_DatabaseConnection_Password, connection_DatabaseConnection_DriverJarPath, connection_DatabaseConnection_DbmsId, connection_DatabaseConnection_Port, connection_DatabaseConnection_FileFieldName, connection_DatabaseConnection_ProductId, connection_DatabaseConnection_dbVersionString, connection_DatabaseConnection_SID, connection_DatabaseConnection_URL, connection_DatabaseConnection_DBRootPath, connection_DatabaseConnection_DatabaseType, connection_DatabaseConnection_SystemSQL, connection_DatabaseConnection_UiSchema, connection_DatabaseConnection_StringQuote, connection_DatabaseConnection_DriverClass, connection_DatabaseConnection_DatasourceName, connection_DatabaseConnection_StandardSQL, connection_DatabaseConnection_SQLMode, connection_DatabaseConnection_ServerName, connection_DatabaseConnection_AdditionalParams, connection_DatabaseConnection_Username, connection_DatabaseConnection_NullChar, connection_DatabaseConnection_cdcTypeMode, connection_DatabaseConnection_SqlSynthax}

# connection_MDMConnection class attributes and methods
connection_MDMConnection_Username: Property = Property(name="Username", type=StringType)
connection_MDMConnection_Password: Property = Property(name="Password", type=StringType)
connection_MDMConnection_Port: Property = Property(name="Port", type=StringType)
connection_MDMConnection_Server: Property = Property(name="Server", type=StringType)
connection_MDMConnection_Universe: Property = Property(name="Universe", type=StringType)
connection_MDMConnection_Datamodel: Property = Property(name="Datamodel", type=StringType)
connection_MDMConnection_Datacluster: Property = Property(name="Datacluster", type=StringType)
connection_MDMConnection_protocol: Property = Property(name="protocol", type=StringType)
connection_MDMConnection_context: Property = Property(name="context", type=StringType)
connection_MDMConnection_serverUrl: Property = Property(name="serverUrl", type=StringType)
connection_MDMConnection_m_getConnectionString: Method = Method(name="getConnectionString", parameters={}, type=StringType)
connection_MDMConnection.attributes={connection_MDMConnection_Datamodel, connection_MDMConnection_protocol, connection_MDMConnection_Port, connection_MDMConnection_Universe, connection_MDMConnection_serverUrl, connection_MDMConnection_Server, connection_MDMConnection_Username, connection_MDMConnection_Password, connection_MDMConnection_Datacluster, connection_MDMConnection_context}
connection_MDMConnection.methods={connection_MDMConnection_m_getConnectionString}

# connection_Concept class attributes and methods
connection_Concept_conceptType: Property = Property(name="conceptType", type=StringType)
connection_Concept_xPathPrefix: Property = Property(name="xPathPrefix", type=StringType)
connection_Concept_LoopExpression: Property = Property(name="LoopExpression", type=StringType)
connection_Concept_LoopLimit: Property = Property(name="LoopLimit", type=StringType)
connection_Concept_inputModel: Property = Property(name="inputModel", type=BooleanType)
connection_Concept.attributes={connection_Concept_conceptType, connection_Concept_LoopLimit, connection_Concept_inputModel, connection_Concept_xPathPrefix, connection_Concept_LoopExpression}

# connection_CDCConnection class attributes and methods

# connection_InputSAPFunctionParameterTable class attributes and methods

# connection_OutputSAPFunctionParameterTable class attributes and methods

# connection_SAPConnection class attributes and methods
connection_SAPConnection_Host: Property = Property(name="Host", type=StringType)
connection_SAPConnection_Username: Property = Property(name="Username", type=StringType)
connection_SAPConnection_Password: Property = Property(name="Password", type=StringType)
connection_SAPConnection_Client: Property = Property(name="Client", type=StringType)
connection_SAPConnection_SystemNumber: Property = Property(name="SystemNumber", type=StringType)
connection_SAPConnection_Language: Property = Property(name="Language", type=StringType)
connection_SAPConnection_currentFucntion: Property = Property(name="currentFucntion", type=StringType)
connection_SAPConnection_jcoVersion: Property = Property(name="jcoVersion", type=StringType)
connection_SAPConnection.attributes={connection_SAPConnection_Language, connection_SAPConnection_Username, connection_SAPConnection_currentFucntion, connection_SAPConnection_Client, connection_SAPConnection_SystemNumber, connection_SAPConnection_jcoVersion, connection_SAPConnection_Password, connection_SAPConnection_Host}

# connection_SAPFunctionUnit class attributes and methods
connection_SAPFunctionUnit_OutputType: Property = Property(name="OutputType", type=StringType)
connection_SAPFunctionUnit_OutputTableName: Property = Property(name="OutputTableName", type=StringType)
connection_SAPFunctionUnit_asXmlSchema: Property = Property(name="asXmlSchema", type=BooleanType)
connection_SAPFunctionUnit_m_setDocument: Method = Method(name="setDocument", parameters={Parameter(name='connection_document', type=StringType)})
connection_SAPFunctionUnit.attributes={connection_SAPFunctionUnit_OutputType, connection_SAPFunctionUnit_OutputTableName, connection_SAPFunctionUnit_asXmlSchema}
connection_SAPFunctionUnit.methods={connection_SAPFunctionUnit_m_setDocument}

# connection_SAPIDocUnit class attributes and methods
connection_SAPIDocUnit_programId: Property = Property(name="programId", type=StringType)
connection_SAPIDocUnit_gatewayService: Property = Property(name="gatewayService", type=StringType)
connection_SAPIDocUnit_useXmlOutput: Property = Property(name="useXmlOutput", type=BooleanType)
connection_SAPIDocUnit_xmlFile: Property = Property(name="xmlFile", type=StringType)
connection_SAPIDocUnit_useHtmlOutput: Property = Property(name="useHtmlOutput", type=BooleanType)
connection_SAPIDocUnit_htmlFile: Property = Property(name="htmlFile", type=StringType)
connection_SAPIDocUnit.attributes={connection_SAPIDocUnit_gatewayService, connection_SAPIDocUnit_useXmlOutput, connection_SAPIDocUnit_htmlFile, connection_SAPIDocUnit_useHtmlOutput, connection_SAPIDocUnit_xmlFile, connection_SAPIDocUnit_programId}

# connection_AdditionalConnectionProperty class attributes and methods
connection_AdditionalConnectionProperty_propertyName: Property = Property(name="propertyName", type=StringType)
connection_AdditionalConnectionProperty_Value: Property = Property(name="Value", type=StringType)
connection_AdditionalConnectionProperty.attributes={connection_AdditionalConnectionProperty_Value, connection_AdditionalConnectionProperty_propertyName}

# connection_SAPBWTable class attributes and methods
connection_SAPBWTable_modelType: Property = Property(name="modelType", type=StringType)
connection_SAPBWTable_active: Property = Property(name="active", type=BooleanType)
connection_SAPBWTable_sourceSystemName: Property = Property(name="sourceSystemName", type=StringType)
connection_SAPBWTable_infoAreaName: Property = Property(name="infoAreaName", type=StringType)
connection_SAPBWTable_innerIOType: Property = Property(name="innerIOType", type=StringType)
connection_SAPBWTable.attributes={connection_SAPBWTable_innerIOType, connection_SAPBWTable_active, connection_SAPBWTable_sourceSystemName, connection_SAPBWTable_infoAreaName, connection_SAPBWTable_modelType}

# connection_SAPFunctionParameterColumn class attributes and methods
connection_SAPFunctionParameterColumn_ParameterType: Property = Property(name="ParameterType", type=StringType)
connection_SAPFunctionParameterColumn_StructureOrTableName: Property = Property(name="StructureOrTableName", type=StringType)
connection_SAPFunctionParameterColumn_DataType: Property = Property(name="DataType", type=StringType)
connection_SAPFunctionParameterColumn_Length: Property = Property(name="Length", type=StringType)
connection_SAPFunctionParameterColumn_Value: Property = Property(name="Value", type=StringType)
connection_SAPFunctionParameterColumn_m_setDescription: Method = Method(name="setDescription", parameters={Parameter(name='connection_description', type=StringType)})
connection_SAPFunctionParameterColumn.attributes={connection_SAPFunctionParameterColumn_ParameterType, connection_SAPFunctionParameterColumn_Length, connection_SAPFunctionParameterColumn_DataType, connection_SAPFunctionParameterColumn_StructureOrTableName, connection_SAPFunctionParameterColumn_Value}
connection_SAPFunctionParameterColumn.methods={connection_SAPFunctionParameterColumn_m_setDescription}

# connection_SAPFunctionParameterTable class attributes and methods

# connection_SAPTestInputParameterTable class attributes and methods

# connection_SAPFunctionParamData class attributes and methods

# connection_SchemaTarget class attributes and methods
connection_SchemaTarget_RelativeXPathQuery: Property = Property(name="RelativeXPathQuery", type=StringType)
connection_SchemaTarget_TagName: Property = Property(name="TagName", type=StringType)
connection_SchemaTarget.attributes={connection_SchemaTarget_RelativeXPathQuery, connection_SchemaTarget_TagName}

# SAPFunctionParameterTable class attributes and methods

# connection_RegexpFileConnection class attributes and methods
connection_RegexpFileConnection_FieldSeparatorType: Property = Property(name="FieldSeparatorType", type=StringType)
connection_RegexpFileConnection.attributes={connection_RegexpFileConnection_FieldSeparatorType}

# connection_XmlFileConnection class attributes and methods
connection_XmlFileConnection_inputModel: Property = Property(name="inputModel", type=BooleanType)
connection_XmlFileConnection_outputFilePath: Property = Property(name="outputFilePath", type=StringType)
connection_XmlFileConnection_fileContent: Property = Property(name="fileContent", type=StringType)
connection_XmlFileConnection_XsdFilePath: Property = Property(name="XsdFilePath", type=StringType)
connection_XmlFileConnection_XmlFilePath: Property = Property(name="XmlFilePath", type=StringType)
connection_XmlFileConnection_Guess: Property = Property(name="Guess", type=BooleanType)
connection_XmlFileConnection_MaskXPattern: Property = Property(name="MaskXPattern", type=StringType)
connection_XmlFileConnection_Encoding: Property = Property(name="Encoding", type=StringType)
connection_XmlFileConnection.attributes={connection_XmlFileConnection_Guess, connection_XmlFileConnection_outputFilePath, connection_XmlFileConnection_MaskXPattern, connection_XmlFileConnection_Encoding, connection_XmlFileConnection_XsdFilePath, connection_XmlFileConnection_fileContent, connection_XmlFileConnection_XmlFilePath, connection_XmlFileConnection_inputModel}

# connection_XmlXPathLoopDescriptor class attributes and methods
connection_XmlXPathLoopDescriptor_AbsoluteXPathQuery: Property = Property(name="AbsoluteXPathQuery", type=StringType)
connection_XmlXPathLoopDescriptor_LimitBoucle: Property = Property(name="LimitBoucle", type=StringType)
connection_XmlXPathLoopDescriptor.attributes={connection_XmlXPathLoopDescriptor_LimitBoucle, connection_XmlXPathLoopDescriptor_AbsoluteXPathQuery}

# connection_XMLFileNode class attributes and methods
connection_XMLFileNode_XMLPath: Property = Property(name="XMLPath", type=StringType)
connection_XMLFileNode_RelatedColumn: Property = Property(name="RelatedColumn", type=StringType)
connection_XMLFileNode_DefaultValue: Property = Property(name="DefaultValue", type=StringType)
connection_XMLFileNode_Attribute: Property = Property(name="Attribute", type=StringType)
connection_XMLFileNode_Order: Property = Property(name="Order", type=IntegerType)
connection_XMLFileNode_Type: Property = Property(name="Type", type=StringType)
connection_XMLFileNode.attributes={connection_XMLFileNode_XMLPath, connection_XMLFileNode_Order, connection_XMLFileNode_Type, connection_XMLFileNode_RelatedColumn, connection_XMLFileNode_Attribute, connection_XMLFileNode_DefaultValue}

# connection_GenericSchemaConnection class attributes and methods
connection_GenericSchemaConnection_mappingTypeUsed: Property = Property(name="mappingTypeUsed", type=BooleanType)
connection_GenericSchemaConnection_mappingTypeId: Property = Property(name="mappingTypeId", type=StringType)
connection_GenericSchemaConnection.attributes={connection_GenericSchemaConnection_mappingTypeId, connection_GenericSchemaConnection_mappingTypeUsed}

# connection_LDAPSchemaConnection class attributes and methods
connection_LDAPSchemaConnection_Host: Property = Property(name="Host", type=StringType)
connection_LDAPSchemaConnection_Port: Property = Property(name="Port", type=StringType)
connection_LDAPSchemaConnection_Protocol: Property = Property(name="Protocol", type=StringType)
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
connection_LDAPSchemaConnection_ReturnAttributes: Property = Property(name="ReturnAttributes", type=StringType)
connection_LDAPSchemaConnection_SelectedDN: Property = Property(name="SelectedDN", type=StringType)
connection_LDAPSchemaConnection.attributes={connection_LDAPSchemaConnection_Value, connection_LDAPSchemaConnection_EncryptionMethodName, connection_LDAPSchemaConnection_Port, connection_LDAPSchemaConnection_UseLimit, connection_LDAPSchemaConnection_Referrals, connection_LDAPSchemaConnection_SelectedDN, connection_LDAPSchemaConnection_BaseDNs, connection_LDAPSchemaConnection_LimitValue, connection_LDAPSchemaConnection_Filter, connection_LDAPSchemaConnection_StorePath, connection_LDAPSchemaConnection_TimeOutLimit, connection_LDAPSchemaConnection_GetBaseDNsFromRoot, connection_LDAPSchemaConnection_CountLimit, connection_LDAPSchemaConnection_Host, connection_LDAPSchemaConnection_BindPrincipal, connection_LDAPSchemaConnection_BindPassword, connection_LDAPSchemaConnection_UseAdvanced, connection_LDAPSchemaConnection_Protocol, connection_LDAPSchemaConnection_Separator, connection_LDAPSchemaConnection_Aliases, connection_LDAPSchemaConnection_SavePassword, connection_LDAPSchemaConnection_UseAuthen, connection_LDAPSchemaConnection_ReturnAttributes}

# connection_Query class attributes and methods
connection_Query_value: Property = Property(name="value", type=StringType)
connection_Query_contextMode: Property = Property(name="contextMode", type=BooleanType)
connection_Query.attributes={connection_Query_value, connection_Query_contextMode}

# connection_LdifFileConnection class attributes and methods
connection_LdifFileConnection_value: Property = Property(name="value", type=StringType)
connection_LdifFileConnection_FilePath: Property = Property(name="FilePath", type=StringType)
connection_LdifFileConnection_LimitEntry: Property = Property(name="LimitEntry", type=IntegerType)
connection_LdifFileConnection_UseLimit: Property = Property(name="UseLimit", type=BooleanType)
connection_LdifFileConnection_Server: Property = Property(name="Server", type=StringType)
connection_LdifFileConnection.attributes={connection_LdifFileConnection_Server, connection_LdifFileConnection_value, connection_LdifFileConnection_UseLimit, connection_LdifFileConnection_FilePath, connection_LdifFileConnection_LimitEntry}

# connection_FileExcelConnection class attributes and methods
connection_FileExcelConnection_SheetName: Property = Property(name="SheetName", type=StringType)
connection_FileExcelConnection_sheetColumns: Property = Property(name="sheetColumns", type=StringType)
connection_FileExcelConnection_firstColumn: Property = Property(name="firstColumn", type=StringType)
connection_FileExcelConnection_lastColumn: Property = Property(name="lastColumn", type=StringType)
connection_FileExcelConnection_thousandSeparator: Property = Property(name="thousandSeparator", type=StringType)
connection_FileExcelConnection_decimalSeparator: Property = Property(name="decimalSeparator", type=StringType)
connection_FileExcelConnection_advancedSpearator: Property = Property(name="advancedSpearator", type=BooleanType)
connection_FileExcelConnection_selectAllSheets: Property = Property(name="selectAllSheets", type=BooleanType)
connection_FileExcelConnection_sheetList: Property = Property(name="sheetList", type=StringType)
connection_FileExcelConnection_generationMode: Property = Property(name="generationMode", type=StringType)
connection_FileExcelConnection.attributes={connection_FileExcelConnection_sheetColumns, connection_FileExcelConnection_selectAllSheets, connection_FileExcelConnection_thousandSeparator, connection_FileExcelConnection_advancedSpearator, connection_FileExcelConnection_firstColumn, connection_FileExcelConnection_decimalSeparator, connection_FileExcelConnection_generationMode, connection_FileExcelConnection_sheetList, connection_FileExcelConnection_lastColumn, connection_FileExcelConnection_SheetName}

# connection_WSDLSchemaConnection class attributes and methods
connection_WSDLSchemaConnection_proxyHost: Property = Property(name="proxyHost", type=StringType)
connection_WSDLSchemaConnection_proxyPort: Property = Property(name="proxyPort", type=StringType)
connection_WSDLSchemaConnection_proxyUser: Property = Property(name="proxyUser", type=StringType)
connection_WSDLSchemaConnection_proxyPassword: Property = Property(name="proxyPassword", type=StringType)
connection_WSDLSchemaConnection_Value: Property = Property(name="Value", type=StringType)
connection_WSDLSchemaConnection_EndpointURI: Property = Property(name="EndpointURI", type=StringType)
connection_WSDLSchemaConnection_Encoding: Property = Property(name="Encoding", type=StringType)
connection_WSDLSchemaConnection_timeOut: Property = Property(name="timeOut", type=IntegerType)
connection_WSDLSchemaConnection_isInputModel: Property = Property(name="isInputModel", type=BooleanType)
connection_WSDLSchemaConnection_serverNameSpace: Property = Property(name="serverNameSpace", type=StringType)
connection_WSDLSchemaConnection_serverName: Property = Property(name="serverName", type=StringType)
connection_WSDLSchemaConnection_portNameSpace: Property = Property(name="portNameSpace", type=StringType)
connection_WSDLSchemaConnection_portName: Property = Property(name="portName", type=StringType)
connection_WSDLSchemaConnection_WSDL: Property = Property(name="WSDL", type=StringType)
connection_WSDLSchemaConnection_needAuth: Property = Property(name="needAuth", type=BooleanType)
connection_WSDLSchemaConnection_methodName: Property = Property(name="methodName", type=StringType)
connection_WSDLSchemaConnection_parameters: Property = Property(name="parameters", type=StringType)
connection_WSDLSchemaConnection_UserName: Property = Property(name="UserName", type=StringType)
connection_WSDLSchemaConnection_Password: Property = Property(name="Password", type=StringType)
connection_WSDLSchemaConnection_useProxy: Property = Property(name="useProxy", type=BooleanType)
connection_WSDLSchemaConnection.attributes={connection_WSDLSchemaConnection_isInputModel, connection_WSDLSchemaConnection_Password, connection_WSDLSchemaConnection_proxyPort, connection_WSDLSchemaConnection_portNameSpace, connection_WSDLSchemaConnection_EndpointURI, connection_WSDLSchemaConnection_proxyUser, connection_WSDLSchemaConnection_timeOut, connection_WSDLSchemaConnection_WSDL, connection_WSDLSchemaConnection_Encoding, connection_WSDLSchemaConnection_serverNameSpace, connection_WSDLSchemaConnection_UserName, connection_WSDLSchemaConnection_proxyPassword, connection_WSDLSchemaConnection_parameters, connection_WSDLSchemaConnection_serverName, connection_WSDLSchemaConnection_useProxy, connection_WSDLSchemaConnection_proxyHost, connection_WSDLSchemaConnection_Value, connection_WSDLSchemaConnection_portName, connection_WSDLSchemaConnection_methodName, connection_WSDLSchemaConnection_needAuth}

# connection_CDCType class attributes and methods
connection_CDCType_linkDB: Property = Property(name="linkDB", type=StringType)
connection_CDCType_journalName: Property = Property(name="journalName", type=StringType)
connection_CDCType.attributes={connection_CDCType_journalName, connection_CDCType_linkDB}

# connection_WSDLParameter class attributes and methods
connection_WSDLParameter_Element: Property = Property(name="Element", type=StringType)
connection_WSDLParameter_source: Property = Property(name="source", type=StringType)
connection_WSDLParameter_Column: Property = Property(name="Column", type=StringType)
connection_WSDLParameter_Expression: Property = Property(name="Expression", type=StringType)
connection_WSDLParameter_ParameterInfo: Property = Property(name="ParameterInfo", type=StringType)
connection_WSDLParameter_ParameterInfoParent: Property = Property(name="ParameterInfoParent", type=StringType)
connection_WSDLParameter.attributes={connection_WSDLParameter_source, connection_WSDLParameter_ParameterInfoParent, connection_WSDLParameter_ParameterInfo, connection_WSDLParameter_Column, connection_WSDLParameter_Element, connection_WSDLParameter_Expression}

# connection_SalesforceSchemaConnection class attributes and methods
connection_SalesforceSchemaConnection_callbackPort: Property = Property(name="callbackPort", type=StringType)
connection_SalesforceSchemaConnection_salesforceVersion: Property = Property(name="salesforceVersion", type=StringType)
connection_SalesforceSchemaConnection_token: Property = Property(name="token", type=StringType)
connection_SalesforceSchemaConnection_loginType: Property = Property(name="loginType", type=StringType)
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
connection_SalesforceSchemaConnection_webServiceUrlTextForOAuth: Property = Property(name="webServiceUrlTextForOAuth", type=StringType)
connection_SalesforceSchemaConnection_consumeKey: Property = Property(name="consumeKey", type=StringType)
connection_SalesforceSchemaConnection_consumeSecret: Property = Property(name="consumeSecret", type=StringType)
connection_SalesforceSchemaConnection_callbackHost: Property = Property(name="callbackHost", type=StringType)
connection_SalesforceSchemaConnection.attributes={connection_SalesforceSchemaConnection_callbackHost, connection_SalesforceSchemaConnection_token, connection_SalesforceSchemaConnection_userName, connection_SalesforceSchemaConnection_proxyPort, connection_SalesforceSchemaConnection_salesforceVersion, connection_SalesforceSchemaConnection_useCustomModuleName, connection_SalesforceSchemaConnection_webServiceUrlTextForOAuth, connection_SalesforceSchemaConnection_password, connection_SalesforceSchemaConnection_moduleName, connection_SalesforceSchemaConnection_proxyHost, connection_SalesforceSchemaConnection_useAlphbet, connection_SalesforceSchemaConnection_webServiceUrl, connection_SalesforceSchemaConnection_batchSize, connection_SalesforceSchemaConnection_consumeKey, connection_SalesforceSchemaConnection_loginType, connection_SalesforceSchemaConnection_proxyPassword, connection_SalesforceSchemaConnection_consumeSecret, connection_SalesforceSchemaConnection_useProxy, connection_SalesforceSchemaConnection_proxyUsername, connection_SalesforceSchemaConnection_timeOut, connection_SalesforceSchemaConnection_callbackPort, connection_SalesforceSchemaConnection_useHttpProxy, connection_SalesforceSchemaConnection_queryCondition}

# connection_SalesforceModuleUnit class attributes and methods
connection_SalesforceModuleUnit_moduleName: Property = Property(name="moduleName", type=StringType)
connection_SalesforceModuleUnit.attributes={connection_SalesforceModuleUnit_moduleName}

# connection_HL7Connection class attributes and methods
connection_HL7Connection_StartChar: Property = Property(name="StartChar", type=StringType)
connection_HL7Connection_EndChar: Property = Property(name="EndChar", type=StringType)
connection_HL7Connection_outputFilePath: Property = Property(name="outputFilePath", type=StringType)
connection_HL7Connection.attributes={connection_HL7Connection_outputFilePath, connection_HL7Connection_EndChar, connection_HL7Connection_StartChar}

# connection_HL7FileNode class attributes and methods
connection_HL7FileNode_Order: Property = Property(name="Order", type=IntegerType)
connection_HL7FileNode_Attribute: Property = Property(name="Attribute", type=StringType)
connection_HL7FileNode_DefaultValue: Property = Property(name="DefaultValue", type=StringType)
connection_HL7FileNode_RelatedColumn: Property = Property(name="RelatedColumn", type=StringType)
connection_HL7FileNode_Repeatable: Property = Property(name="Repeatable", type=BooleanType)
connection_HL7FileNode_FilePath: Property = Property(name="FilePath", type=StringType)
connection_HL7FileNode.attributes={connection_HL7FileNode_Order, connection_HL7FileNode_FilePath, connection_HL7FileNode_Attribute, connection_HL7FileNode_Repeatable, connection_HL7FileNode_DefaultValue, connection_HL7FileNode_RelatedColumn}

# connection_SubscriberTable class attributes and methods
connection_SubscriberTable_system: Property = Property(name="system", type=BooleanType)
connection_SubscriberTable.attributes={connection_SubscriberTable_system}

# TdTable class attributes and methods

# connection_ConceptTarget class attributes and methods
connection_ConceptTarget_targetName: Property = Property(name="targetName", type=StringType)
connection_ConceptTarget_RelativeLoopExpression: Property = Property(name="RelativeLoopExpression", type=StringType)
connection_ConceptTarget.attributes={connection_ConceptTarget_RelativeLoopExpression, connection_ConceptTarget_targetName}

# connection_FTPConnection class attributes and methods
connection_FTPConnection_Host: Property = Property(name="Host", type=StringType)
connection_FTPConnection_Port: Property = Property(name="Port", type=StringType)
connection_FTPConnection_Username: Property = Property(name="Username", type=StringType)
connection_FTPConnection_Password: Property = Property(name="Password", type=StringType)
connection_FTPConnection_Mode: Property = Property(name="Mode", type=StringType)
connection_FTPConnection_Ecoding: Property = Property(name="Ecoding", type=StringType)
connection_FTPConnection_SFTP: Property = Property(name="SFTP", type=BooleanType)
connection_FTPConnection_FTPS: Property = Property(name="FTPS", type=BooleanType)
connection_FTPConnection_Method: Property = Property(name="Method", type=StringType)
connection_FTPConnection_Privatekey: Property = Property(name="Privatekey", type=StringType)
connection_FTPConnection_Passphrase: Property = Property(name="Passphrase", type=StringType)
connection_FTPConnection_KeystoreFile: Property = Property(name="KeystoreFile", type=StringType)
connection_FTPConnection_KeystorePassword: Property = Property(name="KeystorePassword", type=StringType)
connection_FTPConnection_Usesocks: Property = Property(name="Usesocks", type=BooleanType)
connection_FTPConnection_Proxyhost: Property = Property(name="Proxyhost", type=StringType)
connection_FTPConnection_Proxyport: Property = Property(name="Proxyport", type=StringType)
connection_FTPConnection_Proxyuser: Property = Property(name="Proxyuser", type=StringType)
connection_FTPConnection_Proxypassword: Property = Property(name="Proxypassword", type=StringType)
connection_FTPConnection_CustomEncode: Property = Property(name="CustomEncode", type=StringType)
connection_FTPConnection.attributes={connection_FTPConnection_Proxypassword, connection_FTPConnection_Port, connection_FTPConnection_Privatekey, connection_FTPConnection_Method, connection_FTPConnection_KeystoreFile, connection_FTPConnection_Username, connection_FTPConnection_Host, connection_FTPConnection_Password, connection_FTPConnection_Proxyhost, connection_FTPConnection_Proxyport, connection_FTPConnection_Proxyuser, connection_FTPConnection_Passphrase, connection_FTPConnection_Usesocks, connection_FTPConnection_FTPS, connection_FTPConnection_SFTP, connection_FTPConnection_Ecoding, connection_FTPConnection_CustomEncode, connection_FTPConnection_KeystorePassword, connection_FTPConnection_Mode}

# connection_HeaderFooterConnection class attributes and methods
connection_HeaderFooterConnection_isHeader: Property = Property(name="isHeader", type=BooleanType)
connection_HeaderFooterConnection_imports: Property = Property(name="imports", type=StringType)
connection_HeaderFooterConnection_mainCode: Property = Property(name="mainCode", type=StringType)
connection_HeaderFooterConnection_libraries: Property = Property(name="libraries", type=StringType)
connection_HeaderFooterConnection.attributes={connection_HeaderFooterConnection_isHeader, connection_HeaderFooterConnection_imports, connection_HeaderFooterConnection_libraries, connection_HeaderFooterConnection_mainCode}

# connection_GenericPackage class attributes and methods

# Package class attributes and methods

# connection_ValidationRulesConnection class attributes and methods
connection_ValidationRulesConnection_isSelect: Property = Property(name="isSelect", type=BooleanType)
connection_ValidationRulesConnection_isInsert: Property = Property(name="isInsert", type=BooleanType)
connection_ValidationRulesConnection_isUpdate: Property = Property(name="isUpdate", type=BooleanType)
connection_ValidationRulesConnection_isDelete: Property = Property(name="isDelete", type=BooleanType)
connection_ValidationRulesConnection_type: Property = Property(name="type", type=StringType)
connection_ValidationRulesConnection_baseSchema: Property = Property(name="baseSchema", type=StringType)
connection_ValidationRulesConnection_baseColumnNames: Property = Property(name="baseColumnNames", type=StringType)
connection_ValidationRulesConnection_refSchema: Property = Property(name="refSchema", type=StringType)
connection_ValidationRulesConnection_refColumnNames: Property = Property(name="refColumnNames", type=StringType)
connection_ValidationRulesConnection_javaCondition: Property = Property(name="javaCondition", type=StringType)
connection_ValidationRulesConnection_sqlCondition: Property = Property(name="sqlCondition", type=StringType)
connection_ValidationRulesConnection_logicalOperator: Property = Property(name="logicalOperator", type=StringType)
connection_ValidationRulesConnection_isDisallow: Property = Property(name="isDisallow", type=BooleanType)
connection_ValidationRulesConnection_isRejectLink: Property = Property(name="isRejectLink", type=BooleanType)
connection_ValidationRulesConnection.attributes={connection_ValidationRulesConnection_sqlCondition, connection_ValidationRulesConnection_baseSchema, connection_ValidationRulesConnection_javaCondition, connection_ValidationRulesConnection_isSelect, connection_ValidationRulesConnection_isDelete, connection_ValidationRulesConnection_refColumnNames, connection_ValidationRulesConnection_isDisallow, connection_ValidationRulesConnection_logicalOperator, connection_ValidationRulesConnection_type, connection_ValidationRulesConnection_refSchema, connection_ValidationRulesConnection_isUpdate, connection_ValidationRulesConnection_baseColumnNames, connection_ValidationRulesConnection_isRejectLink, connection_ValidationRulesConnection_isInsert}

# connection_BRMSConnection class attributes and methods
connection_BRMSConnection_xmlField: Property = Property(name="xmlField", type=StringType)
connection_BRMSConnection_urlName: Property = Property(name="urlName", type=StringType)
connection_BRMSConnection_tacWebappName: Property = Property(name="tacWebappName", type=StringType)
connection_BRMSConnection_className: Property = Property(name="className", type=StringType)
connection_BRMSConnection_moduleUsed: Property = Property(name="moduleUsed", type=StringType)
connection_BRMSConnection_package: Property = Property(name="package", type=StringType)
connection_BRMSConnection.attributes={connection_BRMSConnection_tacWebappName, connection_BRMSConnection_className, connection_BRMSConnection_xmlField, connection_BRMSConnection_moduleUsed, connection_BRMSConnection_package, connection_BRMSConnection_urlName}

# connection_EDIFACTConnection class attributes and methods
connection_EDIFACTConnection_XmlName: Property = Property(name="XmlName", type=StringType)
connection_EDIFACTConnection_FileName: Property = Property(name="FileName", type=StringType)
connection_EDIFACTConnection_XmlPath: Property = Property(name="XmlPath", type=StringType)
connection_EDIFACTConnection.attributes={connection_EDIFACTConnection_XmlName, connection_EDIFACTConnection_XmlPath, connection_EDIFACTConnection_FileName}

# connection_EDIFACTColumn class attributes and methods
connection_EDIFACTColumn_EDIColumnName: Property = Property(name="EDIColumnName", type=StringType)
connection_EDIFACTColumn_EDIXpath: Property = Property(name="EDIXpath", type=StringType)
connection_EDIFACTColumn.attributes={connection_EDIFACTColumn_EDIColumnName, connection_EDIFACTColumn_EDIXpath}

# MetadataColumn class attributes and methods

# connection_ConditionType class attributes and methods
connection_ConditionType_inputColumn: Property = Property(name="inputColumn", type=StringType)
connection_ConditionType_function: Property = Property(name="function", type=StringType)
connection_ConditionType_operator: Property = Property(name="operator", type=StringType)
connection_ConditionType_value: Property = Property(name="value", type=StringType)
connection_ConditionType.attributes={connection_ConditionType_value, connection_ConditionType_function, connection_ConditionType_inputColumn, connection_ConditionType_operator}

# connection_InnerJoinMap class attributes and methods
connection_InnerJoinMap_key: Property = Property(name="key", type=StringType)
connection_InnerJoinMap_value: Property = Property(name="value", type=StringType)
connection_InnerJoinMap.attributes={connection_InnerJoinMap_key, connection_InnerJoinMap_value}

# connection_SAPTable class attributes and methods
connection_SAPTable_tableSearchType: Property = Property(name="tableSearchType", type=StringType)
connection_SAPTable.attributes={connection_SAPTable_tableSearchType}

# MetadataTable class attributes and methods

# connection_SAPTableField class attributes and methods
connection_SAPTableField_businessName: Property = Property(name="businessName", type=StringType)
connection_SAPTableField_refTable: Property = Property(name="refTable", type=StringType)
connection_SAPTableField.attributes={connection_SAPTableField_businessName, connection_SAPTableField_refTable}

# connection_SAPFunctionParameter class attributes and methods
connection_SAPFunctionParameter_description: Property = Property(name="description", type=StringType)
connection_SAPFunctionParameter_length: Property = Property(name="length", type=StringType)
connection_SAPFunctionParameter_changing: Property = Property(name="changing", type=BooleanType)
connection_SAPFunctionParameter_testValue: Property = Property(name="testValue", type=StringType)
connection_SAPFunctionParameter_tableResideInTables: Property = Property(name="tableResideInTables", type=BooleanType)
connection_SAPFunctionParameter_name: Property = Property(name="name", type=StringType)
connection_SAPFunctionParameter_type: Property = Property(name="type", type=StringType)
connection_SAPFunctionParameter.attributes={connection_SAPFunctionParameter_changing, connection_SAPFunctionParameter_testValue, connection_SAPFunctionParameter_tableResideInTables, connection_SAPFunctionParameter_description, connection_SAPFunctionParameter_length, connection_SAPFunctionParameter_name, connection_SAPFunctionParameter_type}

# connection_relational_TdSqlDataType class attributes and methods
connection_relational_TdSqlDataType_javaDataType: Property = Property(name="javaDataType", type=IntegerType)
connection_relational_TdSqlDataType_nullable: Property = Property(name="nullable", type=StringType)
connection_relational_TdSqlDataType_unsignedAttribute: Property = Property(name="unsignedAttribute", type=StringType)
connection_relational_TdSqlDataType_caseSensitive: Property = Property(name="caseSensitive", type=StringType)
connection_relational_TdSqlDataType_autoIncrement: Property = Property(name="autoIncrement", type=StringType)
connection_relational_TdSqlDataType_localTypeName: Property = Property(name="localTypeName", type=StringType)
connection_relational_TdSqlDataType_searchable: Property = Property(name="searchable", type=StringType)
connection_relational_TdSqlDataType.attributes={connection_relational_TdSqlDataType_nullable, connection_relational_TdSqlDataType_unsignedAttribute, connection_relational_TdSqlDataType_javaDataType, connection_relational_TdSqlDataType_localTypeName, connection_relational_TdSqlDataType_caseSensitive, connection_relational_TdSqlDataType_searchable, connection_relational_TdSqlDataType_autoIncrement}

# SQLSimpleType class attributes and methods

# SAPTable class attributes and methods

# connection_SAPBWTableField class attributes and methods
connection_SAPBWTableField_logicalName: Property = Property(name="logicalName", type=StringType)
connection_SAPBWTableField.attributes={connection_SAPBWTableField_logicalName}

# SAPTableField class attributes and methods

# connection_relational_TdTable class attributes and methods

# relational_Table class attributes and methods

# connection_relational_TdView class attributes and methods

# relational_View class attributes and methods

# connection_relational_TdColumn class attributes and methods
connection_relational_TdColumn_m_setContentType: Method = Method(name="setContentType", parameters={Parameter(name='connection_contentType', type=StringType)})
connection_relational_TdColumn_m_getContentType: Method = Method(name="getContentType", parameters={}, type=StringType)
connection_relational_TdColumn_m_getJavaType: Method = Method(name="getJavaType", parameters={}, type=IntegerType)
connection_relational_TdColumn.methods={connection_relational_TdColumn_m_getContentType, connection_relational_TdColumn_m_setContentType, connection_relational_TdColumn_m_getJavaType}

# relational_TdSqlDataType class attributes and methods

# xml_connection_EObject class attributes and methods

# xml_TdXmlSchema class attributes and methods

# xml_TdXmlContent class attributes and methods

# connection_xml_TdXmlContent class attributes and methods

# Content class attributes and methods

# xml_TdXmlElementType class attributes and methods

# connection_xml_TdXmlSchema class attributes and methods
connection_xml_TdXmlSchema_xsdFilePath: Property = Property(name="xsdFilePath", type=StringType)
connection_xml_TdXmlSchema.attributes={connection_xml_TdXmlSchema_xsdFilePath}

# connection_relational_TdTrigger class attributes and methods

# Trigger class attributes and methods

# connection_relational_TdProcedure class attributes and methods

# Procedure class attributes and methods

# connection_relational_TdExpression class attributes and methods
connection_relational_TdExpression_version: Property = Property(name="version", type=StringType)
connection_relational_TdExpression_modificationDate: Property = Property(name="modificationDate", type=StringType)
connection_relational_TdExpression_name: Property = Property(name="name", type=StringType)
connection_relational_TdExpression_expressionVariableMap: Property = Property(name="expressionVariableMap", type=StringType)
connection_relational_TdExpression.attributes={connection_relational_TdExpression_modificationDate, connection_relational_TdExpression_version, connection_relational_TdExpression_name, connection_relational_TdExpression_expressionVariableMap}

# Expression class attributes and methods

# connection_softwaredeployment_TdDataManager class attributes and methods

# DataManager class attributes and methods

# connection_softwaredeployment_TdSoftwareSystem class attributes and methods

# SoftwareSystem class attributes and methods

# connection_softwaredeployment_TdMachine class attributes and methods

# Machine class attributes and methods

# connection_xml_TdXmlElementType class attributes and methods
connection_xml_TdXmlElementType_javaType: Property = Property(name="javaType", type=StringType)
connection_xml_TdXmlElementType_m_setContentType: Method = Method(name="setContentType", parameters={Parameter(name='connection_contentType', type=StringType)})
connection_xml_TdXmlElementType_m_getContentType: Method = Method(name="getContentType", parameters={}, type=StringType)
connection_xml_TdXmlElementType.attributes={connection_xml_TdXmlElementType_javaType}
connection_xml_TdXmlElementType.methods={connection_xml_TdXmlElementType_m_setContentType, connection_xml_TdXmlElementType_m_getContentType}

# ElementType class attributes and methods

# Schema class attributes and methods

# Relationships
connections0: BinaryAssociation = BinaryAssociation(
    name="connections0",
    ends={
        Property(name="connection_Connection", type=connection_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_Metadata", type=connection_Connection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
queries1: BinaryAssociation = BinaryAssociation(
    name="queries1",
    ends={
        Property(name="QueriesConnection", type=connection_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection", type=connection_QueriesConnection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
table2: BinaryAssociation = BinaryAssociation(
    name="table2",
    ends={
        Property(name="connection_MetadataTable", type=connection_MetadataColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_MetadataColumn", type=connection_MetadataTable, multiplicity=Multiplicity(0, 1))
    }
)
columns3: BinaryAssociation = BinaryAssociation(
    name="columns3",
    ends={
        Property(name="connection_MetadataColumn5", type=connection_MetadataTable, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_MetadataTable4", type=connection_MetadataColumn, multiplicity=Multiplicity(0, 9999))
    }
)
connection6: BinaryAssociation = BinaryAssociation(
    name="connection6",
    ends={
        Property(name="connection_Connection8", type=connection_MetadataTable, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_MetadataTable7", type=connection_Connection, multiplicity=Multiplicity(0, 1))
    }
)
additionalProperties9: BinaryAssociation = BinaryAssociation(
    name="additionalProperties9",
    ends={
        Property(name="connection_AdditionalProperties", type=connection_MetadataTable, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_MetadataTable10", type=connection_AdditionalProperties, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schemas11: BinaryAssociation = BinaryAssociation(
    name="schemas11",
    ends={
        Property(name="connection_Concept", type=connection_MDMConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_MDMConnection", type=connection_Concept, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cdcConns12: BinaryAssociation = BinaryAssociation(
    name="cdcConns12",
    ends={
        Property(name="CDCConnection", type=connection_DatabaseConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection13", type=connection_CDCConnection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
InputParameterTable32: BinaryAssociation = BinaryAssociation(
    name="InputParameterTable32",
    ends={
        Property(name="InputSAPFunctionParameterTable", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="functionUnit", type=connection_InputSAPFunctionParameterTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters14: BinaryAssociation = BinaryAssociation(
    name="parameters14",
    ends={
        Property(name="connection_AdditionalProperties15", type=connection_DatabaseConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_DatabaseConnection", type=connection_AdditionalProperties, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Funtions16: BinaryAssociation = BinaryAssociation(
    name="Funtions16",
    ends={
        Property(name="connection_SAPFunctionUnit", type=connection_SAPConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_SAPConnection", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IDocs17: BinaryAssociation = BinaryAssociation(
    name="IDocs17",
    ends={
        Property(name="SAPIDocUnit", type=connection_SAPConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection18", type=connection_SAPIDocUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
additionalProperties19: BinaryAssociation = BinaryAssociation(
    name="additionalProperties19",
    ends={
        Property(name="connection_AdditionalConnectionProperty", type=connection_SAPConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_SAPConnection20", type=connection_AdditionalConnectionProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BWDataSources21: BinaryAssociation = BinaryAssociation(
    name="BWDataSources21",
    ends={
        Property(name="connection_SAPBWTable", type=connection_SAPConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_SAPConnection22", type=connection_SAPBWTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BWDataStoreObjects23: BinaryAssociation = BinaryAssociation(
    name="BWDataStoreObjects23",
    ends={
        Property(name="connection_SAPBWTable25", type=connection_SAPConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_SAPConnection24", type=connection_SAPBWTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BWInfoCubes26: BinaryAssociation = BinaryAssociation(
    name="BWInfoCubes26",
    ends={
        Property(name="connection_SAPBWTable28", type=connection_SAPConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_SAPConnection27", type=connection_SAPBWTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BWInfoObjects29: BinaryAssociation = BinaryAssociation(
    name="BWInfoObjects29",
    ends={
        Property(name="connection_SAPBWTable31", type=connection_SAPConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_SAPConnection30", type=connection_SAPBWTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
OutputParameterTable33: BinaryAssociation = BinaryAssociation(
    name="OutputParameterTable33",
    ends={
        Property(name="OutputSAPFunctionParameterTable", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="functionUnit34", type=connection_OutputSAPFunctionParameterTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
MetadataTable35: BinaryAssociation = BinaryAssociation(
    name="MetadataTable35",
    ends={
        Property(name="connection_MetadataTable37", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_SAPFunctionUnit36", type=connection_MetadataTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connection38: BinaryAssociation = BinaryAssociation(
    name="connection38",
    ends={
        Property(name="connection_SAPConnection40", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_SAPFunctionUnit39", type=connection_SAPConnection, multiplicity=Multiplicity(0, 1))
    }
)
tables41: BinaryAssociation = BinaryAssociation(
    name="tables41",
    ends={
        Property(name="connection_MetadataTable43", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_SAPFunctionUnit42", type=connection_MetadataTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputTables44: BinaryAssociation = BinaryAssociation(
    name="inputTables44",
    ends={
        Property(name="connection_MetadataTable46", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_SAPFunctionUnit45", type=connection_MetadataTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
TestInputParameterTable47: BinaryAssociation = BinaryAssociation(
    name="TestInputParameterTable47",
    ends={
        Property(name="SAPTestInputParameterTable", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="functionUnit48", type=connection_SAPTestInputParameterTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
paramData49: BinaryAssociation = BinaryAssociation(
    name="paramData49",
    ends={
        Property(name="connection_SAPFunctionParamData", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_SAPFunctionUnit50", type=connection_SAPFunctionParamData, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connection51: BinaryAssociation = BinaryAssociation(
    name="connection51",
    ends={
        Property(name="SAPConnection", type=connection_SAPIDocUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="IDocs", type=connection_SAPConnection, multiplicity=Multiplicity(0, 1))
    }
)
loop63: BinaryAssociation = BinaryAssociation(
    name="loop63",
    ends={
        Property(name="connection_XMLFileNode65", type=connection_XmlFileConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_XmlFileConnection64", type=connection_XMLFileNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schema66: BinaryAssociation = BinaryAssociation(
    name="schema66",
    ends={
        Property(name="XmlXPathLoopDescriptor67", type=connection_SchemaTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="schemaTargets", type=connection_XmlXPathLoopDescriptor, multiplicity=Multiplicity(0, 1))
    }
)
ParameterTable52: BinaryAssociation = BinaryAssociation(
    name="ParameterTable52",
    ends={
        Property(name="SAPFunctionParameterTable", type=connection_SAPFunctionParameterColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=connection_SAPFunctionParameterTable, multiplicity=Multiplicity(0, 1))
    }
)
columns53: BinaryAssociation = BinaryAssociation(
    name="columns53",
    ends={
        Property(name="SAPFunctionParameterColumn", type=connection_SAPFunctionParameterTable, multiplicity=Multiplicity(1, 1)),
        Property(name="ParameterTable", type=connection_SAPFunctionParameterColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionUnit54: BinaryAssociation = BinaryAssociation(
    name="functionUnit54",
    ends={
        Property(name="SAPFunctionUnit", type=connection_InputSAPFunctionParameterTable, multiplicity=Multiplicity(1, 1)),
        Property(name="InputParameterTable", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(0, 1))
    }
)
functionUnit55: BinaryAssociation = BinaryAssociation(
    name="functionUnit55",
    ends={
        Property(name="SAPFunctionUnit56", type=connection_OutputSAPFunctionParameterTable, multiplicity=Multiplicity(1, 1)),
        Property(name="OutputParameterTable", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(0, 1))
    }
)
schema57: BinaryAssociation = BinaryAssociation(
    name="schema57",
    ends={
        Property(name="XmlXPathLoopDescriptor", type=connection_XmlFileConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection58", type=connection_XmlXPathLoopDescriptor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group59: BinaryAssociation = BinaryAssociation(
    name="group59",
    ends={
        Property(name="connection_XMLFileNode", type=connection_XmlFileConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_XmlFileConnection", type=connection_XMLFileNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root60: BinaryAssociation = BinaryAssociation(
    name="root60",
    ends={
        Property(name="connection_XMLFileNode62", type=connection_XmlFileConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_XmlFileConnection61", type=connection_XMLFileNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connection73: BinaryAssociation = BinaryAssociation(
    name="connection73",
    ends={
        Property(name="XmlFileConnection", type=connection_XmlXPathLoopDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=connection_XmlFileConnection, multiplicity=Multiplicity(0, 1))
    }
)
schemaTargets74: BinaryAssociation = BinaryAssociation(
    name="schemaTargets74",
    ends={
        Property(name="SchemaTarget", type=connection_XmlXPathLoopDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="schema75", type=connection_SchemaTarget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connection68: BinaryAssociation = BinaryAssociation(
    name="connection68",
    ends={
        Property(name="Connection", type=connection_QueriesConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="queries", type=connection_Connection, multiplicity=Multiplicity(0, 1))
    }
)
query69: BinaryAssociation = BinaryAssociation(
    name="query69",
    ends={
        Property(name="Query", type=connection_QueriesConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="queries70", type=connection_Query, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
queries71: BinaryAssociation = BinaryAssociation(
    name="queries71",
    ends={
        Property(name="QueriesConnection72", type=connection_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="query", type=connection_QueriesConnection, multiplicity=Multiplicity(0, 1))
    }
)
connection82: BinaryAssociation = BinaryAssociation(
    name="connection82",
    ends={
        Property(name="DatabaseConnection", type=connection_CDCConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="cdcConns", type=connection_DatabaseConnection, multiplicity=Multiplicity(0, 1))
    }
)
cdcTypes83: BinaryAssociation = BinaryAssociation(
    name="cdcTypes83",
    ends={
        Property(name="connection_CDCType", type=connection_CDCConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_CDCConnection", type=connection_CDCType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterValue76: BinaryAssociation = BinaryAssociation(
    name="parameterValue76",
    ends={
        Property(name="connection_WSDLParameter", type=connection_WSDLSchemaConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_WSDLSchemaConnection", type=connection_WSDLParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputParameter77: BinaryAssociation = BinaryAssociation(
    name="outputParameter77",
    ends={
        Property(name="connection_WSDLParameter79", type=connection_WSDLSchemaConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_WSDLSchemaConnection78", type=connection_WSDLParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modules80: BinaryAssociation = BinaryAssociation(
    name="modules80",
    ends={
        Property(name="SalesforceModuleUnit", type=connection_SalesforceSchemaConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection81", type=connection_SalesforceModuleUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loop99: BinaryAssociation = BinaryAssociation(
    name="loop99",
    ends={
        Property(name="connection_XMLFileNode101", type=connection_Concept, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_Concept100", type=connection_XMLFileNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schema102: BinaryAssociation = BinaryAssociation(
    name="schema102",
    ends={
        Property(name="Concept", type=connection_ConceptTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="conceptTargets", type=connection_Concept, multiplicity=Multiplicity(0, 1))
    }
)
subscribers84: BinaryAssociation = BinaryAssociation(
    name="subscribers84",
    ends={
        Property(name="connection_SubscriberTable", type=connection_CDCType, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_CDCType85", type=connection_SubscriberTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cdcConnection86: BinaryAssociation = BinaryAssociation(
    name="cdcConnection86",
    ends={
        Property(name="connection_CDCConnection88", type=connection_CDCType, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_CDCType87", type=connection_CDCConnection, multiplicity=Multiplicity(0, 1))
    }
)
functionUnit89: BinaryAssociation = BinaryAssociation(
    name="functionUnit89",
    ends={
        Property(name="SAPFunctionUnit90", type=connection_SAPTestInputParameterTable, multiplicity=Multiplicity(1, 1)),
        Property(name="TestInputParameterTable", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(0, 1))
    }
)
conceptTargets91: BinaryAssociation = BinaryAssociation(
    name="conceptTargets91",
    ends={
        Property(name="ConceptTarget", type=connection_Concept, multiplicity=Multiplicity(1, 1)),
        Property(name="schema92", type=connection_ConceptTarget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group93: BinaryAssociation = BinaryAssociation(
    name="group93",
    ends={
        Property(name="connection_XMLFileNode95", type=connection_Concept, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_Concept94", type=connection_XMLFileNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root96: BinaryAssociation = BinaryAssociation(
    name="root96",
    ends={
        Property(name="connection_XMLFileNode98", type=connection_Concept, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_Concept97", type=connection_XMLFileNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root103: BinaryAssociation = BinaryAssociation(
    name="root103",
    ends={
        Property(name="connection_HL7FileNode", type=connection_HL7Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_HL7Connection", type=connection_HL7FileNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root104: BinaryAssociation = BinaryAssociation(
    name="root104",
    ends={
        Property(name="connection_XMLFileNode105", type=connection_BRMSConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_BRMSConnection", type=connection_XMLFileNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group106: BinaryAssociation = BinaryAssociation(
    name="group106",
    ends={
        Property(name="connection_XMLFileNode108", type=connection_BRMSConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_BRMSConnection107", type=connection_XMLFileNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loop109: BinaryAssociation = BinaryAssociation(
    name="loop109",
    ends={
        Property(name="connection_XMLFileNode111", type=connection_BRMSConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_BRMSConnection110", type=connection_XMLFileNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditions112: BinaryAssociation = BinaryAssociation(
    name="conditions112",
    ends={
        Property(name="connection_ConditionType", type=connection_ValidationRulesConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_ValidationRulesConnection", type=connection_ConditionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
innerJoins113: BinaryAssociation = BinaryAssociation(
    name="innerJoins113",
    ends={
        Property(name="connection_InnerJoinMap", type=connection_ValidationRulesConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_ValidationRulesConnection114", type=connection_InnerJoinMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children122: BinaryAssociation = BinaryAssociation(
    name="children122",
    ends={
        Property(name="connection_SAPFunctionParameter", type=connection_SAPFunctionParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_SAPFunctionParameter121", type=connection_SAPFunctionParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputRoot123: BinaryAssociation = BinaryAssociation(
    name="inputRoot123",
    ends={
        Property(name="connection_SAPFunctionParameter125", type=connection_SAPFunctionParamData, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_SAPFunctionParamData124", type=connection_SAPFunctionParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outputRoot126: BinaryAssociation = BinaryAssociation(
    name="outputRoot126",
    ends={
        Property(name="connection_SAPFunctionParameter128", type=connection_SAPFunctionParamData, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_SAPFunctionParamData127", type=connection_SAPFunctionParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
MetadataTable115: BinaryAssociation = BinaryAssociation(
    name="MetadataTable115",
    ends={
        Property(name="connection_MetadataTable116", type=connection_SalesforceModuleUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_SalesforceModuleUnit", type=connection_MetadataTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connection117: BinaryAssociation = BinaryAssociation(
    name="connection117",
    ends={
        Property(name="SalesforceSchemaConnection", type=connection_SalesforceModuleUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="modules", type=connection_SalesforceSchemaConnection, multiplicity=Multiplicity(0, 1))
    }
)
tables118: BinaryAssociation = BinaryAssociation(
    name="tables118",
    ends={
        Property(name="connection_MetadataTable120", type=connection_SalesforceModuleUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_SalesforceModuleUnit119", type=connection_MetadataTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sqlDataType129: BinaryAssociation = BinaryAssociation(
    name="sqlDataType129",
    ends={
        Property(name="relational_TdSqlDataType", type=connection_relational_TdColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_relational_TdColumn", type=relational_TdSqlDataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xsdElementDeclaration130: BinaryAssociation = BinaryAssociation(
    name="xsdElementDeclaration130",
    ends={
        Property(name="xml_connection_EObject", type=connection_xml_TdXmlElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_xml_TdXmlElementType", type=xml_connection_EObject, multiplicity=Multiplicity(0, 1))
    }
)
ownedDocument131: BinaryAssociation = BinaryAssociation(
    name="ownedDocument131",
    ends={
        Property(name="xml_TdXmlSchema", type=connection_xml_TdXmlElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_xml_TdXmlElementType132", type=xml_TdXmlSchema, multiplicity=Multiplicity(0, 1))
    }
)
xmlContent133: BinaryAssociation = BinaryAssociation(
    name="xmlContent133",
    ends={
        Property(name="xml_TdXmlContent", type=connection_xml_TdXmlElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_xml_TdXmlElementType134", type=xml_TdXmlContent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xmlElements135: BinaryAssociation = BinaryAssociation(
    name="xmlElements135",
    ends={
        Property(name="xml_TdXmlElementType", type=connection_xml_TdXmlContent, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_xml_TdXmlContent", type=xml_TdXmlElementType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_connection_Metadata_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_Metadata)
gen_connection_Connection_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_Connection)
gen_connection_Connection_softwaredeployment_DataProvider = Generalization(general=softwaredeployment_DataProvider, specific=connection_Connection)
gen_connection_MetadataColumn_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_MetadataColumn)
gen_connection_MetadataColumn_record_Field = Generalization(general=record_Field, specific=connection_MetadataColumn)
gen_connection_MetadataTable_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_MetadataTable)
gen_connection_MetadataTable_core_Class = Generalization(general=core_Class, specific=connection_MetadataTable)
gen_connection_AbstractMetadataObject_ModelElement = Generalization(general=ModelElement, specific=connection_AbstractMetadataObject)
gen_connection_DelimitedFileConnection_FileConnection = Generalization(general=FileConnection, specific=connection_DelimitedFileConnection)
gen_connection_PositionalFileConnection_FileConnection = Generalization(general=FileConnection, specific=connection_PositionalFileConnection)
gen_connection_EbcdicConnection_FileConnection = Generalization(general=FileConnection, specific=connection_EbcdicConnection)
gen_connection_FileConnection_Connection = Generalization(general=Connection, specific=connection_FileConnection)
gen_connection_DatabaseConnection_Connection = Generalization(general=Connection, specific=connection_DatabaseConnection)
gen_connection_MDMConnection_Connection = Generalization(general=Connection, specific=connection_MDMConnection)
gen_connection_SAPConnection_Connection = Generalization(general=Connection, specific=connection_SAPConnection)
gen_connection_SAPFunctionUnit_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_SAPFunctionUnit)
gen_connection_SAPFunctionParameterColumn_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_SAPFunctionParameterColumn)
gen_connection_SAPIDocUnit_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_SAPIDocUnit)
gen_connection_SAPFunctionParameterTable_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_SAPFunctionParameterTable)
gen_connection_InputSAPFunctionParameterTable_SAPFunctionParameterTable = Generalization(general=SAPFunctionParameterTable, specific=connection_InputSAPFunctionParameterTable)
gen_connection_OutputSAPFunctionParameterTable_SAPFunctionParameterTable = Generalization(general=SAPFunctionParameterTable, specific=connection_OutputSAPFunctionParameterTable)
gen_connection_RegexpFileConnection_FileConnection = Generalization(general=FileConnection, specific=connection_RegexpFileConnection)
gen_connection_XmlFileConnection_Connection = Generalization(general=Connection, specific=connection_XmlFileConnection)
gen_connection_GenericSchemaConnection_Connection = Generalization(general=Connection, specific=connection_GenericSchemaConnection)
gen_connection_LDAPSchemaConnection_Connection = Generalization(general=Connection, specific=connection_LDAPSchemaConnection)
gen_connection_Query_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_Query)
gen_connection_LdifFileConnection_Connection = Generalization(general=Connection, specific=connection_LdifFileConnection)
gen_connection_FileExcelConnection_FileConnection = Generalization(general=FileConnection, specific=connection_FileExcelConnection)
gen_connection_WSDLSchemaConnection_Connection = Generalization(general=Connection, specific=connection_WSDLSchemaConnection)
gen_connection_SalesforceSchemaConnection_Connection = Generalization(general=Connection, specific=connection_SalesforceSchemaConnection)
gen_connection_HL7Connection_FileConnection = Generalization(general=FileConnection, specific=connection_HL7Connection)
gen_connection_CDCType_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_CDCType)
gen_connection_SubscriberTable_TdTable = Generalization(general=TdTable, specific=connection_SubscriberTable)
gen_connection_SAPTestInputParameterTable_SAPFunctionParameterTable = Generalization(general=SAPFunctionParameterTable, specific=connection_SAPTestInputParameterTable)
gen_connection_Concept_TdTable = Generalization(general=TdTable, specific=connection_Concept)
gen_connection_FTPConnection_Connection = Generalization(general=Connection, specific=connection_FTPConnection)
gen_connection_HeaderFooterConnection_Connection = Generalization(general=Connection, specific=connection_HeaderFooterConnection)
gen_connection_GenericPackage_Package = Generalization(general=Package, specific=connection_GenericPackage)
gen_connection_ValidationRulesConnection_Connection = Generalization(general=Connection, specific=connection_ValidationRulesConnection)
gen_connection_BRMSConnection_Connection = Generalization(general=Connection, specific=connection_BRMSConnection)
gen_connection_EDIFACTConnection_Connection = Generalization(general=Connection, specific=connection_EDIFACTConnection)
gen_connection_EDIFACTColumn_MetadataColumn = Generalization(general=MetadataColumn, specific=connection_EDIFACTColumn)
gen_connection_SalesforceModuleUnit_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_SalesforceModuleUnit)
gen_connection_SAPTable_MetadataTable = Generalization(general=MetadataTable, specific=connection_SAPTable)
gen_connection_SAPTableField_MetadataColumn = Generalization(general=MetadataColumn, specific=connection_SAPTableField)
gen_connection_relational_TdSqlDataType_SQLSimpleType = Generalization(general=SQLSimpleType, specific=connection_relational_TdSqlDataType)
gen_connection_SAPBWTable_SAPTable = Generalization(general=SAPTable, specific=connection_SAPBWTable)
gen_connection_SAPBWTableField_SAPTableField = Generalization(general=SAPTableField, specific=connection_SAPBWTableField)
gen_connection_relational_TdTable_MetadataTable = Generalization(general=MetadataTable, specific=connection_relational_TdTable)
gen_connection_relational_TdTable_relational_Table = Generalization(general=relational_Table, specific=connection_relational_TdTable)
gen_connection_relational_TdView_MetadataTable = Generalization(general=MetadataTable, specific=connection_relational_TdView)
gen_connection_relational_TdView_relational_View = Generalization(general=relational_View, specific=connection_relational_TdView)
gen_connection_relational_TdColumn_MetadataColumn = Generalization(general=MetadataColumn, specific=connection_relational_TdColumn)
gen_connection_xml_TdXmlContent_Content = Generalization(general=Content, specific=connection_xml_TdXmlContent)
gen_connection_relational_TdTrigger_Trigger = Generalization(general=Trigger, specific=connection_relational_TdTrigger)
gen_connection_relational_TdProcedure_Procedure = Generalization(general=Procedure, specific=connection_relational_TdProcedure)
gen_connection_relational_TdExpression_Expression = Generalization(general=Expression, specific=connection_relational_TdExpression)
gen_connection_softwaredeployment_TdDataManager_DataManager = Generalization(general=DataManager, specific=connection_softwaredeployment_TdDataManager)
gen_connection_softwaredeployment_TdSoftwareSystem_SoftwareSystem = Generalization(general=SoftwareSystem, specific=connection_softwaredeployment_TdSoftwareSystem)
gen_connection_softwaredeployment_TdMachine_Machine = Generalization(general=Machine, specific=connection_softwaredeployment_TdMachine)
gen_connection_xml_TdXmlElementType_ElementType = Generalization(general=ElementType, specific=connection_xml_TdXmlElementType)
gen_connection_xml_TdXmlSchema_Schema = Generalization(general=Schema, specific=connection_xml_TdXmlSchema)

# Domain Model
domain_model = DomainModel(
    name="connection",
    types={connection_Metadata, AbstractMetadataObject, connection_Connection, softwaredeployment_DataProvider, connection_QueriesConnection, connection_MetadataColumn, record_Field, core_Class, connection_MetadataTable, connection_AbstractMetadataObject, ModelElement, connection_DelimitedFileConnection, FileConnection, connection_PositionalFileConnection, connection_EbcdicConnection, connection_AdditionalProperties, connection_FileConnection, Connection, connection_DatabaseConnection, connection_MDMConnection, connection_Concept, connection_CDCConnection, connection_InputSAPFunctionParameterTable, connection_OutputSAPFunctionParameterTable, connection_SAPConnection, connection_SAPFunctionUnit, connection_SAPIDocUnit, connection_AdditionalConnectionProperty, connection_SAPBWTable, connection_SAPFunctionParameterColumn, connection_SAPFunctionParameterTable, connection_SAPTestInputParameterTable, connection_SAPFunctionParamData, connection_SchemaTarget, SAPFunctionParameterTable, connection_RegexpFileConnection, connection_XmlFileConnection, connection_XmlXPathLoopDescriptor, connection_XMLFileNode, connection_GenericSchemaConnection, connection_LDAPSchemaConnection, connection_Query, connection_LdifFileConnection, connection_FileExcelConnection, connection_WSDLSchemaConnection, connection_CDCType, connection_WSDLParameter, connection_SalesforceSchemaConnection, connection_SalesforceModuleUnit, connection_HL7Connection, connection_HL7FileNode, connection_SubscriberTable, TdTable, connection_ConceptTarget, connection_FTPConnection, connection_HeaderFooterConnection, connection_GenericPackage, Package, connection_ValidationRulesConnection, connection_BRMSConnection, connection_EDIFACTConnection, connection_EDIFACTColumn, MetadataColumn, connection_ConditionType, connection_InnerJoinMap, connection_SAPTable, MetadataTable, connection_SAPTableField, connection_SAPFunctionParameter, connection_relational_TdSqlDataType, SQLSimpleType, SAPTable, connection_SAPBWTableField, SAPTableField, connection_relational_TdTable, relational_Table, connection_relational_TdView, relational_View, connection_relational_TdColumn, relational_TdSqlDataType, xml_connection_EObject, xml_TdXmlSchema, xml_TdXmlContent, connection_xml_TdXmlContent, Content, xml_TdXmlElementType, connection_xml_TdXmlSchema, connection_relational_TdTrigger, Trigger, connection_relational_TdProcedure, Procedure, connection_relational_TdExpression, Expression, connection_softwaredeployment_TdDataManager, DataManager, connection_softwaredeployment_TdSoftwareSystem, SoftwareSystem, connection_softwaredeployment_TdMachine, Machine, connection_xml_TdXmlElementType, ElementType, Schema, Escape, RowSeparator, FileFormat, FieldSeparator, MDMConnectionProtocol, MdmConceptType, LogicalOperator, RuleType, Function, Operator, DevelopmentStatus},
    associations={connections0, queries1, table2, columns3, connection6, additionalProperties9, schemas11, cdcConns12, InputParameterTable32, parameters14, Funtions16, IDocs17, additionalProperties19, BWDataSources21, BWDataStoreObjects23, BWInfoCubes26, BWInfoObjects29, OutputParameterTable33, MetadataTable35, connection38, tables41, inputTables44, TestInputParameterTable47, paramData49, connection51, loop63, schema66, ParameterTable52, columns53, functionUnit54, functionUnit55, schema57, group59, root60, connection73, schemaTargets74, connection68, query69, queries71, connection82, cdcTypes83, parameterValue76, outputParameter77, modules80, loop99, schema102, subscribers84, cdcConnection86, functionUnit89, conceptTargets91, group93, root96, root103, root104, group106, loop109, conditions112, innerJoins113, children122, inputRoot123, outputRoot126, MetadataTable115, connection117, tables118, sqlDataType129, xsdElementDeclaration130, ownedDocument131, xmlContent133, xmlElements135},
    generalizations={gen_connection_Metadata_AbstractMetadataObject, gen_connection_Connection_AbstractMetadataObject, gen_connection_Connection_softwaredeployment_DataProvider, gen_connection_MetadataColumn_AbstractMetadataObject, gen_connection_MetadataColumn_record_Field, gen_connection_MetadataTable_AbstractMetadataObject, gen_connection_MetadataTable_core_Class, gen_connection_AbstractMetadataObject_ModelElement, gen_connection_DelimitedFileConnection_FileConnection, gen_connection_PositionalFileConnection_FileConnection, gen_connection_EbcdicConnection_FileConnection, gen_connection_FileConnection_Connection, gen_connection_DatabaseConnection_Connection, gen_connection_MDMConnection_Connection, gen_connection_SAPConnection_Connection, gen_connection_SAPFunctionUnit_AbstractMetadataObject, gen_connection_SAPFunctionParameterColumn_AbstractMetadataObject, gen_connection_SAPIDocUnit_AbstractMetadataObject, gen_connection_SAPFunctionParameterTable_AbstractMetadataObject, gen_connection_InputSAPFunctionParameterTable_SAPFunctionParameterTable, gen_connection_OutputSAPFunctionParameterTable_SAPFunctionParameterTable, gen_connection_RegexpFileConnection_FileConnection, gen_connection_XmlFileConnection_Connection, gen_connection_GenericSchemaConnection_Connection, gen_connection_LDAPSchemaConnection_Connection, gen_connection_Query_AbstractMetadataObject, gen_connection_LdifFileConnection_Connection, gen_connection_FileExcelConnection_FileConnection, gen_connection_WSDLSchemaConnection_Connection, gen_connection_SalesforceSchemaConnection_Connection, gen_connection_HL7Connection_FileConnection, gen_connection_CDCType_AbstractMetadataObject, gen_connection_SubscriberTable_TdTable, gen_connection_SAPTestInputParameterTable_SAPFunctionParameterTable, gen_connection_Concept_TdTable, gen_connection_FTPConnection_Connection, gen_connection_HeaderFooterConnection_Connection, gen_connection_GenericPackage_Package, gen_connection_ValidationRulesConnection_Connection, gen_connection_BRMSConnection_Connection, gen_connection_EDIFACTConnection_Connection, gen_connection_EDIFACTColumn_MetadataColumn, gen_connection_SalesforceModuleUnit_AbstractMetadataObject, gen_connection_SAPTable_MetadataTable, gen_connection_SAPTableField_MetadataColumn, gen_connection_relational_TdSqlDataType_SQLSimpleType, gen_connection_SAPBWTable_SAPTable, gen_connection_SAPBWTableField_SAPTableField, gen_connection_relational_TdTable_MetadataTable, gen_connection_relational_TdTable_relational_Table, gen_connection_relational_TdView_MetadataTable, gen_connection_relational_TdView_relational_View, gen_connection_relational_TdColumn_MetadataColumn, gen_connection_xml_TdXmlContent_Content, gen_connection_relational_TdTrigger_Trigger, gen_connection_relational_TdProcedure_Procedure, gen_connection_relational_TdExpression_Expression, gen_connection_softwaredeployment_TdDataManager_DataManager, gen_connection_softwaredeployment_TdSoftwareSystem_SoftwareSystem, gen_connection_softwaredeployment_TdMachine_Machine, gen_connection_xml_TdXmlElementType_ElementType, gen_connection_xml_TdXmlSchema_Schema},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)