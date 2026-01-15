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
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Text"),
			EnumerationLiteral(name="Date"),
			EnumerationLiteral(name="Time"),
			EnumerationLiteral(name="Email"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="Year"),
			EnumerationLiteral(name="None")
    }
)

ConditionType: Enumeration = Enumeration(
    name="ConditionType",
    literals={
            EnumerationLiteral(name="Hide"),
			EnumerationLiteral(name="Show"),
			EnumerationLiteral(name="Enable"),
			EnumerationLiteral(name="Disable"),
			EnumerationLiteral(name="None")
    }
)

CompositeConditionType: Enumeration = Enumeration(
    name="CompositeConditionType",
    literals={
            EnumerationLiteral(name="And"),
			EnumerationLiteral(name="Or")
    }
)

# Classes
forms_Entity = Class(name="forms::Entity")
EntityModelElement = Class(name="EntityModelElement")
NamedElement = Class(name="NamedElement")
forms_Feature = Class(name="forms::Feature", is_abstract=True)
forms_Attribute = Class(name="forms::Attribute")
Feature = Class(name="Feature")
forms_Enumeration = Class(name="forms::Enumeration")
forms_Relationship = Class(name="forms::Relationship")
forms_EntityModel = Class(name="forms::EntityModel")
forms_EntityModelElement = Class(name="forms::EntityModelElement", is_abstract=True)
forms_Literal = Class(name="forms::Literal")
forms_NamedElement = Class(name="forms::NamedElement", is_abstract=True)
forms_FormModel = Class(name="forms::FormModel")
forms_Form = Class(name="forms::Form")
forms_Page = Class(name="forms::Page")
forms_PageElement = Class(name="forms::PageElement", is_abstract=True)
forms_Condition = Class(name="forms::Condition", is_abstract=True)
forms_Column = Class(name="forms::Column")
forms_TextField = Class(name="forms::TextField")
AttributePageElement = Class(name="AttributePageElement")
forms_TextArea = Class(name="forms::TextArea")
forms_SelectionField = Class(name="forms::SelectionField")
forms_List = Class(name="forms::List")
RelationshipPageElement = Class(name="RelationshipPageElement")
forms_Table = Class(name="forms::Table")
forms_AttributeValueCondition = Class(name="forms::AttributeValueCondition")
Condition = Class(name="Condition")
forms_CompositeCondition = Class(name="forms::CompositeCondition")
forms_TimeSelectionField = Class(name="forms::TimeSelectionField")
forms_AttributePageElement = Class(name="forms::AttributePageElement", is_abstract=True)
PageElement = Class(name="PageElement")
forms_RelationshipPageElement = Class(name="forms::RelationshipPageElement", is_abstract=True)
forms_DateSelectionField = Class(name="forms::DateSelectionField")

# forms_Entity class attributes and methods

# EntityModelElement class attributes and methods

# NamedElement class attributes and methods

# forms_Feature class attributes and methods

# forms_Attribute class attributes and methods
forms_Attribute_type: Property = Property(name="type", type=StringType)
forms_Attribute_mandatory: Property = Property(name="mandatory", type=BooleanType)
forms_Attribute.attributes={forms_Attribute_mandatory, forms_Attribute_type}

# Feature class attributes and methods

# forms_Enumeration class attributes and methods

# forms_Relationship class attributes and methods
forms_Relationship_upperBound: Property = Property(name="upperBound", type=IntegerType)
forms_Relationship_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
forms_Relationship.attributes={forms_Relationship_lowerBound, forms_Relationship_upperBound}

# forms_EntityModel class attributes and methods

# forms_EntityModelElement class attributes and methods

# forms_Literal class attributes and methods
forms_Literal_value: Property = Property(name="value", type=StringType)
forms_Literal.attributes={forms_Literal_value}

# forms_NamedElement class attributes and methods
forms_NamedElement_name: Property = Property(name="name", type=StringType)
forms_NamedElement.attributes={forms_NamedElement_name}

# forms_FormModel class attributes and methods

# forms_Form class attributes and methods
forms_Form_title: Property = Property(name="title", type=StringType)
forms_Form_description: Property = Property(name="description", type=StringType)
forms_Form_welcomeForm: Property = Property(name="welcomeForm", type=BooleanType)
forms_Form.attributes={forms_Form_description, forms_Form_welcomeForm, forms_Form_title}

# forms_Page class attributes and methods
forms_Page_title: Property = Property(name="title", type=StringType)
forms_Page.attributes={forms_Page_title}

# forms_PageElement class attributes and methods
forms_PageElement_label: Property = Property(name="label", type=StringType)
forms_PageElement_elementID: Property = Property(name="elementID", type=StringType)
forms_PageElement.attributes={forms_PageElement_elementID, forms_PageElement_label}

# forms_Condition class attributes and methods
forms_Condition_type: Property = Property(name="type", type=StringType)
forms_Condition_conditionID: Property = Property(name="conditionID", type=StringType)
forms_Condition.attributes={forms_Condition_type, forms_Condition_conditionID}

# forms_Column class attributes and methods

# forms_TextField class attributes and methods
forms_TextField_format: Property = Property(name="format", type=StringType)
forms_TextField.attributes={forms_TextField_format}

# AttributePageElement class attributes and methods

# forms_TextArea class attributes and methods

# forms_SelectionField class attributes and methods

# forms_List class attributes and methods

# RelationshipPageElement class attributes and methods

# forms_Table class attributes and methods

# forms_AttributeValueCondition class attributes and methods
forms_AttributeValueCondition_value: Property = Property(name="value", type=StringType)
forms_AttributeValueCondition.attributes={forms_AttributeValueCondition_value}

# Condition class attributes and methods

# forms_CompositeCondition class attributes and methods
forms_CompositeCondition_compositionType: Property = Property(name="compositionType", type=StringType)
forms_CompositeCondition.attributes={forms_CompositeCondition_compositionType}

# forms_TimeSelectionField class attributes and methods

# forms_AttributePageElement class attributes and methods

# PageElement class attributes and methods

# forms_RelationshipPageElement class attributes and methods

# forms_DateSelectionField class attributes and methods

# Relationships
features0: BinaryAssociation = BinaryAssociation(
    name="features0",
    ends={
        Property(name="forms_Feature", type=forms_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Entity", type=forms_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
id1: BinaryAssociation = BinaryAssociation(
    name="id1",
    ends={
        Property(name="forms_Attribute", type=forms_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Entity2", type=forms_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
superType4: BinaryAssociation = BinaryAssociation(
    name="superType4",
    ends={
        Property(name="forms_Entity5", type=forms_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Entity3", type=forms_Entity, multiplicity=Multiplicity(0, 1))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="forms_Entity9", type=forms_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Relationship", type=forms_Entity, multiplicity=Multiplicity(1, 1))
    }
)
enumeration6: BinaryAssociation = BinaryAssociation(
    name="enumeration6",
    ends={
        Property(name="forms_Enumeration", type=forms_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Attribute7", type=forms_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
opposite11: BinaryAssociation = BinaryAssociation(
    name="opposite11",
    ends={
        Property(name="forms_Relationship12", type=forms_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Relationship10", type=forms_Relationship, multiplicity=Multiplicity(0, 1))
    }
)
literals13: BinaryAssociation = BinaryAssociation(
    name="literals13",
    ends={
        Property(name="forms_Literal", type=forms_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Enumeration14", type=forms_Literal, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
entity17: BinaryAssociation = BinaryAssociation(
    name="entity17",
    ends={
        Property(name="forms_Entity19", type=forms_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Form18", type=forms_Entity, multiplicity=Multiplicity(1, 1))
    }
)
entityModelElements15: BinaryAssociation = BinaryAssociation(
    name="entityModelElements15",
    ends={
        Property(name="forms_EntityModelElement", type=forms_EntityModel, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_EntityModel", type=forms_EntityModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forms16: BinaryAssociation = BinaryAssociation(
    name="forms16",
    ends={
        Property(name="forms_Form", type=forms_FormModel, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_FormModel", type=forms_Form, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pages20: BinaryAssociation = BinaryAssociation(
    name="pages20",
    ends={
        Property(name="forms_Page", type=forms_Form, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Form21", type=forms_Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pageElements22: BinaryAssociation = BinaryAssociation(
    name="pageElements22",
    ends={
        Property(name="forms_PageElement", type=forms_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Page23", type=forms_PageElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition24: BinaryAssociation = BinaryAssociation(
    name="condition24",
    ends={
        Property(name="forms_Condition", type=forms_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Page25", type=forms_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition26: BinaryAssociation = BinaryAssociation(
    name="condition26",
    ends={
        Property(name="forms_Condition28", type=forms_PageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_PageElement27", type=forms_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columns29: BinaryAssociation = BinaryAssociation(
    name="columns29",
    ends={
        Property(name="forms_Column", type=forms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_Table", type=forms_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute30: BinaryAssociation = BinaryAssociation(
    name="attribute30",
    ends={
        Property(name="forms_Attribute31", type=forms_AttributeValueCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_AttributeValueCondition", type=forms_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
composedConditions32: BinaryAssociation = BinaryAssociation(
    name="composedConditions32",
    ends={
        Property(name="forms_Condition33", type=forms_CompositeCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_CompositeCondition", type=forms_Condition, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
attribute34: BinaryAssociation = BinaryAssociation(
    name="attribute34",
    ends={
        Property(name="forms_Attribute35", type=forms_AttributePageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_AttributePageElement", type=forms_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
relationship36: BinaryAssociation = BinaryAssociation(
    name="relationship36",
    ends={
        Property(name="forms_Relationship37", type=forms_RelationshipPageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_RelationshipPageElement", type=forms_Relationship, multiplicity=Multiplicity(1, 1))
    }
)
editingForm38: BinaryAssociation = BinaryAssociation(
    name="editingForm38",
    ends={
        Property(name="forms_Form40", type=forms_RelationshipPageElement, multiplicity=Multiplicity(1, 1)),
        Property(name="forms_RelationshipPageElement39", type=forms_Form, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_forms_Entity_EntityModelElement = Generalization(general=EntityModelElement, specific=forms_Entity)
gen_forms_Entity_NamedElement = Generalization(general=NamedElement, specific=forms_Entity)
gen_forms_Attribute_Feature = Generalization(general=Feature, specific=forms_Attribute)
gen_forms_Relationship_Feature = Generalization(general=Feature, specific=forms_Relationship)
gen_forms_Enumeration_EntityModelElement = Generalization(general=EntityModelElement, specific=forms_Enumeration)
gen_forms_Enumeration_NamedElement = Generalization(general=NamedElement, specific=forms_Enumeration)
gen_forms_Literal_NamedElement = Generalization(general=NamedElement, specific=forms_Literal)
gen_forms_Form_NamedElement = Generalization(general=NamedElement, specific=forms_Form)
gen_forms_Feature_NamedElement = Generalization(general=NamedElement, specific=forms_Feature)
gen_forms_TextField_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_TextField)
gen_forms_TextArea_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_TextArea)
gen_forms_SelectionField_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_SelectionField)
gen_forms_List_RelationshipPageElement = Generalization(general=RelationshipPageElement, specific=forms_List)
gen_forms_Table_RelationshipPageElement = Generalization(general=RelationshipPageElement, specific=forms_Table)
gen_forms_Column_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_Column)
gen_forms_AttributeValueCondition_Condition = Generalization(general=Condition, specific=forms_AttributeValueCondition)
gen_forms_CompositeCondition_Condition = Generalization(general=Condition, specific=forms_CompositeCondition)
gen_forms_TimeSelectionField_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_TimeSelectionField)
gen_forms_AttributePageElement_PageElement = Generalization(general=PageElement, specific=forms_AttributePageElement)
gen_forms_RelationshipPageElement_PageElement = Generalization(general=PageElement, specific=forms_RelationshipPageElement)
gen_forms_DateSelectionField_AttributePageElement = Generalization(general=AttributePageElement, specific=forms_DateSelectionField)

# Domain Model
domain_model = DomainModel(
    name="forms",
    types={forms_Entity, EntityModelElement, NamedElement, forms_Feature, forms_Attribute, Feature, forms_Enumeration, forms_Relationship, forms_EntityModel, forms_EntityModelElement, forms_Literal, forms_NamedElement, forms_FormModel, forms_Form, forms_Page, forms_PageElement, forms_Condition, forms_Column, forms_TextField, AttributePageElement, forms_TextArea, forms_SelectionField, forms_List, RelationshipPageElement, forms_Table, forms_AttributeValueCondition, Condition, forms_CompositeCondition, forms_TimeSelectionField, forms_AttributePageElement, PageElement, forms_RelationshipPageElement, forms_DateSelectionField, AttributeType, ConditionType, CompositeConditionType},
    associations={features0, id1, superType4, target8, enumeration6, opposite11, literals13, entity17, entityModelElements15, forms16, pages20, pageElements22, condition24, condition26, columns29, attribute30, composedConditions32, attribute34, relationship36, editingForm38},
    generalizations={gen_forms_Entity_EntityModelElement, gen_forms_Entity_NamedElement, gen_forms_Attribute_Feature, gen_forms_Relationship_Feature, gen_forms_Enumeration_EntityModelElement, gen_forms_Enumeration_NamedElement, gen_forms_Literal_NamedElement, gen_forms_Form_NamedElement, gen_forms_Feature_NamedElement, gen_forms_TextField_AttributePageElement, gen_forms_TextArea_AttributePageElement, gen_forms_SelectionField_AttributePageElement, gen_forms_List_RelationshipPageElement, gen_forms_Table_RelationshipPageElement, gen_forms_Column_AttributePageElement, gen_forms_AttributeValueCondition_Condition, gen_forms_CompositeCondition_Condition, gen_forms_TimeSelectionField_AttributePageElement, gen_forms_AttributePageElement_PageElement, gen_forms_RelationshipPageElement_PageElement, gen_forms_DateSelectionField_AttributePageElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)