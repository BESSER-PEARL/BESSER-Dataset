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
java_Head = Class(name="java::Head")
java_Type_declaration = Class(name="java::Type::declaration")
java_EObject = Class(name="java::EObject")
java_Interface_declaration = Class(name="java::Interface::declaration")
java_Compilation_unit = Class(name="java::Compilation::unit")
java_Package_statement = Class(name="java::Package::statement")
java_Import_statement = Class(name="java::Import::statement")
java_Method_declaration = Class(name="java::Method::declaration")
java_Field_declaration = Class(name="java::Field::declaration")
java_Class_declaration = Class(name="java::Class::declaration")
java_Parameter = Class(name="java::Parameter")
java_Type = Class(name="java::Type")
java_Parameter_list = Class(name="java::Parameter::list")
java_Statement_block = Class(name="java::Statement::block")
java_Method_call = Class(name="java::Method::call")
Return_value = Class(name="Return::value")
java_Parameter_list_method_call = Class(name="java::Parameter::list::method::call")
java_Constructor_declaration = Class(name="java::Constructor::declaration")
java_Variable_initializer = Class(name="java::Variable::initializer")
java_Expression = Class(name="java::Expression")
java_Variable_declaration = Class(name="java::Variable::declaration")
java_Variable_declarator = Class(name="java::Variable::declarator")
java_Literal_Expression = Class(name="java::Literal::Expression")
java_Arg_List = Class(name="java::Arg::List")
java_Numeric_Expression_NR = Class(name="java::Numeric::Expression::NR")
java_Expression_aux = Class(name="java::Expression::aux")
java_Logical_Expression_NR = Class(name="java::Logical::Expression::NR")
java_Bit_Expression_NR = Class(name="java::Bit::Expression::NR")
java_Cast_Expression = Class(name="java::Cast::Expression")
java_Creating_Expression = Class(name="java::Creating::Expression")
java_Ampersand_Rule = Class(name="java::Ampersand::Rule")
java_Float_Literal = Class(name="java::Float::Literal")
java_Static_initializer = Class(name="java::Static::initializer")
Statement = Class(name="Statement")
java_Return_Statement = Class(name="java::Return::Statement")
java_If_Statement = Class(name="java::If::Statement")
java_Do_Statement = Class(name="java::Do::Statement")
java_While_Statement = Class(name="java::While::Statement")
java_For_Statement = Class(name="java::For::Statement")
java_Switch_Statement = Class(name="java::Switch::Statement")
java_Statement = Class(name="java::Statement")
java_Try_statement = Class(name="java::Try::statement")
java_Return_value = Class(name="java::Return::value")

# java_Head class attributes and methods

# java_Type_declaration class attributes and methods
java_Type_declaration_doc: Property = Property(name="doc", type=StringType)
java_Type_declaration.attributes={java_Type_declaration_doc}

# java_EObject class attributes and methods

# java_Interface_declaration class attributes and methods
java_Interface_declaration_modifiers: Property = Property(name="modifiers", type=StringType)
java_Interface_declaration_interfaceName: Property = Property(name="interfaceName", type=StringType)
java_Interface_declaration_extend: Property = Property(name="extend", type=StringType)
java_Interface_declaration_extends: Property = Property(name="extends", type=StringType)
java_Interface_declaration.attributes={java_Interface_declaration_interfaceName, java_Interface_declaration_extend, java_Interface_declaration_extends, java_Interface_declaration_modifiers}

# java_Compilation_unit class attributes and methods

# java_Package_statement class attributes and methods
java_Package_statement_name: Property = Property(name="name", type=StringType)
java_Package_statement.attributes={java_Package_statement_name}

# java_Import_statement class attributes and methods
java_Import_statement_classname: Property = Property(name="classname", type=StringType)
java_Import_statement_packagename: Property = Property(name="packagename", type=StringType)
java_Import_statement.attributes={java_Import_statement_packagename, java_Import_statement_classname}

# java_Method_declaration class attributes and methods
java_Method_declaration_modifiers: Property = Property(name="modifiers", type=StringType)
java_Method_declaration_name: Property = Property(name="name", type=StringType)
java_Method_declaration_debug: Property = Property(name="debug", type=StringType)
java_Method_declaration.attributes={java_Method_declaration_name, java_Method_declaration_modifiers, java_Method_declaration_debug}

# java_Field_declaration class attributes and methods
java_Field_declaration_doc: Property = Property(name="doc", type=StringType)
java_Field_declaration_debug: Property = Property(name="debug", type=StringType)
java_Field_declaration.attributes={java_Field_declaration_doc, java_Field_declaration_debug}

# java_Class_declaration class attributes and methods
java_Class_declaration_implements: Property = Property(name="implements", type=StringType)
java_Class_declaration_modifiers: Property = Property(name="modifiers", type=StringType)
java_Class_declaration_className: Property = Property(name="className", type=StringType)
java_Class_declaration_extend: Property = Property(name="extend", type=StringType)
java_Class_declaration_implement: Property = Property(name="implement", type=StringType)
java_Class_declaration.attributes={java_Class_declaration_implement, java_Class_declaration_className, java_Class_declaration_extend, java_Class_declaration_implements, java_Class_declaration_modifiers}

# java_Parameter class attributes and methods
java_Parameter_name: Property = Property(name="name", type=StringType)
java_Parameter.attributes={java_Parameter_name}

# java_Type class attributes and methods
java_Type_name: Property = Property(name="name", type=StringType)
java_Type.attributes={java_Type_name}

# java_Parameter_list class attributes and methods

# java_Statement_block class attributes and methods

# java_Method_call class attributes and methods

# Return_value class attributes and methods

# java_Parameter_list_method_call class attributes and methods
java_Parameter_list_method_call_name: Property = Property(name="name", type=StringType)
java_Parameter_list_method_call_parameters: Property = Property(name="parameters", type=StringType)
java_Parameter_list_method_call.attributes={java_Parameter_list_method_call_name, java_Parameter_list_method_call_parameters}

# java_Constructor_declaration class attributes and methods
java_Constructor_declaration_modifiers: Property = Property(name="modifiers", type=StringType)
java_Constructor_declaration_name: Property = Property(name="name", type=StringType)
java_Constructor_declaration.attributes={java_Constructor_declaration_name, java_Constructor_declaration_modifiers}

# java_Variable_initializer class attributes and methods

# java_Expression class attributes and methods
java_Expression_null: Property = Property(name="null", type=StringType)
java_Expression_super: Property = Property(name="super", type=StringType)
java_Expression_this: Property = Property(name="this", type=StringType)
java_Expression_name: Property = Property(name="name", type=StringType)
java_Expression.attributes={java_Expression_super, java_Expression_name, java_Expression_null, java_Expression_this}

# java_Variable_declaration class attributes and methods
java_Variable_declaration_modifiers: Property = Property(name="modifiers", type=StringType)
java_Variable_declaration.attributes={java_Variable_declaration_modifiers}

# java_Variable_declarator class attributes and methods
java_Variable_declarator_name: Property = Property(name="name", type=StringType)
java_Variable_declarator.attributes={java_Variable_declarator_name}

# java_Literal_Expression class attributes and methods
java_Literal_Expression_string: Property = Property(name="string", type=StringType)
java_Literal_Expression_char: Property = Property(name="char", type=StringType)
java_Literal_Expression_exp: Property = Property(name="exp", type=StringType)
java_Literal_Expression_exp1: Property = Property(name="exp1", type=IntegerType)
java_Literal_Expression.attributes={java_Literal_Expression_exp1, java_Literal_Expression_string, java_Literal_Expression_exp, java_Literal_Expression_char}

# java_Arg_List class attributes and methods

# java_Numeric_Expression_NR class attributes and methods
java_Numeric_Expression_NR_sinal_numeric: Property = Property(name="sinal_numeric", type=StringType)
java_Numeric_Expression_NR.attributes={java_Numeric_Expression_NR_sinal_numeric}

# java_Expression_aux class attributes and methods
java_Expression_aux_logicalSign: Property = Property(name="logicalSign", type=StringType)
java_Expression_aux_stringSign: Property = Property(name="stringSign", type=StringType)
java_Expression_aux_bitSign: Property = Property(name="bitSign", type=StringType)
java_Expression_aux_name: Property = Property(name="name", type=StringType)
java_Expression_aux_sgin: Property = Property(name="sgin", type=StringType)
java_Expression_aux_numericSign: Property = Property(name="numericSign", type=StringType)
java_Expression_aux_testingSign: Property = Property(name="testingSign", type=StringType)
java_Expression_aux.attributes={java_Expression_aux_testingSign, java_Expression_aux_stringSign, java_Expression_aux_numericSign, java_Expression_aux_bitSign, java_Expression_aux_sgin, java_Expression_aux_logicalSign, java_Expression_aux_name}

# java_Logical_Expression_NR class attributes and methods
java_Logical_Expression_NR_true: Property = Property(name="true", type=StringType)
java_Logical_Expression_NR_false: Property = Property(name="false", type=StringType)
java_Logical_Expression_NR.attributes={java_Logical_Expression_NR_true, java_Logical_Expression_NR_false}

# java_Bit_Expression_NR class attributes and methods

# java_Cast_Expression class attributes and methods

# java_Creating_Expression class attributes and methods
java_Creating_Expression_className: Property = Property(name="className", type=StringType)
java_Creating_Expression_typeSpecifier: Property = Property(name="typeSpecifier", type=StringType)
java_Creating_Expression.attributes={java_Creating_Expression_className, java_Creating_Expression_typeSpecifier}

# java_Ampersand_Rule class attributes and methods
java_Ampersand_Rule_a1: Property = Property(name="a1", type=StringType)
java_Ampersand_Rule_a2: Property = Property(name="a2", type=StringType)
java_Ampersand_Rule.attributes={java_Ampersand_Rule_a2, java_Ampersand_Rule_a1}

# java_Float_Literal class attributes and methods
java_Float_Literal_decimalDigits1: Property = Property(name="decimalDigits1", type=IntegerType)
java_Float_Literal_decimalDigits2: Property = Property(name="decimalDigits2", type=IntegerType)
java_Float_Literal_exp: Property = Property(name="exp", type=StringType)
java_Float_Literal_floatTypeSufix: Property = Property(name="floatTypeSufix", type=StringType)
java_Float_Literal.attributes={java_Float_Literal_decimalDigits1, java_Float_Literal_floatTypeSufix, java_Float_Literal_decimalDigits2, java_Float_Literal_exp}

# java_Static_initializer class attributes and methods
java_Static_initializer_static: Property = Property(name="static", type=StringType)
java_Static_initializer.attributes={java_Static_initializer_static}

# Statement class attributes and methods

# java_Return_Statement class attributes and methods

# java_If_Statement class attributes and methods

# java_Do_Statement class attributes and methods

# java_While_Statement class attributes and methods

# java_For_Statement class attributes and methods
java_For_Statement_pv: Property = Property(name="pv", type=StringType)
java_For_Statement.attributes={java_For_Statement_pv}

# java_Switch_Statement class attributes and methods

# java_Statement class attributes and methods
java_Statement_name: Property = Property(name="name", type=StringType)
java_Statement.attributes={java_Statement_name}

# java_Try_statement class attributes and methods
java_Try_statement_try: Property = Property(name="try", type=StringType)
java_Try_statement_catchs: Property = Property(name="catchs", type=StringType)
java_Try_statement_finally: Property = Property(name="finally", type=StringType)
java_Try_statement.attributes={java_Try_statement_catchs, java_Try_statement_finally, java_Try_statement_try}

# java_Return_value class attributes and methods
java_Return_value_name: Property = Property(name="name", type=StringType)
java_Return_value.attributes={java_Return_value_name}

# Relationships
type_declarations5: BinaryAssociation = BinaryAssociation(
    name="type_declarations5",
    ends={
        Property(name="java_Type_declaration", type=java_Compilation_unit, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Compilation_unit6", type=java_Type_declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name7: BinaryAssociation = BinaryAssociation(
    name="name7",
    ends={
        Property(name="java_EObject", type=java_Type_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Type_declaration8", type=java_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="java_Compilation_unit", type=java_Head, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Head", type=java_Compilation_unit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package1: BinaryAssociation = BinaryAssociation(
    name="package1",
    ends={
        Property(name="java_Package_statement", type=java_Compilation_unit, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Compilation_unit2", type=java_Package_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
imports3: BinaryAssociation = BinaryAssociation(
    name="imports3",
    ends={
        Property(name="java_Import_statement", type=java_Compilation_unit, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Compilation_unit4", type=java_Import_statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields10: BinaryAssociation = BinaryAssociation(
    name="fields10",
    ends={
        Property(name="java_Field_declaration11", type=java_Class_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Class_declaration", type=java_Field_declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name12: BinaryAssociation = BinaryAssociation(
    name="name12",
    ends={
        Property(name="java_EObject14", type=java_Field_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Field_declaration13", type=java_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fields9: BinaryAssociation = BinaryAssociation(
    name="fields9",
    ends={
        Property(name="java_Field_declaration", type=java_Interface_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Interface_declaration", type=java_Field_declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters21: BinaryAssociation = BinaryAssociation(
    name="parameters21",
    ends={
        Property(name="java_Parameter_list22", type=java_Constructor_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Constructor_declaration", type=java_Parameter_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement23: BinaryAssociation = BinaryAssociation(
    name="statement23",
    ends={
        Property(name="java_Statement_block25", type=java_Constructor_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Constructor_declaration24", type=java_Statement_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter26: BinaryAssociation = BinaryAssociation(
    name="parameter26",
    ends={
        Property(name="java_Parameter", type=java_Parameter_list, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Parameter_list27", type=java_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type15: BinaryAssociation = BinaryAssociation(
    name="type15",
    ends={
        Property(name="java_Type", type=java_Method_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Method_declaration", type=java_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter16: BinaryAssociation = BinaryAssociation(
    name="parameter16",
    ends={
        Property(name="java_Parameter_list", type=java_Method_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Method_declaration17", type=java_Parameter_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement18: BinaryAssociation = BinaryAssociation(
    name="statement18",
    ends={
        Property(name="java_Statement_block", type=java_Method_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Method_declaration19", type=java_Statement_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter20: BinaryAssociation = BinaryAssociation(
    name="parameter20",
    ends={
        Property(name="java_Parameter_list_method_call", type=java_Method_call, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Method_call", type=java_Parameter_list_method_call, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
names38: BinaryAssociation = BinaryAssociation(
    name="names38",
    ends={
        Property(name="java_Variable_declarator40", type=java_Variable_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Variable_declaration39", type=java_Variable_declarator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initializer41: BinaryAssociation = BinaryAssociation(
    name="initializer41",
    ends={
        Property(name="java_Variable_initializer", type=java_Variable_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Variable_declarator42", type=java_Variable_initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression43: BinaryAssociation = BinaryAssociation(
    name="expression43",
    ends={
        Property(name="java_Expression", type=java_Variable_initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Variable_initializer44", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableInitializer146: BinaryAssociation = BinaryAssociation(
    name="variableInitializer146",
    ends={
        Property(name="java_Variable_initializer47", type=java_Variable_initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Variable_initializer45", type=java_Variable_initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variableIniatializer249: BinaryAssociation = BinaryAssociation(
    name="variableIniatializer249",
    ends={
        Property(name="java_Variable_initializer50", type=java_Variable_initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Variable_initializer48", type=java_Variable_initializer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters28: BinaryAssociation = BinaryAssociation(
    name="parameters28",
    ends={
        Property(name="java_Parameter30", type=java_Parameter_list, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Parameter_list29", type=java_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type31: BinaryAssociation = BinaryAssociation(
    name="type31",
    ends={
        Property(name="java_Type33", type=java_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Parameter32", type=java_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type34: BinaryAssociation = BinaryAssociation(
    name="type34",
    ends={
        Property(name="java_Type35", type=java_Variable_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Variable_declaration", type=java_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name36: BinaryAssociation = BinaryAssociation(
    name="name36",
    ends={
        Property(name="java_Variable_declarator", type=java_Variable_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Variable_declaration37", type=java_Variable_declarator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
creatingExpression61: BinaryAssociation = BinaryAssociation(
    name="creatingExpression61",
    ends={
        Property(name="java_Expression62", type=java_Creating_Expression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="java_Creating_Expression", type=java_Expression, multiplicity=Multiplicity(1, 1))
    }
)
literalExpression63: BinaryAssociation = BinaryAssociation(
    name="literalExpression63",
    ends={
        Property(name="java_Literal_Expression", type=java_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Expression64", type=java_Literal_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argList65: BinaryAssociation = BinaryAssociation(
    name="argList65",
    ends={
        Property(name="java_Arg_List", type=java_Expression_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Expression_aux66", type=java_Arg_List, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
numericExpression351: BinaryAssociation = BinaryAssociation(
    name="numericExpression351",
    ends={
        Property(name="java_Numeric_Expression_NR", type=java_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Expression52", type=java_Numeric_Expression_NR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aux53: BinaryAssociation = BinaryAssociation(
    name="aux53",
    ends={
        Property(name="java_Expression_aux", type=java_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Expression54", type=java_Expression_aux, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logicalExpression55: BinaryAssociation = BinaryAssociation(
    name="logicalExpression55",
    ends={
        Property(name="java_Logical_Expression_NR", type=java_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Expression56", type=java_Logical_Expression_NR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bitExpression57: BinaryAssociation = BinaryAssociation(
    name="bitExpression57",
    ends={
        Property(name="java_Bit_Expression_NR", type=java_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Expression58", type=java_Bit_Expression_NR, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
castExpression59: BinaryAssociation = BinaryAssociation(
    name="castExpression59",
    ends={
        Property(name="java_Cast_Expression", type=java_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Expression60", type=java_Cast_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp176: BinaryAssociation = BinaryAssociation(
    name="exp176",
    ends={
        Property(name="java_Expression78", type=java_Expression_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Expression_aux77", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ampersand79: BinaryAssociation = BinaryAssociation(
    name="ampersand79",
    ends={
        Property(name="java_Ampersand_Rule", type=java_Expression_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Expression_aux80", type=java_Ampersand_Rule, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionBit81: BinaryAssociation = BinaryAssociation(
    name="expressionBit81",
    ends={
        Property(name="java_Expression83", type=java_Expression_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Expression_aux82", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
aux68: BinaryAssociation = BinaryAssociation(
    name="aux68",
    ends={
        Property(name="java_Expression_aux69", type=java_Expression_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Expression_aux67", type=java_Expression_aux, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression270: BinaryAssociation = BinaryAssociation(
    name="expression270",
    ends={
        Property(name="java_Expression72", type=java_Expression_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Expression_aux71", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp273: BinaryAssociation = BinaryAssociation(
    name="exp273",
    ends={
        Property(name="java_Expression75", type=java_Expression_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Expression_aux74", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp284: BinaryAssociation = BinaryAssociation(
    name="exp284",
    ends={
        Property(name="java_Literal_Expression85", type=java_Float_Literal, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="java_Float_Literal", type=java_Literal_Expression, multiplicity=Multiplicity(1, 1))
    }
)
argList86: BinaryAssociation = BinaryAssociation(
    name="argList86",
    ends={
        Property(name="java_Arg_List88", type=java_Creating_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Creating_Expression87", type=java_Arg_List, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression89: BinaryAssociation = BinaryAssociation(
    name="expression89",
    ends={
        Property(name="java_Expression91", type=java_Creating_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Creating_Expression90", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type92: BinaryAssociation = BinaryAssociation(
    name="type92",
    ends={
        Property(name="java_Type94", type=java_Cast_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Cast_Expression93", type=java_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression95: BinaryAssociation = BinaryAssociation(
    name="expression95",
    ends={
        Property(name="java_Expression97", type=java_Cast_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Cast_Expression96", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression98: BinaryAssociation = BinaryAssociation(
    name="expression98",
    ends={
        Property(name="java_Expression100", type=java_Bit_Expression_NR, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Bit_Expression_NR99", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression104: BinaryAssociation = BinaryAssociation(
    name="expression104",
    ends={
        Property(name="java_Expression106", type=java_Arg_List, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Arg_List105", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions107: BinaryAssociation = BinaryAssociation(
    name="expressions107",
    ends={
        Property(name="java_Expression109", type=java_Arg_List, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Arg_List108", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression110: BinaryAssociation = BinaryAssociation(
    name="expression110",
    ends={
        Property(name="java_Expression112", type=java_Numeric_Expression_NR, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Numeric_Expression_NR111", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
name113: BinaryAssociation = BinaryAssociation(
    name="name113",
    ends={
        Property(name="java_Statement_block114", type=java_Static_initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Static_initializer", type=java_Statement_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression101: BinaryAssociation = BinaryAssociation(
    name="expression101",
    ends={
        Property(name="java_Expression103", type=java_Logical_Expression_NR, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Logical_Expression_NR102", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnSmt117: BinaryAssociation = BinaryAssociation(
    name="returnSmt117",
    ends={
        Property(name="java_Return_Statement", type=java_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Statement118", type=java_Return_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable119: BinaryAssociation = BinaryAssociation(
    name="variable119",
    ends={
        Property(name="java_Variable_declaration121", type=java_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Statement120", type=java_Variable_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionx122: BinaryAssociation = BinaryAssociation(
    name="expressionx122",
    ends={
        Property(name="java_Expression124", type=java_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Statement123", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ifStatement125: BinaryAssociation = BinaryAssociation(
    name="ifStatement125",
    ends={
        Property(name="java_If_Statement", type=java_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Statement126", type=java_If_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
doStatement127: BinaryAssociation = BinaryAssociation(
    name="doStatement127",
    ends={
        Property(name="java_Do_Statement", type=java_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Statement128", type=java_Do_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whileStatement129: BinaryAssociation = BinaryAssociation(
    name="whileStatement129",
    ends={
        Property(name="java_While_Statement", type=java_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Statement130", type=java_While_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
forStatement131: BinaryAssociation = BinaryAssociation(
    name="forStatement131",
    ends={
        Property(name="java_For_Statement", type=java_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Statement132", type=java_For_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
switchStatement133: BinaryAssociation = BinaryAssociation(
    name="switchStatement133",
    ends={
        Property(name="java_Switch_Statement", type=java_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Statement134", type=java_Switch_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements115: BinaryAssociation = BinaryAssociation(
    name="statements115",
    ends={
        Property(name="java_Statement", type=java_Statement_block, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Statement_block116", type=java_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement138: BinaryAssociation = BinaryAssociation(
    name="statement138",
    ends={
        Property(name="java_Statement139", type=java_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Statement137", type=java_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression140: BinaryAssociation = BinaryAssociation(
    name="expression140",
    ends={
        Property(name="java_Expression142", type=java_Switch_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Switch_Statement141", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressions143: BinaryAssociation = BinaryAssociation(
    name="expressions143",
    ends={
        Property(name="java_Expression145", type=java_Switch_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Switch_Statement144", type=java_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements146: BinaryAssociation = BinaryAssociation(
    name="statements146",
    ends={
        Property(name="java_Statement148", type=java_Switch_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Switch_Statement147", type=java_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable149: BinaryAssociation = BinaryAssociation(
    name="variable149",
    ends={
        Property(name="java_Variable_declaration151", type=java_For_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_For_Statement150", type=java_Variable_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression152: BinaryAssociation = BinaryAssociation(
    name="expression152",
    ends={
        Property(name="java_Expression154", type=java_For_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_For_Statement153", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
try135: BinaryAssociation = BinaryAssociation(
    name="try135",
    ends={
        Property(name="java_Try_statement", type=java_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Statement136", type=java_Try_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression2155: BinaryAssociation = BinaryAssociation(
    name="expression2155",
    ends={
        Property(name="java_Expression157", type=java_For_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_For_Statement156", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression3158: BinaryAssociation = BinaryAssociation(
    name="expression3158",
    ends={
        Property(name="java_Expression160", type=java_For_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_For_Statement159", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement161: BinaryAssociation = BinaryAssociation(
    name="statement161",
    ends={
        Property(name="java_Statement163", type=java_For_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_For_Statement162", type=java_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression164: BinaryAssociation = BinaryAssociation(
    name="expression164",
    ends={
        Property(name="java_Expression166", type=java_While_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_While_Statement165", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement167: BinaryAssociation = BinaryAssociation(
    name="statement167",
    ends={
        Property(name="java_Statement169", type=java_While_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_While_Statement168", type=java_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement170: BinaryAssociation = BinaryAssociation(
    name="statement170",
    ends={
        Property(name="java_Statement172", type=java_Do_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Do_Statement171", type=java_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression173: BinaryAssociation = BinaryAssociation(
    name="expression173",
    ends={
        Property(name="java_Expression175", type=java_Do_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Do_Statement174", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statement179: BinaryAssociation = BinaryAssociation(
    name="statement179",
    ends={
        Property(name="java_Statement181", type=java_If_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_If_Statement180", type=java_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseStatement182: BinaryAssociation = BinaryAssociation(
    name="elseStatement182",
    ends={
        Property(name="java_Statement184", type=java_If_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_If_Statement183", type=java_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rv185: BinaryAssociation = BinaryAssociation(
    name="rv185",
    ends={
        Property(name="java_Return_value", type=java_Return_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Return_Statement186", type=java_Return_value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tryStatement187: BinaryAssociation = BinaryAssociation(
    name="tryStatement187",
    ends={
        Property(name="java_Statement189", type=java_Try_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Try_statement188", type=java_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
RIGHT_PARENTHESISparameters190: BinaryAssociation = BinaryAssociation(
    name="RIGHT_PARENTHESISparameters190",
    ends={
        Property(name="java_Parameter192", type=java_Try_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Try_statement191", type=java_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catchStatements193: BinaryAssociation = BinaryAssociation(
    name="catchStatements193",
    ends={
        Property(name="java_Statement195", type=java_Try_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Try_statement194", type=java_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression176: BinaryAssociation = BinaryAssociation(
    name="expression176",
    ends={
        Property(name="java_Expression178", type=java_If_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_If_Statement177", type=java_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
finallyStatement196: BinaryAssociation = BinaryAssociation(
    name="finallyStatement196",
    ends={
        Property(name="java_Statement198", type=java_Try_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="java_Try_statement197", type=java_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_java_Method_call_Return_value = Generalization(general=Return_value, specific=java_Method_call)
gen_java_Literal_Expression_Return_value = Generalization(general=Return_value, specific=java_Literal_Expression)
gen_java_Statement_block_Statement = Generalization(general=Statement, specific=java_Statement_block)

# Domain Model
domain_model = DomainModel(
    name="java",
    types={java_Head, java_Type_declaration, java_EObject, java_Interface_declaration, java_Compilation_unit, java_Package_statement, java_Import_statement, java_Method_declaration, java_Field_declaration, java_Class_declaration, java_Parameter, java_Type, java_Parameter_list, java_Statement_block, java_Method_call, Return_value, java_Parameter_list_method_call, java_Constructor_declaration, java_Variable_initializer, java_Expression, java_Variable_declaration, java_Variable_declarator, java_Literal_Expression, java_Arg_List, java_Numeric_Expression_NR, java_Expression_aux, java_Logical_Expression_NR, java_Bit_Expression_NR, java_Cast_Expression, java_Creating_Expression, java_Ampersand_Rule, java_Float_Literal, java_Static_initializer, Statement, java_Return_Statement, java_If_Statement, java_Do_Statement, java_While_Statement, java_For_Statement, java_Switch_Statement, java_Statement, java_Try_statement, java_Return_value},
    associations={type_declarations5, name7, elements0, package1, imports3, fields10, name12, fields9, parameters21, statement23, parameter26, type15, parameter16, statement18, parameter20, names38, initializer41, expression43, variableInitializer146, variableIniatializer249, parameters28, type31, type34, name36, creatingExpression61, literalExpression63, argList65, numericExpression351, aux53, logicalExpression55, bitExpression57, castExpression59, exp176, ampersand79, expressionBit81, aux68, expression270, exp273, exp284, argList86, expression89, type92, expression95, expression98, expression104, expressions107, expression110, name113, expression101, returnSmt117, variable119, expressionx122, ifStatement125, doStatement127, whileStatement129, forStatement131, switchStatement133, statements115, statement138, expression140, expressions143, statements146, variable149, expression152, try135, expression2155, expression3158, statement161, expression164, statement167, statement170, expression173, statement179, elseStatement182, rv185, tryStatement187, RIGHT_PARENTHESISparameters190, catchStatements193, expression176, finallyStatement196},
    generalizations={gen_java_Method_call_Return_value, gen_java_Literal_Expression_Return_value, gen_java_Statement_block_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)