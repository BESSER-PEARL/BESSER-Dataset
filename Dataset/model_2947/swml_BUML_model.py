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
SWMLType: Enumeration = Enumeration(
    name="SWMLType",
    literals={
            EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Float"),
			EnumerationLiteral(name="Email"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="Time"),
			EnumerationLiteral(name="Date")
    }
)

# Classes
swml_WebApplication = Class(name="swml::WebApplication")
swml_ContentModel = Class(name="swml::ContentModel")
swml_HypertextModel = Class(name="swml::HypertextModel")
swml_EntityType = Class(name="swml::EntityType")
swml_Attribute = Class(name="swml::Attribute")
swml_Relationship = Class(name="swml::Relationship")
swml_Enumeration = Class(name="swml::Enumeration")
swml_Link = Class(name="swml::Link", is_abstract=True)
swml_Node = Class(name="swml::Node", is_abstract=True)
swml_Page = Class(name="swml::Page", is_abstract=True)
Node = Class(name="Node")
swml_ContextualLink = Class(name="swml::ContextualLink")
Link = Class(name="Link")
swml_NonContextualLink = Class(name="swml::NonContextualLink")
swml_IndexPage = Class(name="swml::IndexPage")
DynamicPage = Class(name="DynamicPage")
swml_EntityPage = Class(name="swml::EntityPage")
swml_DynamicPage = Class(name="swml::DynamicPage", is_abstract=True)
swml_UpdatePage = Class(name="swml::UpdatePage")
EntityPage = Class(name="EntityPage")
swml_DeletePage = Class(name="swml::DeletePage")
swml_CreatePage = Class(name="swml::CreatePage")
swml_StaticPage = Class(name="swml::StaticPage")
Page = Class(name="Page")
swml_Parameter = Class(name="swml::Parameter")
swml_OKLink = Class(name="swml::OKLink")
swml_KOLink = Class(name="swml::KOLink")
swml_LinkJoinNode = Class(name="swml::LinkJoinNode")
swml_Literal = Class(name="swml::Literal")

# swml_WebApplication class attributes and methods
swml_WebApplication_name: Property = Property(name="name", type=StringType)
swml_WebApplication.attributes={swml_WebApplication_name}

# swml_ContentModel class attributes and methods

# swml_HypertextModel class attributes and methods

# swml_EntityType class attributes and methods
swml_EntityType_name: Property = Property(name="name", type=StringType)
swml_EntityType_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
swml_EntityType.attributes={swml_EntityType_isAbstract, swml_EntityType_name}

# swml_Attribute class attributes and methods
swml_Attribute_name: Property = Property(name="name", type=StringType)
swml_Attribute_type: Property = Property(name="type", type=StringType)
swml_Attribute.attributes={swml_Attribute_type, swml_Attribute_name}

# swml_Relationship class attributes and methods
swml_Relationship_name: Property = Property(name="name", type=StringType)
swml_Relationship_upper: Property = Property(name="upper", type=IntegerType)
swml_Relationship_lower: Property = Property(name="lower", type=IntegerType)
swml_Relationship.attributes={swml_Relationship_lower, swml_Relationship_name, swml_Relationship_upper}

# swml_Enumeration class attributes and methods
swml_Enumeration_name: Property = Property(name="name", type=StringType)
swml_Enumeration.attributes={swml_Enumeration_name}

# swml_Link class attributes and methods

# swml_Node class attributes and methods

# swml_Page class attributes and methods
swml_Page_name: Property = Property(name="name", type=StringType)
swml_Page.attributes={swml_Page_name}

# Node class attributes and methods

# swml_ContextualLink class attributes and methods

# Link class attributes and methods

# swml_NonContextualLink class attributes and methods

# swml_IndexPage class attributes and methods

# DynamicPage class attributes and methods

# swml_EntityPage class attributes and methods

# swml_DynamicPage class attributes and methods

# swml_UpdatePage class attributes and methods

# EntityPage class attributes and methods

# swml_DeletePage class attributes and methods

# swml_CreatePage class attributes and methods

# swml_StaticPage class attributes and methods

# Page class attributes and methods

# swml_Parameter class attributes and methods
swml_Parameter_ValueSpec: Property = Property(name="ValueSpec", type=StringType)
swml_Parameter.attributes={swml_Parameter_ValueSpec}

# swml_OKLink class attributes and methods

# swml_KOLink class attributes and methods

# swml_LinkJoinNode class attributes and methods

# swml_Literal class attributes and methods
swml_Literal_name: Property = Property(name="name", type=StringType)
swml_Literal.attributes={swml_Literal_name}

# Relationships
contentModel0: BinaryAssociation = BinaryAssociation(
    name="contentModel0",
    ends={
        Property(name="swml_ContentModel", type=swml_WebApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_WebApplication", type=swml_ContentModel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
hyperTextModel1: BinaryAssociation = BinaryAssociation(
    name="hyperTextModel1",
    ends={
        Property(name="swml_HypertextModel", type=swml_WebApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_WebApplication2", type=swml_HypertextModel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
relationship7: BinaryAssociation = BinaryAssociation(
    name="relationship7",
    ends={
        Property(name="Relationship", type=swml_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="entityType", type=swml_Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superEntityType9: BinaryAssociation = BinaryAssociation(
    name="superEntityType9",
    ends={
        Property(name="swml_EntityType10", type=swml_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_EntityType8", type=swml_EntityType, multiplicity=Multiplicity(0, 1))
    }
)
EnumType11: BinaryAssociation = BinaryAssociation(
    name="EnumType11",
    ends={
        Property(name="swml_Enumeration", type=swml_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Attribute12", type=swml_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
source13: BinaryAssociation = BinaryAssociation(
    name="source13",
    ends={
        Property(name="Node", type=swml_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="link", type=swml_Node, multiplicity=Multiplicity(1, 1))
    }
)
attribute3: BinaryAssociation = BinaryAssociation(
    name="attribute3",
    ends={
        Property(name="swml_Attribute", type=swml_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_EntityType", type=swml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
id4: BinaryAssociation = BinaryAssociation(
    name="id4",
    ends={
        Property(name="swml_Attribute6", type=swml_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_EntityType5", type=swml_Attribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
innerPage17: BinaryAssociation = BinaryAssociation(
    name="innerPage17",
    ends={
        Property(name="swml_DynamicPage", type=swml_EntityPage, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_EntityPage", type=swml_DynamicPage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
displayedEntityType18: BinaryAssociation = BinaryAssociation(
    name="displayedEntityType18",
    ends={
        Property(name="swml_EntityType20", type=swml_DynamicPage, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_DynamicPage19", type=swml_EntityType, multiplicity=Multiplicity(1, 1))
    }
)
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="swml_Node", type=swml_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Link", type=swml_Node, multiplicity=Multiplicity(1, 1))
    }
)
parameter15: BinaryAssociation = BinaryAssociation(
    name="parameter15",
    ends={
        Property(name="swml_Parameter", type=swml_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Link16", type=swml_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entityType21: BinaryAssociation = BinaryAssociation(
    name="entityType21",
    ends={
        Property(name="EntityType", type=swml_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="relationship", type=swml_EntityType, multiplicity=Multiplicity(1, 1))
    }
)
opposite23: BinaryAssociation = BinaryAssociation(
    name="opposite23",
    ends={
        Property(name="swml_Relationship", type=swml_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Relationship22", type=swml_Relationship, multiplicity=Multiplicity(1, 1))
    }
)
target24: BinaryAssociation = BinaryAssociation(
    name="target24",
    ends={
        Property(name="swml_EntityType26", type=swml_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Relationship25", type=swml_EntityType, multiplicity=Multiplicity(1, 1))
    }
)
literals27: BinaryAssociation = BinaryAssociation(
    name="literals27",
    ends={
        Property(name="swml_Literal", type=swml_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_Enumeration28", type=swml_Literal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumerations29: BinaryAssociation = BinaryAssociation(
    name="enumerations29",
    ends={
        Property(name="swml_Enumeration31", type=swml_ContentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_ContentModel30", type=swml_Enumeration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entityType32: BinaryAssociation = BinaryAssociation(
    name="entityType32",
    ends={
        Property(name="swml_EntityType34", type=swml_ContentModel, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_ContentModel33", type=swml_EntityType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
link40: BinaryAssociation = BinaryAssociation(
    name="link40",
    ends={
        Property(name="Link", type=swml_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=swml_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
page35: BinaryAssociation = BinaryAssociation(
    name="page35",
    ends={
        Property(name="swml_Node37", type=swml_HypertextModel, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_HypertextModel36", type=swml_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
homepage38: BinaryAssociation = BinaryAssociation(
    name="homepage38",
    ends={
        Property(name="swml_StaticPage", type=swml_HypertextModel, multiplicity=Multiplicity(1, 1)),
        Property(name="swml_HypertextModel39", type=swml_StaticPage, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_swml_Page_Node = Generalization(general=Node, specific=swml_Page)
gen_swml_ContextualLink_Link = Generalization(general=Link, specific=swml_ContextualLink)
gen_swml_NonContextualLink_Link = Generalization(general=Link, specific=swml_NonContextualLink)
gen_swml_IndexPage_DynamicPage = Generalization(general=DynamicPage, specific=swml_IndexPage)
gen_swml_EntityPage_DynamicPage = Generalization(general=DynamicPage, specific=swml_EntityPage)
gen_swml_UpdatePage_EntityPage = Generalization(general=EntityPage, specific=swml_UpdatePage)
gen_swml_DeletePage_EntityPage = Generalization(general=EntityPage, specific=swml_DeletePage)
gen_swml_CreatePage_EntityPage = Generalization(general=EntityPage, specific=swml_CreatePage)
gen_swml_StaticPage_Page = Generalization(general=Page, specific=swml_StaticPage)
gen_swml_DynamicPage_Page = Generalization(general=Page, specific=swml_DynamicPage)
gen_swml_OKLink_Link = Generalization(general=Link, specific=swml_OKLink)
gen_swml_KOLink_Link = Generalization(general=Link, specific=swml_KOLink)
gen_swml_LinkJoinNode_Page = Generalization(general=Page, specific=swml_LinkJoinNode)
gen_swml_LinkJoinNode_Node = Generalization(general=Node, specific=swml_LinkJoinNode)

# Domain Model
domain_model = DomainModel(
    name="swml",
    types={swml_WebApplication, swml_ContentModel, swml_HypertextModel, swml_EntityType, swml_Attribute, swml_Relationship, swml_Enumeration, swml_Link, swml_Node, swml_Page, Node, swml_ContextualLink, Link, swml_NonContextualLink, swml_IndexPage, DynamicPage, swml_EntityPage, swml_DynamicPage, swml_UpdatePage, EntityPage, swml_DeletePage, swml_CreatePage, swml_StaticPage, Page, swml_Parameter, swml_OKLink, swml_KOLink, swml_LinkJoinNode, swml_Literal, SWMLType},
    associations={contentModel0, hyperTextModel1, relationship7, superEntityType9, EnumType11, source13, attribute3, id4, innerPage17, displayedEntityType18, target14, parameter15, entityType21, opposite23, target24, literals27, enumerations29, entityType32, link40, page35, homepage38},
    generalizations={gen_swml_Page_Node, gen_swml_ContextualLink_Link, gen_swml_NonContextualLink_Link, gen_swml_IndexPage_DynamicPage, gen_swml_EntityPage_DynamicPage, gen_swml_UpdatePage_EntityPage, gen_swml_DeletePage_EntityPage, gen_swml_CreatePage_EntityPage, gen_swml_StaticPage_Page, gen_swml_DynamicPage_Page, gen_swml_OKLink_Link, gen_swml_KOLink_Link, gen_swml_LinkJoinNode_Page, gen_swml_LinkJoinNode_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)