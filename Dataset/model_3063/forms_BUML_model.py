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
AttributeType: Enumeration = Enumeration(
    name="AttributeType",
    literals={
            EnumerationLiteral(name="None"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Text"),
			EnumerationLiteral(name="Date"),
			EnumerationLiteral(name="Year"),
			EnumerationLiteral(name="Time"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="Email")
    }
)

ConditionType: Enumeration = Enumeration(
    name="ConditionType",
    literals={
            EnumerationLiteral(name="Show"),
			EnumerationLiteral(name="Hide"),
			EnumerationLiteral(name="Enable"),
			EnumerationLiteral(name="Disable")
    }
)

CompositeConditionOperator: Enumeration = Enumeration(
    name="CompositeConditionOperator",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
    }
)

# Classes
forms_EntityModel = Class(name="forms::EntityModel")
forms_Entity = Class(name="forms::Entity")
forms_Relationship = Class(name="forms::Relationship")
forms_EnumerationType = Class(name="forms::EnumerationType")
forms_Attribute = Class(name="forms::Attribute")
forms_EnumerationLiteral = Class(name="forms::EnumerationLiteral")
forms_FormModel = Class(name="forms::FormModel")
forms_Form = Class(name="forms::Form")
forms_Page = Class(name="forms::Page")
forms_PageElement = Class(name="forms::PageElement", is_abstract=True)
forms_Condition = Class(name="forms::Condition", is_abstract=True)
forms_AttributePageElement = Class(name="forms::AttributePageElement", is_abstract=True)
PageElement = Class(name="PageElement")
forms_RelationshipPageElement = Class(name="forms::RelationshipPageElement", is_abstract=True)
forms_DateSelectionAttributePageElement = Class(name="forms::DateSelectionAttributePageElement")
forms_TimeSelectionAttributePageElement = Class(name="forms::TimeSelectionAttributePageElement")
forms_ListRelationshipPageElement = Class(name="forms::ListRelationshipPageElement")
RelationshipPageElement = Class(name="RelationshipPageElement")
forms_TableRelationshipPageElement = Class(name="forms::TableRelationshipPageElement")
forms_Column = Class(name="forms::Column")
forms_TextFieldAttributePageElement = Class(name="forms::TextFieldAttributePageElement")
AttributePageElement = Class(name="AttributePageElement")
forms_TextareaAttributePageElement = Class(name="forms::TextareaAttributePageElement")
forms_SelectionAttributePageElement = Class(name="forms::SelectionAttributePageElement")
forms_CompositeCondition = Class(name="forms::CompositeCondition")
forms_AttributeValueCondition = Class(name="forms::AttributeValueCondition")
Condition = Class(name="Condition")

# forms_EntityModel class attributes and methods

# forms_Entity class attributes and methods
forms_Entity_name: Property = Property(name="name", type=StringType)
forms_Entity.attributes={forms_Entity_name}

# forms_Relationship class attributes and methods
forms_Relationship_name: Property = Property(name="name", type=StringType)
forms_Relationship_lowerBound: Property = Property(name="lowerBound", type=StringType)
forms_Relationship_upperBound: Property = Property(name="upperBound", type=StringType)
forms_Relationship.attributes={forms_Relationship_upperBound, forms_Relationship_lowerBound, forms_Relationship_name}

# forms_EnumerationType class attributes and methods
forms_EnumerationType_name: Property = Property(name="name", type=StringType)
forms_EnumerationType.attributes={forms_EnumerationType_name}

# forms_Attribute class attributes and methods
forms_Attribute_name: Property = Property(name="name", type=StringType)
forms_Attribute_mandatory: Property = Property(name="mandatory", type=BooleanType)
forms_Attribute_type: Property = Property(name="type", type=StringType)
forms_Attribute.attributes={forms_Attribute_name, forms_Attribute_mandatory, forms_Attribute_type}

# forms_EnumerationLiteral class attributes and methods
forms_EnumerationLiteral_name: Property = Property(name="name", type=StringType)
forms_EnumerationLiteral_value: Property = Property(name="value", type=StringType)
forms_EnumerationLiteral.attributes={forms_EnumerationLiteral_value, forms_EnumerationLiteral_name}

# forms_FormModel class attributes and methods

# forms_Form class attributes and methods
forms_Form_name: Property = Property(name="name", type=StringType)
forms_Form_title: Property = Property(name="title", type=StringType)
forms_Form_description: Property = Property(name="description", type=StringType)
forms_Form.attributes={forms_Form_description, forms_Form_name, forms_Form_title}

# forms_Page class attributes and methods
forms_Page_title: Property = Property(name="title", type=StringType)
forms_Page.attributes={forms_Page_title}

# forms_PageElement class attributes and methods
forms_PageElement_label: Property = Property(name="label", type=StringType)
forms_PageElement_elementID: Property = Property(name="elementID", type=StringType)
forms_PageElement.attributes={forms_PageElement_label, forms_PageElement_elementID}

# forms_Condition class attributes and methods
forms_Condition_conditionID: Property = Property(name="conditionID", type=StringType)
forms_Condition_type: Property = Property(name="type", type=StringType)
forms_Condition.attributes={forms_Condition_type, forms_Condition_conditionID}

# forms_AttributePageElement class attributes and methods

# PageElement class attributes and methods

# forms_RelationshipPageElement class attributes and methods

# forms_DateSelectionAttributePageElement class attributes and methods

# forms_TimeSelectionAttributePageElement class attributes and methods

# forms_ListRelationshipPageElement class attributes and methods

# RelationshipPageElement class attributes and methods

# forms_TableRelationshipPageElement class attributes and methods

# forms_Column class attributes and methods

# forms_TextFieldAttributePageElement class attributes and methods
forms_TextFieldAttributePageElement_format: Property = Property(name="format", type=StringType)
forms_TextFieldAttributePageElement.attributes={forms_TextFieldAttributePageElement_format}

# AttributePageElement class attributes and methods

# forms_TextareaAttributePageElement class attributes and methods

# forms_SelectionAttributePageElement class attributes and methods

# forms_CompositeCondition class attributes and methods
forms_CompositeCondition_operator: Property = Property(name="operator", type=StringType)
forms_CompositeCondition.attributes={forms_CompositeCondition_operator}

# forms_AttributeValueCondition class attributes and methods
forms_AttributeValueCondition_value: Property = Property(name="value", type=StringType)
forms_AttributeValueCondition.attributes={forms_AttributeValueCondition_value}

# Condition class attributes and methods

# Relationships
superTypes9: BinaryAssociation = BinaryAssociation(
    name="superTypes9",
    ends={
        Property(name="forms_Entity8", type=forms_Entity, multiplicity=Multiplicity(0, 9999)),
        Property(name="forms_Entity10", type=forms_Entity, multiplicity=Multiplicity(1, 1))
    }
)
attributes11: BinaryAssociation = BinaryAssociation(
    name="attributes11",
    ends={
        Property(name="Attribute", type=forms_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entity", type=forms_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationships12: BinaryAssociation = BinaryAssociation(
    name="relationships12",
    ends={
        Property(name="Relationship", type=forms_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=forms_Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entities0: BinaryAssociation = BinaryAssociation(
    name="entities0",
    ends={
        Property(name="forms_Entity", type=forms_EntityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_EntityModel", type=forms_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumerations1: BinaryAssociation = BinaryAssociation(
    name="enumerations1",
    ends={
        Property(name="forms_EnumerationType", type=forms_EntityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_EntityModel2", type=forms_EnumerationType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
id3: BinaryAssociation = BinaryAssociation(
    name="id3",
    ends={
        Property(name="forms_Attribute", type=forms_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Entity4", type=forms_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
superType6: BinaryAssociation = BinaryAssociation(
    name="superType6",
    ends={
        Property(name="forms_Entity7", type=forms_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Entity5", type=forms_Entity, multiplicity=Multiplicity(0, 1))
    }
)
literals17: BinaryAssociation = BinaryAssociation(
    name="literals17",
    ends={
        Property(name="forms_EnumerationLiteral", type=forms_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_EnumerationType18", type=forms_EnumerationLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
enumerationType13: BinaryAssociation = BinaryAssociation(
    name="enumerationType13",
    ends={
        Property(name="forms_EnumerationType15", type=forms_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Attribute14", type=forms_EnumerationType, multiplicity=Multiplicity(0, 1))
    }
)
entity16: BinaryAssociation = BinaryAssociation(
    name="entity16",
    ends={
        Property(name="Entity", type=forms_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=forms_Entity, multiplicity=Multiplicity(0, 1))
    }
)
entityModel26: BinaryAssociation = BinaryAssociation(
    name="entityModel26",
    ends={
        Property(name="forms_EntityModel27", type=forms_FormModel, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_FormModel", type=forms_EntityModel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
forms28: BinaryAssociation = BinaryAssociation(
    name="forms28",
    ends={
        Property(name="forms_Form", type=forms_FormModel, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_FormModel29", type=forms_Form, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
welcomeForm30: BinaryAssociation = BinaryAssociation(
    name="welcomeForm30",
    ends={
        Property(name="forms_Form32", type=forms_FormModel, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_FormModel31", type=forms_Form, multiplicity=Multiplicity(1, 1))
    }
)
entity33: BinaryAssociation = BinaryAssociation(
    name="entity33",
    ends={
        Property(name="forms_Entity35", type=forms_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Form34", type=forms_Entity, multiplicity=Multiplicity(1, 1))
    }
)
pages36: BinaryAssociation = BinaryAssociation(
    name="pages36",
    ends={
        Property(name="Page", type=forms_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="form", type=forms_Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pageElements37: BinaryAssociation = BinaryAssociation(
    name="pageElements37",
    ends={
        Property(name="PageElement", type=forms_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page", type=forms_PageElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditions38: BinaryAssociation = BinaryAssociation(
    name="conditions38",
    ends={
        Property(name="Condition", type=forms_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="page39", type=forms_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source19: BinaryAssociation = BinaryAssociation(
    name="source19",
    ends={
        Property(name="Entity20", type=forms_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="relationships", type=forms_Entity, multiplicity=Multiplicity(0, 1))
    }
)
target21: BinaryAssociation = BinaryAssociation(
    name="target21",
    ends={
        Property(name="forms_Entity22", type=forms_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Relationship", type=forms_Entity, multiplicity=Multiplicity(1, 1))
    }
)
opposite24: BinaryAssociation = BinaryAssociation(
    name="opposite24",
    ends={
        Property(name="forms_Relationship25", type=forms_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Relationship23", type=forms_Relationship, multiplicity=Multiplicity(0, 1))
    }
)
attribute45: BinaryAssociation = BinaryAssociation(
    name="attribute45",
    ends={
        Property(name="forms_Attribute46", type=forms_AttributePageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_AttributePageElement", type=forms_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
form40: BinaryAssociation = BinaryAssociation(
    name="form40",
    ends={
        Property(name="Form", type=forms_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="pages", type=forms_Form, multiplicity=Multiplicity(0, 1))
    }
)
conditions41: BinaryAssociation = BinaryAssociation(
    name="conditions41",
    ends={
        Property(name="Condition42", type=forms_PageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="pageElement", type=forms_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
page43: BinaryAssociation = BinaryAssociation(
    name="page43",
    ends={
        Property(name="Page44", type=forms_PageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="pageElements", type=forms_Page, multiplicity=Multiplicity(0, 1))
    }
)
columns52: BinaryAssociation = BinaryAssociation(
    name="columns52",
    ends={
        Property(name="Column", type=forms_TableRelationshipPageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=forms_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
relationship47: BinaryAssociation = BinaryAssociation(
    name="relationship47",
    ends={
        Property(name="forms_Relationship48", type=forms_RelationshipPageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_RelationshipPageElement", type=forms_Relationship, multiplicity=Multiplicity(1, 1))
    }
)
editingForm49: BinaryAssociation = BinaryAssociation(
    name="editingForm49",
    ends={
        Property(name="forms_Form51", type=forms_RelationshipPageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_RelationshipPageElement50", type=forms_Form, multiplicity=Multiplicity(1, 1))
    }
)
page56: BinaryAssociation = BinaryAssociation(
    name="page56",
    ends={
        Property(name="Page57", type=forms_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="conditions", type=forms_Page, multiplicity=Multiplicity(0, 1))
    }
)
pageElement58: BinaryAssociation = BinaryAssociation(
    name="pageElement58",
    ends={
        Property(name="PageElement60", type=forms_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="conditions59", type=forms_PageElement, multiplicity=Multiplicity(0, 1))
    }
)
parentCondtion61: BinaryAssociation = BinaryAssociation(
    name="parentCondtion61",
    ends={
        Property(name="CompositeCondition", type=forms_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="conditions62", type=forms_CompositeCondition, multiplicity=Multiplicity(0, 1))
    }
)
attribute53: BinaryAssociation = BinaryAssociation(
    name="attribute53",
    ends={
        Property(name="forms_Attribute54", type=forms_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Column", type=forms_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
table55: BinaryAssociation = BinaryAssociation(
    name="table55",
    ends={
        Property(name="TableRelationshipPageElement", type=forms_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=forms_TableRelationshipPageElement, multiplicity=Multiplicity(0, 1))
    }
)
trigger63: BinaryAssociation = BinaryAssociation(
    name="trigger63",
    ends={
        Property(name="forms_AttributePageElement64", type=forms_AttributeValueCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_AttributeValueCondition", type=forms_AttributePageElement, multiplicity=Multiplicity(1, 1))
    }
)
conditions65: BinaryAssociation = BinaryAssociation(
    name="conditions65",
    ends={
        Property(name="Condition66", type=forms_CompositeCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="parentCondtion", type=forms_Condition, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)

# Generalizations
gen_forms_AttributePageElement_PageElement = Generalization(general=PageElement, specific=forms_AttributePageElement)
gen_forms_RelationshipPageElement_PageElement = Generalization(general=PageElement, specific=forms_RelationshipPageElement)
gen_forms_SelectionAttributePageElement_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_SelectionAttributePageElement)
gen_forms_DateSelectionAttributePageElement_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_DateSelectionAttributePageElement)
gen_forms_TimeSelectionAttributePageElement_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_TimeSelectionAttributePageElement)
gen_forms_ListRelationshipPageElement_RelationshipPageElement = Generalization(general=RelationshipPageElement, specific=forms_ListRelationshipPageElement)
gen_forms_TableRelationshipPageElement_RelationshipPageElement = Generalization(general=RelationshipPageElement, specific=forms_TableRelationshipPageElement)
gen_forms_TextFieldAttributePageElement_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_TextFieldAttributePageElement)
gen_forms_TextareaAttributePageElement_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_TextareaAttributePageElement)
gen_forms_AttributeValueCondition_Condition = Generalization(general=Condition, specific=forms_AttributeValueCondition)
gen_forms_CompositeCondition_Condition = Generalization(general=Condition, specific=forms_CompositeCondition)

# Domain Model
domain_model = DomainModel(
    name="forms",
    types={forms_EntityModel, forms_Entity, forms_Relationship, forms_EnumerationType, forms_Attribute, forms_EnumerationLiteral, forms_FormModel, forms_Form, forms_Page, forms_PageElement, forms_Condition, forms_AttributePageElement, PageElement, forms_RelationshipPageElement, forms_DateSelectionAttributePageElement, forms_TimeSelectionAttributePageElement, forms_ListRelationshipPageElement, RelationshipPageElement, forms_TableRelationshipPageElement, forms_Column, forms_TextFieldAttributePageElement, AttributePageElement, forms_TextareaAttributePageElement, forms_SelectionAttributePageElement, forms_CompositeCondition, forms_AttributeValueCondition, Condition, AttributeType, ConditionType, CompositeConditionOperator},
    associations={superTypes9, attributes11, relationships12, entities0, enumerations1, id3, superType6, literals17, enumerationType13, entity16, entityModel26, forms28, welcomeForm30, entity33, pages36, pageElements37, conditions38, source19, target21, opposite24, attribute45, form40, conditions41, page43, columns52, relationship47, editingForm49, page56, pageElement58, parentCondtion61, attribute53, table55, trigger63, conditions65},
    generalizations={gen_forms_AttributePageElement_PageElement, gen_forms_RelationshipPageElement_PageElement, gen_forms_SelectionAttributePageElement_AttributePageElement, gen_forms_DateSelectionAttributePageElement_AttributePageElement, gen_forms_TimeSelectionAttributePageElement_AttributePageElement, gen_forms_ListRelationshipPageElement_RelationshipPageElement, gen_forms_TableRelationshipPageElement_RelationshipPageElement, gen_forms_TextFieldAttributePageElement_AttributePageElement, gen_forms_TextareaAttributePageElement_AttributePageElement, gen_forms_AttributeValueCondition_Condition, gen_forms_CompositeCondition_Condition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)