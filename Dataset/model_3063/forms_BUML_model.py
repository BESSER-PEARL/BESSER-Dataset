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
			EnumerationLiteral(name="None_")
    }
)

OperatorType: Enumeration = Enumeration(
    name="OperatorType",
    literals={
            EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
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

# Classes
forms_Enumeration = Class(name="forms_Enumeration")
forms_Model = Class(name="forms_Model")
forms_Form = Class(name="forms_Form")
forms_Entity = Class(name="forms_Entity")
forms_Attribute = Class(name="forms_Attribute")
forms_Relationship = Class(name="forms_Relationship")
forms_Condition = Class(name="forms_Condition", is_abstract=True)
forms_Literal = Class(name="forms_Literal")
forms_ListRelationshipPageElement = Class(name="forms_ListRelationshipPageElement")
RelationshipPageElement = Class(name="RelationshipPageElement")
forms_TableRelationshipPageElement = Class(name="forms_TableRelationshipPageElement")
forms_Column = Class(name="forms_Column")
forms_Page = Class(name="forms_Page")
forms_PageElement = Class(name="forms_PageElement", is_abstract=True)
forms_AttributePageElement = Class(name="forms_AttributePageElement", is_abstract=True)
PageElement = Class(name="PageElement")
forms_RelationshipPageElement = Class(name="forms_RelationshipPageElement", is_abstract=True)
forms_TextFields = Class(name="forms_TextFields")
AttributePageElement = Class(name="AttributePageElement")
forms_TextAreas = Class(name="forms_TextAreas")
forms_SelectionFields = Class(name="forms_SelectionFields")
forms_DateSelectionFields = Class(name="forms_DateSelectionFields")
forms_TimeSelectionFields = Class(name="forms_TimeSelectionFields")
forms_AttributeValueCondition = Class(name="forms_AttributeValueCondition")
Condition = Class(name="Condition")
forms_CompositeCondition = Class(name="forms_CompositeCondition")

# forms_Enumeration class attributes and methods
forms_Enumeration_name: Property = Property(name="name", type=StringType)
forms_Enumeration.attributes={forms_Enumeration_name}

# forms_Model class attributes and methods

# forms_Form class attributes and methods
forms_Form_name: Property = Property(name="name", type=StringType)
forms_Form_title: Property = Property(name="title", type=StringType)
forms_Form_description: Property = Property(name="description", type=StringType)
forms_Form_isWelcomeForm: Property = Property(name="isWelcomeForm", type=StringType)
forms_Form.attributes={forms_Form_title, forms_Form_description, forms_Form_name, forms_Form_isWelcomeForm}

# forms_Entity class attributes and methods
forms_Entity_name: Property = Property(name="name", type=StringType)
forms_Entity.attributes={forms_Entity_name}

# forms_Attribute class attributes and methods
forms_Attribute_name: Property = Property(name="name", type=StringType)
forms_Attribute_mandatory: Property = Property(name="mandatory", type=BooleanType)
forms_Attribute_type: Property = Property(name="type", type=StringType)
forms_Attribute_isId: Property = Property(name="isId", type=StringType)
forms_Attribute.attributes={forms_Attribute_mandatory, forms_Attribute_type, forms_Attribute_isId, forms_Attribute_name}

# forms_Relationship class attributes and methods
forms_Relationship_name: Property = Property(name="name", type=StringType)
forms_Relationship_lowerBound: Property = Property(name="lowerBound", type=StringType)
forms_Relationship_upperBound: Property = Property(name="upperBound", type=StringType)
forms_Relationship.attributes={forms_Relationship_upperBound, forms_Relationship_lowerBound, forms_Relationship_name}

# forms_Condition class attributes and methods
forms_Condition_conditionID: Property = Property(name="conditionID", type=StringType)
forms_Condition_type: Property = Property(name="type", type=StringType)
forms_Condition.attributes={forms_Condition_conditionID, forms_Condition_type}

# forms_Literal class attributes and methods
forms_Literal_name: Property = Property(name="name", type=StringType)
forms_Literal_value: Property = Property(name="value", type=StringType)
forms_Literal.attributes={forms_Literal_name, forms_Literal_value}

# forms_ListRelationshipPageElement class attributes and methods

# RelationshipPageElement class attributes and methods

# forms_TableRelationshipPageElement class attributes and methods

# forms_Column class attributes and methods

# forms_Page class attributes and methods
forms_Page_title: Property = Property(name="title", type=StringType)
forms_Page.attributes={forms_Page_title}

# forms_PageElement class attributes and methods
forms_PageElement_label: Property = Property(name="label", type=StringType)
forms_PageElement_elementID: Property = Property(name="elementID", type=StringType)
forms_PageElement.attributes={forms_PageElement_label, forms_PageElement_elementID}

# forms_AttributePageElement class attributes and methods
forms_AttributePageElement_value: Property = Property(name="value", type=StringType)
forms_AttributePageElement.attributes={forms_AttributePageElement_value}

# PageElement class attributes and methods

# forms_RelationshipPageElement class attributes and methods

# forms_TextFields class attributes and methods
forms_TextFields_format: Property = Property(name="format", type=StringType)
forms_TextFields.attributes={forms_TextFields_format}

# AttributePageElement class attributes and methods

# forms_TextAreas class attributes and methods

# forms_SelectionFields class attributes and methods

# forms_DateSelectionFields class attributes and methods

# forms_TimeSelectionFields class attributes and methods

# forms_AttributeValueCondition class attributes and methods
forms_AttributeValueCondition_value: Property = Property(name="value", type=StringType)
forms_AttributeValueCondition.attributes={forms_AttributeValueCondition_value}

# Condition class attributes and methods

# forms_CompositeCondition class attributes and methods
forms_CompositeCondition_operatorType: Property = Property(name="operatorType", type=StringType)
forms_CompositeCondition.attributes={forms_CompositeCondition_operatorType}

# Relationships
enumerationType6: BinaryAssociation = BinaryAssociation(
    name="enumerationType6",
    ends={
        Property(name="forms_Enumeration", type=forms_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Attribute7", type=forms_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
modelEntity8: BinaryAssociation = BinaryAssociation(
    name="modelEntity8",
    ends={
        Property(name="forms_Entity9", type=forms_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Model", type=forms_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelForm10: BinaryAssociation = BinaryAssociation(
    name="modelForm10",
    ends={
        Property(name="forms_Form", type=forms_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Model11", type=forms_Form, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelEnumeration12: BinaryAssociation = BinaryAssociation(
    name="modelEnumeration12",
    ends={
        Property(name="forms_Enumeration14", type=forms_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Model13", type=forms_Enumeration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entityAttribute0: BinaryAssociation = BinaryAssociation(
    name="entityAttribute0",
    ends={
        Property(name="forms_Attribute", type=forms_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Entity", type=forms_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationship1: BinaryAssociation = BinaryAssociation(
    name="relationship1",
    ends={
        Property(name="forms_Relationship", type=forms_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Entity2", type=forms_Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType4: BinaryAssociation = BinaryAssociation(
    name="superType4",
    ends={
        Property(name="forms_Entity5", type=forms_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Entity3", type=forms_Entity, multiplicity=Multiplicity(0, 1))
    }
)
target19: BinaryAssociation = BinaryAssociation(
    name="target19",
    ends={
        Property(name="forms_Entity21", type=forms_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Relationship20", type=forms_Entity, multiplicity=Multiplicity(1, 1))
    }
)
opposite23: BinaryAssociation = BinaryAssociation(
    name="opposite23",
    ends={
        Property(name="forms_Relationship24", type=forms_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Relationship22", type=forms_Relationship, multiplicity=Multiplicity(0, 1))
    }
)
modelCondition15: BinaryAssociation = BinaryAssociation(
    name="modelCondition15",
    ends={
        Property(name="forms_Condition", type=forms_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Model16", type=forms_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literal17: BinaryAssociation = BinaryAssociation(
    name="literal17",
    ends={
        Property(name="forms_Literal", type=forms_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Enumeration18", type=forms_Literal, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
editingForm34: BinaryAssociation = BinaryAssociation(
    name="editingForm34",
    ends={
        Property(name="forms_Form35", type=forms_RelationshipPageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_RelationshipPageElement", type=forms_Form, multiplicity=Multiplicity(1, 1))
    }
)
relationshipRef36: BinaryAssociation = BinaryAssociation(
    name="relationshipRef36",
    ends={
        Property(name="forms_Relationship38", type=forms_RelationshipPageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_RelationshipPageElement37", type=forms_Relationship, multiplicity=Multiplicity(1, 1))
    }
)
columns39: BinaryAssociation = BinaryAssociation(
    name="columns39",
    ends={
        Property(name="forms_Column", type=forms_TableRelationshipPageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_TableRelationshipPageElement", type=forms_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributeReference40: BinaryAssociation = BinaryAssociation(
    name="attributeReference40",
    ends={
        Property(name="forms_Attribute42", type=forms_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Column41", type=forms_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
formEntity25: BinaryAssociation = BinaryAssociation(
    name="formEntity25",
    ends={
        Property(name="forms_Entity27", type=forms_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Form26", type=forms_Entity, multiplicity=Multiplicity(1, 1))
    }
)
pages28: BinaryAssociation = BinaryAssociation(
    name="pages28",
    ends={
        Property(name="forms_Page", type=forms_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Form29", type=forms_Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pageElements30: BinaryAssociation = BinaryAssociation(
    name="pageElements30",
    ends={
        Property(name="forms_PageElement", type=forms_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Page31", type=forms_PageElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributeRef32: BinaryAssociation = BinaryAssociation(
    name="attributeRef32",
    ends={
        Property(name="forms_Attribute33", type=forms_AttributePageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_AttributePageElement", type=forms_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
targetPage43: BinaryAssociation = BinaryAssociation(
    name="targetPage43",
    ends={
        Property(name="forms_Page45", type=forms_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Condition44", type=forms_Page, multiplicity=Multiplicity(0, 1))
    }
)
targetPageElement46: BinaryAssociation = BinaryAssociation(
    name="targetPageElement46",
    ends={
        Property(name="forms_PageElement48", type=forms_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Condition47", type=forms_PageElement, multiplicity=Multiplicity(0, 1))
    }
)
attributeToCompare49: BinaryAssociation = BinaryAssociation(
    name="attributeToCompare49",
    ends={
        Property(name="forms_AttributePageElement50", type=forms_AttributeValueCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_AttributeValueCondition", type=forms_AttributePageElement, multiplicity=Multiplicity(1, 1))
    }
)
child151: BinaryAssociation = BinaryAssociation(
    name="child151",
    ends={
        Property(name="forms_Condition52", type=forms_CompositeCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_CompositeCondition", type=forms_Condition, multiplicity=Multiplicity(1, 1))
    }
)
child253: BinaryAssociation = BinaryAssociation(
    name="child253",
    ends={
        Property(name="forms_Condition55", type=forms_CompositeCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_CompositeCondition54", type=forms_Condition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_forms_ListRelationshipPageElement_RelationshipPageElement = Generalization(general=RelationshipPageElement, specific=forms_ListRelationshipPageElement)
gen_forms_TableRelationshipPageElement_RelationshipPageElement = Generalization(general=RelationshipPageElement, specific=forms_TableRelationshipPageElement)
gen_forms_AttributePageElement_PageElement = Generalization(general=PageElement, specific=forms_AttributePageElement)
gen_forms_RelationshipPageElement_PageElement = Generalization(general=PageElement, specific=forms_RelationshipPageElement)
gen_forms_TextFields_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_TextFields)
gen_forms_TextAreas_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_TextAreas)
gen_forms_SelectionFields_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_SelectionFields)
gen_forms_DateSelectionFields_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_DateSelectionFields)
gen_forms_TimeSelectionFields_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_TimeSelectionFields)
gen_forms_AttributeValueCondition_Condition = Generalization(general=Condition, specific=forms_AttributeValueCondition)
gen_forms_CompositeCondition_Condition = Generalization(general=Condition, specific=forms_CompositeCondition)

# Domain Model
domain_model = DomainModel(
    name="forms",
    types={forms_Enumeration, forms_Model, forms_Form, forms_Entity, forms_Attribute, forms_Relationship, forms_Condition, forms_Literal, forms_ListRelationshipPageElement, RelationshipPageElement, forms_TableRelationshipPageElement, forms_Column, forms_Page, forms_PageElement, forms_AttributePageElement, PageElement, forms_RelationshipPageElement, forms_TextFields, AttributePageElement, forms_TextAreas, forms_SelectionFields, forms_DateSelectionFields, forms_TimeSelectionFields, forms_AttributeValueCondition, Condition, forms_CompositeCondition, AttributeType, OperatorType, ConditionType},
    associations={enumerationType6, modelEntity8, modelForm10, modelEnumeration12, entityAttribute0, relationship1, superType4, target19, opposite23, modelCondition15, literal17, editingForm34, relationshipRef36, columns39, attributeReference40, formEntity25, pages28, pageElements30, attributeRef32, targetPage43, targetPageElement46, attributeToCompare49, child151, child253},
    generalizations={gen_forms_ListRelationshipPageElement_RelationshipPageElement, gen_forms_TableRelationshipPageElement_RelationshipPageElement, gen_forms_AttributePageElement_PageElement, gen_forms_RelationshipPageElement_PageElement, gen_forms_TextFields_AttributePageElement, gen_forms_TextAreas_AttributePageElement, gen_forms_SelectionFields_AttributePageElement, gen_forms_DateSelectionFields_AttributePageElement, gen_forms_TimeSelectionFields_AttributePageElement, gen_forms_AttributeValueCondition_Condition, gen_forms_CompositeCondition_Condition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)