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
myDsl_Model = Class(name="myDsl::Model")
myDsl_Member = Class(name="myDsl::Member")
myDsl_IntType = Class(name="myDsl::IntType")
BasicType = Class(name="BasicType")
myDsl_Entity = Class(name="myDsl::Entity")
Member = Class(name="Member")
myDsl_IsServer = Class(name="myDsl::IsServer")
myDsl_Attribute = Class(name="myDsl::Attribute")
myDsl_ValueType = Class(name="myDsl::ValueType")
myDsl_ElementType = Class(name="myDsl::ElementType")
myDsl_EntityType = Class(name="myDsl::EntityType")
ElementType = Class(name="ElementType")
myDsl_BasicType = Class(name="myDsl::BasicType")
myDsl_ArrayType = Class(name="myDsl::ArrayType")
myDsl_ArrayElement = Class(name="myDsl::ArrayElement")
myDsl_Verb = Class(name="myDsl::Verb")
myDsl_Rule = Class(name="myDsl::Rule")
myDsl_Condition = Class(name="myDsl::Condition")
myDsl_Expression = Class(name="myDsl::Expression")
myDsl_IntConstant = Class(name="myDsl::IntConstant")
myDsl_StringConstant = Class(name="myDsl::StringConstant")
myDsl_StringType = Class(name="myDsl::StringType")
myDsl_BoolType = Class(name="myDsl::BoolType")
myDsl_Or = Class(name="myDsl::Or")
Expression = Class(name="Expression")
myDsl_And = Class(name="myDsl::And")
myDsl_Equality = Class(name="myDsl::Equality")
myDsl_Comparison = Class(name="myDsl::Comparison")
myDsl_Plus = Class(name="myDsl::Plus")
myDsl_Minus = Class(name="myDsl::Minus")
myDsl_MulOrDiv = Class(name="myDsl::MulOrDiv")
myDsl_Not = Class(name="myDsl::Not")
myDsl_BoolConstant = Class(name="myDsl::BoolConstant")
myDsl_VariableConstant = Class(name="myDsl::VariableConstant")

# myDsl_Model class attributes and methods

# myDsl_Member class attributes and methods

# myDsl_IntType class attributes and methods
myDsl_IntType_value: Property = Property(name="value", type=IntegerType)
myDsl_IntType.attributes={myDsl_IntType_value}

# BasicType class attributes and methods

# myDsl_Entity class attributes and methods
myDsl_Entity_name: Property = Property(name="name", type=StringType)
myDsl_Entity.attributes={myDsl_Entity_name}

# Member class attributes and methods

# myDsl_IsServer class attributes and methods
myDsl_IsServer_value: Property = Property(name="value", type=StringType)
myDsl_IsServer.attributes={myDsl_IsServer_value}

# myDsl_Attribute class attributes and methods
myDsl_Attribute_name: Property = Property(name="name", type=StringType)
myDsl_Attribute.attributes={myDsl_Attribute_name}

# myDsl_ValueType class attributes and methods

# myDsl_ElementType class attributes and methods

# myDsl_EntityType class attributes and methods

# ElementType class attributes and methods

# myDsl_BasicType class attributes and methods

# myDsl_ArrayType class attributes and methods

# myDsl_ArrayElement class attributes and methods

# myDsl_Verb class attributes and methods
myDsl_Verb_verb: Property = Property(name="verb", type=StringType)
myDsl_Verb_qa: Property = Property(name="qa", type=StringType)
myDsl_Verb.attributes={myDsl_Verb_verb, myDsl_Verb_qa}

# myDsl_Rule class attributes and methods

# myDsl_Condition class attributes and methods

# myDsl_Expression class attributes and methods

# myDsl_IntConstant class attributes and methods
myDsl_IntConstant_value: Property = Property(name="value", type=IntegerType)
myDsl_IntConstant.attributes={myDsl_IntConstant_value}

# myDsl_StringConstant class attributes and methods
myDsl_StringConstant_value: Property = Property(name="value", type=StringType)
myDsl_StringConstant.attributes={myDsl_StringConstant_value}

# myDsl_StringType class attributes and methods
myDsl_StringType_value: Property = Property(name="value", type=StringType)
myDsl_StringType.attributes={myDsl_StringType_value}

# myDsl_BoolType class attributes and methods
myDsl_BoolType_value: Property = Property(name="value", type=StringType)
myDsl_BoolType.attributes={myDsl_BoolType_value}

# myDsl_Or class attributes and methods

# Expression class attributes and methods

# myDsl_And class attributes and methods

# myDsl_Equality class attributes and methods
myDsl_Equality_op: Property = Property(name="op", type=StringType)
myDsl_Equality.attributes={myDsl_Equality_op}

# myDsl_Comparison class attributes and methods
myDsl_Comparison_op: Property = Property(name="op", type=StringType)
myDsl_Comparison.attributes={myDsl_Comparison_op}

# myDsl_Plus class attributes and methods

# myDsl_Minus class attributes and methods

# myDsl_MulOrDiv class attributes and methods
myDsl_MulOrDiv_op: Property = Property(name="op", type=StringType)
myDsl_MulOrDiv.attributes={myDsl_MulOrDiv_op}

# myDsl_Not class attributes and methods

# myDsl_BoolConstant class attributes and methods
myDsl_BoolConstant_value: Property = Property(name="value", type=StringType)
myDsl_BoolConstant.attributes={myDsl_BoolConstant_value}

# myDsl_VariableConstant class attributes and methods

# Relationships
members0: BinaryAssociation = BinaryAssociation(
    name="members0",
    ends={
        Property(name="myDsl_Model", type=myDsl_Member, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="myDsl_Member", type=myDsl_Model, multiplicity=Multiplicity(1, 1))
    }
)
expression19: BinaryAssociation = BinaryAssociation(
    name="expression19",
    ends={
        Property(name="myDsl_Condition20", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="myDsl_Expression", type=myDsl_Condition, multiplicity=Multiplicity(1, 1))
    }
)
is1: BinaryAssociation = BinaryAssociation(
    name="is1",
    ends={
        Property(name="myDsl_IsServer", type=myDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Entity", type=myDsl_IsServer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes2: BinaryAssociation = BinaryAssociation(
    name="attributes2",
    ends={
        Property(name="myDsl_Attribute", type=myDsl_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Entity3", type=myDsl_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value4: BinaryAssociation = BinaryAssociation(
    name="value4",
    ends={
        Property(name="myDsl_ValueType", type=myDsl_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Attribute5", type=myDsl_ValueType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementType6: BinaryAssociation = BinaryAssociation(
    name="elementType6",
    ends={
        Property(name="myDsl_ElementType", type=myDsl_ValueType, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ValueType7", type=myDsl_ElementType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entity8: BinaryAssociation = BinaryAssociation(
    name="entity8",
    ends={
        Property(name="myDsl_Entity9", type=myDsl_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_EntityType", type=myDsl_Entity, multiplicity=Multiplicity(0, 1))
    }
)
arrayElements10: BinaryAssociation = BinaryAssociation(
    name="arrayElements10",
    ends={
        Property(name="myDsl_ArrayElement", type=myDsl_ArrayType, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ArrayType", type=myDsl_ArrayElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value11: BinaryAssociation = BinaryAssociation(
    name="value11",
    ends={
        Property(name="myDsl_BasicType", type=myDsl_ArrayElement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_ArrayElement12", type=myDsl_BasicType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rules13: BinaryAssociation = BinaryAssociation(
    name="rules13",
    ends={
        Property(name="myDsl_Rule", type=myDsl_Verb, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Verb", type=myDsl_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition14: BinaryAssociation = BinaryAssociation(
    name="condition14",
    ends={
        Property(name="myDsl_Condition", type=myDsl_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Rule15", type=myDsl_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
url16: BinaryAssociation = BinaryAssociation(
    name="url16",
    ends={
        Property(name="myDsl_ArrayType18", type=myDsl_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Rule17", type=myDsl_ArrayType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left21: BinaryAssociation = BinaryAssociation(
    name="left21",
    ends={
        Property(name="myDsl_Expression22", type=myDsl_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Or", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right23: BinaryAssociation = BinaryAssociation(
    name="right23",
    ends={
        Property(name="myDsl_Expression25", type=myDsl_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Or24", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left26: BinaryAssociation = BinaryAssociation(
    name="left26",
    ends={
        Property(name="myDsl_Expression27", type=myDsl_And, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_And", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right28: BinaryAssociation = BinaryAssociation(
    name="right28",
    ends={
        Property(name="myDsl_Expression30", type=myDsl_And, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_And29", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left31: BinaryAssociation = BinaryAssociation(
    name="left31",
    ends={
        Property(name="myDsl_Expression32", type=myDsl_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Equality", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right33: BinaryAssociation = BinaryAssociation(
    name="right33",
    ends={
        Property(name="myDsl_Expression35", type=myDsl_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Equality34", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left36: BinaryAssociation = BinaryAssociation(
    name="left36",
    ends={
        Property(name="myDsl_Expression37", type=myDsl_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Comparison", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right38: BinaryAssociation = BinaryAssociation(
    name="right38",
    ends={
        Property(name="myDsl_Expression40", type=myDsl_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Comparison39", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left41: BinaryAssociation = BinaryAssociation(
    name="left41",
    ends={
        Property(name="myDsl_Expression42", type=myDsl_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Plus", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right43: BinaryAssociation = BinaryAssociation(
    name="right43",
    ends={
        Property(name="myDsl_Expression45", type=myDsl_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Plus44", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left46: BinaryAssociation = BinaryAssociation(
    name="left46",
    ends={
        Property(name="myDsl_Expression47", type=myDsl_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Minus", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right48: BinaryAssociation = BinaryAssociation(
    name="right48",
    ends={
        Property(name="myDsl_Expression50", type=myDsl_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Minus49", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left51: BinaryAssociation = BinaryAssociation(
    name="left51",
    ends={
        Property(name="myDsl_Expression52", type=myDsl_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_MulOrDiv", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right53: BinaryAssociation = BinaryAssociation(
    name="right53",
    ends={
        Property(name="myDsl_Expression55", type=myDsl_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_MulOrDiv54", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression56: BinaryAssociation = BinaryAssociation(
    name="expression56",
    ends={
        Property(name="myDsl_Expression57", type=myDsl_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Not", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value58: BinaryAssociation = BinaryAssociation(
    name="value58",
    ends={
        Property(name="myDsl_Attribute59", type=myDsl_VariableConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_VariableConstant", type=myDsl_Attribute, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_myDsl_IntType_BasicType = Generalization(general=BasicType, specific=myDsl_IntType)
gen_myDsl_Entity_Member = Generalization(general=Member, specific=myDsl_Entity)
gen_myDsl_EntityType_ElementType = Generalization(general=ElementType, specific=myDsl_EntityType)
gen_myDsl_BasicType_ElementType = Generalization(general=ElementType, specific=myDsl_BasicType)
gen_myDsl_ArrayType_ElementType = Generalization(general=ElementType, specific=myDsl_ArrayType)
gen_myDsl_Verb_Member = Generalization(general=Member, specific=myDsl_Verb)
gen_myDsl_IntConstant_Expression = Generalization(general=Expression, specific=myDsl_IntConstant)
gen_myDsl_StringConstant_Expression = Generalization(general=Expression, specific=myDsl_StringConstant)
gen_myDsl_StringType_BasicType = Generalization(general=BasicType, specific=myDsl_StringType)
gen_myDsl_BoolType_BasicType = Generalization(general=BasicType, specific=myDsl_BoolType)
gen_myDsl_Or_Expression = Generalization(general=Expression, specific=myDsl_Or)
gen_myDsl_And_Expression = Generalization(general=Expression, specific=myDsl_And)
gen_myDsl_Equality_Expression = Generalization(general=Expression, specific=myDsl_Equality)
gen_myDsl_Comparison_Expression = Generalization(general=Expression, specific=myDsl_Comparison)
gen_myDsl_Plus_Expression = Generalization(general=Expression, specific=myDsl_Plus)
gen_myDsl_Minus_Expression = Generalization(general=Expression, specific=myDsl_Minus)
gen_myDsl_MulOrDiv_Expression = Generalization(general=Expression, specific=myDsl_MulOrDiv)
gen_myDsl_Not_Expression = Generalization(general=Expression, specific=myDsl_Not)
gen_myDsl_BoolConstant_Expression = Generalization(general=Expression, specific=myDsl_BoolConstant)
gen_myDsl_VariableConstant_Expression = Generalization(general=Expression, specific=myDsl_VariableConstant)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Model, myDsl_Member, myDsl_IntType, BasicType, myDsl_Entity, Member, myDsl_IsServer, myDsl_Attribute, myDsl_ValueType, myDsl_ElementType, myDsl_EntityType, ElementType, myDsl_BasicType, myDsl_ArrayType, myDsl_ArrayElement, myDsl_Verb, myDsl_Rule, myDsl_Condition, myDsl_Expression, myDsl_IntConstant, myDsl_StringConstant, myDsl_StringType, myDsl_BoolType, myDsl_Or, Expression, myDsl_And, myDsl_Equality, myDsl_Comparison, myDsl_Plus, myDsl_Minus, myDsl_MulOrDiv, myDsl_Not, myDsl_BoolConstant, myDsl_VariableConstant},
    associations={members0, expression19, is1, attributes2, value4, elementType6, entity8, arrayElements10, value11, rules13, condition14, url16, left21, right23, left26, right28, left31, right33, left36, right38, left41, right43, left46, right48, left51, right53, expression56, value58},
    generalizations={gen_myDsl_IntType_BasicType, gen_myDsl_Entity_Member, gen_myDsl_EntityType_ElementType, gen_myDsl_BasicType_ElementType, gen_myDsl_ArrayType_ElementType, gen_myDsl_Verb_Member, gen_myDsl_IntConstant_Expression, gen_myDsl_StringConstant_Expression, gen_myDsl_StringType_BasicType, gen_myDsl_BoolType_BasicType, gen_myDsl_Or_Expression, gen_myDsl_And_Expression, gen_myDsl_Equality_Expression, gen_myDsl_Comparison_Expression, gen_myDsl_Plus_Expression, gen_myDsl_Minus_Expression, gen_myDsl_MulOrDiv_Expression, gen_myDsl_Not_Expression, gen_myDsl_BoolConstant_Expression, gen_myDsl_VariableConstant_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)