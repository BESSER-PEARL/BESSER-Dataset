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
article_Plugin = Class(name="article::Plugin")
article_Documentation = Class(name="article::Documentation")
StructuralElement = Class(name="StructuralElement")
article_Context = Class(name="article::Context")
article_EmbeddableElement = Class(name="article::EmbeddableElement", is_abstract=True)
article_Category = Class(name="article::Category")
Body = Class(name="Body")
article_Article = Class(name="article::Article")
Chapter = Class(name="Chapter")
article_Chapter = Class(name="article::Chapter")
article_Section = Class(name="article::Section")
article_LinkTarget = Class(name="article::LinkTarget", is_abstract=True)
Identifiable = Class(name="Identifiable")
BodyElementContainer = Class(name="BodyElementContainer")
article_Snippet = Class(name="article::Snippet")
EmbeddableElement = Class(name="EmbeddableElement")
article_Callout = Class(name="article::Callout")
article_Formatter = Class(name="article::Formatter", is_abstract=True)
article_Description = Class(name="article::Description")
article_Diagram = Class(name="article::Diagram")
BodyElement = Class(name="BodyElement")
article_Factory = Class(name="article::Factory", is_abstract=True)
article_JavaElement = Class(name="article::JavaElement")
LinkTarget = Class(name="LinkTarget")
article_StructuralElement = Class(name="article::StructuralElement", is_abstract=True)
article_Link = Class(name="article::Link")
article_Embedding = Class(name="article::Embedding")
article_SourceCode = Class(name="article::SourceCode")
ExternalTarget = Class(name="ExternalTarget")
article_JavaPackage = Class(name="article::JavaPackage")
article_ExternalTarget = Class(name="article::ExternalTarget")
article_Identifiable = Class(name="article::Identifiable", is_abstract=True)
article_Body = Class(name="article::Body", is_abstract=True)
article_BodyElementContainer = Class(name="article::BodyElementContainer", is_abstract=True)
article_BodyElement = Class(name="article::BodyElement", is_abstract=True)
article_Text = Class(name="article::Text")
article_Schemadoc = Class(name="article::Schemadoc")
article_Toc = Class(name="article::Toc")
article_ExtensionPoint = Class(name="article::ExtensionPoint")
article_Javadoc = Class(name="article::Javadoc")
Category = Class(name="Category")
article_ExternalArticle = Class(name="article::ExternalArticle")
Article = Class(name="Article")
article_Image = Class(name="article::Image")
article_TreeNode = Class(name="article::TreeNode")
article_PluginResource = Class(name="article::PluginResource")
ExternalArticle = Class(name="ExternalArticle")
article_Excel = Class(name="article::Excel")
article_JavaFormatter = Class(name="article::JavaFormatter")
Formatter = Class(name="Formatter")
article_XmlFormatter = Class(name="article::XmlFormatter")
article_TreeFormatter = Class(name="article::TreeFormatter")
article_Selection = Class(name="article::Selection")
article_ImageFormatter = Class(name="article::ImageFormatter")
article_HtmlFormatter = Class(name="article::HtmlFormatter")
article_TreeNodeProperty = Class(name="article::TreeNodeProperty")
article_ImageFactory = Class(name="article::ImageFactory")
Factory = Class(name="Factory")
article_Key = Class(name="article::Key")

# article_Plugin class attributes and methods
article_Plugin_name: Property = Property(name="name", type=StringType)
article_Plugin_label: Property = Property(name="label", type=StringType)
article_Plugin.attributes={article_Plugin_label, article_Plugin_name}

# article_Documentation class attributes and methods
article_Documentation_project: Property = Property(name="project", type=StringType)
article_Documentation.attributes={article_Documentation_project}

# StructuralElement class attributes and methods

# article_Context class attributes and methods
article_Context_baseFolder: Property = Property(name="baseFolder", type=StringType)
article_Context_project: Property = Property(name="project", type=StringType)
article_Context_root: Property = Property(name="root", type=StringType)
article_Context.attributes={article_Context_baseFolder, article_Context_root, article_Context_project}

# article_EmbeddableElement class attributes and methods
article_EmbeddableElement_doc: Property = Property(name="doc", type=StringType)
article_EmbeddableElement.attributes={article_EmbeddableElement_doc}

# article_Category class attributes and methods

# Body class attributes and methods

# article_Article class attributes and methods

# Chapter class attributes and methods

# article_Chapter class attributes and methods

# article_Section class attributes and methods

# article_LinkTarget class attributes and methods
article_LinkTarget_defaultLabel: Property = Property(name="defaultLabel", type=StringType)
article_LinkTarget_tooltip: Property = Property(name="tooltip", type=StringType)
article_LinkTarget_m_linkFrom: Method = Method(name="linkFrom", parameters={Parameter(name='source')}, type=StringType)
article_LinkTarget.attributes={article_LinkTarget_defaultLabel, article_LinkTarget_tooltip}
article_LinkTarget.methods={article_LinkTarget_m_linkFrom}

# Identifiable class attributes and methods

# BodyElementContainer class attributes and methods

# article_Snippet class attributes and methods
article_Snippet_title: Property = Property(name="title", type=StringType)
article_Snippet_titleImage: Property = Property(name="titleImage", type=StringType)
article_Snippet.attributes={article_Snippet_titleImage, article_Snippet_title}

# EmbeddableElement class attributes and methods

# article_Callout class attributes and methods

# article_Formatter class attributes and methods

# article_Description class attributes and methods

# article_Diagram class attributes and methods

# BodyElement class attributes and methods

# article_Factory class attributes and methods

# article_JavaElement class attributes and methods
article_JavaElement_classFile: Property = Property(name="classFile", type=StringType)
article_JavaElement.attributes={article_JavaElement_classFile}

# LinkTarget class attributes and methods

# article_StructuralElement class attributes and methods
article_StructuralElement_doc: Property = Property(name="doc", type=StringType)
article_StructuralElement_title: Property = Property(name="title", type=StringType)
article_StructuralElement.attributes={article_StructuralElement_title, article_StructuralElement_doc}

# article_Link class attributes and methods

# article_Embedding class attributes and methods

# article_SourceCode class attributes and methods

# ExternalTarget class attributes and methods

# article_JavaPackage class attributes and methods
article_JavaPackage_name: Property = Property(name="name", type=StringType)
article_JavaPackage.attributes={article_JavaPackage_name}

# article_ExternalTarget class attributes and methods
article_ExternalTarget_url: Property = Property(name="url", type=StringType)
article_ExternalTarget.attributes={article_ExternalTarget_url}

# article_Identifiable class attributes and methods
article_Identifiable_id: Property = Property(name="id", type=StringType)
article_Identifiable.attributes={article_Identifiable_id}

# article_Body class attributes and methods

# article_BodyElementContainer class attributes and methods

# article_BodyElement class attributes and methods
article_BodyElement_tag: Property = Property(name="tag", type=StringType)
article_BodyElement.attributes={article_BodyElement_tag}

# article_Text class attributes and methods

# article_Schemadoc class attributes and methods

# article_Toc class attributes and methods
article_Toc_levels: Property = Property(name="levels", type=IntegerType)
article_Toc.attributes={article_Toc_levels}

# article_ExtensionPoint class attributes and methods
article_ExtensionPoint_name: Property = Property(name="name", type=StringType)
article_ExtensionPoint.attributes={article_ExtensionPoint_name}

# article_Javadoc class attributes and methods

# Category class attributes and methods

# article_ExternalArticle class attributes and methods
article_ExternalArticle_url: Property = Property(name="url", type=StringType)
article_ExternalArticle.attributes={article_ExternalArticle_url}

# Article class attributes and methods

# article_Image class attributes and methods
article_Image_file: Property = Property(name="file", type=StringType)
article_Image.attributes={article_Image_file}

# article_TreeNode class attributes and methods
article_TreeNode_xmi_ID: Property = Property(name="xmi_ID", type=StringType)
article_TreeNode_image: Property = Property(name="image", type=StringType)
article_TreeNode_label: Property = Property(name="label", type=StringType)
article_TreeNode.attributes={article_TreeNode_image, article_TreeNode_xmi_ID, article_TreeNode_label}

# article_PluginResource class attributes and methods

# ExternalArticle class attributes and methods

# article_Excel class attributes and methods

# article_JavaFormatter class attributes and methods

# Formatter class attributes and methods

# article_XmlFormatter class attributes and methods
article_XmlFormatter_file: Property = Property(name="file", type=StringType)
article_XmlFormatter.attributes={article_XmlFormatter_file}

# article_TreeFormatter class attributes and methods
article_TreeFormatter_expanded: Property = Property(name="expanded", type=StringType)
article_TreeFormatter_selected: Property = Property(name="selected", type=StringType)
article_TreeFormatter_file: Property = Property(name="file", type=StringType)
article_TreeFormatter_expandTo: Property = Property(name="expandTo", type=IntegerType)
article_TreeFormatter.attributes={article_TreeFormatter_selected, article_TreeFormatter_expanded, article_TreeFormatter_expandTo, article_TreeFormatter_file}

# article_Selection class attributes and methods

# article_ImageFormatter class attributes and methods
article_ImageFormatter_file: Property = Property(name="file", type=StringType)
article_ImageFormatter.attributes={article_ImageFormatter_file}

# article_HtmlFormatter class attributes and methods
article_HtmlFormatter_file: Property = Property(name="file", type=StringType)
article_HtmlFormatter.attributes={article_HtmlFormatter_file}

# article_TreeNodeProperty class attributes and methods
article_TreeNodeProperty_key: Property = Property(name="key", type=StringType)
article_TreeNodeProperty_valueImage: Property = Property(name="valueImage", type=StringType)
article_TreeNodeProperty_value: Property = Property(name="value", type=StringType)
article_TreeNodeProperty.attributes={article_TreeNodeProperty_value, article_TreeNodeProperty_valueImage, article_TreeNodeProperty_key}

# article_ImageFactory class attributes and methods
article_ImageFactory_file: Property = Property(name="file", type=StringType)
article_ImageFactory.attributes={article_ImageFactory_file}

# Factory class attributes and methods

# article_Key class attributes and methods

# Relationships
dependencies3: BinaryAssociation = BinaryAssociation(
    name="dependencies3",
    ends={
        Property(name="article_Documentation", type=article_Documentation, multiplicity=Multiplicity(1, 1)),
        Property(name="article_Documentation2", type=article_Documentation, multiplicity=Multiplicity(0, 9999))
    }
)
plugins4: BinaryAssociation = BinaryAssociation(
    name="plugins4",
    ends={
        Property(name="article_Plugin", type=article_Documentation, multiplicity=Multiplicity(1, 1)),
        Property(name="article_Documentation5", type=article_Plugin, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context0: BinaryAssociation = BinaryAssociation(
    name="context0",
    ends={
        Property(name="Context", type=article_Documentation, multiplicity=Multiplicity(1, 1)),
        Property(name="documentations", type=article_Context, multiplicity=Multiplicity(1, 1))
    }
)
embeddableElements1: BinaryAssociation = BinaryAssociation(
    name="embeddableElements1",
    ends={
        Property(name="EmbeddableElement", type=article_Documentation, multiplicity=Multiplicity(1, 1)),
        Property(name="documentation", type=article_EmbeddableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
article7: BinaryAssociation = BinaryAssociation(
    name="article7",
    ends={
        Property(name="article_Article", type=article_Chapter, multiplicity=Multiplicity(1, 1)),
        Property(name="article_Chapter", type=article_Article, multiplicity=Multiplicity(1, 1))
    }
)
documentations6: BinaryAssociation = BinaryAssociation(
    name="documentations6",
    ends={
        Property(name="Documentation", type=article_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="context", type=article_Documentation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
snippet21: BinaryAssociation = BinaryAssociation(
    name="snippet21",
    ends={
        Property(name="Snippet", type=article_Callout, multiplicity=Multiplicity(1, 1)),
        Property(name="callouts", type=article_Snippet, multiplicity=Multiplicity(1, 1))
    }
)
sections8: BinaryAssociation = BinaryAssociation(
    name="sections8",
    ends={
        Property(name="Section", type=article_Chapter, multiplicity=Multiplicity(1, 1)),
        Property(name="chapter", type=article_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
documentation22: BinaryAssociation = BinaryAssociation(
    name="documentation22",
    ends={
        Property(name="Documentation23", type=article_EmbeddableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="embeddableElements", type=article_Documentation, multiplicity=Multiplicity(1, 1))
    }
)
callouts9: BinaryAssociation = BinaryAssociation(
    name="callouts9",
    ends={
        Property(name="Callout", type=article_Snippet, multiplicity=Multiplicity(1, 1)),
        Property(name="snippet", type=article_Callout, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formatter10: BinaryAssociation = BinaryAssociation(
    name="formatter10",
    ends={
        Property(name="Formatter", type=article_Snippet, multiplicity=Multiplicity(1, 1)),
        Property(name="snippet11", type=article_Formatter, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
description12: BinaryAssociation = BinaryAssociation(
    name="description12",
    ends={
        Property(name="Description", type=article_Snippet, multiplicity=Multiplicity(1, 1)),
        Property(name="snippet13", type=article_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children15: BinaryAssociation = BinaryAssociation(
    name="children15",
    ends={
        Property(name="StructuralElement", type=article_StructuralElement, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=article_StructuralElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent17: BinaryAssociation = BinaryAssociation(
    name="parent17",
    ends={
        Property(name="StructuralElement18", type=article_StructuralElement, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=article_StructuralElement, multiplicity=Multiplicity(0, 1))
    }
)
documentation19: BinaryAssociation = BinaryAssociation(
    name="documentation19",
    ends={
        Property(name="article_Documentation20", type=article_StructuralElement, multiplicity=Multiplicity(1, 1)),
        Property(name="article_StructuralElement", type=article_Documentation, multiplicity=Multiplicity(1, 1))
    }
)
target28: BinaryAssociation = BinaryAssociation(
    name="target28",
    ends={
        Property(name="article_LinkTarget", type=article_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="article_Link", type=article_LinkTarget, multiplicity=Multiplicity(0, 1))
    }
)
element29: BinaryAssociation = BinaryAssociation(
    name="element29",
    ends={
        Property(name="article_EmbeddableElement", type=article_Embedding, multiplicity=Multiplicity(1, 1)),
        Property(name="article_Embedding", type=article_EmbeddableElement, multiplicity=Multiplicity(1, 1))
    }
)
packages30: BinaryAssociation = BinaryAssociation(
    name="packages30",
    ends={
        Property(name="JavaPackage", type=article_Plugin, multiplicity=Multiplicity(1, 1)),
        Property(name="plugin", type=article_JavaPackage, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
chapter24: BinaryAssociation = BinaryAssociation(
    name="chapter24",
    ends={
        Property(name="Chapter", type=article_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="sections", type=article_Chapter, multiplicity=Multiplicity(1, 1))
    }
)
category25: BinaryAssociation = BinaryAssociation(
    name="category25",
    ends={
        Property(name="article_Category", type=article_Body, multiplicity=Multiplicity(1, 1)),
        Property(name="article_Body", type=article_Category, multiplicity=Multiplicity(0, 1))
    }
)
elements26: BinaryAssociation = BinaryAssociation(
    name="elements26",
    ends={
        Property(name="BodyElement", type=article_BodyElementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="container", type=article_BodyElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
container27: BinaryAssociation = BinaryAssociation(
    name="container27",
    ends={
        Property(name="BodyElementContainer", type=article_BodyElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=article_BodyElementContainer, multiplicity=Multiplicity(1, 1))
    }
)
plugin34: BinaryAssociation = BinaryAssociation(
    name="plugin34",
    ends={
        Property(name="Plugin35", type=article_ExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionPoints", type=article_Plugin, multiplicity=Multiplicity(1, 1))
    }
)
extensionPoints31: BinaryAssociation = BinaryAssociation(
    name="extensionPoints31",
    ends={
        Property(name="ExtensionPoint", type=article_Plugin, multiplicity=Multiplicity(1, 1)),
        Property(name="plugin32", type=article_ExtensionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
plugin33: BinaryAssociation = BinaryAssociation(
    name="plugin33",
    ends={
        Property(name="Plugin", type=article_JavaPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="packages", type=article_Plugin, multiplicity=Multiplicity(1, 1))
    }
)
snippet36: BinaryAssociation = BinaryAssociation(
    name="snippet36",
    ends={
        Property(name="Snippet37", type=article_Formatter, multiplicity=Multiplicity(1, 1)),
        Property(name="formatter", type=article_Snippet, multiplicity=Multiplicity(1, 1))
    }
)
snippet45: BinaryAssociation = BinaryAssociation(
    name="snippet45",
    ends={
        Property(name="Snippet46", type=article_Description, multiplicity=Multiplicity(1, 1)),
        Property(name="description", type=article_Snippet, multiplicity=Multiplicity(1, 1))
    }
)
children39: BinaryAssociation = BinaryAssociation(
    name="children39",
    ends={
        Property(name="article_TreeNode", type=article_TreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="article_TreeNode38", type=article_TreeNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties40: BinaryAssociation = BinaryAssociation(
    name="properties40",
    ends={
        Property(name="article_TreeNodeProperty", type=article_TreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="article_TreeNode41", type=article_TreeNodeProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties43: BinaryAssociation = BinaryAssociation(
    name="properties43",
    ends={
        Property(name="article_TreeNodeProperty44", type=article_TreeNodeProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="article_TreeNodeProperty42", type=article_TreeNodeProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_article_Documentation_StructuralElement = Generalization(general=StructuralElement, specific=article_Documentation)
gen_article_Category_Body = Generalization(general=Body, specific=article_Category)
gen_article_Article_Chapter = Generalization(general=Chapter, specific=article_Article)
gen_article_Chapter_Body = Generalization(general=Body, specific=article_Chapter)
gen_article_LinkTarget_Identifiable = Generalization(general=Identifiable, specific=article_LinkTarget)
gen_article_Callout_BodyElementContainer = Generalization(general=BodyElementContainer, specific=article_Callout)
gen_article_EmbeddableElement_Identifiable = Generalization(general=Identifiable, specific=article_EmbeddableElement)
gen_article_Snippet_EmbeddableElement = Generalization(general=EmbeddableElement, specific=article_Snippet)
gen_article_Diagram_BodyElement = Generalization(general=BodyElement, specific=article_Diagram)
gen_article_Factory_EmbeddableElement = Generalization(general=EmbeddableElement, specific=article_Factory)
gen_article_JavaElement_LinkTarget = Generalization(general=LinkTarget, specific=article_JavaElement)
gen_article_StructuralElement_LinkTarget = Generalization(general=LinkTarget, specific=article_StructuralElement)
gen_article_Link_BodyElement = Generalization(general=BodyElement, specific=article_Link)
gen_article_Embedding_BodyElement = Generalization(general=BodyElement, specific=article_Embedding)
gen_article_SourceCode_ExternalTarget = Generalization(general=ExternalTarget, specific=article_SourceCode)
gen_article_ExternalTarget_LinkTarget = Generalization(general=LinkTarget, specific=article_ExternalTarget)
gen_article_Section_LinkTarget = Generalization(general=LinkTarget, specific=article_Section)
gen_article_Section_BodyElementContainer = Generalization(general=BodyElementContainer, specific=article_Section)
gen_article_Body_StructuralElement = Generalization(general=StructuralElement, specific=article_Body)
gen_article_Body_BodyElementContainer = Generalization(general=BodyElementContainer, specific=article_Body)
gen_article_Text_BodyElement = Generalization(general=BodyElement, specific=article_Text)
gen_article_Schemadoc_Category = Generalization(general=Category, specific=article_Schemadoc)
gen_article_Toc_BodyElement = Generalization(general=BodyElement, specific=article_Toc)
gen_article_Javadoc_Category = Generalization(general=Category, specific=article_Javadoc)
gen_article_ExternalArticle_Article = Generalization(general=Article, specific=article_ExternalArticle)
gen_article_Image_BodyElement = Generalization(general=BodyElement, specific=article_Image)
gen_article_PluginResource_ExternalArticle = Generalization(general=ExternalArticle, specific=article_PluginResource)
gen_article_Excel_BodyElement = Generalization(general=BodyElement, specific=article_Excel)
gen_article_JavaFormatter_Formatter = Generalization(general=Formatter, specific=article_JavaFormatter)
gen_article_XmlFormatter_Formatter = Generalization(general=Formatter, specific=article_XmlFormatter)
gen_article_TreeFormatter_Formatter = Generalization(general=Formatter, specific=article_TreeFormatter)
gen_article_Selection_BodyElement = Generalization(general=BodyElement, specific=article_Selection)
gen_article_ImageFormatter_Formatter = Generalization(general=Formatter, specific=article_ImageFormatter)
gen_article_Description_BodyElementContainer = Generalization(general=BodyElementContainer, specific=article_Description)
gen_article_HtmlFormatter_Formatter = Generalization(general=Formatter, specific=article_HtmlFormatter)
gen_article_ImageFactory_Factory = Generalization(general=Factory, specific=article_ImageFactory)
gen_article_Key_BodyElement = Generalization(general=BodyElement, specific=article_Key)

# Domain Model
domain_model = DomainModel(
    name="article",
    types={article_Plugin, article_Documentation, StructuralElement, article_Context, article_EmbeddableElement, article_Category, Body, article_Article, Chapter, article_Chapter, article_Section, article_LinkTarget, Identifiable, BodyElementContainer, article_Snippet, EmbeddableElement, article_Callout, article_Formatter, article_Description, article_Diagram, BodyElement, article_Factory, article_JavaElement, LinkTarget, article_StructuralElement, article_Link, article_Embedding, article_SourceCode, ExternalTarget, article_JavaPackage, article_ExternalTarget, article_Identifiable, article_Body, article_BodyElementContainer, article_BodyElement, article_Text, article_Schemadoc, article_Toc, article_ExtensionPoint, article_Javadoc, Category, article_ExternalArticle, Article, article_Image, article_TreeNode, article_PluginResource, ExternalArticle, article_Excel, article_JavaFormatter, Formatter, article_XmlFormatter, article_TreeFormatter, article_Selection, article_ImageFormatter, article_HtmlFormatter, article_TreeNodeProperty, article_ImageFactory, Factory, article_Key},
    associations={dependencies3, plugins4, context0, embeddableElements1, article7, documentations6, snippet21, sections8, documentation22, callouts9, formatter10, description12, children15, parent17, documentation19, target28, element29, packages30, chapter24, category25, elements26, container27, plugin34, extensionPoints31, plugin33, snippet36, snippet45, children39, properties40, properties43},
    generalizations={gen_article_Documentation_StructuralElement, gen_article_Category_Body, gen_article_Article_Chapter, gen_article_Chapter_Body, gen_article_LinkTarget_Identifiable, gen_article_Callout_BodyElementContainer, gen_article_EmbeddableElement_Identifiable, gen_article_Snippet_EmbeddableElement, gen_article_Diagram_BodyElement, gen_article_Factory_EmbeddableElement, gen_article_JavaElement_LinkTarget, gen_article_StructuralElement_LinkTarget, gen_article_Link_BodyElement, gen_article_Embedding_BodyElement, gen_article_SourceCode_ExternalTarget, gen_article_ExternalTarget_LinkTarget, gen_article_Section_LinkTarget, gen_article_Section_BodyElementContainer, gen_article_Body_StructuralElement, gen_article_Body_BodyElementContainer, gen_article_Text_BodyElement, gen_article_Schemadoc_Category, gen_article_Toc_BodyElement, gen_article_Javadoc_Category, gen_article_ExternalArticle_Article, gen_article_Image_BodyElement, gen_article_PluginResource_ExternalArticle, gen_article_Excel_BodyElement, gen_article_JavaFormatter_Formatter, gen_article_XmlFormatter_Formatter, gen_article_TreeFormatter_Formatter, gen_article_Selection_BodyElement, gen_article_ImageFormatter_Formatter, gen_article_Description_BodyElementContainer, gen_article_HtmlFormatter_Formatter, gen_article_ImageFactory_Factory, gen_article_Key_BodyElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)