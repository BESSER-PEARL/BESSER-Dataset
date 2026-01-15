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
LayoutType: Enumeration = Enumeration(
    name="LayoutType",
    literals={
            EnumerationLiteral(name="SINGLE_COLUMN"),
			EnumerationLiteral(name="TWO_COLUMNS"),
			EnumerationLiteral(name="LEFT_BAR"),
			EnumerationLiteral(name="RIGHT_BAR"),
			EnumerationLiteral(name="THREE_COLUMNS")
    }
)

# Classes
classLayout2Frontend_Project = Class(name="classLayout2Frontend::Project")
EntitiesModel = Class(name="EntitiesModel")
SiteView = Class(name="SiteView")
PageView = Class(name="PageView")
Entity = Class(name="Entity")
classLayout2Frontend_Entities_Composition = Class(name="classLayout2Frontend::Entities::Composition")
Association = Class(name="Association")
classLayout2Frontend_Entities_Reference = Class(name="classLayout2Frontend::Entities::Reference")
classLayout2Frontend_Entities_Entity = Class(name="classLayout2Frontend::Entities::Entity")
ContainerView = Class(name="ContainerView")
classLayout2Frontend_Entities_EntitiesModel = Class(name="classLayout2Frontend::Entities::EntitiesModel")
EntityModelElement = Class(name="EntityModelElement")
classLayout2Frontend_Entities_EntityModelElement = Class(name="classLayout2Frontend::Entities::EntityModelElement", is_abstract=True)
classLayout2Frontend_Entities_Association = Class(name="classLayout2Frontend::Entities::Association", is_abstract=True)
StructuralFeature = Class(name="StructuralFeature")
classLayout2Frontend_Entities_StructuralFeature = Class(name="classLayout2Frontend::Entities::StructuralFeature", is_abstract=True)
classLayout2Frontend_Views_SiteView = Class(name="classLayout2Frontend::Views::SiteView")
classLayout2Frontend_Entities_Property = Class(name="classLayout2Frontend::Entities::Property")
PropertyType = Class(name="PropertyType")
classLayout2Frontend_Entities_Enumeration = Class(name="classLayout2Frontend::Entities::Enumeration")
Literal = Class(name="Literal")
classLayout2Frontend_Entities_PropertyType = Class(name="classLayout2Frontend::Entities::PropertyType", is_abstract=True)
classLayout2Frontend_Entities_Literal = Class(name="classLayout2Frontend::Entities::Literal")
classLayout2Frontend_Entities_PrimitiveType = Class(name="classLayout2Frontend::Entities::PrimitiveType")
classLayout2Frontend_Views_IterationContainer = Class(name="classLayout2Frontend::Views::IterationContainer")
IterationFilter = Class(name="IterationFilter")
classLayout2Frontend_Views_InputForm = Class(name="classLayout2Frontend::Views::InputForm")
classLayout2Frontend_Views_StaticContainer = Class(name="classLayout2Frontend::Views::StaticContainer")
classLayout2Frontend_Views_Input = Class(name="classLayout2Frontend::Views::Input", is_abstract=True)
AtomicView = Class(name="AtomicView")
classLayout2Frontend_Views_ContainerView = Class(name="classLayout2Frontend::Views::ContainerView", is_abstract=True)
ElementView = Class(name="ElementView")
classLayout2Frontend_Views_AtomicView = Class(name="classLayout2Frontend::Views::AtomicView", is_abstract=True)
classLayout2Frontend_Views_ElementView = Class(name="classLayout2Frontend::Views::ElementView", is_abstract=True)
classLayout2Frontend_Views_IterationFilter = Class(name="classLayout2Frontend::Views::IterationFilter")
classLayout2Frontend_Views_Dropdownlist = Class(name="classLayout2Frontend::Views::Dropdownlist")
Selection = Class(name="Selection")
classLayout2Frontend_Views_RadioButtonGroup = Class(name="classLayout2Frontend::Views::RadioButtonGroup")
classLayout2Frontend_Views_CheckList = Class(name="classLayout2Frontend::Views::CheckList")
classLayout2Frontend_Views_Autocomplete = Class(name="classLayout2Frontend::Views::Autocomplete")
classLayout2Frontend_Views_InputText = Class(name="classLayout2Frontend::Views::InputText")
Input = Class(name="Input")
classLayout2Frontend_Views_Selection = Class(name="classLayout2Frontend::Views::Selection", is_abstract=True)
classLayout2Frontend_Views_Output = Class(name="classLayout2Frontend::Views::Output", is_abstract=True)
classLayout2Frontend_Views_TextArea = Class(name="classLayout2Frontend::Views::TextArea")
Output = Class(name="Output")
classLayout2Frontend_Views_Image = Class(name="classLayout2Frontend::Views::Image")
classLayout2Frontend_Views_PageView = Class(name="classLayout2Frontend::Views::PageView")
classLayout2Frontend_Views_FileUpload = Class(name="classLayout2Frontend::Views::FileUpload")
classLayout2Frontend_Views_List = Class(name="classLayout2Frontend::Views::List")

# classLayout2Frontend_Project class attributes and methods
classLayout2Frontend_Project_name: Property = Property(name="name", type=StringType)
classLayout2Frontend_Project.attributes={classLayout2Frontend_Project_name}

# EntitiesModel class attributes and methods

# SiteView class attributes and methods

# PageView class attributes and methods

# Entity class attributes and methods

# classLayout2Frontend_Entities_Composition class attributes and methods

# Association class attributes and methods

# classLayout2Frontend_Entities_Reference class attributes and methods

# classLayout2Frontend_Entities_Entity class attributes and methods
classLayout2Frontend_Entities_Entity_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
classLayout2Frontend_Entities_Entity.attributes={classLayout2Frontend_Entities_Entity_isAbstract}

# ContainerView class attributes and methods

# classLayout2Frontend_Entities_EntitiesModel class attributes and methods
classLayout2Frontend_Entities_EntitiesModel_name: Property = Property(name="name", type=StringType)
classLayout2Frontend_Entities_EntitiesModel.attributes={classLayout2Frontend_Entities_EntitiesModel_name}

# EntityModelElement class attributes and methods

# classLayout2Frontend_Entities_EntityModelElement class attributes and methods
classLayout2Frontend_Entities_EntityModelElement_name: Property = Property(name="name", type=StringType)
classLayout2Frontend_Entities_EntityModelElement_description: Property = Property(name="description", type=StringType)
classLayout2Frontend_Entities_EntityModelElement_displayName: Property = Property(name="displayName", type=StringType)
classLayout2Frontend_Entities_EntityModelElement.attributes={classLayout2Frontend_Entities_EntityModelElement_description, classLayout2Frontend_Entities_EntityModelElement_name, classLayout2Frontend_Entities_EntityModelElement_displayName}

# classLayout2Frontend_Entities_Association class attributes and methods
classLayout2Frontend_Entities_Association_many: Property = Property(name="many", type=BooleanType)
classLayout2Frontend_Entities_Association.attributes={classLayout2Frontend_Entities_Association_many}

# StructuralFeature class attributes and methods

# classLayout2Frontend_Entities_StructuralFeature class attributes and methods
classLayout2Frontend_Entities_StructuralFeature_required: Property = Property(name="required", type=BooleanType)
classLayout2Frontend_Entities_StructuralFeature.attributes={classLayout2Frontend_Entities_StructuralFeature_required}

# classLayout2Frontend_Views_SiteView class attributes and methods
classLayout2Frontend_Views_SiteView_name: Property = Property(name="name", type=StringType)
classLayout2Frontend_Views_SiteView_templateName: Property = Property(name="templateName", type=StringType)
classLayout2Frontend_Views_SiteView_templateColor: Property = Property(name="templateColor", type=StringType)
classLayout2Frontend_Views_SiteView_displayName: Property = Property(name="displayName", type=StringType)
classLayout2Frontend_Views_SiteView.attributes={classLayout2Frontend_Views_SiteView_templateColor, classLayout2Frontend_Views_SiteView_templateName, classLayout2Frontend_Views_SiteView_displayName, classLayout2Frontend_Views_SiteView_name}

# classLayout2Frontend_Entities_Property class attributes and methods
classLayout2Frontend_Entities_Property_defaultValue: Property = Property(name="defaultValue", type=StringType)
classLayout2Frontend_Entities_Property.attributes={classLayout2Frontend_Entities_Property_defaultValue}

# PropertyType class attributes and methods

# classLayout2Frontend_Entities_Enumeration class attributes and methods

# Literal class attributes and methods

# classLayout2Frontend_Entities_PropertyType class attributes and methods

# classLayout2Frontend_Entities_Literal class attributes and methods
classLayout2Frontend_Entities_Literal_value: Property = Property(name="value", type=IntegerType)
classLayout2Frontend_Entities_Literal.attributes={classLayout2Frontend_Entities_Literal_value}

# classLayout2Frontend_Entities_PrimitiveType class attributes and methods

# classLayout2Frontend_Views_IterationContainer class attributes and methods

# IterationFilter class attributes and methods

# classLayout2Frontend_Views_InputForm class attributes and methods

# classLayout2Frontend_Views_StaticContainer class attributes and methods

# classLayout2Frontend_Views_Input class attributes and methods
classLayout2Frontend_Views_Input_label: Property = Property(name="label", type=StringType)
classLayout2Frontend_Views_Input.attributes={classLayout2Frontend_Views_Input_label}

# AtomicView class attributes and methods

# classLayout2Frontend_Views_ContainerView class attributes and methods

# ElementView class attributes and methods

# classLayout2Frontend_Views_AtomicView class attributes and methods

# classLayout2Frontend_Views_ElementView class attributes and methods
classLayout2Frontend_Views_ElementView_name: Property = Property(name="name", type=StringType)
classLayout2Frontend_Views_ElementView_dsisplayName: Property = Property(name="dsisplayName", type=StringType)
classLayout2Frontend_Views_ElementView_description: Property = Property(name="description", type=StringType)
classLayout2Frontend_Views_ElementView.attributes={classLayout2Frontend_Views_ElementView_description, classLayout2Frontend_Views_ElementView_name, classLayout2Frontend_Views_ElementView_dsisplayName}

# classLayout2Frontend_Views_IterationFilter class attributes and methods

# classLayout2Frontend_Views_Dropdownlist class attributes and methods

# Selection class attributes and methods

# classLayout2Frontend_Views_RadioButtonGroup class attributes and methods

# classLayout2Frontend_Views_CheckList class attributes and methods

# classLayout2Frontend_Views_Autocomplete class attributes and methods
classLayout2Frontend_Views_Autocomplete_multiple: Property = Property(name="multiple", type=BooleanType)
classLayout2Frontend_Views_Autocomplete.attributes={classLayout2Frontend_Views_Autocomplete_multiple}

# classLayout2Frontend_Views_InputText class attributes and methods
classLayout2Frontend_Views_InputText_multiline: Property = Property(name="multiline", type=BooleanType)
classLayout2Frontend_Views_InputText.attributes={classLayout2Frontend_Views_InputText_multiline}

# Input class attributes and methods

# classLayout2Frontend_Views_Selection class attributes and methods

# classLayout2Frontend_Views_Output class attributes and methods

# classLayout2Frontend_Views_TextArea class attributes and methods
classLayout2Frontend_Views_TextArea_value: Property = Property(name="value", type=StringType)
classLayout2Frontend_Views_TextArea.attributes={classLayout2Frontend_Views_TextArea_value}

# Output class attributes and methods

# classLayout2Frontend_Views_Image class attributes and methods
classLayout2Frontend_Views_Image_width: Property = Property(name="width", type=FloatType)
classLayout2Frontend_Views_Image_height: Property = Property(name="height", type=FloatType)
classLayout2Frontend_Views_Image.attributes={classLayout2Frontend_Views_Image_height, classLayout2Frontend_Views_Image_width}

# classLayout2Frontend_Views_PageView class attributes and methods
classLayout2Frontend_Views_PageView_name: Property = Property(name="name", type=StringType)
classLayout2Frontend_Views_PageView_layoutType: Property = Property(name="layoutType", type=StringType)
classLayout2Frontend_Views_PageView.attributes={classLayout2Frontend_Views_PageView_layoutType, classLayout2Frontend_Views_PageView_name}

# classLayout2Frontend_Views_FileUpload class attributes and methods

# classLayout2Frontend_Views_List class attributes and methods
classLayout2Frontend_Views_List_multiple: Property = Property(name="multiple", type=BooleanType)
classLayout2Frontend_Views_List.attributes={classLayout2Frontend_Views_List_multiple}

# Relationships
entitiesmodel0: BinaryAssociation = BinaryAssociation(
    name="entitiesmodel0",
    ends={
        Property(name="EntitiesModel", type=classLayout2Frontend_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Project", type=EntitiesModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
siteViews1: BinaryAssociation = BinaryAssociation(
    name="siteViews1",
    ends={
        Property(name="SiteView", type=classLayout2Frontend_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Project2", type=SiteView, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pageViews3: BinaryAssociation = BinaryAssociation(
    name="pageViews3",
    ends={
        Property(name="PageView", type=classLayout2Frontend_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Project4", type=PageView, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="Entity", type=classLayout2Frontend_Entities_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Entities_Association", type=Entity, multiplicity=Multiplicity(1, 1))
    }
)
superclass9: BinaryAssociation = BinaryAssociation(
    name="superclass9",
    ends={
        Property(name="Entity10", type=classLayout2Frontend_Entities_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Entities_Entity", type=Entity, multiplicity=Multiplicity(0, 1))
    }
)
containerViews5: BinaryAssociation = BinaryAssociation(
    name="containerViews5",
    ends={
        Property(name="ContainerView", type=classLayout2Frontend_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Project6", type=ContainerView, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelElements7: BinaryAssociation = BinaryAssociation(
    name="modelElements7",
    ends={
        Property(name="EntityModelElement", type=classLayout2Frontend_Entities_EntitiesModel, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Entities_EntitiesModel", type=EntityModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pageViews15: BinaryAssociation = BinaryAssociation(
    name="pageViews15",
    ends={
        Property(name="PageView16", type=classLayout2Frontend_Views_SiteView, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Views_SiteView", type=PageView, multiplicity=Multiplicity(0, 9999))
    }
)
structuralFeatures11: BinaryAssociation = BinaryAssociation(
    name="structuralFeatures11",
    ends={
        Property(name="StructuralFeature", type=classLayout2Frontend_Entities_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Entities_Entity12", type=StructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type13: BinaryAssociation = BinaryAssociation(
    name="type13",
    ends={
        Property(name="PropertyType", type=classLayout2Frontend_Entities_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Entities_Property", type=PropertyType, multiplicity=Multiplicity(1, 1))
    }
)
literals14: BinaryAssociation = BinaryAssociation(
    name="literals14",
    ends={
        Property(name="Literal", type=classLayout2Frontend_Entities_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Entities_Enumeration", type=Literal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iterationFilters23: BinaryAssociation = BinaryAssociation(
    name="iterationFilters23",
    ends={
        Property(name="IterationFilter", type=classLayout2Frontend_Views_IterationContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Views_IterationContainer", type=IterationFilter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements17: BinaryAssociation = BinaryAssociation(
    name="elements17",
    ends={
        Property(name="ElementView", type=classLayout2Frontend_Views_ContainerView, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Views_ContainerView", type=ElementView, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity18: BinaryAssociation = BinaryAssociation(
    name="entity18",
    ends={
        Property(name="Entity20", type=classLayout2Frontend_Views_ContainerView, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Views_ContainerView19", type=Entity, multiplicity=Multiplicity(0, 1))
    }
)
property21: BinaryAssociation = BinaryAssociation(
    name="property21",
    ends={
        Property(name="StructuralFeature22", type=classLayout2Frontend_Views_AtomicView, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Views_AtomicView", type=StructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
input26: BinaryAssociation = BinaryAssociation(
    name="input26",
    ends={
        Property(name="Input", type=classLayout2Frontend_Views_IterationFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Views_IterationFilter", type=Input, multiplicity=Multiplicity(0, 1))
    }
)
elementViews24: BinaryAssociation = BinaryAssociation(
    name="elementViews24",
    ends={
        Property(name="ElementView25", type=classLayout2Frontend_Views_PageView, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Views_PageView", type=ElementView, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_classLayout2Frontend_Entities_Composition_Association = Generalization(general=Association, specific=classLayout2Frontend_Entities_Composition)
gen_classLayout2Frontend_Entities_Reference_Association = Generalization(general=Association, specific=classLayout2Frontend_Entities_Reference)
gen_classLayout2Frontend_Entities_Entity_EntityModelElement = Generalization(general=EntityModelElement, specific=classLayout2Frontend_Entities_Entity)
gen_classLayout2Frontend_Entities_Association_StructuralFeature = Generalization(general=StructuralFeature, specific=classLayout2Frontend_Entities_Association)
gen_classLayout2Frontend_Entities_PrimitiveType_PropertyType = Generalization(general=PropertyType, specific=classLayout2Frontend_Entities_PrimitiveType)
gen_classLayout2Frontend_Entities_StructuralFeature_EntityModelElement = Generalization(general=EntityModelElement, specific=classLayout2Frontend_Entities_StructuralFeature)
gen_classLayout2Frontend_Entities_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=classLayout2Frontend_Entities_Property)
gen_classLayout2Frontend_Entities_Enumeration_PropertyType = Generalization(general=PropertyType, specific=classLayout2Frontend_Entities_Enumeration)
gen_classLayout2Frontend_Entities_PropertyType_EntityModelElement = Generalization(general=EntityModelElement, specific=classLayout2Frontend_Entities_PropertyType)
gen_classLayout2Frontend_Entities_Literal_EntityModelElement = Generalization(general=EntityModelElement, specific=classLayout2Frontend_Entities_Literal)
gen_classLayout2Frontend_Views_IterationContainer_ContainerView = Generalization(general=ContainerView, specific=classLayout2Frontend_Views_IterationContainer)
gen_classLayout2Frontend_Views_InputForm_ContainerView = Generalization(general=ContainerView, specific=classLayout2Frontend_Views_InputForm)
gen_classLayout2Frontend_Views_StaticContainer_ContainerView = Generalization(general=ContainerView, specific=classLayout2Frontend_Views_StaticContainer)
gen_classLayout2Frontend_Views_Input_AtomicView = Generalization(general=AtomicView, specific=classLayout2Frontend_Views_Input)
gen_classLayout2Frontend_Views_ContainerView_ElementView = Generalization(general=ElementView, specific=classLayout2Frontend_Views_ContainerView)
gen_classLayout2Frontend_Views_AtomicView_ElementView = Generalization(general=ElementView, specific=classLayout2Frontend_Views_AtomicView)
gen_classLayout2Frontend_Views_Dropdownlist_Selection = Generalization(general=Selection, specific=classLayout2Frontend_Views_Dropdownlist)
gen_classLayout2Frontend_Views_RadioButtonGroup_Selection = Generalization(general=Selection, specific=classLayout2Frontend_Views_RadioButtonGroup)
gen_classLayout2Frontend_Views_CheckList_Selection = Generalization(general=Selection, specific=classLayout2Frontend_Views_CheckList)
gen_classLayout2Frontend_Views_InputText_Input = Generalization(general=Input, specific=classLayout2Frontend_Views_InputText)
gen_classLayout2Frontend_Views_Selection_Input = Generalization(general=Input, specific=classLayout2Frontend_Views_Selection)
gen_classLayout2Frontend_Views_Output_AtomicView = Generalization(general=AtomicView, specific=classLayout2Frontend_Views_Output)
gen_classLayout2Frontend_Views_TextArea_Output = Generalization(general=Output, specific=classLayout2Frontend_Views_TextArea)
gen_classLayout2Frontend_Views_Image_Output = Generalization(general=Output, specific=classLayout2Frontend_Views_Image)
gen_classLayout2Frontend_Views_Autocomplete_Selection = Generalization(general=Selection, specific=classLayout2Frontend_Views_Autocomplete)
gen_classLayout2Frontend_Views_FileUpload_Input = Generalization(general=Input, specific=classLayout2Frontend_Views_FileUpload)
gen_classLayout2Frontend_Views_List_Selection = Generalization(general=Selection, specific=classLayout2Frontend_Views_List)

# Domain Model
domain_model = DomainModel(
    name="classLayout2Frontend",
    types={classLayout2Frontend_Project, EntitiesModel, SiteView, PageView, Entity, classLayout2Frontend_Entities_Composition, Association, classLayout2Frontend_Entities_Reference, classLayout2Frontend_Entities_Entity, ContainerView, classLayout2Frontend_Entities_EntitiesModel, EntityModelElement, classLayout2Frontend_Entities_EntityModelElement, classLayout2Frontend_Entities_Association, StructuralFeature, classLayout2Frontend_Entities_StructuralFeature, classLayout2Frontend_Views_SiteView, classLayout2Frontend_Entities_Property, PropertyType, classLayout2Frontend_Entities_Enumeration, Literal, classLayout2Frontend_Entities_PropertyType, classLayout2Frontend_Entities_Literal, classLayout2Frontend_Entities_PrimitiveType, classLayout2Frontend_Views_IterationContainer, IterationFilter, classLayout2Frontend_Views_InputForm, classLayout2Frontend_Views_StaticContainer, classLayout2Frontend_Views_Input, AtomicView, classLayout2Frontend_Views_ContainerView, ElementView, classLayout2Frontend_Views_AtomicView, classLayout2Frontend_Views_ElementView, classLayout2Frontend_Views_IterationFilter, classLayout2Frontend_Views_Dropdownlist, Selection, classLayout2Frontend_Views_RadioButtonGroup, classLayout2Frontend_Views_CheckList, classLayout2Frontend_Views_Autocomplete, classLayout2Frontend_Views_InputText, Input, classLayout2Frontend_Views_Selection, classLayout2Frontend_Views_Output, classLayout2Frontend_Views_TextArea, Output, classLayout2Frontend_Views_Image, classLayout2Frontend_Views_PageView, classLayout2Frontend_Views_FileUpload, classLayout2Frontend_Views_List, LayoutType},
    associations={entitiesmodel0, siteViews1, pageViews3, target8, superclass9, containerViews5, modelElements7, pageViews15, structuralFeatures11, type13, literals14, iterationFilters23, elements17, entity18, property21, input26, elementViews24},
    generalizations={gen_classLayout2Frontend_Entities_Composition_Association, gen_classLayout2Frontend_Entities_Reference_Association, gen_classLayout2Frontend_Entities_Entity_EntityModelElement, gen_classLayout2Frontend_Entities_Association_StructuralFeature, gen_classLayout2Frontend_Entities_PrimitiveType_PropertyType, gen_classLayout2Frontend_Entities_StructuralFeature_EntityModelElement, gen_classLayout2Frontend_Entities_Property_StructuralFeature, gen_classLayout2Frontend_Entities_Enumeration_PropertyType, gen_classLayout2Frontend_Entities_PropertyType_EntityModelElement, gen_classLayout2Frontend_Entities_Literal_EntityModelElement, gen_classLayout2Frontend_Views_IterationContainer_ContainerView, gen_classLayout2Frontend_Views_InputForm_ContainerView, gen_classLayout2Frontend_Views_StaticContainer_ContainerView, gen_classLayout2Frontend_Views_Input_AtomicView, gen_classLayout2Frontend_Views_ContainerView_ElementView, gen_classLayout2Frontend_Views_AtomicView_ElementView, gen_classLayout2Frontend_Views_Dropdownlist_Selection, gen_classLayout2Frontend_Views_RadioButtonGroup_Selection, gen_classLayout2Frontend_Views_CheckList_Selection, gen_classLayout2Frontend_Views_InputText_Input, gen_classLayout2Frontend_Views_Selection_Input, gen_classLayout2Frontend_Views_Output_AtomicView, gen_classLayout2Frontend_Views_TextArea_Output, gen_classLayout2Frontend_Views_Image_Output, gen_classLayout2Frontend_Views_Autocomplete_Selection, gen_classLayout2Frontend_Views_FileUpload_Input, gen_classLayout2Frontend_Views_List_Selection},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)