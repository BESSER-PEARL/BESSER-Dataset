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
DevelopmentStatus: Enumeration = Enumeration(
    name="DevelopmentStatus",
    literals={
            EnumerationLiteral(name="DRAFT"),
			EnumerationLiteral(name="PROD")
    }
)

# Classes
cwm_relational_TdTable = Class(name="cwm_relational_TdTable")
Table = Class(name="Table")
cwm_relational_TdView = Class(name="cwm_relational_TdView")
View = Class(name="View")
cwm_relational_TdCatalog = Class(name="cwm_relational_TdCatalog")
Catalog = Class(name="Catalog")
cwm_relational_TdSchema = Class(name="cwm_relational_TdSchema")
Schema = Class(name="Schema")
cwm_relational_TdColumn = Class(name="cwm_relational_TdColumn")
Column = Class(name="Column")
TdSqlDataType = Class(name="TdSqlDataType")
cwm_relational_TdSqlDataType = Class(name="cwm_relational_TdSqlDataType")
SQLSimpleType = Class(name="SQLSimpleType")
cwm_relational_TdTrigger = Class(name="cwm_relational_TdTrigger")
Trigger = Class(name="Trigger")
cwm_relational_TdProcedure = Class(name="cwm_relational_TdProcedure")
Procedure = Class(name="Procedure")
cwm_softwaredeployment_TdProviderConnection = Class(name="cwm_softwaredeployment_TdProviderConnection")
ProviderConnection = Class(name="ProviderConnection")
cwm_softwaredeployment_TdDataManager = Class(name="cwm_softwaredeployment_TdDataManager")
DataManager = Class(name="DataManager")
cwm_softwaredeployment_TdDataProvider = Class(name="cwm_softwaredeployment_TdDataProvider")
DataProvider = Class(name="DataProvider")
xml_cwm_EObject = Class(name="xml_cwm_EObject")
TdXMLDocument = Class(name="TdXMLDocument")
TdXMLContent = Class(name="TdXMLContent")
cwm_xml_TdXMLContent = Class(name="cwm_xml_TdXMLContent")
Content = Class(name="Content")
TdXMLElement = Class(name="TdXMLElement")
cwm_xml_TdXMLDocument = Class(name="cwm_xml_TdXMLDocument")
Document = Class(name="Document")
cwm_softwaredeployment_TdSoftwareSystem = Class(name="cwm_softwaredeployment_TdSoftwareSystem")
SoftwareSystem = Class(name="SoftwareSystem")
cwm_softwaredeployment_TdMachine = Class(name="cwm_softwaredeployment_TdMachine")
Machine = Class(name="Machine")
cwm_xml_TdXMLElement = Class(name="cwm_xml_TdXMLElement")
Element = Class(name="Element")

# cwm_relational_TdTable class attributes and methods

# Table class attributes and methods

# cwm_relational_TdView class attributes and methods

# View class attributes and methods

# cwm_relational_TdCatalog class attributes and methods
cwm_relational_TdCatalog_m_addSchema: Method = Method(name="addSchema", parameters={Parameter(name='cwm_schema', type=StringType)}, type=BooleanType)
cwm_relational_TdCatalog.methods={cwm_relational_TdCatalog_m_addSchema}

# Catalog class attributes and methods

# cwm_relational_TdSchema class attributes and methods

# Schema class attributes and methods

# cwm_relational_TdColumn class attributes and methods
cwm_relational_TdColumn_javaType: Property = Property(name="javaType", type=IntegerType)
cwm_relational_TdColumn_m_setContentType: Method = Method(name="setContentType", parameters={Parameter(name='cwm_contentType', type=StringType)})
cwm_relational_TdColumn_m_getContentType: Method = Method(name="getContentType", parameters={}, type=StringType)
cwm_relational_TdColumn.attributes={cwm_relational_TdColumn_javaType}
cwm_relational_TdColumn.methods={cwm_relational_TdColumn_m_getContentType, cwm_relational_TdColumn_m_setContentType}

# Column class attributes and methods

# TdSqlDataType class attributes and methods

# cwm_relational_TdSqlDataType class attributes and methods
cwm_relational_TdSqlDataType_javaDataType: Property = Property(name="javaDataType", type=IntegerType)
cwm_relational_TdSqlDataType_nullable: Property = Property(name="nullable", type=StringType)
cwm_relational_TdSqlDataType_unsignedAttribute: Property = Property(name="unsignedAttribute", type=StringType)
cwm_relational_TdSqlDataType_caseSensitive: Property = Property(name="caseSensitive", type=StringType)
cwm_relational_TdSqlDataType_autoIncrement: Property = Property(name="autoIncrement", type=StringType)
cwm_relational_TdSqlDataType_localTypeName: Property = Property(name="localTypeName", type=StringType)
cwm_relational_TdSqlDataType_searchable: Property = Property(name="searchable", type=StringType)
cwm_relational_TdSqlDataType.attributes={cwm_relational_TdSqlDataType_localTypeName, cwm_relational_TdSqlDataType_autoIncrement, cwm_relational_TdSqlDataType_caseSensitive, cwm_relational_TdSqlDataType_unsignedAttribute, cwm_relational_TdSqlDataType_searchable, cwm_relational_TdSqlDataType_javaDataType, cwm_relational_TdSqlDataType_nullable}

# SQLSimpleType class attributes and methods

# cwm_relational_TdTrigger class attributes and methods

# Trigger class attributes and methods

# cwm_relational_TdProcedure class attributes and methods

# Procedure class attributes and methods

# cwm_softwaredeployment_TdProviderConnection class attributes and methods
cwm_softwaredeployment_TdProviderConnection_login: Property = Property(name="login", type=StringType)
cwm_softwaredeployment_TdProviderConnection_password: Property = Property(name="password", type=StringType)
cwm_softwaredeployment_TdProviderConnection_connectionString: Property = Property(name="connectionString", type=StringType)
cwm_softwaredeployment_TdProviderConnection_driverClassName: Property = Property(name="driverClassName", type=StringType)
cwm_softwaredeployment_TdProviderConnection.attributes={cwm_softwaredeployment_TdProviderConnection_connectionString, cwm_softwaredeployment_TdProviderConnection_driverClassName, cwm_softwaredeployment_TdProviderConnection_password, cwm_softwaredeployment_TdProviderConnection_login}

# ProviderConnection class attributes and methods

# cwm_softwaredeployment_TdDataManager class attributes and methods

# DataManager class attributes and methods

# cwm_softwaredeployment_TdDataProvider class attributes and methods

# DataProvider class attributes and methods

# xml_cwm_EObject class attributes and methods

# TdXMLDocument class attributes and methods

# TdXMLContent class attributes and methods

# cwm_xml_TdXMLContent class attributes and methods

# Content class attributes and methods

# TdXMLElement class attributes and methods

# cwm_xml_TdXMLDocument class attributes and methods
cwm_xml_TdXMLDocument_xsdFilePath: Property = Property(name="xsdFilePath", type=StringType)
cwm_xml_TdXMLDocument.attributes={cwm_xml_TdXMLDocument_xsdFilePath}

# Document class attributes and methods

# cwm_softwaredeployment_TdSoftwareSystem class attributes and methods

# SoftwareSystem class attributes and methods

# cwm_softwaredeployment_TdMachine class attributes and methods

# Machine class attributes and methods

# cwm_xml_TdXMLElement class attributes and methods
cwm_xml_TdXMLElement_javaType: Property = Property(name="javaType", type=StringType)
cwm_xml_TdXMLElement_m_setContentType: Method = Method(name="setContentType", parameters={Parameter(name='cwm_contentType', type=StringType)})
cwm_xml_TdXMLElement_m_getContentType: Method = Method(name="getContentType", parameters={}, type=StringType)
cwm_xml_TdXMLElement.attributes={cwm_xml_TdXMLElement_javaType}
cwm_xml_TdXMLElement.methods={cwm_xml_TdXMLElement_m_setContentType, cwm_xml_TdXMLElement_m_getContentType}

# Element class attributes and methods

# Relationships
sqlDataType0: BinaryAssociation = BinaryAssociation(
    name="sqlDataType0",
    ends={
        Property(name="TdSqlDataType", type=cwm_relational_TdColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="cwm_relational_TdColumn", type=TdSqlDataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xsdElementDeclaration1: BinaryAssociation = BinaryAssociation(
    name="xsdElementDeclaration1",
    ends={
        Property(name="xml_cwm_EObject", type=cwm_xml_TdXMLElement, multiplicity=Multiplicity(1, 1)),
        Property(name="cwm_xml_TdXMLElement", type=xml_cwm_EObject, multiplicity=Multiplicity(0, 1))
    }
)
ownedDocument2: BinaryAssociation = BinaryAssociation(
    name="ownedDocument2",
    ends={
        Property(name="TdXMLDocument", type=cwm_xml_TdXMLElement, multiplicity=Multiplicity(1, 1)),
        Property(name="cwm_xml_TdXMLElement3", type=TdXMLDocument, multiplicity=Multiplicity(0, 1))
    }
)
xmlContent4: BinaryAssociation = BinaryAssociation(
    name="xmlContent4",
    ends={
        Property(name="TdXMLContent", type=cwm_xml_TdXMLElement, multiplicity=Multiplicity(1, 1)),
        Property(name="cwm_xml_TdXMLElement5", type=TdXMLContent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xmlElements6: BinaryAssociation = BinaryAssociation(
    name="xmlElements6",
    ends={
        Property(name="TdXMLElement", type=cwm_xml_TdXMLContent, multiplicity=Multiplicity(1, 1)),
        Property(name="cwm_xml_TdXMLContent", type=TdXMLElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_cwm_relational_TdTable_Table = Generalization(general=Table, specific=cwm_relational_TdTable)
gen_cwm_relational_TdView_View = Generalization(general=View, specific=cwm_relational_TdView)
gen_cwm_relational_TdCatalog_Catalog = Generalization(general=Catalog, specific=cwm_relational_TdCatalog)
gen_cwm_relational_TdSchema_Schema = Generalization(general=Schema, specific=cwm_relational_TdSchema)
gen_cwm_relational_TdSqlDataType_SQLSimpleType = Generalization(general=SQLSimpleType, specific=cwm_relational_TdSqlDataType)
gen_cwm_relational_TdTrigger_Trigger = Generalization(general=Trigger, specific=cwm_relational_TdTrigger)
gen_cwm_relational_TdProcedure_Procedure = Generalization(general=Procedure, specific=cwm_relational_TdProcedure)
gen_cwm_softwaredeployment_TdProviderConnection_ProviderConnection = Generalization(general=ProviderConnection, specific=cwm_softwaredeployment_TdProviderConnection)
gen_cwm_softwaredeployment_TdDataManager_DataManager = Generalization(general=DataManager, specific=cwm_softwaredeployment_TdDataManager)
gen_cwm_softwaredeployment_TdDataProvider_DataProvider = Generalization(general=DataProvider, specific=cwm_softwaredeployment_TdDataProvider)
gen_cwm_relational_TdColumn_Column = Generalization(general=Column, specific=cwm_relational_TdColumn)
gen_cwm_xml_TdXMLContent_Content = Generalization(general=Content, specific=cwm_xml_TdXMLContent)
gen_cwm_xml_TdXMLDocument_Document = Generalization(general=Document, specific=cwm_xml_TdXMLDocument)
gen_cwm_softwaredeployment_TdSoftwareSystem_SoftwareSystem = Generalization(general=SoftwareSystem, specific=cwm_softwaredeployment_TdSoftwareSystem)
gen_cwm_softwaredeployment_TdMachine_Machine = Generalization(general=Machine, specific=cwm_softwaredeployment_TdMachine)
gen_cwm_xml_TdXMLElement_Element = Generalization(general=Element, specific=cwm_xml_TdXMLElement)

# Domain Model
domain_model = DomainModel(
    name="cwm",
    types={cwm_relational_TdTable, Table, cwm_relational_TdView, View, cwm_relational_TdCatalog, Catalog, cwm_relational_TdSchema, Schema, cwm_relational_TdColumn, Column, TdSqlDataType, cwm_relational_TdSqlDataType, SQLSimpleType, cwm_relational_TdTrigger, Trigger, cwm_relational_TdProcedure, Procedure, cwm_softwaredeployment_TdProviderConnection, ProviderConnection, cwm_softwaredeployment_TdDataManager, DataManager, cwm_softwaredeployment_TdDataProvider, DataProvider, xml_cwm_EObject, TdXMLDocument, TdXMLContent, cwm_xml_TdXMLContent, Content, TdXMLElement, cwm_xml_TdXMLDocument, Document, cwm_softwaredeployment_TdSoftwareSystem, SoftwareSystem, cwm_softwaredeployment_TdMachine, Machine, cwm_xml_TdXMLElement, Element, DevelopmentStatus},
    associations={sqlDataType0, xsdElementDeclaration1, ownedDocument2, xmlContent4, xmlElements6},
    generalizations={gen_cwm_relational_TdTable_Table, gen_cwm_relational_TdView_View, gen_cwm_relational_TdCatalog_Catalog, gen_cwm_relational_TdSchema_Schema, gen_cwm_relational_TdSqlDataType_SQLSimpleType, gen_cwm_relational_TdTrigger_Trigger, gen_cwm_relational_TdProcedure_Procedure, gen_cwm_softwaredeployment_TdProviderConnection_ProviderConnection, gen_cwm_softwaredeployment_TdDataManager_DataManager, gen_cwm_softwaredeployment_TdDataProvider_DataProvider, gen_cwm_relational_TdColumn_Column, gen_cwm_xml_TdXMLContent_Content, gen_cwm_xml_TdXMLDocument_Document, gen_cwm_softwaredeployment_TdSoftwareSystem_SoftwareSystem, gen_cwm_softwaredeployment_TdMachine_Machine, gen_cwm_xml_TdXMLElement_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)