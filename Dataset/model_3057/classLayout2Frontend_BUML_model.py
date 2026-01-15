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
classLayout2Frontend_PageView = Class(name="classLayout2Frontend::PageView")
classLayout2Frontend_ContainerView = Class(name="classLayout2Frontend::ContainerView", is_abstract=True)
classLayout2Frontend_Composition = Class(name="classLayout2Frontend::Composition")
Association = Class(name="Association")
classLayout2Frontend_Association = Class(name="classLayout2Frontend::Association", is_abstract=True)
StructuralFeature = Class(name="StructuralFeature")
classLayout2Frontend_Entity = Class(name="classLayout2Frontend::Entity")
classLayout2Frontend_PropertyType = Class(name="classLayout2Frontend::PropertyType", is_abstract=True)
EntityModelElement = Class(name="EntityModelElement")
classLayout2Frontend_Property = Class(name="classLayout2Frontend::Property")
classLayout2Frontend_EntitiesModel = Class(name="classLayout2Frontend::EntitiesModel")
classLayout2Frontend_SiteView = Class(name="classLayout2Frontend::SiteView")
classLayout2Frontend_EntityModelElement = Class(name="classLayout2Frontend::EntityModelElement", is_abstract=True)
classLayout2Frontend_PrimitiveType = Class(name="classLayout2Frontend::PrimitiveType")
PropertyType = Class(name="PropertyType")
classLayout2Frontend_Literal = Class(name="classLayout2Frontend::Literal")
classLayout2Frontend_Enumeration = Class(name="classLayout2Frontend::Enumeration")
classLayout2Frontend_StructuralFeature = Class(name="classLayout2Frontend::StructuralFeature", is_abstract=True)
classLayout2Frontend_AtomicView = Class(name="classLayout2Frontend::AtomicView", is_abstract=True)
ElementView = Class(name="ElementView")
classLayout2Frontend_Autocomplete = Class(name="classLayout2Frontend::Autocomplete")
Selection = Class(name="Selection")
classLayout2Frontend_Dropdownlist = Class(name="classLayout2Frontend::Dropdownlist")
classLayout2Frontend_Image = Class(name="classLayout2Frontend::Image")
Output = Class(name="Output")
classLayout2Frontend_List = Class(name="classLayout2Frontend::List")
classLayout2Frontend_Output = Class(name="classLayout2Frontend::Output", is_abstract=True)
AtomicView = Class(name="AtomicView")
classLayout2Frontend_IterationFilter = Class(name="classLayout2Frontend::IterationFilter")
classLayout2Frontend_Input = Class(name="classLayout2Frontend::Input", is_abstract=True)
classLayout2Frontend_InputText = Class(name="classLayout2Frontend::InputText")
Input = Class(name="Input")
classLayout2Frontend_Reference = Class(name="classLayout2Frontend::Reference")
classLayout2Frontend_ElementView = Class(name="classLayout2Frontend::ElementView", is_abstract=True)
classLayout2Frontend_StaticContainer = Class(name="classLayout2Frontend::StaticContainer")
ContainerView = Class(name="ContainerView")
classLayout2Frontend_TextArea = Class(name="classLayout2Frontend::TextArea")
classLayout2Frontend_IterationContainer = Class(name="classLayout2Frontend::IterationContainer")
classLayout2Frontend_InputForm = Class(name="classLayout2Frontend::InputForm")
classLayout2Frontend_CheckList = Class(name="classLayout2Frontend::CheckList")
classLayout2Frontend_RadioButtonGroup = Class(name="classLayout2Frontend::RadioButtonGroup")
classLayout2Frontend_FileUpload = Class(name="classLayout2Frontend::FileUpload")
classLayout2Frontend_Selection = Class(name="classLayout2Frontend::Selection", is_abstract=True)

# classLayout2Frontend_Project class attributes and methods
classLayout2Frontend_Project_name: Property = Property(name="name", type=StringType)
classLayout2Frontend_Project.attributes={classLayout2Frontend_Project_name}

# classLayout2Frontend_PageView class attributes and methods
classLayout2Frontend_PageView_layoutType: Property = Property(name="layoutType", type=StringType)
classLayout2Frontend_PageView_name: Property = Property(name="name", type=StringType)
classLayout2Frontend_PageView.attributes={classLayout2Frontend_PageView_layoutType, classLayout2Frontend_PageView_name}

# classLayout2Frontend_ContainerView class attributes and methods

# classLayout2Frontend_Composition class attributes and methods

# Association class attributes and methods

# classLayout2Frontend_Association class attributes and methods
classLayout2Frontend_Association_many: Property = Property(name="many", type=BooleanType)
classLayout2Frontend_Association.attributes={classLayout2Frontend_Association_many}

# StructuralFeature class attributes and methods

# classLayout2Frontend_Entity class attributes and methods
classLayout2Frontend_Entity_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
classLayout2Frontend_Entity.attributes={classLayout2Frontend_Entity_isAbstract}

# classLayout2Frontend_PropertyType class attributes and methods

# EntityModelElement class attributes and methods

# classLayout2Frontend_Property class attributes and methods
classLayout2Frontend_Property_defaultValue: Property = Property(name="defaultValue", type=StringType)
classLayout2Frontend_Property.attributes={classLayout2Frontend_Property_defaultValue}

# classLayout2Frontend_EntitiesModel class attributes and methods
classLayout2Frontend_EntitiesModel_name: Property = Property(name="name", type=StringType)
classLayout2Frontend_EntitiesModel.attributes={classLayout2Frontend_EntitiesModel_name}

# classLayout2Frontend_SiteView class attributes and methods
classLayout2Frontend_SiteView_name: Property = Property(name="name", type=StringType)
classLayout2Frontend_SiteView_templateName: Property = Property(name="templateName", type=StringType)
classLayout2Frontend_SiteView_templateColor: Property = Property(name="templateColor", type=StringType)
classLayout2Frontend_SiteView_displayName: Property = Property(name="displayName", type=StringType)
classLayout2Frontend_SiteView.attributes={classLayout2Frontend_SiteView_displayName, classLayout2Frontend_SiteView_templateName, classLayout2Frontend_SiteView_name, classLayout2Frontend_SiteView_templateColor}

# classLayout2Frontend_EntityModelElement class attributes and methods
classLayout2Frontend_EntityModelElement_name: Property = Property(name="name", type=StringType)
classLayout2Frontend_EntityModelElement_description: Property = Property(name="description", type=StringType)
classLayout2Frontend_EntityModelElement_displayName: Property = Property(name="displayName", type=StringType)
classLayout2Frontend_EntityModelElement.attributes={classLayout2Frontend_EntityModelElement_displayName, classLayout2Frontend_EntityModelElement_name, classLayout2Frontend_EntityModelElement_description}

# classLayout2Frontend_PrimitiveType class attributes and methods

# PropertyType class attributes and methods

# classLayout2Frontend_Literal class attributes and methods
classLayout2Frontend_Literal_value: Property = Property(name="value", type=IntegerType)
classLayout2Frontend_Literal.attributes={classLayout2Frontend_Literal_value}

# classLayout2Frontend_Enumeration class attributes and methods

# classLayout2Frontend_StructuralFeature class attributes and methods
classLayout2Frontend_StructuralFeature_required: Property = Property(name="required", type=BooleanType)
classLayout2Frontend_StructuralFeature.attributes={classLayout2Frontend_StructuralFeature_required}

# classLayout2Frontend_AtomicView class attributes and methods

# ElementView class attributes and methods

# classLayout2Frontend_Autocomplete class attributes and methods
classLayout2Frontend_Autocomplete_multiple: Property = Property(name="multiple", type=BooleanType)
classLayout2Frontend_Autocomplete.attributes={classLayout2Frontend_Autocomplete_multiple}

# Selection class attributes and methods

# classLayout2Frontend_Dropdownlist class attributes and methods

# classLayout2Frontend_Image class attributes and methods
classLayout2Frontend_Image_width: Property = Property(name="width", type=FloatType)
classLayout2Frontend_Image_height: Property = Property(name="height", type=FloatType)
classLayout2Frontend_Image.attributes={classLayout2Frontend_Image_width, classLayout2Frontend_Image_height}

# Output class attributes and methods

# classLayout2Frontend_List class attributes and methods
classLayout2Frontend_List_multiple: Property = Property(name="multiple", type=BooleanType)
classLayout2Frontend_List.attributes={classLayout2Frontend_List_multiple}

# classLayout2Frontend_Output class attributes and methods

# AtomicView class attributes and methods

# classLayout2Frontend_IterationFilter class attributes and methods

# classLayout2Frontend_Input class attributes and methods
classLayout2Frontend_Input_label: Property = Property(name="label", type=StringType)
classLayout2Frontend_Input.attributes={classLayout2Frontend_Input_label}

# classLayout2Frontend_InputText class attributes and methods
classLayout2Frontend_InputText_multiline: Property = Property(name="multiline", type=BooleanType)
classLayout2Frontend_InputText.attributes={classLayout2Frontend_InputText_multiline}

# Input class attributes and methods

# classLayout2Frontend_Reference class attributes and methods

# classLayout2Frontend_ElementView class attributes and methods
classLayout2Frontend_ElementView_name: Property = Property(name="name", type=StringType)
classLayout2Frontend_ElementView_displayName: Property = Property(name="displayName", type=StringType)
classLayout2Frontend_ElementView_description: Property = Property(name="description", type=StringType)
classLayout2Frontend_ElementView.attributes={classLayout2Frontend_ElementView_description, classLayout2Frontend_ElementView_displayName, classLayout2Frontend_ElementView_name}

# classLayout2Frontend_StaticContainer class attributes and methods

# ContainerView class attributes and methods

# classLayout2Frontend_TextArea class attributes and methods
classLayout2Frontend_TextArea_value: Property = Property(name="value", type=StringType)
classLayout2Frontend_TextArea_isTitle: Property = Property(name="isTitle", type=BooleanType)
classLayout2Frontend_TextArea.attributes={classLayout2Frontend_TextArea_value, classLayout2Frontend_TextArea_isTitle}

# classLayout2Frontend_IterationContainer class attributes and methods

# classLayout2Frontend_InputForm class attributes and methods

# classLayout2Frontend_CheckList class attributes and methods

# classLayout2Frontend_RadioButtonGroup class attributes and methods

# classLayout2Frontend_FileUpload class attributes and methods

# classLayout2Frontend_Selection class attributes and methods

# Relationships
siteViews1: BinaryAssociation = BinaryAssociation(
    name="siteViews1",
    ends={
        Property(name="classLayout2Frontend_SiteView", type=classLayout2Frontend_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Project2", type=classLayout2Frontend_SiteView, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pageViews3: BinaryAssociation = BinaryAssociation(
    name="pageViews3",
    ends={
        Property(name="classLayout2Frontend_PageView", type=classLayout2Frontend_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Project4", type=classLayout2Frontend_PageView, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containerViews5: BinaryAssociation = BinaryAssociation(
    name="containerViews5",
    ends={
        Property(name="classLayout2Frontend_ContainerView", type=classLayout2Frontend_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Project6", type=classLayout2Frontend_ContainerView, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="classLayout2Frontend_Entity", type=classLayout2Frontend_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Association", type=classLayout2Frontend_Entity, multiplicity=Multiplicity(1, 1))
    }
)
type8: BinaryAssociation = BinaryAssociation(
    name="type8",
    ends={
        Property(name="classLayout2Frontend_PropertyType", type=classLayout2Frontend_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Property", type=classLayout2Frontend_PropertyType, multiplicity=Multiplicity(1, 1))
    }
)
entitiesmodel0: BinaryAssociation = BinaryAssociation(
    name="entitiesmodel0",
    ends={
        Property(name="classLayout2Frontend_EntitiesModel", type=classLayout2Frontend_Project, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Project", type=classLayout2Frontend_EntitiesModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modelElements9: BinaryAssociation = BinaryAssociation(
    name="modelElements9",
    ends={
        Property(name="classLayout2Frontend_EntityModelElement", type=classLayout2Frontend_EntitiesModel, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_EntitiesModel10", type=classLayout2Frontend_EntityModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superclass12: BinaryAssociation = BinaryAssociation(
    name="superclass12",
    ends={
        Property(name="classLayout2Frontend_Entity13", type=classLayout2Frontend_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Entity11", type=classLayout2Frontend_Entity, multiplicity=Multiplicity(0, 1))
    }
)
structuralFeatures14: BinaryAssociation = BinaryAssociation(
    name="structuralFeatures14",
    ends={
        Property(name="classLayout2Frontend_StructuralFeature", type=classLayout2Frontend_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Entity15", type=classLayout2Frontend_StructuralFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property17: BinaryAssociation = BinaryAssociation(
    name="property17",
    ends={
        Property(name="classLayout2Frontend_StructuralFeature18", type=classLayout2Frontend_AtomicView, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_AtomicView", type=classLayout2Frontend_StructuralFeature, multiplicity=Multiplicity(0, 1))
    }
)
input19: BinaryAssociation = BinaryAssociation(
    name="input19",
    ends={
        Property(name="classLayout2Frontend_Input", type=classLayout2Frontend_IterationFilter, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_IterationFilter", type=classLayout2Frontend_Input, multiplicity=Multiplicity(0, 1))
    }
)
literals16: BinaryAssociation = BinaryAssociation(
    name="literals16",
    ends={
        Property(name="classLayout2Frontend_Literal", type=classLayout2Frontend_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_Enumeration", type=classLayout2Frontend_Literal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementViews20: BinaryAssociation = BinaryAssociation(
    name="elementViews20",
    ends={
        Property(name="classLayout2Frontend_ElementView", type=classLayout2Frontend_PageView, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_PageView21", type=classLayout2Frontend_ElementView, multiplicity=Multiplicity(0, 9999))
    }
)
pageViews22: BinaryAssociation = BinaryAssociation(
    name="pageViews22",
    ends={
        Property(name="classLayout2Frontend_PageView24", type=classLayout2Frontend_SiteView, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_SiteView23", type=classLayout2Frontend_PageView, multiplicity=Multiplicity(0, 9999))
    }
)
iterationFilters25: BinaryAssociation = BinaryAssociation(
    name="iterationFilters25",
    ends={
        Property(name="classLayout2Frontend_IterationFilter26", type=classLayout2Frontend_IterationContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_IterationContainer", type=classLayout2Frontend_IterationFilter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements27: BinaryAssociation = BinaryAssociation(
    name="elements27",
    ends={
        Property(name="classLayout2Frontend_ElementView29", type=classLayout2Frontend_ContainerView, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_ContainerView28", type=classLayout2Frontend_ElementView, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity30: BinaryAssociation = BinaryAssociation(
    name="entity30",
    ends={
        Property(name="classLayout2Frontend_Entity32", type=classLayout2Frontend_ContainerView, multiplicity=Multiplicity(1, 1)),
        Property(name="classLayout2Frontend_ContainerView31", type=classLayout2Frontend_Entity, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_classLayout2Frontend_Composition_Association = Generalization(general=Association, specific=classLayout2Frontend_Composition)
gen_classLayout2Frontend_Association_StructuralFeature = Generalization(general=StructuralFeature, specific=classLayout2Frontend_Association)
gen_classLayout2Frontend_PropertyType_EntityModelElement = Generalization(general=EntityModelElement, specific=classLayout2Frontend_PropertyType)
gen_classLayout2Frontend_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=classLayout2Frontend_Property)
gen_classLayout2Frontend_Entity_EntityModelElement = Generalization(general=EntityModelElement, specific=classLayout2Frontend_Entity)
gen_classLayout2Frontend_PrimitiveType_PropertyType = Generalization(general=PropertyType, specific=classLayout2Frontend_PrimitiveType)
gen_classLayout2Frontend_Literal_EntityModelElement = Generalization(general=EntityModelElement, specific=classLayout2Frontend_Literal)
gen_classLayout2Frontend_Enumeration_PropertyType = Generalization(general=PropertyType, specific=classLayout2Frontend_Enumeration)
gen_classLayout2Frontend_StructuralFeature_EntityModelElement = Generalization(general=EntityModelElement, specific=classLayout2Frontend_StructuralFeature)
gen_classLayout2Frontend_Reference_Association = Generalization(general=Association, specific=classLayout2Frontend_Reference)
gen_classLayout2Frontend_AtomicView_ElementView = Generalization(general=ElementView, specific=classLayout2Frontend_AtomicView)
gen_classLayout2Frontend_Autocomplete_Selection = Generalization(general=Selection, specific=classLayout2Frontend_Autocomplete)
gen_classLayout2Frontend_Dropdownlist_Selection = Generalization(general=Selection, specific=classLayout2Frontend_Dropdownlist)
gen_classLayout2Frontend_Image_Output = Generalization(general=Output, specific=classLayout2Frontend_Image)
gen_classLayout2Frontend_List_Selection = Generalization(general=Selection, specific=classLayout2Frontend_List)
gen_classLayout2Frontend_Output_AtomicView = Generalization(general=AtomicView, specific=classLayout2Frontend_Output)
gen_classLayout2Frontend_InputText_Input = Generalization(general=Input, specific=classLayout2Frontend_InputText)
gen_classLayout2Frontend_StaticContainer_ContainerView = Generalization(general=ContainerView, specific=classLayout2Frontend_StaticContainer)
gen_classLayout2Frontend_TextArea_Output = Generalization(general=Output, specific=classLayout2Frontend_TextArea)
gen_classLayout2Frontend_IterationContainer_ContainerView = Generalization(general=ContainerView, specific=classLayout2Frontend_IterationContainer)
gen_classLayout2Frontend_InputForm_ContainerView = Generalization(general=ContainerView, specific=classLayout2Frontend_InputForm)
gen_classLayout2Frontend_CheckList_Selection = Generalization(general=Selection, specific=classLayout2Frontend_CheckList)
gen_classLayout2Frontend_RadioButtonGroup_Selection = Generalization(general=Selection, specific=classLayout2Frontend_RadioButtonGroup)
gen_classLayout2Frontend_ContainerView_ElementView = Generalization(general=ElementView, specific=classLayout2Frontend_ContainerView)
gen_classLayout2Frontend_FileUpload_Input = Generalization(general=Input, specific=classLayout2Frontend_FileUpload)
gen_classLayout2Frontend_Selection_Input = Generalization(general=Input, specific=classLayout2Frontend_Selection)
gen_classLayout2Frontend_Input_AtomicView = Generalization(general=AtomicView, specific=classLayout2Frontend_Input)

# Domain Model
domain_model = DomainModel(
    name="classLayout2Frontend",
    types={classLayout2Frontend_Project, classLayout2Frontend_PageView, classLayout2Frontend_ContainerView, classLayout2Frontend_Composition, Association, classLayout2Frontend_Association, StructuralFeature, classLayout2Frontend_Entity, classLayout2Frontend_PropertyType, EntityModelElement, classLayout2Frontend_Property, classLayout2Frontend_EntitiesModel, classLayout2Frontend_SiteView, classLayout2Frontend_EntityModelElement, classLayout2Frontend_PrimitiveType, PropertyType, classLayout2Frontend_Literal, classLayout2Frontend_Enumeration, classLayout2Frontend_StructuralFeature, classLayout2Frontend_AtomicView, ElementView, classLayout2Frontend_Autocomplete, Selection, classLayout2Frontend_Dropdownlist, classLayout2Frontend_Image, Output, classLayout2Frontend_List, classLayout2Frontend_Output, AtomicView, classLayout2Frontend_IterationFilter, classLayout2Frontend_Input, classLayout2Frontend_InputText, Input, classLayout2Frontend_Reference, classLayout2Frontend_ElementView, classLayout2Frontend_StaticContainer, ContainerView, classLayout2Frontend_TextArea, classLayout2Frontend_IterationContainer, classLayout2Frontend_InputForm, classLayout2Frontend_CheckList, classLayout2Frontend_RadioButtonGroup, classLayout2Frontend_FileUpload, classLayout2Frontend_Selection, LayoutType},
    associations={siteViews1, pageViews3, containerViews5, target7, type8, entitiesmodel0, modelElements9, superclass12, structuralFeatures14, property17, input19, literals16, elementViews20, pageViews22, iterationFilters25, elements27, entity30},
    generalizations={gen_classLayout2Frontend_Composition_Association, gen_classLayout2Frontend_Association_StructuralFeature, gen_classLayout2Frontend_PropertyType_EntityModelElement, gen_classLayout2Frontend_Property_StructuralFeature, gen_classLayout2Frontend_Entity_EntityModelElement, gen_classLayout2Frontend_PrimitiveType_PropertyType, gen_classLayout2Frontend_Literal_EntityModelElement, gen_classLayout2Frontend_Enumeration_PropertyType, gen_classLayout2Frontend_StructuralFeature_EntityModelElement, gen_classLayout2Frontend_Reference_Association, gen_classLayout2Frontend_AtomicView_ElementView, gen_classLayout2Frontend_Autocomplete_Selection, gen_classLayout2Frontend_Dropdownlist_Selection, gen_classLayout2Frontend_Image_Output, gen_classLayout2Frontend_List_Selection, gen_classLayout2Frontend_Output_AtomicView, gen_classLayout2Frontend_InputText_Input, gen_classLayout2Frontend_StaticContainer_ContainerView, gen_classLayout2Frontend_TextArea_Output, gen_classLayout2Frontend_IterationContainer_ContainerView, gen_classLayout2Frontend_InputForm_ContainerView, gen_classLayout2Frontend_CheckList_Selection, gen_classLayout2Frontend_RadioButtonGroup_Selection, gen_classLayout2Frontend_ContainerView_ElementView, gen_classLayout2Frontend_FileUpload_Input, gen_classLayout2Frontend_Selection_Input, gen_classLayout2Frontend_Input_AtomicView},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)