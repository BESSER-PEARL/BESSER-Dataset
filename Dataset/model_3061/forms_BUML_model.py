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
            EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Text"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Date"),
			EnumerationLiteral(name="Time"),
			EnumerationLiteral(name="Email"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="None")
    }
)

conditionType: Enumeration = Enumeration(
    name="conditionType",
    literals={
            EnumerationLiteral(name="Hide"),
			EnumerationLiteral(name="Show"),
			EnumerationLiteral(name="Enable"),
			EnumerationLiteral(name="Disable")
    }
)

# Classes
forms_Attribute = Class(name="forms::Attribute")
forms_Relationship = Class(name="forms::Relationship")
forms_Entity = Class(name="forms::Entity")
forms_Enumeration = Class(name="forms::Enumeration")
forms_Literal = Class(name="forms::Literal")
forms_RelationshipPageElement = Class(name="forms::RelationshipPageElement", is_abstract=True)
forms_TextArea = Class(name="forms::TextArea")
AttributePageElement = Class(name="AttributePageElement")
forms_SelectionField = Class(name="forms::SelectionField")
forms_Form = Class(name="forms::Form")
forms_Page = Class(name="forms::Page")
forms_PageElement = Class(name="forms::PageElement", is_abstract=True)
forms_AttributePageElement = Class(name="forms::AttributePageElement", is_abstract=True)
PageElement = Class(name="PageElement")
forms_CompositionCondition = Class(name="forms::CompositionCondition")
Condition = Class(name="Condition")
forms_AttributeValueCondition = Class(name="forms::AttributeValueCondition")
forms_DateSelectionField = Class(name="forms::DateSelectionField")
forms_TimeSelectionField = Class(name="forms::TimeSelectionField")
forms_TextField = Class(name="forms::TextField")
forms_List = Class(name="forms::List")
RelationshipPageElement = Class(name="RelationshipPageElement")
forms_Table = Class(name="forms::Table")
forms_Column = Class(name="forms::Column")
forms_Condition = Class(name="forms::Condition", is_abstract=True)
forms_EMFL_EntityModel = Class(name="forms::EMFL::EntityModel")
forms_EMFL_FormModel = Class(name="forms::EMFL::FormModel")

# forms_Attribute class attributes and methods
forms_Attribute_name: Property = Property(name="name", type=StringType)
forms_Attribute_mandatory: Property = Property(name="mandatory", type=BooleanType)
forms_Attribute_type: Property = Property(name="type", type=StringType)
forms_Attribute.attributes={forms_Attribute_mandatory, forms_Attribute_name, forms_Attribute_type}

# forms_Relationship class attributes and methods
forms_Relationship_name: Property = Property(name="name", type=StringType)
forms_Relationship_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
forms_Relationship_upperBound: Property = Property(name="upperBound", type=IntegerType)
forms_Relationship.attributes={forms_Relationship_name, forms_Relationship_lowerBound, forms_Relationship_upperBound}

# forms_Entity class attributes and methods
forms_Entity_name: Property = Property(name="name", type=StringType)
forms_Entity.attributes={forms_Entity_name}

# forms_Enumeration class attributes and methods
forms_Enumeration_name: Property = Property(name="name", type=StringType)
forms_Enumeration.attributes={forms_Enumeration_name}

# forms_Literal class attributes and methods
forms_Literal_name: Property = Property(name="name", type=StringType)
forms_Literal_Value: Property = Property(name="Value", type=StringType)
forms_Literal.attributes={forms_Literal_Value, forms_Literal_name}

# forms_RelationshipPageElement class attributes and methods

# forms_TextArea class attributes and methods

# AttributePageElement class attributes and methods

# forms_SelectionField class attributes and methods

# forms_Form class attributes and methods
forms_Form_title: Property = Property(name="title", type=StringType)
forms_Form_description: Property = Property(name="description", type=StringType)
forms_Form_isWelcomeForm: Property = Property(name="isWelcomeForm", type=BooleanType)
forms_Form_name: Property = Property(name="name", type=StringType)
forms_Form.attributes={forms_Form_description, forms_Form_title, forms_Form_name, forms_Form_isWelcomeForm}

# forms_Page class attributes and methods
forms_Page_title: Property = Property(name="title", type=StringType)
forms_Page.attributes={forms_Page_title}

# forms_PageElement class attributes and methods
forms_PageElement_elementID: Property = Property(name="elementID", type=IntegerType)
forms_PageElement_label: Property = Property(name="label", type=StringType)
forms_PageElement.attributes={forms_PageElement_label, forms_PageElement_elementID}

# forms_AttributePageElement class attributes and methods

# PageElement class attributes and methods

# forms_CompositionCondition class attributes and methods
forms_CompositionCondition_isAnd: Property = Property(name="isAnd", type=BooleanType)
forms_CompositionCondition.attributes={forms_CompositionCondition_isAnd}

# Condition class attributes and methods

# forms_AttributeValueCondition class attributes and methods
forms_AttributeValueCondition_type: Property = Property(name="type", type=StringType)
forms_AttributeValueCondition_value: Property = Property(name="value", type=StringType)
forms_AttributeValueCondition.attributes={forms_AttributeValueCondition_type, forms_AttributeValueCondition_value}

# forms_DateSelectionField class attributes and methods

# forms_TimeSelectionField class attributes and methods

# forms_TextField class attributes and methods
forms_TextField_format: Property = Property(name="format", type=StringType)
forms_TextField.attributes={forms_TextField_format}

# forms_List class attributes and methods

# RelationshipPageElement class attributes and methods

# forms_Table class attributes and methods

# forms_Column class attributes and methods

# forms_Condition class attributes and methods
forms_Condition_conditionId: Property = Property(name="conditionId", type=IntegerType)
forms_Condition.attributes={forms_Condition_conditionId}

# forms_EMFL_EntityModel class attributes and methods

# forms_EMFL_FormModel class attributes and methods

# Relationships
attributes0: BinaryAssociation = BinaryAssociation(
    name="attributes0",
    ends={
        Property(name="forms_Attribute", type=forms_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Entity", type=forms_Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
identifier1: BinaryAssociation = BinaryAssociation(
    name="identifier1",
    ends={
        Property(name="forms_Attribute3", type=forms_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Entity2", type=forms_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
target13: BinaryAssociation = BinaryAssociation(
    name="target13",
    ends={
        Property(name="forms_Entity15", type=forms_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Relationship14", type=forms_Entity, multiplicity=Multiplicity(1, 1))
    }
)
opposite17: BinaryAssociation = BinaryAssociation(
    name="opposite17",
    ends={
        Property(name="forms_Relationship18", type=forms_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Relationship16", type=forms_Relationship, multiplicity=Multiplicity(0, 1))
    }
)
relationships4: BinaryAssociation = BinaryAssociation(
    name="relationships4",
    ends={
        Property(name="forms_Relationship", type=forms_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Entity5", type=forms_Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supertypes7: BinaryAssociation = BinaryAssociation(
    name="supertypes7",
    ends={
        Property(name="forms_Entity8", type=forms_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Entity6", type=forms_Entity, multiplicity=Multiplicity(0, 1))
    }
)
enumerationType9: BinaryAssociation = BinaryAssociation(
    name="enumerationType9",
    ends={
        Property(name="forms_Enumeration", type=forms_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Attribute10", type=forms_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
consists11: BinaryAssociation = BinaryAssociation(
    name="consists11",
    ends={
        Property(name="forms_Literal", type=forms_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Enumeration12", type=forms_Literal, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
editing_form27: BinaryAssociation = BinaryAssociation(
    name="editing_form27",
    ends={
        Property(name="forms_Form28", type=forms_RelationshipPageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_RelationshipPageElement", type=forms_Form, multiplicity=Multiplicity(1, 1))
    }
)
refers_to29: BinaryAssociation = BinaryAssociation(
    name="refers_to29",
    ends={
        Property(name="forms_Relationship31", type=forms_RelationshipPageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_RelationshipPageElement30", type=forms_Relationship, multiplicity=Multiplicity(1, 1))
    }
)
consists19: BinaryAssociation = BinaryAssociation(
    name="consists19",
    ends={
        Property(name="forms_Page", type=forms_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Form", type=forms_Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associated_with20: BinaryAssociation = BinaryAssociation(
    name="associated_with20",
    ends={
        Property(name="forms_Entity22", type=forms_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Form21", type=forms_Entity, multiplicity=Multiplicity(1, 1))
    }
)
contains23: BinaryAssociation = BinaryAssociation(
    name="contains23",
    ends={
        Property(name="forms_PageElement", type=forms_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Page24", type=forms_PageElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refers_to25: BinaryAssociation = BinaryAssociation(
    name="refers_to25",
    ends={
        Property(name="forms_Attribute26", type=forms_AttributePageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_AttributePageElement", type=forms_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
combinesAttributeValue36: BinaryAssociation = BinaryAssociation(
    name="combinesAttributeValue36",
    ends={
        Property(name="forms_AttributeValueCondition", type=forms_CompositionCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_CompositionCondition", type=forms_AttributeValueCondition, multiplicity=Multiplicity(0, 2))
    }
)
consists32: BinaryAssociation = BinaryAssociation(
    name="consists32",
    ends={
        Property(name="forms_Column", type=forms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Table", type=forms_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refers_to33: BinaryAssociation = BinaryAssociation(
    name="refers_to33",
    ends={
        Property(name="forms_Attribute35", type=forms_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Column34", type=forms_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
conditions51: BinaryAssociation = BinaryAssociation(
    name="conditions51",
    ends={
        Property(name="forms_Condition", type=forms_EMFL_FormModel, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_EMFL_FormModel52", type=forms_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entities53: BinaryAssociation = BinaryAssociation(
    name="entities53",
    ends={
        Property(name="forms_Entity55", type=forms_EMFL_FormModel, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_EMFL_FormModel54", type=forms_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entities56: BinaryAssociation = BinaryAssociation(
    name="entities56",
    ends={
        Property(name="forms_Entity57", type=forms_EMFL_EntityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_EMFL_EntityModel", type=forms_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enums58: BinaryAssociation = BinaryAssociation(
    name="enums58",
    ends={
        Property(name="forms_Enumeration60", type=forms_EMFL_EntityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_EMFL_EntityModel59", type=forms_Enumeration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
combinesComposite38: BinaryAssociation = BinaryAssociation(
    name="combinesComposite38",
    ends={
        Property(name="forms_CompositionCondition39", type=forms_CompositionCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_CompositionCondition37", type=forms_CompositionCondition, multiplicity=Multiplicity(0, 2))
    }
)
conditionsPage40: BinaryAssociation = BinaryAssociation(
    name="conditionsPage40",
    ends={
        Property(name="forms_Page42", type=forms_AttributeValueCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_AttributeValueCondition41", type=forms_Page, multiplicity=Multiplicity(0, 1))
    }
)
conditionsPageElement43: BinaryAssociation = BinaryAssociation(
    name="conditionsPageElement43",
    ends={
        Property(name="forms_PageElement45", type=forms_AttributeValueCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_AttributeValueCondition44", type=forms_PageElement, multiplicity=Multiplicity(0, 1))
    }
)
attributePageElement46: BinaryAssociation = BinaryAssociation(
    name="attributePageElement46",
    ends={
        Property(name="forms_PageElement48", type=forms_AttributeValueCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_AttributeValueCondition47", type=forms_PageElement, multiplicity=Multiplicity(0, 1))
    }
)
forms49: BinaryAssociation = BinaryAssociation(
    name="forms49",
    ends={
        Property(name="forms_Form50", type=forms_EMFL_FormModel, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_EMFL_FormModel", type=forms_Form, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_forms_RelationshipPageElement_PageElement = Generalization(general=PageElement, specific=forms_RelationshipPageElement)
gen_forms_TextArea_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_TextArea)
gen_forms_SelectionField_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_SelectionField)
gen_forms_AttributePageElement_PageElement = Generalization(general=PageElement, specific=forms_AttributePageElement)
gen_forms_CompositionCondition_Condition = Generalization(general=Condition, specific=forms_CompositionCondition)
gen_forms_DateSelectionField_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_DateSelectionField)
gen_forms_TimeSelectionField_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_TimeSelectionField)
gen_forms_TextField_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_TextField)
gen_forms_List_RelationshipPageElement = Generalization(general=RelationshipPageElement, specific=forms_List)
gen_forms_Table_RelationshipPageElement = Generalization(general=RelationshipPageElement, specific=forms_Table)
gen_forms_AttributeValueCondition_Condition = Generalization(general=Condition, specific=forms_AttributeValueCondition)

# Domain Model
domain_model = DomainModel(
    name="forms",
    types={forms_Attribute, forms_Relationship, forms_Entity, forms_Enumeration, forms_Literal, forms_RelationshipPageElement, forms_TextArea, AttributePageElement, forms_SelectionField, forms_Form, forms_Page, forms_PageElement, forms_AttributePageElement, PageElement, forms_CompositionCondition, Condition, forms_AttributeValueCondition, forms_DateSelectionField, forms_TimeSelectionField, forms_TextField, forms_List, RelationshipPageElement, forms_Table, forms_Column, forms_Condition, forms_EMFL_EntityModel, forms_EMFL_FormModel, AttributeType, conditionType},
    associations={attributes0, identifier1, target13, opposite17, relationships4, supertypes7, enumerationType9, consists11, editing_form27, refers_to29, consists19, associated_with20, contains23, refers_to25, combinesAttributeValue36, consists32, refers_to33, conditions51, entities53, entities56, enums58, combinesComposite38, conditionsPage40, conditionsPageElement43, attributePageElement46, forms49},
    generalizations={gen_forms_RelationshipPageElement_PageElement, gen_forms_TextArea_AttributePageElement, gen_forms_SelectionField_AttributePageElement, gen_forms_AttributePageElement_PageElement, gen_forms_CompositionCondition_Condition, gen_forms_DateSelectionField_AttributePageElement, gen_forms_TimeSelectionField_AttributePageElement, gen_forms_TextField_AttributePageElement, gen_forms_List_RelationshipPageElement, gen_forms_Table_RelationshipPageElement, gen_forms_AttributeValueCondition_Condition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)