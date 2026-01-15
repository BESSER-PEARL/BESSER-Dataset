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
UnifiedMetamodel__Dto = Class(name="UnifiedMetamodel::::Dto")
LayerSegment = Class(name="LayerSegment")
UnifiedMetamodel__Ejb = Class(name="UnifiedMetamodel::::Ejb")
Layer = Class(name="Layer")
UnifiedMetamodel__LayerSegment = Class(name="UnifiedMetamodel::::LayerSegment")
UnifiedMetamodel__ArquitectureMetamodel = Class(name="UnifiedMetamodel::::ArquitectureMetamodel")
UnifiedMetamodel__Store = Class(name="UnifiedMetamodel::::Store")
UnifiedMetamodel__UI = Class(name="UnifiedMetamodel::::UI")
UnifiedMetamodel__Layer = Class(name="UnifiedMetamodel::::Layer")
UnifiedMetamodel__RestEntity = Class(name="UnifiedMetamodel::::RestEntity")
UnifiedMetamodel__Facade = Class(name="UnifiedMetamodel::::Facade")
UnifiedMetamodel__War = Class(name="UnifiedMetamodel::::War")
UnifiedMetamodel__Component = Class(name="UnifiedMetamodel::::Component")
UnifiedMetamodel__RelationArch = Class(name="UnifiedMetamodel::::RelationArch")
UnifiedMetamodel__exchange = Class(name="UnifiedMetamodel::::exchange")
UnifiedMetamodel__Composition = Class(name="UnifiedMetamodel::::Composition")
RelationDom = Class(name="RelationDom")
UnifiedMetamodel__Operations = Class(name="UnifiedMetamodel::::Operations")
UnifiedMetamodel__Entity = Class(name="UnifiedMetamodel::::Entity")
UnifiedMetamodel__Containers = Class(name="UnifiedMetamodel::::Containers")
UnifiedMetamodel__Pojo = Class(name="UnifiedMetamodel::::Pojo")
UnifiedMetamodel__Services = Class(name="UnifiedMetamodel::::Services")
UnifiedMetamodel__Metamodel = Class(name="UnifiedMetamodel::::Metamodel")
UnifiedMetamodel__DomainMetamodel = Class(name="UnifiedMetamodel::::DomainMetamodel")
UnifiedMetamodel__TechnologyMetamodel = Class(name="UnifiedMetamodel::::TechnologyMetamodel")
UnifiedMetamodel__Read = Class(name="UnifiedMetamodel::::Read")
Operations = Class(name="Operations")
UnifiedMetamodel__Create = Class(name="UnifiedMetamodel::::Create")
UnifiedMetamodel__sale = Class(name="UnifiedMetamodel::::sale")
Transaction = Class(name="Transaction")
UnifiedMetamodel__Module = Class(name="UnifiedMetamodel::::Module")
UnifiedMetamodel__Submodule = Class(name="UnifiedMetamodel::::Submodule")
UnifiedMetamodel__SpecialEntity = Class(name="UnifiedMetamodel::::SpecialEntity")
Entity = Class(name="Entity")
UnifiedMetamodel__Transaction = Class(name="UnifiedMetamodel::::Transaction")
UnifiedMetamodel__GeneralEntity = Class(name="UnifiedMetamodel::::GeneralEntity")
UnifiedMetamodel__Property = Class(name="UnifiedMetamodel::::Property")
UnifiedMetamodel__RelationDom = Class(name="UnifiedMetamodel::::RelationDom")
UnifiedMetamodel__File = Class(name="UnifiedMetamodel::::File")
UnifiedMetamodel__ActionDispatcher = Class(name="UnifiedMetamodel::::ActionDispatcher")
UnifiedMetamodel__ActionCreator = Class(name="UnifiedMetamodel::::ActionCreator")
UnifiedMetamodel__Router = Class(name="UnifiedMetamodel::::Router")
ModuleFront = Class(name="ModuleFront")
UnifiedMetamodel__JSON = Class(name="UnifiedMetamodel::::JSON")
File = Class(name="File")
UnifiedMetamodel__MD = Class(name="UnifiedMetamodel::::MD")
UnifiedMetamodel__CSS = Class(name="UnifiedMetamodel::::CSS")
UnifiedMetamodel__APICall = Class(name="UnifiedMetamodel::::APICall")
UnifiedMetamodel__Directory = Class(name="UnifiedMetamodel::::Directory")
UnifiedMetamodel__Container = Class(name="UnifiedMetamodel::::Container")
UnifiedMetamodel__State = Class(name="UnifiedMetamodel::::State")
UnifiedMetamodel__Action = Class(name="UnifiedMetamodel::::Action")
UnifiedMetamodel__Reducer = Class(name="UnifiedMetamodel::::Reducer")
UnifiedMetamodel__ModuleFront = Class(name="UnifiedMetamodel::::ModuleFront")
UnifiedMetamodel__UIFront = Class(name="UnifiedMetamodel::::UIFront")
ComponentFront = Class(name="ComponentFront")
UnifiedMetamodel__Visualizer = Class(name="UnifiedMetamodel::::Visualizer")
UIFront = Class(name="UIFront")
UnifiedMetamodel__Design = Class(name="UnifiedMetamodel::::Design")
UnifiedMetamodel__RouterComponent = Class(name="UnifiedMetamodel::::RouterComponent")
UnifiedMetamodel__ServicesFront = Class(name="UnifiedMetamodel::::ServicesFront")
UnifiedMetamodel__Functionality = Class(name="UnifiedMetamodel::::Functionality")
UnifiedMetamodel__ComponentFront = Class(name="UnifiedMetamodel::::ComponentFront")
UnifiedMetamodel__JS = Class(name="UnifiedMetamodel::::JS")
UnifiedMetamodel__Redux = Class(name="UnifiedMetamodel::::Redux")
UnifiedMetamodel__ReactApp = Class(name="UnifiedMetamodel::::ReactApp")
UnifiedMetamodel__EInterface = Class(name="UnifiedMetamodel::::EInterface")
UnifiedMetamodel__AbstractMethod = Class(name="UnifiedMetamodel::::AbstractMethod")
UnifiedMetamodel__Library = Class(name="UnifiedMetamodel::::Library")
UnifiedMetamodel__JavaApp = Class(name="UnifiedMetamodel::::JavaApp")
UnifiedMetamodel__JEE_Project = Class(name="UnifiedMetamodel::::JEE::Project")
UnifiedMetamodel__Subproject = Class(name="UnifiedMetamodel::::Subproject")
UnifiedMetamodel__NativeClass = Class(name="UnifiedMetamodel::::NativeClass")
EClass = Class(name="EClass")
UnifiedMetamodel__Epackage = Class(name="UnifiedMetamodel::::Epackage")
UnifiedMetamodel__Annotation = Class(name="UnifiedMetamodel::::Annotation")
UnifiedMetamodel__Attribute = Class(name="UnifiedMetamodel::::Attribute")
UnifiedMetamodel__EClass = Class(name="UnifiedMetamodel::::EClass")
UnifiedMetamodel__GenericClass = Class(name="UnifiedMetamodel::::GenericClass")
UnifiedMetamodel__AbstractClass = Class(name="UnifiedMetamodel::::AbstractClass")
UnifiedMetamodel__MethodBack = Class(name="UnifiedMetamodel::::MethodBack")
UnifiedMetamodel__Descriptor = Class(name="UnifiedMetamodel::::Descriptor")
UnifiedMetamodel__JavaScript = Class(name="UnifiedMetamodel::::JavaScript")
UnifiedMetamodel__Util = Class(name="UnifiedMetamodel::::Util")
UnifiedMetamodel__Reducers = Class(name="UnifiedMetamodel::::Reducers")
UnifiedMetamodel__Actions = Class(name="UnifiedMetamodel::::Actions")
UnifiedMetamodel__Back = Class(name="UnifiedMetamodel::::Back")
Component = Class(name="Component")
UnifiedMetamodel__Front = Class(name="UnifiedMetamodel::::Front")

# UnifiedMetamodel__Dto class attributes and methods

# LayerSegment class attributes and methods

# UnifiedMetamodel__Ejb class attributes and methods

# Layer class attributes and methods

# UnifiedMetamodel__LayerSegment class attributes and methods
UnifiedMetamodel__LayerSegment_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__LayerSegment.attributes={UnifiedMetamodel__LayerSegment_name}

# UnifiedMetamodel__ArquitectureMetamodel class attributes and methods

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

# UnifiedMetamodel__RelationArch class attributes and methods
UnifiedMetamodel__RelationArch_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__RelationArch.attributes={UnifiedMetamodel__RelationArch_name}

# UnifiedMetamodel__exchange class attributes and methods

# UnifiedMetamodel__Composition class attributes and methods

# RelationDom class attributes and methods

# UnifiedMetamodel__Operations class attributes and methods

# UnifiedMetamodel__Entity class attributes and methods
UnifiedMetamodel__Entity_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Entity.attributes={UnifiedMetamodel__Entity_name}

# UnifiedMetamodel__Containers class attributes and methods

# UnifiedMetamodel__Pojo class attributes and methods

# UnifiedMetamodel__Services class attributes and methods

# UnifiedMetamodel__Metamodel class attributes and methods
UnifiedMetamodel__Metamodel_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Metamodel.attributes={UnifiedMetamodel__Metamodel_name}

# UnifiedMetamodel__DomainMetamodel class attributes and methods

# UnifiedMetamodel__TechnologyMetamodel class attributes and methods

# UnifiedMetamodel__Read class attributes and methods

# Operations class attributes and methods

# UnifiedMetamodel__Create class attributes and methods

# UnifiedMetamodel__sale class attributes and methods

# Transaction class attributes and methods

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

# UnifiedMetamodel__Property class attributes and methods
UnifiedMetamodel__Property_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Property_type: Property = Property(name="type", type=StringType)
UnifiedMetamodel__Property.attributes={UnifiedMetamodel__Property_name, UnifiedMetamodel__Property_type}

# UnifiedMetamodel__RelationDom class attributes and methods

# UnifiedMetamodel__File class attributes and methods
UnifiedMetamodel__File_type: Property = Property(name="type", type=StringType)
UnifiedMetamodel__File_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__File.attributes={UnifiedMetamodel__File_type, UnifiedMetamodel__File_name}

# UnifiedMetamodel__ActionDispatcher class attributes and methods
UnifiedMetamodel__ActionDispatcher_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__ActionDispatcher.attributes={UnifiedMetamodel__ActionDispatcher_name}

# UnifiedMetamodel__ActionCreator class attributes and methods
UnifiedMetamodel__ActionCreator_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__ActionCreator.attributes={UnifiedMetamodel__ActionCreator_name}

# UnifiedMetamodel__Router class attributes and methods

# ModuleFront class attributes and methods

# UnifiedMetamodel__JSON class attributes and methods

# File class attributes and methods

# UnifiedMetamodel__MD class attributes and methods

# UnifiedMetamodel__CSS class attributes and methods

# UnifiedMetamodel__APICall class attributes and methods

# UnifiedMetamodel__Directory class attributes and methods
UnifiedMetamodel__Directory_purpose: Property = Property(name="purpose", type=StringType)
UnifiedMetamodel__Directory_isRoot: Property = Property(name="isRoot", type=BooleanType)
UnifiedMetamodel__Directory_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Directory.attributes={UnifiedMetamodel__Directory_isRoot, UnifiedMetamodel__Directory_purpose, UnifiedMetamodel__Directory_name}

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

# UnifiedMetamodel__UIFront class attributes and methods

# ComponentFront class attributes and methods

# UnifiedMetamodel__Visualizer class attributes and methods

# UIFront class attributes and methods

# UnifiedMetamodel__Design class attributes and methods

# UnifiedMetamodel__RouterComponent class attributes and methods

# UnifiedMetamodel__ServicesFront class attributes and methods
UnifiedMetamodel__ServicesFront_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__ServicesFront.attributes={UnifiedMetamodel__ServicesFront_name}

# UnifiedMetamodel__Functionality class attributes and methods
UnifiedMetamodel__Functionality_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Functionality.attributes={UnifiedMetamodel__Functionality_name}

# UnifiedMetamodel__ComponentFront class attributes and methods
UnifiedMetamodel__ComponentFront_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__ComponentFront.attributes={UnifiedMetamodel__ComponentFront_name}

# UnifiedMetamodel__JS class attributes and methods

# UnifiedMetamodel__Redux class attributes and methods

# UnifiedMetamodel__ReactApp class attributes and methods

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

# UnifiedMetamodel__JavaApp class attributes and methods

# UnifiedMetamodel__JEE_Project class attributes and methods
UnifiedMetamodel__JEE_Project_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__JEE_Project.attributes={UnifiedMetamodel__JEE_Project_name}

# UnifiedMetamodel__Subproject class attributes and methods
UnifiedMetamodel__Subproject_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Subproject.attributes={UnifiedMetamodel__Subproject_name}

# UnifiedMetamodel__NativeClass class attributes and methods
UnifiedMetamodel__NativeClass_primitiveRef: Property = Property(name="primitiveRef", type=StringType)
UnifiedMetamodel__NativeClass.attributes={UnifiedMetamodel__NativeClass_primitiveRef}

# EClass class attributes and methods

# UnifiedMetamodel__Epackage class attributes and methods
UnifiedMetamodel__Epackage_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Epackage.attributes={UnifiedMetamodel__Epackage_name}

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

# UnifiedMetamodel__AbstractClass class attributes and methods

# UnifiedMetamodel__MethodBack class attributes and methods
UnifiedMetamodel__MethodBack_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__MethodBack.attributes={UnifiedMetamodel__MethodBack_name}

# UnifiedMetamodel__Descriptor class attributes and methods
UnifiedMetamodel__Descriptor_name: Property = Property(name="name", type=StringType)
UnifiedMetamodel__Descriptor_path: Property = Property(name="path", type=StringType)
UnifiedMetamodel__Descriptor.attributes={UnifiedMetamodel__Descriptor_name, UnifiedMetamodel__Descriptor_path}

# UnifiedMetamodel__JavaScript class attributes and methods

# UnifiedMetamodel__Util class attributes and methods

# UnifiedMetamodel__Reducers class attributes and methods

# UnifiedMetamodel__Actions class attributes and methods

# UnifiedMetamodel__Back class attributes and methods

# Component class attributes and methods

# UnifiedMetamodel__Front class attributes and methods

# Relationships
layersegment3: BinaryAssociation = BinaryAssociation(
    name="layersegment3",
    ends={
        Property(name="UnifiedMetamodel__LayerSegment4", type=UnifiedMetamodel__LayerSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__LayerSegment2", type=UnifiedMetamodel__LayerSegment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allowToUse1: BinaryAssociation = BinaryAssociation(
    name="allowToUse1",
    ends={
        Property(name="UnifiedMetamodel__LayerSegment", type=UnifiedMetamodel__LayerSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__LayerSegment0", type=UnifiedMetamodel__LayerSegment, multiplicity=Multiplicity(0, 9999))
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="UnifiedMetamodel__Layer13", type=UnifiedMetamodel__RelationArch, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__RelationArch12", type=UnifiedMetamodel__Layer, multiplicity=Multiplicity(1, 1))
    }
)
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="UnifiedMetamodel__Layer16", type=UnifiedMetamodel__RelationArch, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__RelationArch15", type=UnifiedMetamodel__Layer, multiplicity=Multiplicity(1, 1))
    }
)
layerSegments5: BinaryAssociation = BinaryAssociation(
    name="layerSegments5",
    ends={
        Property(name="UnifiedMetamodel__LayerSegment6", type=UnifiedMetamodel__Layer, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Layer", type=UnifiedMetamodel__LayerSegment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
layers7: BinaryAssociation = BinaryAssociation(
    name="layers7",
    ends={
        Property(name="UnifiedMetamodel__Layer8", type=UnifiedMetamodel__Component, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Component", type=UnifiedMetamodel__Layer, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
relations9: BinaryAssociation = BinaryAssociation(
    name="relations9",
    ends={
        Property(name="UnifiedMetamodel__RelationArch", type=UnifiedMetamodel__Component, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Component10", type=UnifiedMetamodel__RelationArch, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
operates_on25: BinaryAssociation = BinaryAssociation(
    name="operates_on25",
    ends={
        Property(name="UnifiedMetamodel__Entity", type=UnifiedMetamodel__Operations, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Operations", type=UnifiedMetamodel__Entity, multiplicity=Multiplicity(1, 1))
    }
)
components17: BinaryAssociation = BinaryAssociation(
    name="components17",
    ends={
        Property(name="UnifiedMetamodel__Component18", type=UnifiedMetamodel__ArquitectureMetamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__ArquitectureMetamodel", type=UnifiedMetamodel__Component, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
arquitecturemetamodel19: BinaryAssociation = BinaryAssociation(
    name="arquitecturemetamodel19",
    ends={
        Property(name="UnifiedMetamodel__ArquitectureMetamodel20", type=UnifiedMetamodel__Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Metamodel", type=UnifiedMetamodel__ArquitectureMetamodel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
domainmetamodel21: BinaryAssociation = BinaryAssociation(
    name="domainmetamodel21",
    ends={
        Property(name="UnifiedMetamodel__DomainMetamodel", type=UnifiedMetamodel__Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Metamodel22", type=UnifiedMetamodel__DomainMetamodel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
technologymetamodel23: BinaryAssociation = BinaryAssociation(
    name="technologymetamodel23",
    ends={
        Property(name="UnifiedMetamodel__TechnologyMetamodel", type=UnifiedMetamodel__Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Metamodel24", type=UnifiedMetamodel__TechnologyMetamodel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operates_on35: BinaryAssociation = BinaryAssociation(
    name="operates_on35",
    ends={
        Property(name="UnifiedMetamodel__GeneralEntity", type=UnifiedMetamodel__Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Transaction36", type=UnifiedMetamodel__GeneralEntity, multiplicity=Multiplicity(1, 9999))
    }
)
operations37: BinaryAssociation = BinaryAssociation(
    name="operations37",
    ends={
        Property(name="UnifiedMetamodel__Operations39", type=UnifiedMetamodel__Submodule, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Submodule38", type=UnifiedMetamodel__Operations, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
submodule26: BinaryAssociation = BinaryAssociation(
    name="submodule26",
    ends={
        Property(name="UnifiedMetamodel__Submodule", type=UnifiedMetamodel__Module, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Module", type=UnifiedMetamodel__Submodule, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transaction27: BinaryAssociation = BinaryAssociation(
    name="transaction27",
    ends={
        Property(name="UnifiedMetamodel__Transaction", type=UnifiedMetamodel__SpecialEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__SpecialEntity", type=UnifiedMetamodel__Transaction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
property28: BinaryAssociation = BinaryAssociation(
    name="property28",
    ends={
        Property(name="UnifiedMetamodel__Property", type=UnifiedMetamodel__Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Entity29", type=UnifiedMetamodel__Property, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
source30: BinaryAssociation = BinaryAssociation(
    name="source30",
    ends={
        Property(name="UnifiedMetamodel__Entity31", type=UnifiedMetamodel__RelationDom, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__RelationDom", type=UnifiedMetamodel__Entity, multiplicity=Multiplicity(1, 1))
    }
)
target32: BinaryAssociation = BinaryAssociation(
    name="target32",
    ends={
        Property(name="UnifiedMetamodel__Entity34", type=UnifiedMetamodel__RelationDom, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__RelationDom33", type=UnifiedMetamodel__Entity, multiplicity=Multiplicity(1, 1))
    }
)
directories51: BinaryAssociation = BinaryAssociation(
    name="directories51",
    ends={
        Property(name="UnifiedMetamodel__Directory", type=UnifiedMetamodel__Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Directory50", type=UnifiedMetamodel__Directory, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
files52: BinaryAssociation = BinaryAssociation(
    name="files52",
    ends={
        Property(name="UnifiedMetamodel__File", type=UnifiedMetamodel__Directory, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Directory53", type=UnifiedMetamodel__File, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity40: BinaryAssociation = BinaryAssociation(
    name="entity40",
    ends={
        Property(name="UnifiedMetamodel__Entity42", type=UnifiedMetamodel__Submodule, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Submodule41", type=UnifiedMetamodel__Entity, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
module43: BinaryAssociation = BinaryAssociation(
    name="module43",
    ends={
        Property(name="UnifiedMetamodel__Module45", type=UnifiedMetamodel__DomainMetamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__DomainMetamodel44", type=UnifiedMetamodel__Module, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
relationdom46: BinaryAssociation = BinaryAssociation(
    name="relationdom46",
    ends={
        Property(name="UnifiedMetamodel__RelationDom48", type=UnifiedMetamodel__DomainMetamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__DomainMetamodel47", type=UnifiedMetamodel__RelationDom, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
use49: BinaryAssociation = BinaryAssociation(
    name="use49",
    ends={
        Property(name="UnifiedMetamodel__ActionCreator", type=UnifiedMetamodel__ActionDispatcher, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__ActionDispatcher", type=UnifiedMetamodel__ActionCreator, multiplicity=Multiplicity(0, 1))
    }
)
routes59: BinaryAssociation = BinaryAssociation(
    name="routes59",
    ends={
        Property(name="UnifiedMetamodel__UIFront", type=UnifiedMetamodel__RouterComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__RouterComponent", type=UnifiedMetamodel__UIFront, multiplicity=Multiplicity(1, 9999))
    }
)
dispatches60: BinaryAssociation = BinaryAssociation(
    name="dispatches60",
    ends={
        Property(name="UnifiedMetamodel__ActionDispatcher61", type=UnifiedMetamodel__Container, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Container", type=UnifiedMetamodel__ActionDispatcher, multiplicity=Multiplicity(0, 9999))
    }
)
action54: BinaryAssociation = BinaryAssociation(
    name="action54",
    ends={
        Property(name="UnifiedMetamodel__Action", type=UnifiedMetamodel__State, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__State", type=UnifiedMetamodel__Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
reducer55: BinaryAssociation = BinaryAssociation(
    name="reducer55",
    ends={
        Property(name="UnifiedMetamodel__Reducer", type=UnifiedMetamodel__State, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__State56", type=UnifiedMetamodel__Reducer, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
use57: BinaryAssociation = BinaryAssociation(
    name="use57",
    ends={
        Property(name="UnifiedMetamodel__ModuleFront", type=UnifiedMetamodel__State, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__State58", type=UnifiedMetamodel__ModuleFront, multiplicity=Multiplicity(1, 9999))
    }
)
state71: BinaryAssociation = BinaryAssociation(
    name="state71",
    ends={
        Property(name="UnifiedMetamodel__State73", type=UnifiedMetamodel__Functionality, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Functionality72", type=UnifiedMetamodel__State, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
services74: BinaryAssociation = BinaryAssociation(
    name="services74",
    ends={
        Property(name="UnifiedMetamodel__ServicesFront76", type=UnifiedMetamodel__Functionality, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Functionality75", type=UnifiedMetamodel__ServicesFront, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
IsOrganizedBy77: BinaryAssociation = BinaryAssociation(
    name="IsOrganizedBy77",
    ends={
        Property(name="UnifiedMetamodel__Directory79", type=UnifiedMetamodel__Functionality, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Functionality78", type=UnifiedMetamodel__Directory, multiplicity=Multiplicity(1, 1))
    }
)
maps62: BinaryAssociation = BinaryAssociation(
    name="maps62",
    ends={
        Property(name="UnifiedMetamodel__Reducer64", type=UnifiedMetamodel__Container, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Container63", type=UnifiedMetamodel__Reducer, multiplicity=Multiplicity(0, 9999))
    }
)
use65: BinaryAssociation = BinaryAssociation(
    name="use65",
    ends={
        Property(name="UnifiedMetamodel__ModuleFront66", type=UnifiedMetamodel__ServicesFront, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__ServicesFront", type=UnifiedMetamodel__ModuleFront, multiplicity=Multiplicity(1, 9999))
    }
)
isOrganizedIn67: BinaryAssociation = BinaryAssociation(
    name="isOrganizedIn67",
    ends={
        Property(name="UnifiedMetamodel__Directory69", type=UnifiedMetamodel__ServicesFront, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__ServicesFront68", type=UnifiedMetamodel__Directory, multiplicity=Multiplicity(0, 1))
    }
)
components70: BinaryAssociation = BinaryAssociation(
    name="components70",
    ends={
        Property(name="UnifiedMetamodel__ComponentFront", type=UnifiedMetamodel__Functionality, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Functionality", type=UnifiedMetamodel__ComponentFront, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
use97: BinaryAssociation = BinaryAssociation(
    name="use97",
    ends={
        Property(name="UnifiedMetamodel__ModuleFront99", type=UnifiedMetamodel__ComponentFront, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__ComponentFront98", type=UnifiedMetamodel__ModuleFront, multiplicity=Multiplicity(1, 9999))
    }
)
actiondispatcher80: BinaryAssociation = BinaryAssociation(
    name="actiondispatcher80",
    ends={
        Property(name="UnifiedMetamodel__ActionDispatcher82", type=UnifiedMetamodel__Action, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Action81", type=UnifiedMetamodel__ActionDispatcher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actioncreator83: BinaryAssociation = BinaryAssociation(
    name="actioncreator83",
    ends={
        Property(name="UnifiedMetamodel__ActionCreator85", type=UnifiedMetamodel__Action, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Action84", type=UnifiedMetamodel__ActionCreator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actionDirectory86: BinaryAssociation = BinaryAssociation(
    name="actionDirectory86",
    ends={
        Property(name="UnifiedMetamodel__Directory88", type=UnifiedMetamodel__Action, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Action87", type=UnifiedMetamodel__Directory, multiplicity=Multiplicity(1, 1))
    }
)
functionalities89: BinaryAssociation = BinaryAssociation(
    name="functionalities89",
    ends={
        Property(name="UnifiedMetamodel__Functionality90", type=UnifiedMetamodel__ReactApp, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__ReactApp", type=UnifiedMetamodel__Functionality, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
modules91: BinaryAssociation = BinaryAssociation(
    name="modules91",
    ends={
        Property(name="UnifiedMetamodel__ModuleFront93", type=UnifiedMetamodel__ReactApp, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__ReactApp92", type=UnifiedMetamodel__ModuleFront, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
directories94: BinaryAssociation = BinaryAssociation(
    name="directories94",
    ends={
        Property(name="UnifiedMetamodel__Directory96", type=UnifiedMetamodel__ReactApp, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__ReactApp95", type=UnifiedMetamodel__Directory, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
inWithin100: BinaryAssociation = BinaryAssociation(
    name="inWithin100",
    ends={
        Property(name="UnifiedMetamodel__Directory102", type=UnifiedMetamodel__ComponentFront, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__ComponentFront101", type=UnifiedMetamodel__Directory, multiplicity=Multiplicity(1, 1))
    }
)
catches103: BinaryAssociation = BinaryAssociation(
    name="catches103",
    ends={
        Property(name="UnifiedMetamodel__ActionCreator105", type=UnifiedMetamodel__Reducer, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Reducer104", type=UnifiedMetamodel__ActionCreator, multiplicity=Multiplicity(0, 9999))
    }
)
reducerDirectory106: BinaryAssociation = BinaryAssociation(
    name="reducerDirectory106",
    ends={
        Property(name="UnifiedMetamodel__Directory108", type=UnifiedMetamodel__Reducer, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Reducer107", type=UnifiedMetamodel__Directory, multiplicity=Multiplicity(0, 1))
    }
)
isPresentIn109: BinaryAssociation = BinaryAssociation(
    name="isPresentIn109",
    ends={
        Property(name="UnifiedMetamodel__Directory111", type=UnifiedMetamodel__ModuleFront, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__ModuleFront110", type=UnifiedMetamodel__Directory, multiplicity=Multiplicity(1, 1))
    }
)
abstractmethod121: BinaryAssociation = BinaryAssociation(
    name="abstractmethod121",
    ends={
        Property(name="UnifiedMetamodel__AbstractMethod", type=UnifiedMetamodel__EInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__EInterface", type=UnifiedMetamodel__AbstractMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
techback112: BinaryAssociation = BinaryAssociation(
    name="techback112",
    ends={
        Property(name="UnifiedMetamodel__JavaApp", type=UnifiedMetamodel__TechnologyMetamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__TechnologyMetamodel113", type=UnifiedMetamodel__JavaApp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
techfront114: BinaryAssociation = BinaryAssociation(
    name="techfront114",
    ends={
        Property(name="UnifiedMetamodel__ReactApp116", type=UnifiedMetamodel__TechnologyMetamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__TechnologyMetamodel115", type=UnifiedMetamodel__ReactApp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
jee_project117: BinaryAssociation = BinaryAssociation(
    name="jee_project117",
    ends={
        Property(name="UnifiedMetamodel__JEE_Project", type=UnifiedMetamodel__JavaApp, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__JavaApp118", type=UnifiedMetamodel__JEE_Project, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
subproject119: BinaryAssociation = BinaryAssociation(
    name="subproject119",
    ends={
        Property(name="UnifiedMetamodel__Subproject", type=UnifiedMetamodel__JEE_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__JEE_Project120", type=UnifiedMetamodel__Subproject, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
abstractmethod141: BinaryAssociation = BinaryAssociation(
    name="abstractmethod141",
    ends={
        Property(name="UnifiedMetamodel__AbstractMethod143", type=UnifiedMetamodel__AbstractClass, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__AbstractClass142", type=UnifiedMetamodel__AbstractMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class144: BinaryAssociation = BinaryAssociation(
    name="class144",
    ends={
        Property(name="UnifiedMetamodel__EClass145", type=UnifiedMetamodel__Epackage, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Epackage", type=UnifiedMetamodel__EClass, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
attribute146: BinaryAssociation = BinaryAssociation(
    name="attribute146",
    ends={
        Property(name="UnifiedMetamodel__Attribute148", type=UnifiedMetamodel__EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__EClass147", type=UnifiedMetamodel__Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method149: BinaryAssociation = BinaryAssociation(
    name="method149",
    ends={
        Property(name="UnifiedMetamodel__MethodBack151", type=UnifiedMetamodel__EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__EClass150", type=UnifiedMetamodel__MethodBack, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation152: BinaryAssociation = BinaryAssociation(
    name="annotation152",
    ends={
        Property(name="UnifiedMetamodel__Annotation154", type=UnifiedMetamodel__EClass, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__EClass153", type=UnifiedMetamodel__Annotation, multiplicity=Multiplicity(0, 1))
    }
)
nativeclass122: BinaryAssociation = BinaryAssociation(
    name="nativeclass122",
    ends={
        Property(name="UnifiedMetamodel__NativeClass", type=UnifiedMetamodel__Library, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Library", type=UnifiedMetamodel__NativeClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation123: BinaryAssociation = BinaryAssociation(
    name="annotation123",
    ends={
        Property(name="UnifiedMetamodel__Annotation", type=UnifiedMetamodel__Library, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Library124", type=UnifiedMetamodel__Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation125: BinaryAssociation = BinaryAssociation(
    name="annotation125",
    ends={
        Property(name="UnifiedMetamodel__Annotation126", type=UnifiedMetamodel__Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Attribute", type=UnifiedMetamodel__Annotation, multiplicity=Multiplicity(0, 1))
    }
)
type127: BinaryAssociation = BinaryAssociation(
    name="type127",
    ends={
        Property(name="UnifiedMetamodel__EClass", type=UnifiedMetamodel__Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Attribute128", type=UnifiedMetamodel__EClass, multiplicity=Multiplicity(1, 1))
    }
)
implement129: BinaryAssociation = BinaryAssociation(
    name="implement129",
    ends={
        Property(name="UnifiedMetamodel__EInterface130", type=UnifiedMetamodel__GenericClass, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__GenericClass", type=UnifiedMetamodel__EInterface, multiplicity=Multiplicity(0, 9999))
    }
)
extends131: BinaryAssociation = BinaryAssociation(
    name="extends131",
    ends={
        Property(name="UnifiedMetamodel__AbstractClass", type=UnifiedMetamodel__GenericClass, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__GenericClass132", type=UnifiedMetamodel__AbstractClass, multiplicity=Multiplicity(0, 1))
    }
)
annotation133: BinaryAssociation = BinaryAssociation(
    name="annotation133",
    ends={
        Property(name="UnifiedMetamodel__Annotation134", type=UnifiedMetamodel__MethodBack, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__MethodBack", type=UnifiedMetamodel__Annotation, multiplicity=Multiplicity(0, 1))
    }
)
return135: BinaryAssociation = BinaryAssociation(
    name="return135",
    ends={
        Property(name="UnifiedMetamodel__EClass137", type=UnifiedMetamodel__MethodBack, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__MethodBack136", type=UnifiedMetamodel__EClass, multiplicity=Multiplicity(0, 1))
    }
)
arguments138: BinaryAssociation = BinaryAssociation(
    name="arguments138",
    ends={
        Property(name="UnifiedMetamodel__EClass140", type=UnifiedMetamodel__MethodBack, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__MethodBack139", type=UnifiedMetamodel__EClass, multiplicity=Multiplicity(0, 9999))
    }
)
return166: BinaryAssociation = BinaryAssociation(
    name="return166",
    ends={
        Property(name="UnifiedMetamodel__EClass168", type=UnifiedMetamodel__AbstractMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__AbstractMethod167", type=UnifiedMetamodel__EClass, multiplicity=Multiplicity(0, 1))
    }
)
arguments169: BinaryAssociation = BinaryAssociation(
    name="arguments169",
    ends={
        Property(name="UnifiedMetamodel__EClass171", type=UnifiedMetamodel__AbstractMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__AbstractMethod170", type=UnifiedMetamodel__EClass, multiplicity=Multiplicity(0, 9999))
    }
)
descriptor155: BinaryAssociation = BinaryAssociation(
    name="descriptor155",
    ends={
        Property(name="UnifiedMetamodel__Descriptor", type=UnifiedMetamodel__Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Annotation156", type=UnifiedMetamodel__Descriptor, multiplicity=Multiplicity(0, 1))
    }
)
descriptor157: BinaryAssociation = BinaryAssociation(
    name="descriptor157",
    ends={
        Property(name="UnifiedMetamodel__Descriptor159", type=UnifiedMetamodel__Subproject, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Subproject158", type=UnifiedMetamodel__Descriptor, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
package160: BinaryAssociation = BinaryAssociation(
    name="package160",
    ends={
        Property(name="UnifiedMetamodel__Epackage162", type=UnifiedMetamodel__Subproject, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Subproject161", type=UnifiedMetamodel__Epackage, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
library163: BinaryAssociation = BinaryAssociation(
    name="library163",
    ends={
        Property(name="UnifiedMetamodel__Library165", type=UnifiedMetamodel__Subproject, multiplicity=Multiplicity(1, 1)),
        Property(name="UnifiedMetamodel__Subproject164", type=UnifiedMetamodel__Library, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_UnifiedMetamodel__Dto_LayerSegment = Generalization(general=LayerSegment, specific=UnifiedMetamodel__Dto)
gen_UnifiedMetamodel__Ejb_Layer = Generalization(general=Layer, specific=UnifiedMetamodel__Ejb)
gen_UnifiedMetamodel__Store_LayerSegment = Generalization(general=LayerSegment, specific=UnifiedMetamodel__Store)
gen_UnifiedMetamodel__UI_LayerSegment = Generalization(general=LayerSegment, specific=UnifiedMetamodel__UI)
gen_UnifiedMetamodel__RestEntity_LayerSegment = Generalization(general=LayerSegment, specific=UnifiedMetamodel__RestEntity)
gen_UnifiedMetamodel__Facade_LayerSegment = Generalization(general=LayerSegment, specific=UnifiedMetamodel__Facade)
gen_UnifiedMetamodel__War_Layer = Generalization(general=Layer, specific=UnifiedMetamodel__War)
gen_UnifiedMetamodel__exchange_Transaction = Generalization(general=Transaction, specific=UnifiedMetamodel__exchange)
gen_UnifiedMetamodel__Composition_RelationDom = Generalization(general=RelationDom, specific=UnifiedMetamodel__Composition)
gen_UnifiedMetamodel__Containers_LayerSegment = Generalization(general=LayerSegment, specific=UnifiedMetamodel__Containers)
gen_UnifiedMetamodel__Pojo_LayerSegment = Generalization(general=LayerSegment, specific=UnifiedMetamodel__Pojo)
gen_UnifiedMetamodel__Services_LayerSegment = Generalization(general=LayerSegment, specific=UnifiedMetamodel__Services)
gen_UnifiedMetamodel__Read_Operations = Generalization(general=Operations, specific=UnifiedMetamodel__Read)
gen_UnifiedMetamodel__Create_Operations = Generalization(general=Operations, specific=UnifiedMetamodel__Create)
gen_UnifiedMetamodel__sale_Transaction = Generalization(general=Transaction, specific=UnifiedMetamodel__sale)
gen_UnifiedMetamodel__SpecialEntity_Entity = Generalization(general=Entity, specific=UnifiedMetamodel__SpecialEntity)
gen_UnifiedMetamodel__GeneralEntity_Entity = Generalization(general=Entity, specific=UnifiedMetamodel__GeneralEntity)
gen_UnifiedMetamodel__Router_ModuleFront = Generalization(general=ModuleFront, specific=UnifiedMetamodel__Router)
gen_UnifiedMetamodel__JSON_File = Generalization(general=File, specific=UnifiedMetamodel__JSON)
gen_UnifiedMetamodel__MD_File = Generalization(general=File, specific=UnifiedMetamodel__MD)
gen_UnifiedMetamodel__CSS_File = Generalization(general=File, specific=UnifiedMetamodel__CSS)
gen_UnifiedMetamodel__APICall_ModuleFront = Generalization(general=ModuleFront, specific=UnifiedMetamodel__APICall)
gen_UnifiedMetamodel__Container_ComponentFront = Generalization(general=ComponentFront, specific=UnifiedMetamodel__Container)
gen_UnifiedMetamodel__UIFront_ComponentFront = Generalization(general=ComponentFront, specific=UnifiedMetamodel__UIFront)
gen_UnifiedMetamodel__Visualizer_UIFront = Generalization(general=UIFront, specific=UnifiedMetamodel__Visualizer)
gen_UnifiedMetamodel__Design_ModuleFront = Generalization(general=ModuleFront, specific=UnifiedMetamodel__Design)
gen_UnifiedMetamodel__RouterComponent_UIFront = Generalization(general=UIFront, specific=UnifiedMetamodel__RouterComponent)
gen_UnifiedMetamodel__JS_File = Generalization(general=File, specific=UnifiedMetamodel__JS)
gen_UnifiedMetamodel__Redux_ModuleFront = Generalization(general=ModuleFront, specific=UnifiedMetamodel__Redux)
gen_UnifiedMetamodel__NativeClass_EClass = Generalization(general=EClass, specific=UnifiedMetamodel__NativeClass)
gen_UnifiedMetamodel__Annotation_EClass = Generalization(general=EClass, specific=UnifiedMetamodel__Annotation)
gen_UnifiedMetamodel__GenericClass_EClass = Generalization(general=EClass, specific=UnifiedMetamodel__GenericClass)
gen_UnifiedMetamodel__AbstractClass_EClass = Generalization(general=EClass, specific=UnifiedMetamodel__AbstractClass)
gen_UnifiedMetamodel__JavaScript_Layer = Generalization(general=Layer, specific=UnifiedMetamodel__JavaScript)
gen_UnifiedMetamodel__Util_LayerSegment = Generalization(general=LayerSegment, specific=UnifiedMetamodel__Util)
gen_UnifiedMetamodel__Reducers_LayerSegment = Generalization(general=LayerSegment, specific=UnifiedMetamodel__Reducers)
gen_UnifiedMetamodel__Actions_LayerSegment = Generalization(general=LayerSegment, specific=UnifiedMetamodel__Actions)
gen_UnifiedMetamodel__Back_Component = Generalization(general=Component, specific=UnifiedMetamodel__Back)
gen_UnifiedMetamodel__Front_Component = Generalization(general=Component, specific=UnifiedMetamodel__Front)

# Domain Model
domain_model = DomainModel(
    name="UnifiedMetamodel_",
    types={UnifiedMetamodel__Dto, LayerSegment, UnifiedMetamodel__Ejb, Layer, UnifiedMetamodel__LayerSegment, UnifiedMetamodel__ArquitectureMetamodel, UnifiedMetamodel__Store, UnifiedMetamodel__UI, UnifiedMetamodel__Layer, UnifiedMetamodel__RestEntity, UnifiedMetamodel__Facade, UnifiedMetamodel__War, UnifiedMetamodel__Component, UnifiedMetamodel__RelationArch, UnifiedMetamodel__exchange, UnifiedMetamodel__Composition, RelationDom, UnifiedMetamodel__Operations, UnifiedMetamodel__Entity, UnifiedMetamodel__Containers, UnifiedMetamodel__Pojo, UnifiedMetamodel__Services, UnifiedMetamodel__Metamodel, UnifiedMetamodel__DomainMetamodel, UnifiedMetamodel__TechnologyMetamodel, UnifiedMetamodel__Read, Operations, UnifiedMetamodel__Create, UnifiedMetamodel__sale, Transaction, UnifiedMetamodel__Module, UnifiedMetamodel__Submodule, UnifiedMetamodel__SpecialEntity, Entity, UnifiedMetamodel__Transaction, UnifiedMetamodel__GeneralEntity, UnifiedMetamodel__Property, UnifiedMetamodel__RelationDom, UnifiedMetamodel__File, UnifiedMetamodel__ActionDispatcher, UnifiedMetamodel__ActionCreator, UnifiedMetamodel__Router, ModuleFront, UnifiedMetamodel__JSON, File, UnifiedMetamodel__MD, UnifiedMetamodel__CSS, UnifiedMetamodel__APICall, UnifiedMetamodel__Directory, UnifiedMetamodel__Container, UnifiedMetamodel__State, UnifiedMetamodel__Action, UnifiedMetamodel__Reducer, UnifiedMetamodel__ModuleFront, UnifiedMetamodel__UIFront, ComponentFront, UnifiedMetamodel__Visualizer, UIFront, UnifiedMetamodel__Design, UnifiedMetamodel__RouterComponent, UnifiedMetamodel__ServicesFront, UnifiedMetamodel__Functionality, UnifiedMetamodel__ComponentFront, UnifiedMetamodel__JS, UnifiedMetamodel__Redux, UnifiedMetamodel__ReactApp, UnifiedMetamodel__EInterface, UnifiedMetamodel__AbstractMethod, UnifiedMetamodel__Library, UnifiedMetamodel__JavaApp, UnifiedMetamodel__JEE_Project, UnifiedMetamodel__Subproject, UnifiedMetamodel__NativeClass, EClass, UnifiedMetamodel__Epackage, UnifiedMetamodel__Annotation, UnifiedMetamodel__Attribute, UnifiedMetamodel__EClass, UnifiedMetamodel__GenericClass, UnifiedMetamodel__AbstractClass, UnifiedMetamodel__MethodBack, UnifiedMetamodel__Descriptor, UnifiedMetamodel__JavaScript, UnifiedMetamodel__Util, UnifiedMetamodel__Reducers, UnifiedMetamodel__Actions, UnifiedMetamodel__Back, Component, UnifiedMetamodel__Front},
    associations={layersegment3, allowToUse1, source11, target14, layerSegments5, layers7, relations9, operates_on25, components17, arquitecturemetamodel19, domainmetamodel21, technologymetamodel23, operates_on35, operations37, submodule26, transaction27, property28, source30, target32, directories51, files52, entity40, module43, relationdom46, use49, routes59, dispatches60, action54, reducer55, use57, state71, services74, IsOrganizedBy77, maps62, use65, isOrganizedIn67, components70, use97, actiondispatcher80, actioncreator83, actionDirectory86, functionalities89, modules91, directories94, inWithin100, catches103, reducerDirectory106, isPresentIn109, abstractmethod121, techback112, techfront114, jee_project117, subproject119, abstractmethod141, class144, attribute146, method149, annotation152, nativeclass122, annotation123, annotation125, type127, implement129, extends131, annotation133, return135, arguments138, return166, arguments169, descriptor155, descriptor157, package160, library163},
    generalizations={gen_UnifiedMetamodel__Dto_LayerSegment, gen_UnifiedMetamodel__Ejb_Layer, gen_UnifiedMetamodel__Store_LayerSegment, gen_UnifiedMetamodel__UI_LayerSegment, gen_UnifiedMetamodel__RestEntity_LayerSegment, gen_UnifiedMetamodel__Facade_LayerSegment, gen_UnifiedMetamodel__War_Layer, gen_UnifiedMetamodel__exchange_Transaction, gen_UnifiedMetamodel__Composition_RelationDom, gen_UnifiedMetamodel__Containers_LayerSegment, gen_UnifiedMetamodel__Pojo_LayerSegment, gen_UnifiedMetamodel__Services_LayerSegment, gen_UnifiedMetamodel__Read_Operations, gen_UnifiedMetamodel__Create_Operations, gen_UnifiedMetamodel__sale_Transaction, gen_UnifiedMetamodel__SpecialEntity_Entity, gen_UnifiedMetamodel__GeneralEntity_Entity, gen_UnifiedMetamodel__Router_ModuleFront, gen_UnifiedMetamodel__JSON_File, gen_UnifiedMetamodel__MD_File, gen_UnifiedMetamodel__CSS_File, gen_UnifiedMetamodel__APICall_ModuleFront, gen_UnifiedMetamodel__Container_ComponentFront, gen_UnifiedMetamodel__UIFront_ComponentFront, gen_UnifiedMetamodel__Visualizer_UIFront, gen_UnifiedMetamodel__Design_ModuleFront, gen_UnifiedMetamodel__RouterComponent_UIFront, gen_UnifiedMetamodel__JS_File, gen_UnifiedMetamodel__Redux_ModuleFront, gen_UnifiedMetamodel__NativeClass_EClass, gen_UnifiedMetamodel__Annotation_EClass, gen_UnifiedMetamodel__GenericClass_EClass, gen_UnifiedMetamodel__AbstractClass_EClass, gen_UnifiedMetamodel__JavaScript_Layer, gen_UnifiedMetamodel__Util_LayerSegment, gen_UnifiedMetamodel__Reducers_LayerSegment, gen_UnifiedMetamodel__Actions_LayerSegment, gen_UnifiedMetamodel__Back_Component, gen_UnifiedMetamodel__Front_Component},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)