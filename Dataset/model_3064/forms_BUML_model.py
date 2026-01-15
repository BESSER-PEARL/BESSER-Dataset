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
			EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Text"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Date"),
			EnumerationLiteral(name="Time"),
			EnumerationLiteral(name="Year"),
			EnumerationLiteral(name="Email"),
			EnumerationLiteral(name="Boolean")
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

Operators: Enumeration = Enumeration(
    name="Operators",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
    }
)

# Classes
forms_EFML = Class(name="forms::EFML")
forms_Entity = Class(name="forms::Entity")
forms_Form = Class(name="forms::Form")
forms_Attribute = Class(name="forms::Attribute")
forms_Relationship = Class(name="forms::Relationship")
forms_Enumeration = Class(name="forms::Enumeration")
forms_Literal = Class(name="forms::Literal")
forms_TextField = Class(name="forms::TextField")
AttributePageElement = Class(name="AttributePageElement")
forms_Page = Class(name="forms::Page")
forms_PageElement = Class(name="forms::PageElement", is_abstract=True)
forms_AttributePageElement = Class(name="forms::AttributePageElement", is_abstract=True)
PageElement = Class(name="PageElement")
forms_RelationshipPageElement = Class(name="forms::RelationshipPageElement", is_abstract=True)
forms_CompositeCondition = Class(name="forms::CompositeCondition")
forms_TextArea = Class(name="forms::TextArea")
forms_SelectionField = Class(name="forms::SelectionField")
forms_DateSelectionField = Class(name="forms::DateSelectionField")
forms_TimeSelectionField = Class(name="forms::TimeSelectionField")
forms_List = Class(name="forms::List")
RelationshipPageElement = Class(name="RelationshipPageElement")
forms_Table = Class(name="forms::Table")
forms_Column = Class(name="forms::Column")
forms_Condition = Class(name="forms::Condition", is_abstract=True)
forms_AttributeValueCondition = Class(name="forms::AttributeValueCondition")
Condition = Class(name="Condition")

# forms_EFML class attributes and methods

# forms_Entity class attributes and methods
forms_Entity_name: Property = Property(name="name", type=StringType)
forms_Entity.attributes={forms_Entity_name}

# forms_Form class attributes and methods
forms_Form_description: Property = Property(name="description", type=StringType)
forms_Form_name: Property = Property(name="name", type=StringType)
forms_Form_title: Property = Property(name="title", type=StringType)
forms_Form_mainForm: Property = Property(name="mainForm", type=BooleanType)
forms_Form.attributes={forms_Form_title, forms_Form_description, forms_Form_name, forms_Form_mainForm}

# forms_Attribute class attributes and methods
forms_Attribute_name: Property = Property(name="name", type=StringType)
forms_Attribute_mandatory: Property = Property(name="mandatory", type=BooleanType)
forms_Attribute_type: Property = Property(name="type", type=StringType)
forms_Attribute.attributes={forms_Attribute_name, forms_Attribute_type, forms_Attribute_mandatory}

# forms_Relationship class attributes and methods
forms_Relationship_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
forms_Relationship_name: Property = Property(name="name", type=StringType)
forms_Relationship_upperBound: Property = Property(name="upperBound", type=IntegerType)
forms_Relationship.attributes={forms_Relationship_upperBound, forms_Relationship_lowerBound, forms_Relationship_name}

# forms_Enumeration class attributes and methods
forms_Enumeration_name: Property = Property(name="name", type=StringType)
forms_Enumeration.attributes={forms_Enumeration_name}

# forms_Literal class attributes and methods
forms_Literal_name: Property = Property(name="name", type=StringType)
forms_Literal_value: Property = Property(name="value", type=StringType)
forms_Literal.attributes={forms_Literal_value, forms_Literal_name}

# forms_TextField class attributes and methods
forms_TextField_format: Property = Property(name="format", type=StringType)
forms_TextField.attributes={forms_TextField_format}

# AttributePageElement class attributes and methods

# forms_Page class attributes and methods
forms_Page_title: Property = Property(name="title", type=StringType)
forms_Page.attributes={forms_Page_title}

# forms_PageElement class attributes and methods
forms_PageElement_label: Property = Property(name="label", type=StringType)
forms_PageElement_elementID: Property = Property(name="elementID", type=StringType)
forms_PageElement.attributes={forms_PageElement_label, forms_PageElement_elementID}

# forms_AttributePageElement class attributes and methods

# PageElement class attributes and methods

# forms_RelationshipPageElement class attributes and methods

# forms_CompositeCondition class attributes and methods
forms_CompositeCondition_operator: Property = Property(name="operator", type=StringType)
forms_CompositeCondition.attributes={forms_CompositeCondition_operator}

# forms_TextArea class attributes and methods

# forms_SelectionField class attributes and methods

# forms_DateSelectionField class attributes and methods

# forms_TimeSelectionField class attributes and methods

# forms_List class attributes and methods

# RelationshipPageElement class attributes and methods

# forms_Table class attributes and methods

# forms_Column class attributes and methods

# forms_Condition class attributes and methods
forms_Condition_conditionID: Property = Property(name="conditionID", type=StringType)
forms_Condition_type: Property = Property(name="type", type=StringType)
forms_Condition.attributes={forms_Condition_conditionID, forms_Condition_type}

# forms_AttributeValueCondition class attributes and methods
forms_AttributeValueCondition_value: Property = Property(name="value", type=StringType)
forms_AttributeValueCondition.attributes={forms_AttributeValueCondition_value}

# Condition class attributes and methods

# Relationships
entities0: BinaryAssociation = BinaryAssociation(
    name="entities0",
    ends={
        Property(name="forms_Entity", type=forms_EFML, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_EFML", type=forms_Entity, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
forms1: BinaryAssociation = BinaryAssociation(
    name="forms1",
    ends={
        Property(name="forms_Form", type=forms_EFML, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_EFML2", type=forms_Form, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes3: BinaryAssociation = BinaryAssociation(
    name="attributes3",
    ends={
        Property(name="forms_Attribute", type=forms_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Entity4", type=forms_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
id5: BinaryAssociation = BinaryAssociation(
    name="id5",
    ends={
        Property(name="forms_Attribute7", type=forms_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Entity6", type=forms_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
relationships8: BinaryAssociation = BinaryAssociation(
    name="relationships8",
    ends={
        Property(name="forms_Relationship", type=forms_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Entity9", type=forms_Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType11: BinaryAssociation = BinaryAssociation(
    name="superType11",
    ends={
        Property(name="forms_Entity12", type=forms_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Entity10", type=forms_Entity, multiplicity=Multiplicity(0, 1))
    }
)
enumerationType13: BinaryAssociation = BinaryAssociation(
    name="enumerationType13",
    ends={
        Property(name="forms_Enumeration", type=forms_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Attribute14", type=forms_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
literals15: BinaryAssociation = BinaryAssociation(
    name="literals15",
    ends={
        Property(name="forms_Literal", type=forms_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Enumeration16", type=forms_Literal, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
opposite18: BinaryAssociation = BinaryAssociation(
    name="opposite18",
    ends={
        Property(name="forms_Relationship19", type=forms_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Relationship17", type=forms_Relationship, multiplicity=Multiplicity(0, 1))
    }
)
target20: BinaryAssociation = BinaryAssociation(
    name="target20",
    ends={
        Property(name="forms_Entity22", type=forms_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Relationship21", type=forms_Entity, multiplicity=Multiplicity(1, 1))
    }
)
entity23: BinaryAssociation = BinaryAssociation(
    name="entity23",
    ends={
        Property(name="forms_Entity25", type=forms_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Form24", type=forms_Entity, multiplicity=Multiplicity(1, 1))
    }
)
pages26: BinaryAssociation = BinaryAssociation(
    name="pages26",
    ends={
        Property(name="forms_Page", type=forms_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Form27", type=forms_Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pageElements28: BinaryAssociation = BinaryAssociation(
    name="pageElements28",
    ends={
        Property(name="forms_PageElement", type=forms_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Page29", type=forms_PageElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute30: BinaryAssociation = BinaryAssociation(
    name="attribute30",
    ends={
        Property(name="forms_Attribute31", type=forms_AttributePageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_AttributePageElement", type=forms_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
editingForm32: BinaryAssociation = BinaryAssociation(
    name="editingForm32",
    ends={
        Property(name="forms_Form33", type=forms_RelationshipPageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_RelationshipPageElement", type=forms_Form, multiplicity=Multiplicity(1, 1))
    }
)
columns34: BinaryAssociation = BinaryAssociation(
    name="columns34",
    ends={
        Property(name="forms_Column", type=forms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Table", type=forms_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entityAttribute35: BinaryAssociation = BinaryAssociation(
    name="entityAttribute35",
    ends={
        Property(name="forms_Attribute37", type=forms_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Column36", type=forms_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
conditions38: BinaryAssociation = BinaryAssociation(
    name="conditions38",
    ends={
        Property(name="forms_Condition", type=forms_CompositeCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_CompositeCondition", type=forms_Condition, multiplicity=Multiplicity(2, 2))
    }
)

# Generalizations
gen_forms_TextField_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_TextField)
gen_forms_AttributePageElement_PageElement = Generalization(general=PageElement, specific=forms_AttributePageElement)
gen_forms_RelationshipPageElement_PageElement = Generalization(general=PageElement, specific=forms_RelationshipPageElement)
gen_forms_CompositeCondition_Condition = Generalization(general=Condition, specific=forms_CompositeCondition)
gen_forms_TextArea_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_TextArea)
gen_forms_SelectionField_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_SelectionField)
gen_forms_DateSelectionField_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_DateSelectionField)
gen_forms_TimeSelectionField_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_TimeSelectionField)
gen_forms_List_RelationshipPageElement = Generalization(general=RelationshipPageElement, specific=forms_List)
gen_forms_Table_RelationshipPageElement = Generalization(general=RelationshipPageElement, specific=forms_Table)
gen_forms_AttributeValueCondition_Condition = Generalization(general=Condition, specific=forms_AttributeValueCondition)

# Domain Model
domain_model = DomainModel(
    name="forms",
    types={forms_EFML, forms_Entity, forms_Form, forms_Attribute, forms_Relationship, forms_Enumeration, forms_Literal, forms_TextField, AttributePageElement, forms_Page, forms_PageElement, forms_AttributePageElement, PageElement, forms_RelationshipPageElement, forms_CompositeCondition, forms_TextArea, forms_SelectionField, forms_DateSelectionField, forms_TimeSelectionField, forms_List, RelationshipPageElement, forms_Table, forms_Column, forms_Condition, forms_AttributeValueCondition, Condition, AttributeType, ConditionType, Operators},
    associations={entities0, forms1, attributes3, id5, relationships8, superType11, enumerationType13, literals15, opposite18, target20, entity23, pages26, pageElements28, attribute30, editingForm32, columns34, entityAttribute35, conditions38},
    generalizations={gen_forms_TextField_AttributePageElement, gen_forms_AttributePageElement_PageElement, gen_forms_RelationshipPageElement_PageElement, gen_forms_CompositeCondition_Condition, gen_forms_TextArea_AttributePageElement, gen_forms_SelectionField_AttributePageElement, gen_forms_DateSelectionField_AttributePageElement, gen_forms_TimeSelectionField_AttributePageElement, gen_forms_List_RelationshipPageElement, gen_forms_Table_RelationshipPageElement, gen_forms_AttributeValueCondition_Condition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)