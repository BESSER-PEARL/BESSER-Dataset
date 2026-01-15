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
tortugaDSL_TortugaProgram = Class(name="tortugaDSL::TortugaProgram")
tortugaDSL_SENTENCE = Class(name="tortugaDSL::SENTENCE")
tortugaDSL_MOVE = Class(name="tortugaDSL::MOVE")
SENTENCE = Class(name="SENTENCE")
tortugaDSL_EXPRESSION = Class(name="tortugaDSL::EXPRESSION")
tortugaDSL_FORWARD = Class(name="tortugaDSL::FORWARD")
MOVE = Class(name="MOVE")
tortugaDSL_LEFT = Class(name="tortugaDSL::LEFT")
tortugaDSL_RIGHT = Class(name="tortugaDSL::RIGHT")
tortugaDSL_SET_X = Class(name="tortugaDSL::SET::X")
tortugaDSL_COLOREABLE = Class(name="tortugaDSL::COLOREABLE")
tortugaDSL_COLOR_SPEC = Class(name="tortugaDSL::COLOR::SPEC")
tortugaDSL_PENCOLOR = Class(name="tortugaDSL::PENCOLOR")
COLOREABLE = Class(name="COLOREABLE")
tortugaDSL_CANVAS_COLOR = Class(name="tortugaDSL::CANVAS::COLOR")
tortugaDSL_FONT_SPEC = Class(name="tortugaDSL::FONT::SPEC")
tortugaDSL_FONT_SIZE = Class(name="tortugaDSL::FONT::SIZE")
FONT_SPEC = Class(name="FONT::SPEC")
tortugaDSL_FONT_STYLE = Class(name="tortugaDSL::FONT::STYLE")
tortugaDSL_FontStyleValues = Class(name="tortugaDSL::FontStyleValues")
tortugaDSL_CLEAR = Class(name="tortugaDSL::CLEAR")
tortugaDSL_HOME = Class(name="tortugaDSL::HOME")
tortugaDSL_SET_Y = Class(name="tortugaDSL::SET::Y")
tortugaDSL_DRAWING_SENTENCE = Class(name="tortugaDSL::DRAWING::SENTENCE")
tortugaDSL_PENDOWN = Class(name="tortugaDSL::PENDOWN")
DRAWING_SENTENCE = Class(name="DRAWING::SENTENCE")
tortugaDSL_PENUP = Class(name="tortugaDSL::PENUP")
tortugaDSL_VARIABLE_REF = Class(name="tortugaDSL::VARIABLE::REF")
EXPRESSION = Class(name="EXPRESSION")
tortugaDSL_VALUE = Class(name="tortugaDSL::VALUE")
tortugaDSL_CONTENT = Class(name="tortugaDSL::CONTENT")
tortugaDSL_OPERATION = Class(name="tortugaDSL::OPERATION")
tortugaDSL_SUM = Class(name="tortugaDSL::SUM")
OPERATION = Class(name="OPERATION")
tortugaDSL_SUBTRACT = Class(name="tortugaDSL::SUBTRACT")
tortugaDSL_MULTIPLY = Class(name="tortugaDSL::MULTIPLY")
tortugaDSL_DIVIDE = Class(name="tortugaDSL::DIVIDE")
tortugaDSL_CONTROL_SENTENCES = Class(name="tortugaDSL::CONTROL::SENTENCES")
tortugaDSL_DRAW_STRING = Class(name="tortugaDSL::DRAW::STRING")
tortugaDSL_REFERENCIABLE = Class(name="tortugaDSL::REFERENCIABLE")
tortugaDSL_MAKE = Class(name="tortugaDSL::MAKE")
REFERENCIABLE = Class(name="REFERENCIABLE")
tortugaDSL_PARAM = Class(name="tortugaDSL::PARAM")
tortugaDSL_PROCEDURE_CALL = Class(name="tortugaDSL::PROCEDURE::CALL")
tortugaDSL_IF = Class(name="tortugaDSL::IF")
tortugaDSL_BOOLEAN_EXPRESSION = Class(name="tortugaDSL::BOOLEAN::EXPRESSION")
tortugaDSL_EQUALS = Class(name="tortugaDSL::EQUALS")
BOOLEAN_EXPRESSION = Class(name="BOOLEAN::EXPRESSION")
tortugaDSL_GREATER_THAN = Class(name="tortugaDSL::GREATER::THAN")
tortugaDSL_LESSER_THAN = Class(name="tortugaDSL::LESSER::THAN")
tortugaDSL_BOLD = Class(name="tortugaDSL::BOLD")
FontStyleValues = Class(name="FontStyleValues")
tortugaDSL_ITALIC = Class(name="tortugaDSL::ITALIC")
tortugaDSL_PLAIN = Class(name="tortugaDSL::PLAIN")
tortugaDSL_REPEAT = Class(name="tortugaDSL::REPEAT")
CONTROL_SENTENCES = Class(name="CONTROL::SENTENCES")
tortugaDSL_TO = Class(name="tortugaDSL::TO")

# tortugaDSL_TortugaProgram class attributes and methods

# tortugaDSL_SENTENCE class attributes and methods

# tortugaDSL_MOVE class attributes and methods

# SENTENCE class attributes and methods

# tortugaDSL_EXPRESSION class attributes and methods

# tortugaDSL_FORWARD class attributes and methods

# MOVE class attributes and methods

# tortugaDSL_LEFT class attributes and methods

# tortugaDSL_RIGHT class attributes and methods

# tortugaDSL_SET_X class attributes and methods

# tortugaDSL_COLOREABLE class attributes and methods
tortugaDSL_COLOREABLE_color: Property = Property(name="color", type=StringType)
tortugaDSL_COLOREABLE.attributes={tortugaDSL_COLOREABLE_color}

# tortugaDSL_COLOR_SPEC class attributes and methods

# tortugaDSL_PENCOLOR class attributes and methods

# COLOREABLE class attributes and methods

# tortugaDSL_CANVAS_COLOR class attributes and methods

# tortugaDSL_FONT_SPEC class attributes and methods

# tortugaDSL_FONT_SIZE class attributes and methods

# FONT_SPEC class attributes and methods

# tortugaDSL_FONT_STYLE class attributes and methods

# tortugaDSL_FontStyleValues class attributes and methods

# tortugaDSL_CLEAR class attributes and methods

# tortugaDSL_HOME class attributes and methods

# tortugaDSL_SET_Y class attributes and methods

# tortugaDSL_DRAWING_SENTENCE class attributes and methods

# tortugaDSL_PENDOWN class attributes and methods

# DRAWING_SENTENCE class attributes and methods

# tortugaDSL_PENUP class attributes and methods

# tortugaDSL_VARIABLE_REF class attributes and methods

# EXPRESSION class attributes and methods

# tortugaDSL_VALUE class attributes and methods
tortugaDSL_VALUE_val: Property = Property(name="val", type=FloatType)
tortugaDSL_VALUE.attributes={tortugaDSL_VALUE_val}

# tortugaDSL_CONTENT class attributes and methods

# tortugaDSL_OPERATION class attributes and methods

# tortugaDSL_SUM class attributes and methods

# OPERATION class attributes and methods

# tortugaDSL_SUBTRACT class attributes and methods

# tortugaDSL_MULTIPLY class attributes and methods

# tortugaDSL_DIVIDE class attributes and methods

# tortugaDSL_CONTROL_SENTENCES class attributes and methods

# tortugaDSL_DRAW_STRING class attributes and methods
tortugaDSL_DRAW_STRING_text: Property = Property(name="text", type=StringType)
tortugaDSL_DRAW_STRING.attributes={tortugaDSL_DRAW_STRING_text}

# tortugaDSL_REFERENCIABLE class attributes and methods
tortugaDSL_REFERENCIABLE_name: Property = Property(name="name", type=StringType)
tortugaDSL_REFERENCIABLE.attributes={tortugaDSL_REFERENCIABLE_name}

# tortugaDSL_MAKE class attributes and methods

# REFERENCIABLE class attributes and methods

# tortugaDSL_PARAM class attributes and methods

# tortugaDSL_PROCEDURE_CALL class attributes and methods

# tortugaDSL_IF class attributes and methods

# tortugaDSL_BOOLEAN_EXPRESSION class attributes and methods

# tortugaDSL_EQUALS class attributes and methods

# BOOLEAN_EXPRESSION class attributes and methods

# tortugaDSL_GREATER_THAN class attributes and methods

# tortugaDSL_LESSER_THAN class attributes and methods

# tortugaDSL_BOLD class attributes and methods

# FontStyleValues class attributes and methods

# tortugaDSL_ITALIC class attributes and methods

# tortugaDSL_PLAIN class attributes and methods

# tortugaDSL_REPEAT class attributes and methods

# CONTROL_SENTENCES class attributes and methods

# tortugaDSL_TO class attributes and methods
tortugaDSL_TO_name: Property = Property(name="name", type=StringType)
tortugaDSL_TO.attributes={tortugaDSL_TO_name}

# Relationships
sentences0: BinaryAssociation = BinaryAssociation(
    name="sentences0",
    ends={
        Property(name="tortugaDSL_SENTENCE", type=tortugaDSL_TortugaProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_TortugaProgram", type=tortugaDSL_SENTENCE, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
amount1: BinaryAssociation = BinaryAssociation(
    name="amount1",
    ends={
        Property(name="tortugaDSL_EXPRESSION", type=tortugaDSL_MOVE, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_MOVE", type=tortugaDSL_EXPRESSION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
colorSpec2: BinaryAssociation = BinaryAssociation(
    name="colorSpec2",
    ends={
        Property(name="tortugaDSL_COLOR_SPEC", type=tortugaDSL_COLOREABLE, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_COLOREABLE", type=tortugaDSL_COLOR_SPEC, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
red3: BinaryAssociation = BinaryAssociation(
    name="red3",
    ends={
        Property(name="tortugaDSL_EXPRESSION5", type=tortugaDSL_COLOR_SPEC, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_COLOR_SPEC4", type=tortugaDSL_EXPRESSION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
green6: BinaryAssociation = BinaryAssociation(
    name="green6",
    ends={
        Property(name="tortugaDSL_EXPRESSION8", type=tortugaDSL_COLOR_SPEC, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_COLOR_SPEC7", type=tortugaDSL_EXPRESSION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blue9: BinaryAssociation = BinaryAssociation(
    name="blue9",
    ends={
        Property(name="tortugaDSL_EXPRESSION11", type=tortugaDSL_COLOR_SPEC, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_COLOR_SPEC10", type=tortugaDSL_EXPRESSION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alpha12: BinaryAssociation = BinaryAssociation(
    name="alpha12",
    ends={
        Property(name="tortugaDSL_EXPRESSION14", type=tortugaDSL_COLOR_SPEC, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_COLOR_SPEC13", type=tortugaDSL_EXPRESSION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
size15: BinaryAssociation = BinaryAssociation(
    name="size15",
    ends={
        Property(name="tortugaDSL_EXPRESSION16", type=tortugaDSL_FONT_SIZE, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_FONT_SIZE", type=tortugaDSL_EXPRESSION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
style17: BinaryAssociation = BinaryAssociation(
    name="style17",
    ends={
        Property(name="tortugaDSL_FontStyleValues", type=tortugaDSL_FONT_STYLE, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_FONT_STYLE", type=tortugaDSL_FontStyleValues, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value18: BinaryAssociation = BinaryAssociation(
    name="value18",
    ends={
        Property(name="tortugaDSL_EXPRESSION19", type=tortugaDSL_MAKE, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_MAKE", type=tortugaDSL_EXPRESSION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toVar20: BinaryAssociation = BinaryAssociation(
    name="toVar20",
    ends={
        Property(name="tortugaDSL_REFERENCIABLE", type=tortugaDSL_VARIABLE_REF, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_VARIABLE_REF", type=tortugaDSL_REFERENCIABLE, multiplicity=Multiplicity(0, 1))
    }
)
var21: BinaryAssociation = BinaryAssociation(
    name="var21",
    ends={
        Property(name="tortugaDSL_MAKE22", type=tortugaDSL_CONTENT, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_CONTENT", type=tortugaDSL_MAKE, multiplicity=Multiplicity(0, 1))
    }
)
targetVariable23: BinaryAssociation = BinaryAssociation(
    name="targetVariable23",
    ends={
        Property(name="tortugaDSL_MAKE24", type=tortugaDSL_OPERATION, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_OPERATION", type=tortugaDSL_MAKE, multiplicity=Multiplicity(0, 1))
    }
)
valOne25: BinaryAssociation = BinaryAssociation(
    name="valOne25",
    ends={
        Property(name="tortugaDSL_EXPRESSION27", type=tortugaDSL_OPERATION, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_OPERATION26", type=tortugaDSL_EXPRESSION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valTwo28: BinaryAssociation = BinaryAssociation(
    name="valTwo28",
    ends={
        Property(name="tortugaDSL_EXPRESSION30", type=tortugaDSL_OPERATION, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_OPERATION29", type=tortugaDSL_EXPRESSION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commands31: BinaryAssociation = BinaryAssociation(
    name="commands31",
    ends={
        Property(name="tortugaDSL_SENTENCE32", type=tortugaDSL_CONTROL_SENTENCES, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_CONTROL_SENTENCES", type=tortugaDSL_SENTENCE, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters35: BinaryAssociation = BinaryAssociation(
    name="parameters35",
    ends={
        Property(name="tortugaDSL_PARAM", type=tortugaDSL_TO, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_TO", type=tortugaDSL_PARAM, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
to36: BinaryAssociation = BinaryAssociation(
    name="to36",
    ends={
        Property(name="tortugaDSL_TO37", type=tortugaDSL_PROCEDURE_CALL, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_PROCEDURE_CALL", type=tortugaDSL_TO, multiplicity=Multiplicity(0, 1))
    }
)
params38: BinaryAssociation = BinaryAssociation(
    name="params38",
    ends={
        Property(name="tortugaDSL_EXPRESSION40", type=tortugaDSL_PROCEDURE_CALL, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_PROCEDURE_CALL39", type=tortugaDSL_EXPRESSION, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition41: BinaryAssociation = BinaryAssociation(
    name="condition41",
    ends={
        Property(name="tortugaDSL_BOOLEAN_EXPRESSION", type=tortugaDSL_IF, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_IF", type=tortugaDSL_BOOLEAN_EXPRESSION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op142: BinaryAssociation = BinaryAssociation(
    name="op142",
    ends={
        Property(name="tortugaDSL_EXPRESSION44", type=tortugaDSL_BOOLEAN_EXPRESSION, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_BOOLEAN_EXPRESSION43", type=tortugaDSL_EXPRESSION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op245: BinaryAssociation = BinaryAssociation(
    name="op245",
    ends={
        Property(name="tortugaDSL_EXPRESSION47", type=tortugaDSL_BOOLEAN_EXPRESSION, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_BOOLEAN_EXPRESSION46", type=tortugaDSL_EXPRESSION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
times33: BinaryAssociation = BinaryAssociation(
    name="times33",
    ends={
        Property(name="tortugaDSL_EXPRESSION34", type=tortugaDSL_REPEAT, multiplicity=Multiplicity(1, 1)),
        Property(name="tortugaDSL_REPEAT", type=tortugaDSL_EXPRESSION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_tortugaDSL_MOVE_SENTENCE = Generalization(general=SENTENCE, specific=tortugaDSL_MOVE)
gen_tortugaDSL_FORWARD_MOVE = Generalization(general=MOVE, specific=tortugaDSL_FORWARD)
gen_tortugaDSL_LEFT_MOVE = Generalization(general=MOVE, specific=tortugaDSL_LEFT)
gen_tortugaDSL_RIGHT_MOVE = Generalization(general=MOVE, specific=tortugaDSL_RIGHT)
gen_tortugaDSL_COLOREABLE_DRAWING_SENTENCE = Generalization(general=DRAWING_SENTENCE, specific=tortugaDSL_COLOREABLE)
gen_tortugaDSL_PENCOLOR_COLOREABLE = Generalization(general=COLOREABLE, specific=tortugaDSL_PENCOLOR)
gen_tortugaDSL_CANVAS_COLOR_COLOREABLE = Generalization(general=COLOREABLE, specific=tortugaDSL_CANVAS_COLOR)
gen_tortugaDSL_FONT_SPEC_DRAWING_SENTENCE = Generalization(general=DRAWING_SENTENCE, specific=tortugaDSL_FONT_SPEC)
gen_tortugaDSL_FONT_SIZE_FONT_SPEC = Generalization(general=FONT_SPEC, specific=tortugaDSL_FONT_SIZE)
gen_tortugaDSL_FONT_STYLE_FONT_SPEC = Generalization(general=FONT_SPEC, specific=tortugaDSL_FONT_STYLE)
gen_tortugaDSL_CLEAR_DRAWING_SENTENCE = Generalization(general=DRAWING_SENTENCE, specific=tortugaDSL_CLEAR)
gen_tortugaDSL_HOME_DRAWING_SENTENCE = Generalization(general=DRAWING_SENTENCE, specific=tortugaDSL_HOME)
gen_tortugaDSL_SET_X_MOVE = Generalization(general=MOVE, specific=tortugaDSL_SET_X)
gen_tortugaDSL_SET_Y_MOVE = Generalization(general=MOVE, specific=tortugaDSL_SET_Y)
gen_tortugaDSL_DRAWING_SENTENCE_SENTENCE = Generalization(general=SENTENCE, specific=tortugaDSL_DRAWING_SENTENCE)
gen_tortugaDSL_PENDOWN_DRAWING_SENTENCE = Generalization(general=DRAWING_SENTENCE, specific=tortugaDSL_PENDOWN)
gen_tortugaDSL_PENUP_DRAWING_SENTENCE = Generalization(general=DRAWING_SENTENCE, specific=tortugaDSL_PENUP)
gen_tortugaDSL_VARIABLE_REF_EXPRESSION = Generalization(general=EXPRESSION, specific=tortugaDSL_VARIABLE_REF)
gen_tortugaDSL_VALUE_EXPRESSION = Generalization(general=EXPRESSION, specific=tortugaDSL_VALUE)
gen_tortugaDSL_CONTENT_SENTENCE = Generalization(general=SENTENCE, specific=tortugaDSL_CONTENT)
gen_tortugaDSL_OPERATION_SENTENCE = Generalization(general=SENTENCE, specific=tortugaDSL_OPERATION)
gen_tortugaDSL_SUM_OPERATION = Generalization(general=OPERATION, specific=tortugaDSL_SUM)
gen_tortugaDSL_SUBTRACT_OPERATION = Generalization(general=OPERATION, specific=tortugaDSL_SUBTRACT)
gen_tortugaDSL_MULTIPLY_OPERATION = Generalization(general=OPERATION, specific=tortugaDSL_MULTIPLY)
gen_tortugaDSL_DIVIDE_OPERATION = Generalization(general=OPERATION, specific=tortugaDSL_DIVIDE)
gen_tortugaDSL_CONTROL_SENTENCES_SENTENCE = Generalization(general=SENTENCE, specific=tortugaDSL_CONTROL_SENTENCES)
gen_tortugaDSL_DRAW_STRING_DRAWING_SENTENCE = Generalization(general=DRAWING_SENTENCE, specific=tortugaDSL_DRAW_STRING)
gen_tortugaDSL_MAKE_SENTENCE = Generalization(general=SENTENCE, specific=tortugaDSL_MAKE)
gen_tortugaDSL_MAKE_REFERENCIABLE = Generalization(general=REFERENCIABLE, specific=tortugaDSL_MAKE)
gen_tortugaDSL_PARAM_REFERENCIABLE = Generalization(general=REFERENCIABLE, specific=tortugaDSL_PARAM)
gen_tortugaDSL_PROCEDURE_CALL_SENTENCE = Generalization(general=SENTENCE, specific=tortugaDSL_PROCEDURE_CALL)
gen_tortugaDSL_IF_CONTROL_SENTENCES = Generalization(general=CONTROL_SENTENCES, specific=tortugaDSL_IF)
gen_tortugaDSL_EQUALS_BOOLEAN_EXPRESSION = Generalization(general=BOOLEAN_EXPRESSION, specific=tortugaDSL_EQUALS)
gen_tortugaDSL_GREATER_THAN_BOOLEAN_EXPRESSION = Generalization(general=BOOLEAN_EXPRESSION, specific=tortugaDSL_GREATER_THAN)
gen_tortugaDSL_LESSER_THAN_BOOLEAN_EXPRESSION = Generalization(general=BOOLEAN_EXPRESSION, specific=tortugaDSL_LESSER_THAN)
gen_tortugaDSL_BOLD_FontStyleValues = Generalization(general=FontStyleValues, specific=tortugaDSL_BOLD)
gen_tortugaDSL_ITALIC_FontStyleValues = Generalization(general=FontStyleValues, specific=tortugaDSL_ITALIC)
gen_tortugaDSL_PLAIN_FontStyleValues = Generalization(general=FontStyleValues, specific=tortugaDSL_PLAIN)
gen_tortugaDSL_REPEAT_CONTROL_SENTENCES = Generalization(general=CONTROL_SENTENCES, specific=tortugaDSL_REPEAT)
gen_tortugaDSL_TO_CONTROL_SENTENCES = Generalization(general=CONTROL_SENTENCES, specific=tortugaDSL_TO)

# Domain Model
domain_model = DomainModel(
    name="tortugaDSL",
    types={tortugaDSL_TortugaProgram, tortugaDSL_SENTENCE, tortugaDSL_MOVE, SENTENCE, tortugaDSL_EXPRESSION, tortugaDSL_FORWARD, MOVE, tortugaDSL_LEFT, tortugaDSL_RIGHT, tortugaDSL_SET_X, tortugaDSL_COLOREABLE, tortugaDSL_COLOR_SPEC, tortugaDSL_PENCOLOR, COLOREABLE, tortugaDSL_CANVAS_COLOR, tortugaDSL_FONT_SPEC, tortugaDSL_FONT_SIZE, FONT_SPEC, tortugaDSL_FONT_STYLE, tortugaDSL_FontStyleValues, tortugaDSL_CLEAR, tortugaDSL_HOME, tortugaDSL_SET_Y, tortugaDSL_DRAWING_SENTENCE, tortugaDSL_PENDOWN, DRAWING_SENTENCE, tortugaDSL_PENUP, tortugaDSL_VARIABLE_REF, EXPRESSION, tortugaDSL_VALUE, tortugaDSL_CONTENT, tortugaDSL_OPERATION, tortugaDSL_SUM, OPERATION, tortugaDSL_SUBTRACT, tortugaDSL_MULTIPLY, tortugaDSL_DIVIDE, tortugaDSL_CONTROL_SENTENCES, tortugaDSL_DRAW_STRING, tortugaDSL_REFERENCIABLE, tortugaDSL_MAKE, REFERENCIABLE, tortugaDSL_PARAM, tortugaDSL_PROCEDURE_CALL, tortugaDSL_IF, tortugaDSL_BOOLEAN_EXPRESSION, tortugaDSL_EQUALS, BOOLEAN_EXPRESSION, tortugaDSL_GREATER_THAN, tortugaDSL_LESSER_THAN, tortugaDSL_BOLD, FontStyleValues, tortugaDSL_ITALIC, tortugaDSL_PLAIN, tortugaDSL_REPEAT, CONTROL_SENTENCES, tortugaDSL_TO},
    associations={sentences0, amount1, colorSpec2, red3, green6, blue9, alpha12, size15, style17, value18, toVar20, var21, targetVariable23, valOne25, valTwo28, commands31, parameters35, to36, params38, condition41, op142, op245, times33},
    generalizations={gen_tortugaDSL_MOVE_SENTENCE, gen_tortugaDSL_FORWARD_MOVE, gen_tortugaDSL_LEFT_MOVE, gen_tortugaDSL_RIGHT_MOVE, gen_tortugaDSL_COLOREABLE_DRAWING_SENTENCE, gen_tortugaDSL_PENCOLOR_COLOREABLE, gen_tortugaDSL_CANVAS_COLOR_COLOREABLE, gen_tortugaDSL_FONT_SPEC_DRAWING_SENTENCE, gen_tortugaDSL_FONT_SIZE_FONT_SPEC, gen_tortugaDSL_FONT_STYLE_FONT_SPEC, gen_tortugaDSL_CLEAR_DRAWING_SENTENCE, gen_tortugaDSL_HOME_DRAWING_SENTENCE, gen_tortugaDSL_SET_X_MOVE, gen_tortugaDSL_SET_Y_MOVE, gen_tortugaDSL_DRAWING_SENTENCE_SENTENCE, gen_tortugaDSL_PENDOWN_DRAWING_SENTENCE, gen_tortugaDSL_PENUP_DRAWING_SENTENCE, gen_tortugaDSL_VARIABLE_REF_EXPRESSION, gen_tortugaDSL_VALUE_EXPRESSION, gen_tortugaDSL_CONTENT_SENTENCE, gen_tortugaDSL_OPERATION_SENTENCE, gen_tortugaDSL_SUM_OPERATION, gen_tortugaDSL_SUBTRACT_OPERATION, gen_tortugaDSL_MULTIPLY_OPERATION, gen_tortugaDSL_DIVIDE_OPERATION, gen_tortugaDSL_CONTROL_SENTENCES_SENTENCE, gen_tortugaDSL_DRAW_STRING_DRAWING_SENTENCE, gen_tortugaDSL_MAKE_SENTENCE, gen_tortugaDSL_MAKE_REFERENCIABLE, gen_tortugaDSL_PARAM_REFERENCIABLE, gen_tortugaDSL_PROCEDURE_CALL_SENTENCE, gen_tortugaDSL_IF_CONTROL_SENTENCES, gen_tortugaDSL_EQUALS_BOOLEAN_EXPRESSION, gen_tortugaDSL_GREATER_THAN_BOOLEAN_EXPRESSION, gen_tortugaDSL_LESSER_THAN_BOOLEAN_EXPRESSION, gen_tortugaDSL_BOLD_FontStyleValues, gen_tortugaDSL_ITALIC_FontStyleValues, gen_tortugaDSL_PLAIN_FontStyleValues, gen_tortugaDSL_REPEAT_CONTROL_SENTENCES, gen_tortugaDSL_TO_CONTROL_SENTENCES},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)