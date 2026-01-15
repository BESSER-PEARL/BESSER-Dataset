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
myDsl_Type_declaration = Class(name="myDsl::Type::declaration")
myDsl_Class_declaration = Class(name="myDsl::Class::declaration")
myDsl_Interface_declaration = Class(name="myDsl::Interface::declaration")
myDsl_Model = Class(name="myDsl::Model")
myDsl_Compilation_unit = Class(name="myDsl::Compilation::unit")
myDsl_Package_statement = Class(name="myDsl::Package::statement")
myDsl_Import_statement = Class(name="myDsl::Import::statement")
myDsl_Static_initializer = Class(name="myDsl::Static::initializer")
myDsl_Type = Class(name="myDsl::Type")
myDsl_Parameter_list = Class(name="myDsl::Parameter::list")
myDsl_Field_declaration = Class(name="myDsl::Field::declaration")
myDsl_Variable_declaration = Class(name="myDsl::Variable::declaration")
myDsl_Constructor_declaration = Class(name="myDsl::Constructor::declaration")
myDsl_Method_declaration = Class(name="myDsl::Method::declaration")
myDsl_Variable_declarator = Class(name="myDsl::Variable::declarator")
myDsl_Statement_block = Class(name="myDsl::Statement::block")
myDsl_Parameter = Class(name="myDsl::Parameter")
myDsl_Statement = Class(name="myDsl::Statement")
myDsl_Variable_initializer = Class(name="myDsl::Variable::initializer")
myDsl_Array_initializer = Class(name="myDsl::Array::initializer")
myDsl_Expression = Class(name="myDsl::Expression")
myDsl_Type_specifier = Class(name="myDsl::Type::specifier")
myDsl_If_statement = Class(name="myDsl::If::statement")
myDsl_Do_Statement = Class(name="myDsl::Do::Statement")
myDsl_While_Statement = Class(name="myDsl::While::Statement")
myDsl_For_Statement = Class(name="myDsl::For::Statement")
myDsl_Switch_statement = Class(name="myDsl::Switch::statement")
myDsl_Try_statement = Class(name="myDsl::Try::statement")
myDsl_Creating_Expression = Class(name="myDsl::Creating::Expression")
myDsl_Literal_Expression = Class(name="myDsl::Literal::Expression")
myDsl_Numeric_Expression_NR = Class(name="myDsl::Numeric::Expression::NR")
myDsl_Expression_aux = Class(name="myDsl::Expression::aux")
myDsl_Logical_Expression_NR = Class(name="myDsl::Logical::Expression::NR")
myDsl_Bit_Expression_NR = Class(name="myDsl::Bit::Expression::NR")
myDsl_Cast_Expression = Class(name="myDsl::Cast::Expression")
myDsl_Float_Literal = Class(name="myDsl::Float::Literal")
myDsl_Arg_List = Class(name="myDsl::Arg::List")
myDsl_Ampersand_Rule = Class(name="myDsl::Ampersand::Rule")

# myDsl_Type_declaration class attributes and methods
myDsl_Type_declaration_comment: Property = Property(name="comment", type=StringType)
myDsl_Type_declaration.attributes={myDsl_Type_declaration_comment}

# myDsl_Class_declaration class attributes and methods
myDsl_Class_declaration_modifiers: Property = Property(name="modifiers", type=StringType)
myDsl_Class_declaration_className: Property = Property(name="className", type=StringType)
myDsl_Class_declaration_classHerdada: Property = Property(name="classHerdada", type=StringType)
myDsl_Class_declaration_interfaceImplementada: Property = Property(name="interfaceImplementada", type=StringType)
myDsl_Class_declaration_interfacesImplementadas: Property = Property(name="interfacesImplementadas", type=StringType)
myDsl_Class_declaration.attributes={myDsl_Class_declaration_interfaceImplementada, myDsl_Class_declaration_className, myDsl_Class_declaration_classHerdada, myDsl_Class_declaration_interfacesImplementadas, myDsl_Class_declaration_modifiers}

# myDsl_Interface_declaration class attributes and methods
myDsl_Interface_declaration_modifiers: Property = Property(name="modifiers", type=StringType)
myDsl_Interface_declaration_interfaceName: Property = Property(name="interfaceName", type=StringType)
myDsl_Interface_declaration_interfaceHerdada: Property = Property(name="interfaceHerdada", type=StringType)
myDsl_Interface_declaration_interfacesHerdadas: Property = Property(name="interfacesHerdadas", type=StringType)
myDsl_Interface_declaration.attributes={myDsl_Interface_declaration_interfaceName, myDsl_Interface_declaration_interfacesHerdadas, myDsl_Interface_declaration_modifiers, myDsl_Interface_declaration_interfaceHerdada}

# myDsl_Model class attributes and methods

# myDsl_Compilation_unit class attributes and methods

# myDsl_Package_statement class attributes and methods
myDsl_Package_statement_pacName: Property = Property(name="pacName", type=StringType)
myDsl_Package_statement.attributes={myDsl_Package_statement_pacName}

# myDsl_Import_statement class attributes and methods
myDsl_Import_statement_pacName: Property = Property(name="pacName", type=StringType)
myDsl_Import_statement_className: Property = Property(name="className", type=StringType)
myDsl_Import_statement.attributes={myDsl_Import_statement_className, myDsl_Import_statement_pacName}

# myDsl_Static_initializer class attributes and methods
myDsl_Static_initializer_static: Property = Property(name="static", type=StringType)
myDsl_Static_initializer.attributes={myDsl_Static_initializer_static}

# myDsl_Type class attributes and methods
myDsl_Type_typeVector: Property = Property(name="typeVector", type=StringType)
myDsl_Type.attributes={myDsl_Type_typeVector}

# myDsl_Parameter_list class attributes and methods

# myDsl_Field_declaration class attributes and methods
myDsl_Field_declaration_comment: Property = Property(name="comment", type=StringType)
myDsl_Field_declaration.attributes={myDsl_Field_declaration_comment}

# myDsl_Variable_declaration class attributes and methods
myDsl_Variable_declaration_modifiersVariable: Property = Property(name="modifiersVariable", type=StringType)
myDsl_Variable_declaration.attributes={myDsl_Variable_declaration_modifiersVariable}

# myDsl_Constructor_declaration class attributes and methods
myDsl_Constructor_declaration_modifiersConstructor: Property = Property(name="modifiersConstructor", type=StringType)
myDsl_Constructor_declaration_nameConstructor: Property = Property(name="nameConstructor", type=StringType)
myDsl_Constructor_declaration_lParen: Property = Property(name="lParen", type=StringType)
myDsl_Constructor_declaration_rparent: Property = Property(name="rparent", type=StringType)
myDsl_Constructor_declaration.attributes={myDsl_Constructor_declaration_lParen, myDsl_Constructor_declaration_rparent, myDsl_Constructor_declaration_nameConstructor, myDsl_Constructor_declaration_modifiersConstructor}

# myDsl_Method_declaration class attributes and methods
myDsl_Method_declaration_modifiersMethod: Property = Property(name="modifiersMethod", type=StringType)
myDsl_Method_declaration_nameMethod: Property = Property(name="nameMethod", type=StringType)
myDsl_Method_declaration_lParen: Property = Property(name="lParen", type=StringType)
myDsl_Method_declaration_rparent: Property = Property(name="rparent", type=StringType)
myDsl_Method_declaration_debug: Property = Property(name="debug", type=StringType)
myDsl_Method_declaration.attributes={myDsl_Method_declaration_lParen, myDsl_Method_declaration_modifiersMethod, myDsl_Method_declaration_debug, myDsl_Method_declaration_rparent, myDsl_Method_declaration_nameMethod}

# myDsl_Variable_declarator class attributes and methods
myDsl_Variable_declarator_nameVariable: Property = Property(name="nameVariable", type=StringType)
myDsl_Variable_declarator_lenVector: Property = Property(name="lenVector", type=StringType)
myDsl_Variable_declarator.attributes={myDsl_Variable_declarator_lenVector, myDsl_Variable_declarator_nameVariable}

# myDsl_Statement_block class attributes and methods
myDsl_Statement_block_rCurly: Property = Property(name="rCurly", type=StringType)
myDsl_Statement_block_lCurly: Property = Property(name="lCurly", type=StringType)
myDsl_Statement_block.attributes={myDsl_Statement_block_rCurly, myDsl_Statement_block_lCurly}

# myDsl_Parameter class attributes and methods
myDsl_Parameter_parameterName: Property = Property(name="parameterName", type=StringType)
myDsl_Parameter.attributes={myDsl_Parameter_parameterName}

# myDsl_Statement class attributes and methods
myDsl_Statement_nameStatement: Property = Property(name="nameStatement", type=StringType)
myDsl_Statement_name: Property = Property(name="name", type=StringType)
myDsl_Statement_g: Property = Property(name="g", type=StringType)
myDsl_Statement_rparent: Property = Property(name="rparent", type=StringType)
myDsl_Statement_ret: Property = Property(name="ret", type=StringType)
myDsl_Statement.attributes={myDsl_Statement_g, myDsl_Statement_ret, myDsl_Statement_name, myDsl_Statement_rparent, myDsl_Statement_nameStatement}

# myDsl_Variable_initializer class attributes and methods

# myDsl_Array_initializer class attributes and methods

# myDsl_Expression class attributes and methods
myDsl_Expression_null: Property = Property(name="null", type=StringType)
myDsl_Expression_super: Property = Property(name="super", type=StringType)
myDsl_Expression_this: Property = Property(name="this", type=StringType)
myDsl_Expression_name: Property = Property(name="name", type=StringType)
myDsl_Expression.attributes={myDsl_Expression_this, myDsl_Expression_super, myDsl_Expression_null, myDsl_Expression_name}

# myDsl_Type_specifier class attributes and methods
myDsl_Type_specifier_primitiveType: Property = Property(name="primitiveType", type=StringType)
myDsl_Type_specifier_className: Property = Property(name="className", type=StringType)
myDsl_Type_specifier.attributes={myDsl_Type_specifier_className, myDsl_Type_specifier_primitiveType}

# myDsl_If_statement class attributes and methods
myDsl_If_statement_rparent: Property = Property(name="rparent", type=StringType)
myDsl_If_statement_lparen: Property = Property(name="lparen", type=StringType)
myDsl_If_statement.attributes={myDsl_If_statement_lparen, myDsl_If_statement_rparent}

# myDsl_Do_Statement class attributes and methods
myDsl_Do_Statement_lparent: Property = Property(name="lparent", type=StringType)
myDsl_Do_Statement_rparent: Property = Property(name="rparent", type=StringType)
myDsl_Do_Statement.attributes={myDsl_Do_Statement_lparent, myDsl_Do_Statement_rparent}

# myDsl_While_Statement class attributes and methods
myDsl_While_Statement_rparent: Property = Property(name="rparent", type=StringType)
myDsl_While_Statement.attributes={myDsl_While_Statement_rparent}

# myDsl_For_Statement class attributes and methods

# myDsl_Switch_statement class attributes and methods
myDsl_Switch_statement_lParen: Property = Property(name="lParen", type=StringType)
myDsl_Switch_statement_rparent: Property = Property(name="rparent", type=StringType)
myDsl_Switch_statement.attributes={myDsl_Switch_statement_lParen, myDsl_Switch_statement_rparent}

# myDsl_Try_statement class attributes and methods
myDsl_Try_statement_lParen: Property = Property(name="lParen", type=StringType)
myDsl_Try_statement_rparent: Property = Property(name="rparent", type=StringType)
myDsl_Try_statement.attributes={myDsl_Try_statement_lParen, myDsl_Try_statement_rparent}

# myDsl_Creating_Expression class attributes and methods
myDsl_Creating_Expression_className: Property = Property(name="className", type=StringType)
myDsl_Creating_Expression.attributes={myDsl_Creating_Expression_className}

# myDsl_Literal_Expression class attributes and methods
myDsl_Literal_Expression_exp: Property = Property(name="exp", type=StringType)
myDsl_Literal_Expression_exp1: Property = Property(name="exp1", type=IntegerType)
myDsl_Literal_Expression_string: Property = Property(name="string", type=StringType)
myDsl_Literal_Expression_charLit: Property = Property(name="charLit", type=StringType)
myDsl_Literal_Expression.attributes={myDsl_Literal_Expression_exp1, myDsl_Literal_Expression_charLit, myDsl_Literal_Expression_exp, myDsl_Literal_Expression_string}

# myDsl_Numeric_Expression_NR class attributes and methods
myDsl_Numeric_Expression_NR_sinal_numeric: Property = Property(name="sinal_numeric", type=StringType)
myDsl_Numeric_Expression_NR.attributes={myDsl_Numeric_Expression_NR_sinal_numeric}

# myDsl_Expression_aux class attributes and methods
myDsl_Expression_aux_bitSign: Property = Property(name="bitSign", type=StringType)
myDsl_Expression_aux_logicOp: Property = Property(name="logicOp", type=StringType)
myDsl_Expression_aux_name: Property = Property(name="name", type=StringType)
myDsl_Expression_aux_sgin: Property = Property(name="sgin", type=StringType)
myDsl_Expression_aux_numericSign: Property = Property(name="numericSign", type=StringType)
myDsl_Expression_aux_testingSign: Property = Property(name="testingSign", type=StringType)
myDsl_Expression_aux_logicalSign: Property = Property(name="logicalSign", type=StringType)
myDsl_Expression_aux_stringSign: Property = Property(name="stringSign", type=StringType)
myDsl_Expression_aux.attributes={myDsl_Expression_aux_stringSign, myDsl_Expression_aux_logicalSign, myDsl_Expression_aux_numericSign, myDsl_Expression_aux_bitSign, myDsl_Expression_aux_name, myDsl_Expression_aux_logicOp, myDsl_Expression_aux_testingSign, myDsl_Expression_aux_sgin}

# myDsl_Logical_Expression_NR class attributes and methods
myDsl_Logical_Expression_NR_exclamation: Property = Property(name="exclamation", type=StringType)
myDsl_Logical_Expression_NR_true: Property = Property(name="true", type=StringType)
myDsl_Logical_Expression_NR_false: Property = Property(name="false", type=StringType)
myDsl_Logical_Expression_NR.attributes={myDsl_Logical_Expression_NR_true, myDsl_Logical_Expression_NR_false, myDsl_Logical_Expression_NR_exclamation}

# myDsl_Bit_Expression_NR class attributes and methods

# myDsl_Cast_Expression class attributes and methods

# myDsl_Float_Literal class attributes and methods
myDsl_Float_Literal_decimalDigits1: Property = Property(name="decimalDigits1", type=IntegerType)
myDsl_Float_Literal_decimalDigits2: Property = Property(name="decimalDigits2", type=IntegerType)
myDsl_Float_Literal_exp: Property = Property(name="exp", type=StringType)
myDsl_Float_Literal_floatTypeSufix: Property = Property(name="floatTypeSufix", type=StringType)
myDsl_Float_Literal.attributes={myDsl_Float_Literal_decimalDigits2, myDsl_Float_Literal_decimalDigits1, myDsl_Float_Literal_floatTypeSufix, myDsl_Float_Literal_exp}

# myDsl_Arg_List class attributes and methods

# myDsl_Ampersand_Rule class attributes and methods
myDsl_Ampersand_Rule_a1: Property = Property(name="a1", type=StringType)
myDsl_Ampersand_Rule_a2: Property = Property(name="a2", type=StringType)
myDsl_Ampersand_Rule.attributes={myDsl_Ampersand_Rule_a1, myDsl_Ampersand_Rule_a2}

# Relationships
typeDeclarations5: BinaryAssociation = BinaryAssociation(
    name="typeDeclarations5",
    ends={
        Property(name="myDsl_Type_declaration", type=myDsl_Compilation_unit, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Compilation_unit6", type=myDsl_Type_declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classDec7: BinaryAssociation = BinaryAssociation(
    name="classDec7",
    ends={
        Property(name="myDsl_Class_declaration", type=myDsl_Type_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Type_declaration8", type=myDsl_Class_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
interfaceDec9: BinaryAssociation = BinaryAssociation(
    name="interfaceDec9",
    ends={
        Property(name="myDsl_Interface_declaration", type=myDsl_Type_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Type_declaration10", type=myDsl_Interface_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
greetings0: BinaryAssociation = BinaryAssociation(
    name="greetings0",
    ends={
        Property(name="myDsl_Compilation_unit", type=myDsl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Model", type=myDsl_Compilation_unit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name1: BinaryAssociation = BinaryAssociation(
    name="name1",
    ends={
        Property(name="myDsl_Package_statement", type=myDsl_Compilation_unit, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Compilation_unit2", type=myDsl_Package_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
methodName20: BinaryAssociation = BinaryAssociation(
    name="methodName20",
    ends={
        Property(name="myDsl_Method_declaration", type=myDsl_Field_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Field_declaration21", type=myDsl_Method_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports3: BinaryAssociation = BinaryAssociation(
    name="imports3",
    ends={
        Property(name="myDsl_Import_statement", type=myDsl_Compilation_unit, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Compilation_unit4", type=myDsl_Import_statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
staticinitializer22: BinaryAssociation = BinaryAssociation(
    name="staticinitializer22",
    ends={
        Property(name="myDsl_Static_initializer", type=myDsl_Field_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Field_declaration23", type=myDsl_Static_initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeMethod24: BinaryAssociation = BinaryAssociation(
    name="typeMethod24",
    ends={
        Property(name="myDsl_Type", type=myDsl_Method_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Method_declaration25", type=myDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterListMethod26: BinaryAssociation = BinaryAssociation(
    name="parameterListMethod26",
    ends={
        Property(name="myDsl_Parameter_list", type=myDsl_Method_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Method_declaration27", type=myDsl_Parameter_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fieldsDeclaration11: BinaryAssociation = BinaryAssociation(
    name="fieldsDeclaration11",
    ends={
        Property(name="myDsl_Field_declaration", type=myDsl_Interface_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Interface_declaration12", type=myDsl_Field_declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fieldsDeclaration13: BinaryAssociation = BinaryAssociation(
    name="fieldsDeclaration13",
    ends={
        Property(name="myDsl_Field_declaration15", type=myDsl_Class_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Class_declaration14", type=myDsl_Field_declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableDeclaration16: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration16",
    ends={
        Property(name="myDsl_Variable_declaration", type=myDsl_Field_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Field_declaration17", type=myDsl_Variable_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contructorName18: BinaryAssociation = BinaryAssociation(
    name="contructorName18",
    ends={
        Property(name="myDsl_Constructor_declaration", type=myDsl_Field_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Field_declaration19", type=myDsl_Constructor_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type44: BinaryAssociation = BinaryAssociation(
    name="type44",
    ends={
        Property(name="myDsl_Type46", type=myDsl_Variable_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Variable_declaration45", type=myDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nameVariable47: BinaryAssociation = BinaryAssociation(
    name="nameVariable47",
    ends={
        Property(name="myDsl_Variable_declarator", type=myDsl_Variable_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Variable_declaration48", type=myDsl_Variable_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
names49: BinaryAssociation = BinaryAssociation(
    name="names49",
    ends={
        Property(name="myDsl_Variable_declarator51", type=myDsl_Variable_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Variable_declaration50", type=myDsl_Variable_declarator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statementMethod28: BinaryAssociation = BinaryAssociation(
    name="statementMethod28",
    ends={
        Property(name="myDsl_Statement_block", type=myDsl_Method_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Method_declaration29", type=myDsl_Statement_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterListConstructor30: BinaryAssociation = BinaryAssociation(
    name="parameterListConstructor30",
    ends={
        Property(name="myDsl_Parameter_list32", type=myDsl_Constructor_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Constructor_declaration31", type=myDsl_Parameter_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statementConstructor33: BinaryAssociation = BinaryAssociation(
    name="statementConstructor33",
    ends={
        Property(name="myDsl_Statement_block35", type=myDsl_Constructor_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Constructor_declaration34", type=myDsl_Statement_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter36: BinaryAssociation = BinaryAssociation(
    name="parameter36",
    ends={
        Property(name="myDsl_Parameter", type=myDsl_Parameter_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Parameter_list37", type=myDsl_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters38: BinaryAssociation = BinaryAssociation(
    name="parameters38",
    ends={
        Property(name="myDsl_Parameter40", type=myDsl_Parameter_list, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Parameter_list39", type=myDsl_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type41: BinaryAssociation = BinaryAssociation(
    name="type41",
    ends={
        Property(name="myDsl_Type43", type=myDsl_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Parameter42", type=myDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statments66: BinaryAssociation = BinaryAssociation(
    name="statments66",
    ends={
        Property(name="myDsl_Statement", type=myDsl_Statement_block, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement_block67", type=myDsl_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableDeclaration68: BinaryAssociation = BinaryAssociation(
    name="variableDeclaration68",
    ends={
        Property(name="myDsl_Variable_declaration70", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement69", type=myDsl_Variable_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionStatement71: BinaryAssociation = BinaryAssociation(
    name="expressionStatement71",
    ends={
        Property(name="myDsl_Expression73", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement72", type=myDsl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
vari52: BinaryAssociation = BinaryAssociation(
    name="vari52",
    ends={
        Property(name="myDsl_Variable_initializer", type=myDsl_Variable_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Variable_declarator53", type=myDsl_Variable_initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array_init54: BinaryAssociation = BinaryAssociation(
    name="array_init54",
    ends={
        Property(name="myDsl_Array_initializer", type=myDsl_Variable_initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Variable_initializer55", type=myDsl_Array_initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression56: BinaryAssociation = BinaryAssociation(
    name="expression56",
    ends={
        Property(name="myDsl_Expression", type=myDsl_Variable_initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Variable_initializer57", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableinitializer58: BinaryAssociation = BinaryAssociation(
    name="variableinitializer58",
    ends={
        Property(name="myDsl_Variable_initializer60", type=myDsl_Array_initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Array_initializer59", type=myDsl_Variable_initializer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeSpecifier61: BinaryAssociation = BinaryAssociation(
    name="typeSpecifier61",
    ends={
        Property(name="myDsl_Type_specifier", type=myDsl_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Type62", type=myDsl_Type_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name63: BinaryAssociation = BinaryAssociation(
    name="name63",
    ends={
        Property(name="myDsl_Statement_block65", type=myDsl_Static_initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Static_initializer64", type=myDsl_Statement_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tryStatement93: BinaryAssociation = BinaryAssociation(
    name="tryStatement93",
    ends={
        Property(name="myDsl_Try_statement", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement94", type=myDsl_Try_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement96: BinaryAssociation = BinaryAssociation(
    name="statement96",
    ends={
        Property(name="myDsl_Statement97", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement95", type=myDsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable98: BinaryAssociation = BinaryAssociation(
    name="variable98",
    ends={
        Property(name="myDsl_Variable_declaration100", type=myDsl_For_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_For_Statement99", type=myDsl_Variable_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression101: BinaryAssociation = BinaryAssociation(
    name="expression101",
    ends={
        Property(name="myDsl_Expression103", type=myDsl_For_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_For_Statement102", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression2104: BinaryAssociation = BinaryAssociation(
    name="expression2104",
    ends={
        Property(name="myDsl_Expression106", type=myDsl_For_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_For_Statement105", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifStatement74: BinaryAssociation = BinaryAssociation(
    name="ifStatement74",
    ends={
        Property(name="myDsl_If_statement", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement75", type=myDsl_If_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doStatement76: BinaryAssociation = BinaryAssociation(
    name="doStatement76",
    ends={
        Property(name="myDsl_Do_Statement", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement77", type=myDsl_Do_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whileStatement78: BinaryAssociation = BinaryAssociation(
    name="whileStatement78",
    ends={
        Property(name="myDsl_While_Statement", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement79", type=myDsl_While_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forStatement80: BinaryAssociation = BinaryAssociation(
    name="forStatement80",
    ends={
        Property(name="myDsl_For_Statement", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement81", type=myDsl_For_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switchStatement82: BinaryAssociation = BinaryAssociation(
    name="switchStatement82",
    ends={
        Property(name="myDsl_Switch_statement", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement83", type=myDsl_Switch_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression84: BinaryAssociation = BinaryAssociation(
    name="expression84",
    ends={
        Property(name="myDsl_Expression86", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement85", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
syncStatement88: BinaryAssociation = BinaryAssociation(
    name="syncStatement88",
    ends={
        Property(name="myDsl_Statement89", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement87", type=myDsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statementBlock90: BinaryAssociation = BinaryAssociation(
    name="statementBlock90",
    ends={
        Property(name="myDsl_Statement_block92", type=myDsl_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Statement91", type=myDsl_Statement_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
creatingExpression123: BinaryAssociation = BinaryAssociation(
    name="creatingExpression123",
    ends={
        Property(name="myDsl_Creating_Expression", type=myDsl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression124", type=myDsl_Creating_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literalExpression125: BinaryAssociation = BinaryAssociation(
    name="literalExpression125",
    ends={
        Property(name="myDsl_Literal_Expression", type=myDsl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression126", type=myDsl_Literal_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression3107: BinaryAssociation = BinaryAssociation(
    name="expression3107",
    ends={
        Property(name="myDsl_Expression109", type=myDsl_For_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_For_Statement108", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement110: BinaryAssociation = BinaryAssociation(
    name="statement110",
    ends={
        Property(name="myDsl_Statement112", type=myDsl_For_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_For_Statement111", type=myDsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
numericExpression3113: BinaryAssociation = BinaryAssociation(
    name="numericExpression3113",
    ends={
        Property(name="myDsl_Numeric_Expression_NR", type=myDsl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression114", type=myDsl_Numeric_Expression_NR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aux115: BinaryAssociation = BinaryAssociation(
    name="aux115",
    ends={
        Property(name="myDsl_Expression_aux", type=myDsl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression116", type=myDsl_Expression_aux, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logicalExpression117: BinaryAssociation = BinaryAssociation(
    name="logicalExpression117",
    ends={
        Property(name="myDsl_Logical_Expression_NR", type=myDsl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression118", type=myDsl_Logical_Expression_NR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bitExpression119: BinaryAssociation = BinaryAssociation(
    name="bitExpression119",
    ends={
        Property(name="myDsl_Bit_Expression_NR", type=myDsl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression120", type=myDsl_Bit_Expression_NR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
castExpression121: BinaryAssociation = BinaryAssociation(
    name="castExpression121",
    ends={
        Property(name="myDsl_Cast_Expression", type=myDsl_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression122", type=myDsl_Cast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionBit146: BinaryAssociation = BinaryAssociation(
    name="expressionBit146",
    ends={
        Property(name="myDsl_Expression148", type=myDsl_Expression_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression_aux147", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logicExp149: BinaryAssociation = BinaryAssociation(
    name="logicExp149",
    ends={
        Property(name="myDsl_Expression151", type=myDsl_Expression_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression_aux150", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp2152: BinaryAssociation = BinaryAssociation(
    name="exp2152",
    ends={
        Property(name="myDsl_Float_Literal", type=myDsl_Literal_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Literal_Expression153", type=myDsl_Float_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argList127: BinaryAssociation = BinaryAssociation(
    name="argList127",
    ends={
        Property(name="myDsl_Arg_List", type=myDsl_Expression_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression_aux128", type=myDsl_Arg_List, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aux130: BinaryAssociation = BinaryAssociation(
    name="aux130",
    ends={
        Property(name="myDsl_Expression_aux131", type=myDsl_Expression_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression_aux129", type=myDsl_Expression_aux, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression2132: BinaryAssociation = BinaryAssociation(
    name="expression2132",
    ends={
        Property(name="myDsl_Expression134", type=myDsl_Expression_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression_aux133", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionComma135: BinaryAssociation = BinaryAssociation(
    name="expressionComma135",
    ends={
        Property(name="myDsl_Expression137", type=myDsl_Expression_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression_aux136", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp2138: BinaryAssociation = BinaryAssociation(
    name="exp2138",
    ends={
        Property(name="myDsl_Expression140", type=myDsl_Expression_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression_aux139", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp1141: BinaryAssociation = BinaryAssociation(
    name="exp1141",
    ends={
        Property(name="myDsl_Expression143", type=myDsl_Expression_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression_aux142", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ampersand144: BinaryAssociation = BinaryAssociation(
    name="ampersand144",
    ends={
        Property(name="myDsl_Ampersand_Rule", type=myDsl_Expression_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Expression_aux145", type=myDsl_Ampersand_Rule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression181: BinaryAssociation = BinaryAssociation(
    name="expression181",
    ends={
        Property(name="myDsl_Expression183", type=myDsl_Numeric_Expression_NR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Numeric_Expression_NR182", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression184: BinaryAssociation = BinaryAssociation(
    name="expression184",
    ends={
        Property(name="myDsl_Expression186", type=myDsl_Switch_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Switch_statement185", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression2187: BinaryAssociation = BinaryAssociation(
    name="expression2187",
    ends={
        Property(name="myDsl_Expression189", type=myDsl_Switch_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Switch_statement188", type=myDsl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
switchStatements190: BinaryAssociation = BinaryAssociation(
    name="switchStatements190",
    ends={
        Property(name="myDsl_Statement192", type=myDsl_Switch_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Switch_statement191", type=myDsl_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argList154: BinaryAssociation = BinaryAssociation(
    name="argList154",
    ends={
        Property(name="myDsl_Arg_List156", type=myDsl_Creating_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Creating_Expression155", type=myDsl_Arg_List, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeSpecifier157: BinaryAssociation = BinaryAssociation(
    name="typeSpecifier157",
    ends={
        Property(name="myDsl_Type_specifier159", type=myDsl_Creating_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Creating_Expression158", type=myDsl_Type_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression160: BinaryAssociation = BinaryAssociation(
    name="expression160",
    ends={
        Property(name="myDsl_Expression162", type=myDsl_Creating_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Creating_Expression161", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type163: BinaryAssociation = BinaryAssociation(
    name="type163",
    ends={
        Property(name="myDsl_Type165", type=myDsl_Cast_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Cast_Expression164", type=myDsl_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression166: BinaryAssociation = BinaryAssociation(
    name="expression166",
    ends={
        Property(name="myDsl_Expression168", type=myDsl_Cast_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Cast_Expression167", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression169: BinaryAssociation = BinaryAssociation(
    name="expression169",
    ends={
        Property(name="myDsl_Expression171", type=myDsl_Bit_Expression_NR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Bit_Expression_NR170", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression172: BinaryAssociation = BinaryAssociation(
    name="expression172",
    ends={
        Property(name="myDsl_Expression174", type=myDsl_Logical_Expression_NR, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Logical_Expression_NR173", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression175: BinaryAssociation = BinaryAssociation(
    name="expression175",
    ends={
        Property(name="myDsl_Expression177", type=myDsl_Arg_List, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Arg_List176", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions178: BinaryAssociation = BinaryAssociation(
    name="expressions178",
    ends={
        Property(name="myDsl_Expression180", type=myDsl_Arg_List, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Arg_List179", type=myDsl_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
idStatement205: BinaryAssociation = BinaryAssociation(
    name="idStatement205",
    ends={
        Property(name="myDsl_Statement207", type=myDsl_If_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_If_statement206", type=myDsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseStatement208: BinaryAssociation = BinaryAssociation(
    name="elseStatement208",
    ends={
        Property(name="myDsl_Statement210", type=myDsl_If_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_If_statement209", type=myDsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression193: BinaryAssociation = BinaryAssociation(
    name="expression193",
    ends={
        Property(name="myDsl_Expression195", type=myDsl_While_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_While_Statement194", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whileStatement196: BinaryAssociation = BinaryAssociation(
    name="whileStatement196",
    ends={
        Property(name="myDsl_Statement198", type=myDsl_While_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_While_Statement197", type=myDsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doStatement199: BinaryAssociation = BinaryAssociation(
    name="doStatement199",
    ends={
        Property(name="myDsl_Statement201", type=myDsl_Do_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Do_Statement200", type=myDsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression202: BinaryAssociation = BinaryAssociation(
    name="expression202",
    ends={
        Property(name="myDsl_Expression204", type=myDsl_If_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_If_statement203", type=myDsl_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tryStatement211: BinaryAssociation = BinaryAssociation(
    name="tryStatement211",
    ends={
        Property(name="myDsl_Statement213", type=myDsl_Try_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Try_statement212", type=myDsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters214: BinaryAssociation = BinaryAssociation(
    name="parameters214",
    ends={
        Property(name="myDsl_Parameter216", type=myDsl_Try_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Try_statement215", type=myDsl_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catchStatement217: BinaryAssociation = BinaryAssociation(
    name="catchStatement217",
    ends={
        Property(name="myDsl_Statement219", type=myDsl_Try_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Try_statement218", type=myDsl_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
finallyStatement220: BinaryAssociation = BinaryAssociation(
    name="finallyStatement220",
    ends={
        Property(name="myDsl_Statement222", type=myDsl_Try_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="myDsl_Try_statement221", type=myDsl_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="myDsl",
    types={myDsl_Type_declaration, myDsl_Class_declaration, myDsl_Interface_declaration, myDsl_Model, myDsl_Compilation_unit, myDsl_Package_statement, myDsl_Import_statement, myDsl_Static_initializer, myDsl_Type, myDsl_Parameter_list, myDsl_Field_declaration, myDsl_Variable_declaration, myDsl_Constructor_declaration, myDsl_Method_declaration, myDsl_Variable_declarator, myDsl_Statement_block, myDsl_Parameter, myDsl_Statement, myDsl_Variable_initializer, myDsl_Array_initializer, myDsl_Expression, myDsl_Type_specifier, myDsl_If_statement, myDsl_Do_Statement, myDsl_While_Statement, myDsl_For_Statement, myDsl_Switch_statement, myDsl_Try_statement, myDsl_Creating_Expression, myDsl_Literal_Expression, myDsl_Numeric_Expression_NR, myDsl_Expression_aux, myDsl_Logical_Expression_NR, myDsl_Bit_Expression_NR, myDsl_Cast_Expression, myDsl_Float_Literal, myDsl_Arg_List, myDsl_Ampersand_Rule},
    associations={typeDeclarations5, classDec7, interfaceDec9, greetings0, name1, methodName20, imports3, staticinitializer22, typeMethod24, parameterListMethod26, fieldsDeclaration11, fieldsDeclaration13, variableDeclaration16, contructorName18, type44, nameVariable47, names49, statementMethod28, parameterListConstructor30, statementConstructor33, parameter36, parameters38, type41, statments66, variableDeclaration68, expressionStatement71, vari52, array_init54, expression56, variableinitializer58, typeSpecifier61, name63, tryStatement93, statement96, variable98, expression101, expression2104, ifStatement74, doStatement76, whileStatement78, forStatement80, switchStatement82, expression84, syncStatement88, statementBlock90, creatingExpression123, literalExpression125, expression3107, statement110, numericExpression3113, aux115, logicalExpression117, bitExpression119, castExpression121, expressionBit146, logicExp149, exp2152, argList127, aux130, expression2132, expressionComma135, exp2138, exp1141, ampersand144, expression181, expression184, expression2187, switchStatements190, argList154, typeSpecifier157, expression160, type163, expression166, expression169, expression172, expression175, expressions178, idStatement205, elseStatement208, expression193, whileStatement196, doStatement199, expression202, tryStatement211, parameters214, catchStatement217, finallyStatement220},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)