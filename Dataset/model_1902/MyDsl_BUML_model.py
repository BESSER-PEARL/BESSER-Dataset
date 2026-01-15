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
myDsl_System = Class(name="myDsl::System")
myDsl_EntityName = Class(name="myDsl::EntityName")
myDsl_GeneralEntity = Class(name="myDsl::GeneralEntity")
myDsl_Domain = Class(name="myDsl::Domain")
myDsl_Property = Class(name="myDsl::Property")
myDsl_Architecture = Class(name="myDsl::Architecture")
myDsl_Technology = Class(name="myDsl::Technology")
myDsl_Type = Class(name="myDsl::Type")
myDsl_Module = Class(name="myDsl::Module")
myDsl_RelationDom = Class(name="myDsl::RelationDom")
myDsl_Submodule = Class(name="myDsl::Submodule")
myDsl_Operation = Class(name="myDsl::Operation")
myDsl_EObject = Class(name="myDsl::EObject")
myDsl_Layer = Class(name="myDsl::Layer")
myDsl_LayerSegment = Class(name="myDsl::LayerSegment")
myDsl_LayerSegmentRelation = Class(name="myDsl::LayerSegmentRelation")
myDsl_SublayerSegment = Class(name="myDsl::SublayerSegment")
AbstractFrontElement = Class(name="AbstractFrontElement")
myDsl_SpecialEntity = Class(name="myDsl::SpecialEntity")
myDsl_JavaApp = Class(name="myDsl::JavaApp")
myDsl_Transaction = Class(name="myDsl::Transaction")
myDsl_ReactApp = Class(name="myDsl::ReactApp")
myDsl_Operateson = Class(name="myDsl::Operateson")
myDsl_JeeProject = Class(name="myDsl::JeeProject")
myDsl_Subproject = Class(name="myDsl::Subproject")
myDsl_Epackage = Class(name="myDsl::Epackage")
myDsl_Component = Class(name="myDsl::Component")
myDsl_Library = Class(name="myDsl::Library")
myDsl_RelationArch = Class(name="myDsl::RelationArch")
myDsl_Attribute = Class(name="myDsl::Attribute")
myDsl_MethodBack = Class(name="myDsl::MethodBack")
myDsl_Annotation = Class(name="myDsl::Annotation")
myDsl_AbstractMethod = Class(name="myDsl::AbstractMethod")
myDsl_GenericClass = Class(name="myDsl::GenericClass")
myDsl_Einterface = Class(name="myDsl::Einterface")
myDsl_NativeClass = Class(name="myDsl::NativeClass")
myDsl_Eclass = Class(name="myDsl::Eclass")
myDsl_Descriptor = Class(name="myDsl::Descriptor")
myDsl_AbstractClass = Class(name="myDsl::AbstractClass")
Eclass = Class(name="Eclass")
myDsl_Functionality = Class(name="myDsl::Functionality")
myDsl_Directory = Class(name="myDsl::Directory")
myDsl_JsModule = Class(name="myDsl::JsModule")
myDsl_RouterComponent = Class(name="myDsl::RouterComponent")
myDsl_Container = Class(name="myDsl::Container")
myDsl_Visualizer = Class(name="myDsl::Visualizer")
myDsl_State = Class(name="myDsl::State")
myDsl_AbstractFrontElement = Class(name="myDsl::AbstractFrontElement")
UIComponent = Class(name="UIComponent")
myDsl_UIComponent = Class(name="myDsl::UIComponent")
myDsl_JsMethod = Class(name="myDsl::JsMethod")
myDsl_ServiceFront = Class(name="myDsl::ServiceFront")
myDsl_File = Class(name="myDsl::File")
myDsl_Md = Class(name="myDsl::Md")
File = Class(name="File")
myDsl_Js = Class(name="myDsl::Js")
myDsl_Json = Class(name="myDsl::Json")
myDsl_Css = Class(name="myDsl::Css")
myDsl_Action = Class(name="myDsl::Action")
myDsl_AxiosRequest = Class(name="myDsl::AxiosRequest")
myDsl_Reducer = Class(name="myDsl::Reducer")
myDsl_ActionCreator = Class(name="myDsl::ActionCreator")
myDsl_ActionDispatcher = Class(name="myDsl::ActionDispatcher")
myDsl_JsMethodArgs = Class(name="myDsl::JsMethodArgs")

# myDsl_System class attributes and methods

# myDsl_EntityName class attributes and methods
myDsl_EntityName_name: Property = Property(name="name", type=StringType)
myDsl_EntityName.attributes={myDsl_EntityName_name}

# myDsl_GeneralEntity class attributes and methods

# myDsl_Domain class attributes and methods

# myDsl_Property class attributes and methods
myDsl_Property_name: Property = Property(name="name", type=StringType)
myDsl_Property.attributes={myDsl_Property_name}

# myDsl_Architecture class attributes and methods

# myDsl_Technology class attributes and methods

# myDsl_Type class attributes and methods
myDsl_Type_name: Property = Property(name="name", type=StringType)
myDsl_Type.attributes={myDsl_Type_name}

# myDsl_Module class attributes and methods
myDsl_Module_name: Property = Property(name="name", type=StringType)
myDsl_Module.attributes={myDsl_Module_name}

# myDsl_RelationDom class attributes and methods

# myDsl_Submodule class attributes and methods
myDsl_Submodule_name: Property = Property(name="name", type=StringType)
myDsl_Submodule.attributes={myDsl_Submodule_name}

# myDsl_Operation class attributes and methods
myDsl_Operation_type: Property = Property(name="type", type=StringType)
myDsl_Operation.attributes={myDsl_Operation_type}

# myDsl_EObject class attributes and methods

# myDsl_Layer class attributes and methods
myDsl_Layer_name: Property = Property(name="name", type=StringType)
myDsl_Layer.attributes={myDsl_Layer_name}

# myDsl_LayerSegment class attributes and methods
myDsl_LayerSegment_name: Property = Property(name="name", type=StringType)
myDsl_LayerSegment.attributes={myDsl_LayerSegment_name}

# myDsl_LayerSegmentRelation class attributes and methods
myDsl_LayerSegmentRelation_layerSegment: Property = Property(name="layerSegment", type=StringType)
myDsl_LayerSegmentRelation.attributes={myDsl_LayerSegmentRelation_layerSegment}

# myDsl_SublayerSegment class attributes and methods
myDsl_SublayerSegment_name: Property = Property(name="name", type=StringType)
myDsl_SublayerSegment.attributes={myDsl_SublayerSegment_name}

# AbstractFrontElement class attributes and methods

# myDsl_SpecialEntity class attributes and methods

# myDsl_JavaApp class attributes and methods

# myDsl_Transaction class attributes and methods
myDsl_Transaction_type: Property = Property(name="type", type=StringType)
myDsl_Transaction.attributes={myDsl_Transaction_type}

# myDsl_ReactApp class attributes and methods

# myDsl_Operateson class attributes and methods

# myDsl_JeeProject class attributes and methods
myDsl_JeeProject_name: Property = Property(name="name", type=StringType)
myDsl_JeeProject.attributes={myDsl_JeeProject_name}

# myDsl_Subproject class attributes and methods
myDsl_Subproject_name: Property = Property(name="name", type=StringType)
myDsl_Subproject.attributes={myDsl_Subproject_name}

# myDsl_Epackage class attributes and methods
myDsl_Epackage_name: Property = Property(name="name", type=StringType)
myDsl_Epackage.attributes={myDsl_Epackage_name}

# myDsl_Component class attributes and methods
myDsl_Component_name: Property = Property(name="name", type=StringType)
myDsl_Component.attributes={myDsl_Component_name}

# myDsl_Library class attributes and methods
myDsl_Library_name: Property = Property(name="name", type=StringType)
myDsl_Library_isNative: Property = Property(name="isNative", type=StringType)
myDsl_Library.attributes={myDsl_Library_isNative, myDsl_Library_name}

# myDsl_RelationArch class attributes and methods
myDsl_RelationArch_name: Property = Property(name="name", type=StringType)
myDsl_RelationArch_source: Property = Property(name="source", type=StringType)
myDsl_RelationArch_target: Property = Property(name="target", type=StringType)
myDsl_RelationArch.attributes={myDsl_RelationArch_target, myDsl_RelationArch_source, myDsl_RelationArch_name}

# myDsl_Attribute class attributes and methods
myDsl_Attribute_name: Property = Property(name="name", type=StringType)
myDsl_Attribute.attributes={myDsl_Attribute_name}

# myDsl_MethodBack class attributes and methods
myDsl_MethodBack_name: Property = Property(name="name", type=StringType)
myDsl_MethodBack.attributes={myDsl_MethodBack_name}

# myDsl_Annotation class attributes and methods
myDsl_Annotation_propertie: Property = Property(name="propertie", type=StringType)
myDsl_Annotation.attributes={myDsl_Annotation_propertie}

# myDsl_AbstractMethod class attributes and methods
myDsl_AbstractMethod_name: Property = Property(name="name", type=StringType)
myDsl_AbstractMethod.attributes={myDsl_AbstractMethod_name}

# myDsl_GenericClass class attributes and methods

# myDsl_Einterface class attributes and methods
myDsl_Einterface_name: Property = Property(name="name", type=StringType)
myDsl_Einterface.attributes={myDsl_Einterface_name}

# myDsl_NativeClass class attributes and methods

# myDsl_Eclass class attributes and methods
myDsl_Eclass_name: Property = Property(name="name", type=StringType)
myDsl_Eclass.attributes={myDsl_Eclass_name}

# myDsl_Descriptor class attributes and methods
myDsl_Descriptor_name: Property = Property(name="name", type=StringType)
myDsl_Descriptor_path: Property = Property(name="path", type=StringType)
myDsl_Descriptor.attributes={myDsl_Descriptor_name, myDsl_Descriptor_path}

# myDsl_AbstractClass class attributes and methods

# Eclass class attributes and methods

# myDsl_Functionality class attributes and methods
myDsl_Functionality_name: Property = Property(name="name", type=StringType)
myDsl_Functionality.attributes={myDsl_Functionality_name}

# myDsl_Directory class attributes and methods
myDsl_Directory_name: Property = Property(name="name", type=StringType)
myDsl_Directory_purpose: Property = Property(name="purpose", type=StringType)
myDsl_Directory.attributes={myDsl_Directory_name, myDsl_Directory_purpose}

# myDsl_JsModule class attributes and methods
myDsl_JsModule_name: Property = Property(name="name", type=StringType)
myDsl_JsModule.attributes={myDsl_JsModule_name}

# myDsl_RouterComponent class attributes and methods
myDsl_RouterComponent_name: Property = Property(name="name", type=StringType)
myDsl_RouterComponent.attributes={myDsl_RouterComponent_name}

# myDsl_Container class attributes and methods
myDsl_Container_name: Property = Property(name="name", type=StringType)
myDsl_Container.attributes={myDsl_Container_name}

# myDsl_Visualizer class attributes and methods
myDsl_Visualizer_name: Property = Property(name="name", type=StringType)
myDsl_Visualizer.attributes={myDsl_Visualizer_name}

# myDsl_State class attributes and methods
myDsl_State_name: Property = Property(name="name", type=StringType)
myDsl_State.attributes={myDsl_State_name}

# myDsl_AbstractFrontElement class attributes and methods

# UIComponent class attributes and methods

# myDsl_UIComponent class attributes and methods

# myDsl_JsMethod class attributes and methods
myDsl_JsMethod_name: Property = Property(name="name", type=StringType)
myDsl_JsMethod_type: Property = Property(name="type", type=StringType)
myDsl_JsMethod.attributes={myDsl_JsMethod_type, myDsl_JsMethod_name}

# myDsl_ServiceFront class attributes and methods
myDsl_ServiceFront_name: Property = Property(name="name", type=StringType)
myDsl_ServiceFront_method: Property = Property(name="method", type=StringType)
myDsl_ServiceFront.attributes={myDsl_ServiceFront_method, myDsl_ServiceFront_name}

# myDsl_File class attributes and methods
myDsl_File_name: Property = Property(name="name", type=StringType)
myDsl_File_type: Property = Property(name="type", type=StringType)
myDsl_File.attributes={myDsl_File_name, myDsl_File_type}

# myDsl_Md class attributes and methods

# File class attributes and methods

# myDsl_Js class attributes and methods

# myDsl_Json class attributes and methods

# myDsl_Css class attributes and methods

# myDsl_Action class attributes and methods
myDsl_Action_name: Property = Property(name="name", type=StringType)
myDsl_Action.attributes={myDsl_Action_name}

# myDsl_AxiosRequest class attributes and methods
myDsl_AxiosRequest_name: Property = Property(name="name", type=StringType)
myDsl_AxiosRequest_axiosRestMethod: Property = Property(name="axiosRestMethod", type=StringType)
myDsl_AxiosRequest_url: Property = Property(name="url", type=StringType)
myDsl_AxiosRequest.attributes={myDsl_AxiosRequest_axiosRestMethod, myDsl_AxiosRequest_name, myDsl_AxiosRequest_url}

# myDsl_Reducer class attributes and methods
myDsl_Reducer_name: Property = Property(name="name", type=StringType)
myDsl_Reducer.attributes={myDsl_Reducer_name}

# myDsl_ActionCreator class attributes and methods
myDsl_ActionCreator_name: Property = Property(name="name", type=StringType)
myDsl_ActionCreator_type: Property = Property(name="type", type=StringType)
myDsl_ActionCreator.attributes={myDsl_ActionCreator_name, myDsl_ActionCreator_type}

# myDsl_ActionDispatcher class attributes and methods
myDsl_ActionDispatcher_name: Property = Property(name="name", type=StringType)
myDsl_ActionDispatcher.attributes={myDsl_ActionDispatcher_name}

# myDsl_JsMethodArgs class attributes and methods
myDsl_JsMethodArgs_name: Property = Property(name="name", type=StringType)
myDsl_JsMethodArgs.attributes={myDsl_JsMethodArgs_name}

# Relationships
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="myDsl_EntityName", type=myDsl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Operation18", type=myDsl_EntityName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name19: BinaryAssociation = BinaryAssociation(
    name="name19",
    ends={
        Property(name="myDsl_EntityName20", type=myDsl_GeneralEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_GeneralEntity", type=myDsl_EntityName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dom0: BinaryAssociation = BinaryAssociation(
    name="dom0",
    ends={
        Property(name="myDsl_Domain", type=myDsl_System, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_System", type=myDsl_Domain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties21: BinaryAssociation = BinaryAssociation(
    name="properties21",
    ends={
        Property(name="myDsl_Property", type=myDsl_GeneralEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_GeneralEntity22", type=myDsl_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arch1: BinaryAssociation = BinaryAssociation(
    name="arch1",
    ends={
        Property(name="myDsl_Architecture", type=myDsl_System, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_System2", type=myDsl_Architecture, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tech3: BinaryAssociation = BinaryAssociation(
    name="tech3",
    ends={
        Property(name="myDsl_Technology", type=myDsl_System, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_System4", type=myDsl_Technology, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types5: BinaryAssociation = BinaryAssociation(
    name="types5",
    ends={
        Property(name="myDsl_Type", type=myDsl_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Domain6", type=myDsl_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modules7: BinaryAssociation = BinaryAssociation(
    name="modules7",
    ends={
        Property(name="myDsl_Module", type=myDsl_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Domain8", type=myDsl_Module, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations9: BinaryAssociation = BinaryAssociation(
    name="relations9",
    ends={
        Property(name="myDsl_RelationDom", type=myDsl_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Domain10", type=myDsl_RelationDom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
submodules11: BinaryAssociation = BinaryAssociation(
    name="submodules11",
    ends={
        Property(name="myDsl_Submodule", type=myDsl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Module12", type=myDsl_Submodule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations13: BinaryAssociation = BinaryAssociation(
    name="operations13",
    ends={
        Property(name="myDsl_Operation", type=myDsl_Submodule, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Submodule14", type=myDsl_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entities15: BinaryAssociation = BinaryAssociation(
    name="entities15",
    ends={
        Property(name="myDsl_EObject", type=myDsl_Submodule, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Submodule16", type=myDsl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layer48: BinaryAssociation = BinaryAssociation(
    name="layer48",
    ends={
        Property(name="myDsl_Layer", type=myDsl_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Component49", type=myDsl_Layer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layerSegments50: BinaryAssociation = BinaryAssociation(
    name="layerSegments50",
    ends={
        Property(name="myDsl_LayerSegment", type=myDsl_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Layer51", type=myDsl_LayerSegment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations52: BinaryAssociation = BinaryAssociation(
    name="relations52",
    ends={
        Property(name="myDsl_LayerSegmentRelation", type=myDsl_LayerSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_LayerSegment53", type=myDsl_LayerSegmentRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sublayerSegments54: BinaryAssociation = BinaryAssociation(
    name="sublayerSegments54",
    ends={
        Property(name="myDsl_SublayerSegment", type=myDsl_LayerSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_LayerSegment55", type=myDsl_SublayerSegment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type23: BinaryAssociation = BinaryAssociation(
    name="type23",
    ends={
        Property(name="myDsl_Type25", type=myDsl_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Property24", type=myDsl_Type, multiplicity=Multiplicity(0, 1))
    }
)
name26: BinaryAssociation = BinaryAssociation(
    name="name26",
    ends={
        Property(name="myDsl_EntityName27", type=myDsl_SpecialEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SpecialEntity", type=myDsl_EntityName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties28: BinaryAssociation = BinaryAssociation(
    name="properties28",
    ends={
        Property(name="myDsl_Property30", type=myDsl_SpecialEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SpecialEntity29", type=myDsl_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
java56: BinaryAssociation = BinaryAssociation(
    name="java56",
    ends={
        Property(name="myDsl_JavaApp", type=myDsl_Technology, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Technology57", type=myDsl_JavaApp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transactions31: BinaryAssociation = BinaryAssociation(
    name="transactions31",
    ends={
        Property(name="myDsl_Transaction", type=myDsl_SpecialEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_SpecialEntity32", type=myDsl_Transaction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
react58: BinaryAssociation = BinaryAssociation(
    name="react58",
    ends={
        Property(name="myDsl_ReactApp", type=myDsl_Technology, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Technology59", type=myDsl_ReactApp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operateson33: BinaryAssociation = BinaryAssociation(
    name="operateson33",
    ends={
        Property(name="myDsl_Operateson", type=myDsl_Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Transaction34", type=myDsl_Operateson, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
jeeproject60: BinaryAssociation = BinaryAssociation(
    name="jeeproject60",
    ends={
        Property(name="myDsl_JeeProject", type=myDsl_JavaApp, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_JavaApp61", type=myDsl_JeeProject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operateson35: BinaryAssociation = BinaryAssociation(
    name="operateson35",
    ends={
        Property(name="myDsl_EntityName37", type=myDsl_Operateson, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Operateson36", type=myDsl_EntityName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subproject62: BinaryAssociation = BinaryAssociation(
    name="subproject62",
    ends={
        Property(name="myDsl_Subproject", type=myDsl_JeeProject, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_JeeProject63", type=myDsl_Subproject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source38: BinaryAssociation = BinaryAssociation(
    name="source38",
    ends={
        Property(name="myDsl_EntityName40", type=myDsl_RelationDom, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_RelationDom39", type=myDsl_EntityName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target41: BinaryAssociation = BinaryAssociation(
    name="target41",
    ends={
        Property(name="myDsl_EntityName43", type=myDsl_RelationDom, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_RelationDom42", type=myDsl_EntityName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
epackage64: BinaryAssociation = BinaryAssociation(
    name="epackage64",
    ends={
        Property(name="myDsl_Epackage", type=myDsl_Subproject, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Subproject65", type=myDsl_Epackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
componentes44: BinaryAssociation = BinaryAssociation(
    name="componentes44",
    ends={
        Property(name="myDsl_Component", type=myDsl_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Architecture45", type=myDsl_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationArch46: BinaryAssociation = BinaryAssociation(
    name="relationArch46",
    ends={
        Property(name="myDsl_RelationArch", type=myDsl_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Architecture47", type=myDsl_RelationArch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute70: BinaryAssociation = BinaryAssociation(
    name="attribute70",
    ends={
        Property(name="myDsl_Attribute", type=myDsl_AbstractClass, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_AbstractClass", type=myDsl_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodClass71: BinaryAssociation = BinaryAssociation(
    name="methodClass71",
    ends={
        Property(name="myDsl_MethodBack", type=myDsl_AbstractClass, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_AbstractClass72", type=myDsl_MethodBack, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation73: BinaryAssociation = BinaryAssociation(
    name="annotation73",
    ends={
        Property(name="myDsl_Annotation", type=myDsl_AbstractClass, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_AbstractClass74", type=myDsl_Annotation, multiplicity=Multiplicity(0, 1))
    }
)
abstractMethod75: BinaryAssociation = BinaryAssociation(
    name="abstractMethod75",
    ends={
        Property(name="myDsl_AbstractMethod", type=myDsl_AbstractClass, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_AbstractClass76", type=myDsl_AbstractMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute77: BinaryAssociation = BinaryAssociation(
    name="attribute77",
    ends={
        Property(name="myDsl_Attribute78", type=myDsl_GenericClass, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_GenericClass", type=myDsl_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodClass79: BinaryAssociation = BinaryAssociation(
    name="methodClass79",
    ends={
        Property(name="myDsl_MethodBack81", type=myDsl_GenericClass, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_GenericClass80", type=myDsl_MethodBack, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation82: BinaryAssociation = BinaryAssociation(
    name="annotation82",
    ends={
        Property(name="myDsl_Annotation84", type=myDsl_GenericClass, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_GenericClass83", type=myDsl_Annotation, multiplicity=Multiplicity(0, 1))
    }
)
abs85: BinaryAssociation = BinaryAssociation(
    name="abs85",
    ends={
        Property(name="myDsl_AbstractClass87", type=myDsl_GenericClass, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_GenericClass86", type=myDsl_AbstractClass, multiplicity=Multiplicity(0, 1))
    }
)
imp88: BinaryAssociation = BinaryAssociation(
    name="imp88",
    ends={
        Property(name="myDsl_Einterface", type=myDsl_GenericClass, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_GenericClass89", type=myDsl_Einterface, multiplicity=Multiplicity(0, 1))
    }
)
attribute90: BinaryAssociation = BinaryAssociation(
    name="attribute90",
    ends={
        Property(name="myDsl_Attribute92", type=myDsl_Einterface, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Einterface91", type=myDsl_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abstractMethod93: BinaryAssociation = BinaryAssociation(
    name="abstractMethod93",
    ends={
        Property(name="myDsl_AbstractMethod95", type=myDsl_Einterface, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Einterface94", type=myDsl_AbstractMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute96: BinaryAssociation = BinaryAssociation(
    name="attribute96",
    ends={
        Property(name="myDsl_Attribute97", type=myDsl_NativeClass, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_NativeClass", type=myDsl_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodClass98: BinaryAssociation = BinaryAssociation(
    name="methodClass98",
    ends={
        Property(name="myDsl_MethodBack100", type=myDsl_NativeClass, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_NativeClass99", type=myDsl_MethodBack, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
library66: BinaryAssociation = BinaryAssociation(
    name="library66",
    ends={
        Property(name="myDsl_Library", type=myDsl_Subproject, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Subproject67", type=myDsl_Library, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptor68: BinaryAssociation = BinaryAssociation(
    name="descriptor68",
    ends={
        Property(name="myDsl_Descriptor", type=myDsl_Subproject, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Subproject69", type=myDsl_Descriptor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type101: BinaryAssociation = BinaryAssociation(
    name="type101",
    ends={
        Property(name="myDsl_Eclass", type=myDsl_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Attribute102", type=myDsl_Eclass, multiplicity=Multiplicity(0, 1))
    }
)
eclass103: BinaryAssociation = BinaryAssociation(
    name="eclass103",
    ends={
        Property(name="myDsl_Eclass105", type=myDsl_Epackage, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Epackage104", type=myDsl_Eclass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arg106: BinaryAssociation = BinaryAssociation(
    name="arg106",
    ends={
        Property(name="myDsl_Eclass108", type=myDsl_MethodBack, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_MethodBack107", type=myDsl_Eclass, multiplicity=Multiplicity(0, 1))
    }
)
type109: BinaryAssociation = BinaryAssociation(
    name="type109",
    ends={
        Property(name="myDsl_Eclass111", type=myDsl_MethodBack, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_MethodBack110", type=myDsl_Eclass, multiplicity=Multiplicity(0, 1))
    }
)
arg112: BinaryAssociation = BinaryAssociation(
    name="arg112",
    ends={
        Property(name="myDsl_Eclass114", type=myDsl_AbstractMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_AbstractMethod113", type=myDsl_Eclass, multiplicity=Multiplicity(0, 1))
    }
)
type115: BinaryAssociation = BinaryAssociation(
    name="type115",
    ends={
        Property(name="myDsl_Eclass117", type=myDsl_AbstractMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_AbstractMethod116", type=myDsl_Eclass, multiplicity=Multiplicity(0, 1))
    }
)
elements121: BinaryAssociation = BinaryAssociation(
    name="elements121",
    ends={
        Property(name="myDsl_AbstractFrontElement", type=myDsl_ReactApp, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReactApp122", type=myDsl_AbstractFrontElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
func123: BinaryAssociation = BinaryAssociation(
    name="func123",
    ends={
        Property(name="myDsl_Functionality", type=myDsl_ReactApp, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReactApp124", type=myDsl_Functionality, multiplicity=Multiplicity(0, 1))
    }
)
dir125: BinaryAssociation = BinaryAssociation(
    name="dir125",
    ends={
        Property(name="myDsl_Directory", type=myDsl_ReactApp, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReactApp126", type=myDsl_Directory, multiplicity=Multiplicity(0, 1))
    }
)
mod127: BinaryAssociation = BinaryAssociation(
    name="mod127",
    ends={
        Property(name="myDsl_JsModule", type=myDsl_ReactApp, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ReactApp128", type=myDsl_JsModule, multiplicity=Multiplicity(0, 1))
    }
)
route129: BinaryAssociation = BinaryAssociation(
    name="route129",
    ends={
        Property(name="myDsl_RouterComponent", type=myDsl_Functionality, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Functionality130", type=myDsl_RouterComponent, multiplicity=Multiplicity(0, 1))
    }
)
wrap131: BinaryAssociation = BinaryAssociation(
    name="wrap131",
    ends={
        Property(name="myDsl_Container", type=myDsl_Functionality, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Functionality132", type=myDsl_Container, multiplicity=Multiplicity(0, 1))
    }
)
render133: BinaryAssociation = BinaryAssociation(
    name="render133",
    ends={
        Property(name="myDsl_Visualizer", type=myDsl_Functionality, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Functionality134", type=myDsl_Visualizer, multiplicity=Multiplicity(0, 1))
    }
)
state135: BinaryAssociation = BinaryAssociation(
    name="state135",
    ends={
        Property(name="myDsl_State", type=myDsl_Functionality, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Functionality136", type=myDsl_State, multiplicity=Multiplicity(0, 1))
    }
)
annotation118: BinaryAssociation = BinaryAssociation(
    name="annotation118",
    ends={
        Property(name="myDsl_Annotation120", type=myDsl_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Library119", type=myDsl_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type139: BinaryAssociation = BinaryAssociation(
    name="type139",
    ends={
        Property(name="myDsl_Directory141", type=myDsl_Functionality, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Functionality140", type=myDsl_Directory, multiplicity=Multiplicity(0, 1))
    }
)
type142: BinaryAssociation = BinaryAssociation(
    name="type142",
    ends={
        Property(name="myDsl_AbstractFrontElement144", type=myDsl_RouterComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_RouterComponent143", type=myDsl_AbstractFrontElement, multiplicity=Multiplicity(0, 1))
    }
)
route145: BinaryAssociation = BinaryAssociation(
    name="route145",
    ends={
        Property(name="myDsl_UIComponent", type=myDsl_RouterComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_RouterComponent146", type=myDsl_UIComponent, multiplicity=Multiplicity(0, 1))
    }
)
type147: BinaryAssociation = BinaryAssociation(
    name="type147",
    ends={
        Property(name="myDsl_AbstractFrontElement149", type=myDsl_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Container148", type=myDsl_AbstractFrontElement, multiplicity=Multiplicity(0, 1))
    }
)
type150: BinaryAssociation = BinaryAssociation(
    name="type150",
    ends={
        Property(name="myDsl_AbstractFrontElement152", type=myDsl_Visualizer, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Visualizer151", type=myDsl_AbstractFrontElement, multiplicity=Multiplicity(0, 1))
    }
)
methods153: BinaryAssociation = BinaryAssociation(
    name="methods153",
    ends={
        Property(name="myDsl_JsMethod", type=myDsl_Visualizer, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Visualizer154", type=myDsl_JsMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type155: BinaryAssociation = BinaryAssociation(
    name="type155",
    ends={
        Property(name="myDsl_JsModule157", type=myDsl_ServiceFront, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ServiceFront156", type=myDsl_JsModule, multiplicity=Multiplicity(0, 1))
    }
)
service137: BinaryAssociation = BinaryAssociation(
    name="service137",
    ends={
        Property(name="myDsl_ServiceFront", type=myDsl_Functionality, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Functionality138", type=myDsl_ServiceFront, multiplicity=Multiplicity(0, 1))
    }
)
requests158: BinaryAssociation = BinaryAssociation(
    name="requests158",
    ends={
        Property(name="myDsl_AxiosRequest", type=myDsl_ServiceFront, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ServiceFront159", type=myDsl_AxiosRequest, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
file160: BinaryAssociation = BinaryAssociation(
    name="file160",
    ends={
        Property(name="myDsl_File", type=myDsl_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Directory161", type=myDsl_File, multiplicity=Multiplicity(0, 1))
    }
)
subdirectory163: BinaryAssociation = BinaryAssociation(
    name="subdirectory163",
    ends={
        Property(name="myDsl_Directory164", type=myDsl_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Directory162", type=myDsl_Directory, multiplicity=Multiplicity(0, 1))
    }
)
reducer167: BinaryAssociation = BinaryAssociation(
    name="reducer167",
    ends={
        Property(name="myDsl_Reducer", type=myDsl_State, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_State168", type=myDsl_Reducer, multiplicity=Multiplicity(0, 1))
    }
)
actionCreator169: BinaryAssociation = BinaryAssociation(
    name="actionCreator169",
    ends={
        Property(name="myDsl_ActionCreator", type=myDsl_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Action170", type=myDsl_ActionCreator, multiplicity=Multiplicity(0, 1))
    }
)
actionDispatcher171: BinaryAssociation = BinaryAssociation(
    name="actionDispatcher171",
    ends={
        Property(name="myDsl_ActionDispatcher", type=myDsl_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Action172", type=myDsl_ActionDispatcher, multiplicity=Multiplicity(0, 1))
    }
)
dir173: BinaryAssociation = BinaryAssociation(
    name="dir173",
    ends={
        Property(name="myDsl_Directory175", type=myDsl_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Action174", type=myDsl_Directory, multiplicity=Multiplicity(0, 1))
    }
)
action165: BinaryAssociation = BinaryAssociation(
    name="action165",
    ends={
        Property(name="myDsl_Action", type=myDsl_State, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_State166", type=myDsl_Action, multiplicity=Multiplicity(0, 1))
    }
)
type176: BinaryAssociation = BinaryAssociation(
    name="type176",
    ends={
        Property(name="myDsl_ActionCreator178", type=myDsl_ActionDispatcher, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ActionDispatcher177", type=myDsl_ActionCreator, multiplicity=Multiplicity(0, 1))
    }
)
type179: BinaryAssociation = BinaryAssociation(
    name="type179",
    ends={
        Property(name="myDsl_AbstractFrontElement181", type=myDsl_Reducer, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Reducer180", type=myDsl_AbstractFrontElement, multiplicity=Multiplicity(0, 1))
    }
)
type182: BinaryAssociation = BinaryAssociation(
    name="type182",
    ends={
        Property(name="myDsl_Directory184", type=myDsl_JsModule, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_JsModule183", type=myDsl_Directory, multiplicity=Multiplicity(0, 1))
    }
)
arguments185: BinaryAssociation = BinaryAssociation(
    name="arguments185",
    ends={
        Property(name="myDsl_JsMethodArgs", type=myDsl_JsMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_JsMethod186", type=myDsl_JsMethodArgs, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
data187: BinaryAssociation = BinaryAssociation(
    name="data187",
    ends={
        Property(name="myDsl_JsMethodArgs189", type=myDsl_AxiosRequest, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_AxiosRequest188", type=myDsl_JsMethodArgs, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_myDsl_Type_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=myDsl_Type)
gen_myDsl_GenericClass_Eclass = Generalization(general=Eclass, specific=myDsl_GenericClass)
gen_myDsl_NativeClass_Eclass = Generalization(general=Eclass, specific=myDsl_NativeClass)
gen_myDsl_AbstractClass_Eclass = Generalization(general=Eclass, specific=myDsl_AbstractClass)
gen_myDsl_Annotation_Eclass = Generalization(general=Eclass, specific=myDsl_Annotation)
gen_myDsl_ReactApp_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=myDsl_ReactApp)
gen_myDsl_Functionality_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=myDsl_Functionality)
gen_myDsl_RouterComponent_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=myDsl_RouterComponent)
gen_myDsl_RouterComponent_UIComponent = Generalization(general=UIComponent, specific=myDsl_RouterComponent)
gen_myDsl_Container_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=myDsl_Container)
gen_myDsl_Visualizer_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=myDsl_Visualizer)
gen_myDsl_Visualizer_UIComponent = Generalization(general=UIComponent, specific=myDsl_Visualizer)
gen_myDsl_ServiceFront_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=myDsl_ServiceFront)
gen_myDsl_Directory_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=myDsl_Directory)
gen_myDsl_File_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=myDsl_File)
gen_myDsl_Md_File = Generalization(general=File, specific=myDsl_Md)
gen_myDsl_Js_File = Generalization(general=File, specific=myDsl_Js)
gen_myDsl_Json_File = Generalization(general=File, specific=myDsl_Json)
gen_myDsl_Css_File = Generalization(general=File, specific=myDsl_Css)
gen_myDsl_State_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=myDsl_State)
gen_myDsl_Action_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=myDsl_Action)
gen_myDsl_ActionDispatcher_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=myDsl_ActionDispatcher)
gen_myDsl_Reducer_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=myDsl_Reducer)
gen_myDsl_JsModule_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=myDsl_JsModule)
gen_myDsl_ActionCreator_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=myDsl_ActionCreator)
gen_myDsl_AxiosRequest_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=myDsl_AxiosRequest)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_System, myDsl_EntityName, myDsl_GeneralEntity, myDsl_Domain, myDsl_Property, myDsl_Architecture, myDsl_Technology, myDsl_Type, myDsl_Module, myDsl_RelationDom, myDsl_Submodule, myDsl_Operation, myDsl_EObject, myDsl_Layer, myDsl_LayerSegment, myDsl_LayerSegmentRelation, myDsl_SublayerSegment, AbstractFrontElement, myDsl_SpecialEntity, myDsl_JavaApp, myDsl_Transaction, myDsl_ReactApp, myDsl_Operateson, myDsl_JeeProject, myDsl_Subproject, myDsl_Epackage, myDsl_Component, myDsl_Library, myDsl_RelationArch, myDsl_Attribute, myDsl_MethodBack, myDsl_Annotation, myDsl_AbstractMethod, myDsl_GenericClass, myDsl_Einterface, myDsl_NativeClass, myDsl_Eclass, myDsl_Descriptor, myDsl_AbstractClass, Eclass, myDsl_Functionality, myDsl_Directory, myDsl_JsModule, myDsl_RouterComponent, myDsl_Container, myDsl_Visualizer, myDsl_State, myDsl_AbstractFrontElement, UIComponent, myDsl_UIComponent, myDsl_JsMethod, myDsl_ServiceFront, myDsl_File, myDsl_Md, File, myDsl_Js, myDsl_Json, myDsl_Css, myDsl_Action, myDsl_AxiosRequest, myDsl_Reducer, myDsl_ActionCreator, myDsl_ActionDispatcher, myDsl_JsMethodArgs},
    associations={target17, name19, dom0, properties21, arch1, tech3, types5, modules7, relations9, submodules11, operations13, entities15, layer48, layerSegments50, relations52, sublayerSegments54, type23, name26, properties28, java56, transactions31, react58, operateson33, jeeproject60, operateson35, subproject62, source38, target41, epackage64, componentes44, relationArch46, attribute70, methodClass71, annotation73, abstractMethod75, attribute77, methodClass79, annotation82, abs85, imp88, attribute90, abstractMethod93, attribute96, methodClass98, library66, descriptor68, type101, eclass103, arg106, type109, arg112, type115, elements121, func123, dir125, mod127, route129, wrap131, render133, state135, annotation118, type139, type142, route145, type147, type150, methods153, type155, service137, requests158, file160, subdirectory163, reducer167, actionCreator169, actionDispatcher171, dir173, action165, type176, type179, type182, arguments185, data187},
    generalizations={gen_myDsl_Type_AbstractFrontElement, gen_myDsl_GenericClass_Eclass, gen_myDsl_NativeClass_Eclass, gen_myDsl_AbstractClass_Eclass, gen_myDsl_Annotation_Eclass, gen_myDsl_ReactApp_AbstractFrontElement, gen_myDsl_Functionality_AbstractFrontElement, gen_myDsl_RouterComponent_AbstractFrontElement, gen_myDsl_RouterComponent_UIComponent, gen_myDsl_Container_AbstractFrontElement, gen_myDsl_Visualizer_AbstractFrontElement, gen_myDsl_Visualizer_UIComponent, gen_myDsl_ServiceFront_AbstractFrontElement, gen_myDsl_Directory_AbstractFrontElement, gen_myDsl_File_AbstractFrontElement, gen_myDsl_Md_File, gen_myDsl_Js_File, gen_myDsl_Json_File, gen_myDsl_Css_File, gen_myDsl_State_AbstractFrontElement, gen_myDsl_Action_AbstractFrontElement, gen_myDsl_ActionDispatcher_AbstractFrontElement, gen_myDsl_Reducer_AbstractFrontElement, gen_myDsl_JsModule_AbstractFrontElement, gen_myDsl_ActionCreator_AbstractFrontElement, gen_myDsl_AxiosRequest_AbstractFrontElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)