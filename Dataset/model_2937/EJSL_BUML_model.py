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
PluginKinds: Enumeration = Enumeration(
    name="PluginKinds",
    literals={
            EnumerationLiteral(name="authenticate"),
			EnumerationLiteral(name="captcha"),
			EnumerationLiteral(name="content"),
			EnumerationLiteral(name="contact"),
			EnumerationLiteral(name="editors"),
			EnumerationLiteral(name="extensions"),
			EnumerationLiteral(name="finder"),
			EnumerationLiteral(name="quick_icons"),
			EnumerationLiteral(name="search"),
			EnumerationLiteral(name="system"),
			EnumerationLiteral(name="user"),
			EnumerationLiteral(name="xml_rpc")
    }
)

PageActionKind: Enumeration = Enumeration(
    name="PageActionKind",
    literals={
            EnumerationLiteral(name="SAVE"),
			EnumerationLiteral(name="NEW"),
			EnumerationLiteral(name="SAVE_CLOSE"),
			EnumerationLiteral(name="SAVE_COPY"),
			EnumerationLiteral(name="CANCEL"),
			EnumerationLiteral(name="CLOSE"),
			EnumerationLiteral(name="ARCHIVE"),
			EnumerationLiteral(name="EDIT"),
			EnumerationLiteral(name="PUBLISH"),
			EnumerationLiteral(name="UNPUBLISH"),
			EnumerationLiteral(name="HIDE"),
			EnumerationLiteral(name="CHECKIN"),
			EnumerationLiteral(name="TRASH"),
			EnumerationLiteral(name="INDIVIDUAL"),
			EnumerationLiteral(name="LOGIN"),
			EnumerationLiteral(name="PWRESET")
    }
)

PageActionPositionKind: Enumeration = Enumeration(
    name="PageActionPositionKind",
    literals={
            EnumerationLiteral(name="top"),
			EnumerationLiteral(name="center"),
			EnumerationLiteral(name="bottom")
    }
)

StandardTypeKinds: Enumeration = Enumeration(
    name="StandardTypeKinds",
    literals={
            EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="Text"),
			EnumerationLiteral(name="Short_Text"),
			EnumerationLiteral(name="Time"),
			EnumerationLiteral(name="Date"),
			EnumerationLiteral(name="Datetime"),
			EnumerationLiteral(name="Link"),
			EnumerationLiteral(name="Image"),
			EnumerationLiteral(name="File"),
			EnumerationLiteral(name="Label"),
			EnumerationLiteral(name="Encrypted_Text")
    }
)

DataAccessKinds: Enumeration = Enumeration(
    name="DataAccessKinds",
    literals={
            EnumerationLiteral(name="backendDAO"),
			EnumerationLiteral(name="frontendDAO"),
			EnumerationLiteral(name="database"),
			EnumerationLiteral(name="webservice")
    }
)

SimpleHTMLTypeKinds: Enumeration = Enumeration(
    name="SimpleHTMLTypeKinds",
    literals={
            EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Yes_No_Buttons"),
			EnumerationLiteral(name="Textarea"),
			EnumerationLiteral(name="Text_Field"),
			EnumerationLiteral(name="Link"),
			EnumerationLiteral(name="Datepicker"),
			EnumerationLiteral(name="Imagepicker"),
			EnumerationLiteral(name="Filepicker"),
			EnumerationLiteral(name="Text_Field_NE"),
			EnumerationLiteral(name="Editor")
    }
)

ComplexHTMLTypeKinds: Enumeration = Enumeration(
    name="ComplexHTMLTypeKinds",
    literals={
            EnumerationLiteral(name="Select"),
			EnumerationLiteral(name="Multiselect"),
			EnumerationLiteral(name="Checkbox"),
			EnumerationLiteral(name="Radiobutton")
    }
)

CoreComponent: Enumeration = Enumeration(
    name="CoreComponent",
    literals={
            EnumerationLiteral(name="User"),
			EnumerationLiteral(name="Menu"),
			EnumerationLiteral(name="Content")
    }
)

PageKinds: Enumeration = Enumeration(
    name="PageKinds",
    literals={
            EnumerationLiteral(name="custom"),
			EnumerationLiteral(name="list"),
			EnumerationLiteral(name="details")
    }
)

# Classes
eJSL_EJSLModel = Class(name="eJSL::EJSLModel")
eJSL_EJSLPart = Class(name="eJSL::EJSLPart")
eJSL_Datatype = Class(name="eJSL::Datatype")
eJSL_Parameter = Class(name="eJSL::Parameter")
eJSL_ParameterGroup = Class(name="eJSL::ParameterGroup")
eJSL_Feature = Class(name="eJSL::Feature")
eJSL_CMSCore = Class(name="eJSL::CMSCore")
eJSL_Page = Class(name="eJSL::Page")
eJSL_Section = Class(name="eJSL::Section")
eJSL_Type = Class(name="eJSL::Type")
eJSL_DatatypeReference = Class(name="eJSL::DatatypeReference")
Type = Class(name="Type")
HTMLTypes = Class(name="HTMLTypes")
eJSL_StandardTypes = Class(name="eJSL::StandardTypes")
eJSL_HTMLTypes = Class(name="eJSL::HTMLTypes")
eJSL_KeyValuePair = Class(name="eJSL::KeyValuePair")
EJSLPart = Class(name="EJSLPart")
eJSL_coreFeature = Class(name="eJSL::coreFeature")
eJSL_CMSExtension = Class(name="eJSL::CMSExtension")
eJSL_Extension = Class(name="eJSL::Extension")
eJSL_Entitypackage = Class(name="eJSL::Entitypackage")
eJSL_Entity = Class(name="eJSL::Entity")
eJSL_Attribute = Class(name="eJSL::Attribute")
eJSL_Reference = Class(name="eJSL::Reference")
eJSL_PageAction = Class(name="eJSL::PageAction")
eJSL_Link = Class(name="eJSL::Link")
eJSL_StaticPage = Class(name="eJSL::StaticPage")
Page = Class(name="Page")
eJSL_DynamicPage = Class(name="eJSL::DynamicPage")
eJSL_IndexPage = Class(name="eJSL::IndexPage")
DynamicPage = Class(name="DynamicPage")
eJSL_DetailsPage = Class(name="eJSL::DetailsPage")
eJSL_DetailPageField = Class(name="eJSL::DetailPageField")
eJSL_CustomPage = Class(name="eJSL::CustomPage")
eJSL_SimpleHTMLTypes = Class(name="eJSL::SimpleHTMLTypes")
eJSL_ComplexHTMLTypes = Class(name="eJSL::ComplexHTMLTypes")
eJSL_ExternalLink = Class(name="eJSL::ExternalLink")
Link = Class(name="Link")
eJSL_InternalLink = Class(name="eJSL::InternalLink")
eJSL_ContextLink = Class(name="eJSL::ContextLink")
InternalLink = Class(name="InternalLink")
eJSL_LinkParameter = Class(name="eJSL::LinkParameter")
eJSL_Manifestation = Class(name="eJSL::Manifestation")
eJSL_Language = Class(name="eJSL::Language")
eJSL_ExtensionPackage = Class(name="eJSL::ExtensionPackage")
Extension = Class(name="Extension")
eJSL_Component = Class(name="eJSL::Component")
eJSL_PageReference = Class(name="eJSL::PageReference")
eJSL_BackendSection = Class(name="eJSL::BackendSection")
Section = Class(name="Section")
eJSL_FrontendSection = Class(name="eJSL::FrontendSection")
eJSL_Module = Class(name="eJSL::Module")
eJSL_Plugin = Class(name="eJSL::Plugin")
eJSL_Library = Class(name="eJSL::Library")
eJSL_Class = Class(name="eJSL::Class")
eJSL_Package = Class(name="eJSL::Package")
eJSL_Method = Class(name="eJSL::Method")
eJSL_ComponentReference = Class(name="eJSL::ComponentReference")
eJSL_MethodParameter = Class(name="eJSL::MethodParameter")
eJSL_Template = Class(name="eJSL::Template")
eJSL_Position = Class(name="eJSL::Position")
eJSL_CssBlock = Class(name="eJSL::CssBlock")
eJSL_Author = Class(name="eJSL::Author")
eJSL_PositionParameter = Class(name="eJSL::PositionParameter")

# eJSL_EJSLModel class attributes and methods
eJSL_EJSLModel_name: Property = Property(name="name", type=StringType)
eJSL_EJSLModel.attributes={eJSL_EJSLModel_name}

# eJSL_EJSLPart class attributes and methods

# eJSL_Datatype class attributes and methods
eJSL_Datatype_name: Property = Property(name="name", type=StringType)
eJSL_Datatype_type: Property = Property(name="type", type=StringType)
eJSL_Datatype.attributes={eJSL_Datatype_name, eJSL_Datatype_type}

# eJSL_Parameter class attributes and methods
eJSL_Parameter_name: Property = Property(name="name", type=StringType)
eJSL_Parameter_defaultvalue: Property = Property(name="defaultvalue", type=StringType)
eJSL_Parameter_label: Property = Property(name="label", type=StringType)
eJSL_Parameter_size: Property = Property(name="size", type=IntegerType)
eJSL_Parameter_descripton: Property = Property(name="descripton", type=StringType)
eJSL_Parameter.attributes={eJSL_Parameter_size, eJSL_Parameter_name, eJSL_Parameter_defaultvalue, eJSL_Parameter_descripton, eJSL_Parameter_label}

# eJSL_ParameterGroup class attributes and methods
eJSL_ParameterGroup_name: Property = Property(name="name", type=StringType)
eJSL_ParameterGroup_label: Property = Property(name="label", type=StringType)
eJSL_ParameterGroup.attributes={eJSL_ParameterGroup_label, eJSL_ParameterGroup_name}

# eJSL_Feature class attributes and methods

# eJSL_CMSCore class attributes and methods

# eJSL_Page class attributes and methods
eJSL_Page_name: Property = Property(name="name", type=StringType)
eJSL_Page.attributes={eJSL_Page_name}

# eJSL_Section class attributes and methods

# eJSL_Type class attributes and methods

# eJSL_DatatypeReference class attributes and methods

# Type class attributes and methods

# HTMLTypes class attributes and methods

# eJSL_StandardTypes class attributes and methods
eJSL_StandardTypes_type: Property = Property(name="type", type=StringType)
eJSL_StandardTypes_notnull: Property = Property(name="notnull", type=BooleanType)
eJSL_StandardTypes_default: Property = Property(name="default", type=StringType)
eJSL_StandardTypes_autoincrement: Property = Property(name="autoincrement", type=BooleanType)
eJSL_StandardTypes.attributes={eJSL_StandardTypes_notnull, eJSL_StandardTypes_type, eJSL_StandardTypes_default, eJSL_StandardTypes_autoincrement}

# eJSL_HTMLTypes class attributes and methods

# eJSL_KeyValuePair class attributes and methods
eJSL_KeyValuePair_name: Property = Property(name="name", type=StringType)
eJSL_KeyValuePair_value: Property = Property(name="value", type=StringType)
eJSL_KeyValuePair.attributes={eJSL_KeyValuePair_value, eJSL_KeyValuePair_name}

# EJSLPart class attributes and methods

# eJSL_coreFeature class attributes and methods

# eJSL_CMSExtension class attributes and methods

# eJSL_Extension class attributes and methods
eJSL_Extension_name: Property = Property(name="name", type=StringType)
eJSL_Extension.attributes={eJSL_Extension_name}

# eJSL_Entitypackage class attributes and methods
eJSL_Entitypackage_name: Property = Property(name="name", type=StringType)
eJSL_Entitypackage.attributes={eJSL_Entitypackage_name}

# eJSL_Entity class attributes and methods
eJSL_Entity_name: Property = Property(name="name", type=StringType)
eJSL_Entity_preserve: Property = Property(name="preserve", type=BooleanType)
eJSL_Entity.attributes={eJSL_Entity_preserve, eJSL_Entity_name}

# eJSL_Attribute class attributes and methods
eJSL_Attribute_name: Property = Property(name="name", type=StringType)
eJSL_Attribute_preserve: Property = Property(name="preserve", type=BooleanType)
eJSL_Attribute_isunique: Property = Property(name="isunique", type=BooleanType)
eJSL_Attribute_id: Property = Property(name="id", type=BooleanType)
eJSL_Attribute_isprimary: Property = Property(name="isprimary", type=BooleanType)
eJSL_Attribute.attributes={eJSL_Attribute_isprimary, eJSL_Attribute_preserve, eJSL_Attribute_isunique, eJSL_Attribute_id, eJSL_Attribute_name}

# eJSL_Reference class attributes and methods
eJSL_Reference_preserve: Property = Property(name="preserve", type=BooleanType)
eJSL_Reference_id: Property = Property(name="id", type=BooleanType)
eJSL_Reference_lower: Property = Property(name="lower", type=StringType)
eJSL_Reference_upper: Property = Property(name="upper", type=StringType)
eJSL_Reference.attributes={eJSL_Reference_lower, eJSL_Reference_id, eJSL_Reference_upper, eJSL_Reference_preserve}

# eJSL_PageAction class attributes and methods
eJSL_PageAction_name: Property = Property(name="name", type=StringType)
eJSL_PageAction_pageActionType: Property = Property(name="pageActionType", type=StringType)
eJSL_PageAction_pageActionPosition: Property = Property(name="pageActionPosition", type=StringType)
eJSL_PageAction.attributes={eJSL_PageAction_pageActionType, eJSL_PageAction_name, eJSL_PageAction_pageActionPosition}

# eJSL_Link class attributes and methods

# eJSL_StaticPage class attributes and methods
eJSL_StaticPage_preserve: Property = Property(name="preserve", type=BooleanType)
eJSL_StaticPage_HTMLBody: Property = Property(name="HTMLBody", type=StringType)
eJSL_StaticPage.attributes={eJSL_StaticPage_preserve, eJSL_StaticPage_HTMLBody}

# Page class attributes and methods

# eJSL_DynamicPage class attributes and methods
eJSL_DynamicPage_preserve: Property = Property(name="preserve", type=BooleanType)
eJSL_DynamicPage.attributes={eJSL_DynamicPage_preserve}

# eJSL_IndexPage class attributes and methods

# DynamicPage class attributes and methods

# eJSL_DetailsPage class attributes and methods

# eJSL_DetailPageField class attributes and methods

# eJSL_CustomPage class attributes and methods
eJSL_CustomPage_preserve: Property = Property(name="preserve", type=StringType)
eJSL_CustomPage_pageType: Property = Property(name="pageType", type=StringType)
eJSL_CustomPage.attributes={eJSL_CustomPage_preserve, eJSL_CustomPage_pageType}

# eJSL_SimpleHTMLTypes class attributes and methods
eJSL_SimpleHTMLTypes_htmltype: Property = Property(name="htmltype", type=StringType)
eJSL_SimpleHTMLTypes.attributes={eJSL_SimpleHTMLTypes_htmltype}

# eJSL_ComplexHTMLTypes class attributes and methods
eJSL_ComplexHTMLTypes_htmltype: Property = Property(name="htmltype", type=StringType)
eJSL_ComplexHTMLTypes.attributes={eJSL_ComplexHTMLTypes_htmltype}

# eJSL_ExternalLink class attributes and methods
eJSL_ExternalLink_target: Property = Property(name="target", type=StringType)
eJSL_ExternalLink_label: Property = Property(name="label", type=StringType)
eJSL_ExternalLink.attributes={eJSL_ExternalLink_label, eJSL_ExternalLink_target}

# Link class attributes and methods

# eJSL_InternalLink class attributes and methods
eJSL_InternalLink_name: Property = Property(name="name", type=StringType)
eJSL_InternalLink.attributes={eJSL_InternalLink_name}

# eJSL_ContextLink class attributes and methods

# InternalLink class attributes and methods

# eJSL_LinkParameter class attributes and methods
eJSL_LinkParameter_name: Property = Property(name="name", type=StringType)
eJSL_LinkParameter_id: Property = Property(name="id", type=BooleanType)
eJSL_LinkParameter_value: Property = Property(name="value", type=StringType)
eJSL_LinkParameter.attributes={eJSL_LinkParameter_name, eJSL_LinkParameter_value, eJSL_LinkParameter_id}

# eJSL_Manifestation class attributes and methods
eJSL_Manifestation_creationdate: Property = Property(name="creationdate", type=StringType)
eJSL_Manifestation_copyright: Property = Property(name="copyright", type=StringType)
eJSL_Manifestation_license: Property = Property(name="license", type=StringType)
eJSL_Manifestation_link: Property = Property(name="link", type=StringType)
eJSL_Manifestation_version: Property = Property(name="version", type=StringType)
eJSL_Manifestation_description: Property = Property(name="description", type=StringType)
eJSL_Manifestation.attributes={eJSL_Manifestation_license, eJSL_Manifestation_link, eJSL_Manifestation_copyright, eJSL_Manifestation_version, eJSL_Manifestation_creationdate, eJSL_Manifestation_description}

# eJSL_Language class attributes and methods
eJSL_Language_sys: Property = Property(name="sys", type=BooleanType)
eJSL_Language_name: Property = Property(name="name", type=StringType)
eJSL_Language.attributes={eJSL_Language_sys, eJSL_Language_name}

# eJSL_ExtensionPackage class attributes and methods

# Extension class attributes and methods

# eJSL_Component class attributes and methods

# eJSL_PageReference class attributes and methods
eJSL_PageReference_sect: Property = Property(name="sect", type=StringType)
eJSL_PageReference.attributes={eJSL_PageReference_sect}

# eJSL_BackendSection class attributes and methods

# Section class attributes and methods

# eJSL_FrontendSection class attributes and methods

# eJSL_Module class attributes and methods

# eJSL_Plugin class attributes and methods
eJSL_Plugin_type: Property = Property(name="type", type=StringType)
eJSL_Plugin.attributes={eJSL_Plugin_type}

# eJSL_Library class attributes and methods

# eJSL_Class class attributes and methods
eJSL_Class_name: Property = Property(name="name", type=StringType)
eJSL_Class.attributes={eJSL_Class_name}

# eJSL_Package class attributes and methods
eJSL_Package_name: Property = Property(name="name", type=StringType)
eJSL_Package.attributes={eJSL_Package_name}

# eJSL_Method class attributes and methods
eJSL_Method_name: Property = Property(name="name", type=StringType)
eJSL_Method_returnvalue: Property = Property(name="returnvalue", type=StringType)
eJSL_Method.attributes={eJSL_Method_name, eJSL_Method_returnvalue}

# eJSL_ComponentReference class attributes and methods
eJSL_ComponentReference_core: Property = Property(name="core", type=StringType)
eJSL_ComponentReference.attributes={eJSL_ComponentReference_core}

# eJSL_MethodParameter class attributes and methods
eJSL_MethodParameter_name: Property = Property(name="name", type=StringType)
eJSL_MethodParameter.attributes={eJSL_MethodParameter_name}

# eJSL_Template class attributes and methods

# eJSL_Position class attributes and methods
eJSL_Position_name: Property = Property(name="name", type=StringType)
eJSL_Position.attributes={eJSL_Position_name}

# eJSL_CssBlock class attributes and methods
eJSL_CssBlock_selector: Property = Property(name="selector", type=StringType)
eJSL_CssBlock.attributes={eJSL_CssBlock_selector}

# eJSL_Author class attributes and methods
eJSL_Author_name: Property = Property(name="name", type=StringType)
eJSL_Author_authoremail: Property = Property(name="authoremail", type=StringType)
eJSL_Author_authorurl: Property = Property(name="authorurl", type=StringType)
eJSL_Author.attributes={eJSL_Author_name, eJSL_Author_authoremail, eJSL_Author_authorurl}

# eJSL_PositionParameter class attributes and methods
eJSL_PositionParameter_name: Property = Property(name="name", type=StringType)
eJSL_PositionParameter_divid: Property = Property(name="divid", type=StringType)
eJSL_PositionParameter_type: Property = Property(name="type", type=StringType)
eJSL_PositionParameter.attributes={eJSL_PositionParameter_name, eJSL_PositionParameter_divid, eJSL_PositionParameter_type}

# Relationships
ejslPart0: BinaryAssociation = BinaryAssociation(
    name="ejslPart0",
    ends={
        Property(name="eJSL_EJSLPart", type=eJSL_EJSLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_EJSLModel", type=eJSL_EJSLPart, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
datatypes1: BinaryAssociation = BinaryAssociation(
    name="datatypes1",
    ends={
        Property(name="eJSL_Datatype", type=eJSL_EJSLPart, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_EJSLPart2", type=eJSL_Datatype, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalparameters3: BinaryAssociation = BinaryAssociation(
    name="globalparameters3",
    ends={
        Property(name="eJSL_Parameter", type=eJSL_EJSLPart, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_EJSLPart4", type=eJSL_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parametergroups5: BinaryAssociation = BinaryAssociation(
    name="parametergroups5",
    ends={
        Property(name="eJSL_ParameterGroup", type=eJSL_EJSLPart, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_EJSLPart6", type=eJSL_ParameterGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
feature7: BinaryAssociation = BinaryAssociation(
    name="feature7",
    ends={
        Property(name="eJSL_Feature", type=eJSL_EJSLPart, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_EJSLPart8", type=eJSL_Feature, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entities12: BinaryAssociation = BinaryAssociation(
    name="entities12",
    ends={
        Property(name="eJSL_Entity", type=eJSL_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Feature13", type=eJSL_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pages14: BinaryAssociation = BinaryAssociation(
    name="pages14",
    ends={
        Property(name="eJSL_Page", type=eJSL_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Feature15", type=eJSL_Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sections16: BinaryAssociation = BinaryAssociation(
    name="sections16",
    ends={
        Property(name="eJSL_Section", type=eJSL_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Feature17", type=eJSL_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type18: BinaryAssociation = BinaryAssociation(
    name="type18",
    ends={
        Property(name="eJSL_Datatype19", type=eJSL_DatatypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_DatatypeReference", type=eJSL_Datatype, multiplicity=Multiplicity(0, 1))
    }
)
dtype20: BinaryAssociation = BinaryAssociation(
    name="dtype20",
    ends={
        Property(name="eJSL_HTMLTypes", type=eJSL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Parameter21", type=eJSL_HTMLTypes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values22: BinaryAssociation = BinaryAssociation(
    name="values22",
    ends={
        Property(name="eJSL_KeyValuePair", type=eJSL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Parameter23", type=eJSL_KeyValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes24: BinaryAssociation = BinaryAssociation(
    name="attributes24",
    ends={
        Property(name="eJSL_KeyValuePair26", type=eJSL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Parameter25", type=eJSL_KeyValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalparameters27: BinaryAssociation = BinaryAssociation(
    name="globalparameters27",
    ends={
        Property(name="eJSL_Parameter29", type=eJSL_ParameterGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_ParameterGroup28", type=eJSL_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
parameters30: BinaryAssociation = BinaryAssociation(
    name="parameters30",
    ends={
        Property(name="eJSL_Parameter32", type=eJSL_ParameterGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_ParameterGroup31", type=eJSL_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensions9: BinaryAssociation = BinaryAssociation(
    name="extensions9",
    ends={
        Property(name="eJSL_Extension", type=eJSL_CMSExtension, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_CMSExtension", type=eJSL_Extension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entitypackages10: BinaryAssociation = BinaryAssociation(
    name="entitypackages10",
    ends={
        Property(name="eJSL_Entitypackage", type=eJSL_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Feature11", type=eJSL_Entitypackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entities36: BinaryAssociation = BinaryAssociation(
    name="entities36",
    ends={
        Property(name="eJSL_Entitypackage37", type=eJSL_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="eJSL_Entity38", type=eJSL_Entitypackage, multiplicity=Multiplicity(1, 1))
    }
)
datatypes39: BinaryAssociation = BinaryAssociation(
    name="datatypes39",
    ends={
        Property(name="eJSL_Datatype41", type=eJSL_Entitypackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Entitypackage40", type=eJSL_Datatype, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supertype43: BinaryAssociation = BinaryAssociation(
    name="supertype43",
    ends={
        Property(name="eJSL_Entity44", type=eJSL_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Entity42", type=eJSL_Entity, multiplicity=Multiplicity(0, 1))
    }
)
attributes45: BinaryAssociation = BinaryAssociation(
    name="attributes45",
    ends={
        Property(name="eJSL_Attribute", type=eJSL_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Entity46", type=eJSL_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references47: BinaryAssociation = BinaryAssociation(
    name="references47",
    ends={
        Property(name="eJSL_Reference", type=eJSL_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Entity48", type=eJSL_Reference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type49: BinaryAssociation = BinaryAssociation(
    name="type49",
    ends={
        Property(name="eJSL_Type", type=eJSL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Attribute50", type=eJSL_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
withattribute52: BinaryAssociation = BinaryAssociation(
    name="withattribute52",
    ends={
        Property(name="eJSL_Attribute53", type=eJSL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Attribute51", type=eJSL_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
attribute54: BinaryAssociation = BinaryAssociation(
    name="attribute54",
    ends={
        Property(name="eJSL_Attribute56", type=eJSL_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Reference55", type=eJSL_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
entity57: BinaryAssociation = BinaryAssociation(
    name="entity57",
    ends={
        Property(name="eJSL_Entity59", type=eJSL_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Reference58", type=eJSL_Entity, multiplicity=Multiplicity(0, 1))
    }
)
attributerefereced60: BinaryAssociation = BinaryAssociation(
    name="attributerefereced60",
    ends={
        Property(name="eJSL_Attribute62", type=eJSL_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Reference61", type=eJSL_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
parametergroups63: BinaryAssociation = BinaryAssociation(
    name="parametergroups63",
    ends={
        Property(name="eJSL_ParameterGroup65", type=eJSL_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Page64", type=eJSL_ParameterGroup, multiplicity=Multiplicity(0, 9999))
    }
)
globalparameters66: BinaryAssociation = BinaryAssociation(
    name="globalparameters66",
    ends={
        Property(name="eJSL_Parameter68", type=eJSL_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Page67", type=eJSL_Parameter, multiplicity=Multiplicity(0, 9999))
    }
)
entitypackages34: BinaryAssociation = BinaryAssociation(
    name="entitypackages34",
    ends={
        Property(name="eJSL_Entitypackage35", type=eJSL_Entitypackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Entitypackage33", type=eJSL_Entitypackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
links74: BinaryAssociation = BinaryAssociation(
    name="links74",
    ends={
        Property(name="eJSL_Link", type=eJSL_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Page75", type=eJSL_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entities76: BinaryAssociation = BinaryAssociation(
    name="entities76",
    ends={
        Property(name="eJSL_Entity77", type=eJSL_DynamicPage, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_DynamicPage", type=eJSL_Entity, multiplicity=Multiplicity(0, 9999))
    }
)
tablecolumns78: BinaryAssociation = BinaryAssociation(
    name="tablecolumns78",
    ends={
        Property(name="eJSL_Attribute80", type=eJSL_DynamicPage, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_DynamicPage79", type=eJSL_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
filters81: BinaryAssociation = BinaryAssociation(
    name="filters81",
    ends={
        Property(name="eJSL_Attribute83", type=eJSL_DynamicPage, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_DynamicPage82", type=eJSL_Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
editfields84: BinaryAssociation = BinaryAssociation(
    name="editfields84",
    ends={
        Property(name="eJSL_DetailPageField", type=eJSL_DetailsPage, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_DetailsPage", type=eJSL_DetailPageField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute85: BinaryAssociation = BinaryAssociation(
    name="attribute85",
    ends={
        Property(name="eJSL_Attribute87", type=eJSL_DetailPageField, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_DetailPageField86", type=eJSL_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
htmltype88: BinaryAssociation = BinaryAssociation(
    name="htmltype88",
    ends={
        Property(name="eJSL_HTMLTypes90", type=eJSL_DetailPageField, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_DetailPageField89", type=eJSL_HTMLTypes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
values91: BinaryAssociation = BinaryAssociation(
    name="values91",
    ends={
        Property(name="eJSL_KeyValuePair93", type=eJSL_DetailPageField, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_DetailPageField92", type=eJSL_KeyValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes94: BinaryAssociation = BinaryAssociation(
    name="attributes94",
    ends={
        Property(name="eJSL_KeyValuePair96", type=eJSL_DetailPageField, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_DetailPageField95", type=eJSL_KeyValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entities97: BinaryAssociation = BinaryAssociation(
    name="entities97",
    ends={
        Property(name="eJSL_Entity98", type=eJSL_CustomPage, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_CustomPage", type=eJSL_Entity, multiplicity=Multiplicity(0, 9999))
    }
)
localparameters69: BinaryAssociation = BinaryAssociation(
    name="localparameters69",
    ends={
        Property(name="eJSL_Parameter71", type=eJSL_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Page70", type=eJSL_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pageactions72: BinaryAssociation = BinaryAssociation(
    name="pageactions72",
    ends={
        Property(name="eJSL_PageAction", type=eJSL_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Page73", type=eJSL_PageAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
linkedAttribute99: BinaryAssociation = BinaryAssociation(
    name="linkedAttribute99",
    ends={
        Property(name="eJSL_Attribute101", type=eJSL_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Link100", type=eJSL_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
linkedAction102: BinaryAssociation = BinaryAssociation(
    name="linkedAction102",
    ends={
        Property(name="eJSL_PageAction104", type=eJSL_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Link103", type=eJSL_PageAction, multiplicity=Multiplicity(0, 1))
    }
)
target105: BinaryAssociation = BinaryAssociation(
    name="target105",
    ends={
        Property(name="eJSL_Page106", type=eJSL_InternalLink, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_InternalLink", type=eJSL_Page, multiplicity=Multiplicity(0, 1))
    }
)
linkparameters107: BinaryAssociation = BinaryAssociation(
    name="linkparameters107",
    ends={
        Property(name="eJSL_LinkParameter", type=eJSL_ContextLink, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_ContextLink", type=eJSL_LinkParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attvalue108: BinaryAssociation = BinaryAssociation(
    name="attvalue108",
    ends={
        Property(name="eJSL_Attribute110", type=eJSL_LinkParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_LinkParameter109", type=eJSL_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
manifest111: BinaryAssociation = BinaryAssociation(
    name="manifest111",
    ends={
        Property(name="eJSL_Manifestation", type=eJSL_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Extension112", type=eJSL_Manifestation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
languages113: BinaryAssociation = BinaryAssociation(
    name="languages113",
    ends={
        Property(name="eJSL_Language", type=eJSL_Extension, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Extension114", type=eJSL_Language, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensions115: BinaryAssociation = BinaryAssociation(
    name="extensions115",
    ends={
        Property(name="eJSL_Extension116", type=eJSL_ExtensionPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_ExtensionPackage", type=eJSL_Extension, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
globalParamter117: BinaryAssociation = BinaryAssociation(
    name="globalParamter117",
    ends={
        Property(name="eJSL_ParameterGroup118", type=eJSL_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Component", type=eJSL_ParameterGroup, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sections119: BinaryAssociation = BinaryAssociation(
    name="sections119",
    ends={
        Property(name="eJSL_Section121", type=eJSL_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Component120", type=eJSL_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pageRef122: BinaryAssociation = BinaryAssociation(
    name="pageRef122",
    ends={
        Property(name="eJSL_PageReference", type=eJSL_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Section123", type=eJSL_PageReference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref129: BinaryAssociation = BinaryAssociation(
    name="ref129",
    ends={
        Property(name="eJSL_Component131", type=eJSL_ComponentReference, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_ComponentReference130", type=eJSL_Component, multiplicity=Multiplicity(0, 1))
    }
)
pageRef132: BinaryAssociation = BinaryAssociation(
    name="pageRef132",
    ends={
        Property(name="eJSL_PageReference133", type=eJSL_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Module", type=eJSL_PageReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entities134: BinaryAssociation = BinaryAssociation(
    name="entities134",
    ends={
        Property(name="eJSL_Entity135", type=eJSL_Plugin, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Plugin", type=eJSL_Entity, multiplicity=Multiplicity(0, 9999))
    }
)
localparameters136: BinaryAssociation = BinaryAssociation(
    name="localparameters136",
    ends={
        Property(name="eJSL_Parameter138", type=eJSL_Plugin, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Plugin137", type=eJSL_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entities139: BinaryAssociation = BinaryAssociation(
    name="entities139",
    ends={
        Property(name="eJSL_Entity140", type=eJSL_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Library", type=eJSL_Entity, multiplicity=Multiplicity(0, 9999))
    }
)
classes141: BinaryAssociation = BinaryAssociation(
    name="classes141",
    ends={
        Property(name="eJSL_Class", type=eJSL_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Library142", type=eJSL_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages143: BinaryAssociation = BinaryAssociation(
    name="packages143",
    ends={
        Property(name="eJSL_Package", type=eJSL_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Library144", type=eJSL_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages146: BinaryAssociation = BinaryAssociation(
    name="packages146",
    ends={
        Property(name="eJSL_Package147", type=eJSL_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Package145", type=eJSL_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes148: BinaryAssociation = BinaryAssociation(
    name="classes148",
    ends={
        Property(name="eJSL_Class150", type=eJSL_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Package149", type=eJSL_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supertype152: BinaryAssociation = BinaryAssociation(
    name="supertype152",
    ends={
        Property(name="eJSL_Class153", type=eJSL_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Class151", type=eJSL_Class, multiplicity=Multiplicity(0, 1))
    }
)
references155: BinaryAssociation = BinaryAssociation(
    name="references155",
    ends={
        Property(name="eJSL_Class156", type=eJSL_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Class154", type=eJSL_Class, multiplicity=Multiplicity(0, 9999))
    }
)
entities157: BinaryAssociation = BinaryAssociation(
    name="entities157",
    ends={
        Property(name="eJSL_Entity159", type=eJSL_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Class158", type=eJSL_Entity, multiplicity=Multiplicity(0, 9999))
    }
)
methods160: BinaryAssociation = BinaryAssociation(
    name="methods160",
    ends={
        Property(name="eJSL_Method", type=eJSL_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Class161", type=eJSL_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
page124: BinaryAssociation = BinaryAssociation(
    name="page124",
    ends={
        Property(name="eJSL_Page126", type=eJSL_PageReference, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_PageReference125", type=eJSL_Page, multiplicity=Multiplicity(0, 1))
    }
)
pagescr127: BinaryAssociation = BinaryAssociation(
    name="pagescr127",
    ends={
        Property(name="eJSL_ComponentReference", type=eJSL_PageReference, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_PageReference128", type=eJSL_ComponentReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodparameters165: BinaryAssociation = BinaryAssociation(
    name="methodparameters165",
    ends={
        Property(name="eJSL_MethodParameter", type=eJSL_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Method166", type=eJSL_MethodParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type167: BinaryAssociation = BinaryAssociation(
    name="type167",
    ends={
        Property(name="eJSL_Type169", type=eJSL_MethodParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_MethodParameter168", type=eJSL_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
localparameters170: BinaryAssociation = BinaryAssociation(
    name="localparameters170",
    ends={
        Property(name="eJSL_Parameter171", type=eJSL_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Template", type=eJSL_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
positions172: BinaryAssociation = BinaryAssociation(
    name="positions172",
    ends={
        Property(name="eJSL_Position", type=eJSL_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Template173", type=eJSL_Position, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cssblocks174: BinaryAssociation = BinaryAssociation(
    name="cssblocks174",
    ends={
        Property(name="eJSL_CssBlock", type=eJSL_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Template175", type=eJSL_CssBlock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors176: BinaryAssociation = BinaryAssociation(
    name="authors176",
    ends={
        Property(name="eJSL_Author", type=eJSL_Manifestation, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Manifestation177", type=eJSL_Author, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyvaluepairs178: BinaryAssociation = BinaryAssociation(
    name="keyvaluepairs178",
    ends={
        Property(name="eJSL_KeyValuePair180", type=eJSL_Language, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Language179", type=eJSL_KeyValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
positionparameters181: BinaryAssociation = BinaryAssociation(
    name="positionparameters181",
    ends={
        Property(name="eJSL_PositionParameter", type=eJSL_Position, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Position182", type=eJSL_PositionParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type162: BinaryAssociation = BinaryAssociation(
    name="type162",
    ends={
        Property(name="eJSL_Type164", type=eJSL_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_Method163", type=eJSL_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keyvaluepairs183: BinaryAssociation = BinaryAssociation(
    name="keyvaluepairs183",
    ends={
        Property(name="eJSL_KeyValuePair185", type=eJSL_PositionParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_PositionParameter184", type=eJSL_KeyValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyvaluepairs186: BinaryAssociation = BinaryAssociation(
    name="keyvaluepairs186",
    ends={
        Property(name="eJSL_KeyValuePair188", type=eJSL_CssBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="eJSL_CssBlock187", type=eJSL_KeyValuePair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_eJSL_DatatypeReference_Type = Generalization(general=Type, specific=eJSL_DatatypeReference)
gen_eJSL_DatatypeReference_HTMLTypes = Generalization(general=HTMLTypes, specific=eJSL_DatatypeReference)
gen_eJSL_StandardTypes_Type = Generalization(general=Type, specific=eJSL_StandardTypes)
gen_eJSL_CMSCore_EJSLPart = Generalization(general=EJSLPart, specific=eJSL_CMSCore)
gen_eJSL_CMSExtension_EJSLPart = Generalization(general=EJSLPart, specific=eJSL_CMSExtension)
gen_eJSL_StaticPage_Page = Generalization(general=Page, specific=eJSL_StaticPage)
gen_eJSL_DynamicPage_Page = Generalization(general=Page, specific=eJSL_DynamicPage)
gen_eJSL_IndexPage_DynamicPage = Generalization(general=DynamicPage, specific=eJSL_IndexPage)
gen_eJSL_DetailsPage_DynamicPage = Generalization(general=DynamicPage, specific=eJSL_DetailsPage)
gen_eJSL_CustomPage_Page = Generalization(general=Page, specific=eJSL_CustomPage)
gen_eJSL_SimpleHTMLTypes_HTMLTypes = Generalization(general=HTMLTypes, specific=eJSL_SimpleHTMLTypes)
gen_eJSL_ComplexHTMLTypes_HTMLTypes = Generalization(general=HTMLTypes, specific=eJSL_ComplexHTMLTypes)
gen_eJSL_ExternalLink_Link = Generalization(general=Link, specific=eJSL_ExternalLink)
gen_eJSL_InternalLink_Link = Generalization(general=Link, specific=eJSL_InternalLink)
gen_eJSL_ContextLink_InternalLink = Generalization(general=InternalLink, specific=eJSL_ContextLink)
gen_eJSL_ExtensionPackage_Extension = Generalization(general=Extension, specific=eJSL_ExtensionPackage)
gen_eJSL_Component_Extension = Generalization(general=Extension, specific=eJSL_Component)
gen_eJSL_BackendSection_Section = Generalization(general=Section, specific=eJSL_BackendSection)
gen_eJSL_FrontendSection_Section = Generalization(general=Section, specific=eJSL_FrontendSection)
gen_eJSL_Module_Extension = Generalization(general=Extension, specific=eJSL_Module)
gen_eJSL_Plugin_Extension = Generalization(general=Extension, specific=eJSL_Plugin)
gen_eJSL_Library_Extension = Generalization(general=Extension, specific=eJSL_Library)
gen_eJSL_Template_Extension = Generalization(general=Extension, specific=eJSL_Template)

# Domain Model
domain_model = DomainModel(
    name="eJSL",
    types={eJSL_EJSLModel, eJSL_EJSLPart, eJSL_Datatype, eJSL_Parameter, eJSL_ParameterGroup, eJSL_Feature, eJSL_CMSCore, eJSL_Page, eJSL_Section, eJSL_Type, eJSL_DatatypeReference, Type, HTMLTypes, eJSL_StandardTypes, eJSL_HTMLTypes, eJSL_KeyValuePair, EJSLPart, eJSL_coreFeature, eJSL_CMSExtension, eJSL_Extension, eJSL_Entitypackage, eJSL_Entity, eJSL_Attribute, eJSL_Reference, eJSL_PageAction, eJSL_Link, eJSL_StaticPage, Page, eJSL_DynamicPage, eJSL_IndexPage, DynamicPage, eJSL_DetailsPage, eJSL_DetailPageField, eJSL_CustomPage, eJSL_SimpleHTMLTypes, eJSL_ComplexHTMLTypes, eJSL_ExternalLink, Link, eJSL_InternalLink, eJSL_ContextLink, InternalLink, eJSL_LinkParameter, eJSL_Manifestation, eJSL_Language, eJSL_ExtensionPackage, Extension, eJSL_Component, eJSL_PageReference, eJSL_BackendSection, Section, eJSL_FrontendSection, eJSL_Module, eJSL_Plugin, eJSL_Library, eJSL_Class, eJSL_Package, eJSL_Method, eJSL_ComponentReference, eJSL_MethodParameter, eJSL_Template, eJSL_Position, eJSL_CssBlock, eJSL_Author, eJSL_PositionParameter, PluginKinds, PageActionKind, PageActionPositionKind, StandardTypeKinds, DataAccessKinds, SimpleHTMLTypeKinds, ComplexHTMLTypeKinds, CoreComponent, PageKinds},
    associations={ejslPart0, datatypes1, globalparameters3, parametergroups5, feature7, entities12, pages14, sections16, type18, dtype20, values22, attributes24, globalparameters27, parameters30, extensions9, entitypackages10, entities36, datatypes39, supertype43, attributes45, references47, type49, withattribute52, attribute54, entity57, attributerefereced60, parametergroups63, globalparameters66, entitypackages34, links74, entities76, tablecolumns78, filters81, editfields84, attribute85, htmltype88, values91, attributes94, entities97, localparameters69, pageactions72, linkedAttribute99, linkedAction102, target105, linkparameters107, attvalue108, manifest111, languages113, extensions115, globalParamter117, sections119, pageRef122, ref129, pageRef132, entities134, localparameters136, entities139, classes141, packages143, packages146, classes148, supertype152, references155, entities157, methods160, page124, pagescr127, methodparameters165, type167, localparameters170, positions172, cssblocks174, authors176, keyvaluepairs178, positionparameters181, type162, keyvaluepairs183, keyvaluepairs186},
    generalizations={gen_eJSL_DatatypeReference_Type, gen_eJSL_DatatypeReference_HTMLTypes, gen_eJSL_StandardTypes_Type, gen_eJSL_CMSCore_EJSLPart, gen_eJSL_CMSExtension_EJSLPart, gen_eJSL_StaticPage_Page, gen_eJSL_DynamicPage_Page, gen_eJSL_IndexPage_DynamicPage, gen_eJSL_DetailsPage_DynamicPage, gen_eJSL_CustomPage_Page, gen_eJSL_SimpleHTMLTypes_HTMLTypes, gen_eJSL_ComplexHTMLTypes_HTMLTypes, gen_eJSL_ExternalLink_Link, gen_eJSL_InternalLink_Link, gen_eJSL_ContextLink_InternalLink, gen_eJSL_ExtensionPackage_Extension, gen_eJSL_Component_Extension, gen_eJSL_BackendSection_Section, gen_eJSL_FrontendSection_Section, gen_eJSL_Module_Extension, gen_eJSL_Plugin_Extension, gen_eJSL_Library_Extension, gen_eJSL_Template_Extension},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)