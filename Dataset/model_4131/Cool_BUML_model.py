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
cool_Program = Class(name="cool::Program")
cool_Class_ = Class(name="cool::Class::")
Type = Class(name="Type")
IdentifiableElement = Class(name="IdentifiableElement")
cool_PrimaryExpression = Class(name="cool::PrimaryExpression")
Expression = Class(name="Expression")
cool_SelfTypeLiteral = Class(name="cool::SelfTypeLiteral")
PrimaryExpression = Class(name="PrimaryExpression")
cool_IdentifierRefExpression = Class(name="cool::IdentifierRefExpression")
cool_IdentifiableElement = Class(name="cool::IdentifiableElement")
cool_Literal = Class(name="cool::Literal")
cool_NumberLiteral = Class(name="cool::NumberLiteral")
Literal = Class(name="Literal")
cool_StringLiteral = Class(name="cool::StringLiteral")
cool_BooleanLiteral = Class(name="cool::BooleanLiteral")
cool_Type = Class(name="cool::Type")
cool_Feature_ = Class(name="cool::Feature::")
cool_Attr = Class(name="cool::Attr")
Feature_ = Class(name="Feature::")
cool_Expression = Class(name="cool::Expression")
cool_Method = Class(name="cool::Method")
cool_Formal = Class(name="cool::Formal")
cool_DispatchExpression = Class(name="cool::DispatchExpression")
cool_ConditionalExpression = Class(name="cool::ConditionalExpression")
cool_LoopExpression = Class(name="cool::LoopExpression")
cool_ParenExpression = Class(name="cool::ParenExpression")
cool_AssignmentExpression = Class(name="cool::AssignmentExpression")
cool_NegationExpression = Class(name="cool::NegationExpression")
cool_IntegerCompositeExpression = Class(name="cool::IntegerCompositeExpression")
cool_NewExpression = Class(name="cool::NewExpression")
cool_CaseExpression = Class(name="cool::CaseExpression")
cool_Case = Class(name="cool::Case")
cool_BlockExpression = Class(name="cool::BlockExpression")
cool_IsvoidExpression = Class(name="cool::IsvoidExpression")
cool_LetExpression = Class(name="cool::LetExpression")
cool_LetDeclaration = Class(name="cool::LetDeclaration")
cool_MultiplicationExpression = Class(name="cool::MultiplicationExpression")
cool_Div = Class(name="cool::Div")
cool_CompareExpression = Class(name="cool::CompareExpression")
cool_AdditionExpression = Class(name="cool::AdditionExpression")
cool_Minus = Class(name="cool::Minus")

# cool_Program class attributes and methods

# cool_Class_ class attributes and methods

# Type class attributes and methods

# IdentifiableElement class attributes and methods

# cool_PrimaryExpression class attributes and methods

# Expression class attributes and methods

# cool_SelfTypeLiteral class attributes and methods

# PrimaryExpression class attributes and methods

# cool_IdentifierRefExpression class attributes and methods

# cool_IdentifiableElement class attributes and methods
cool_IdentifiableElement_name: Property = Property(name="name", type=StringType)
cool_IdentifiableElement.attributes={cool_IdentifiableElement_name}

# cool_Literal class attributes and methods

# cool_NumberLiteral class attributes and methods
cool_NumberLiteral_value: Property = Property(name="value", type=IntegerType)
cool_NumberLiteral.attributes={cool_NumberLiteral_value}

# Literal class attributes and methods

# cool_StringLiteral class attributes and methods
cool_StringLiteral_value: Property = Property(name="value", type=StringType)
cool_StringLiteral.attributes={cool_StringLiteral_value}

# cool_BooleanLiteral class attributes and methods
cool_BooleanLiteral_value: Property = Property(name="value", type=StringType)
cool_BooleanLiteral.attributes={cool_BooleanLiteral_value}

# cool_Type class attributes and methods

# cool_Feature_ class attributes and methods

# cool_Attr class attributes and methods

# Feature_ class attributes and methods

# cool_Expression class attributes and methods

# cool_Method class attributes and methods

# cool_Formal class attributes and methods

# cool_DispatchExpression class attributes and methods

# cool_ConditionalExpression class attributes and methods

# cool_LoopExpression class attributes and methods

# cool_ParenExpression class attributes and methods

# cool_AssignmentExpression class attributes and methods
cool_AssignmentExpression_name: Property = Property(name="name", type=StringType)
cool_AssignmentExpression.attributes={cool_AssignmentExpression_name}

# cool_NegationExpression class attributes and methods

# cool_IntegerCompositeExpression class attributes and methods

# cool_NewExpression class attributes and methods

# cool_CaseExpression class attributes and methods

# cool_Case class attributes and methods

# cool_BlockExpression class attributes and methods

# cool_IsvoidExpression class attributes and methods

# cool_LetExpression class attributes and methods

# cool_LetDeclaration class attributes and methods

# cool_MultiplicationExpression class attributes and methods

# cool_Div class attributes and methods

# cool_CompareExpression class attributes and methods
cool_CompareExpression_op: Property = Property(name="op", type=StringType)
cool_CompareExpression.attributes={cool_CompareExpression_op}

# cool_AdditionExpression class attributes and methods

# cool_Minus class attributes and methods

# Relationships
classes0: BinaryAssociation = BinaryAssociation(
    name="classes0",
    ends={
        Property(name="cool_Class_", type=cool_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_Program", type=cool_Class_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr13: BinaryAssociation = BinaryAssociation(
    name="expr13",
    ends={
        Property(name="cool_Expression15", type=cool_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_Method14", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_decl16: BinaryAssociation = BinaryAssociation(
    name="type_decl16",
    ends={
        Property(name="cool_Type18", type=cool_Formal, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_Formal17", type=cool_Type, multiplicity=Multiplicity(0, 1))
    }
)
id19: BinaryAssociation = BinaryAssociation(
    name="id19",
    ends={
        Property(name="cool_IdentifiableElement", type=cool_IdentifierRefExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_IdentifierRefExpression", type=cool_IdentifiableElement, multiplicity=Multiplicity(0, 1))
    }
)
parent1: BinaryAssociation = BinaryAssociation(
    name="parent1",
    ends={
        Property(name="cool_Type", type=cool_Class_, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_Class_2", type=cool_Type, multiplicity=Multiplicity(0, 1))
    }
)
features3: BinaryAssociation = BinaryAssociation(
    name="features3",
    ends={
        Property(name="cool_Feature_", type=cool_Class_, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_Class_4", type=cool_Feature_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type_decl5: BinaryAssociation = BinaryAssociation(
    name="type_decl5",
    ends={
        Property(name="cool_Type6", type=cool_Attr, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_Attr", type=cool_Type, multiplicity=Multiplicity(0, 1))
    }
)
init7: BinaryAssociation = BinaryAssociation(
    name="init7",
    ends={
        Property(name="cool_Expression", type=cool_Attr, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_Attr8", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formals9: BinaryAssociation = BinaryAssociation(
    name="formals9",
    ends={
        Property(name="cool_Formal", type=cool_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_Method", type=cool_Formal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
return_type10: BinaryAssociation = BinaryAssociation(
    name="return_type10",
    ends={
        Property(name="cool_Type12", type=cool_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_Method11", type=cool_Type, multiplicity=Multiplicity(0, 1))
    }
)
ref30: BinaryAssociation = BinaryAssociation(
    name="ref30",
    ends={
        Property(name="cool_IdentifierRefExpression31", type=cool_DispatchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_DispatchExpression", type=cool_IdentifierRefExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actual32: BinaryAssociation = BinaryAssociation(
    name="actual32",
    ends={
        Property(name="cool_Expression34", type=cool_DispatchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_DispatchExpression33", type=cool_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
chain36: BinaryAssociation = BinaryAssociation(
    name="chain36",
    ends={
        Property(name="cool_DispatchExpression37", type=cool_DispatchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_DispatchExpression35", type=cool_DispatchExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left38: BinaryAssociation = BinaryAssociation(
    name="left38",
    ends={
        Property(name="cool_PrimaryExpression", type=cool_DispatchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_DispatchExpression39", type=cool_PrimaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_name40: BinaryAssociation = BinaryAssociation(
    name="type_name40",
    ends={
        Property(name="cool_Type42", type=cool_DispatchExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_DispatchExpression41", type=cool_Type, multiplicity=Multiplicity(0, 1))
    }
)
pred43: BinaryAssociation = BinaryAssociation(
    name="pred43",
    ends={
        Property(name="cool_Expression44", type=cool_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_ConditionalExpression", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then_exp45: BinaryAssociation = BinaryAssociation(
    name="then_exp45",
    ends={
        Property(name="cool_Expression47", type=cool_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_ConditionalExpression46", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else_exp48: BinaryAssociation = BinaryAssociation(
    name="else_exp48",
    ends={
        Property(name="cool_Expression50", type=cool_ConditionalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_ConditionalExpression49", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr20: BinaryAssociation = BinaryAssociation(
    name="expr20",
    ends={
        Property(name="cool_Expression21", type=cool_ParenExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_ParenExpression", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr22: BinaryAssociation = BinaryAssociation(
    name="expr22",
    ends={
        Property(name="cool_Expression23", type=cool_AssignmentExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_AssignmentExpression", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr24: BinaryAssociation = BinaryAssociation(
    name="expr24",
    ends={
        Property(name="cool_Expression25", type=cool_NegationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_NegationExpression", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr26: BinaryAssociation = BinaryAssociation(
    name="expr26",
    ends={
        Property(name="cool_Expression27", type=cool_IntegerCompositeExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_IntegerCompositeExpression", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_name28: BinaryAssociation = BinaryAssociation(
    name="type_name28",
    ends={
        Property(name="cool_Type29", type=cool_NewExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_NewExpression", type=cool_Type, multiplicity=Multiplicity(0, 1))
    }
)
body61: BinaryAssociation = BinaryAssociation(
    name="body61",
    ends={
        Property(name="cool_Expression63", type=cool_LetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_LetExpression62", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_decl64: BinaryAssociation = BinaryAssociation(
    name="type_decl64",
    ends={
        Property(name="cool_Type66", type=cool_LetDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_LetDeclaration65", type=cool_Type, multiplicity=Multiplicity(0, 1))
    }
)
init67: BinaryAssociation = BinaryAssociation(
    name="init67",
    ends={
        Property(name="cool_Expression69", type=cool_LetDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_LetDeclaration68", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expr70: BinaryAssociation = BinaryAssociation(
    name="expr70",
    ends={
        Property(name="cool_Expression71", type=cool_CaseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_CaseExpression", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
case72: BinaryAssociation = BinaryAssociation(
    name="case72",
    ends={
        Property(name="cool_Case", type=cool_CaseExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_CaseExpression73", type=cool_Case, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type_decl74: BinaryAssociation = BinaryAssociation(
    name="type_decl74",
    ends={
        Property(name="cool_Type76", type=cool_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_Case75", type=cool_Type, multiplicity=Multiplicity(0, 1))
    }
)
expr77: BinaryAssociation = BinaryAssociation(
    name="expr77",
    ends={
        Property(name="cool_Expression79", type=cool_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_Case78", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pred51: BinaryAssociation = BinaryAssociation(
    name="pred51",
    ends={
        Property(name="cool_Expression52", type=cool_LoopExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_LoopExpression", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body53: BinaryAssociation = BinaryAssociation(
    name="body53",
    ends={
        Property(name="cool_Expression55", type=cool_LoopExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_LoopExpression54", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body56: BinaryAssociation = BinaryAssociation(
    name="body56",
    ends={
        Property(name="cool_Expression57", type=cool_BlockExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_BlockExpression", type=cool_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expr58: BinaryAssociation = BinaryAssociation(
    name="expr58",
    ends={
        Property(name="cool_Expression59", type=cool_IsvoidExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_IsvoidExpression", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration60: BinaryAssociation = BinaryAssociation(
    name="declaration60",
    ends={
        Property(name="cool_LetDeclaration", type=cool_LetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_LetExpression", type=cool_LetDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
right92: BinaryAssociation = BinaryAssociation(
    name="right92",
    ends={
        Property(name="cool_Expression94", type=cool_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_Minus93", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left95: BinaryAssociation = BinaryAssociation(
    name="left95",
    ends={
        Property(name="cool_Expression96", type=cool_MultiplicationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_MultiplicationExpression", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right97: BinaryAssociation = BinaryAssociation(
    name="right97",
    ends={
        Property(name="cool_Expression99", type=cool_MultiplicationExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_MultiplicationExpression98", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op100: BinaryAssociation = BinaryAssociation(
    name="op100",
    ends={
        Property(name="cool_Expression101", type=cool_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_Div", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right102: BinaryAssociation = BinaryAssociation(
    name="right102",
    ends={
        Property(name="cool_Expression104", type=cool_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_Div103", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left80: BinaryAssociation = BinaryAssociation(
    name="left80",
    ends={
        Property(name="cool_Expression81", type=cool_CompareExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_CompareExpression", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right82: BinaryAssociation = BinaryAssociation(
    name="right82",
    ends={
        Property(name="cool_Expression84", type=cool_CompareExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_CompareExpression83", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left85: BinaryAssociation = BinaryAssociation(
    name="left85",
    ends={
        Property(name="cool_Expression86", type=cool_AdditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_AdditionExpression", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right87: BinaryAssociation = BinaryAssociation(
    name="right87",
    ends={
        Property(name="cool_Expression89", type=cool_AdditionExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_AdditionExpression88", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op90: BinaryAssociation = BinaryAssociation(
    name="op90",
    ends={
        Property(name="cool_Expression91", type=cool_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="cool_Minus", type=cool_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_cool_Class__Type = Generalization(general=Type, specific=cool_Class_)
gen_cool_Formal_IdentifiableElement = Generalization(general=IdentifiableElement, specific=cool_Formal)
gen_cool_PrimaryExpression_Expression = Generalization(general=Expression, specific=cool_PrimaryExpression)
gen_cool_SelfTypeLiteral_PrimaryExpression = Generalization(general=PrimaryExpression, specific=cool_SelfTypeLiteral)
gen_cool_IdentifierRefExpression_PrimaryExpression = Generalization(general=PrimaryExpression, specific=cool_IdentifierRefExpression)
gen_cool_Literal_PrimaryExpression = Generalization(general=PrimaryExpression, specific=cool_Literal)
gen_cool_NumberLiteral_Literal = Generalization(general=Literal, specific=cool_NumberLiteral)
gen_cool_StringLiteral_Literal = Generalization(general=Literal, specific=cool_StringLiteral)
gen_cool_BooleanLiteral_Literal = Generalization(general=Literal, specific=cool_BooleanLiteral)
gen_cool_Class__IdentifiableElement = Generalization(general=IdentifiableElement, specific=cool_Class_)
gen_cool_Feature__IdentifiableElement = Generalization(general=IdentifiableElement, specific=cool_Feature_)
gen_cool_Attr_Feature_ = Generalization(general=Feature_, specific=cool_Attr)
gen_cool_Method_Feature_ = Generalization(general=Feature_, specific=cool_Method)
gen_cool_DispatchExpression_PrimaryExpression = Generalization(general=PrimaryExpression, specific=cool_DispatchExpression)
gen_cool_ConditionalExpression_PrimaryExpression = Generalization(general=PrimaryExpression, specific=cool_ConditionalExpression)
gen_cool_LoopExpression_PrimaryExpression = Generalization(general=PrimaryExpression, specific=cool_LoopExpression)
gen_cool_ParenExpression_PrimaryExpression = Generalization(general=PrimaryExpression, specific=cool_ParenExpression)
gen_cool_AssignmentExpression_PrimaryExpression = Generalization(general=PrimaryExpression, specific=cool_AssignmentExpression)
gen_cool_NegationExpression_PrimaryExpression = Generalization(general=PrimaryExpression, specific=cool_NegationExpression)
gen_cool_IntegerCompositeExpression_PrimaryExpression = Generalization(general=PrimaryExpression, specific=cool_IntegerCompositeExpression)
gen_cool_NewExpression_PrimaryExpression = Generalization(general=PrimaryExpression, specific=cool_NewExpression)
gen_cool_LetDeclaration_IdentifiableElement = Generalization(general=IdentifiableElement, specific=cool_LetDeclaration)
gen_cool_CaseExpression_PrimaryExpression = Generalization(general=PrimaryExpression, specific=cool_CaseExpression)
gen_cool_Case_IdentifiableElement = Generalization(general=IdentifiableElement, specific=cool_Case)
gen_cool_BlockExpression_PrimaryExpression = Generalization(general=PrimaryExpression, specific=cool_BlockExpression)
gen_cool_IsvoidExpression_PrimaryExpression = Generalization(general=PrimaryExpression, specific=cool_IsvoidExpression)
gen_cool_LetExpression_PrimaryExpression = Generalization(general=PrimaryExpression, specific=cool_LetExpression)
gen_cool_MultiplicationExpression_Expression = Generalization(general=Expression, specific=cool_MultiplicationExpression)
gen_cool_Div_Expression = Generalization(general=Expression, specific=cool_Div)
gen_cool_CompareExpression_Expression = Generalization(general=Expression, specific=cool_CompareExpression)
gen_cool_AdditionExpression_Expression = Generalization(general=Expression, specific=cool_AdditionExpression)
gen_cool_Minus_Expression = Generalization(general=Expression, specific=cool_Minus)

# Domain Model
domain_model = DomainModel(
    name="cool",
    types={cool_Program, cool_Class_, Type, IdentifiableElement, cool_PrimaryExpression, Expression, cool_SelfTypeLiteral, PrimaryExpression, cool_IdentifierRefExpression, cool_IdentifiableElement, cool_Literal, cool_NumberLiteral, Literal, cool_StringLiteral, cool_BooleanLiteral, cool_Type, cool_Feature_, cool_Attr, Feature_, cool_Expression, cool_Method, cool_Formal, cool_DispatchExpression, cool_ConditionalExpression, cool_LoopExpression, cool_ParenExpression, cool_AssignmentExpression, cool_NegationExpression, cool_IntegerCompositeExpression, cool_NewExpression, cool_CaseExpression, cool_Case, cool_BlockExpression, cool_IsvoidExpression, cool_LetExpression, cool_LetDeclaration, cool_MultiplicationExpression, cool_Div, cool_CompareExpression, cool_AdditionExpression, cool_Minus},
    associations={classes0, expr13, type_decl16, id19, parent1, features3, type_decl5, init7, formals9, return_type10, ref30, actual32, chain36, left38, type_name40, pred43, then_exp45, else_exp48, expr20, expr22, expr24, expr26, type_name28, body61, type_decl64, init67, expr70, case72, type_decl74, expr77, pred51, body53, body56, expr58, declaration60, right92, left95, right97, op100, right102, left80, right82, left85, right87, op90},
    generalizations={gen_cool_Class__Type, gen_cool_Formal_IdentifiableElement, gen_cool_PrimaryExpression_Expression, gen_cool_SelfTypeLiteral_PrimaryExpression, gen_cool_IdentifierRefExpression_PrimaryExpression, gen_cool_Literal_PrimaryExpression, gen_cool_NumberLiteral_Literal, gen_cool_StringLiteral_Literal, gen_cool_BooleanLiteral_Literal, gen_cool_Class__IdentifiableElement, gen_cool_Feature__IdentifiableElement, gen_cool_Attr_Feature_, gen_cool_Method_Feature_, gen_cool_DispatchExpression_PrimaryExpression, gen_cool_ConditionalExpression_PrimaryExpression, gen_cool_LoopExpression_PrimaryExpression, gen_cool_ParenExpression_PrimaryExpression, gen_cool_AssignmentExpression_PrimaryExpression, gen_cool_NegationExpression_PrimaryExpression, gen_cool_IntegerCompositeExpression_PrimaryExpression, gen_cool_NewExpression_PrimaryExpression, gen_cool_LetDeclaration_IdentifiableElement, gen_cool_CaseExpression_PrimaryExpression, gen_cool_Case_IdentifiableElement, gen_cool_BlockExpression_PrimaryExpression, gen_cool_IsvoidExpression_PrimaryExpression, gen_cool_LetExpression_PrimaryExpression, gen_cool_MultiplicationExpression_Expression, gen_cool_Div_Expression, gen_cool_CompareExpression_Expression, gen_cool_AdditionExpression_Expression, gen_cool_Minus_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)