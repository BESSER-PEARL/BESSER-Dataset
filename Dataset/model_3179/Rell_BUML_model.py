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
rell_Model = Class(name="rell::Model")
rell_ClassDefinition = Class(name="rell::ClassDefinition")
rell_Operation = Class(name="rell::Operation")
rell_Attribute = Class(name="rell::Attribute")
rell_RelAttrubutesList = Class(name="rell::RelAttrubutesList")
rell_VariableDeclaration = Class(name="rell::VariableDeclaration")
rell_Expression = Class(name="rell::Expression")
rell_Relational = Class(name="rell::Relational")
rell_Conditions = Class(name="rell::Conditions")
rell_Update = Class(name="rell::Update")
Relational = Class(name="Relational")
rell_VariableInit = Class(name="rell::VariableInit")
rell_Delete = Class(name="rell::Delete")
rell_Create = Class(name="rell::Create")
rell_Statement = Class(name="rell::Statement")
rell_Variable = Class(name="rell::Variable")
Statement = Class(name="Statement")
rell_ConditionElement = Class(name="rell::ConditionElement")
rell_TypeReference = Class(name="rell::TypeReference")
rell_PrimitiveType = Class(name="rell::PrimitiveType")
rell_ClassType = Class(name="rell::ClassType")
rell_And = Class(name="rell::And")
rell_Equality = Class(name="rell::Equality")
rell_Or = Class(name="rell::Or")
Expression = Class(name="Expression")
rell_Comparison = Class(name="rell::Comparison")
rell_Plus = Class(name="rell::Plus")
rell_IntConstant = Class(name="rell::IntConstant")
rell_StringConstant = Class(name="rell::StringConstant")
rell_BoolConstant = Class(name="rell::BoolConstant")
rell_VariableRef = Class(name="rell::VariableRef")
rell_Minus = Class(name="rell::Minus")
rell_Not = Class(name="rell::Not")
rell_MulOrDiv = Class(name="rell::MulOrDiv")

# rell_Model class attributes and methods

# rell_ClassDefinition class attributes and methods
rell_ClassDefinition_name: Property = Property(name="name", type=StringType)
rell_ClassDefinition.attributes={rell_ClassDefinition_name}

# rell_Operation class attributes and methods
rell_Operation_name: Property = Property(name="name", type=StringType)
rell_Operation.attributes={rell_Operation_name}

# rell_Attribute class attributes and methods
rell_Attribute_modificator: Property = Property(name="modificator", type=StringType)
rell_Attribute.attributes={rell_Attribute_modificator}

# rell_RelAttrubutesList class attributes and methods

# rell_VariableDeclaration class attributes and methods
rell_VariableDeclaration_name: Property = Property(name="name", type=StringType)
rell_VariableDeclaration.attributes={rell_VariableDeclaration_name}

# rell_Expression class attributes and methods

# rell_Relational class attributes and methods
rell_Relational_entity: Property = Property(name="entity", type=StringType)
rell_Relational.attributes={rell_Relational_entity}

# rell_Conditions class attributes and methods

# rell_Update class attributes and methods

# Relational class attributes and methods

# rell_VariableInit class attributes and methods

# rell_Delete class attributes and methods

# rell_Create class attributes and methods

# rell_Statement class attributes and methods

# rell_Variable class attributes and methods

# Statement class attributes and methods

# rell_ConditionElement class attributes and methods
rell_ConditionElement_compareName: Property = Property(name="compareName", type=StringType)
rell_ConditionElement.attributes={rell_ConditionElement_compareName}

# rell_TypeReference class attributes and methods

# rell_PrimitiveType class attributes and methods
rell_PrimitiveType_primitiveType: Property = Property(name="primitiveType", type=StringType)
rell_PrimitiveType.attributes={rell_PrimitiveType_primitiveType}

# rell_ClassType class attributes and methods

# rell_And class attributes and methods

# rell_Equality class attributes and methods
rell_Equality_op: Property = Property(name="op", type=StringType)
rell_Equality.attributes={rell_Equality_op}

# rell_Or class attributes and methods

# Expression class attributes and methods

# rell_Comparison class attributes and methods
rell_Comparison_op: Property = Property(name="op", type=StringType)
rell_Comparison.attributes={rell_Comparison_op}

# rell_Plus class attributes and methods

# rell_IntConstant class attributes and methods
rell_IntConstant_value: Property = Property(name="value", type=IntegerType)
rell_IntConstant.attributes={rell_IntConstant_value}

# rell_StringConstant class attributes and methods
rell_StringConstant_value: Property = Property(name="value", type=StringType)
rell_StringConstant.attributes={rell_StringConstant_value}

# rell_BoolConstant class attributes and methods
rell_BoolConstant_value: Property = Property(name="value", type=StringType)
rell_BoolConstant.attributes={rell_BoolConstant_value}

# rell_VariableRef class attributes and methods

# rell_Minus class attributes and methods

# rell_Not class attributes and methods

# rell_MulOrDiv class attributes and methods
rell_MulOrDiv_op: Property = Property(name="op", type=StringType)
rell_MulOrDiv.attributes={rell_MulOrDiv_op}

# Relationships
entities0: BinaryAssociation = BinaryAssociation(
    name="entities0",
    ends={
        Property(name="rell_ClassDefinition", type=rell_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Model", type=rell_ClassDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations1: BinaryAssociation = BinaryAssociation(
    name="operations1",
    ends={
        Property(name="rell_Operation", type=rell_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Model2", type=rell_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType4: BinaryAssociation = BinaryAssociation(
    name="superType4",
    ends={
        Property(name="rell_ClassDefinition5", type=rell_ClassDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_ClassDefinition3", type=rell_ClassDefinition, multiplicity=Multiplicity(0, 1))
    }
)
attributes6: BinaryAssociation = BinaryAssociation(
    name="attributes6",
    ends={
        Property(name="rell_Attribute", type=rell_ClassDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_ClassDefinition7", type=rell_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters8: BinaryAssociation = BinaryAssociation(
    name="parameters8",
    ends={
        Property(name="rell_RelAttrubutesList", type=rell_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Operation9", type=rell_RelAttrubutesList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable13: BinaryAssociation = BinaryAssociation(
    name="variable13",
    ends={
        Property(name="rell_Variable", type=rell_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Variable12", type=rell_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration14: BinaryAssociation = BinaryAssociation(
    name="declaration14",
    ends={
        Property(name="rell_VariableDeclaration", type=rell_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Variable15", type=rell_VariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression16: BinaryAssociation = BinaryAssociation(
    name="expression16",
    ends={
        Property(name="rell_Expression", type=rell_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Variable17", type=rell_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relation19: BinaryAssociation = BinaryAssociation(
    name="relation19",
    ends={
        Property(name="rell_Relational", type=rell_Relational, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Relational18", type=rell_Relational, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
conditions20: BinaryAssociation = BinaryAssociation(
    name="conditions20",
    ends={
        Property(name="rell_Conditions", type=rell_Relational, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Relational21", type=rell_Conditions, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableList22: BinaryAssociation = BinaryAssociation(
    name="variableList22",
    ends={
        Property(name="rell_VariableInit", type=rell_Update, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Update", type=rell_VariableInit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements10: BinaryAssociation = BinaryAssociation(
    name="statements10",
    ends={
        Property(name="rell_Statement", type=rell_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Operation11", type=rell_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr25: BinaryAssociation = BinaryAssociation(
    name="expr25",
    ends={
        Property(name="rell_Expression27", type=rell_ConditionElement, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_ConditionElement26", type=rell_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varInit29: BinaryAssociation = BinaryAssociation(
    name="varInit29",
    ends={
        Property(name="rell_VariableInit30", type=rell_VariableInit, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_VariableInit28", type=rell_VariableInit, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name31: BinaryAssociation = BinaryAssociation(
    name="name31",
    ends={
        Property(name="rell_VariableDeclaration33", type=rell_VariableInit, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_VariableInit32", type=rell_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
expression34: BinaryAssociation = BinaryAssociation(
    name="expression34",
    ends={
        Property(name="rell_Expression36", type=rell_VariableInit, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_VariableInit35", type=rell_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
or38: BinaryAssociation = BinaryAssociation(
    name="or38",
    ends={
        Property(name="rell_Expression39", type=rell_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Expression37", type=rell_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value40: BinaryAssociation = BinaryAssociation(
    name="value40",
    ends={
        Property(name="rell_VariableDeclaration42", type=rell_RelAttrubutesList, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_RelAttrubutesList41", type=rell_VariableDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements23: BinaryAssociation = BinaryAssociation(
    name="elements23",
    ends={
        Property(name="rell_ConditionElement", type=rell_Conditions, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Conditions24", type=rell_ConditionElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type46: BinaryAssociation = BinaryAssociation(
    name="type46",
    ends={
        Property(name="rell_TypeReference", type=rell_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_VariableDeclaration47", type=rell_TypeReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primitive48: BinaryAssociation = BinaryAssociation(
    name="primitive48",
    ends={
        Property(name="rell_PrimitiveType", type=rell_TypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_TypeReference49", type=rell_PrimitiveType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entityType50: BinaryAssociation = BinaryAssociation(
    name="entityType50",
    ends={
        Property(name="rell_ClassType", type=rell_TypeReference, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_TypeReference51", type=rell_ClassType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable43: BinaryAssociation = BinaryAssociation(
    name="variable43",
    ends={
        Property(name="rell_VariableDeclaration45", type=rell_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Attribute44", type=rell_VariableDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left55: BinaryAssociation = BinaryAssociation(
    name="left55",
    ends={
        Property(name="rell_Expression56", type=rell_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Or", type=rell_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right57: BinaryAssociation = BinaryAssociation(
    name="right57",
    ends={
        Property(name="rell_Expression59", type=rell_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Or58", type=rell_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left60: BinaryAssociation = BinaryAssociation(
    name="left60",
    ends={
        Property(name="rell_Expression61", type=rell_And, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_And", type=rell_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right62: BinaryAssociation = BinaryAssociation(
    name="right62",
    ends={
        Property(name="rell_Expression64", type=rell_And, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_And63", type=rell_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left65: BinaryAssociation = BinaryAssociation(
    name="left65",
    ends={
        Property(name="rell_Expression66", type=rell_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Equality", type=rell_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entityRef52: BinaryAssociation = BinaryAssociation(
    name="entityRef52",
    ends={
        Property(name="rell_ClassDefinition54", type=rell_ClassType, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_ClassType53", type=rell_ClassDefinition, multiplicity=Multiplicity(0, 1))
    }
)
left70: BinaryAssociation = BinaryAssociation(
    name="left70",
    ends={
        Property(name="rell_Expression71", type=rell_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Comparison", type=rell_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right72: BinaryAssociation = BinaryAssociation(
    name="right72",
    ends={
        Property(name="rell_Expression74", type=rell_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Comparison73", type=rell_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left75: BinaryAssociation = BinaryAssociation(
    name="left75",
    ends={
        Property(name="rell_Expression76", type=rell_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Plus", type=rell_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right77: BinaryAssociation = BinaryAssociation(
    name="right77",
    ends={
        Property(name="rell_Expression79", type=rell_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Plus78", type=rell_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right67: BinaryAssociation = BinaryAssociation(
    name="right67",
    ends={
        Property(name="rell_Expression69", type=rell_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Equality68", type=rell_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left80: BinaryAssociation = BinaryAssociation(
    name="left80",
    ends={
        Property(name="rell_Expression81", type=rell_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Minus", type=rell_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right82: BinaryAssociation = BinaryAssociation(
    name="right82",
    ends={
        Property(name="rell_Expression84", type=rell_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Minus83", type=rell_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left87: BinaryAssociation = BinaryAssociation(
    name="left87",
    ends={
        Property(name="rell_Expression88", type=rell_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_MulOrDiv", type=rell_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right89: BinaryAssociation = BinaryAssociation(
    name="right89",
    ends={
        Property(name="rell_Expression91", type=rell_MulOrDiv, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_MulOrDiv90", type=rell_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression92: BinaryAssociation = BinaryAssociation(
    name="expression92",
    ends={
        Property(name="rell_Expression93", type=rell_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_Not", type=rell_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable85: BinaryAssociation = BinaryAssociation(
    name="variable85",
    ends={
        Property(name="rell_VariableDeclaration86", type=rell_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="rell_VariableRef", type=rell_VariableDeclaration, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_rell_Relational_Statement = Generalization(general=Statement, specific=rell_Relational)
gen_rell_Update_Relational = Generalization(general=Relational, specific=rell_Update)
gen_rell_Delete_Relational = Generalization(general=Relational, specific=rell_Delete)
gen_rell_Create_Relational = Generalization(general=Relational, specific=rell_Create)
gen_rell_Variable_Statement = Generalization(general=Statement, specific=rell_Variable)
gen_rell_VariableInit_Statement = Generalization(general=Statement, specific=rell_VariableInit)
gen_rell_And_Expression = Generalization(general=Expression, specific=rell_And)
gen_rell_Equality_Expression = Generalization(general=Expression, specific=rell_Equality)
gen_rell_Or_Expression = Generalization(general=Expression, specific=rell_Or)
gen_rell_Comparison_Expression = Generalization(general=Expression, specific=rell_Comparison)
gen_rell_Plus_Expression = Generalization(general=Expression, specific=rell_Plus)
gen_rell_IntConstant_Expression = Generalization(general=Expression, specific=rell_IntConstant)
gen_rell_StringConstant_Expression = Generalization(general=Expression, specific=rell_StringConstant)
gen_rell_BoolConstant_Expression = Generalization(general=Expression, specific=rell_BoolConstant)
gen_rell_VariableRef_Expression = Generalization(general=Expression, specific=rell_VariableRef)
gen_rell_Minus_Expression = Generalization(general=Expression, specific=rell_Minus)
gen_rell_Not_Expression = Generalization(general=Expression, specific=rell_Not)
gen_rell_MulOrDiv_Expression = Generalization(general=Expression, specific=rell_MulOrDiv)

# Domain Model
domain_model = DomainModel(
    name="rell",
    types={rell_Model, rell_ClassDefinition, rell_Operation, rell_Attribute, rell_RelAttrubutesList, rell_VariableDeclaration, rell_Expression, rell_Relational, rell_Conditions, rell_Update, Relational, rell_VariableInit, rell_Delete, rell_Create, rell_Statement, rell_Variable, Statement, rell_ConditionElement, rell_TypeReference, rell_PrimitiveType, rell_ClassType, rell_And, rell_Equality, rell_Or, Expression, rell_Comparison, rell_Plus, rell_IntConstant, rell_StringConstant, rell_BoolConstant, rell_VariableRef, rell_Minus, rell_Not, rell_MulOrDiv},
    associations={entities0, operations1, superType4, attributes6, parameters8, variable13, declaration14, expression16, relation19, conditions20, variableList22, statements10, expr25, varInit29, name31, expression34, or38, value40, elements23, type46, primitive48, entityType50, variable43, left55, right57, left60, right62, left65, entityRef52, left70, right72, left75, right77, right67, left80, right82, left87, right89, expression92, variable85},
    generalizations={gen_rell_Relational_Statement, gen_rell_Update_Relational, gen_rell_Delete_Relational, gen_rell_Create_Relational, gen_rell_Variable_Statement, gen_rell_VariableInit_Statement, gen_rell_And_Expression, gen_rell_Equality_Expression, gen_rell_Or_Expression, gen_rell_Comparison_Expression, gen_rell_Plus_Expression, gen_rell_IntConstant_Expression, gen_rell_StringConstant_Expression, gen_rell_BoolConstant_Expression, gen_rell_VariableRef_Expression, gen_rell_Minus_Expression, gen_rell_Not_Expression, gen_rell_MulOrDiv_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)