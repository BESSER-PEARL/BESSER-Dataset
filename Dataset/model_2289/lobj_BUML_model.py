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
lobj_LearningObject = Class(name="lobj::LearningObject", is_abstract=True)
lobj_HypertextContent = Class(name="lobj::HypertextContent")
lobj_Block = Class(name="lobj::Block", is_abstract=True)
LearningObject = Class(name="LearningObject")
lobj_BlockMeta = Class(name="lobj::BlockMeta")
lobj_ExternalMetadata = Class(name="lobj::ExternalMetadata")
lobj_AccessControl = Class(name="lobj::AccessControl")
lobj_HypertextBlock = Class(name="lobj::HypertextBlock")
Block = Class(name="Block")
lobj_BlockAudiofile = Class(name="lobj::BlockAudiofile")
lobj_AbstractContent = Class(name="lobj::AbstractContent", is_abstract=True)
lobj_Language = Class(name="lobj::Language")
lobj_Source = Class(name="lobj::Source")
AbstractContent = Class(name="AbstractContent")
lobj_ResrcFile = Class(name="lobj::ResrcFile")
lobj_BlockFolder = Class(name="lobj::BlockFolder")
lobj_FolderMeta = Class(name="lobj::FolderMeta")
lobj_Course = Class(name="lobj::Course")
lobj_Category = Class(name="lobj::Category")
lobj_TitleMeta = Class(name="lobj::TitleMeta")
lobj_CorrBlock = Class(name="lobj::CorrBlock")
lobj_PresentationBlock = Class(name="lobj::PresentationBlock")
lobj_Coursetype = Class(name="lobj::Coursetype")
lobj_CourseMeta = Class(name="lobj::CourseMeta")
lobj_Module = Class(name="lobj::Module")
lobj_Item = Class(name="lobj::Item")
lobj_LearningUnit = Class(name="lobj::LearningUnit")
lobj_LuMeta = Class(name="lobj::LuMeta")
lobj_LuFolder = Class(name="lobj::LuFolder")
lobj_ModuleMeta = Class(name="lobj::ModuleMeta")
lobj_ResrcFolder = Class(name="lobj::ResrcFolder")
lobj_Node = Class(name="lobj::Node", is_abstract=True)
lobj_ModuleFolder = Class(name="lobj::ModuleFolder")
lobj_Theme = Class(name="lobj::Theme")
lobj_SimpleDidacMeta = Class(name="lobj::SimpleDidacMeta")
lobj_ThemeNode = Class(name="lobj::ThemeNode")
Node = Class(name="Node")
lobj_LuNode = Class(name="lobj::LuNode")
lobj_ResrcFiletype = Class(name="lobj::ResrcFiletype")
lobj_ResrcMeta = Class(name="lobj::ResrcMeta")
lobj_User = Class(name="lobj::User")
lobj_Sharednotes = Class(name="lobj::Sharednotes")
lobj_Userauthorization = Class(name="lobj::Userauthorization")
lobj_Edition = Class(name="lobj::Edition")
lobj_Address = Class(name="lobj::Address")
lobj_Affiliation = Class(name="lobj::Affiliation")
lobj_Author = Class(name="lobj::Author")
lobj_Person = Class(name="lobj::Person")
lobj_Blocktype = Class(name="lobj::Blocktype")
lobj_Domain = Class(name="lobj::Domain")
lobj_DidacMeta = Class(name="lobj::DidacMeta")
SimpleDidacMeta = Class(name="SimpleDidacMeta")
lobj_Precognition = Class(name="lobj::Precognition")
lobj_PublishInfo = Class(name="lobj::PublishInfo")
lobj_AuthorizationTypes = Class(name="lobj::AuthorizationTypes")
lobj_Note = Class(name="lobj::Note")
lobj_Publisher = Class(name="lobj::Publisher")
lobj_InternalRef = Class(name="lobj::InternalRef")

# lobj_LearningObject class attributes and methods
lobj_LearningObject_timestamp: Property = Property(name="timestamp", type=DateType)
lobj_LearningObject_synchronized: Property = Property(name="synchronized", type=BooleanType)
lobj_LearningObject_id: Property = Property(name="id", type=StringType)
lobj_LearningObject.attributes={lobj_LearningObject_synchronized, lobj_LearningObject_timestamp, lobj_LearningObject_id}

# lobj_HypertextContent class attributes and methods
lobj_HypertextContent_content: Property = Property(name="content", type=StringType)
lobj_HypertextContent.attributes={lobj_HypertextContent_content}

# lobj_Block class attributes and methods

# LearningObject class attributes and methods

# lobj_BlockMeta class attributes and methods
lobj_BlockMeta_lod: Property = Property(name="lod", type=StringType)
lobj_BlockMeta_rendering: Property = Property(name="rendering", type=StringType)
lobj_BlockMeta_creationDate: Property = Property(name="creationDate", type=DateType)
lobj_BlockMeta_lastModified: Property = Property(name="lastModified", type=DateType)
lobj_BlockMeta.attributes={lobj_BlockMeta_lod, lobj_BlockMeta_creationDate, lobj_BlockMeta_rendering, lobj_BlockMeta_lastModified}

# lobj_ExternalMetadata class attributes and methods
lobj_ExternalMetadata_ref: Property = Property(name="ref", type=StringType)
lobj_ExternalMetadata_file: Property = Property(name="file", type=StringType)
lobj_ExternalMetadata_id: Property = Property(name="id", type=StringType)
lobj_ExternalMetadata.attributes={lobj_ExternalMetadata_ref, lobj_ExternalMetadata_id, lobj_ExternalMetadata_file}

# lobj_AccessControl class attributes and methods
lobj_AccessControl_lastStatusChange: Property = Property(name="lastStatusChange", type=DateType)
lobj_AccessControl_lastModified: Property = Property(name="lastModified", type=DateType)
lobj_AccessControl_status: Property = Property(name="status", type=StringType)
lobj_AccessControl_globalAccess: Property = Property(name="globalAccess", type=BooleanType)
lobj_AccessControl_id: Property = Property(name="id", type=StringType)
lobj_AccessControl.attributes={lobj_AccessControl_status, lobj_AccessControl_lastModified, lobj_AccessControl_globalAccess, lobj_AccessControl_lastStatusChange, lobj_AccessControl_id}

# lobj_HypertextBlock class attributes and methods

# Block class attributes and methods

# lobj_BlockAudiofile class attributes and methods
lobj_BlockAudiofile_originalextension: Property = Property(name="originalextension", type=StringType)
lobj_BlockAudiofile_filesize: Property = Property(name="filesize", type=IntegerType)
lobj_BlockAudiofile_resrcHref: Property = Property(name="resrcHref", type=StringType)
lobj_BlockAudiofile_file: Property = Property(name="file", type=StringType)
lobj_BlockAudiofile.attributes={lobj_BlockAudiofile_originalextension, lobj_BlockAudiofile_filesize, lobj_BlockAudiofile_resrcHref, lobj_BlockAudiofile_file}

# lobj_AbstractContent class attributes and methods
lobj_AbstractContent_heading: Property = Property(name="heading", type=StringType)
lobj_AbstractContent.attributes={lobj_AbstractContent_heading}

# lobj_Language class attributes and methods
lobj_Language_language: Property = Property(name="language", type=StringType)
lobj_Language_code: Property = Property(name="code", type=StringType)
lobj_Language.attributes={lobj_Language_language, lobj_Language_code}

# lobj_Source class attributes and methods
lobj_Source_title: Property = Property(name="title", type=StringType)
lobj_Source_subtitle: Property = Property(name="subtitle", type=StringType)
lobj_Source_publishedIn: Property = Property(name="publishedIn", type=StringType)
lobj_Source_publishedBy: Property = Property(name="publishedBy", type=StringType)
lobj_Source_publishDate: Property = Property(name="publishDate", type=StringType)
lobj_Source_pp: Property = Property(name="pp", type=StringType)
lobj_Source_id: Property = Property(name="id", type=StringType)
lobj_Source.attributes={lobj_Source_publishedBy, lobj_Source_id, lobj_Source_publishedIn, lobj_Source_publishDate, lobj_Source_pp, lobj_Source_subtitle, lobj_Source_title}

# AbstractContent class attributes and methods

# lobj_ResrcFile class attributes and methods
lobj_ResrcFile_filesize: Property = Property(name="filesize", type=IntegerType)
lobj_ResrcFile_resrcHref: Property = Property(name="resrcHref", type=StringType)
lobj_ResrcFile_file: Property = Property(name="file", type=StringType)
lobj_ResrcFile_file_tn: Property = Property(name="file_tn", type=StringType)
lobj_ResrcFile_originalextension: Property = Property(name="originalextension", type=StringType)
lobj_ResrcFile.attributes={lobj_ResrcFile_resrcHref, lobj_ResrcFile_originalextension, lobj_ResrcFile_file, lobj_ResrcFile_filesize, lobj_ResrcFile_file_tn}

# lobj_BlockFolder class attributes and methods

# lobj_FolderMeta class attributes and methods
lobj_FolderMeta_title: Property = Property(name="title", type=StringType)
lobj_FolderMeta_description: Property = Property(name="description", type=StringType)
lobj_FolderMeta_creationDate: Property = Property(name="creationDate", type=DateType)
lobj_FolderMeta.attributes={lobj_FolderMeta_description, lobj_FolderMeta_creationDate, lobj_FolderMeta_title}

# lobj_Course class attributes and methods
lobj_Course_outlineAsXml: Property = Property(name="outlineAsXml", type=StringType)
lobj_Course.attributes={lobj_Course_outlineAsXml}

# lobj_Category class attributes and methods

# lobj_TitleMeta class attributes and methods
lobj_TitleMeta_title: Property = Property(name="title", type=StringType)
lobj_TitleMeta_id: Property = Property(name="id", type=StringType)
lobj_TitleMeta.attributes={lobj_TitleMeta_title, lobj_TitleMeta_id}

# lobj_CorrBlock class attributes and methods
lobj_CorrBlock_id: Property = Property(name="id", type=StringType)
lobj_CorrBlock.attributes={lobj_CorrBlock_id}

# lobj_PresentationBlock class attributes and methods
lobj_PresentationBlock_id: Property = Property(name="id", type=StringType)
lobj_PresentationBlock_lod: Property = Property(name="lod", type=IntegerType)
lobj_PresentationBlock_rendering: Property = Property(name="rendering", type=StringType)
lobj_PresentationBlock.attributes={lobj_PresentationBlock_rendering, lobj_PresentationBlock_id, lobj_PresentationBlock_lod}

# lobj_Coursetype class attributes and methods
lobj_Coursetype_id: Property = Property(name="id", type=StringType)
lobj_Coursetype_title: Property = Property(name="title", type=StringType)
lobj_Coursetype_description: Property = Property(name="description", type=StringType)
lobj_Coursetype.attributes={lobj_Coursetype_description, lobj_Coursetype_title, lobj_Coursetype_id}

# lobj_CourseMeta class attributes and methods
lobj_CourseMeta_fromext: Property = Property(name="fromext", type=StringType)
lobj_CourseMeta_hours: Property = Property(name="hours", type=IntegerType)
lobj_CourseMeta_lvanr: Property = Property(name="lvanr", type=StringType)
lobj_CourseMeta_columnfilterasxml: Property = Property(name="columnfilterasxml", type=StringType)
lobj_CourseMeta_creationDate: Property = Property(name="creationDate", type=DateType)
lobj_CourseMeta.attributes={lobj_CourseMeta_columnfilterasxml, lobj_CourseMeta_hours, lobj_CourseMeta_lvanr, lobj_CourseMeta_creationDate, lobj_CourseMeta_fromext}

# lobj_Module class attributes and methods
lobj_Module_moduleFile: Property = Property(name="moduleFile", type=StringType)
lobj_Module_treeAsXml: Property = Property(name="treeAsXml", type=StringType)
lobj_Module.attributes={lobj_Module_moduleFile, lobj_Module_treeAsXml}

# lobj_Item class attributes and methods
lobj_Item_luRef: Property = Property(name="luRef", type=StringType)
lobj_Item_id: Property = Property(name="id", type=StringType)
lobj_Item.attributes={lobj_Item_id, lobj_Item_luRef}

# lobj_LearningUnit class attributes and methods
lobj_LearningUnit_treeAsXml: Property = Property(name="treeAsXml", type=StringType)
lobj_LearningUnit_luFile: Property = Property(name="luFile", type=StringType)
lobj_LearningUnit.attributes={lobj_LearningUnit_luFile, lobj_LearningUnit_treeAsXml}

# lobj_LuMeta class attributes and methods
lobj_LuMeta_creationDate: Property = Property(name="creationDate", type=DateType)
lobj_LuMeta.attributes={lobj_LuMeta_creationDate}

# lobj_LuFolder class attributes and methods

# lobj_ModuleMeta class attributes and methods
lobj_ModuleMeta_creationDate: Property = Property(name="creationDate", type=DateType)
lobj_ModuleMeta.attributes={lobj_ModuleMeta_creationDate}

# lobj_ResrcFolder class attributes and methods
lobj_ResrcFolder_deleteScheduled: Property = Property(name="deleteScheduled", type=BooleanType)
lobj_ResrcFolder.attributes={lobj_ResrcFolder_deleteScheduled}

# lobj_Node class attributes and methods
lobj_Node_visible: Property = Property(name="visible", type=BooleanType)
lobj_Node_id: Property = Property(name="id", type=StringType)
lobj_Node.attributes={lobj_Node_id, lobj_Node_visible}

# lobj_ModuleFolder class attributes and methods

# lobj_Theme class attributes and methods

# lobj_SimpleDidacMeta class attributes and methods
lobj_SimpleDidacMeta_id: Property = Property(name="id", type=StringType)
lobj_SimpleDidacMeta_title: Property = Property(name="title", type=StringType)
lobj_SimpleDidacMeta_description: Property = Property(name="description", type=StringType)
lobj_SimpleDidacMeta_keywords: Property = Property(name="keywords", type=StringType)
lobj_SimpleDidacMeta.attributes={lobj_SimpleDidacMeta_keywords, lobj_SimpleDidacMeta_description, lobj_SimpleDidacMeta_title, lobj_SimpleDidacMeta_id}

# lobj_ThemeNode class attributes and methods

# Node class attributes and methods

# lobj_LuNode class attributes and methods

# lobj_ResrcFiletype class attributes and methods
lobj_ResrcFiletype_filetypeExtension: Property = Property(name="filetypeExtension", type=StringType)
lobj_ResrcFiletype_filetypeDesc: Property = Property(name="filetypeDesc", type=StringType)
lobj_ResrcFiletype_image: Property = Property(name="image", type=BooleanType)
lobj_ResrcFiletype_applet: Property = Property(name="applet", type=BooleanType)
lobj_ResrcFiletype_filetypeImageSmall: Property = Property(name="filetypeImageSmall", type=StringType)
lobj_ResrcFiletype_filetypeImageBif: Property = Property(name="filetypeImageBif", type=StringType)
lobj_ResrcFiletype_id: Property = Property(name="id", type=StringType)
lobj_ResrcFiletype.attributes={lobj_ResrcFiletype_filetypeDesc, lobj_ResrcFiletype_filetypeImageBif, lobj_ResrcFiletype_id, lobj_ResrcFiletype_applet, lobj_ResrcFiletype_filetypeExtension, lobj_ResrcFiletype_filetypeImageSmall, lobj_ResrcFiletype_image}

# lobj_ResrcMeta class attributes and methods
lobj_ResrcMeta_filename: Property = Property(name="filename", type=StringType)
lobj_ResrcMeta_parameters: Property = Property(name="parameters", type=StringType)
lobj_ResrcMeta_height: Property = Property(name="height", type=IntegerType)
lobj_ResrcMeta_width: Property = Property(name="width", type=IntegerType)
lobj_ResrcMeta_creationDate: Property = Property(name="creationDate", type=DateType)
lobj_ResrcMeta_lastModified: Property = Property(name="lastModified", type=DateType)
lobj_ResrcMeta_title: Property = Property(name="title", type=StringType)
lobj_ResrcMeta_description: Property = Property(name="description", type=StringType)
lobj_ResrcMeta_keywords: Property = Property(name="keywords", type=StringType)
lobj_ResrcMeta.attributes={lobj_ResrcMeta_description, lobj_ResrcMeta_parameters, lobj_ResrcMeta_creationDate, lobj_ResrcMeta_lastModified, lobj_ResrcMeta_title, lobj_ResrcMeta_filename, lobj_ResrcMeta_keywords, lobj_ResrcMeta_height, lobj_ResrcMeta_width}

# lobj_User class attributes and methods
lobj_User_entryasxml: Property = Property(name="entryasxml", type=StringType)
lobj_User_languagenr: Property = Property(name="languagenr", type=StringType)
lobj_User_notificationprofileasxml: Property = Property(name="notificationprofileasxml", type=StringType)
lobj_User_loginname: Property = Property(name="loginname", type=StringType)
lobj_User_password: Property = Property(name="password", type=StringType)
lobj_User_firstname: Property = Property(name="firstname", type=StringType)
lobj_User_lastname: Property = Property(name="lastname", type=StringType)
lobj_User_matriculationnr: Property = Property(name="matriculationnr", type=StringType)
lobj_User_scn: Property = Property(name="scn", type=StringType)
lobj_User_icqnumber: Property = Property(name="icqnumber", type=StringType)
lobj_User_icqpassword: Property = Property(name="icqpassword", type=StringType)
lobj_User_id: Property = Property(name="id", type=StringType)
lobj_User_dossierasxml: Property = Property(name="dossierasxml", type=StringType)
lobj_User_photo: Property = Property(name="photo", type=StringType)
lobj_User_onlinestatus: Property = Property(name="onlinestatus", type=StringType)
lobj_User_onlinedate: Property = Property(name="onlinedate", type=DateType)
lobj_User_datafilter: Property = Property(name="datafilter", type=StringType)
lobj_User_inchatsince: Property = Property(name="inchatsince", type=DateType)
lobj_User_contchatdate: Property = Property(name="contchatdate", type=DateType)
lobj_User_chatroomnr: Property = Property(name="chatroomnr", type=StringType)
lobj_User_fromext: Property = Property(name="fromext", type=StringType)
lobj_User_lastlogindate: Property = Property(name="lastlogindate", type=DateType)
lobj_User_currlogindate: Property = Property(name="currlogindate", type=DateType)
lobj_User_lastcoursematerialnr: Property = Property(name="lastcoursematerialnr", type=StringType)
lobj_User_lastcoursematerialviewnr: Property = Property(name="lastcoursematerialviewnr", type=StringType)
lobj_User_authenticateldap: Property = Property(name="authenticateldap", type=StringType)
lobj_User_photochanged: Property = Property(name="photochanged", type=StringType)
lobj_User.attributes={lobj_User_languagenr, lobj_User_currlogindate, lobj_User_photochanged, lobj_User_lastname, lobj_User_fromext, lobj_User_scn, lobj_User_datafilter, lobj_User_firstname, lobj_User_icqnumber, lobj_User_onlinestatus, lobj_User_lastcoursematerialviewnr, lobj_User_dossierasxml, lobj_User_notificationprofileasxml, lobj_User_authenticateldap, lobj_User_loginname, lobj_User_matriculationnr, lobj_User_photo, lobj_User_icqpassword, lobj_User_id, lobj_User_onlinedate, lobj_User_lastcoursematerialnr, lobj_User_entryasxml, lobj_User_contchatdate, lobj_User_inchatsince, lobj_User_password, lobj_User_lastlogindate, lobj_User_chatroomnr}

# lobj_Sharednotes class attributes and methods
lobj_Sharednotes_id: Property = Property(name="id", type=StringType)
lobj_Sharednotes.attributes={lobj_Sharednotes_id}

# lobj_Userauthorization class attributes and methods
lobj_Userauthorization_id: Property = Property(name="id", type=StringType)
lobj_Userauthorization.attributes={lobj_Userauthorization_id}

# lobj_Edition class attributes and methods
lobj_Edition_status: Property = Property(name="status", type=StringType)
lobj_Edition_editionCreationDate: Property = Property(name="editionCreationDate", type=DateType)
lobj_Edition_editionNr: Property = Property(name="editionNr", type=StringType)
lobj_Edition_editedBy: Property = Property(name="editedBy", type=StringType)
lobj_Edition_version: Property = Property(name="version", type=StringType)
lobj_Edition_lastVersionNumber: Property = Property(name="lastVersionNumber", type=StringType)
lobj_Edition_id: Property = Property(name="id", type=StringType)
lobj_Edition.attributes={lobj_Edition_editionCreationDate, lobj_Edition_version, lobj_Edition_editedBy, lobj_Edition_lastVersionNumber, lobj_Edition_status, lobj_Edition_id, lobj_Edition_editionNr}

# lobj_Address class attributes and methods
lobj_Address_fax: Property = Property(name="fax", type=StringType)
lobj_Address_email: Property = Property(name="email", type=StringType)
lobj_Address_otheraddr: Property = Property(name="otheraddr", type=StringType)
lobj_Address_street: Property = Property(name="street", type=StringType)
lobj_Address_postcode: Property = Property(name="postcode", type=StringType)
lobj_Address_city: Property = Property(name="city", type=StringType)
lobj_Address_state: Property = Property(name="state", type=StringType)
lobj_Address_country: Property = Property(name="country", type=StringType)
lobj_Address_phone: Property = Property(name="phone", type=StringType)
lobj_Address_id: Property = Property(name="id", type=StringType)
lobj_Address.attributes={lobj_Address_fax, lobj_Address_street, lobj_Address_city, lobj_Address_email, lobj_Address_postcode, lobj_Address_otheraddr, lobj_Address_id, lobj_Address_country, lobj_Address_state, lobj_Address_phone}

# lobj_Affiliation class attributes and methods
lobj_Affiliation_shortaffil: Property = Property(name="shortaffil", type=StringType)
lobj_Affiliation_jobtitle: Property = Property(name="jobtitle", type=StringType)
lobj_Affiliation_orgname: Property = Property(name="orgname", type=StringType)
lobj_Affiliation_orgdiv: Property = Property(name="orgdiv", type=StringType)
lobj_Affiliation_id: Property = Property(name="id", type=StringType)
lobj_Affiliation.attributes={lobj_Affiliation_orgname, lobj_Affiliation_id, lobj_Affiliation_jobtitle, lobj_Affiliation_orgdiv, lobj_Affiliation_shortaffil}

# lobj_Author class attributes and methods
lobj_Author_id: Property = Property(name="id", type=StringType)
lobj_Author_credittype: Property = Property(name="credittype", type=StringType)
lobj_Author_email: Property = Property(name="email", type=StringType)
lobj_Author.attributes={lobj_Author_credittype, lobj_Author_email, lobj_Author_id}

# lobj_Person class attributes and methods
lobj_Person_contrib: Property = Property(name="contrib", type=StringType)
lobj_Person_honorific: Property = Property(name="honorific", type=StringType)
lobj_Person_firstname: Property = Property(name="firstname", type=StringType)
lobj_Person_surname: Property = Property(name="surname", type=StringType)
lobj_Person_personblurb: Property = Property(name="personblurb", type=StringType)
lobj_Person_id: Property = Property(name="id", type=StringType)
lobj_Person.attributes={lobj_Person_firstname, lobj_Person_id, lobj_Person_contrib, lobj_Person_surname, lobj_Person_honorific, lobj_Person_personblurb}

# lobj_Blocktype class attributes and methods
lobj_Blocktype_description: Property = Property(name="description", type=StringType)
lobj_Blocktype_creationDate: Property = Property(name="creationDate", type=DateType)
lobj_Blocktype_name: Property = Property(name="name", type=StringType)
lobj_Blocktype_styleRef: Property = Property(name="styleRef", type=StringType)
lobj_Blocktype_id: Property = Property(name="id", type=StringType)
lobj_Blocktype.attributes={lobj_Blocktype_styleRef, lobj_Blocktype_creationDate, lobj_Blocktype_id, lobj_Blocktype_name, lobj_Blocktype_description}

# lobj_Domain class attributes and methods
lobj_Domain_name: Property = Property(name="name", type=StringType)
lobj_Domain_description: Property = Property(name="description", type=StringType)
lobj_Domain_creationDate: Property = Property(name="creationDate", type=DateType)
lobj_Domain_serverURL: Property = Property(name="serverURL", type=StringType)
lobj_Domain_id: Property = Property(name="id", type=StringType)
lobj_Domain.attributes={lobj_Domain_description, lobj_Domain_creationDate, lobj_Domain_id, lobj_Domain_name, lobj_Domain_serverURL}

# lobj_DidacMeta class attributes and methods
lobj_DidacMeta_goal: Property = Property(name="goal", type=StringType)
lobj_DidacMeta.attributes={lobj_DidacMeta_goal}

# SimpleDidacMeta class attributes and methods

# lobj_Precognition class attributes and methods
lobj_Precognition_precog: Property = Property(name="precog", type=StringType)
lobj_Precognition_id: Property = Property(name="id", type=StringType)
lobj_Precognition.attributes={lobj_Precognition_id, lobj_Precognition_precog}

# lobj_PublishInfo class attributes and methods
lobj_PublishInfo_id: Property = Property(name="id", type=StringType)
lobj_PublishInfo_edition: Property = Property(name="edition", type=StringType)
lobj_PublishInfo_pubdate: Property = Property(name="pubdate", type=DateType)
lobj_PublishInfo_pubsnumber: Property = Property(name="pubsnumber", type=StringType)
lobj_PublishInfo_releaseinfo: Property = Property(name="releaseinfo", type=StringType)
lobj_PublishInfo.attributes={lobj_PublishInfo_releaseinfo, lobj_PublishInfo_id, lobj_PublishInfo_pubsnumber, lobj_PublishInfo_pubdate, lobj_PublishInfo_edition}

# lobj_AuthorizationTypes class attributes and methods
lobj_AuthorizationTypes_authType: Property = Property(name="authType", type=StringType)
lobj_AuthorizationTypes_authTypeDesc: Property = Property(name="authTypeDesc", type=StringType)
lobj_AuthorizationTypes_readOnly: Property = Property(name="readOnly", type=BooleanType)
lobj_AuthorizationTypes_id: Property = Property(name="id", type=StringType)
lobj_AuthorizationTypes.attributes={lobj_AuthorizationTypes_authTypeDesc, lobj_AuthorizationTypes_authType, lobj_AuthorizationTypes_id, lobj_AuthorizationTypes_readOnly}

# lobj_Note class attributes and methods
lobj_Note_date: Property = Property(name="date", type=DateType)
lobj_Note_noteAuthor: Property = Property(name="noteAuthor", type=StringType)
lobj_Note_content: Property = Property(name="content", type=StringType)
lobj_Note_id: Property = Property(name="id", type=StringType)
lobj_Note.attributes={lobj_Note_noteAuthor, lobj_Note_id, lobj_Note_content, lobj_Note_date}

# lobj_Publisher class attributes and methods
lobj_Publisher_publishername: Property = Property(name="publishername", type=StringType)
lobj_Publisher_id: Property = Property(name="id", type=StringType)
lobj_Publisher.attributes={lobj_Publisher_id, lobj_Publisher_publishername}

# lobj_InternalRef class attributes and methods
lobj_InternalRef_ref: Property = Property(name="ref", type=StringType)
lobj_InternalRef_file: Property = Property(name="file", type=StringType)
lobj_InternalRef_reftype: Property = Property(name="reftype", type=StringType)
lobj_InternalRef_id: Property = Property(name="id", type=StringType)
lobj_InternalRef.attributes={lobj_InternalRef_file, lobj_InternalRef_reftype, lobj_InternalRef_id, lobj_InternalRef_ref}

# Relationships
hypertextContent5: BinaryAssociation = BinaryAssociation(
    name="hypertextContent5",
    ends={
        Property(name="lobj_HypertextContent", type=lobj_HypertextBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_HypertextBlock", type=lobj_HypertextContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blockMeta0: BinaryAssociation = BinaryAssociation(
    name="blockMeta0",
    ends={
        Property(name="lobj_BlockMeta", type=lobj_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Block", type=lobj_BlockMeta, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
externalMetadata1: BinaryAssociation = BinaryAssociation(
    name="externalMetadata1",
    ends={
        Property(name="lobj_ExternalMetadata", type=lobj_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Block2", type=lobj_ExternalMetadata, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accessControl3: BinaryAssociation = BinaryAssociation(
    name="accessControl3",
    ends={
        Property(name="lobj_AccessControl", type=lobj_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Block4", type=lobj_AccessControl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blockAudiofile9: BinaryAssociation = BinaryAssociation(
    name="blockAudiofile9",
    ends={
        Property(name="lobj_BlockAudiofile", type=lobj_HypertextContent, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_HypertextContent10", type=lobj_BlockAudiofile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
language6: BinaryAssociation = BinaryAssociation(
    name="language6",
    ends={
        Property(name="lobj_Language", type=lobj_AbstractContent, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_AbstractContent", type=lobj_Language, multiplicity=Multiplicity(0, 1))
    }
)
source7: BinaryAssociation = BinaryAssociation(
    name="source7",
    ends={
        Property(name="lobj_Source", type=lobj_AbstractContent, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_AbstractContent8", type=lobj_Source, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
folderMeta12: BinaryAssociation = BinaryAssociation(
    name="folderMeta12",
    ends={
        Property(name="lobj_BlockFolder", type=lobj_FolderMeta, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="lobj_FolderMeta", type=lobj_BlockFolder, multiplicity=Multiplicity(1, 1))
    }
)
resrcFile11: BinaryAssociation = BinaryAssociation(
    name="resrcFile11",
    ends={
        Property(name="ResrcFile", type=lobj_HypertextContent, multiplicity=Multiplicity(1, 1)),
        Property(name="hypertextContent", type=lobj_ResrcFile, multiplicity=Multiplicity(0, 9999))
    }
)
blockFolder14: BinaryAssociation = BinaryAssociation(
    name="blockFolder14",
    ends={
        Property(name="lobj_BlockFolder15", type=lobj_BlockFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_BlockFolder13", type=lobj_BlockFolder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block16: BinaryAssociation = BinaryAssociation(
    name="block16",
    ends={
        Property(name="lobj_Block18", type=lobj_BlockFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_BlockFolder17", type=lobj_Block, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accessControl19: BinaryAssociation = BinaryAssociation(
    name="accessControl19",
    ends={
        Property(name="lobj_AccessControl21", type=lobj_BlockFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_BlockFolder20", type=lobj_AccessControl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
titleMeta22: BinaryAssociation = BinaryAssociation(
    name="titleMeta22",
    ends={
        Property(name="lobj_TitleMeta", type=lobj_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Category", type=lobj_TitleMeta, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
course23: BinaryAssociation = BinaryAssociation(
    name="course23",
    ends={
        Property(name="lobj_Course", type=lobj_Category, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Category24", type=lobj_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
presentationBlock25: BinaryAssociation = BinaryAssociation(
    name="presentationBlock25",
    ends={
        Property(name="lobj_PresentationBlock", type=lobj_CorrBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_CorrBlock", type=lobj_PresentationBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
titleMeta26: BinaryAssociation = BinaryAssociation(
    name="titleMeta26",
    ends={
        Property(name="lobj_TitleMeta28", type=lobj_CorrBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_CorrBlock27", type=lobj_TitleMeta, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
coursetype34: BinaryAssociation = BinaryAssociation(
    name="coursetype34",
    ends={
        Property(name="lobj_Coursetype", type=lobj_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Course35", type=lobj_Coursetype, multiplicity=Multiplicity(0, 1))
    }
)
courseMeta29: BinaryAssociation = BinaryAssociation(
    name="courseMeta29",
    ends={
        Property(name="lobj_CourseMeta", type=lobj_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Course30", type=lobj_CourseMeta, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
externalMetadata31: BinaryAssociation = BinaryAssociation(
    name="externalMetadata31",
    ends={
        Property(name="lobj_ExternalMetadata33", type=lobj_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Course32", type=lobj_ExternalMetadata, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module36: BinaryAssociation = BinaryAssociation(
    name="module36",
    ends={
        Property(name="lobj_Module", type=lobj_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Course37", type=lobj_Module, multiplicity=Multiplicity(0, 9999))
    }
)
corrBlock38: BinaryAssociation = BinaryAssociation(
    name="corrBlock38",
    ends={
        Property(name="lobj_CorrBlock39", type=lobj_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Item", type=lobj_CorrBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childitems41: BinaryAssociation = BinaryAssociation(
    name="childitems41",
    ends={
        Property(name="lobj_Item42", type=lobj_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Item40", type=lobj_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
luMeta43: BinaryAssociation = BinaryAssociation(
    name="luMeta43",
    ends={
        Property(name="lobj_LuMeta", type=lobj_LearningUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_LearningUnit", type=lobj_LuMeta, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
externalMetadata44: BinaryAssociation = BinaryAssociation(
    name="externalMetadata44",
    ends={
        Property(name="lobj_ExternalMetadata46", type=lobj_LearningUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_LearningUnit45", type=lobj_ExternalMetadata, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
externalMetadata66: BinaryAssociation = BinaryAssociation(
    name="externalMetadata66",
    ends={
        Property(name="lobj_ExternalMetadata68", type=lobj_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Module67", type=lobj_ExternalMetadata, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accessControl47: BinaryAssociation = BinaryAssociation(
    name="accessControl47",
    ends={
        Property(name="lobj_AccessControl49", type=lobj_LearningUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_LearningUnit48", type=lobj_AccessControl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
item50: BinaryAssociation = BinaryAssociation(
    name="item50",
    ends={
        Property(name="lobj_Item52", type=lobj_LearningUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_LearningUnit51", type=lobj_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
folderMeta53: BinaryAssociation = BinaryAssociation(
    name="folderMeta53",
    ends={
        Property(name="lobj_FolderMeta54", type=lobj_LuFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_LuFolder", type=lobj_FolderMeta, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
luFolder56: BinaryAssociation = BinaryAssociation(
    name="luFolder56",
    ends={
        Property(name="lobj_LuFolder57", type=lobj_LuFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_LuFolder55", type=lobj_LuFolder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
learningUnit58: BinaryAssociation = BinaryAssociation(
    name="learningUnit58",
    ends={
        Property(name="lobj_LearningUnit60", type=lobj_LuFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_LuFolder59", type=lobj_LearningUnit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accessControl61: BinaryAssociation = BinaryAssociation(
    name="accessControl61",
    ends={
        Property(name="lobj_AccessControl63", type=lobj_LuFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_LuFolder62", type=lobj_AccessControl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
moduleMeta64: BinaryAssociation = BinaryAssociation(
    name="moduleMeta64",
    ends={
        Property(name="lobj_ModuleMeta", type=lobj_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Module65", type=lobj_ModuleMeta, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
folderMeta85: BinaryAssociation = BinaryAssociation(
    name="folderMeta85",
    ends={
        Property(name="lobj_FolderMeta86", type=lobj_ResrcFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_ResrcFolder", type=lobj_FolderMeta, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rootNode69: BinaryAssociation = BinaryAssociation(
    name="rootNode69",
    ends={
        Property(name="lobj_Node", type=lobj_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Module70", type=lobj_Node, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
accessControl71: BinaryAssociation = BinaryAssociation(
    name="accessControl71",
    ends={
        Property(name="lobj_AccessControl73", type=lobj_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Module72", type=lobj_AccessControl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
folderMeta74: BinaryAssociation = BinaryAssociation(
    name="folderMeta74",
    ends={
        Property(name="lobj_FolderMeta75", type=lobj_ModuleFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_ModuleFolder", type=lobj_FolderMeta, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
moduleFolder77: BinaryAssociation = BinaryAssociation(
    name="moduleFolder77",
    ends={
        Property(name="lobj_ModuleFolder78", type=lobj_ModuleFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_ModuleFolder76", type=lobj_ModuleFolder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
module79: BinaryAssociation = BinaryAssociation(
    name="module79",
    ends={
        Property(name="lobj_Module81", type=lobj_ModuleFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_ModuleFolder80", type=lobj_Module, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accessControl82: BinaryAssociation = BinaryAssociation(
    name="accessControl82",
    ends={
        Property(name="lobj_AccessControl84", type=lobj_ModuleFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_ModuleFolder83", type=lobj_AccessControl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resrcFolder88: BinaryAssociation = BinaryAssociation(
    name="resrcFolder88",
    ends={
        Property(name="lobj_ResrcFolder89", type=lobj_ResrcFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_ResrcFolder87", type=lobj_ResrcFolder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accessControl90: BinaryAssociation = BinaryAssociation(
    name="accessControl90",
    ends={
        Property(name="lobj_AccessControl92", type=lobj_ResrcFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_ResrcFolder91", type=lobj_AccessControl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resrcFile93: BinaryAssociation = BinaryAssociation(
    name="resrcFile93",
    ends={
        Property(name="lobj_ResrcFile", type=lobj_ResrcFolder, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_ResrcFolder94", type=lobj_ResrcFile, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simpleDidacMeta95: BinaryAssociation = BinaryAssociation(
    name="simpleDidacMeta95",
    ends={
        Property(name="lobj_SimpleDidacMeta", type=lobj_Theme, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Theme", type=lobj_SimpleDidacMeta, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block96: BinaryAssociation = BinaryAssociation(
    name="block96",
    ends={
        Property(name="lobj_Block98", type=lobj_PresentationBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_PresentationBlock97", type=lobj_Block, multiplicity=Multiplicity(0, 1))
    }
)
theme99: BinaryAssociation = BinaryAssociation(
    name="theme99",
    ends={
        Property(name="lobj_Theme100", type=lobj_ThemeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_ThemeNode", type=lobj_Theme, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
childnodes101: BinaryAssociation = BinaryAssociation(
    name="childnodes101",
    ends={
        Property(name="lobj_Node103", type=lobj_ThemeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_ThemeNode102", type=lobj_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
learningUnit104: BinaryAssociation = BinaryAssociation(
    name="learningUnit104",
    ends={
        Property(name="lobj_LearningUnit105", type=lobj_LuNode, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_LuNode", type=lobj_LearningUnit, multiplicity=Multiplicity(0, 1))
    }
)
accesscontrol106: BinaryAssociation = BinaryAssociation(
    name="accesscontrol106",
    ends={
        Property(name="lobj_AccessControl108", type=lobj_ResrcFile, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_ResrcFile107", type=lobj_AccessControl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resrcFiletype109: BinaryAssociation = BinaryAssociation(
    name="resrcFiletype109",
    ends={
        Property(name="lobj_ResrcFiletype", type=lobj_ResrcFile, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_ResrcFile110", type=lobj_ResrcFiletype, multiplicity=Multiplicity(0, 1))
    }
)
source111: BinaryAssociation = BinaryAssociation(
    name="source111",
    ends={
        Property(name="lobj_Source113", type=lobj_ResrcFile, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_ResrcFile112", type=lobj_Source, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hypertextContent114: BinaryAssociation = BinaryAssociation(
    name="hypertextContent114",
    ends={
        Property(name="HypertextContent", type=lobj_ResrcFile, multiplicity=Multiplicity(1, 1)),
        Property(name="resrcFile", type=lobj_HypertextContent, multiplicity=Multiplicity(0, 9999))
    }
)
resrcMeta115: BinaryAssociation = BinaryAssociation(
    name="resrcMeta115",
    ends={
        Property(name="lobj_ResrcMeta", type=lobj_ResrcFile, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_ResrcFile116", type=lobj_ResrcMeta, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lastStatusChangeBy125: BinaryAssociation = BinaryAssociation(
    name="lastStatusChangeBy125",
    ends={
        Property(name="lobj_User127", type=lobj_AccessControl, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_AccessControl126", type=lobj_User, multiplicity=Multiplicity(0, 1))
    }
)
resrcFiletype117: BinaryAssociation = BinaryAssociation(
    name="resrcFiletype117",
    ends={
        Property(name="lobj_ResrcFiletype119", type=lobj_BlockAudiofile, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_BlockAudiofile118", type=lobj_ResrcFiletype, multiplicity=Multiplicity(0, 1))
    }
)
owner120: BinaryAssociation = BinaryAssociation(
    name="owner120",
    ends={
        Property(name="lobj_User", type=lobj_AccessControl, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_AccessControl121", type=lobj_User, multiplicity=Multiplicity(0, 1))
    }
)
lastModifiedBy122: BinaryAssociation = BinaryAssociation(
    name="lastModifiedBy122",
    ends={
        Property(name="lobj_User124", type=lobj_AccessControl, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_AccessControl123", type=lobj_User, multiplicity=Multiplicity(0, 1))
    }
)
sharednotes128: BinaryAssociation = BinaryAssociation(
    name="sharednotes128",
    ends={
        Property(name="lobj_Sharednotes", type=lobj_AccessControl, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_AccessControl129", type=lobj_Sharednotes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
authorizes130: BinaryAssociation = BinaryAssociation(
    name="authorizes130",
    ends={
        Property(name="lobj_Userauthorization", type=lobj_AccessControl, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_AccessControl131", type=lobj_Userauthorization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
editionHistory132: BinaryAssociation = BinaryAssociation(
    name="editionHistory132",
    ends={
        Property(name="lobj_Edition", type=lobj_AccessControl, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_AccessControl133", type=lobj_Edition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
address134: BinaryAssociation = BinaryAssociation(
    name="address134",
    ends={
        Property(name="lobj_Address", type=lobj_Affiliation, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Affiliation", type=lobj_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
person135: BinaryAssociation = BinaryAssociation(
    name="person135",
    ends={
        Property(name="lobj_Person", type=lobj_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Author", type=lobj_Person, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
address136: BinaryAssociation = BinaryAssociation(
    name="address136",
    ends={
        Property(name="lobj_Address138", type=lobj_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Author137", type=lobj_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blocktype139: BinaryAssociation = BinaryAssociation(
    name="blocktype139",
    ends={
        Property(name="lobj_Blocktype", type=lobj_BlockMeta, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_BlockMeta140", type=lobj_Blocktype, multiplicity=Multiplicity(0, 1))
    }
)
simpleDidacMeta141: BinaryAssociation = BinaryAssociation(
    name="simpleDidacMeta141",
    ends={
        Property(name="lobj_SimpleDidacMeta143", type=lobj_BlockMeta, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_BlockMeta142", type=lobj_SimpleDidacMeta, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defLang144: BinaryAssociation = BinaryAssociation(
    name="defLang144",
    ends={
        Property(name="lobj_Language146", type=lobj_BlockMeta, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_BlockMeta145", type=lobj_Language, multiplicity=Multiplicity(0, 1))
    }
)
language148: BinaryAssociation = BinaryAssociation(
    name="language148",
    ends={
        Property(name="lobj_Language150", type=lobj_TitleMeta, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_TitleMeta149", type=lobj_Language, multiplicity=Multiplicity(0, 1))
    }
)
domains147: BinaryAssociation = BinaryAssociation(
    name="domains147",
    ends={
        Property(name="Domain", type=lobj_Blocktype, multiplicity=Multiplicity(1, 1)),
        Property(name="blocktypes", type=lobj_Domain, multiplicity=Multiplicity(0, 9999))
    }
)
didacMeta151: BinaryAssociation = BinaryAssociation(
    name="didacMeta151",
    ends={
        Property(name="lobj_DidacMeta", type=lobj_CourseMeta, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_CourseMeta152", type=lobj_DidacMeta, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lecturer153: BinaryAssociation = BinaryAssociation(
    name="lecturer153",
    ends={
        Property(name="lobj_User155", type=lobj_CourseMeta, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_CourseMeta154", type=lobj_User, multiplicity=Multiplicity(0, 1))
    }
)
defLang156: BinaryAssociation = BinaryAssociation(
    name="defLang156",
    ends={
        Property(name="lobj_Language158", type=lobj_CourseMeta, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_CourseMeta157", type=lobj_Language, multiplicity=Multiplicity(0, 1))
    }
)
language159: BinaryAssociation = BinaryAssociation(
    name="language159",
    ends={
        Property(name="lobj_Language161", type=lobj_SimpleDidacMeta, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_SimpleDidacMeta160", type=lobj_Language, multiplicity=Multiplicity(0, 1))
    }
)
precognition162: BinaryAssociation = BinaryAssociation(
    name="precognition162",
    ends={
        Property(name="lobj_Precognition", type=lobj_DidacMeta, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_DidacMeta163", type=lobj_Precognition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blocktypes164: BinaryAssociation = BinaryAssociation(
    name="blocktypes164",
    ends={
        Property(name="Blocktype", type=lobj_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="domains", type=lobj_Blocktype, multiplicity=Multiplicity(0, 9999))
    }
)
defLang175: BinaryAssociation = BinaryAssociation(
    name="defLang175",
    ends={
        Property(name="lobj_Language177", type=lobj_LuMeta, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_LuMeta176", type=lobj_Language, multiplicity=Multiplicity(0, 1))
    }
)
didacMeta165: BinaryAssociation = BinaryAssociation(
    name="didacMeta165",
    ends={
        Property(name="lobj_DidacMeta167", type=lobj_LuMeta, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_LuMeta166", type=lobj_DidacMeta, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domain168: BinaryAssociation = BinaryAssociation(
    name="domain168",
    ends={
        Property(name="lobj_Domain", type=lobj_LuMeta, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_LuMeta169", type=lobj_Domain, multiplicity=Multiplicity(0, 1))
    }
)
authors170: BinaryAssociation = BinaryAssociation(
    name="authors170",
    ends={
        Property(name="lobj_Author172", type=lobj_LuMeta, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_LuMeta171", type=lobj_Author, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
publishInfo173: BinaryAssociation = BinaryAssociation(
    name="publishInfo173",
    ends={
        Property(name="lobj_PublishInfo", type=lobj_LuMeta, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_LuMeta174", type=lobj_PublishInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
affiliations183: BinaryAssociation = BinaryAssociation(
    name="affiliations183",
    ends={
        Property(name="lobj_Affiliation185", type=lobj_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Person184", type=lobj_Affiliation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
user178: BinaryAssociation = BinaryAssociation(
    name="user178",
    ends={
        Property(name="lobj_User180", type=lobj_Userauthorization, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Userauthorization179", type=lobj_User, multiplicity=Multiplicity(0, 1))
    }
)
authType181: BinaryAssociation = BinaryAssociation(
    name="authType181",
    ends={
        Property(name="lobj_AuthorizationTypes", type=lobj_Userauthorization, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Userauthorization182", type=lobj_AuthorizationTypes, multiplicity=Multiplicity(0, 1))
    }
)
address186: BinaryAssociation = BinaryAssociation(
    name="address186",
    ends={
        Property(name="lobj_Address187", type=lobj_Publisher, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Publisher", type=lobj_Address, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
publisher188: BinaryAssociation = BinaryAssociation(
    name="publisher188",
    ends={
        Property(name="lobj_Publisher190", type=lobj_PublishInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_PublishInfo189", type=lobj_Publisher, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
notes191: BinaryAssociation = BinaryAssociation(
    name="notes191",
    ends={
        Property(name="lobj_Note", type=lobj_Sharednotes, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Sharednotes192", type=lobj_Note, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
language193: BinaryAssociation = BinaryAssociation(
    name="language193",
    ends={
        Property(name="lobj_Language195", type=lobj_Coursetype, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Coursetype194", type=lobj_Language, multiplicity=Multiplicity(0, 1))
    }
)
didacMeta201: BinaryAssociation = BinaryAssociation(
    name="didacMeta201",
    ends={
        Property(name="lobj_DidacMeta203", type=lobj_ModuleMeta, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_ModuleMeta202", type=lobj_DidacMeta, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
internalRefs196: BinaryAssociation = BinaryAssociation(
    name="internalRefs196",
    ends={
        Property(name="lobj_InternalRef", type=lobj_Precognition, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Precognition197", type=lobj_InternalRef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
language198: BinaryAssociation = BinaryAssociation(
    name="language198",
    ends={
        Property(name="lobj_Language200", type=lobj_InternalRef, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_InternalRef199", type=lobj_Language, multiplicity=Multiplicity(0, 1))
    }
)
authors204: BinaryAssociation = BinaryAssociation(
    name="authors204",
    ends={
        Property(name="lobj_Author206", type=lobj_ModuleMeta, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_ModuleMeta205", type=lobj_Author, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
publishInfo207: BinaryAssociation = BinaryAssociation(
    name="publishInfo207",
    ends={
        Property(name="lobj_PublishInfo209", type=lobj_ModuleMeta, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_ModuleMeta208", type=lobj_PublishInfo, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defLang210: BinaryAssociation = BinaryAssociation(
    name="defLang210",
    ends={
        Property(name="lobj_Language212", type=lobj_ModuleMeta, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_ModuleMeta211", type=lobj_Language, multiplicity=Multiplicity(0, 1))
    }
)
author213: BinaryAssociation = BinaryAssociation(
    name="author213",
    ends={
        Property(name="lobj_Author215", type=lobj_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_Source214", type=lobj_Author, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
authorizations216: BinaryAssociation = BinaryAssociation(
    name="authorizations216",
    ends={
        Property(name="lobj_AuthorizationTypes218", type=lobj_User, multiplicity=Multiplicity(1, 1)),
        Property(name="lobj_User217", type=lobj_AuthorizationTypes, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_lobj_Block_LearningObject = Generalization(general=LearningObject, specific=lobj_Block)
gen_lobj_HypertextBlock_Block = Generalization(general=Block, specific=lobj_HypertextBlock)
gen_lobj_AbstractContent_LearningObject = Generalization(general=LearningObject, specific=lobj_AbstractContent)
gen_lobj_HypertextContent_AbstractContent = Generalization(general=AbstractContent, specific=lobj_HypertextContent)
gen_lobj_BlockFolder_LearningObject = Generalization(general=LearningObject, specific=lobj_BlockFolder)
gen_lobj_Category_LearningObject = Generalization(general=LearningObject, specific=lobj_Category)
gen_lobj_Course_LearningObject = Generalization(general=LearningObject, specific=lobj_Course)
gen_lobj_LearningUnit_LearningObject = Generalization(general=LearningObject, specific=lobj_LearningUnit)
gen_lobj_LuFolder_LearningObject = Generalization(general=LearningObject, specific=lobj_LuFolder)
gen_lobj_Module_LearningObject = Generalization(general=LearningObject, specific=lobj_Module)
gen_lobj_ResrcFolder_LearningObject = Generalization(general=LearningObject, specific=lobj_ResrcFolder)
gen_lobj_ModuleFolder_LearningObject = Generalization(general=LearningObject, specific=lobj_ModuleFolder)
gen_lobj_Theme_LearningObject = Generalization(general=LearningObject, specific=lobj_Theme)
gen_lobj_ThemeNode_Node = Generalization(general=Node, specific=lobj_ThemeNode)
gen_lobj_LuNode_Node = Generalization(general=Node, specific=lobj_LuNode)
gen_lobj_ResrcFile_LearningObject = Generalization(general=LearningObject, specific=lobj_ResrcFile)
gen_lobj_BlockAudiofile_LearningObject = Generalization(general=LearningObject, specific=lobj_BlockAudiofile)
gen_lobj_BlockMeta_LearningObject = Generalization(general=LearningObject, specific=lobj_BlockMeta)
gen_lobj_CourseMeta_LearningObject = Generalization(general=LearningObject, specific=lobj_CourseMeta)
gen_lobj_DidacMeta_SimpleDidacMeta = Generalization(general=SimpleDidacMeta, specific=lobj_DidacMeta)
gen_lobj_FolderMeta_LearningObject = Generalization(general=LearningObject, specific=lobj_FolderMeta)
gen_lobj_LuMeta_LearningObject = Generalization(general=LearningObject, specific=lobj_LuMeta)
gen_lobj_ResrcMeta_LearningObject = Generalization(general=LearningObject, specific=lobj_ResrcMeta)
gen_lobj_ModuleMeta_LearningObject = Generalization(general=LearningObject, specific=lobj_ModuleMeta)

# Domain Model
domain_model = DomainModel(
    name="lobj",
    types={lobj_LearningObject, lobj_HypertextContent, lobj_Block, LearningObject, lobj_BlockMeta, lobj_ExternalMetadata, lobj_AccessControl, lobj_HypertextBlock, Block, lobj_BlockAudiofile, lobj_AbstractContent, lobj_Language, lobj_Source, AbstractContent, lobj_ResrcFile, lobj_BlockFolder, lobj_FolderMeta, lobj_Course, lobj_Category, lobj_TitleMeta, lobj_CorrBlock, lobj_PresentationBlock, lobj_Coursetype, lobj_CourseMeta, lobj_Module, lobj_Item, lobj_LearningUnit, lobj_LuMeta, lobj_LuFolder, lobj_ModuleMeta, lobj_ResrcFolder, lobj_Node, lobj_ModuleFolder, lobj_Theme, lobj_SimpleDidacMeta, lobj_ThemeNode, Node, lobj_LuNode, lobj_ResrcFiletype, lobj_ResrcMeta, lobj_User, lobj_Sharednotes, lobj_Userauthorization, lobj_Edition, lobj_Address, lobj_Affiliation, lobj_Author, lobj_Person, lobj_Blocktype, lobj_Domain, lobj_DidacMeta, SimpleDidacMeta, lobj_Precognition, lobj_PublishInfo, lobj_AuthorizationTypes, lobj_Note, lobj_Publisher, lobj_InternalRef},
    associations={hypertextContent5, blockMeta0, externalMetadata1, accessControl3, blockAudiofile9, language6, source7, folderMeta12, resrcFile11, blockFolder14, block16, accessControl19, titleMeta22, course23, presentationBlock25, titleMeta26, coursetype34, courseMeta29, externalMetadata31, module36, corrBlock38, childitems41, luMeta43, externalMetadata44, externalMetadata66, accessControl47, item50, folderMeta53, luFolder56, learningUnit58, accessControl61, moduleMeta64, folderMeta85, rootNode69, accessControl71, folderMeta74, moduleFolder77, module79, accessControl82, resrcFolder88, accessControl90, resrcFile93, simpleDidacMeta95, block96, theme99, childnodes101, learningUnit104, accesscontrol106, resrcFiletype109, source111, hypertextContent114, resrcMeta115, lastStatusChangeBy125, resrcFiletype117, owner120, lastModifiedBy122, sharednotes128, authorizes130, editionHistory132, address134, person135, address136, blocktype139, simpleDidacMeta141, defLang144, language148, domains147, didacMeta151, lecturer153, defLang156, language159, precognition162, blocktypes164, defLang175, didacMeta165, domain168, authors170, publishInfo173, affiliations183, user178, authType181, address186, publisher188, notes191, language193, didacMeta201, internalRefs196, language198, authors204, publishInfo207, defLang210, author213, authorizations216},
    generalizations={gen_lobj_Block_LearningObject, gen_lobj_HypertextBlock_Block, gen_lobj_AbstractContent_LearningObject, gen_lobj_HypertextContent_AbstractContent, gen_lobj_BlockFolder_LearningObject, gen_lobj_Category_LearningObject, gen_lobj_Course_LearningObject, gen_lobj_LearningUnit_LearningObject, gen_lobj_LuFolder_LearningObject, gen_lobj_Module_LearningObject, gen_lobj_ResrcFolder_LearningObject, gen_lobj_ModuleFolder_LearningObject, gen_lobj_Theme_LearningObject, gen_lobj_ThemeNode_Node, gen_lobj_LuNode_Node, gen_lobj_ResrcFile_LearningObject, gen_lobj_BlockAudiofile_LearningObject, gen_lobj_BlockMeta_LearningObject, gen_lobj_CourseMeta_LearningObject, gen_lobj_DidacMeta_SimpleDidacMeta, gen_lobj_FolderMeta_LearningObject, gen_lobj_LuMeta_LearningObject, gen_lobj_ResrcMeta_LearningObject, gen_lobj_ModuleMeta_LearningObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)