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
expressions_StringValue = Class(name="expressions::StringValue")
expressions_Variable = Class(name="expressions::Variable")
expressions_Equivalent = Class(name="expressions::Equivalent")
expressions_LExpression = Class(name="expressions::LExpression")
expressions_CExpression = Class(name="expressions::CExpression")
LExpression = Class(name="LExpression")
expressions_SomeValue = Class(name="expressions::SomeValue")
CExpression = Class(name="CExpression")
expressions_AExpression = Class(name="expressions::AExpression")
SomeValue = Class(name="SomeValue")
expressions_NumberValue = Class(name="expressions::NumberValue")
AExpression = Class(name="AExpression")
expressions_BooleanValue = Class(name="expressions::BooleanValue")
expressions_Xor = Class(name="expressions::Xor")
expressions_And = Class(name="expressions::And")
expressions_Imply = Class(name="expressions::Imply")
expressions_Or = Class(name="expressions::Or")
expressions_GreaterOrEqual = Class(name="expressions::GreaterOrEqual")
expressions_Greater = Class(name="expressions::Greater")
expressions_Not = Class(name="expressions::Not")
expressions_LessOrEqual = Class(name="expressions::LessOrEqual")
expressions_Less = Class(name="expressions::Less")
expressions_Approx = Class(name="expressions::Approx")
expressions_Equal = Class(name="expressions::Equal")
expressions_Unequal = Class(name="expressions::Unequal")
expressions_Div = Class(name="expressions::Div")
expressions_Mod = Class(name="expressions::Mod")
expressions_Plus = Class(name="expressions::Plus")
expressions_Minus = Class(name="expressions::Minus")
expressions_Multi = Class(name="expressions::Multi")
expressions_Pow = Class(name="expressions::Pow")

# expressions_StringValue class attributes and methods
expressions_StringValue_strValue: Property = Property(name="strValue", type=StringType)
expressions_StringValue.attributes={expressions_StringValue_strValue}

# expressions_Variable class attributes and methods
expressions_Variable_varName: Property = Property(name="varName", type=StringType)
expressions_Variable.attributes={expressions_Variable_varName}

# expressions_Equivalent class attributes and methods

# expressions_LExpression class attributes and methods

# expressions_CExpression class attributes and methods

# LExpression class attributes and methods

# expressions_SomeValue class attributes and methods

# CExpression class attributes and methods

# expressions_AExpression class attributes and methods

# SomeValue class attributes and methods

# expressions_NumberValue class attributes and methods
expressions_NumberValue_numValue: Property = Property(name="numValue", type=StringType)
expressions_NumberValue.attributes={expressions_NumberValue_numValue}

# AExpression class attributes and methods

# expressions_BooleanValue class attributes and methods
expressions_BooleanValue_value: Property = Property(name="value", type=BooleanType)
expressions_BooleanValue.attributes={expressions_BooleanValue_value}

# expressions_Xor class attributes and methods

# expressions_And class attributes and methods

# expressions_Imply class attributes and methods

# expressions_Or class attributes and methods

# expressions_GreaterOrEqual class attributes and methods

# expressions_Greater class attributes and methods

# expressions_Not class attributes and methods

# expressions_LessOrEqual class attributes and methods

# expressions_Less class attributes and methods

# expressions_Approx class attributes and methods

# expressions_Equal class attributes and methods

# expressions_Unequal class attributes and methods

# expressions_Div class attributes and methods

# expressions_Mod class attributes and methods

# expressions_Plus class attributes and methods

# expressions_Minus class attributes and methods

# expressions_Multi class attributes and methods

# expressions_Pow class attributes and methods

# Relationships
right11: BinaryAssociation = BinaryAssociation(
    name="right11",
    ends={
        Property(name="expressions_LExpression13", type=expressions_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Or12", type=expressions_LExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left14: BinaryAssociation = BinaryAssociation(
    name="left14",
    ends={
        Property(name="expressions_LExpression15", type=expressions_Xor, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Xor", type=expressions_LExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right16: BinaryAssociation = BinaryAssociation(
    name="right16",
    ends={
        Property(name="expressions_LExpression18", type=expressions_Xor, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Xor17", type=expressions_LExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left19: BinaryAssociation = BinaryAssociation(
    name="left19",
    ends={
        Property(name="expressions_LExpression20", type=expressions_And, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_And", type=expressions_LExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left0: BinaryAssociation = BinaryAssociation(
    name="left0",
    ends={
        Property(name="expressions_LExpression", type=expressions_Equivalent, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Equivalent", type=expressions_LExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right1: BinaryAssociation = BinaryAssociation(
    name="right1",
    ends={
        Property(name="expressions_LExpression3", type=expressions_Equivalent, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Equivalent2", type=expressions_LExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left4: BinaryAssociation = BinaryAssociation(
    name="left4",
    ends={
        Property(name="expressions_LExpression5", type=expressions_Imply, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Imply", type=expressions_LExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right6: BinaryAssociation = BinaryAssociation(
    name="right6",
    ends={
        Property(name="expressions_LExpression8", type=expressions_Imply, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Imply7", type=expressions_LExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left9: BinaryAssociation = BinaryAssociation(
    name="left9",
    ends={
        Property(name="expressions_LExpression10", type=expressions_Or, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Or", type=expressions_LExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left30: BinaryAssociation = BinaryAssociation(
    name="left30",
    ends={
        Property(name="expressions_SomeValue31", type=expressions_Less, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Less", type=expressions_SomeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right32: BinaryAssociation = BinaryAssociation(
    name="right32",
    ends={
        Property(name="expressions_SomeValue34", type=expressions_Less, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Less33", type=expressions_SomeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left35: BinaryAssociation = BinaryAssociation(
    name="left35",
    ends={
        Property(name="expressions_SomeValue36", type=expressions_GreaterOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_GreaterOrEqual", type=expressions_SomeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right37: BinaryAssociation = BinaryAssociation(
    name="right37",
    ends={
        Property(name="expressions_SomeValue39", type=expressions_GreaterOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_GreaterOrEqual38", type=expressions_SomeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right21: BinaryAssociation = BinaryAssociation(
    name="right21",
    ends={
        Property(name="expressions_LExpression23", type=expressions_And, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_And22", type=expressions_LExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
not24: BinaryAssociation = BinaryAssociation(
    name="not24",
    ends={
        Property(name="expressions_LExpression25", type=expressions_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Not", type=expressions_LExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left26: BinaryAssociation = BinaryAssociation(
    name="left26",
    ends={
        Property(name="expressions_SomeValue", type=expressions_LessOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_LessOrEqual", type=expressions_SomeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right27: BinaryAssociation = BinaryAssociation(
    name="right27",
    ends={
        Property(name="expressions_SomeValue29", type=expressions_LessOrEqual, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_LessOrEqual28", type=expressions_SomeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left50: BinaryAssociation = BinaryAssociation(
    name="left50",
    ends={
        Property(name="expressions_Unequal", type=expressions_SomeValue, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="expressions_SomeValue51", type=expressions_Unequal, multiplicity=Multiplicity(1, 1))
    }
)
right52: BinaryAssociation = BinaryAssociation(
    name="right52",
    ends={
        Property(name="expressions_SomeValue54", type=expressions_Unequal, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Unequal53", type=expressions_SomeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left40: BinaryAssociation = BinaryAssociation(
    name="left40",
    ends={
        Property(name="expressions_SomeValue41", type=expressions_Greater, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Greater", type=expressions_SomeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right42: BinaryAssociation = BinaryAssociation(
    name="right42",
    ends={
        Property(name="expressions_SomeValue44", type=expressions_Greater, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Greater43", type=expressions_SomeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left45: BinaryAssociation = BinaryAssociation(
    name="left45",
    ends={
        Property(name="expressions_SomeValue46", type=expressions_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Equal", type=expressions_SomeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right47: BinaryAssociation = BinaryAssociation(
    name="right47",
    ends={
        Property(name="expressions_SomeValue49", type=expressions_Equal, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Equal48", type=expressions_SomeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left55: BinaryAssociation = BinaryAssociation(
    name="left55",
    ends={
        Property(name="expressions_SomeValue56", type=expressions_Approx, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Approx", type=expressions_SomeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right71: BinaryAssociation = BinaryAssociation(
    name="right71",
    ends={
        Property(name="expressions_AExpression73", type=expressions_Multi, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Multi72", type=expressions_AExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right57: BinaryAssociation = BinaryAssociation(
    name="right57",
    ends={
        Property(name="expressions_SomeValue59", type=expressions_Approx, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Approx58", type=expressions_SomeValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left74: BinaryAssociation = BinaryAssociation(
    name="left74",
    ends={
        Property(name="expressions_AExpression75", type=expressions_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Div", type=expressions_AExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right76: BinaryAssociation = BinaryAssociation(
    name="right76",
    ends={
        Property(name="expressions_AExpression78", type=expressions_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Div77", type=expressions_AExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left60: BinaryAssociation = BinaryAssociation(
    name="left60",
    ends={
        Property(name="expressions_AExpression", type=expressions_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Plus", type=expressions_AExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right61: BinaryAssociation = BinaryAssociation(
    name="right61",
    ends={
        Property(name="expressions_AExpression63", type=expressions_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Plus62", type=expressions_AExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left64: BinaryAssociation = BinaryAssociation(
    name="left64",
    ends={
        Property(name="expressions_AExpression65", type=expressions_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Minus", type=expressions_AExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right66: BinaryAssociation = BinaryAssociation(
    name="right66",
    ends={
        Property(name="expressions_AExpression68", type=expressions_Minus, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Minus67", type=expressions_AExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left69: BinaryAssociation = BinaryAssociation(
    name="left69",
    ends={
        Property(name="expressions_AExpression70", type=expressions_Multi, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Multi", type=expressions_AExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left79: BinaryAssociation = BinaryAssociation(
    name="left79",
    ends={
        Property(name="expressions_AExpression80", type=expressions_Mod, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Mod", type=expressions_AExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right81: BinaryAssociation = BinaryAssociation(
    name="right81",
    ends={
        Property(name="expressions_AExpression83", type=expressions_Mod, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Mod82", type=expressions_AExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left84: BinaryAssociation = BinaryAssociation(
    name="left84",
    ends={
        Property(name="expressions_AExpression85", type=expressions_Pow, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Pow", type=expressions_AExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right86: BinaryAssociation = BinaryAssociation(
    name="right86",
    ends={
        Property(name="expressions_AExpression88", type=expressions_Pow, multiplicity=Multiplicity(1, 1)),
        Property(name="expressions_Pow87", type=expressions_AExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_expressions_StringValue_SomeValue = Generalization(general=SomeValue, specific=expressions_StringValue)
gen_expressions_Variable_LExpression = Generalization(general=LExpression, specific=expressions_Variable)
gen_expressions_Variable_AExpression = Generalization(general=AExpression, specific=expressions_Variable)
gen_expressions_Equivalent_LExpression = Generalization(general=LExpression, specific=expressions_Equivalent)
gen_expressions_CExpression_LExpression = Generalization(general=LExpression, specific=expressions_CExpression)
gen_expressions_SomeValue_CExpression = Generalization(general=CExpression, specific=expressions_SomeValue)
gen_expressions_AExpression_SomeValue = Generalization(general=SomeValue, specific=expressions_AExpression)
gen_expressions_NumberValue_AExpression = Generalization(general=AExpression, specific=expressions_NumberValue)
gen_expressions_BooleanValue_LExpression = Generalization(general=LExpression, specific=expressions_BooleanValue)
gen_expressions_BooleanValue_SomeValue = Generalization(general=SomeValue, specific=expressions_BooleanValue)
gen_expressions_Xor_LExpression = Generalization(general=LExpression, specific=expressions_Xor)
gen_expressions_And_LExpression = Generalization(general=LExpression, specific=expressions_And)
gen_expressions_Imply_LExpression = Generalization(general=LExpression, specific=expressions_Imply)
gen_expressions_Or_LExpression = Generalization(general=LExpression, specific=expressions_Or)
gen_expressions_GreaterOrEqual_CExpression = Generalization(general=CExpression, specific=expressions_GreaterOrEqual)
gen_expressions_Greater_CExpression = Generalization(general=CExpression, specific=expressions_Greater)
gen_expressions_Not_LExpression = Generalization(general=LExpression, specific=expressions_Not)
gen_expressions_LessOrEqual_CExpression = Generalization(general=CExpression, specific=expressions_LessOrEqual)
gen_expressions_Less_CExpression = Generalization(general=CExpression, specific=expressions_Less)
gen_expressions_Equal_CExpression = Generalization(general=CExpression, specific=expressions_Equal)
gen_expressions_Approx_CExpression = Generalization(general=CExpression, specific=expressions_Approx)
gen_expressions_Unequal_CExpression = Generalization(general=CExpression, specific=expressions_Unequal)
gen_expressions_Div_AExpression = Generalization(general=AExpression, specific=expressions_Div)
gen_expressions_Mod_AExpression = Generalization(general=AExpression, specific=expressions_Mod)
gen_expressions_Plus_AExpression = Generalization(general=AExpression, specific=expressions_Plus)
gen_expressions_Minus_AExpression = Generalization(general=AExpression, specific=expressions_Minus)
gen_expressions_Multi_AExpression = Generalization(general=AExpression, specific=expressions_Multi)
gen_expressions_Pow_AExpression = Generalization(general=AExpression, specific=expressions_Pow)

# Domain Model
domain_model = DomainModel(
    name="expressions",
    types={expressions_StringValue, expressions_Variable, expressions_Equivalent, expressions_LExpression, expressions_CExpression, LExpression, expressions_SomeValue, CExpression, expressions_AExpression, SomeValue, expressions_NumberValue, AExpression, expressions_BooleanValue, expressions_Xor, expressions_And, expressions_Imply, expressions_Or, expressions_GreaterOrEqual, expressions_Greater, expressions_Not, expressions_LessOrEqual, expressions_Less, expressions_Approx, expressions_Equal, expressions_Unequal, expressions_Div, expressions_Mod, expressions_Plus, expressions_Minus, expressions_Multi, expressions_Pow},
    associations={right11, left14, right16, left19, left0, right1, left4, right6, left9, left30, right32, left35, right37, right21, not24, left26, right27, left50, right52, left40, right42, left45, right47, left55, right71, right57, left74, right76, left60, right61, left64, right66, left69, left79, right81, left84, right86},
    generalizations={gen_expressions_StringValue_SomeValue, gen_expressions_Variable_LExpression, gen_expressions_Variable_AExpression, gen_expressions_Equivalent_LExpression, gen_expressions_CExpression_LExpression, gen_expressions_SomeValue_CExpression, gen_expressions_AExpression_SomeValue, gen_expressions_NumberValue_AExpression, gen_expressions_BooleanValue_LExpression, gen_expressions_BooleanValue_SomeValue, gen_expressions_Xor_LExpression, gen_expressions_And_LExpression, gen_expressions_Imply_LExpression, gen_expressions_Or_LExpression, gen_expressions_GreaterOrEqual_CExpression, gen_expressions_Greater_CExpression, gen_expressions_Not_LExpression, gen_expressions_LessOrEqual_CExpression, gen_expressions_Less_CExpression, gen_expressions_Equal_CExpression, gen_expressions_Approx_CExpression, gen_expressions_Unequal_CExpression, gen_expressions_Div_AExpression, gen_expressions_Mod_AExpression, gen_expressions_Plus_AExpression, gen_expressions_Minus_AExpression, gen_expressions_Multi_AExpression, gen_expressions_Pow_AExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)