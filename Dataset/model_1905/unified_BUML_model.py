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
UnifiedMetamodel__Ejb = Class(name="UnifiedMetamodel::::Ejb")
Layer = Class(name="Layer")
UnifiedMetamodel__Store = Class(name="UnifiedMetamodel::::Store")
UnifiedMetamodel__UI = Class(name="UnifiedMetamodel::::UI")
UnifiedMetamodel__Layer = Class(name="UnifiedMetamodel::::Layer")
UnifiedMetamodel__RestEntity = Class(name="UnifiedMetamodel::::RestEntity")
UnifiedMetamodel__Facade = Class(name="UnifiedMetamodel::::Facade")
UnifiedMetamodel__War = Class(name="UnifiedMetamodel::::War")
UnifiedMetamodel__Component = Class(name="UnifiedMetamodel::::Component")
UnifiedMetamodel__LayerSegment = Class(name="UnifiedMetamodel::::LayerSegment")
UnifiedMetamodel__SubLayerSegment = Class(name="UnifiedMetamodel::::SubLayerSegment")
UnifiedMetamodel__Dto = Class(name="UnifiedMetamodel::::Dto")
LayerSegment = Class(name="LayerSegment")
UnifiedMetamodel__Containers = Class(name="UnifiedMetamodel::::Containers")
UnifiedMetamodel__Pojo = Class(name="UnifiedMetamodel::::Pojo")
UnifiedMetamodel__Services = Class(name="UnifiedMetamodel::::Services")
UnifiedMetamodel__Metamodel = Class(name="UnifiedMetamodel::::Metamodel")
UnifiedMetamodel__DomainMetamodel = Class(name="UnifiedMetamodel::::DomainMetamodel")
UnifiedMetamodel__TechnologyMetamodel = Class(name="UnifiedMetamodel::::TechnologyMetamodel")
UnifiedMetamodel__RelationArch = Class(name="UnifiedMetamodel::::RelationArch")
UnifiedMetamodel__ArquitectureMetamodel = Class(name="UnifiedMetamodel::::ArquitectureMetamodel")
UnifiedMetamodel__Composition = Class(name="UnifiedMetamodel::::Composition")
RelationDom = Class(name="RelationDom")
UnifiedMetamodel__Operations = Class(name="UnifiedMetamodel::::Operations")
UnifiedMetamodel__Entity = Class(name="UnifiedMetamodel::::Entity")
UnifiedMetamodel__Module = Class(name="UnifiedMetamodel::::Module")
UnifiedMetamodel__Submodule = Class(name="UnifiedMetamodel::::Submodule")
UnifiedMetamodel__SpecialEntity = Class(name="UnifiedMetamodel::::SpecialEntity")
Entity = Class(name="Entity")
UnifiedMetamodel__Transaction = Class(name="UnifiedMetamodel::::Transaction")
UnifiedMetamodel__GeneralEntity = Class(name="UnifiedMetamodel::::GeneralEntity")
UnifiedMetamodel__Read = Class(name="UnifiedMetamodel::::Read")
Operations = Class(name="Operations")
UnifiedMetamodel__Create = Class(name="UnifiedMetamodel::::Create")
UnifiedMetamodel__Sale = Class(name="UnifiedMetamodel::::Sale")
Transaction = Class(name="Transaction")
UnifiedMetamodel__Exchange = Class(name="UnifiedMetamodel::::Exchange")
UnifiedMetamodel__Property = Class(name="UnifiedMetamodel::::Property")
UnifiedMetamodel__RelationDom = Class(name="UnifiedMetamodel::::RelationDom")
UnifiedMetamodel__MD = Class(name="UnifiedMetamodel::::MD")
UnifiedMetamodel__CSS = Class(name="UnifiedMetamodel::::CSS")
UnifiedMetamodel__APICall = Class(name="UnifiedMetamodel::::APICall")
UnifiedMetamodel__Directory = Class(name="UnifiedMetamodel::::Directory")
UnifiedMetamodel__File = Class(name="UnifiedMetamodel::::File")
UnifiedMetamodel__ActionDispatcher = Class(name="UnifiedMetamodel::::ActionDispatcher")
UnifiedMetamodel__ActionCreator = Class(name="UnifiedMetamodel::::ActionCreator")
UnifiedMetamodel__Router = Class(name="UnifiedMetamodel::::Router")
ModuleFront = Class(name="ModuleFront")
UnifiedMetamodel__JSON = Class(name="UnifiedMetamodel::::JSON")
UnifiedMetamodel__UIFront = Class(name="UnifiedMetamodel::::UIFront")
File = Class(name="File")
ComponentFront = Class(name="ComponentFront")
UnifiedMetamodel__Visualizer = Class(name="UnifiedMetamodel::::Visualizer")
UIFront = Class(name="UIFront")
UnifiedMetamodel__Design = Class(name="UnifiedMetamodel::::Design")
UnifiedMetamodel__RouterComponent = Class(name="UnifiedMetamodel::::RouterComponent")
UnifiedMetamodel__Container = Class(name="UnifiedMetamodel::::Container")
UnifiedMetamodel__State = Class(name="UnifiedMetamodel::::State")
UnifiedMetamodel__Action = Class(name="UnifiedMetamodel::::Action")
UnifiedMetamodel__Reducer = Class(name="UnifiedMetamodel::::Reducer")
UnifiedMetamodel__ModuleFront = Class(name="UnifiedMetamodel::::ModuleFront")
UnifiedMetamodel__Functionality = Class(name="UnifiedMetamodel::::Functionality")
UnifiedMetamodel__ComponentFront = Class(name="UnifiedMetamodel::::ComponentFront")
UnifiedMetamodel__JS = Class(name="UnifiedMetamodel::::JS")
UnifiedMetamodel__ServicesFront = Class(name="UnifiedMetamodel::::ServicesFront")
UnifiedMetamodel__Redux = Class(name="UnifiedMetamodel::::Redux")
UnifiedMetamodel__ReactApp = Class(name="UnifiedMetamodel::::ReactApp")
UnifiedMetamodel__JavaApp = Class(name="UnifiedMetamodel::::JavaApp")
UnifiedMetamodel__JEE_Project = Class(name="UnifiedMetamodel::::JEE::Project")
UnifiedMetamodel__Subproject = Class(name="UnifiedMetamodel::::Subproject")
UnifiedMetamodel__Annotation = Class(name="UnifiedMetamodel::::Annotation")
UnifiedMetamodel__Attribute = Class(name="UnifiedMetamodel::::Attribute")
UnifiedMetamodel__EClass = Class(name="UnifiedMetamodel::::EClass")
UnifiedMetamodel__GenericClass = Class(name="UnifiedMetamodel::::GenericClass")
UnifiedMetamodel__NativeClass = Class(name="UnifiedMetamodel::::NativeClass")
EClass = Class(name="EClass")
UnifiedMetamodel__EInterface = Class(name="UnifiedMetamodel::::EInterface")
UnifiedMetamodel__AbstractMethod = Class(name="UnifiedMetamodel::::AbstractMethod")
UnifiedMetamodel__Library = Class(name="UnifiedMetamodel::::Library")
UnifiedMetamodel__Epackage = Class(name="UnifiedMetamodel::::Epackage")
UnifiedMetamodel__AbstractClass = Class(name="UnifiedMetamodel::::AbstractClass")
UnifiedMetamodel__MethodBack = Class(name="UnifiedMetamodel::::MethodBack")
UnifiedMetamodel__Descriptor = Class(name="UnifiedMetamodel::::Descriptor")
UnifiedMetamodel__JavaScript = Class(name="UnifiedMetamodel::::JavaScript")
UnifiedMetamodel__React = Class(name="UnifiedMetamodel::::React")
UnifiedMetamodel__Util = Class(name="UnifiedMetamodel::::Util")
UnifiedMetamodel__Reducers = Class(name="UnifiedMetamodel::::Reducers")
SubLayerSegment = Class(name="SubLayerSegment")
UnifiedMetamodel__Actions = Class(name="UnifiedMetamodel::::Actions")
UnifiedMetamodel__Back = Class(name="UnifiedMetamodel::::Back")
Component = Class(name="Component")
UnifiedMetamodel__Front = Class(name="UnifiedMetamodel::::Front")

# UnifiedMetamodel__Ejb class attributes and methods

# Layer class attributes and methods

# UnifiedMetamodel__Store class attributes and methods

# UnifiedMetamodel__UI class attributes and methods

# UnifiedMetamodel__Layer class attributes and methods
UnifiedMetamodel__Layer_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Layer.attributes={UnifiedMetamodel__Layer_name}

# UnifiedMetamodel__RestEntity class attributes and methods

# UnifiedMetamodel__Facade class attributes and methods

# UnifiedMetamodel__War class attributes and methods

# UnifiedMetamodel__Component class attributes and methods
UnifiedMetamodel__Component_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Component.attributes={UnifiedMetamodel__Component_name}

# UnifiedMetamodel__LayerSegment class attributes and methods

# UnifiedMetamodel__SubLayerSegment class attributes and methods

# UnifiedMetamodel__Dto class attributes and methods

# LayerSegment class attributes and methods

# UnifiedMetamodel__Containers class attributes and methods

# UnifiedMetamodel__Pojo class attributes and methods

# UnifiedMetamodel__Services class attributes and methods

# UnifiedMetamodel__Metamodel class attributes and methods
UnifiedMetamodel__Metamodel_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Metamodel.attributes={UnifiedMetamodel__Metamodel_name}

# UnifiedMetamodel__DomainMetamodel class attributes and methods

# UnifiedMetamodel__TechnologyMetamodel class attributes and methods

# UnifiedMetamodel__RelationArch class attributes and methods
UnifiedMetamodel__RelationArch_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__RelationArch.attributes={UnifiedMetamodel__RelationArch_name}

# UnifiedMetamodel__ArquitectureMetamodel class attributes and methods

# UnifiedMetamodel__Composition class attributes and methods

# RelationDom class attributes and methods

# UnifiedMetamodel__Operations class attributes and methods

# UnifiedMetamodel__Entity class attributes and methods
UnifiedMetamodel__Entity_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Entity.attributes={UnifiedMetamodel__Entity_name}

# UnifiedMetamodel__Module class attributes and methods
UnifiedMetamodel__Module_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Module.attributes={UnifiedMetamodel__Module_name}

# UnifiedMetamodel__Submodule class attributes and methods
UnifiedMetamodel__Submodule_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Submodule.attributes={UnifiedMetamodel__Submodule_name}

# UnifiedMetamodel__SpecialEntity class attributes and methods

# Entity class attributes and methods

# UnifiedMetamodel__Transaction class attributes and methods

# UnifiedMetamodel__GeneralEntity class attributes and methods

# UnifiedMetamodel__Read class attributes and methods

# Operations class attributes and methods

# UnifiedMetamodel__Create class attributes and methods

# UnifiedMetamodel__Sale class attributes and methods

# Transaction class attributes and methods

# UnifiedMetamodel__Exchange class attributes and methods

# UnifiedMetamodel__Property class attributes and methods
UnifiedMetamodel__Property_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Property_type: Property = Property(name="type", type=StringType)
UnifiedMetamodel__Property.attributes={UnifiedMetamodel__Property_name, UnifiedMetamodel__Property_type}

# UnifiedMetamodel__RelationDom class attributes and methods

# UnifiedMetamodel__MD class attributes and methods

# UnifiedMetamodel__CSS class attributes and methods

# UnifiedMetamodel__APICall class attributes and methods

# UnifiedMetamodel__Directory class attributes and methods
UnifiedMetamodel__Directory_purpose: Property = Property(name="purpose", type=StringType)
UnifiedMetamodel__Directory_isRoot: Property = Property(name="isRoot", type=BooleanType)
UnifiedMetamodel__Directory_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Directory.attributes={UnifiedMetamodel__Directory_purpose, UnifiedMetamodel__Directory_name, UnifiedMetamodel__Directory_isRoot}

# UnifiedMetamodel__File class attributes and methods
UnifiedMetamodel__File_type: Property = Property(name="type", type=StringType)
UnifiedMetamodel__File_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__File.attributes={UnifiedMetamodel__File_name, UnifiedMetamodel__File_type}

# UnifiedMetamodel__ActionDispatcher class attributes and methods
UnifiedMetamodel__ActionDispatcher_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__ActionDispatcher.attributes={UnifiedMetamodel__ActionDispatcher_name}

# UnifiedMetamodel__ActionCreator class attributes and methods
UnifiedMetamodel__ActionCreator_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__ActionCreator.attributes={UnifiedMetamodel__ActionCreator_name}

# UnifiedMetamodel__Router class attributes and methods

# ModuleFront class attributes and methods

# UnifiedMetamodel__JSON class attributes and methods

# UnifiedMetamodel__UIFront class attributes and methods

# File class attributes and methods

# ComponentFront class attributes and methods

# UnifiedMetamodel__Visualizer class attributes and methods

# UIFront class attributes and methods

# UnifiedMetamodel__Design class attributes and methods

# UnifiedMetamodel__RouterComponent class attributes and methods

# UnifiedMetamodel__Container class attributes and methods

# UnifiedMetamodel__State class attributes and methods

# UnifiedMetamodel__Action class attributes and methods
UnifiedMetamodel__Action_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Action.attributes={UnifiedMetamodel__Action_name}

# UnifiedMetamodel__Reducer class attributes and methods
UnifiedMetamodel__Reducer_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Reducer.attributes={UnifiedMetamodel__Reducer_name}

# UnifiedMetamodel__ModuleFront class attributes and methods
UnifiedMetamodel__ModuleFront_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__ModuleFront.attributes={UnifiedMetamodel__ModuleFront_name}

# UnifiedMetamodel__Functionality class attributes and methods
UnifiedMetamodel__Functionality_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Functionality.attributes={UnifiedMetamodel__Functionality_name}

# UnifiedMetamodel__ComponentFront class attributes and methods
UnifiedMetamodel__ComponentFront_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__ComponentFront.attributes={UnifiedMetamodel__ComponentFront_name}

# UnifiedMetamodel__JS class attributes and methods

# UnifiedMetamodel__ServicesFront class attributes and methods
UnifiedMetamodel__ServicesFront_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__ServicesFront.attributes={UnifiedMetamodel__ServicesFront_name}

# UnifiedMetamodel__Redux class attributes and methods

# UnifiedMetamodel__ReactApp class attributes and methods

# UnifiedMetamodel__JavaApp class attributes and methods

# UnifiedMetamodel__JEE_Project class attributes and methods
UnifiedMetamodel__JEE_Project_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__JEE_Project.attributes={UnifiedMetamodel__JEE_Project_name}

# UnifiedMetamodel__Subproject class attributes and methods
UnifiedMetamodel__Subproject_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Subproject.attributes={UnifiedMetamodel__Subproject_name}

# UnifiedMetamodel__Annotation class attributes and methods
UnifiedMetamodel__Annotation_properties: Property = Property(name="properties", type=StringType)
UnifiedMetamodel__Annotation.attributes={UnifiedMetamodel__Annotation_properties}

# UnifiedMetamodel__Attribute class attributes and methods
UnifiedMetamodel__Attribute_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Attribute.attributes={UnifiedMetamodel__Attribute_name}

# UnifiedMetamodel__EClass class attributes and methods
UnifiedMetamodel__EClass_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__EClass.attributes={UnifiedMetamodel__EClass_name}

# UnifiedMetamodel__GenericClass class attributes and methods

# UnifiedMetamodel__NativeClass class attributes and methods
UnifiedMetamodel__NativeClass_primitiveRef: Property = Property(name="primitiveRef", type=StringType)
UnifiedMetamodel__NativeClass.attributes={UnifiedMetamodel__NativeClass_primitiveRef}

# EClass class attributes and methods

# UnifiedMetamodel__EInterface class attributes and methods
UnifiedMetamodel__EInterface_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__EInterface.attributes={UnifiedMetamodel__EInterface_name}

# UnifiedMetamodel__AbstractMethod class attributes and methods
UnifiedMetamodel__AbstractMethod_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__AbstractMethod.attributes={UnifiedMetamodel__AbstractMethod_name}

# UnifiedMetamodel__Library class attributes and methods
UnifiedMetamodel__Library_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Library_isNative: Property = Property(name="isNative", type=BooleanType)
UnifiedMetamodel__Library.attributes={UnifiedMetamodel__Library_name, UnifiedMetamodel__Library_isNative}

# UnifiedMetamodel__Epackage class attributes and methods
UnifiedMetamodel__Epackage_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Epackage.attributes={UnifiedMetamodel__Epackage_name}

# UnifiedMetamodel__AbstractClass class attributes and methods

# UnifiedMetamodel__MethodBack class attributes and methods
UnifiedMetamodel__MethodBack_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__MethodBack.attributes={UnifiedMetamodel__MethodBack_name}

# UnifiedMetamodel__Descriptor class attributes and methods
UnifiedMetamodel__Descriptor_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Descriptor_path: Property = Property(name="path", type=StringType)
UnifiedMetamodel__Descriptor.attributes={UnifiedMetamodel__Descriptor_name, UnifiedMetamodel__Descriptor_path}

# UnifiedMetamodel__JavaScript class attributes and methods

# UnifiedMetamodel__React class attributes and methods

# UnifiedMetamodel__Util class attributes and methods

# UnifiedMetamodel__Reducers class attributes and methods

# SubLayerSegment class attributes and methods

# UnifiedMetamodel__Actions class attributes and methods

# UnifiedMetamodel__Back class attributes and methods

# Component class attributes and methods

# UnifiedMetamodel__Front class attributes and methods

# Relationships
layerSegments4: BinaryAssociation = BinaryAssociation(
    name="layerSegments4",
    ends={
        Property(name="UnifiedMetamodel__LayerSegment5", type=UnifiedMetamodel__Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Layer", type=UnifiedMetamodel__LayerSegment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layers6: BinaryAssociation = BinaryAssociation(
    name="layers6",
    ends={
        Property(name="UnifiedMetamodel__Layer7", type=UnifiedMetamodel__Component, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Component", type=UnifiedMetamodel__Layer, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
allowToUse1: BinaryAssociation = BinaryAssociation(
    name="allowToUse1",
    ends={
        Property(name="UnifiedMetamodel__LayerSegment", type=UnifiedMetamodel__LayerSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__LayerSegment0", type=UnifiedMetamodel__LayerSegment, multiplicity=Multiplicity(0, 9999))
    }
)
sublayersegment2: BinaryAssociation = BinaryAssociation(
    name="sublayersegment2",
    ends={
        Property(name="UnifiedMetamodel__SubLayerSegment", type=UnifiedMetamodel__LayerSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__LayerSegment3", type=UnifiedMetamodel__SubLayerSegment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components13: BinaryAssociation = BinaryAssociation(
    name="components13",
    ends={
        Property(name="UnifiedMetamodel__Component14", type=UnifiedMetamodel__ArquitectureMetamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__ArquitectureMetamodel", type=UnifiedMetamodel__Component, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
relations15: BinaryAssociation = BinaryAssociation(
    name="relations15",
    ends={
        Property(name="UnifiedMetamodel__RelationArch17", type=UnifiedMetamodel__ArquitectureMetamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__ArquitectureMetamodel16", type=UnifiedMetamodel__RelationArch, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
arquitecturemetamodel18: BinaryAssociation = BinaryAssociation(
    name="arquitecturemetamodel18",
    ends={
        Property(name="UnifiedMetamodel__ArquitectureMetamodel19", type=UnifiedMetamodel__Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Metamodel", type=UnifiedMetamodel__ArquitectureMetamodel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
domainmetamodel20: BinaryAssociation = BinaryAssociation(
    name="domainmetamodel20",
    ends={
        Property(name="UnifiedMetamodel__DomainMetamodel", type=UnifiedMetamodel__Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Metamodel21", type=UnifiedMetamodel__DomainMetamodel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="UnifiedMetamodel__Layer9", type=UnifiedMetamodel__RelationArch, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__RelationArch", type=UnifiedMetamodel__Layer, multiplicity=Multiplicity(1, 1))
    }
)
target10: BinaryAssociation = BinaryAssociation(
    name="target10",
    ends={
        Property(name="UnifiedMetamodel__Layer12", type=UnifiedMetamodel__RelationArch, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__RelationArch11", type=UnifiedMetamodel__Layer, multiplicity=Multiplicity(1, 1))
    }
)
operates_on24: BinaryAssociation = BinaryAssociation(
    name="operates_on24",
    ends={
        Property(name="UnifiedMetamodel__Entity", type=UnifiedMetamodel__Operations, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Operations", type=UnifiedMetamodel__Entity, multiplicity=Multiplicity(1, 1))
    }
)
submodule25: BinaryAssociation = BinaryAssociation(
    name="submodule25",
    ends={
        Property(name="UnifiedMetamodel__Submodule", type=UnifiedMetamodel__Module, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Module", type=UnifiedMetamodel__Submodule, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transaction26: BinaryAssociation = BinaryAssociation(
    name="transaction26",
    ends={
        Property(name="UnifiedMetamodel__Transaction", type=UnifiedMetamodel__SpecialEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__SpecialEntity", type=UnifiedMetamodel__Transaction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
technologymetamodel22: BinaryAssociation = BinaryAssociation(
    name="technologymetamodel22",
    ends={
        Property(name="UnifiedMetamodel__TechnologyMetamodel", type=UnifiedMetamodel__Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Metamodel23", type=UnifiedMetamodel__TechnologyMetamodel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operates_on34: BinaryAssociation = BinaryAssociation(
    name="operates_on34",
    ends={
        Property(name="UnifiedMetamodel__GeneralEntity", type=UnifiedMetamodel__Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Transaction35", type=UnifiedMetamodel__GeneralEntity, multiplicity=Multiplicity(1, 9999))
    }
)
operations36: BinaryAssociation = BinaryAssociation(
    name="operations36",
    ends={
        Property(name="UnifiedMetamodel__Operations38", type=UnifiedMetamodel__Submodule, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Submodule37", type=UnifiedMetamodel__Operations, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
entity39: BinaryAssociation = BinaryAssociation(
    name="entity39",
    ends={
        Property(name="UnifiedMetamodel__Entity41", type=UnifiedMetamodel__Submodule, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Submodule40", type=UnifiedMetamodel__Entity, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
module42: BinaryAssociation = BinaryAssociation(
    name="module42",
    ends={
        Property(name="UnifiedMetamodel__Module44", type=UnifiedMetamodel__DomainMetamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__DomainMetamodel43", type=UnifiedMetamodel__Module, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
relationdom45: BinaryAssociation = BinaryAssociation(
    name="relationdom45",
    ends={
        Property(name="UnifiedMetamodel__RelationDom47", type=UnifiedMetamodel__DomainMetamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__DomainMetamodel46", type=UnifiedMetamodel__RelationDom, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
property27: BinaryAssociation = BinaryAssociation(
    name="property27",
    ends={
        Property(name="UnifiedMetamodel__Property", type=UnifiedMetamodel__Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Entity28", type=UnifiedMetamodel__Property, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
source29: BinaryAssociation = BinaryAssociation(
    name="source29",
    ends={
        Property(name="UnifiedMetamodel__Entity30", type=UnifiedMetamodel__RelationDom, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__RelationDom", type=UnifiedMetamodel__Entity, multiplicity=Multiplicity(1, 1))
    }
)
target31: BinaryAssociation = BinaryAssociation(
    name="target31",
    ends={
        Property(name="UnifiedMetamodel__Entity33", type=UnifiedMetamodel__RelationDom, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__RelationDom32", type=UnifiedMetamodel__Entity, multiplicity=Multiplicity(1, 1))
    }
)
directories50: BinaryAssociation = BinaryAssociation(
    name="directories50",
    ends={
        Property(name="UnifiedMetamodel__Directory", type=UnifiedMetamodel__Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Directory49", type=UnifiedMetamodel__Directory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
use48: BinaryAssociation = BinaryAssociation(
    name="use48",
    ends={
        Property(name="UnifiedMetamodel__ActionCreator", type=UnifiedMetamodel__ActionDispatcher, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__ActionDispatcher", type=UnifiedMetamodel__ActionCreator, multiplicity=Multiplicity(0, 1))
    }
)
routes58: BinaryAssociation = BinaryAssociation(
    name="routes58",
    ends={
        Property(name="UnifiedMetamodel__UIFront", type=UnifiedMetamodel__RouterComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__RouterComponent", type=UnifiedMetamodel__UIFront, multiplicity=Multiplicity(1, 9999))
    }
)
files51: BinaryAssociation = BinaryAssociation(
    name="files51",
    ends={
        Property(name="UnifiedMetamodel__File", type=UnifiedMetamodel__Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Directory52", type=UnifiedMetamodel__File, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dispatches59: BinaryAssociation = BinaryAssociation(
    name="dispatches59",
    ends={
        Property(name="UnifiedMetamodel__ActionDispatcher60", type=UnifiedMetamodel__Container, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Container", type=UnifiedMetamodel__ActionDispatcher, multiplicity=Multiplicity(0, 9999))
    }
)
action53: BinaryAssociation = BinaryAssociation(
    name="action53",
    ends={
        Property(name="UnifiedMetamodel__Action", type=UnifiedMetamodel__State, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__State", type=UnifiedMetamodel__Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
reducer54: BinaryAssociation = BinaryAssociation(
    name="reducer54",
    ends={
        Property(name="UnifiedMetamodel__Reducer", type=UnifiedMetamodel__State, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__State55", type=UnifiedMetamodel__Reducer, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
use56: BinaryAssociation = BinaryAssociation(
    name="use56",
    ends={
        Property(name="UnifiedMetamodel__ModuleFront", type=UnifiedMetamodel__State, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__State57", type=UnifiedMetamodel__ModuleFront, multiplicity=Multiplicity(1, 9999))
    }
)
components69: BinaryAssociation = BinaryAssociation(
    name="components69",
    ends={
        Property(name="UnifiedMetamodel__ComponentFront", type=UnifiedMetamodel__Functionality, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Functionality", type=UnifiedMetamodel__ComponentFront, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
state70: BinaryAssociation = BinaryAssociation(
    name="state70",
    ends={
        Property(name="UnifiedMetamodel__State72", type=UnifiedMetamodel__Functionality, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Functionality71", type=UnifiedMetamodel__State, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
services73: BinaryAssociation = BinaryAssociation(
    name="services73",
    ends={
        Property(name="UnifiedMetamodel__ServicesFront75", type=UnifiedMetamodel__Functionality, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Functionality74", type=UnifiedMetamodel__ServicesFront, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
IsOrganizedBy76: BinaryAssociation = BinaryAssociation(
    name="IsOrganizedBy76",
    ends={
        Property(name="UnifiedMetamodel__Directory78", type=UnifiedMetamodel__Functionality, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Functionality77", type=UnifiedMetamodel__Directory, multiplicity=Multiplicity(1, 1))
    }
)
actiondispatcher79: BinaryAssociation = BinaryAssociation(
    name="actiondispatcher79",
    ends={
        Property(name="UnifiedMetamodel__ActionDispatcher81", type=UnifiedMetamodel__Action, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Action80", type=UnifiedMetamodel__ActionDispatcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
maps61: BinaryAssociation = BinaryAssociation(
    name="maps61",
    ends={
        Property(name="UnifiedMetamodel__Reducer63", type=UnifiedMetamodel__Container, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Container62", type=UnifiedMetamodel__Reducer, multiplicity=Multiplicity(0, 9999))
    }
)
actioncreator82: BinaryAssociation = BinaryAssociation(
    name="actioncreator82",
    ends={
        Property(name="UnifiedMetamodel__ActionCreator84", type=UnifiedMetamodel__Action, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Action83", type=UnifiedMetamodel__ActionCreator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
use64: BinaryAssociation = BinaryAssociation(
    name="use64",
    ends={
        Property(name="UnifiedMetamodel__ModuleFront65", type=UnifiedMetamodel__ServicesFront, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__ServicesFront", type=UnifiedMetamodel__ModuleFront, multiplicity=Multiplicity(1, 9999))
    }
)
isOrganizedIn66: BinaryAssociation = BinaryAssociation(
    name="isOrganizedIn66",
    ends={
        Property(name="UnifiedMetamodel__Directory68", type=UnifiedMetamodel__ServicesFront, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__ServicesFront67", type=UnifiedMetamodel__Directory, multiplicity=Multiplicity(0, 1))
    }
)
functionalities88: BinaryAssociation = BinaryAssociation(
    name="functionalities88",
    ends={
        Property(name="UnifiedMetamodel__Functionality89", type=UnifiedMetamodel__ReactApp, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__ReactApp", type=UnifiedMetamodel__Functionality, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
modules90: BinaryAssociation = BinaryAssociation(
    name="modules90",
    ends={
        Property(name="UnifiedMetamodel__ModuleFront92", type=UnifiedMetamodel__ReactApp, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__ReactApp91", type=UnifiedMetamodel__ModuleFront, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
directories93: BinaryAssociation = BinaryAssociation(
    name="directories93",
    ends={
        Property(name="UnifiedMetamodel__Directory95", type=UnifiedMetamodel__ReactApp, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__ReactApp94", type=UnifiedMetamodel__Directory, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
use96: BinaryAssociation = BinaryAssociation(
    name="use96",
    ends={
        Property(name="UnifiedMetamodel__ModuleFront98", type=UnifiedMetamodel__ComponentFront, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__ComponentFront97", type=UnifiedMetamodel__ModuleFront, multiplicity=Multiplicity(1, 9999))
    }
)
actionDirectory85: BinaryAssociation = BinaryAssociation(
    name="actionDirectory85",
    ends={
        Property(name="UnifiedMetamodel__Directory87", type=UnifiedMetamodel__Action, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Action86", type=UnifiedMetamodel__Directory, multiplicity=Multiplicity(1, 1))
    }
)
isPresentIn108: BinaryAssociation = BinaryAssociation(
    name="isPresentIn108",
    ends={
        Property(name="UnifiedMetamodel__Directory110", type=UnifiedMetamodel__ModuleFront, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__ModuleFront109", type=UnifiedMetamodel__Directory, multiplicity=Multiplicity(1, 1))
    }
)
techback111: BinaryAssociation = BinaryAssociation(
    name="techback111",
    ends={
        Property(name="UnifiedMetamodel__JavaApp", type=UnifiedMetamodel__TechnologyMetamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__TechnologyMetamodel112", type=UnifiedMetamodel__JavaApp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
techfront113: BinaryAssociation = BinaryAssociation(
    name="techfront113",
    ends={
        Property(name="UnifiedMetamodel__ReactApp115", type=UnifiedMetamodel__TechnologyMetamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__TechnologyMetamodel114", type=UnifiedMetamodel__ReactApp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
jee_project116: BinaryAssociation = BinaryAssociation(
    name="jee_project116",
    ends={
        Property(name="UnifiedMetamodel__JEE_Project", type=UnifiedMetamodel__JavaApp, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__JavaApp117", type=UnifiedMetamodel__JEE_Project, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inWithin99: BinaryAssociation = BinaryAssociation(
    name="inWithin99",
    ends={
        Property(name="UnifiedMetamodel__Directory101", type=UnifiedMetamodel__ComponentFront, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__ComponentFront100", type=UnifiedMetamodel__Directory, multiplicity=Multiplicity(1, 1))
    }
)
subproject118: BinaryAssociation = BinaryAssociation(
    name="subproject118",
    ends={
        Property(name="UnifiedMetamodel__Subproject", type=UnifiedMetamodel__JEE_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__JEE_Project119", type=UnifiedMetamodel__Subproject, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
catches102: BinaryAssociation = BinaryAssociation(
    name="catches102",
    ends={
        Property(name="UnifiedMetamodel__ActionCreator104", type=UnifiedMetamodel__Reducer, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Reducer103", type=UnifiedMetamodel__ActionCreator, multiplicity=Multiplicity(0, 9999))
    }
)
reducerDirectory105: BinaryAssociation = BinaryAssociation(
    name="reducerDirectory105",
    ends={
        Property(name="UnifiedMetamodel__Directory107", type=UnifiedMetamodel__Reducer, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Reducer106", type=UnifiedMetamodel__Directory, multiplicity=Multiplicity(0, 1))
    }
)
nativeclass121: BinaryAssociation = BinaryAssociation(
    name="nativeclass121",
    ends={
        Property(name="UnifiedMetamodel__NativeClass", type=UnifiedMetamodel__Library, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Library", type=UnifiedMetamodel__NativeClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation122: BinaryAssociation = BinaryAssociation(
    name="annotation122",
    ends={
        Property(name="UnifiedMetamodel__Annotation", type=UnifiedMetamodel__Library, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Library123", type=UnifiedMetamodel__Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation124: BinaryAssociation = BinaryAssociation(
    name="annotation124",
    ends={
        Property(name="UnifiedMetamodel__Annotation125", type=UnifiedMetamodel__Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Attribute", type=UnifiedMetamodel__Annotation, multiplicity=Multiplicity(0, 1))
    }
)
type126: BinaryAssociation = BinaryAssociation(
    name="type126",
    ends={
        Property(name="UnifiedMetamodel__EClass", type=UnifiedMetamodel__Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Attribute127", type=UnifiedMetamodel__EClass, multiplicity=Multiplicity(1, 1))
    }
)
abstractmethod120: BinaryAssociation = BinaryAssociation(
    name="abstractmethod120",
    ends={
        Property(name="UnifiedMetamodel__AbstractMethod", type=UnifiedMetamodel__EInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__EInterface", type=UnifiedMetamodel__AbstractMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
return134: BinaryAssociation = BinaryAssociation(
    name="return134",
    ends={
        Property(name="UnifiedMetamodel__EClass136", type=UnifiedMetamodel__MethodBack, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__MethodBack135", type=UnifiedMetamodel__EClass, multiplicity=Multiplicity(0, 1))
    }
)
arguments137: BinaryAssociation = BinaryAssociation(
    name="arguments137",
    ends={
        Property(name="UnifiedMetamodel__EClass139", type=UnifiedMetamodel__MethodBack, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__MethodBack138", type=UnifiedMetamodel__EClass, multiplicity=Multiplicity(0, 9999))
    }
)
abstractmethod140: BinaryAssociation = BinaryAssociation(
    name="abstractmethod140",
    ends={
        Property(name="UnifiedMetamodel__AbstractMethod142", type=UnifiedMetamodel__AbstractClass, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__AbstractClass141", type=UnifiedMetamodel__AbstractMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class143: BinaryAssociation = BinaryAssociation(
    name="class143",
    ends={
        Property(name="UnifiedMetamodel__EClass144", type=UnifiedMetamodel__Epackage, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Epackage", type=UnifiedMetamodel__EClass, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
implement128: BinaryAssociation = BinaryAssociation(
    name="implement128",
    ends={
        Property(name="UnifiedMetamodel__EInterface129", type=UnifiedMetamodel__GenericClass, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__GenericClass", type=UnifiedMetamodel__EInterface, multiplicity=Multiplicity(0, 9999))
    }
)
extends130: BinaryAssociation = BinaryAssociation(
    name="extends130",
    ends={
        Property(name="UnifiedMetamodel__AbstractClass", type=UnifiedMetamodel__GenericClass, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__GenericClass131", type=UnifiedMetamodel__AbstractClass, multiplicity=Multiplicity(0, 1))
    }
)
annotation132: BinaryAssociation = BinaryAssociation(
    name="annotation132",
    ends={
        Property(name="UnifiedMetamodel__Annotation133", type=UnifiedMetamodel__MethodBack, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__MethodBack", type=UnifiedMetamodel__Annotation, multiplicity=Multiplicity(0, 1))
    }
)
descriptor154: BinaryAssociation = BinaryAssociation(
    name="descriptor154",
    ends={
        Property(name="UnifiedMetamodel__Descriptor", type=UnifiedMetamodel__Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Annotation155", type=UnifiedMetamodel__Descriptor, multiplicity=Multiplicity(0, 1))
    }
)
descriptor156: BinaryAssociation = BinaryAssociation(
    name="descriptor156",
    ends={
        Property(name="UnifiedMetamodel__Descriptor158", type=UnifiedMetamodel__Subproject, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Subproject157", type=UnifiedMetamodel__Descriptor, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
package159: BinaryAssociation = BinaryAssociation(
    name="package159",
    ends={
        Property(name="UnifiedMetamodel__Epackage161", type=UnifiedMetamodel__Subproject, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Subproject160", type=UnifiedMetamodel__Epackage, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
library162: BinaryAssociation = BinaryAssociation(
    name="library162",
    ends={
        Property(name="UnifiedMetamodel__Library164", type=UnifiedMetamodel__Subproject, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Subproject163", type=UnifiedMetamodel__Library, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
attribute145: BinaryAssociation = BinaryAssociation(
    name="attribute145",
    ends={
        Property(name="UnifiedMetamodel__Attribute147", type=UnifiedMetamodel__EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__EClass146", type=UnifiedMetamodel__Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method148: BinaryAssociation = BinaryAssociation(
    name="method148",
    ends={
        Property(name="UnifiedMetamodel__MethodBack150", type=UnifiedMetamodel__EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__EClass149", type=UnifiedMetamodel__MethodBack, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation151: BinaryAssociation = BinaryAssociation(
    name="annotation151",
    ends={
        Property(name="UnifiedMetamodel__Annotation153", type=UnifiedMetamodel__EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__EClass152", type=UnifiedMetamodel__Annotation, multiplicity=Multiplicity(0, 1))
    }
)
return165: BinaryAssociation = BinaryAssociation(
    name="return165",
    ends={
        Property(name="UnifiedMetamodel__EClass167", type=UnifiedMetamodel__AbstractMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__AbstractMethod166", type=UnifiedMetamodel__EClass, multiplicity=Multiplicity(0, 1))
    }
)
arguments168: BinaryAssociation = BinaryAssociation(
    name="arguments168",
    ends={
        Property(name="UnifiedMetamodel__EClass170", type=UnifiedMetamodel__AbstractMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__AbstractMethod169", type=UnifiedMetamodel__EClass, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_UnifiedMetamodel__Ejb_Layer = Generalization(general=Layer, specific=UnifiedMetamodel__Ejb)
gen_UnifiedMetamodel__Store_LayerSegment = Generalization(general=LayerSegment, specific=UnifiedMetamodel__Store)
gen_UnifiedMetamodel__UI_LayerSegment = Generalization(general=LayerSegment, specific=UnifiedMetamodel__UI)
gen_UnifiedMetamodel__RestEntity_LayerSegment = Generalization(general=LayerSegment, specific=UnifiedMetamodel__RestEntity)
gen_UnifiedMetamodel__Facade_LayerSegment = Generalization(general=LayerSegment, specific=UnifiedMetamodel__Facade)
gen_UnifiedMetamodel__War_Layer = Generalization(general=Layer, specific=UnifiedMetamodel__War)
gen_UnifiedMetamodel__Dto_LayerSegment = Generalization(general=LayerSegment, specific=UnifiedMetamodel__Dto)
gen_UnifiedMetamodel__Containers_LayerSegment = Generalization(general=LayerSegment, specific=UnifiedMetamodel__Containers)
gen_UnifiedMetamodel__Pojo_LayerSegment = Generalization(general=LayerSegment, specific=UnifiedMetamodel__Pojo)
gen_UnifiedMetamodel__Services_LayerSegment = Generalization(general=LayerSegment, specific=UnifiedMetamodel__Services)
gen_UnifiedMetamodel__Composition_RelationDom = Generalization(general=RelationDom, specific=UnifiedMetamodel__Composition)
gen_UnifiedMetamodel__SpecialEntity_Entity = Generalization(general=Entity, specific=UnifiedMetamodel__SpecialEntity)
gen_UnifiedMetamodel__GeneralEntity_Entity = Generalization(general=Entity, specific=UnifiedMetamodel__GeneralEntity)
gen_UnifiedMetamodel__Read_Operations = Generalization(general=Operations, specific=UnifiedMetamodel__Read)
gen_UnifiedMetamodel__Create_Operations = Generalization(general=Operations, specific=UnifiedMetamodel__Create)
gen_UnifiedMetamodel__Sale_Transaction = Generalization(general=Transaction, specific=UnifiedMetamodel__Sale)
gen_UnifiedMetamodel__Exchange_Transaction = Generalization(general=Transaction, specific=UnifiedMetamodel__Exchange)
gen_UnifiedMetamodel__MD_File = Generalization(general=File, specific=UnifiedMetamodel__MD)
gen_UnifiedMetamodel__CSS_File = Generalization(general=File, specific=UnifiedMetamodel__CSS)
gen_UnifiedMetamodel__APICall_ModuleFront = Generalization(general=ModuleFront, specific=UnifiedMetamodel__APICall)
gen_UnifiedMetamodel__Router_ModuleFront = Generalization(general=ModuleFront, specific=UnifiedMetamodel__Router)
gen_UnifiedMetamodel__JSON_File = Generalization(general=File, specific=UnifiedMetamodel__JSON)
gen_UnifiedMetamodel__UIFront_ComponentFront = Generalization(general=ComponentFront, specific=UnifiedMetamodel__UIFront)
gen_UnifiedMetamodel__Visualizer_UIFront = Generalization(general=UIFront, specific=UnifiedMetamodel__Visualizer)
gen_UnifiedMetamodel__Design_ModuleFront = Generalization(general=ModuleFront, specific=UnifiedMetamodel__Design)
gen_UnifiedMetamodel__RouterComponent_UIFront = Generalization(general=UIFront, specific=UnifiedMetamodel__RouterComponent)
gen_UnifiedMetamodel__Container_ComponentFront = Generalization(general=ComponentFront, specific=UnifiedMetamodel__Container)
gen_UnifiedMetamodel__JS_File = Generalization(general=File, specific=UnifiedMetamodel__JS)
gen_UnifiedMetamodel__Redux_ModuleFront = Generalization(general=ModuleFront, specific=UnifiedMetamodel__Redux)
gen_UnifiedMetamodel__NativeClass_EClass = Generalization(general=EClass, specific=UnifiedMetamodel__NativeClass)
gen_UnifiedMetamodel__AbstractClass_EClass = Generalization(general=EClass, specific=UnifiedMetamodel__AbstractClass)
gen_UnifiedMetamodel__GenericClass_EClass = Generalization(general=EClass, specific=UnifiedMetamodel__GenericClass)
gen_UnifiedMetamodel__JavaScript_Layer = Generalization(general=Layer, specific=UnifiedMetamodel__JavaScript)
gen_UnifiedMetamodel__Annotation_EClass = Generalization(general=EClass, specific=UnifiedMetamodel__Annotation)
gen_UnifiedMetamodel__React_ModuleFront = Generalization(general=ModuleFront, specific=UnifiedMetamodel__React)
gen_UnifiedMetamodel__Util_LayerSegment = Generalization(general=LayerSegment, specific=UnifiedMetamodel__Util)
gen_UnifiedMetamodel__Reducers_SubLayerSegment = Generalization(general=SubLayerSegment, specific=UnifiedMetamodel__Reducers)
gen_UnifiedMetamodel__Actions_SubLayerSegment = Generalization(general=SubLayerSegment, specific=UnifiedMetamodel__Actions)
gen_UnifiedMetamodel__Back_Component = Generalization(general=Component, specific=UnifiedMetamodel__Back)
gen_UnifiedMetamodel__Front_Component = Generalization(general=Component, specific=UnifiedMetamodel__Front)

# Domain Model
domain_model = DomainModel(
    name="UnifiedMetamodel_",
    types={UnifiedMetamodel__Ejb, Layer, UnifiedMetamodel__Store, UnifiedMetamodel__UI, UnifiedMetamodel__Layer, UnifiedMetamodel__RestEntity, UnifiedMetamodel__Facade, UnifiedMetamodel__War, UnifiedMetamodel__Component, UnifiedMetamodel__LayerSegment, UnifiedMetamodel__SubLayerSegment, UnifiedMetamodel__Dto, LayerSegment, UnifiedMetamodel__Containers, UnifiedMetamodel__Pojo, UnifiedMetamodel__Services, UnifiedMetamodel__Metamodel, UnifiedMetamodel__DomainMetamodel, UnifiedMetamodel__TechnologyMetamodel, UnifiedMetamodel__RelationArch, UnifiedMetamodel__ArquitectureMetamodel, UnifiedMetamodel__Composition, RelationDom, UnifiedMetamodel__Operations, UnifiedMetamodel__Entity, UnifiedMetamodel__Module, UnifiedMetamodel__Submodule, UnifiedMetamodel__SpecialEntity, Entity, UnifiedMetamodel__Transaction, UnifiedMetamodel__GeneralEntity, UnifiedMetamodel__Read, Operations, UnifiedMetamodel__Create, UnifiedMetamodel__Sale, Transaction, UnifiedMetamodel__Exchange, UnifiedMetamodel__Property, UnifiedMetamodel__RelationDom, UnifiedMetamodel__MD, UnifiedMetamodel__CSS, UnifiedMetamodel__APICall, UnifiedMetamodel__Directory, UnifiedMetamodel__File, UnifiedMetamodel__ActionDispatcher, UnifiedMetamodel__ActionCreator, UnifiedMetamodel__Router, ModuleFront, UnifiedMetamodel__JSON, UnifiedMetamodel__UIFront, File, ComponentFront, UnifiedMetamodel__Visualizer, UIFront, UnifiedMetamodel__Design, UnifiedMetamodel__RouterComponent, UnifiedMetamodel__Container, UnifiedMetamodel__State, UnifiedMetamodel__Action, UnifiedMetamodel__Reducer, UnifiedMetamodel__ModuleFront, UnifiedMetamodel__Functionality, UnifiedMetamodel__ComponentFront, UnifiedMetamodel__JS, UnifiedMetamodel__ServicesFront, UnifiedMetamodel__Redux, UnifiedMetamodel__ReactApp, UnifiedMetamodel__JavaApp, UnifiedMetamodel__JEE_Project, UnifiedMetamodel__Subproject, UnifiedMetamodel__Annotation, UnifiedMetamodel__Attribute, UnifiedMetamodel__EClass, UnifiedMetamodel__GenericClass, UnifiedMetamodel__NativeClass, EClass, UnifiedMetamodel__EInterface, UnifiedMetamodel__AbstractMethod, UnifiedMetamodel__Library, UnifiedMetamodel__Epackage, UnifiedMetamodel__AbstractClass, UnifiedMetamodel__MethodBack, UnifiedMetamodel__Descriptor, UnifiedMetamodel__JavaScript, UnifiedMetamodel__React, UnifiedMetamodel__Util, UnifiedMetamodel__Reducers, SubLayerSegment, UnifiedMetamodel__Actions, UnifiedMetamodel__Back, Component, UnifiedMetamodel__Front},
    associations={layerSegments4, layers6, allowToUse1, sublayersegment2, components13, relations15, arquitecturemetamodel18, domainmetamodel20, source8, target10, operates_on24, submodule25, transaction26, technologymetamodel22, operates_on34, operations36, entity39, module42, relationdom45, property27, source29, target31, directories50, use48, routes58, files51, dispatches59, action53, reducer54, use56, components69, state70, services73, IsOrganizedBy76, actiondispatcher79, maps61, actioncreator82, use64, isOrganizedIn66, functionalities88, modules90, directories93, use96, actionDirectory85, isPresentIn108, techback111, techfront113, jee_project116, inWithin99, subproject118, catches102, reducerDirectory105, nativeclass121, annotation122, annotation124, type126, abstractmethod120, return134, arguments137, abstractmethod140, class143, implement128, extends130, annotation132, descriptor154, descriptor156, package159, library162, attribute145, method148, annotation151, return165, arguments168},
    generalizations={gen_UnifiedMetamodel__Ejb_Layer, gen_UnifiedMetamodel__Store_LayerSegment, gen_UnifiedMetamodel__UI_LayerSegment, gen_UnifiedMetamodel__RestEntity_LayerSegment, gen_UnifiedMetamodel__Facade_LayerSegment, gen_UnifiedMetamodel__War_Layer, gen_UnifiedMetamodel__Dto_LayerSegment, gen_UnifiedMetamodel__Containers_LayerSegment, gen_UnifiedMetamodel__Pojo_LayerSegment, gen_UnifiedMetamodel__Services_LayerSegment, gen_UnifiedMetamodel__Composition_RelationDom, gen_UnifiedMetamodel__SpecialEntity_Entity, gen_UnifiedMetamodel__GeneralEntity_Entity, gen_UnifiedMetamodel__Read_Operations, gen_UnifiedMetamodel__Create_Operations, gen_UnifiedMetamodel__Sale_Transaction, gen_UnifiedMetamodel__Exchange_Transaction, gen_UnifiedMetamodel__MD_File, gen_UnifiedMetamodel__CSS_File, gen_UnifiedMetamodel__APICall_ModuleFront, gen_UnifiedMetamodel__Router_ModuleFront, gen_UnifiedMetamodel__JSON_File, gen_UnifiedMetamodel__UIFront_ComponentFront, gen_UnifiedMetamodel__Visualizer_UIFront, gen_UnifiedMetamodel__Design_ModuleFront, gen_UnifiedMetamodel__RouterComponent_UIFront, gen_UnifiedMetamodel__Container_ComponentFront, gen_UnifiedMetamodel__JS_File, gen_UnifiedMetamodel__Redux_ModuleFront, gen_UnifiedMetamodel__NativeClass_EClass, gen_UnifiedMetamodel__AbstractClass_EClass, gen_UnifiedMetamodel__GenericClass_EClass, gen_UnifiedMetamodel__JavaScript_Layer, gen_UnifiedMetamodel__Annotation_EClass, gen_UnifiedMetamodel__React_ModuleFront, gen_UnifiedMetamodel__Util_LayerSegment, gen_UnifiedMetamodel__Reducers_SubLayerSegment, gen_UnifiedMetamodel__Actions_SubLayerSegment, gen_UnifiedMetamodel__Back_Component, gen_UnifiedMetamodel__Front_Component},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)