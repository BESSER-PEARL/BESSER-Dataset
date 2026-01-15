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
dsl_System = Class(name="dsl::System")
dsl_Domain = Class(name="dsl::Domain")
dsl_Architecture = Class(name="dsl::Architecture")
dsl_RelationDom = Class(name="dsl::RelationDom")
dsl_Submodule = Class(name="dsl::Submodule")
dsl_Operation = Class(name="dsl::Operation")
dsl_Technology = Class(name="dsl::Technology")
dsl_Type = Class(name="dsl::Type")
dsl_Module = Class(name="dsl::Module")
dsl_GeneralEntity = Class(name="dsl::GeneralEntity")
dsl_Property = Class(name="dsl::Property")
AbstractFrontElement = Class(name="AbstractFrontElement")
dsl_EObject = Class(name="dsl::EObject")
dsl_EntityName = Class(name="dsl::EntityName")
dsl_Operateson = Class(name="dsl::Operateson")
dsl_SpecialEntity = Class(name="dsl::SpecialEntity")
dsl_Transaction = Class(name="dsl::Transaction")
dsl_Component = Class(name="dsl::Component")
dsl_Layer = Class(name="dsl::Layer")
dsl_RelationArch = Class(name="dsl::RelationArch")
dsl_LayerSegment = Class(name="dsl::LayerSegment")
dsl_SublayerSegment = Class(name="dsl::SublayerSegment")
dsl_LayerSegmentRelation = Class(name="dsl::LayerSegmentRelation")
dsl_ReactApp = Class(name="dsl::ReactApp")
dsl_JavaApp = Class(name="dsl::JavaApp")
dsl_JeeProject = Class(name="dsl::JeeProject")
dsl_Epackage = Class(name="dsl::Epackage")
dsl_Library = Class(name="dsl::Library")
dsl_Descriptor = Class(name="dsl::Descriptor")
dsl_Subproject = Class(name="dsl::Subproject")
dsl_AbstractMethod = Class(name="dsl::AbstractMethod")
dsl_GenericClass = Class(name="dsl::GenericClass")
dsl_AbstractClass = Class(name="dsl::AbstractClass")
Eclass = Class(name="Eclass")
dsl_Attribute = Class(name="dsl::Attribute")
dsl_MethodBack = Class(name="dsl::MethodBack")
dsl_Annotation = Class(name="dsl::Annotation")
dsl_NativeClass = Class(name="dsl::NativeClass")
dsl_Eclass = Class(name="dsl::Eclass")
dsl_Einterface = Class(name="dsl::Einterface")
dsl_AbstractFrontElement = Class(name="dsl::AbstractFrontElement")
dsl_Functionality = Class(name="dsl::Functionality")
dsl_Directory = Class(name="dsl::Directory")
dsl_Container = Class(name="dsl::Container")
dsl_Visualizer = Class(name="dsl::Visualizer")
dsl_State = Class(name="dsl::State")
dsl_ServiceFront = Class(name="dsl::ServiceFront")
dsl_JsModule = Class(name="dsl::JsModule")
dsl_RouterComponent = Class(name="dsl::RouterComponent")
UIComponent = Class(name="UIComponent")
dsl_UIComponent = Class(name="dsl::UIComponent")
dsl_Md = Class(name="dsl::Md")
File = Class(name="File")
dsl_Js = Class(name="dsl::Js")
dsl_Json = Class(name="dsl::Json")
dsl_File = Class(name="dsl::File")
dsl_Reducer = Class(name="dsl::Reducer")
dsl_Css = Class(name="dsl::Css")
dsl_Action = Class(name="dsl::Action")
dsl_ActionCreator = Class(name="dsl::ActionCreator")
dsl_ActionDispatcher = Class(name="dsl::ActionDispatcher")

# dsl_System class attributes and methods

# dsl_Domain class attributes and methods

# dsl_Architecture class attributes and methods

# dsl_RelationDom class attributes and methods

# dsl_Submodule class attributes and methods
dsl_Submodule_name: Property = Property(name="name", type=StringType)
dsl_Submodule.attributes={dsl_Submodule_name}

# dsl_Operation class attributes and methods
dsl_Operation_type: Property = Property(name="type", type=StringType)
dsl_Operation.attributes={dsl_Operation_type}

# dsl_Technology class attributes and methods

# dsl_Type class attributes and methods
dsl_Type_name: Property = Property(name="name", type=StringType)
dsl_Type.attributes={dsl_Type_name}

# dsl_Module class attributes and methods
dsl_Module_name: Property = Property(name="name", type=StringType)
dsl_Module.attributes={dsl_Module_name}

# dsl_GeneralEntity class attributes and methods

# dsl_Property class attributes and methods
dsl_Property_name: Property = Property(name="name", type=StringType)
dsl_Property.attributes={dsl_Property_name}

# AbstractFrontElement class attributes and methods

# dsl_EObject class attributes and methods

# dsl_EntityName class attributes and methods
dsl_EntityName_name: Property = Property(name="name", type=StringType)
dsl_EntityName.attributes={dsl_EntityName_name}

# dsl_Operateson class attributes and methods

# dsl_SpecialEntity class attributes and methods

# dsl_Transaction class attributes and methods
dsl_Transaction_type: Property = Property(name="type", type=StringType)
dsl_Transaction.attributes={dsl_Transaction_type}

# dsl_Component class attributes and methods
dsl_Component_name: Property = Property(name="name", type=StringType)
dsl_Component.attributes={dsl_Component_name}

# dsl_Layer class attributes and methods
dsl_Layer_name: Property = Property(name="name", type=StringType)
dsl_Layer.attributes={dsl_Layer_name}

# dsl_RelationArch class attributes and methods
dsl_RelationArch_name: Property = Property(name="name", type=StringType)
dsl_RelationArch_source: Property = Property(name="source", type=StringType)
dsl_RelationArch.attributes={dsl_RelationArch_source, dsl_RelationArch_name}

# dsl_LayerSegment class attributes and methods
dsl_LayerSegment_name: Property = Property(name="name", type=StringType)
dsl_LayerSegment.attributes={dsl_LayerSegment_name}

# dsl_SublayerSegment class attributes and methods
dsl_SublayerSegment_name: Property = Property(name="name", type=StringType)
dsl_SublayerSegment.attributes={dsl_SublayerSegment_name}

# dsl_LayerSegmentRelation class attributes and methods
dsl_LayerSegmentRelation_layerSegment: Property = Property(name="layerSegment", type=StringType)
dsl_LayerSegmentRelation.attributes={dsl_LayerSegmentRelation_layerSegment}

# dsl_ReactApp class attributes and methods

# dsl_JavaApp class attributes and methods

# dsl_JeeProject class attributes and methods
dsl_JeeProject_name: Property = Property(name="name", type=StringType)
dsl_JeeProject.attributes={dsl_JeeProject_name}

# dsl_Epackage class attributes and methods
dsl_Epackage_name: Property = Property(name="name", type=StringType)
dsl_Epackage.attributes={dsl_Epackage_name}

# dsl_Library class attributes and methods
dsl_Library_name: Property = Property(name="name", type=StringType)
dsl_Library_isNative: Property = Property(name="isNative", type=StringType)
dsl_Library.attributes={dsl_Library_isNative, dsl_Library_name}

# dsl_Descriptor class attributes and methods
dsl_Descriptor_name: Property = Property(name="name", type=StringType)
dsl_Descriptor.attributes={dsl_Descriptor_name}

# dsl_Subproject class attributes and methods
dsl_Subproject_name: Property = Property(name="name", type=StringType)
dsl_Subproject.attributes={dsl_Subproject_name}

# dsl_AbstractMethod class attributes and methods
dsl_AbstractMethod_name: Property = Property(name="name", type=StringType)
dsl_AbstractMethod.attributes={dsl_AbstractMethod_name}

# dsl_GenericClass class attributes and methods

# dsl_AbstractClass class attributes and methods

# Eclass class attributes and methods

# dsl_Attribute class attributes and methods
dsl_Attribute_name: Property = Property(name="name", type=StringType)
dsl_Attribute.attributes={dsl_Attribute_name}

# dsl_MethodBack class attributes and methods
dsl_MethodBack_name: Property = Property(name="name", type=StringType)
dsl_MethodBack.attributes={dsl_MethodBack_name}

# dsl_Annotation class attributes and methods
dsl_Annotation_propertie: Property = Property(name="propertie", type=StringType)
dsl_Annotation.attributes={dsl_Annotation_propertie}

# dsl_NativeClass class attributes and methods

# dsl_Eclass class attributes and methods
dsl_Eclass_name: Property = Property(name="name", type=StringType)
dsl_Eclass.attributes={dsl_Eclass_name}

# dsl_Einterface class attributes and methods
dsl_Einterface_name: Property = Property(name="name", type=StringType)
dsl_Einterface.attributes={dsl_Einterface_name}

# dsl_AbstractFrontElement class attributes and methods

# dsl_Functionality class attributes and methods
dsl_Functionality_name: Property = Property(name="name", type=StringType)
dsl_Functionality.attributes={dsl_Functionality_name}

# dsl_Directory class attributes and methods
dsl_Directory_purpose: Property = Property(name="purpose", type=StringType)
dsl_Directory_name: Property = Property(name="name", type=StringType)
dsl_Directory.attributes={dsl_Directory_purpose, dsl_Directory_name}

# dsl_Container class attributes and methods
dsl_Container_name: Property = Property(name="name", type=StringType)
dsl_Container.attributes={dsl_Container_name}

# dsl_Visualizer class attributes and methods
dsl_Visualizer_name: Property = Property(name="name", type=StringType)
dsl_Visualizer.attributes={dsl_Visualizer_name}

# dsl_State class attributes and methods
dsl_State_name: Property = Property(name="name", type=StringType)
dsl_State.attributes={dsl_State_name}

# dsl_ServiceFront class attributes and methods
dsl_ServiceFront_name: Property = Property(name="name", type=StringType)
dsl_ServiceFront_method: Property = Property(name="method", type=StringType)
dsl_ServiceFront.attributes={dsl_ServiceFront_method, dsl_ServiceFront_name}

# dsl_JsModule class attributes and methods
dsl_JsModule_name: Property = Property(name="name", type=StringType)
dsl_JsModule.attributes={dsl_JsModule_name}

# dsl_RouterComponent class attributes and methods
dsl_RouterComponent_name: Property = Property(name="name", type=StringType)
dsl_RouterComponent.attributes={dsl_RouterComponent_name}

# UIComponent class attributes and methods

# dsl_UIComponent class attributes and methods

# dsl_Md class attributes and methods

# File class attributes and methods

# dsl_Js class attributes and methods

# dsl_Json class attributes and methods

# dsl_File class attributes and methods
dsl_File_name: Property = Property(name="name", type=StringType)
dsl_File_type: Property = Property(name="type", type=StringType)
dsl_File.attributes={dsl_File_name, dsl_File_type}

# dsl_Reducer class attributes and methods
dsl_Reducer_name: Property = Property(name="name", type=StringType)
dsl_Reducer.attributes={dsl_Reducer_name}

# dsl_Css class attributes and methods

# dsl_Action class attributes and methods
dsl_Action_name: Property = Property(name="name", type=StringType)
dsl_Action.attributes={dsl_Action_name}

# dsl_ActionCreator class attributes and methods
dsl_ActionCreator_name: Property = Property(name="name", type=StringType)
dsl_ActionCreator_type: Property = Property(name="type", type=StringType)
dsl_ActionCreator.attributes={dsl_ActionCreator_name, dsl_ActionCreator_type}

# dsl_ActionDispatcher class attributes and methods
dsl_ActionDispatcher_name: Property = Property(name="name", type=StringType)
dsl_ActionDispatcher.attributes={dsl_ActionDispatcher_name}

# Relationships
dom0: BinaryAssociation = BinaryAssociation(
    name="dom0",
    ends={
        Property(name="dsl_Domain", type=dsl_System, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_System", type=dsl_Domain, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arch1: BinaryAssociation = BinaryAssociation(
    name="arch1",
    ends={
        Property(name="dsl_Architecture", type=dsl_System, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_System2", type=dsl_Architecture, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relations9: BinaryAssociation = BinaryAssociation(
    name="relations9",
    ends={
        Property(name="dsl_RelationDom", type=dsl_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Domain10", type=dsl_RelationDom, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
submodules11: BinaryAssociation = BinaryAssociation(
    name="submodules11",
    ends={
        Property(name="dsl_Submodule", type=dsl_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Module12", type=dsl_Submodule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations13: BinaryAssociation = BinaryAssociation(
    name="operations13",
    ends={
        Property(name="dsl_Operation", type=dsl_Submodule, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Submodule14", type=dsl_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tech3: BinaryAssociation = BinaryAssociation(
    name="tech3",
    ends={
        Property(name="dsl_Technology", type=dsl_System, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_System4", type=dsl_Technology, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types5: BinaryAssociation = BinaryAssociation(
    name="types5",
    ends={
        Property(name="dsl_Type", type=dsl_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Domain6", type=dsl_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modules7: BinaryAssociation = BinaryAssociation(
    name="modules7",
    ends={
        Property(name="dsl_Module", type=dsl_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Domain8", type=dsl_Module, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name19: BinaryAssociation = BinaryAssociation(
    name="name19",
    ends={
        Property(name="dsl_EntityName20", type=dsl_GeneralEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_GeneralEntity", type=dsl_EntityName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties21: BinaryAssociation = BinaryAssociation(
    name="properties21",
    ends={
        Property(name="dsl_Property", type=dsl_GeneralEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_GeneralEntity22", type=dsl_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type23: BinaryAssociation = BinaryAssociation(
    name="type23",
    ends={
        Property(name="dsl_Type25", type=dsl_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Property24", type=dsl_Type, multiplicity=Multiplicity(0, 1))
    }
)
entities15: BinaryAssociation = BinaryAssociation(
    name="entities15",
    ends={
        Property(name="dsl_EObject", type=dsl_Submodule, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Submodule16", type=dsl_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="dsl_EntityName", type=dsl_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Operation18", type=dsl_EntityName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operateson33: BinaryAssociation = BinaryAssociation(
    name="operateson33",
    ends={
        Property(name="dsl_Operateson", type=dsl_Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Transaction34", type=dsl_Operateson, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operateson35: BinaryAssociation = BinaryAssociation(
    name="operateson35",
    ends={
        Property(name="dsl_EntityName37", type=dsl_Operateson, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Operateson36", type=dsl_EntityName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name26: BinaryAssociation = BinaryAssociation(
    name="name26",
    ends={
        Property(name="dsl_EntityName27", type=dsl_SpecialEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_SpecialEntity", type=dsl_EntityName, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties28: BinaryAssociation = BinaryAssociation(
    name="properties28",
    ends={
        Property(name="dsl_Property30", type=dsl_SpecialEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_SpecialEntity29", type=dsl_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transactions31: BinaryAssociation = BinaryAssociation(
    name="transactions31",
    ends={
        Property(name="dsl_Transaction", type=dsl_SpecialEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_SpecialEntity32", type=dsl_Transaction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target41: BinaryAssociation = BinaryAssociation(
    name="target41",
    ends={
        Property(name="dsl_RelationDom42", type=dsl_EntityName, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="dsl_EntityName43", type=dsl_RelationDom, multiplicity=Multiplicity(1, 1))
    }
)
componentes44: BinaryAssociation = BinaryAssociation(
    name="componentes44",
    ends={
        Property(name="dsl_Component", type=dsl_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Architecture45", type=dsl_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source38: BinaryAssociation = BinaryAssociation(
    name="source38",
    ends={
        Property(name="dsl_EntityName40", type=dsl_RelationDom, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_RelationDom39", type=dsl_EntityName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationArch46: BinaryAssociation = BinaryAssociation(
    name="relationArch46",
    ends={
        Property(name="dsl_RelationArch", type=dsl_Architecture, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Architecture47", type=dsl_RelationArch, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layerSegments50: BinaryAssociation = BinaryAssociation(
    name="layerSegments50",
    ends={
        Property(name="dsl_LayerSegment", type=dsl_Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Layer51", type=dsl_LayerSegment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layer48: BinaryAssociation = BinaryAssociation(
    name="layer48",
    ends={
        Property(name="dsl_Layer", type=dsl_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Component49", type=dsl_Layer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations52: BinaryAssociation = BinaryAssociation(
    name="relations52",
    ends={
        Property(name="dsl_LayerSegmentRelation", type=dsl_LayerSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_LayerSegment53", type=dsl_LayerSegmentRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sublayerSegments54: BinaryAssociation = BinaryAssociation(
    name="sublayerSegments54",
    ends={
        Property(name="dsl_SublayerSegment", type=dsl_LayerSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_LayerSegment55", type=dsl_SublayerSegment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
java56: BinaryAssociation = BinaryAssociation(
    name="java56",
    ends={
        Property(name="dsl_Technology57", type=dsl_JavaApp, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="dsl_JavaApp", type=dsl_Technology, multiplicity=Multiplicity(1, 1))
    }
)
react58: BinaryAssociation = BinaryAssociation(
    name="react58",
    ends={
        Property(name="dsl_ReactApp", type=dsl_Technology, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Technology59", type=dsl_ReactApp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
jeeproject60: BinaryAssociation = BinaryAssociation(
    name="jeeproject60",
    ends={
        Property(name="dsl_JeeProject", type=dsl_JavaApp, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_JavaApp61", type=dsl_JeeProject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
epackage64: BinaryAssociation = BinaryAssociation(
    name="epackage64",
    ends={
        Property(name="dsl_Epackage", type=dsl_Subproject, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Subproject65", type=dsl_Epackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
library66: BinaryAssociation = BinaryAssociation(
    name="library66",
    ends={
        Property(name="dsl_Library", type=dsl_Subproject, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Subproject67", type=dsl_Library, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
descriptor68: BinaryAssociation = BinaryAssociation(
    name="descriptor68",
    ends={
        Property(name="dsl_Descriptor", type=dsl_Subproject, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Subproject69", type=dsl_Descriptor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subproject62: BinaryAssociation = BinaryAssociation(
    name="subproject62",
    ends={
        Property(name="dsl_Subproject", type=dsl_JeeProject, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_JeeProject63", type=dsl_Subproject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abstractMethod75: BinaryAssociation = BinaryAssociation(
    name="abstractMethod75",
    ends={
        Property(name="dsl_AbstractMethod", type=dsl_AbstractClass, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AbstractClass76", type=dsl_AbstractMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute77: BinaryAssociation = BinaryAssociation(
    name="attribute77",
    ends={
        Property(name="dsl_Attribute78", type=dsl_GenericClass, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_GenericClass", type=dsl_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodClass79: BinaryAssociation = BinaryAssociation(
    name="methodClass79",
    ends={
        Property(name="dsl_MethodBack81", type=dsl_GenericClass, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_GenericClass80", type=dsl_MethodBack, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation82: BinaryAssociation = BinaryAssociation(
    name="annotation82",
    ends={
        Property(name="dsl_Annotation84", type=dsl_GenericClass, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_GenericClass83", type=dsl_Annotation, multiplicity=Multiplicity(0, 1))
    }
)
attribute70: BinaryAssociation = BinaryAssociation(
    name="attribute70",
    ends={
        Property(name="dsl_Attribute", type=dsl_AbstractClass, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AbstractClass", type=dsl_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodClass71: BinaryAssociation = BinaryAssociation(
    name="methodClass71",
    ends={
        Property(name="dsl_MethodBack", type=dsl_AbstractClass, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AbstractClass72", type=dsl_MethodBack, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation73: BinaryAssociation = BinaryAssociation(
    name="annotation73",
    ends={
        Property(name="dsl_Annotation", type=dsl_AbstractClass, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AbstractClass74", type=dsl_Annotation, multiplicity=Multiplicity(0, 1))
    }
)
abstractMethod93: BinaryAssociation = BinaryAssociation(
    name="abstractMethod93",
    ends={
        Property(name="dsl_AbstractMethod95", type=dsl_Einterface, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Einterface94", type=dsl_AbstractMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute96: BinaryAssociation = BinaryAssociation(
    name="attribute96",
    ends={
        Property(name="dsl_Attribute97", type=dsl_NativeClass, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_NativeClass", type=dsl_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methodClass98: BinaryAssociation = BinaryAssociation(
    name="methodClass98",
    ends={
        Property(name="dsl_MethodBack100", type=dsl_NativeClass, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_NativeClass99", type=dsl_MethodBack, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abs85: BinaryAssociation = BinaryAssociation(
    name="abs85",
    ends={
        Property(name="dsl_AbstractClass87", type=dsl_GenericClass, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_GenericClass86", type=dsl_AbstractClass, multiplicity=Multiplicity(0, 1))
    }
)
imp88: BinaryAssociation = BinaryAssociation(
    name="imp88",
    ends={
        Property(name="dsl_Einterface", type=dsl_GenericClass, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_GenericClass89", type=dsl_Einterface, multiplicity=Multiplicity(0, 1))
    }
)
attribute90: BinaryAssociation = BinaryAssociation(
    name="attribute90",
    ends={
        Property(name="dsl_Attribute92", type=dsl_Einterface, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Einterface91", type=dsl_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arg106: BinaryAssociation = BinaryAssociation(
    name="arg106",
    ends={
        Property(name="dsl_Eclass108", type=dsl_MethodBack, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MethodBack107", type=dsl_Eclass, multiplicity=Multiplicity(0, 1))
    }
)
type109: BinaryAssociation = BinaryAssociation(
    name="type109",
    ends={
        Property(name="dsl_Eclass111", type=dsl_MethodBack, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_MethodBack110", type=dsl_Eclass, multiplicity=Multiplicity(0, 1))
    }
)
arg112: BinaryAssociation = BinaryAssociation(
    name="arg112",
    ends={
        Property(name="dsl_Eclass114", type=dsl_AbstractMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AbstractMethod113", type=dsl_Eclass, multiplicity=Multiplicity(0, 1))
    }
)
type101: BinaryAssociation = BinaryAssociation(
    name="type101",
    ends={
        Property(name="dsl_Eclass", type=dsl_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Attribute102", type=dsl_Eclass, multiplicity=Multiplicity(0, 1))
    }
)
eclass103: BinaryAssociation = BinaryAssociation(
    name="eclass103",
    ends={
        Property(name="dsl_Eclass105", type=dsl_Epackage, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Epackage104", type=dsl_Eclass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation118: BinaryAssociation = BinaryAssociation(
    name="annotation118",
    ends={
        Property(name="dsl_Annotation120", type=dsl_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Library119", type=dsl_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements121: BinaryAssociation = BinaryAssociation(
    name="elements121",
    ends={
        Property(name="dsl_AbstractFrontElement", type=dsl_ReactApp, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ReactApp122", type=dsl_AbstractFrontElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
func123: BinaryAssociation = BinaryAssociation(
    name="func123",
    ends={
        Property(name="dsl_Functionality", type=dsl_ReactApp, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ReactApp124", type=dsl_Functionality, multiplicity=Multiplicity(0, 1))
    }
)
dir125: BinaryAssociation = BinaryAssociation(
    name="dir125",
    ends={
        Property(name="dsl_Directory", type=dsl_ReactApp, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ReactApp126", type=dsl_Directory, multiplicity=Multiplicity(0, 1))
    }
)
type115: BinaryAssociation = BinaryAssociation(
    name="type115",
    ends={
        Property(name="dsl_Eclass117", type=dsl_AbstractMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_AbstractMethod116", type=dsl_Eclass, multiplicity=Multiplicity(0, 1))
    }
)
wrap131: BinaryAssociation = BinaryAssociation(
    name="wrap131",
    ends={
        Property(name="dsl_Container", type=dsl_Functionality, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Functionality132", type=dsl_Container, multiplicity=Multiplicity(0, 1))
    }
)
render133: BinaryAssociation = BinaryAssociation(
    name="render133",
    ends={
        Property(name="dsl_Visualizer", type=dsl_Functionality, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Functionality134", type=dsl_Visualizer, multiplicity=Multiplicity(0, 1))
    }
)
state135: BinaryAssociation = BinaryAssociation(
    name="state135",
    ends={
        Property(name="dsl_State", type=dsl_Functionality, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Functionality136", type=dsl_State, multiplicity=Multiplicity(0, 1))
    }
)
service137: BinaryAssociation = BinaryAssociation(
    name="service137",
    ends={
        Property(name="dsl_ServiceFront", type=dsl_Functionality, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Functionality138", type=dsl_ServiceFront, multiplicity=Multiplicity(0, 1))
    }
)
type139: BinaryAssociation = BinaryAssociation(
    name="type139",
    ends={
        Property(name="dsl_Directory141", type=dsl_Functionality, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Functionality140", type=dsl_Directory, multiplicity=Multiplicity(0, 1))
    }
)
mod127: BinaryAssociation = BinaryAssociation(
    name="mod127",
    ends={
        Property(name="dsl_JsModule", type=dsl_ReactApp, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ReactApp128", type=dsl_JsModule, multiplicity=Multiplicity(0, 1))
    }
)
route129: BinaryAssociation = BinaryAssociation(
    name="route129",
    ends={
        Property(name="dsl_RouterComponent", type=dsl_Functionality, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Functionality130", type=dsl_RouterComponent, multiplicity=Multiplicity(0, 1))
    }
)
type147: BinaryAssociation = BinaryAssociation(
    name="type147",
    ends={
        Property(name="dsl_AbstractFrontElement149", type=dsl_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Container148", type=dsl_AbstractFrontElement, multiplicity=Multiplicity(0, 1))
    }
)
type150: BinaryAssociation = BinaryAssociation(
    name="type150",
    ends={
        Property(name="dsl_AbstractFrontElement152", type=dsl_Visualizer, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Visualizer151", type=dsl_AbstractFrontElement, multiplicity=Multiplicity(0, 1))
    }
)
type142: BinaryAssociation = BinaryAssociation(
    name="type142",
    ends={
        Property(name="dsl_AbstractFrontElement144", type=dsl_RouterComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_RouterComponent143", type=dsl_AbstractFrontElement, multiplicity=Multiplicity(0, 1))
    }
)
route145: BinaryAssociation = BinaryAssociation(
    name="route145",
    ends={
        Property(name="dsl_UIComponent", type=dsl_RouterComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_RouterComponent146", type=dsl_UIComponent, multiplicity=Multiplicity(0, 1))
    }
)
subdirectory159: BinaryAssociation = BinaryAssociation(
    name="subdirectory159",
    ends={
        Property(name="dsl_Directory160", type=dsl_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Directory158", type=dsl_Directory, multiplicity=Multiplicity(0, 1))
    }
)
type153: BinaryAssociation = BinaryAssociation(
    name="type153",
    ends={
        Property(name="dsl_JsModule155", type=dsl_ServiceFront, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ServiceFront154", type=dsl_JsModule, multiplicity=Multiplicity(0, 1))
    }
)
file156: BinaryAssociation = BinaryAssociation(
    name="file156",
    ends={
        Property(name="dsl_File", type=dsl_Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Directory157", type=dsl_File, multiplicity=Multiplicity(0, 1))
    }
)
reducer163: BinaryAssociation = BinaryAssociation(
    name="reducer163",
    ends={
        Property(name="dsl_Reducer", type=dsl_State, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_State164", type=dsl_Reducer, multiplicity=Multiplicity(0, 1))
    }
)
action161: BinaryAssociation = BinaryAssociation(
    name="action161",
    ends={
        Property(name="dsl_Action", type=dsl_State, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_State162", type=dsl_Action, multiplicity=Multiplicity(0, 1))
    }
)
actionCreator165: BinaryAssociation = BinaryAssociation(
    name="actionCreator165",
    ends={
        Property(name="dsl_ActionCreator", type=dsl_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Action166", type=dsl_ActionCreator, multiplicity=Multiplicity(0, 1))
    }
)
dir169: BinaryAssociation = BinaryAssociation(
    name="dir169",
    ends={
        Property(name="dsl_Directory171", type=dsl_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Action170", type=dsl_Directory, multiplicity=Multiplicity(0, 1))
    }
)
actionDispatcher167: BinaryAssociation = BinaryAssociation(
    name="actionDispatcher167",
    ends={
        Property(name="dsl_ActionDispatcher", type=dsl_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Action168", type=dsl_ActionDispatcher, multiplicity=Multiplicity(0, 1))
    }
)
type175: BinaryAssociation = BinaryAssociation(
    name="type175",
    ends={
        Property(name="dsl_AbstractFrontElement177", type=dsl_Reducer, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Reducer176", type=dsl_AbstractFrontElement, multiplicity=Multiplicity(0, 1))
    }
)
type172: BinaryAssociation = BinaryAssociation(
    name="type172",
    ends={
        Property(name="dsl_ActionCreator174", type=dsl_ActionDispatcher, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_ActionDispatcher173", type=dsl_ActionCreator, multiplicity=Multiplicity(0, 1))
    }
)
type178: BinaryAssociation = BinaryAssociation(
    name="type178",
    ends={
        Property(name="dsl_Directory180", type=dsl_JsModule, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_JsModule179", type=dsl_Directory, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_dsl_Type_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=dsl_Type)
gen_dsl_GenericClass_Eclass = Generalization(general=Eclass, specific=dsl_GenericClass)
gen_dsl_AbstractClass_Eclass = Generalization(general=Eclass, specific=dsl_AbstractClass)
gen_dsl_NativeClass_Eclass = Generalization(general=Eclass, specific=dsl_NativeClass)
gen_dsl_ReactApp_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=dsl_ReactApp)
gen_dsl_Annotation_Eclass = Generalization(general=Eclass, specific=dsl_Annotation)
gen_dsl_Functionality_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=dsl_Functionality)
gen_dsl_Container_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=dsl_Container)
gen_dsl_Visualizer_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=dsl_Visualizer)
gen_dsl_Visualizer_UIComponent = Generalization(general=UIComponent, specific=dsl_Visualizer)
gen_dsl_ServiceFront_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=dsl_ServiceFront)
gen_dsl_RouterComponent_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=dsl_RouterComponent)
gen_dsl_RouterComponent_UIComponent = Generalization(general=UIComponent, specific=dsl_RouterComponent)
gen_dsl_File_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=dsl_File)
gen_dsl_Md_File = Generalization(general=File, specific=dsl_Md)
gen_dsl_Js_File = Generalization(general=File, specific=dsl_Js)
gen_dsl_Json_File = Generalization(general=File, specific=dsl_Json)
gen_dsl_Directory_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=dsl_Directory)
gen_dsl_Css_File = Generalization(general=File, specific=dsl_Css)
gen_dsl_State_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=dsl_State)
gen_dsl_Action_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=dsl_Action)
gen_dsl_ActionCreator_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=dsl_ActionCreator)
gen_dsl_ActionDispatcher_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=dsl_ActionDispatcher)
gen_dsl_Reducer_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=dsl_Reducer)
gen_dsl_JsModule_AbstractFrontElement = Generalization(general=AbstractFrontElement, specific=dsl_JsModule)

# Domain Model
domain_model = DomainModel(
    name="dsl",
    types={dsl_System, dsl_Domain, dsl_Architecture, dsl_RelationDom, dsl_Submodule, dsl_Operation, dsl_Technology, dsl_Type, dsl_Module, dsl_GeneralEntity, dsl_Property, AbstractFrontElement, dsl_EObject, dsl_EntityName, dsl_Operateson, dsl_SpecialEntity, dsl_Transaction, dsl_Component, dsl_Layer, dsl_RelationArch, dsl_LayerSegment, dsl_SublayerSegment, dsl_LayerSegmentRelation, dsl_ReactApp, dsl_JavaApp, dsl_JeeProject, dsl_Epackage, dsl_Library, dsl_Descriptor, dsl_Subproject, dsl_AbstractMethod, dsl_GenericClass, dsl_AbstractClass, Eclass, dsl_Attribute, dsl_MethodBack, dsl_Annotation, dsl_NativeClass, dsl_Eclass, dsl_Einterface, dsl_AbstractFrontElement, dsl_Functionality, dsl_Directory, dsl_Container, dsl_Visualizer, dsl_State, dsl_ServiceFront, dsl_JsModule, dsl_RouterComponent, UIComponent, dsl_UIComponent, dsl_Md, File, dsl_Js, dsl_Json, dsl_File, dsl_Reducer, dsl_Css, dsl_Action, dsl_ActionCreator, dsl_ActionDispatcher},
    associations={dom0, arch1, relations9, submodules11, operations13, tech3, types5, modules7, name19, properties21, type23, entities15, target17, operateson33, operateson35, name26, properties28, transactions31, target41, componentes44, source38, relationArch46, layerSegments50, layer48, relations52, sublayerSegments54, java56, react58, jeeproject60, epackage64, library66, descriptor68, subproject62, abstractMethod75, attribute77, methodClass79, annotation82, attribute70, methodClass71, annotation73, abstractMethod93, attribute96, methodClass98, abs85, imp88, attribute90, arg106, type109, arg112, type101, eclass103, annotation118, elements121, func123, dir125, type115, wrap131, render133, state135, service137, type139, mod127, route129, type147, type150, type142, route145, subdirectory159, type153, file156, reducer163, action161, actionCreator165, dir169, actionDispatcher167, type175, type172, type178},
    generalizations={gen_dsl_Type_AbstractFrontElement, gen_dsl_GenericClass_Eclass, gen_dsl_AbstractClass_Eclass, gen_dsl_NativeClass_Eclass, gen_dsl_ReactApp_AbstractFrontElement, gen_dsl_Annotation_Eclass, gen_dsl_Functionality_AbstractFrontElement, gen_dsl_Container_AbstractFrontElement, gen_dsl_Visualizer_AbstractFrontElement, gen_dsl_Visualizer_UIComponent, gen_dsl_ServiceFront_AbstractFrontElement, gen_dsl_RouterComponent_AbstractFrontElement, gen_dsl_RouterComponent_UIComponent, gen_dsl_File_AbstractFrontElement, gen_dsl_Md_File, gen_dsl_Js_File, gen_dsl_Json_File, gen_dsl_Directory_AbstractFrontElement, gen_dsl_Css_File, gen_dsl_State_AbstractFrontElement, gen_dsl_Action_AbstractFrontElement, gen_dsl_ActionCreator_AbstractFrontElement, gen_dsl_ActionDispatcher_AbstractFrontElement, gen_dsl_Reducer_AbstractFrontElement, gen_dsl_JsModule_AbstractFrontElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)