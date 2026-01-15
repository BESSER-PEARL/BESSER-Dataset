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
go_Go = Class(name="go::Go")
go_Greeting = Class(name="go::Greeting")
Greeting = Class(name="Greeting")
go_Atrib = Class(name="go::Atrib")
go_AtribVar = Class(name="go::AtribVar")
go_ReAtrib = Class(name="go::ReAtrib")
go_Atrib_Aux = Class(name="go::Atrib::Aux")
go_Variable = Class(name="go::Variable")
Atrib_Aux = Class(name="Atrib::Aux")
SwitchCase = Class(name="SwitchCase")
go_Decl = Class(name="go::Decl")
go_DecVar = Class(name="go::DecVar")
OperationsOneEquals = Class(name="OperationsOneEquals")
go_EObject = Class(name="go::EObject")
go_MultDecVars = Class(name="go::MultDecVars")
go_TypeValue = Class(name="go::TypeValue")
operationsOne = Class(name="operationsOne")
Expression = Class(name="Expression")
go_Cases = Class(name="go::Cases")
varFor = Class(name="varFor")
go_Expression = Class(name="go::Expression")
go_Atri = Class(name="go::Atri")
go_Params = Class(name="go::Params")
Atri = Class(name="Atri")
go_Str = Class(name="go::Str")
TypeValue = Class(name="TypeValue")
go_OperationsOneEquals = Class(name="go::OperationsOneEquals")
go_Numbers = Class(name="go::Numbers")
F = Class(name="F")
go_DecVars = Class(name="go::DecVars")
go_SwitchCase = Class(name="go::SwitchCase")
go_Operations = Class(name="go::Operations")
go_I = Class(name="go::I")
go_T = Class(name="go::T")
Operations = Class(name="Operations")
I = Class(name="I")
go_Y = Class(name="go::Y")
go_F = Class(name="go::F")
T = Class(name="T")
go_Condition = Class(name="go::Condition")
go_IfCondition = Class(name="go::IfCondition")
go_Intg = Class(name="go::Intg")
go_Double = Class(name="go::Double")
ElseIfCondition = Class(name="ElseIfCondition")
go_ElseIfCondition = Class(name="go::ElseIfCondition")
go_ElseCondition = Class(name="go::ElseCondition")
go_DecFunc = Class(name="go::DecFunc")
go_FunctionBody = Class(name="go::FunctionBody")
go_FunctionReturn = Class(name="go::FunctionReturn")
go_CallFor = Class(name="go::CallFor")
go_operationsOne = Class(name="go::operationsOne")
go_varFor = Class(name="go::varFor")
CallFor = Class(name="CallFor")
go_Bool = Class(name="go::Bool")
go_DataType = Class(name="go::DataType")
go_Addition = Class(name="go::Addition")
go_Subtration = Class(name="go::Subtration")
go_Multiplication = Class(name="go::Multiplication")
go_CallFunc = Class(name="go::CallFunc")
go_Division = Class(name="go::Division")
go_OrExpression = Class(name="go::OrExpression")
go_AndExpression = Class(name="go::AndExpression")
go_ComparisonExpression = Class(name="go::ComparisonExpression")
go_Literal = Class(name="go::Literal")

# go_Go class attributes and methods

# go_Greeting class attributes and methods

# Greeting class attributes and methods

# go_Atrib class attributes and methods
go_Atrib_name: Property = Property(name="name", type=StringType)
go_Atrib_type: Property = Property(name="type", type=StringType)
go_Atrib_modifier: Property = Property(name="modifier", type=StringType)
go_Atrib.attributes={go_Atrib_name, go_Atrib_type, go_Atrib_modifier}

# go_AtribVar class attributes and methods
go_AtribVar_vars: Property = Property(name="vars", type=StringType)
go_AtribVar_type: Property = Property(name="type", type=StringType)
go_AtribVar.attributes={go_AtribVar_type, go_AtribVar_vars}

# go_ReAtrib class attributes and methods
go_ReAtrib_name: Property = Property(name="name", type=StringType)
go_ReAtrib.attributes={go_ReAtrib_name}

# go_Atrib_Aux class attributes and methods

# go_Variable class attributes and methods
go_Variable_name: Property = Property(name="name", type=StringType)
go_Variable.attributes={go_Variable_name}

# Atrib_Aux class attributes and methods

# SwitchCase class attributes and methods

# go_Decl class attributes and methods
go_Decl_name: Property = Property(name="name", type=StringType)
go_Decl_type: Property = Property(name="type", type=StringType)
go_Decl.attributes={go_Decl_name, go_Decl_type}

# go_DecVar class attributes and methods

# OperationsOneEquals class attributes and methods

# go_EObject class attributes and methods

# go_MultDecVars class attributes and methods
go_MultDecVars_name: Property = Property(name="name", type=StringType)
go_MultDecVars_value: Property = Property(name="value", type=StringType)
go_MultDecVars.attributes={go_MultDecVars_value, go_MultDecVars_name}

# go_TypeValue class attributes and methods

# operationsOne class attributes and methods

# Expression class attributes and methods

# go_Cases class attributes and methods

# varFor class attributes and methods

# go_Expression class attributes and methods

# go_Atri class attributes and methods

# go_Params class attributes and methods
go_Params_params: Property = Property(name="params", type=StringType)
go_Params_type: Property = Property(name="type", type=StringType)
go_Params.attributes={go_Params_params, go_Params_type}

# Atri class attributes and methods

# go_Str class attributes and methods
go_Str_s: Property = Property(name="s", type=StringType)
go_Str.attributes={go_Str_s}

# TypeValue class attributes and methods

# go_OperationsOneEquals class attributes and methods

# go_Numbers class attributes and methods

# F class attributes and methods

# go_DecVars class attributes and methods
go_DecVars_vars: Property = Property(name="vars", type=StringType)
go_DecVars.attributes={go_DecVars_vars}

# go_SwitchCase class attributes and methods

# go_Operations class attributes and methods

# go_I class attributes and methods

# go_T class attributes and methods

# Operations class attributes and methods

# I class attributes and methods

# go_Y class attributes and methods

# go_F class attributes and methods

# T class attributes and methods

# go_Condition class attributes and methods

# go_IfCondition class attributes and methods

# go_Intg class attributes and methods
go_Intg_i: Property = Property(name="i", type=IntegerType)
go_Intg.attributes={go_Intg_i}

# go_Double class attributes and methods
go_Double_d: Property = Property(name="d", type=IntegerType)
go_Double.attributes={go_Double_d}

# ElseIfCondition class attributes and methods

# go_ElseIfCondition class attributes and methods

# go_ElseCondition class attributes and methods

# go_DecFunc class attributes and methods
go_DecFunc_name: Property = Property(name="name", type=StringType)
go_DecFunc_returnType: Property = Property(name="returnType", type=StringType)
go_DecFunc.attributes={go_DecFunc_name, go_DecFunc_returnType}

# go_FunctionBody class attributes and methods

# go_FunctionReturn class attributes and methods

# go_CallFor class attributes and methods

# go_operationsOne class attributes and methods

# go_varFor class attributes and methods

# CallFor class attributes and methods

# go_Bool class attributes and methods
go_Bool_val: Property = Property(name="val", type=StringType)
go_Bool.attributes={go_Bool_val}

# go_DataType class attributes and methods
go_DataType_name: Property = Property(name="name", type=StringType)
go_DataType.attributes={go_DataType_name}

# go_Addition class attributes and methods

# go_Subtration class attributes and methods

# go_Multiplication class attributes and methods

# go_CallFunc class attributes and methods
go_CallFunc_nameFunc: Property = Property(name="nameFunc", type=StringType)
go_CallFunc.attributes={go_CallFunc_nameFunc}

# go_Division class attributes and methods

# go_OrExpression class attributes and methods

# go_AndExpression class attributes and methods

# go_ComparisonExpression class attributes and methods

# go_Literal class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="go_Greeting", type=go_Go, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Go", type=go_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaration1: BinaryAssociation = BinaryAssociation(
    name="declaration1",
    ends={
        Property(name="go_Decl", type=go_DecVar, multiplicity=Multiplicity(1, 1)),
        Property(name="go_DecVar", type=go_Decl, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
atribuicao2: BinaryAssociation = BinaryAssociation(
    name="atribuicao2",
    ends={
        Property(name="go_Atrib", type=go_DecVar, multiplicity=Multiplicity(1, 1)),
        Property(name="go_DecVar3", type=go_Atrib, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment4: BinaryAssociation = BinaryAssociation(
    name="assignment4",
    ends={
        Property(name="go_AtribVar", type=go_DecVar, multiplicity=Multiplicity(1, 1)),
        Property(name="go_DecVar5", type=go_AtribVar, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reassignment6: BinaryAssociation = BinaryAssociation(
    name="reassignment6",
    ends={
        Property(name="go_ReAtrib", type=go_DecVar, multiplicity=Multiplicity(1, 1)),
        Property(name="go_DecVar7", type=go_ReAtrib, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
atrb8: BinaryAssociation = BinaryAssociation(
    name="atrb8",
    ends={
        Property(name="go_Atrib_Aux", type=go_AtribVar, multiplicity=Multiplicity(1, 1)),
        Property(name="go_AtribVar9", type=go_Atrib_Aux, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
atrib14: BinaryAssociation = BinaryAssociation(
    name="atrib14",
    ends={
        Property(name="go_Atrib_Aux16", type=go_Atrib, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Atrib15", type=go_Atrib_Aux, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
k17: BinaryAssociation = BinaryAssociation(
    name="k17",
    ends={
        Property(name="go_EObject", type=go_Atrib, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Atrib18", type=go_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
atrib19: BinaryAssociation = BinaryAssociation(
    name="atrib19",
    ends={
        Property(name="go_Atrib_Aux21", type=go_ReAtrib, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ReAtrib20", type=go_Atrib_Aux, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
k22: BinaryAssociation = BinaryAssociation(
    name="k22",
    ends={
        Property(name="go_EObject24", type=go_ReAtrib, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ReAtrib23", type=go_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typw25: BinaryAssociation = BinaryAssociation(
    name="typw25",
    ends={
        Property(name="go_TypeValue", type=go_MultDecVars, multiplicity=Multiplicity(1, 1)),
        Property(name="go_MultDecVars", type=go_TypeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cas10: BinaryAssociation = BinaryAssociation(
    name="cas10",
    ends={
        Property(name="go_Cases", type=go_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Variable", type=go_Cases, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
k11: BinaryAssociation = BinaryAssociation(
    name="k11",
    ends={
        Property(name="go_Greeting13", type=go_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Variable12", type=go_Greeting, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
x28: BinaryAssociation = BinaryAssociation(
    name="x28",
    ends={
        Property(name="go_Expression", type=go_Cases, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Cases29", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
v30: BinaryAssociation = BinaryAssociation(
    name="v30",
    ends={
        Property(name="go_Greeting32", type=go_Cases, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Cases31", type=go_Greeting, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
atrb26: BinaryAssociation = BinaryAssociation(
    name="atrb26",
    ends={
        Property(name="go_Atrib_Aux27", type=go_DecVars, multiplicity=Multiplicity(1, 1)),
        Property(name="go_DecVars", type=go_Atrib_Aux, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
o36: BinaryAssociation = BinaryAssociation(
    name="o36",
    ends={
        Property(name="go_EObject37", type=go_T, multiplicity=Multiplicity(1, 1)),
        Property(name="go_T", type=go_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
o38: BinaryAssociation = BinaryAssociation(
    name="o38",
    ends={
        Property(name="go_EObject39", type=go_Y, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Y", type=go_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
int33: BinaryAssociation = BinaryAssociation(
    name="int33",
    ends={
        Property(name="go_Intg", type=go_Numbers, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Numbers", type=go_Intg, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
d34: BinaryAssociation = BinaryAssociation(
    name="d34",
    ends={
        Property(name="go_Double", type=go_Numbers, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Numbers35", type=go_Double, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
cond45: BinaryAssociation = BinaryAssociation(
    name="cond45",
    ends={
        Property(name="go_Expression47", type=go_IfCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="go_IfCondition46", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then48: BinaryAssociation = BinaryAssociation(
    name="then48",
    ends={
        Property(name="go_Greeting50", type=go_IfCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="go_IfCondition49", type=go_Greeting, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then51: BinaryAssociation = BinaryAssociation(
    name="then51",
    ends={
        Property(name="go_Greeting53", type=go_ElseCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ElseCondition52", type=go_Greeting, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
boolean55: BinaryAssociation = BinaryAssociation(
    name="boolean55",
    ends={
        Property(name="go_Expression56", type=go_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Expression54", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sum58: BinaryAssociation = BinaryAssociation(
    name="sum58",
    ends={
        Property(name="go_Expression59", type=go_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Expression57", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sub61: BinaryAssociation = BinaryAssociation(
    name="sub61",
    ends={
        Property(name="go_Expression62", type=go_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Expression60", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
if40: BinaryAssociation = BinaryAssociation(
    name="if40",
    ends={
        Property(name="go_IfCondition", type=go_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Condition", type=go_IfCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseif41: BinaryAssociation = BinaryAssociation(
    name="elseif41",
    ends={
        Property(name="go_ElseIfCondition", type=go_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Condition42", type=go_ElseIfCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else43: BinaryAssociation = BinaryAssociation(
    name="else43",
    ends={
        Property(name="go_ElseCondition", type=go_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Condition44", type=go_ElseCondition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
param65: BinaryAssociation = BinaryAssociation(
    name="param65",
    ends={
        Property(name="go_Params", type=go_DecFunc, multiplicity=Multiplicity(1, 1)),
        Property(name="go_DecFunc", type=go_Params, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body66: BinaryAssociation = BinaryAssociation(
    name="body66",
    ends={
        Property(name="go_FunctionBody", type=go_DecFunc, multiplicity=Multiplicity(1, 1)),
        Property(name="go_DecFunc67", type=go_FunctionBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args68: BinaryAssociation = BinaryAssociation(
    name="args68",
    ends={
        Property(name="go_Greeting70", type=go_FunctionBody, multiplicity=Multiplicity(1, 1)),
        Property(name="go_FunctionBody69", type=go_Greeting, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ret71: BinaryAssociation = BinaryAssociation(
    name="ret71",
    ends={
        Property(name="go_FunctionReturn", type=go_FunctionBody, multiplicity=Multiplicity(1, 1)),
        Property(name="go_FunctionBody72", type=go_FunctionReturn, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
x63: BinaryAssociation = BinaryAssociation(
    name="x63",
    ends={
        Property(name="go_EObject64", type=go_CallFor, multiplicity=Multiplicity(1, 1)),
        Property(name="go_CallFor", type=go_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left78: BinaryAssociation = BinaryAssociation(
    name="left78",
    ends={
        Property(name="go_Expression79", type=go_Addition, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Addition", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right80: BinaryAssociation = BinaryAssociation(
    name="right80",
    ends={
        Property(name="go_Expression82", type=go_Addition, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Addition81", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left83: BinaryAssociation = BinaryAssociation(
    name="left83",
    ends={
        Property(name="go_Expression84", type=go_Subtration, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Subtration", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right85: BinaryAssociation = BinaryAssociation(
    name="right85",
    ends={
        Property(name="go_Expression87", type=go_Subtration, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Subtration86", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType73: BinaryAssociation = BinaryAssociation(
    name="returnType73",
    ends={
        Property(name="go_Atrib_Aux75", type=go_FunctionReturn, multiplicity=Multiplicity(1, 1)),
        Property(name="go_FunctionReturn74", type=go_Atrib_Aux, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
param76: BinaryAssociation = BinaryAssociation(
    name="param76",
    ends={
        Property(name="go_Params77", type=go_CallFunc, multiplicity=Multiplicity(1, 1)),
        Property(name="go_CallFunc", type=go_Params, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right90: BinaryAssociation = BinaryAssociation(
    name="right90",
    ends={
        Property(name="go_Expression92", type=go_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Multiplication91", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left93: BinaryAssociation = BinaryAssociation(
    name="left93",
    ends={
        Property(name="go_Expression94", type=go_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Division", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right95: BinaryAssociation = BinaryAssociation(
    name="right95",
    ends={
        Property(name="go_Expression97", type=go_Division, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Division96", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left88: BinaryAssociation = BinaryAssociation(
    name="left88",
    ends={
        Property(name="go_Expression89", type=go_Multiplication, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Multiplication", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left103: BinaryAssociation = BinaryAssociation(
    name="left103",
    ends={
        Property(name="go_Expression104", type=go_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="go_AndExpression", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right105: BinaryAssociation = BinaryAssociation(
    name="right105",
    ends={
        Property(name="go_Expression107", type=go_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="go_AndExpression106", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left108: BinaryAssociation = BinaryAssociation(
    name="left108",
    ends={
        Property(name="go_Expression109", type=go_ComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ComparisonExpression", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right110: BinaryAssociation = BinaryAssociation(
    name="right110",
    ends={
        Property(name="go_Expression112", type=go_ComparisonExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="go_ComparisonExpression111", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left98: BinaryAssociation = BinaryAssociation(
    name="left98",
    ends={
        Property(name="go_Expression99", type=go_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="go_OrExpression", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right100: BinaryAssociation = BinaryAssociation(
    name="right100",
    ends={
        Property(name="go_Expression102", type=go_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="go_OrExpression101", type=go_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value113: BinaryAssociation = BinaryAssociation(
    name="value113",
    ends={
        Property(name="go_Bool", type=go_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="go_Literal", type=go_Bool, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_go_DecVar_Greeting = Generalization(general=Greeting, specific=go_DecVar)
gen_go_Variable_Greeting = Generalization(general=Greeting, specific=go_Variable)
gen_go_Variable_Atrib_Aux = Generalization(general=Atrib_Aux, specific=go_Variable)
gen_go_Variable_SwitchCase = Generalization(general=SwitchCase, specific=go_Variable)
gen_go_Variable_OperationsOneEquals = Generalization(general=OperationsOneEquals, specific=go_Variable)
gen_go_ReAtrib_varFor = Generalization(general=varFor, specific=go_ReAtrib)
gen_go_MultDecVars_Greeting = Generalization(general=Greeting, specific=go_MultDecVars)
gen_go_Variable_operationsOne = Generalization(general=operationsOne, specific=go_Variable)
gen_go_Variable_Expression = Generalization(general=Expression, specific=go_Variable)
gen_go_Atrib_varFor = Generalization(general=varFor, specific=go_Atrib)
gen_go_Atri_Atrib_Aux = Generalization(general=Atrib_Aux, specific=go_Atri)
gen_go_TypeValue_Atri = Generalization(general=Atri, specific=go_TypeValue)
gen_go_Str_TypeValue = Generalization(general=TypeValue, specific=go_Str)
gen_go_Numbers_TypeValue = Generalization(general=TypeValue, specific=go_Numbers)
gen_go_Numbers_F = Generalization(general=F, specific=go_Numbers)
gen_go_SwitchCase_Greeting = Generalization(general=Greeting, specific=go_SwitchCase)
gen_go_Operations_Atrib_Aux = Generalization(general=Atrib_Aux, specific=go_Operations)
gen_go_T_Operations = Generalization(general=Operations, specific=go_T)
gen_go_T_I = Generalization(general=I, specific=go_T)
gen_go_F_T = Generalization(general=T, specific=go_F)
gen_go_Condition_Greeting = Generalization(general=Greeting, specific=go_Condition)
gen_go_Numbers_Expression = Generalization(general=Expression, specific=go_Numbers)
gen_go_IfCondition_ElseIfCondition = Generalization(general=ElseIfCondition, specific=go_IfCondition)
gen_go_Expression_varFor = Generalization(general=varFor, specific=go_Expression)
gen_go_DecFunc_Greeting = Generalization(general=Greeting, specific=go_DecFunc)
gen_go_CallFor_Greeting = Generalization(general=Greeting, specific=go_CallFor)
gen_go_varFor_CallFor = Generalization(general=CallFor, specific=go_varFor)
gen_go_Bool_TypeValue = Generalization(general=TypeValue, specific=go_Bool)
gen_go_DataType_Greeting = Generalization(general=Greeting, specific=go_DataType)
gen_go_Addition_Expression = Generalization(general=Expression, specific=go_Addition)
gen_go_Subtration_Expression = Generalization(general=Expression, specific=go_Subtration)
gen_go_Multiplication_Expression = Generalization(general=Expression, specific=go_Multiplication)
gen_go_CallFunc_Greeting = Generalization(general=Greeting, specific=go_CallFunc)
gen_go_CallFunc_Atrib_Aux = Generalization(general=Atrib_Aux, specific=go_CallFunc)
gen_go_Division_Expression = Generalization(general=Expression, specific=go_Division)
gen_go_OrExpression_Expression = Generalization(general=Expression, specific=go_OrExpression)
gen_go_AndExpression_Expression = Generalization(general=Expression, specific=go_AndExpression)
gen_go_ComparisonExpression_Expression = Generalization(general=Expression, specific=go_ComparisonExpression)
gen_go_Literal_Expression = Generalization(general=Expression, specific=go_Literal)

# Domain Model
domain_model = DomainModel(
    name="go",
    types={go_Go, go_Greeting, Greeting, go_Atrib, go_AtribVar, go_ReAtrib, go_Atrib_Aux, go_Variable, Atrib_Aux, SwitchCase, go_Decl, go_DecVar, OperationsOneEquals, go_EObject, go_MultDecVars, go_TypeValue, operationsOne, Expression, go_Cases, varFor, go_Expression, go_Atri, go_Params, Atri, go_Str, TypeValue, go_OperationsOneEquals, go_Numbers, F, go_DecVars, go_SwitchCase, go_Operations, go_I, go_T, Operations, I, go_Y, go_F, T, go_Condition, go_IfCondition, go_Intg, go_Double, ElseIfCondition, go_ElseIfCondition, go_ElseCondition, go_DecFunc, go_FunctionBody, go_FunctionReturn, go_CallFor, go_operationsOne, go_varFor, CallFor, go_Bool, go_DataType, go_Addition, go_Subtration, go_Multiplication, go_CallFunc, go_Division, go_OrExpression, go_AndExpression, go_ComparisonExpression, go_Literal},
    associations={elements0, declaration1, atribuicao2, assignment4, reassignment6, atrb8, atrib14, k17, atrib19, k22, typw25, cas10, k11, x28, v30, atrb26, o36, o38, int33, d34, cond45, then48, then51, boolean55, sum58, sub61, if40, elseif41, else43, param65, body66, args68, ret71, x63, left78, right80, left83, right85, returnType73, param76, right90, left93, right95, left88, left103, right105, left108, right110, left98, right100, value113},
    generalizations={gen_go_DecVar_Greeting, gen_go_Variable_Greeting, gen_go_Variable_Atrib_Aux, gen_go_Variable_SwitchCase, gen_go_Variable_OperationsOneEquals, gen_go_ReAtrib_varFor, gen_go_MultDecVars_Greeting, gen_go_Variable_operationsOne, gen_go_Variable_Expression, gen_go_Atrib_varFor, gen_go_Atri_Atrib_Aux, gen_go_TypeValue_Atri, gen_go_Str_TypeValue, gen_go_Numbers_TypeValue, gen_go_Numbers_F, gen_go_SwitchCase_Greeting, gen_go_Operations_Atrib_Aux, gen_go_T_Operations, gen_go_T_I, gen_go_F_T, gen_go_Condition_Greeting, gen_go_Numbers_Expression, gen_go_IfCondition_ElseIfCondition, gen_go_Expression_varFor, gen_go_DecFunc_Greeting, gen_go_CallFor_Greeting, gen_go_varFor_CallFor, gen_go_Bool_TypeValue, gen_go_DataType_Greeting, gen_go_Addition_Expression, gen_go_Subtration_Expression, gen_go_Multiplication_Expression, gen_go_CallFunc_Greeting, gen_go_CallFunc_Atrib_Aux, gen_go_Division_Expression, gen_go_OrExpression_Expression, gen_go_AndExpression_Expression, gen_go_ComparisonExpression_Expression, gen_go_Literal_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)