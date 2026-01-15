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
ColumnType: Enumeration = Enumeration(
    name="ColumnType",
    literals={
            EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Float"),
			EnumerationLiteral(name="Text")
    }
)

FieldType: Enumeration = Enumeration(
    name="FieldType",
    literals={
            EnumerationLiteral(name="TextBox"),
			EnumerationLiteral(name="CheckBox"),
			EnumerationLiteral(name="RadioButton"),
			EnumerationLiteral(name="SubmitButton")
    }
)

# Classes
webApplication_data_DataSource = Class(name="webApplication::data::DataSource")
webApplication_Named = Class(name="webApplication::Named")
webApplication_WebApplicationModel = Class(name="webApplication::WebApplicationModel")
Named = Class(name="Named")
Entity = Class(name="Entity")
DataSource = Class(name="DataSource")
Page = Class(name="Page")
Content = Class(name="Content")
Link = Class(name="Link")
Form = Class(name="Form")
webApplication_data_Entity = Class(name="webApplication::data::Entity")
Column = Class(name="Column")
RelatedEntity = Class(name="RelatedEntity")
webApplication_data_Column = Class(name="webApplication::data::Column")
webApplication_data_RelatedEntity = Class(name="webApplication::data::RelatedEntity")
webApplication_content_Page = Class(name="webApplication::content::Page")
webApplication_content_Content = Class(name="webApplication::content::Content", is_abstract=True)
webApplication_content_Form = Class(name="webApplication::content::Form")
webApplication_content_Link = Class(name="webApplication::content::Link")
webApplication_content_Menu = Class(name="webApplication::content::Menu")
webApplication_content_SingleContent = Class(name="webApplication::content::SingleContent")
webApplication_content_MultipleContent = Class(name="webApplication::content::MultipleContent")
webApplication_content_CRUDForm = Class(name="webApplication::content::CRUDForm")
Field = Class(name="Field")
webApplication_content_Field = Class(name="webApplication::content::Field")

# webApplication_data_DataSource class attributes and methods

# webApplication_Named class attributes and methods
webApplication_Named_name: Property = Property(name="name", type=StringType)
webApplication_Named.attributes={webApplication_Named_name}

# webApplication_WebApplicationModel class attributes and methods

# Named class attributes and methods

# Entity class attributes and methods

# DataSource class attributes and methods

# Page class attributes and methods

# Content class attributes and methods

# Link class attributes and methods

# Form class attributes and methods

# webApplication_data_Entity class attributes and methods
webApplication_data_Entity_numberOfColumns: Property = Property(name="numberOfColumns", type=StringType)
webApplication_data_Entity_m_getPK: Method = Method(name="getPK", parameters={}, type=StringType)
webApplication_data_Entity_m_getPKRelated: Method = Method(name="getPKRelated", parameters={}, type=StringType)
webApplication_data_Entity.attributes={webApplication_data_Entity_numberOfColumns}
webApplication_data_Entity.methods={webApplication_data_Entity_m_getPKRelated, webApplication_data_Entity_m_getPK}

# Column class attributes and methods

# RelatedEntity class attributes and methods

# webApplication_data_Column class attributes and methods
webApplication_data_Column_type: Property = Property(name="type", type=StringType)
webApplication_data_Column_lenght: Property = Property(name="lenght", type=IntegerType)
webApplication_data_Column_PK: Property = Property(name="PK", type=BooleanType)
webApplication_data_Column.attributes={webApplication_data_Column_PK, webApplication_data_Column_type, webApplication_data_Column_lenght}

# webApplication_data_RelatedEntity class attributes and methods

# webApplication_content_Page class attributes and methods

# webApplication_content_Content class attributes and methods

# webApplication_content_Form class attributes and methods

# webApplication_content_Link class attributes and methods

# webApplication_content_Menu class attributes and methods
webApplication_content_Menu_itemName: Property = Property(name="itemName", type=StringType)
webApplication_content_Menu_url: Property = Property(name="url", type=StringType)
webApplication_content_Menu_order: Property = Property(name="order", type=IntegerType)
webApplication_content_Menu.attributes={webApplication_content_Menu_itemName, webApplication_content_Menu_order, webApplication_content_Menu_url}

# webApplication_content_SingleContent class attributes and methods

# webApplication_content_MultipleContent class attributes and methods
webApplication_content_MultipleContent_paginated: Property = Property(name="paginated", type=BooleanType)
webApplication_content_MultipleContent_size: Property = Property(name="size", type=IntegerType)
webApplication_content_MultipleContent.attributes={webApplication_content_MultipleContent_paginated, webApplication_content_MultipleContent_size}

# webApplication_content_CRUDForm class attributes and methods

# Field class attributes and methods

# webApplication_content_Field class attributes and methods
webApplication_content_Field_type: Property = Property(name="type", type=StringType)
webApplication_content_Field.attributes={webApplication_content_Field_type}

# Relationships
entities0: BinaryAssociation = BinaryAssociation(
    name="entities0",
    ends={
        Property(name="Entity", type=webApplication_WebApplicationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="webApplication_WebApplicationModel", type=Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataSources1: BinaryAssociation = BinaryAssociation(
    name="dataSources1",
    ends={
        Property(name="DataSource", type=webApplication_WebApplicationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="webApplication_WebApplicationModel2", type=DataSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pages3: BinaryAssociation = BinaryAssociation(
    name="pages3",
    ends={
        Property(name="Page", type=webApplication_WebApplicationModel, multiplicity=Multiplicity(1, 1)),
        Property(name="webApplication_WebApplicationModel4", type=Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents15: BinaryAssociation = BinaryAssociation(
    name="contents15",
    ends={
        Property(name="Content", type=webApplication_content_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="webApplication_content_Page", type=Content, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
links16: BinaryAssociation = BinaryAssociation(
    name="links16",
    ends={
        Property(name="Link", type=webApplication_content_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="webApplication_content_Page17", type=Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forms18: BinaryAssociation = BinaryAssociation(
    name="forms18",
    ends={
        Property(name="Form", type=webApplication_content_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="webApplication_content_Page19", type=Form, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity5: BinaryAssociation = BinaryAssociation(
    name="entity5",
    ends={
        Property(name="Entity6", type=webApplication_data_DataSource, multiplicity=Multiplicity(1, 1)),
        Property(name="webApplication_data_DataSource", type=Entity, multiplicity=Multiplicity(1, 1))
    }
)
columns7: BinaryAssociation = BinaryAssociation(
    name="columns7",
    ends={
        Property(name="Column", type=webApplication_data_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="webApplication_data_Entity", type=Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
relates8: BinaryAssociation = BinaryAssociation(
    name="relates8",
    ends={
        Property(name="RelatedEntity", type=webApplication_data_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="webApplication_data_Entity9", type=RelatedEntity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatedEntities10: BinaryAssociation = BinaryAssociation(
    name="relatedEntities10",
    ends={
        Property(name="Entity12", type=webApplication_data_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="webApplication_data_Entity11", type=Entity, multiplicity=Multiplicity(0, 9999))
    }
)
relatesTo13: BinaryAssociation = BinaryAssociation(
    name="relatesTo13",
    ends={
        Property(name="Entity14", type=webApplication_data_RelatedEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="webApplication_data_RelatedEntity", type=Entity, multiplicity=Multiplicity(1, 1))
    }
)
dataSource20: BinaryAssociation = BinaryAssociation(
    name="dataSource20",
    ends={
        Property(name="DataSource21", type=webApplication_content_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="webApplication_content_Content", type=DataSource, multiplicity=Multiplicity(1, 1))
    }
)
from22: BinaryAssociation = BinaryAssociation(
    name="from22",
    ends={
        Property(name="Page23", type=webApplication_content_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="webApplication_content_Link", type=Page, multiplicity=Multiplicity(1, 1))
    }
)
to24: BinaryAssociation = BinaryAssociation(
    name="to24",
    ends={
        Property(name="Page26", type=webApplication_content_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="webApplication_content_Link25", type=Page, multiplicity=Multiplicity(1, 1))
    }
)
fields27: BinaryAssociation = BinaryAssociation(
    name="fields27",
    ends={
        Property(name="Field", type=webApplication_content_CRUDForm, multiplicity=Multiplicity(1, 1)),
        Property(name="webApplication_content_CRUDForm", type=Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_webApplication_data_DataSource_Named = Generalization(general=Named, specific=webApplication_data_DataSource)
gen_webApplication_WebApplicationModel_Named = Generalization(general=Named, specific=webApplication_WebApplicationModel)
gen_webApplication_data_Entity_Named = Generalization(general=Named, specific=webApplication_data_Entity)
gen_webApplication_data_Column_Named = Generalization(general=Named, specific=webApplication_data_Column)
gen_webApplication_data_RelatedEntity_Named = Generalization(general=Named, specific=webApplication_data_RelatedEntity)
gen_webApplication_content_Page_Named = Generalization(general=Named, specific=webApplication_content_Page)
gen_webApplication_content_Content_Named = Generalization(general=Named, specific=webApplication_content_Content)
gen_webApplication_content_Form_Named = Generalization(general=Named, specific=webApplication_content_Form)
gen_webApplication_content_Link_Named = Generalization(general=Named, specific=webApplication_content_Link)
gen_webApplication_content_Menu_Content = Generalization(general=Content, specific=webApplication_content_Menu)
gen_webApplication_content_SingleContent_Content = Generalization(general=Content, specific=webApplication_content_SingleContent)
gen_webApplication_content_MultipleContent_Content = Generalization(general=Content, specific=webApplication_content_MultipleContent)
gen_webApplication_content_CRUDForm_Form = Generalization(general=Form, specific=webApplication_content_CRUDForm)
gen_webApplication_content_Field_Named = Generalization(general=Named, specific=webApplication_content_Field)

# Domain Model
domain_model = DomainModel(
    name="webApplication",
    types={webApplication_data_DataSource, webApplication_Named, webApplication_WebApplicationModel, Named, Entity, DataSource, Page, Content, Link, Form, webApplication_data_Entity, Column, RelatedEntity, webApplication_data_Column, webApplication_data_RelatedEntity, webApplication_content_Page, webApplication_content_Content, webApplication_content_Form, webApplication_content_Link, webApplication_content_Menu, webApplication_content_SingleContent, webApplication_content_MultipleContent, webApplication_content_CRUDForm, Field, webApplication_content_Field, ColumnType, FieldType},
    associations={entities0, dataSources1, pages3, contents15, links16, forms18, entity5, columns7, relates8, relatedEntities10, relatesTo13, dataSource20, from22, to24, fields27},
    generalizations={gen_webApplication_data_DataSource_Named, gen_webApplication_WebApplicationModel_Named, gen_webApplication_data_Entity_Named, gen_webApplication_data_Column_Named, gen_webApplication_data_RelatedEntity_Named, gen_webApplication_content_Page_Named, gen_webApplication_content_Content_Named, gen_webApplication_content_Form_Named, gen_webApplication_content_Link_Named, gen_webApplication_content_Menu_Content, gen_webApplication_content_SingleContent_Content, gen_webApplication_content_MultipleContent_Content, gen_webApplication_content_CRUDForm_Form, gen_webApplication_content_Field_Named},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)