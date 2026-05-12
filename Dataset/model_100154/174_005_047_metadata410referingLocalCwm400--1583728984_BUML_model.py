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

MDMConnectionProtocol: Enumeration = Enumeration(
    name="MDMConnectionProtocol",
    literals={
            EnumerationLiteral(name="HTTP")
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
connection_MetadataTable = Class(name="connection_MetadataTable")
connection_AbstractMetadataObject = Class(name="connection_AbstractMetadataObject", is_abstract=True)
ModelElement = Class(name="ModelElement")
core_Class = Class(name="core_Class")
connection_DelimitedFileConnection = Class(name="connection_DelimitedFileConnection")
FileConnection = Class(name="FileConnection")
connection_PositionalFileConnection = Class(name="connection_PositionalFileConnection")
connection_EbcdicConnection = Class(name="connection_EbcdicConnection")
connection_MDMConnection = Class(name="connection_MDMConnection")
connection_Concept = Class(name="connection_Concept")
connection_FileConnection = Class(name="connection_FileConnection", is_abstract=True)
Connection = Class(name="Connection")
connection_DatabaseConnection = Class(name="connection_DatabaseConnection")
connection_CDCConnection = Class(name="connection_CDCConnection")
connection_SAPConnection = Class(name="connection_SAPConnection")
connection_SAPFunctionUnit = Class(name="connection_SAPFunctionUnit")
connection_SAPIDocUnit = Class(name="connection_SAPIDocUnit")
connection_InputSAPFunctionParameterTable = Class(name="connection_InputSAPFunctionParameterTable")
connection_OutputSAPFunctionParameterTable = Class(name="connection_OutputSAPFunctionParameterTable")
connection_SAPTestInputParameterTable = Class(name="connection_SAPTestInputParameterTable")
connection_SAPFunctionParameterColumn = Class(name="connection_SAPFunctionParameterColumn")
connection_SAPFunctionParameterTable = Class(name="connection_SAPFunctionParameterTable")
SAPFunctionParameterTable = Class(name="SAPFunctionParameterTable")
connection_RegexpFileConnection = Class(name="connection_RegexpFileConnection")
connection_XmlFileConnection = Class(name="connection_XmlFileConnection")
connection_XmlXPathLoopDescriptor = Class(name="connection_XmlXPathLoopDescriptor")
connection_XMLFileNode = Class(name="connection_XMLFileNode")
connection_SchemaTarget = Class(name="connection_SchemaTarget")
connection_Query = Class(name="connection_Query")
connection_LdifFileConnection = Class(name="connection_LdifFileConnection")
connection_FileExcelConnection = Class(name="connection_FileExcelConnection")
connection_LDAPSchemaConnection = Class(name="connection_LDAPSchemaConnection")
connection_WSDLSchemaConnection = Class(name="connection_WSDLSchemaConnection")
connection_GenericSchemaConnection = Class(name="connection_GenericSchemaConnection")
connection_WSDLParameter = Class(name="connection_WSDLParameter")
connection_SalesforceSchemaConnection = Class(name="connection_SalesforceSchemaConnection")
connection_CDCType = Class(name="connection_CDCType")
TdTable = Class(name="TdTable")
connection_ConceptTarget = Class(name="connection_ConceptTarget")
connection_HL7Connection = Class(name="connection_HL7Connection")
connection_HL7FileNode = Class(name="connection_HL7FileNode")
connection_HeaderFooterConnection = Class(name="connection_HeaderFooterConnection")
connection_SubscriberTable = Class(name="connection_SubscriberTable")
connection_GenericPackage = Class(name="connection_GenericPackage")
Package = Class(name="Package")
connection_FTPConnection = Class(name="connection_FTPConnection")
Machine = Class(name="Machine")
connection_relational_TdTable = Class(name="connection_relational_TdTable")
MetadataTable = Class(name="MetadataTable")
relational_Table = Class(name="relational_Table")
connection_relational_TdView = Class(name="connection_relational_TdView")
connection_xml_TdXmlElementType = Class(name="connection_xml_TdXmlElementType")
relational_View = Class(name="relational_View")
ElementType = Class(name="ElementType")
connection_relational_TdColumn = Class(name="connection_relational_TdColumn")
MetadataColumn = Class(name="MetadataColumn")
xml_connection_EObject = Class(name="xml_connection_EObject")
xml_TdXmlSchema = Class(name="xml_TdXmlSchema")
relational_TdSqlDataType = Class(name="relational_TdSqlDataType")
connection_relational_TdSqlDataType = Class(name="connection_relational_TdSqlDataType")
SQLSimpleType = Class(name="SQLSimpleType")
connection_relational_TdTrigger = Class(name="connection_relational_TdTrigger")
Trigger = Class(name="Trigger")
connection_relational_TdProcedure = Class(name="connection_relational_TdProcedure")
Procedure = Class(name="Procedure")
connection_softwaredeployment_TdDataManager = Class(name="connection_softwaredeployment_TdDataManager")
DataManager = Class(name="DataManager")
connection_softwaredeployment_TdSoftwareSystem = Class(name="connection_softwaredeployment_TdSoftwareSystem")
SoftwareSystem = Class(name="SoftwareSystem")
connection_softwaredeployment_TdMachine = Class(name="connection_softwaredeployment_TdMachine")
xml_TdXmlContent = Class(name="xml_TdXmlContent")
connection_xml_TdXmlContent = Class(name="connection_xml_TdXmlContent")
Content = Class(name="Content")
xml_TdXmlElementType = Class(name="xml_TdXmlElementType")
connection_xml_TdXmlSchema = Class(name="connection_xml_TdXmlSchema")
Schema = Class(name="Schema")

# connection_Metadata class attributes and methods

# AbstractMetadataObject class attributes and methods

# connection_Connection class attributes and methods
connection_Connection_version: Property = Property(name="version", type=StringType)
connection_Connection_ContextMode: Property = Property(name="ContextMode", type=BooleanType)
connection_Connection_ContextId: Property = Property(name="ContextId", type=StringType)
connection_Connection.attributes={connection_Connection_ContextId, connection_Connection_ContextMode, connection_Connection_version}

# softwaredeployment_DataProvider class attributes and methods

# connection_QueriesConnection class attributes and methods

# connection_MetadataColumn class attributes and methods
connection_MetadataColumn_sourceType: Property = Property(name="sourceType", type=StringType)
connection_MetadataColumn_defaultValue: Property = Property(name="defaultValue", type=StringType)
connection_MetadataColumn_talendType: Property = Property(name="talendType", type=StringType)
connection_MetadataColumn_key: Property = Property(name="key", type=BooleanType)
connection_MetadataColumn_nullable: Property = Property(name="nullable", type=BooleanType)
connection_MetadataColumn_displayField: Property = Property(name="displayField", type=StringType)
connection_MetadataColumn_originalField: Property = Property(name="originalField", type=StringType)
connection_MetadataColumn_pattern: Property = Property(name="pattern", type=StringType)
connection_MetadataColumn.attributes={connection_MetadataColumn_key, connection_MetadataColumn_displayField, connection_MetadataColumn_nullable, connection_MetadataColumn_talendType, connection_MetadataColumn_pattern, connection_MetadataColumn_defaultValue, connection_MetadataColumn_originalField, connection_MetadataColumn_sourceType}

# record_Field class attributes and methods

# connection_MetadataTable class attributes and methods
connection_MetadataTable_sourceName: Property = Property(name="sourceName", type=StringType)
connection_MetadataTable_tableType: Property = Property(name="tableType", type=StringType)
connection_MetadataTable_attachedCDC: Property = Property(name="attachedCDC", type=BooleanType)
connection_MetadataTable_activatedCDC: Property = Property(name="activatedCDC", type=BooleanType)
connection_MetadataTable.attributes={connection_MetadataTable_tableType, connection_MetadataTable_attachedCDC, connection_MetadataTable_sourceName, connection_MetadataTable_activatedCDC}

# connection_AbstractMetadataObject class attributes and methods
connection_AbstractMetadataObject_properties: Property = Property(name="properties", type=StringType)
connection_AbstractMetadataObject_id: Property = Property(name="id", type=StringType)
connection_AbstractMetadataObject_comment: Property = Property(name="comment", type=StringType)
connection_AbstractMetadataObject_label: Property = Property(name="label", type=StringType)
connection_AbstractMetadataObject_readOnly: Property = Property(name="readOnly", type=BooleanType)
connection_AbstractMetadataObject_synchronised: Property = Property(name="synchronised", type=BooleanType)
connection_AbstractMetadataObject_divergency: Property = Property(name="divergency", type=BooleanType)
connection_AbstractMetadataObject.attributes={connection_AbstractMetadataObject_id, connection_AbstractMetadataObject_synchronised, connection_AbstractMetadataObject_divergency, connection_AbstractMetadataObject_readOnly, connection_AbstractMetadataObject_label, connection_AbstractMetadataObject_properties, connection_AbstractMetadataObject_comment}

# ModelElement class attributes and methods

# core_Class class attributes and methods

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
connection_MDMConnection_context: Property = Property(name="context", type=StringType)
connection_MDMConnection_protocol: Property = Property(name="protocol", type=StringType)
connection_MDMConnection_m_getConnectionString: Method = Method(name="getConnectionString", parameters={}, type=StringType)
connection_MDMConnection.attributes={connection_MDMConnection_Server, connection_MDMConnection_Port, connection_MDMConnection_Universe, connection_MDMConnection_Username, connection_MDMConnection_protocol, connection_MDMConnection_context, connection_MDMConnection_Password, connection_MDMConnection_Datacluster, connection_MDMConnection_Datamodel}
connection_MDMConnection.methods={connection_MDMConnection_m_getConnectionString}

# connection_Concept class attributes and methods
connection_Concept_LoopExpression: Property = Property(name="LoopExpression", type=StringType)
connection_Concept_LoopLimit: Property = Property(name="LoopLimit", type=StringType)
connection_Concept_inputModel: Property = Property(name="inputModel", type=BooleanType)
connection_Concept.attributes={connection_Concept_LoopExpression, connection_Concept_LoopLimit, connection_Concept_inputModel}

# connection_FileConnection class attributes and methods
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
connection_FileConnection_Server: Property = Property(name="Server", type=StringType)
connection_FileConnection.attributes={connection_FileConnection_FilePath, connection_FileConnection_EscapeChar, connection_FileConnection_RowSeparatorType, connection_FileConnection_FirstLineCaption, connection_FileConnection_RowSeparatorValue, connection_FileConnection_FieldSeparatorValue, connection_FileConnection_UseLimit, connection_FileConnection_FooterValue, connection_FileConnection_TextIdentifier, connection_FileConnection_EscapeType, connection_FileConnection_TextEnclosure, connection_FileConnection_HeaderValue, connection_FileConnection_UseFooter, connection_FileConnection_RemoveEmptyRow, connection_FileConnection_Format, connection_FileConnection_LimitValue, connection_FileConnection_CsvOption, connection_FileConnection_Server, connection_FileConnection_Encoding, connection_FileConnection_UseHeader}

# Connection class attributes and methods

# connection_DatabaseConnection class attributes and methods
connection_DatabaseConnection_DatabaseType: Property = Property(name="DatabaseType", type=StringType)
connection_DatabaseConnection_DriverJarPath: Property = Property(name="DriverJarPath", type=StringType)
connection_DatabaseConnection_DriverClass: Property = Property(name="DriverClass", type=StringType)
connection_DatabaseConnection_URL: Property = Property(name="URL", type=StringType)
connection_DatabaseConnection_dbVersionString: Property = Property(name="dbVersionString", type=StringType)
connection_DatabaseConnection_Port: Property = Property(name="Port", type=StringType)
connection_DatabaseConnection_Username: Property = Property(name="Username", type=StringType)
connection_DatabaseConnection_Password: Property = Property(name="Password", type=StringType)
connection_DatabaseConnection_FileFieldName: Property = Property(name="FileFieldName", type=StringType)
connection_DatabaseConnection_SID: Property = Property(name="SID", type=StringType)
connection_DatabaseConnection_SqlSynthax: Property = Property(name="SqlSynthax", type=StringType)
connection_DatabaseConnection_StringQuote: Property = Property(name="StringQuote", type=StringType)
connection_DatabaseConnection_NullChar: Property = Property(name="NullChar", type=StringType)
connection_DatabaseConnection_DbmsId: Property = Property(name="DbmsId", type=StringType)
connection_DatabaseConnection_ProductId: Property = Property(name="ProductId", type=StringType)
connection_DatabaseConnection_DBRootPath: Property = Property(name="DBRootPath", type=StringType)
connection_DatabaseConnection_AdditionalParams: Property = Property(name="AdditionalParams", type=StringType)
connection_DatabaseConnection_StandardSQL: Property = Property(name="StandardSQL", type=BooleanType)
connection_DatabaseConnection_SystemSQL: Property = Property(name="SystemSQL", type=BooleanType)
connection_DatabaseConnection_cdcTypeMode: Property = Property(name="cdcTypeMode", type=StringType)
connection_DatabaseConnection_SQLMode: Property = Property(name="SQLMode", type=BooleanType)
connection_DatabaseConnection_UiSchema: Property = Property(name="UiSchema", type=StringType)
connection_DatabaseConnection_ServerName: Property = Property(name="ServerName", type=StringType)
connection_DatabaseConnection_DatasourceName: Property = Property(name="DatasourceName", type=StringType)
connection_DatabaseConnection.attributes={connection_DatabaseConnection_ServerName, connection_DatabaseConnection_NullChar, connection_DatabaseConnection_dbVersionString, connection_DatabaseConnection_DatabaseType, connection_DatabaseConnection_StringQuote, connection_DatabaseConnection_cdcTypeMode, connection_DatabaseConnection_DriverClass, connection_DatabaseConnection_DatasourceName, connection_DatabaseConnection_StandardSQL, connection_DatabaseConnection_Username, connection_DatabaseConnection_Port, connection_DatabaseConnection_SqlSynthax, connection_DatabaseConnection_Password, connection_DatabaseConnection_DBRootPath, connection_DatabaseConnection_DriverJarPath, connection_DatabaseConnection_SQLMode, connection_DatabaseConnection_AdditionalParams, connection_DatabaseConnection_FileFieldName, connection_DatabaseConnection_URL, connection_DatabaseConnection_ProductId, connection_DatabaseConnection_UiSchema, connection_DatabaseConnection_DbmsId, connection_DatabaseConnection_SID, connection_DatabaseConnection_SystemSQL}

# connection_CDCConnection class attributes and methods

# connection_SAPConnection class attributes and methods
connection_SAPConnection_Host: Property = Property(name="Host", type=StringType)
connection_SAPConnection_Username: Property = Property(name="Username", type=StringType)
connection_SAPConnection_Password: Property = Property(name="Password", type=StringType)
connection_SAPConnection_Client: Property = Property(name="Client", type=StringType)
connection_SAPConnection_SystemNumber: Property = Property(name="SystemNumber", type=StringType)
connection_SAPConnection_Language: Property = Property(name="Language", type=StringType)
connection_SAPConnection_currentFucntion: Property = Property(name="currentFucntion", type=StringType)
connection_SAPConnection.attributes={connection_SAPConnection_Client, connection_SAPConnection_currentFucntion, connection_SAPConnection_Username, connection_SAPConnection_SystemNumber, connection_SAPConnection_Language, connection_SAPConnection_Password, connection_SAPConnection_Host}

# connection_SAPFunctionUnit class attributes and methods
connection_SAPFunctionUnit_OutputTableName: Property = Property(name="OutputTableName", type=StringType)
connection_SAPFunctionUnit_OutputType: Property = Property(name="OutputType", type=StringType)
connection_SAPFunctionUnit_m_setDocument: Method = Method(name="setDocument", parameters={Parameter(name='connection_document', type=StringType)})
connection_SAPFunctionUnit.attributes={connection_SAPFunctionUnit_OutputTableName, connection_SAPFunctionUnit_OutputType}
connection_SAPFunctionUnit.methods={connection_SAPFunctionUnit_m_setDocument}

# connection_SAPIDocUnit class attributes and methods
connection_SAPIDocUnit_programId: Property = Property(name="programId", type=StringType)
connection_SAPIDocUnit_gatewayService: Property = Property(name="gatewayService", type=StringType)
connection_SAPIDocUnit_useXmlOutput: Property = Property(name="useXmlOutput", type=BooleanType)
connection_SAPIDocUnit_xmlFile: Property = Property(name="xmlFile", type=StringType)
connection_SAPIDocUnit_useHtmlOutput: Property = Property(name="useHtmlOutput", type=BooleanType)
connection_SAPIDocUnit_htmlFile: Property = Property(name="htmlFile", type=StringType)
connection_SAPIDocUnit.attributes={connection_SAPIDocUnit_programId, connection_SAPIDocUnit_htmlFile, connection_SAPIDocUnit_xmlFile, connection_SAPIDocUnit_useHtmlOutput, connection_SAPIDocUnit_useXmlOutput, connection_SAPIDocUnit_gatewayService}

# connection_InputSAPFunctionParameterTable class attributes and methods

# connection_OutputSAPFunctionParameterTable class attributes and methods

# connection_SAPTestInputParameterTable class attributes and methods

# connection_SAPFunctionParameterColumn class attributes and methods
connection_SAPFunctionParameterColumn_ParameterType: Property = Property(name="ParameterType", type=StringType)
connection_SAPFunctionParameterColumn_StructureOrTableName: Property = Property(name="StructureOrTableName", type=StringType)
connection_SAPFunctionParameterColumn_DataType: Property = Property(name="DataType", type=StringType)
connection_SAPFunctionParameterColumn_Length: Property = Property(name="Length", type=StringType)
connection_SAPFunctionParameterColumn_Value: Property = Property(name="Value", type=StringType)
connection_SAPFunctionParameterColumn_m_setDescription: Method = Method(name="setDescription", parameters={Parameter(name='connection_description', type=StringType)})
connection_SAPFunctionParameterColumn.attributes={connection_SAPFunctionParameterColumn_DataType, connection_SAPFunctionParameterColumn_Value, connection_SAPFunctionParameterColumn_Length, connection_SAPFunctionParameterColumn_StructureOrTableName, connection_SAPFunctionParameterColumn_ParameterType}
connection_SAPFunctionParameterColumn.methods={connection_SAPFunctionParameterColumn_m_setDescription}

# connection_SAPFunctionParameterTable class attributes and methods

# SAPFunctionParameterTable class attributes and methods

# connection_RegexpFileConnection class attributes and methods
connection_RegexpFileConnection_FieldSeparatorType: Property = Property(name="FieldSeparatorType", type=StringType)
connection_RegexpFileConnection.attributes={connection_RegexpFileConnection_FieldSeparatorType}

# connection_XmlFileConnection class attributes and methods
connection_XmlFileConnection_XsdFilePath: Property = Property(name="XsdFilePath", type=StringType)
connection_XmlFileConnection_XmlFilePath: Property = Property(name="XmlFilePath", type=StringType)
connection_XmlFileConnection_Guess: Property = Property(name="Guess", type=BooleanType)
connection_XmlFileConnection_MaskXPattern: Property = Property(name="MaskXPattern", type=StringType)
connection_XmlFileConnection_Encoding: Property = Property(name="Encoding", type=StringType)
connection_XmlFileConnection_inputModel: Property = Property(name="inputModel", type=BooleanType)
connection_XmlFileConnection_outputFilePath: Property = Property(name="outputFilePath", type=StringType)
connection_XmlFileConnection.attributes={connection_XmlFileConnection_Encoding, connection_XmlFileConnection_XmlFilePath, connection_XmlFileConnection_inputModel, connection_XmlFileConnection_outputFilePath, connection_XmlFileConnection_Guess, connection_XmlFileConnection_MaskXPattern, connection_XmlFileConnection_XsdFilePath}

# connection_XmlXPathLoopDescriptor class attributes and methods
connection_XmlXPathLoopDescriptor_LimitBoucle: Property = Property(name="LimitBoucle", type=StringType)
connection_XmlXPathLoopDescriptor_AbsoluteXPathQuery: Property = Property(name="AbsoluteXPathQuery", type=StringType)
connection_XmlXPathLoopDescriptor.attributes={connection_XmlXPathLoopDescriptor_AbsoluteXPathQuery, connection_XmlXPathLoopDescriptor_LimitBoucle}

# connection_XMLFileNode class attributes and methods
connection_XMLFileNode_XMLPath: Property = Property(name="XMLPath", type=StringType)
connection_XMLFileNode_RelatedColumn: Property = Property(name="RelatedColumn", type=StringType)
connection_XMLFileNode_DefaultValue: Property = Property(name="DefaultValue", type=StringType)
connection_XMLFileNode_Attribute: Property = Property(name="Attribute", type=StringType)
connection_XMLFileNode_Order: Property = Property(name="Order", type=IntegerType)
connection_XMLFileNode_Type: Property = Property(name="Type", type=StringType)
connection_XMLFileNode.attributes={connection_XMLFileNode_Type, connection_XMLFileNode_Order, connection_XMLFileNode_Attribute, connection_XMLFileNode_DefaultValue, connection_XMLFileNode_RelatedColumn, connection_XMLFileNode_XMLPath}

# connection_SchemaTarget class attributes and methods
connection_SchemaTarget_RelativeXPathQuery: Property = Property(name="RelativeXPathQuery", type=StringType)
connection_SchemaTarget_TagName: Property = Property(name="TagName", type=StringType)
connection_SchemaTarget.attributes={connection_SchemaTarget_RelativeXPathQuery, connection_SchemaTarget_TagName}

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
connection_LdifFileConnection.attributes={connection_LdifFileConnection_UseLimit, connection_LdifFileConnection_FilePath, connection_LdifFileConnection_value, connection_LdifFileConnection_Server, connection_LdifFileConnection_LimitEntry}

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
connection_FileExcelConnection.attributes={connection_FileExcelConnection_sheetColumns, connection_FileExcelConnection_advancedSpearator, connection_FileExcelConnection_SheetName, connection_FileExcelConnection_decimalSeparator, connection_FileExcelConnection_firstColumn, connection_FileExcelConnection_thousandSeparator, connection_FileExcelConnection_sheetList, connection_FileExcelConnection_selectAllSheets, connection_FileExcelConnection_lastColumn}

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
connection_LDAPSchemaConnection.attributes={connection_LDAPSchemaConnection_Port, connection_LDAPSchemaConnection_CountLimit, connection_LDAPSchemaConnection_Separator, connection_LDAPSchemaConnection_Host, connection_LDAPSchemaConnection_TimeOutLimit, connection_LDAPSchemaConnection_Aliases, connection_LDAPSchemaConnection_Protocol, connection_LDAPSchemaConnection_LimitValue, connection_LDAPSchemaConnection_Filter, connection_LDAPSchemaConnection_Referrals, connection_LDAPSchemaConnection_EncryptionMethodName, connection_LDAPSchemaConnection_Value, connection_LDAPSchemaConnection_UseLimit, connection_LDAPSchemaConnection_GetBaseDNsFromRoot, connection_LDAPSchemaConnection_StorePath, connection_LDAPSchemaConnection_SelectedDN, connection_LDAPSchemaConnection_BindPrincipal, connection_LDAPSchemaConnection_BaseDNs, connection_LDAPSchemaConnection_BindPassword, connection_LDAPSchemaConnection_SavePassword, connection_LDAPSchemaConnection_UseAdvanced, connection_LDAPSchemaConnection_ReturnAttributes, connection_LDAPSchemaConnection_UseAuthen}

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
connection_WSDLSchemaConnection_Encoding: Property = Property(name="Encoding", type=StringType)
connection_WSDLSchemaConnection_timeOut: Property = Property(name="timeOut", type=IntegerType)
connection_WSDLSchemaConnection_isInputModel: Property = Property(name="isInputModel", type=BooleanType)
connection_WSDLSchemaConnection_serverNameSpace: Property = Property(name="serverNameSpace", type=StringType)
connection_WSDLSchemaConnection_serverName: Property = Property(name="serverName", type=StringType)
connection_WSDLSchemaConnection_portNameSpace: Property = Property(name="portNameSpace", type=StringType)
connection_WSDLSchemaConnection_portName: Property = Property(name="portName", type=StringType)
connection_WSDLSchemaConnection_proxyPassword: Property = Property(name="proxyPassword", type=StringType)
connection_WSDLSchemaConnection_Value: Property = Property(name="Value", type=StringType)
connection_WSDLSchemaConnection_EndpointURI: Property = Property(name="EndpointURI", type=StringType)
connection_WSDLSchemaConnection.attributes={connection_WSDLSchemaConnection_proxyUser, connection_WSDLSchemaConnection_proxyPassword, connection_WSDLSchemaConnection_Password, connection_WSDLSchemaConnection_WSDL, connection_WSDLSchemaConnection_parameters, connection_WSDLSchemaConnection_UserName, connection_WSDLSchemaConnection_isInputModel, connection_WSDLSchemaConnection_portNameSpace, connection_WSDLSchemaConnection_needAuth, connection_WSDLSchemaConnection_EndpointURI, connection_WSDLSchemaConnection_useProxy, connection_WSDLSchemaConnection_Value, connection_WSDLSchemaConnection_proxyPort, connection_WSDLSchemaConnection_proxyHost, connection_WSDLSchemaConnection_serverName, connection_WSDLSchemaConnection_serverNameSpace, connection_WSDLSchemaConnection_methodName, connection_WSDLSchemaConnection_Encoding, connection_WSDLSchemaConnection_timeOut, connection_WSDLSchemaConnection_portName}

# connection_GenericSchemaConnection class attributes and methods
connection_GenericSchemaConnection_mappingTypeId: Property = Property(name="mappingTypeId", type=StringType)
connection_GenericSchemaConnection_mappingTypeUsed: Property = Property(name="mappingTypeUsed", type=BooleanType)
connection_GenericSchemaConnection.attributes={connection_GenericSchemaConnection_mappingTypeId, connection_GenericSchemaConnection_mappingTypeUsed}

# connection_WSDLParameter class attributes and methods
connection_WSDLParameter_Element: Property = Property(name="Element", type=StringType)
connection_WSDLParameter_source: Property = Property(name="source", type=StringType)
connection_WSDLParameter_Column: Property = Property(name="Column", type=StringType)
connection_WSDLParameter_Expression: Property = Property(name="Expression", type=StringType)
connection_WSDLParameter_ParameterInfo: Property = Property(name="ParameterInfo", type=StringType)
connection_WSDLParameter_ParameterInfoParent: Property = Property(name="ParameterInfoParent", type=StringType)
connection_WSDLParameter.attributes={connection_WSDLParameter_Expression, connection_WSDLParameter_Element, connection_WSDLParameter_Column, connection_WSDLParameter_ParameterInfo, connection_WSDLParameter_source, connection_WSDLParameter_ParameterInfoParent}

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
connection_SalesforceSchemaConnection.attributes={connection_SalesforceSchemaConnection_useCustomModuleName, connection_SalesforceSchemaConnection_timeOut, connection_SalesforceSchemaConnection_proxyUsername, connection_SalesforceSchemaConnection_proxyPassword, connection_SalesforceSchemaConnection_batchSize, connection_SalesforceSchemaConnection_webServiceUrl, connection_SalesforceSchemaConnection_useProxy, connection_SalesforceSchemaConnection_useAlphbet, connection_SalesforceSchemaConnection_password, connection_SalesforceSchemaConnection_moduleName, connection_SalesforceSchemaConnection_queryCondition, connection_SalesforceSchemaConnection_proxyPort, connection_SalesforceSchemaConnection_proxyHost, connection_SalesforceSchemaConnection_useHttpProxy, connection_SalesforceSchemaConnection_userName}

# connection_CDCType class attributes and methods
connection_CDCType_linkDB: Property = Property(name="linkDB", type=StringType)
connection_CDCType_journalName: Property = Property(name="journalName", type=StringType)
connection_CDCType.attributes={connection_CDCType_journalName, connection_CDCType_linkDB}

# TdTable class attributes and methods

# connection_ConceptTarget class attributes and methods
connection_ConceptTarget_targetName: Property = Property(name="targetName", type=StringType)
connection_ConceptTarget_RelativeLoopExpression: Property = Property(name="RelativeLoopExpression", type=StringType)
connection_ConceptTarget.attributes={connection_ConceptTarget_targetName, connection_ConceptTarget_RelativeLoopExpression}

# connection_HL7Connection class attributes and methods
connection_HL7Connection_StartChar: Property = Property(name="StartChar", type=StringType)
connection_HL7Connection_EndChar: Property = Property(name="EndChar", type=StringType)
connection_HL7Connection_outputFilePath: Property = Property(name="outputFilePath", type=StringType)
connection_HL7Connection.attributes={connection_HL7Connection_EndChar, connection_HL7Connection_outputFilePath, connection_HL7Connection_StartChar}

# connection_HL7FileNode class attributes and methods
connection_HL7FileNode_FilePath: Property = Property(name="FilePath", type=StringType)
connection_HL7FileNode_Order: Property = Property(name="Order", type=IntegerType)
connection_HL7FileNode_Attribute: Property = Property(name="Attribute", type=StringType)
connection_HL7FileNode_DefaultValue: Property = Property(name="DefaultValue", type=StringType)
connection_HL7FileNode_RelatedColumn: Property = Property(name="RelatedColumn", type=StringType)
connection_HL7FileNode_Repeatable: Property = Property(name="Repeatable", type=BooleanType)
connection_HL7FileNode.attributes={connection_HL7FileNode_Repeatable, connection_HL7FileNode_FilePath, connection_HL7FileNode_DefaultValue, connection_HL7FileNode_RelatedColumn, connection_HL7FileNode_Order, connection_HL7FileNode_Attribute}

# connection_HeaderFooterConnection class attributes and methods
connection_HeaderFooterConnection_isHeader: Property = Property(name="isHeader", type=BooleanType)
connection_HeaderFooterConnection_imports: Property = Property(name="imports", type=StringType)
connection_HeaderFooterConnection_mainCode: Property = Property(name="mainCode", type=StringType)
connection_HeaderFooterConnection_libraries: Property = Property(name="libraries", type=StringType)
connection_HeaderFooterConnection.attributes={connection_HeaderFooterConnection_imports, connection_HeaderFooterConnection_mainCode, connection_HeaderFooterConnection_isHeader, connection_HeaderFooterConnection_libraries}

# connection_SubscriberTable class attributes and methods
connection_SubscriberTable_system: Property = Property(name="system", type=BooleanType)
connection_SubscriberTable.attributes={connection_SubscriberTable_system}

# connection_GenericPackage class attributes and methods

# Package class attributes and methods

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
connection_FTPConnection_KeystoreFile: Property = Property(name="KeystoreFile", type=StringType)
connection_FTPConnection_KeystorePassword: Property = Property(name="KeystorePassword", type=StringType)
connection_FTPConnection_Usesocks: Property = Property(name="Usesocks", type=BooleanType)
connection_FTPConnection_CustomEncode: Property = Property(name="CustomEncode", type=StringType)
connection_FTPConnection_Proxyhost: Property = Property(name="Proxyhost", type=StringType)
connection_FTPConnection_Proxyport: Property = Property(name="Proxyport", type=StringType)
connection_FTPConnection_Proxyuser: Property = Property(name="Proxyuser", type=StringType)
connection_FTPConnection_Proxypassword: Property = Property(name="Proxypassword", type=StringType)
connection_FTPConnection.attributes={connection_FTPConnection_Ecoding, connection_FTPConnection_Password, connection_FTPConnection_KeystorePassword, connection_FTPConnection_Proxypassword, connection_FTPConnection_Proxyuser, connection_FTPConnection_CustomEncode, connection_FTPConnection_Mode, connection_FTPConnection_KeystoreFile, connection_FTPConnection_Usesocks, connection_FTPConnection_Proxyport, connection_FTPConnection_Username, connection_FTPConnection_Method, connection_FTPConnection_Port, connection_FTPConnection_Proxyhost, connection_FTPConnection_SFTP, connection_FTPConnection_Host, connection_FTPConnection_FTPS}

# Machine class attributes and methods

# connection_relational_TdTable class attributes and methods

# MetadataTable class attributes and methods

# relational_Table class attributes and methods

# connection_relational_TdView class attributes and methods

# connection_xml_TdXmlElementType class attributes and methods
connection_xml_TdXmlElementType_javaType: Property = Property(name="javaType", type=StringType)
connection_xml_TdXmlElementType_m_setContentType: Method = Method(name="setContentType", parameters={Parameter(name='connection_contentType', type=StringType)})
connection_xml_TdXmlElementType_m_getContentType: Method = Method(name="getContentType", parameters={}, type=StringType)
connection_xml_TdXmlElementType.attributes={connection_xml_TdXmlElementType_javaType}
connection_xml_TdXmlElementType.methods={connection_xml_TdXmlElementType_m_setContentType, connection_xml_TdXmlElementType_m_getContentType}

# relational_View class attributes and methods

# ElementType class attributes and methods

# connection_relational_TdColumn class attributes and methods
connection_relational_TdColumn_m_setContentType: Method = Method(name="setContentType", parameters={Parameter(name='connection_contentType', type=StringType)})
connection_relational_TdColumn_m_getContentType: Method = Method(name="getContentType", parameters={}, type=StringType)
connection_relational_TdColumn_m_getJavaType: Method = Method(name="getJavaType", parameters={}, type=IntegerType)
connection_relational_TdColumn.methods={connection_relational_TdColumn_m_setContentType, connection_relational_TdColumn_m_getContentType, connection_relational_TdColumn_m_getJavaType}

# MetadataColumn class attributes and methods

# xml_connection_EObject class attributes and methods

# xml_TdXmlSchema class attributes and methods

# relational_TdSqlDataType class attributes and methods

# connection_relational_TdSqlDataType class attributes and methods
connection_relational_TdSqlDataType_javaDataType: Property = Property(name="javaDataType", type=IntegerType)
connection_relational_TdSqlDataType_nullable: Property = Property(name="nullable", type=StringType)
connection_relational_TdSqlDataType_unsignedAttribute: Property = Property(name="unsignedAttribute", type=StringType)
connection_relational_TdSqlDataType_caseSensitive: Property = Property(name="caseSensitive", type=StringType)
connection_relational_TdSqlDataType_autoIncrement: Property = Property(name="autoIncrement", type=StringType)
connection_relational_TdSqlDataType_localTypeName: Property = Property(name="localTypeName", type=StringType)
connection_relational_TdSqlDataType_searchable: Property = Property(name="searchable", type=StringType)
connection_relational_TdSqlDataType.attributes={connection_relational_TdSqlDataType_nullable, connection_relational_TdSqlDataType_caseSensitive, connection_relational_TdSqlDataType_searchable, connection_relational_TdSqlDataType_unsignedAttribute, connection_relational_TdSqlDataType_autoIncrement, connection_relational_TdSqlDataType_localTypeName, connection_relational_TdSqlDataType_javaDataType}

# SQLSimpleType class attributes and methods

# connection_relational_TdTrigger class attributes and methods

# Trigger class attributes and methods

# connection_relational_TdProcedure class attributes and methods

# Procedure class attributes and methods

# connection_softwaredeployment_TdDataManager class attributes and methods

# DataManager class attributes and methods

# connection_softwaredeployment_TdSoftwareSystem class attributes and methods

# SoftwareSystem class attributes and methods

# connection_softwaredeployment_TdMachine class attributes and methods

# xml_TdXmlContent class attributes and methods

# connection_xml_TdXmlContent class attributes and methods

# Content class attributes and methods

# xml_TdXmlElementType class attributes and methods

# connection_xml_TdXmlSchema class attributes and methods
connection_xml_TdXmlSchema_xsdFilePath: Property = Property(name="xsdFilePath", type=StringType)
connection_xml_TdXmlSchema.attributes={connection_xml_TdXmlSchema_xsdFilePath}

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
schemas9: BinaryAssociation = BinaryAssociation(
    name="schemas9",
    ends={
        Property(name="connection_Concept", type=connection_MDMConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_MDMConnection", type=connection_Concept, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cdcConns10: BinaryAssociation = BinaryAssociation(
    name="cdcConns10",
    ends={
        Property(name="CDCConnection", type=connection_DatabaseConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection11", type=connection_CDCConnection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Funtions12: BinaryAssociation = BinaryAssociation(
    name="Funtions12",
    ends={
        Property(name="SAPFunctionUnit", type=connection_SAPConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection13", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IDocs14: BinaryAssociation = BinaryAssociation(
    name="IDocs14",
    ends={
        Property(name="SAPIDocUnit", type=connection_SAPConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection15", type=connection_SAPIDocUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
InputParameterTable16: BinaryAssociation = BinaryAssociation(
    name="InputParameterTable16",
    ends={
        Property(name="InputSAPFunctionParameterTable", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="functionUnit", type=connection_InputSAPFunctionParameterTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
OutputParameterTable17: BinaryAssociation = BinaryAssociation(
    name="OutputParameterTable17",
    ends={
        Property(name="OutputSAPFunctionParameterTable", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="functionUnit18", type=connection_OutputSAPFunctionParameterTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
MetadataTable19: BinaryAssociation = BinaryAssociation(
    name="MetadataTable19",
    ends={
        Property(name="connection_MetadataTable20", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_SAPFunctionUnit", type=connection_MetadataTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connection21: BinaryAssociation = BinaryAssociation(
    name="connection21",
    ends={
        Property(name="SAPConnection", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="Funtions", type=connection_SAPConnection, multiplicity=Multiplicity(0, 1))
    }
)
tables22: BinaryAssociation = BinaryAssociation(
    name="tables22",
    ends={
        Property(name="connection_MetadataTable24", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_SAPFunctionUnit23", type=connection_MetadataTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
TestInputParameterTable25: BinaryAssociation = BinaryAssociation(
    name="TestInputParameterTable25",
    ends={
        Property(name="SAPTestInputParameterTable", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="functionUnit26", type=connection_SAPTestInputParameterTable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
connection27: BinaryAssociation = BinaryAssociation(
    name="connection27",
    ends={
        Property(name="SAPConnection28", type=connection_SAPIDocUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="IDocs", type=connection_SAPConnection, multiplicity=Multiplicity(0, 1))
    }
)
ParameterTable29: BinaryAssociation = BinaryAssociation(
    name="ParameterTable29",
    ends={
        Property(name="SAPFunctionParameterTable", type=connection_SAPFunctionParameterColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=connection_SAPFunctionParameterTable, multiplicity=Multiplicity(0, 1))
    }
)
functionUnit31: BinaryAssociation = BinaryAssociation(
    name="functionUnit31",
    ends={
        Property(name="SAPFunctionUnit32", type=connection_InputSAPFunctionParameterTable, multiplicity=Multiplicity(1, 1)),
        Property(name="InputParameterTable", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(0, 1))
    }
)
functionUnit33: BinaryAssociation = BinaryAssociation(
    name="functionUnit33",
    ends={
        Property(name="SAPFunctionUnit34", type=connection_OutputSAPFunctionParameterTable, multiplicity=Multiplicity(1, 1)),
        Property(name="OutputParameterTable", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(0, 1))
    }
)
schema35: BinaryAssociation = BinaryAssociation(
    name="schema35",
    ends={
        Property(name="XmlXPathLoopDescriptor", type=connection_XmlFileConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection36", type=connection_XmlXPathLoopDescriptor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group37: BinaryAssociation = BinaryAssociation(
    name="group37",
    ends={
        Property(name="connection_XMLFileNode", type=connection_XmlFileConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_XmlFileConnection", type=connection_XMLFileNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root38: BinaryAssociation = BinaryAssociation(
    name="root38",
    ends={
        Property(name="connection_XMLFileNode40", type=connection_XmlFileConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_XmlFileConnection39", type=connection_XMLFileNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loop41: BinaryAssociation = BinaryAssociation(
    name="loop41",
    ends={
        Property(name="connection_XMLFileNode43", type=connection_XmlFileConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_XmlFileConnection42", type=connection_XMLFileNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schema44: BinaryAssociation = BinaryAssociation(
    name="schema44",
    ends={
        Property(name="XmlXPathLoopDescriptor45", type=connection_SchemaTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="schemaTargets", type=connection_XmlXPathLoopDescriptor, multiplicity=Multiplicity(0, 1))
    }
)
connection46: BinaryAssociation = BinaryAssociation(
    name="connection46",
    ends={
        Property(name="Connection", type=connection_QueriesConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="queries", type=connection_Connection, multiplicity=Multiplicity(0, 1))
    }
)
query47: BinaryAssociation = BinaryAssociation(
    name="query47",
    ends={
        Property(name="Query", type=connection_QueriesConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="queries48", type=connection_Query, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns30: BinaryAssociation = BinaryAssociation(
    name="columns30",
    ends={
        Property(name="SAPFunctionParameterColumn", type=connection_SAPFunctionParameterTable, multiplicity=Multiplicity(1, 1)),
        Property(name="ParameterTable", type=connection_SAPFunctionParameterColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
queries49: BinaryAssociation = BinaryAssociation(
    name="queries49",
    ends={
        Property(name="QueriesConnection50", type=connection_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="query", type=connection_QueriesConnection, multiplicity=Multiplicity(0, 1))
    }
)
connection51: BinaryAssociation = BinaryAssociation(
    name="connection51",
    ends={
        Property(name="XmlFileConnection", type=connection_XmlXPathLoopDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=connection_XmlFileConnection, multiplicity=Multiplicity(0, 1))
    }
)
schemaTargets52: BinaryAssociation = BinaryAssociation(
    name="schemaTargets52",
    ends={
        Property(name="SchemaTarget", type=connection_XmlXPathLoopDescriptor, multiplicity=Multiplicity(1, 1)),
        Property(name="schema53", type=connection_SchemaTarget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterValue54: BinaryAssociation = BinaryAssociation(
    name="parameterValue54",
    ends={
        Property(name="connection_WSDLParameter", type=connection_WSDLSchemaConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_WSDLSchemaConnection", type=connection_WSDLParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputParameter55: BinaryAssociation = BinaryAssociation(
    name="outputParameter55",
    ends={
        Property(name="connection_WSDLParameter57", type=connection_WSDLSchemaConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_WSDLSchemaConnection56", type=connection_WSDLParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connection58: BinaryAssociation = BinaryAssociation(
    name="connection58",
    ends={
        Property(name="DatabaseConnection", type=connection_CDCConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="cdcConns", type=connection_DatabaseConnection, multiplicity=Multiplicity(0, 1))
    }
)
cdcTypes59: BinaryAssociation = BinaryAssociation(
    name="cdcTypes59",
    ends={
        Property(name="connection_CDCType", type=connection_CDCConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_CDCConnection", type=connection_CDCType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cdcConnection62: BinaryAssociation = BinaryAssociation(
    name="cdcConnection62",
    ends={
        Property(name="connection_CDCConnection64", type=connection_CDCType, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_CDCType63", type=connection_CDCConnection, multiplicity=Multiplicity(0, 1))
    }
)
functionUnit65: BinaryAssociation = BinaryAssociation(
    name="functionUnit65",
    ends={
        Property(name="SAPFunctionUnit66", type=connection_SAPTestInputParameterTable, multiplicity=Multiplicity(1, 1)),
        Property(name="TestInputParameterTable", type=connection_SAPFunctionUnit, multiplicity=Multiplicity(0, 1))
    }
)
conceptTargets67: BinaryAssociation = BinaryAssociation(
    name="conceptTargets67",
    ends={
        Property(name="ConceptTarget", type=connection_Concept, multiplicity=Multiplicity(1, 1)),
        Property(name="schema68", type=connection_ConceptTarget, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
group69: BinaryAssociation = BinaryAssociation(
    name="group69",
    ends={
        Property(name="connection_XMLFileNode71", type=connection_Concept, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_Concept70", type=connection_XMLFileNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
root72: BinaryAssociation = BinaryAssociation(
    name="root72",
    ends={
        Property(name="connection_XMLFileNode74", type=connection_Concept, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_Concept73", type=connection_XMLFileNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loop75: BinaryAssociation = BinaryAssociation(
    name="loop75",
    ends={
        Property(name="connection_XMLFileNode77", type=connection_Concept, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_Concept76", type=connection_XMLFileNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schema78: BinaryAssociation = BinaryAssociation(
    name="schema78",
    ends={
        Property(name="Concept", type=connection_ConceptTarget, multiplicity=Multiplicity(1, 1)),
        Property(name="conceptTargets", type=connection_Concept, multiplicity=Multiplicity(0, 1))
    }
)
root79: BinaryAssociation = BinaryAssociation(
    name="root79",
    ends={
        Property(name="connection_HL7FileNode", type=connection_HL7Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_HL7Connection", type=connection_HL7FileNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subscribers60: BinaryAssociation = BinaryAssociation(
    name="subscribers60",
    ends={
        Property(name="connection_SubscriberTable", type=connection_CDCType, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_CDCType61", type=connection_SubscriberTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xsdElementDeclaration81: BinaryAssociation = BinaryAssociation(
    name="xsdElementDeclaration81",
    ends={
        Property(name="xml_connection_EObject", type=connection_xml_TdXmlElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_xml_TdXmlElementType", type=xml_connection_EObject, multiplicity=Multiplicity(0, 1))
    }
)
ownedDocument82: BinaryAssociation = BinaryAssociation(
    name="ownedDocument82",
    ends={
        Property(name="xml_TdXmlSchema", type=connection_xml_TdXmlElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_xml_TdXmlElementType83", type=xml_TdXmlSchema, multiplicity=Multiplicity(0, 1))
    }
)
sqlDataType80: BinaryAssociation = BinaryAssociation(
    name="sqlDataType80",
    ends={
        Property(name="relational_TdSqlDataType", type=connection_relational_TdColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_relational_TdColumn", type=relational_TdSqlDataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xmlContent84: BinaryAssociation = BinaryAssociation(
    name="xmlContent84",
    ends={
        Property(name="xml_TdXmlContent", type=connection_xml_TdXmlElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="connection_xml_TdXmlElementType85", type=xml_TdXmlContent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xmlElements86: BinaryAssociation = BinaryAssociation(
    name="xmlElements86",
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
gen_connection_AbstractMetadataObject_ModelElement = Generalization(general=ModelElement, specific=connection_AbstractMetadataObject)
gen_connection_MetadataTable_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_MetadataTable)
gen_connection_MetadataTable_core_Class = Generalization(general=core_Class, specific=connection_MetadataTable)
gen_connection_DelimitedFileConnection_FileConnection = Generalization(general=FileConnection, specific=connection_DelimitedFileConnection)
gen_connection_PositionalFileConnection_FileConnection = Generalization(general=FileConnection, specific=connection_PositionalFileConnection)
gen_connection_EbcdicConnection_FileConnection = Generalization(general=FileConnection, specific=connection_EbcdicConnection)
gen_connection_MDMConnection_Connection = Generalization(general=Connection, specific=connection_MDMConnection)
gen_connection_FileConnection_Connection = Generalization(general=Connection, specific=connection_FileConnection)
gen_connection_DatabaseConnection_Connection = Generalization(general=Connection, specific=connection_DatabaseConnection)
gen_connection_SAPConnection_Connection = Generalization(general=Connection, specific=connection_SAPConnection)
gen_connection_SAPFunctionUnit_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_SAPFunctionUnit)
gen_connection_SAPIDocUnit_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_SAPIDocUnit)
gen_connection_SAPFunctionParameterColumn_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_SAPFunctionParameterColumn)
gen_connection_InputSAPFunctionParameterTable_SAPFunctionParameterTable = Generalization(general=SAPFunctionParameterTable, specific=connection_InputSAPFunctionParameterTable)
gen_connection_OutputSAPFunctionParameterTable_SAPFunctionParameterTable = Generalization(general=SAPFunctionParameterTable, specific=connection_OutputSAPFunctionParameterTable)
gen_connection_RegexpFileConnection_FileConnection = Generalization(general=FileConnection, specific=connection_RegexpFileConnection)
gen_connection_XmlFileConnection_Connection = Generalization(general=Connection, specific=connection_XmlFileConnection)
gen_connection_SAPFunctionParameterTable_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_SAPFunctionParameterTable)
gen_connection_Query_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_Query)
gen_connection_LdifFileConnection_Connection = Generalization(general=Connection, specific=connection_LdifFileConnection)
gen_connection_FileExcelConnection_FileConnection = Generalization(general=FileConnection, specific=connection_FileExcelConnection)
gen_connection_LDAPSchemaConnection_Connection = Generalization(general=Connection, specific=connection_LDAPSchemaConnection)
gen_connection_WSDLSchemaConnection_Connection = Generalization(general=Connection, specific=connection_WSDLSchemaConnection)
gen_connection_GenericSchemaConnection_Connection = Generalization(general=Connection, specific=connection_GenericSchemaConnection)
gen_connection_SalesforceSchemaConnection_Connection = Generalization(general=Connection, specific=connection_SalesforceSchemaConnection)
gen_connection_CDCType_AbstractMetadataObject = Generalization(general=AbstractMetadataObject, specific=connection_CDCType)
gen_connection_SubscriberTable_TdTable = Generalization(general=TdTable, specific=connection_SubscriberTable)
gen_connection_SAPTestInputParameterTable_SAPFunctionParameterTable = Generalization(general=SAPFunctionParameterTable, specific=connection_SAPTestInputParameterTable)
gen_connection_Concept_TdTable = Generalization(general=TdTable, specific=connection_Concept)
gen_connection_HL7Connection_FileConnection = Generalization(general=FileConnection, specific=connection_HL7Connection)
gen_connection_HeaderFooterConnection_Connection = Generalization(general=Connection, specific=connection_HeaderFooterConnection)
gen_connection_GenericPackage_Package = Generalization(general=Package, specific=connection_GenericPackage)
gen_connection_FTPConnection_Connection = Generalization(general=Connection, specific=connection_FTPConnection)
gen_connection_softwaredeployment_TdMachine_Machine = Generalization(general=Machine, specific=connection_softwaredeployment_TdMachine)
gen_connection_relational_TdTable_MetadataTable = Generalization(general=MetadataTable, specific=connection_relational_TdTable)
gen_connection_relational_TdTable_relational_Table = Generalization(general=relational_Table, specific=connection_relational_TdTable)
gen_connection_relational_TdView_MetadataTable = Generalization(general=MetadataTable, specific=connection_relational_TdView)
gen_connection_relational_TdView_relational_View = Generalization(general=relational_View, specific=connection_relational_TdView)
gen_connection_xml_TdXmlElementType_ElementType = Generalization(general=ElementType, specific=connection_xml_TdXmlElementType)
gen_connection_relational_TdColumn_MetadataColumn = Generalization(general=MetadataColumn, specific=connection_relational_TdColumn)
gen_connection_relational_TdSqlDataType_SQLSimpleType = Generalization(general=SQLSimpleType, specific=connection_relational_TdSqlDataType)
gen_connection_relational_TdTrigger_Trigger = Generalization(general=Trigger, specific=connection_relational_TdTrigger)
gen_connection_relational_TdProcedure_Procedure = Generalization(general=Procedure, specific=connection_relational_TdProcedure)
gen_connection_softwaredeployment_TdDataManager_DataManager = Generalization(general=DataManager, specific=connection_softwaredeployment_TdDataManager)
gen_connection_softwaredeployment_TdSoftwareSystem_SoftwareSystem = Generalization(general=SoftwareSystem, specific=connection_softwaredeployment_TdSoftwareSystem)
gen_connection_xml_TdXmlContent_Content = Generalization(general=Content, specific=connection_xml_TdXmlContent)
gen_connection_xml_TdXmlSchema_Schema = Generalization(general=Schema, specific=connection_xml_TdXmlSchema)

# Domain Model
domain_model = DomainModel(
    name="connection",
    types={connection_Metadata, AbstractMetadataObject, connection_Connection, softwaredeployment_DataProvider, connection_QueriesConnection, connection_MetadataColumn, record_Field, connection_MetadataTable, connection_AbstractMetadataObject, ModelElement, core_Class, connection_DelimitedFileConnection, FileConnection, connection_PositionalFileConnection, connection_EbcdicConnection, connection_MDMConnection, connection_Concept, connection_FileConnection, Connection, connection_DatabaseConnection, connection_CDCConnection, connection_SAPConnection, connection_SAPFunctionUnit, connection_SAPIDocUnit, connection_InputSAPFunctionParameterTable, connection_OutputSAPFunctionParameterTable, connection_SAPTestInputParameterTable, connection_SAPFunctionParameterColumn, connection_SAPFunctionParameterTable, SAPFunctionParameterTable, connection_RegexpFileConnection, connection_XmlFileConnection, connection_XmlXPathLoopDescriptor, connection_XMLFileNode, connection_SchemaTarget, connection_Query, connection_LdifFileConnection, connection_FileExcelConnection, connection_LDAPSchemaConnection, connection_WSDLSchemaConnection, connection_GenericSchemaConnection, connection_WSDLParameter, connection_SalesforceSchemaConnection, connection_CDCType, TdTable, connection_ConceptTarget, connection_HL7Connection, connection_HL7FileNode, connection_HeaderFooterConnection, connection_SubscriberTable, connection_GenericPackage, Package, connection_FTPConnection, Machine, connection_relational_TdTable, MetadataTable, relational_Table, connection_relational_TdView, connection_xml_TdXmlElementType, relational_View, ElementType, connection_relational_TdColumn, MetadataColumn, xml_connection_EObject, xml_TdXmlSchema, relational_TdSqlDataType, connection_relational_TdSqlDataType, SQLSimpleType, connection_relational_TdTrigger, Trigger, connection_relational_TdProcedure, Procedure, connection_softwaredeployment_TdDataManager, DataManager, connection_softwaredeployment_TdSoftwareSystem, SoftwareSystem, connection_softwaredeployment_TdMachine, xml_TdXmlContent, connection_xml_TdXmlContent, Content, xml_TdXmlElementType, connection_xml_TdXmlSchema, Schema, FileFormat, FieldSeparator, Escape, RowSeparator, MDMConnectionProtocol, DevelopmentStatus},
    associations={connections0, queries1, table2, columns3, connection6, schemas9, cdcConns10, Funtions12, IDocs14, InputParameterTable16, OutputParameterTable17, MetadataTable19, connection21, tables22, TestInputParameterTable25, connection27, ParameterTable29, functionUnit31, functionUnit33, schema35, group37, root38, loop41, schema44, connection46, query47, columns30, queries49, connection51, schemaTargets52, parameterValue54, outputParameter55, connection58, cdcTypes59, cdcConnection62, functionUnit65, conceptTargets67, group69, root72, loop75, schema78, root79, subscribers60, xsdElementDeclaration81, ownedDocument82, sqlDataType80, xmlContent84, xmlElements86},
    generalizations={gen_connection_Metadata_AbstractMetadataObject, gen_connection_Connection_AbstractMetadataObject, gen_connection_Connection_softwaredeployment_DataProvider, gen_connection_MetadataColumn_AbstractMetadataObject, gen_connection_MetadataColumn_record_Field, gen_connection_AbstractMetadataObject_ModelElement, gen_connection_MetadataTable_AbstractMetadataObject, gen_connection_MetadataTable_core_Class, gen_connection_DelimitedFileConnection_FileConnection, gen_connection_PositionalFileConnection_FileConnection, gen_connection_EbcdicConnection_FileConnection, gen_connection_MDMConnection_Connection, gen_connection_FileConnection_Connection, gen_connection_DatabaseConnection_Connection, gen_connection_SAPConnection_Connection, gen_connection_SAPFunctionUnit_AbstractMetadataObject, gen_connection_SAPIDocUnit_AbstractMetadataObject, gen_connection_SAPFunctionParameterColumn_AbstractMetadataObject, gen_connection_InputSAPFunctionParameterTable_SAPFunctionParameterTable, gen_connection_OutputSAPFunctionParameterTable_SAPFunctionParameterTable, gen_connection_RegexpFileConnection_FileConnection, gen_connection_XmlFileConnection_Connection, gen_connection_SAPFunctionParameterTable_AbstractMetadataObject, gen_connection_Query_AbstractMetadataObject, gen_connection_LdifFileConnection_Connection, gen_connection_FileExcelConnection_FileConnection, gen_connection_LDAPSchemaConnection_Connection, gen_connection_WSDLSchemaConnection_Connection, gen_connection_GenericSchemaConnection_Connection, gen_connection_SalesforceSchemaConnection_Connection, gen_connection_CDCType_AbstractMetadataObject, gen_connection_SubscriberTable_TdTable, gen_connection_SAPTestInputParameterTable_SAPFunctionParameterTable, gen_connection_Concept_TdTable, gen_connection_HL7Connection_FileConnection, gen_connection_HeaderFooterConnection_Connection, gen_connection_GenericPackage_Package, gen_connection_FTPConnection_Connection, gen_connection_softwaredeployment_TdMachine_Machine, gen_connection_relational_TdTable_MetadataTable, gen_connection_relational_TdTable_relational_Table, gen_connection_relational_TdView_MetadataTable, gen_connection_relational_TdView_relational_View, gen_connection_xml_TdXmlElementType_ElementType, gen_connection_relational_TdColumn_MetadataColumn, gen_connection_relational_TdSqlDataType_SQLSimpleType, gen_connection_relational_TdTrigger_Trigger, gen_connection_relational_TdProcedure_Procedure, gen_connection_softwaredeployment_TdDataManager_DataManager, gen_connection_softwaredeployment_TdSoftwareSystem_SoftwareSystem, gen_connection_xml_TdXmlContent_Content, gen_connection_xml_TdXmlSchema_Schema},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)