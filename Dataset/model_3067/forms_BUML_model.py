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
			EnumerationLiteral(name="Year"),
			EnumerationLiteral(name="Email"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="None")
    }
)

ConditionType: Enumeration = Enumeration(
    name="ConditionType",
    literals={
            EnumerationLiteral(name="Hide"),
			EnumerationLiteral(name="Show"),
			EnumerationLiteral(name="Enable"),
			EnumerationLiteral(name="Disable")
    }
)

BooleanOperators: Enumeration = Enumeration(
    name="BooleanOperators",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
    }
)

# Classes
Entity = Class(name="Entity")
Enumeration_ = Class(name="Enumeration")
Form = Class(name="Form")
forms_EFML_model = Class(name="forms::EFML::model")
Attribute = Class(name="Attribute")
Relationship = Class(name="Relationship")
forms_entityModeling_Attribute = Class(name="forms::entityModeling::Attribute")
forms_entityModeling_Entity = Class(name="forms::entityModeling::Entity")
forms_entityModeling_Enumeration = Class(name="forms::entityModeling::Enumeration")
Literal = Class(name="Literal")
forms_entityModeling_Relationship = Class(name="forms::entityModeling::Relationship")
forms_entityModeling_Literal = Class(name="forms::entityModeling::Literal")
Page = Class(name="Page")
forms_entityModeling_Page = Class(name="forms::entityModeling::Page")
PageElement = Class(name="PageElement")
Condition = Class(name="Condition")
forms_entityModeling_Form = Class(name="forms::entityModeling::Form")
forms_entityModeling_AttributePageElement = Class(name="forms::entityModeling::AttributePageElement", is_abstract=True)
forms_entityModeling_RelationshipPageElement = Class(name="forms::entityModeling::RelationshipPageElement", is_abstract=True)
forms_entityModeling_PageElement = Class(name="forms::entityModeling::PageElement", is_abstract=True)
forms_entityModeling_Textfield = Class(name="forms::entityModeling::Textfield")
AttributePageElement = Class(name="AttributePageElement")
forms_entityModeling_Textarea = Class(name="forms::entityModeling::Textarea")
forms_entityModeling_SelectionField = Class(name="forms::entityModeling::SelectionField")
forms_entityModeling_DateSelectionField = Class(name="forms::entityModeling::DateSelectionField")
forms_entityModeling_TimeSelectionField = Class(name="forms::entityModeling::TimeSelectionField")
forms_entityModeling_List = Class(name="forms::entityModeling::List")
RelationshipPageElement = Class(name="RelationshipPageElement")
forms_entityModeling_Table = Class(name="forms::entityModeling::Table")
Column = Class(name="Column")
forms_entityModeling_Column = Class(name="forms::entityModeling::Column")
forms_entityModeling_Condition = Class(name="forms::entityModeling::Condition", is_abstract=True)
forms_entityModeling_CompositeCondition = Class(name="forms::entityModeling::CompositeCondition")
forms_entityModeling_AttributeValueCondition = Class(name="forms::entityModeling::AttributeValueCondition")

# Entity class attributes and methods

# Enumeration class attributes and methods

# Form class attributes and methods

# forms_EFML_model class attributes and methods

# Attribute class attributes and methods

# Relationship class attributes and methods

# forms_entityModeling_Attribute class attributes and methods
forms_entityModeling_Attribute_mandatory: Property = Property(name="mandatory", type=BooleanType)
forms_entityModeling_Attribute_type: Property = Property(name="type", type=StringType)
forms_entityModeling_Attribute_name: Property = Property(name="name", type=StringType)
forms_entityModeling_Attribute.attributes={forms_entityModeling_Attribute_name, forms_entityModeling_Attribute_type, forms_entityModeling_Attribute_mandatory}

# forms_entityModeling_Entity class attributes and methods
forms_entityModeling_Entity_name: Property = Property(name="name", type=StringType)
forms_entityModeling_Entity.attributes={forms_entityModeling_Entity_name}

# forms_entityModeling_Enumeration class attributes and methods
forms_entityModeling_Enumeration_name: Property = Property(name="name", type=StringType)
forms_entityModeling_Enumeration.attributes={forms_entityModeling_Enumeration_name}

# Literal class attributes and methods

# forms_entityModeling_Relationship class attributes and methods
forms_entityModeling_Relationship_name: Property = Property(name="name", type=StringType)
forms_entityModeling_Relationship_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
forms_entityModeling_Relationship_upperBound: Property = Property(name="upperBound", type=IntegerType)
forms_entityModeling_Relationship.attributes={forms_entityModeling_Relationship_upperBound, forms_entityModeling_Relationship_name, forms_entityModeling_Relationship_lowerBound}

# forms_entityModeling_Literal class attributes and methods
forms_entityModeling_Literal_name: Property = Property(name="name", type=StringType)
forms_entityModeling_Literal_value: Property = Property(name="value", type=StringType)
forms_entityModeling_Literal.attributes={forms_entityModeling_Literal_value, forms_entityModeling_Literal_name}

# Page class attributes and methods

# forms_entityModeling_Page class attributes and methods
forms_entityModeling_Page_title: Property = Property(name="title", type=StringType)
forms_entityModeling_Page.attributes={forms_entityModeling_Page_title}

# PageElement class attributes and methods

# Condition class attributes and methods

# forms_entityModeling_Form class attributes and methods
forms_entityModeling_Form_name: Property = Property(name="name", type=StringType)
forms_entityModeling_Form_title: Property = Property(name="title", type=StringType)
forms_entityModeling_Form_description: Property = Property(name="description", type=StringType)
forms_entityModeling_Form.attributes={forms_entityModeling_Form_description, forms_entityModeling_Form_title, forms_entityModeling_Form_name}

# forms_entityModeling_AttributePageElement class attributes and methods
forms_entityModeling_AttributePageElement_valueOfAttribute: Property = Property(name="valueOfAttribute", type=StringType)
forms_entityModeling_AttributePageElement_m_enterValues: Method = Method(name="enterValues", parameters={})
forms_entityModeling_AttributePageElement.attributes={forms_entityModeling_AttributePageElement_valueOfAttribute}
forms_entityModeling_AttributePageElement.methods={forms_entityModeling_AttributePageElement_m_enterValues}

# forms_entityModeling_RelationshipPageElement class attributes and methods

# forms_entityModeling_PageElement class attributes and methods
forms_entityModeling_PageElement_label: Property = Property(name="label", type=StringType)
forms_entityModeling_PageElement_elementID: Property = Property(name="elementID", type=StringType)
forms_entityModeling_PageElement.attributes={forms_entityModeling_PageElement_label, forms_entityModeling_PageElement_elementID}

# forms_entityModeling_Textfield class attributes and methods
forms_entityModeling_Textfield_allowedValueFormat: Property = Property(name="allowedValueFormat", type=StringType)
forms_entityModeling_Textfield.attributes={forms_entityModeling_Textfield_allowedValueFormat}

# AttributePageElement class attributes and methods

# forms_entityModeling_Textarea class attributes and methods

# forms_entityModeling_SelectionField class attributes and methods

# forms_entityModeling_DateSelectionField class attributes and methods

# forms_entityModeling_TimeSelectionField class attributes and methods

# forms_entityModeling_List class attributes and methods

# RelationshipPageElement class attributes and methods

# forms_entityModeling_Table class attributes and methods

# Column class attributes and methods

# forms_entityModeling_Column class attributes and methods

# forms_entityModeling_Condition class attributes and methods
forms_entityModeling_Condition_type: Property = Property(name="type", type=StringType)
forms_entityModeling_Condition_conditionID: Property = Property(name="conditionID", type=StringType)
forms_entityModeling_Condition.attributes={forms_entityModeling_Condition_conditionID, forms_entityModeling_Condition_type}

# forms_entityModeling_CompositeCondition class attributes and methods
forms_entityModeling_CompositeCondition_booleanOperator: Property = Property(name="booleanOperator", type=StringType)
forms_entityModeling_CompositeCondition.attributes={forms_entityModeling_CompositeCondition_booleanOperator}

# forms_entityModeling_AttributeValueCondition class attributes and methods

# Relationships
entities0: BinaryAssociation = BinaryAssociation(
    name="entities0",
    ends={
        Property(name="Entity", type=forms_EFML_model, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_EFML_model", type=Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumerations1: BinaryAssociation = BinaryAssociation(
    name="enumerations1",
    ends={
        Property(name="Enumeration", type=forms_EFML_model, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_EFML_model2", type=Enumeration_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
welcomeForm3: BinaryAssociation = BinaryAssociation(
    name="welcomeForm3",
    ends={
        Property(name="Form", type=forms_EFML_model, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_EFML_model4", type=Form, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
forms5: BinaryAssociation = BinaryAssociation(
    name="forms5",
    ends={
        Property(name="Form7", type=forms_EFML_model, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_EFML_model6", type=Form, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
id8: BinaryAssociation = BinaryAssociation(
    name="id8",
    ends={
        Property(name="Attribute", type=forms_entityModeling_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_entityModeling_Entity", type=Attribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes9: BinaryAssociation = BinaryAssociation(
    name="attributes9",
    ends={
        Property(name="Attribute11", type=forms_entityModeling_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_entityModeling_Entity10", type=Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType12: BinaryAssociation = BinaryAssociation(
    name="superType12",
    ends={
        Property(name="Entity14", type=forms_entityModeling_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_entityModeling_Entity13", type=Entity, multiplicity=Multiplicity(0, 1))
    }
)
relationships15: BinaryAssociation = BinaryAssociation(
    name="relationships15",
    ends={
        Property(name="Relationship", type=forms_entityModeling_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_entityModeling_Entity16", type=Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumerationType17: BinaryAssociation = BinaryAssociation(
    name="enumerationType17",
    ends={
        Property(name="Enumeration18", type=forms_entityModeling_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_entityModeling_Attribute", type=Enumeration_, multiplicity=Multiplicity(0, 1))
    }
)
literals19: BinaryAssociation = BinaryAssociation(
    name="literals19",
    ends={
        Property(name="Literal", type=forms_entityModeling_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_entityModeling_Enumeration", type=Literal, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
opposite22: BinaryAssociation = BinaryAssociation(
    name="opposite22",
    ends={
        Property(name="Relationship24", type=forms_entityModeling_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_entityModeling_Relationship23", type=Relationship, multiplicity=Multiplicity(0, 1))
    }
)
target20: BinaryAssociation = BinaryAssociation(
    name="target20",
    ends={
        Property(name="Entity21", type=forms_entityModeling_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_entityModeling_Relationship", type=Entity, multiplicity=Multiplicity(1, 1))
    }
)
entity25: BinaryAssociation = BinaryAssociation(
    name="entity25",
    ends={
        Property(name="Entity26", type=forms_entityModeling_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_entityModeling_Form", type=Entity, multiplicity=Multiplicity(1, 1))
    }
)
pages27: BinaryAssociation = BinaryAssociation(
    name="pages27",
    ends={
        Property(name="Page", type=forms_entityModeling_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_entityModeling_Form28", type=Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pageElements29: BinaryAssociation = BinaryAssociation(
    name="pageElements29",
    ends={
        Property(name="PageElement", type=forms_entityModeling_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_entityModeling_Page", type=PageElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition32: BinaryAssociation = BinaryAssociation(
    name="condition32",
    ends={
        Property(name="Condition33", type=forms_entityModeling_PageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_entityModeling_PageElement", type=Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributeToEnterValues34: BinaryAssociation = BinaryAssociation(
    name="attributeToEnterValues34",
    ends={
        Property(name="Attribute35", type=forms_entityModeling_AttributePageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_entityModeling_AttributePageElement", type=Attribute, multiplicity=Multiplicity(1, 1))
    }
)
condition30: BinaryAssociation = BinaryAssociation(
    name="condition30",
    ends={
        Property(name="Condition", type=forms_entityModeling_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_entityModeling_Page31", type=Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
editingForm38: BinaryAssociation = BinaryAssociation(
    name="editingForm38",
    ends={
        Property(name="Form40", type=forms_entityModeling_RelationshipPageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_entityModeling_RelationshipPageElement39", type=Form, multiplicity=Multiplicity(1, 1))
    }
)
relationshipToEnterValues36: BinaryAssociation = BinaryAssociation(
    name="relationshipToEnterValues36",
    ends={
        Property(name="Relationship37", type=forms_entityModeling_RelationshipPageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_entityModeling_RelationshipPageElement", type=Relationship, multiplicity=Multiplicity(1, 1))
    }
)
Columns43: BinaryAssociation = BinaryAssociation(
    name="Columns43",
    ends={
        Property(name="Column", type=forms_entityModeling_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_entityModeling_Table", type=Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
attribute44: BinaryAssociation = BinaryAssociation(
    name="attribute44",
    ends={
        Property(name="Attribute45", type=forms_entityModeling_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_entityModeling_Column", type=Attribute, multiplicity=Multiplicity(1, 1))
    }
)
alreadyEnteredEntity41: BinaryAssociation = BinaryAssociation(
    name="alreadyEnteredEntity41",
    ends={
        Property(name="Entity42", type=forms_entityModeling_List, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_entityModeling_List", type=Entity, multiplicity=Multiplicity(0, 9999))
    }
)
value46: BinaryAssociation = BinaryAssociation(
    name="value46",
    ends={
        Property(name="Attribute47", type=forms_entityModeling_AttributeValueCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_entityModeling_AttributeValueCondition", type=Attribute, multiplicity=Multiplicity(0, 1))
    }
)
composedConditions48: BinaryAssociation = BinaryAssociation(
    name="composedConditions48",
    ends={
        Property(name="Condition49", type=forms_entityModeling_CompositeCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_entityModeling_CompositeCondition", type=Condition, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)

# Generalizations
gen_forms_entityModeling_AttributePageElement_PageElement = Generalization(general=PageElement, specific=forms_entityModeling_AttributePageElement)
gen_forms_entityModeling_RelationshipPageElement_PageElement = Generalization(general=PageElement, specific=forms_entityModeling_RelationshipPageElement)
gen_forms_entityModeling_Textfield_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_entityModeling_Textfield)
gen_forms_entityModeling_Textarea_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_entityModeling_Textarea)
gen_forms_entityModeling_SelectionField_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_entityModeling_SelectionField)
gen_forms_entityModeling_DateSelectionField_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_entityModeling_DateSelectionField)
gen_forms_entityModeling_TimeSelectionField_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_entityModeling_TimeSelectionField)
gen_forms_entityModeling_List_RelationshipPageElement = Generalization(general=RelationshipPageElement, specific=forms_entityModeling_List)
gen_forms_entityModeling_Table_RelationshipPageElement = Generalization(general=RelationshipPageElement, specific=forms_entityModeling_Table)
gen_forms_entityModeling_CompositeCondition_Condition = Generalization(general=Condition, specific=forms_entityModeling_CompositeCondition)
gen_forms_entityModeling_AttributeValueCondition_Condition = Generalization(general=Condition, specific=forms_entityModeling_AttributeValueCondition)

# Domain Model
domain_model = DomainModel(
    name="forms",
    types={Entity, Enumeration_, Form, forms_EFML_model, Attribute, Relationship, forms_entityModeling_Attribute, forms_entityModeling_Entity, forms_entityModeling_Enumeration, Literal, forms_entityModeling_Relationship, forms_entityModeling_Literal, Page, forms_entityModeling_Page, PageElement, Condition, forms_entityModeling_Form, forms_entityModeling_AttributePageElement, forms_entityModeling_RelationshipPageElement, forms_entityModeling_PageElement, forms_entityModeling_Textfield, AttributePageElement, forms_entityModeling_Textarea, forms_entityModeling_SelectionField, forms_entityModeling_DateSelectionField, forms_entityModeling_TimeSelectionField, forms_entityModeling_List, RelationshipPageElement, forms_entityModeling_Table, Column, forms_entityModeling_Column, forms_entityModeling_Condition, forms_entityModeling_CompositeCondition, forms_entityModeling_AttributeValueCondition, AttributeType, ConditionType, BooleanOperators},
    associations={entities0, enumerations1, welcomeForm3, forms5, id8, attributes9, superType12, relationships15, enumerationType17, literals19, opposite22, target20, entity25, pages27, pageElements29, condition32, attributeToEnterValues34, condition30, editingForm38, relationshipToEnterValues36, Columns43, attribute44, alreadyEnteredEntity41, value46, composedConditions48},
    generalizations={gen_forms_entityModeling_AttributePageElement_PageElement, gen_forms_entityModeling_RelationshipPageElement_PageElement, gen_forms_entityModeling_Textfield_AttributePageElement, gen_forms_entityModeling_Textarea_AttributePageElement, gen_forms_entityModeling_SelectionField_AttributePageElement, gen_forms_entityModeling_DateSelectionField_AttributePageElement, gen_forms_entityModeling_TimeSelectionField_AttributePageElement, gen_forms_entityModeling_List_RelationshipPageElement, gen_forms_entityModeling_Table_RelationshipPageElement, gen_forms_entityModeling_CompositeCondition_Condition, gen_forms_entityModeling_AttributeValueCondition_Condition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)