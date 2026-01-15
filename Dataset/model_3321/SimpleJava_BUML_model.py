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
simpleJava_type_declaration = Class(name="simpleJava::type::declaration")
simpleJava_name = Class(name="simpleJava::name")
simpleJava_Model = Class(name="simpleJava::Model")
simpleJava_compilation_unit = Class(name="simpleJava::compilation::unit")
Model = Class(name="Model")
simpleJava_package_statement = Class(name="simpleJava::package::statement")
simpleJava_import_statement = Class(name="simpleJava::import::statement")
simpleJava_class_declaration = Class(name="simpleJava::class::declaration")
simpleJava_interface_declaration = Class(name="simpleJava::interface::declaration")
simpleJava_doc_comment = Class(name="simpleJava::doc::comment")
type_declaration = Class(name="type::declaration")
simpleJava_MODIFIER = Class(name="simpleJava::MODIFIER")
simpleJava_field_declaration = Class(name="simpleJava::field::declaration")
simpleJava_type = Class(name="simpleJava::type")
simpleJava_parameter_list = Class(name="simpleJava::parameter::list")
simpleJava_method_declaration = Class(name="simpleJava::method::declaration")
simpleJava_constructor_declaration = Class(name="simpleJava::constructor::declaration")
simpleJava_variable_declaration = Class(name="simpleJava::variable::declaration")
simpleJava_static_initializer = Class(name="simpleJava::static::initializer")
simpleJava_if_statement = Class(name="simpleJava::if::statement")
simpleJava_do_statement = Class(name="simpleJava::do::statement")
simpleJava_while_statement = Class(name="simpleJava::while::statement")
simpleJava_statement_block = Class(name="simpleJava::statement::block")
simpleJava_parameter = Class(name="simpleJava::parameter")
simpleJava_statement = Class(name="simpleJava::statement")
simpleJava_expression = Class(name="simpleJava::expression")
simpleJava_variable_declarator = Class(name="simpleJava::variable::declarator")
simpleJava_for_statement = Class(name="simpleJava::for::statement")
simpleJava_try_statement = Class(name="simpleJava::try::statement")
simpleJava_switch_statement = Class(name="simpleJava::switch::statement")
simpleJava_variable_initializer = Class(name="simpleJava::variable::initializer")
simpleJava_creating_expression = Class(name="simpleJava::creating::expression")
newBlock = Class(name="newBlock")
simpleJava_bit_expression = Class(name="simpleJava::bit::expression")
simpleJava_creating_aux = Class(name="simpleJava::creating::aux")
simpleJava_type_specifier = Class(name="simpleJava::type::specifier")
simpleJava_newBlock = Class(name="simpleJava::newBlock")
simpleJava_exp_aux = Class(name="simpleJava::exp::aux")
expression = Class(name="expression")
expression_aux = Class(name="expression::aux")
simpleJava_logical_expression = Class(name="simpleJava::logical::expression")
simpleJava_numeric_expression = Class(name="simpleJava::numeric::expression")
simpleJava_literal_expression = Class(name="simpleJava::literal::expression")
simpleJava_expression_aux = Class(name="simpleJava::expression::aux")
simpleJava_arglist = Class(name="simpleJava::arglist")
simpleJava_mais_aux = Class(name="simpleJava::mais::aux")
simpleJava_aux = Class(name="simpleJava::aux")
creating_aux = Class(name="creating::aux")
simpleJava_package_name_aux = Class(name="simpleJava::package::name::aux")
variable_declarator = Class(name="variable::declarator")
exp_aux = Class(name="exp::aux")

# simpleJava_type_declaration class attributes and methods

# simpleJava_name class attributes and methods
simpleJava_name_nome: Property = Property(name="nome", type=StringType)
simpleJava_name.attributes={simpleJava_name_nome}

# simpleJava_Model class attributes and methods

# simpleJava_compilation_unit class attributes and methods

# Model class attributes and methods

# simpleJava_package_statement class attributes and methods

# simpleJava_import_statement class attributes and methods

# simpleJava_class_declaration class attributes and methods
simpleJava_class_declaration_nomeClasse: Property = Property(name="nomeClasse", type=StringType)
simpleJava_class_declaration.attributes={simpleJava_class_declaration_nomeClasse}

# simpleJava_interface_declaration class attributes and methods
simpleJava_interface_declaration_nomeInterface: Property = Property(name="nomeInterface", type=StringType)
simpleJava_interface_declaration.attributes={simpleJava_interface_declaration_nomeInterface}

# simpleJava_doc_comment class attributes and methods
simpleJava_doc_comment_comentario: Property = Property(name="comentario", type=StringType)
simpleJava_doc_comment.attributes={simpleJava_doc_comment_comentario}

# type_declaration class attributes and methods

# simpleJava_MODIFIER class attributes and methods
simpleJava_MODIFIER_modificador: Property = Property(name="modificador", type=StringType)
simpleJava_MODIFIER.attributes={simpleJava_MODIFIER_modificador}

# simpleJava_field_declaration class attributes and methods

# simpleJava_type class attributes and methods

# simpleJava_parameter_list class attributes and methods

# simpleJava_method_declaration class attributes and methods
simpleJava_method_declaration_nomeMetodo: Property = Property(name="nomeMetodo", type=StringType)
simpleJava_method_declaration.attributes={simpleJava_method_declaration_nomeMetodo}

# simpleJava_constructor_declaration class attributes and methods
simpleJava_constructor_declaration_nomeContrutor: Property = Property(name="nomeContrutor", type=StringType)
simpleJava_constructor_declaration.attributes={simpleJava_constructor_declaration_nomeContrutor}

# simpleJava_variable_declaration class attributes and methods

# simpleJava_static_initializer class attributes and methods

# simpleJava_if_statement class attributes and methods

# simpleJava_do_statement class attributes and methods

# simpleJava_while_statement class attributes and methods

# simpleJava_statement_block class attributes and methods

# simpleJava_parameter class attributes and methods
simpleJava_parameter_nomeParametro: Property = Property(name="nomeParametro", type=StringType)
simpleJava_parameter.attributes={simpleJava_parameter_nomeParametro}

# simpleJava_statement class attributes and methods
simpleJava_statement_break: Property = Property(name="break", type=StringType)
simpleJava_statement_continue: Property = Property(name="continue", type=StringType)
simpleJava_statement.attributes={simpleJava_statement_break, simpleJava_statement_continue}

# simpleJava_expression class attributes and methods
simpleJava_expression_identificador: Property = Property(name="identificador", type=StringType)
simpleJava_expression.attributes={simpleJava_expression_identificador}

# simpleJava_variable_declarator class attributes and methods
simpleJava_variable_declarator_nomeVariavel: Property = Property(name="nomeVariavel", type=StringType)
simpleJava_variable_declarator_op: Property = Property(name="op", type=StringType)
simpleJava_variable_declarator.attributes={simpleJava_variable_declarator_op, simpleJava_variable_declarator_nomeVariavel}

# simpleJava_for_statement class attributes and methods

# simpleJava_try_statement class attributes and methods

# simpleJava_switch_statement class attributes and methods

# simpleJava_variable_initializer class attributes and methods

# simpleJava_creating_expression class attributes and methods

# newBlock class attributes and methods

# simpleJava_bit_expression class attributes and methods
simpleJava_bit_expression_operador: Property = Property(name="operador", type=StringType)
simpleJava_bit_expression.attributes={simpleJava_bit_expression_operador}

# simpleJava_creating_aux class attributes and methods

# simpleJava_type_specifier class attributes and methods
simpleJava_type_specifier_nome: Property = Property(name="nome", type=StringType)
simpleJava_type_specifier.attributes={simpleJava_type_specifier_nome}

# simpleJava_newBlock class attributes and methods

# simpleJava_exp_aux class attributes and methods

# expression class attributes and methods

# expression_aux class attributes and methods

# simpleJava_logical_expression class attributes and methods
simpleJava_logical_expression_operador: Property = Property(name="operador", type=StringType)
simpleJava_logical_expression.attributes={simpleJava_logical_expression_operador}

# simpleJava_numeric_expression class attributes and methods
simpleJava_numeric_expression_operador: Property = Property(name="operador", type=StringType)
simpleJava_numeric_expression.attributes={simpleJava_numeric_expression_operador}

# simpleJava_literal_expression class attributes and methods
simpleJava_literal_expression_decimal: Property = Property(name="decimal", type=StringType)
simpleJava_literal_expression_inteiro: Property = Property(name="inteiro", type=StringType)
simpleJava_literal_expression_l_float: Property = Property(name="l_float", type=StringType)
simpleJava_literal_expression_string: Property = Property(name="string", type=StringType)
simpleJava_literal_expression.attributes={simpleJava_literal_expression_l_float, simpleJava_literal_expression_inteiro, simpleJava_literal_expression_decimal, simpleJava_literal_expression_string}

# simpleJava_expression_aux class attributes and methods
simpleJava_expression_aux_operador: Property = Property(name="operador", type=StringType)
simpleJava_expression_aux.attributes={simpleJava_expression_aux_operador}

# simpleJava_arglist class attributes and methods
simpleJava_arglist_nomeParametro: Property = Property(name="nomeParametro", type=StringType)
simpleJava_arglist.attributes={simpleJava_arglist_nomeParametro}

# simpleJava_mais_aux class attributes and methods
simpleJava_mais_aux_operador: Property = Property(name="operador", type=StringType)
simpleJava_mais_aux.attributes={simpleJava_mais_aux_operador}

# simpleJava_aux class attributes and methods

# creating_aux class attributes and methods

# simpleJava_package_name_aux class attributes and methods
simpleJava_package_name_aux_nomePacote: Property = Property(name="nomePacote", type=StringType)
simpleJava_package_name_aux.attributes={simpleJava_package_name_aux_nomePacote}

# variable_declarator class attributes and methods

# exp_aux class attributes and methods

# Relationships
declaracao3: BinaryAssociation = BinaryAssociation(
    name="declaracao3",
    ends={
        Property(name="simpleJava_type_declaration", type=simpleJava_compilation_unit, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_compilation_unit4", type=simpleJava_type_declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
noomePacote5: BinaryAssociation = BinaryAssociation(
    name="noomePacote5",
    ends={
        Property(name="simpleJava_name", type=simpleJava_package_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_package_statement6", type=simpleJava_name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pacote0: BinaryAssociation = BinaryAssociation(
    name="pacote0",
    ends={
        Property(name="simpleJava_package_statement", type=simpleJava_compilation_unit, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_compilation_unit", type=simpleJava_package_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
importes1: BinaryAssociation = BinaryAssociation(
    name="importes1",
    ends={
        Property(name="simpleJava_import_statement", type=simpleJava_compilation_unit, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_compilation_unit2", type=simpleJava_import_statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
corpoClasse22: BinaryAssociation = BinaryAssociation(
    name="corpoClasse22",
    ends={
        Property(name="simpleJava_class_declaration23", type=simpleJava_field_declaration, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="simpleJava_field_declaration", type=simpleJava_class_declaration, multiplicity=Multiplicity(1, 1))
    }
)
declaracaoClasse25: BinaryAssociation = BinaryAssociation(
    name="declaracaoClasse25",
    ends={
        Property(name="simpleJava_class_declaration26", type=simpleJava_class_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_class_declaration24", type=simpleJava_class_declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modificadores27: BinaryAssociation = BinaryAssociation(
    name="modificadores27",
    ends={
        Property(name="simpleJava_MODIFIER29", type=simpleJava_interface_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_interface_declaration28", type=simpleJava_MODIFIER, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nomeImporte7: BinaryAssociation = BinaryAssociation(
    name="nomeImporte7",
    ends={
        Property(name="simpleJava_name9", type=simpleJava_import_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_import_statement8", type=simpleJava_name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaracaoClasse10: BinaryAssociation = BinaryAssociation(
    name="declaracaoClasse10",
    ends={
        Property(name="simpleJava_class_declaration", type=simpleJava_type_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_type_declaration11", type=simpleJava_class_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaracaoInterface12: BinaryAssociation = BinaryAssociation(
    name="declaracaoInterface12",
    ends={
        Property(name="simpleJava_interface_declaration", type=simpleJava_type_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_type_declaration13", type=simpleJava_interface_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modificadores14: BinaryAssociation = BinaryAssociation(
    name="modificadores14",
    ends={
        Property(name="simpleJava_MODIFIER", type=simpleJava_class_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_class_declaration15", type=simpleJava_MODIFIER, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superclasse16: BinaryAssociation = BinaryAssociation(
    name="superclasse16",
    ends={
        Property(name="simpleJava_name18", type=simpleJava_class_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_class_declaration17", type=simpleJava_name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implementosClasse19: BinaryAssociation = BinaryAssociation(
    name="implementosClasse19",
    ends={
        Property(name="simpleJava_name21", type=simpleJava_class_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_class_declaration20", type=simpleJava_name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modificadorMetodo46: BinaryAssociation = BinaryAssociation(
    name="modificadorMetodo46",
    ends={
        Property(name="simpleJava_MODIFIER48", type=simpleJava_method_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_method_declaration47", type=simpleJava_MODIFIER, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tipoRetorno49: BinaryAssociation = BinaryAssociation(
    name="tipoRetorno49",
    ends={
        Property(name="simpleJava_type", type=simpleJava_method_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_method_declaration50", type=simpleJava_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superinterfaces30: BinaryAssociation = BinaryAssociation(
    name="superinterfaces30",
    ends={
        Property(name="simpleJava_name32", type=simpleJava_interface_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_interface_declaration31", type=simpleJava_name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
corpoInterface33: BinaryAssociation = BinaryAssociation(
    name="corpoInterface33",
    ends={
        Property(name="simpleJava_field_declaration35", type=simpleJava_interface_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_interface_declaration34", type=simpleJava_field_declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comentario36: BinaryAssociation = BinaryAssociation(
    name="comentario36",
    ends={
        Property(name="simpleJava_doc_comment", type=simpleJava_field_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_field_declaration37", type=simpleJava_doc_comment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaracaoMetodo38: BinaryAssociation = BinaryAssociation(
    name="declaracaoMetodo38",
    ends={
        Property(name="simpleJava_method_declaration", type=simpleJava_field_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_field_declaration39", type=simpleJava_method_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaracaoConstrutor40: BinaryAssociation = BinaryAssociation(
    name="declaracaoConstrutor40",
    ends={
        Property(name="simpleJava_constructor_declaration", type=simpleJava_field_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_field_declaration41", type=simpleJava_constructor_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaracaoVariavel42: BinaryAssociation = BinaryAssociation(
    name="declaracaoVariavel42",
    ends={
        Property(name="simpleJava_variable_declaration", type=simpleJava_field_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_field_declaration43", type=simpleJava_variable_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
estatico44: BinaryAssociation = BinaryAssociation(
    name="estatico44",
    ends={
        Property(name="simpleJava_static_initializer", type=simpleJava_field_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_field_declaration45", type=simpleJava_static_initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
corpoIf70: BinaryAssociation = BinaryAssociation(
    name="corpoIf70",
    ends={
        Property(name="simpleJava_if_statement", type=simpleJava_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_statement71", type=simpleJava_if_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
corpoDoWhile72: BinaryAssociation = BinaryAssociation(
    name="corpoDoWhile72",
    ends={
        Property(name="simpleJava_do_statement", type=simpleJava_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_statement73", type=simpleJava_do_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parametrosMetodo51: BinaryAssociation = BinaryAssociation(
    name="parametrosMetodo51",
    ends={
        Property(name="simpleJava_parameter_list", type=simpleJava_method_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_method_declaration52", type=simpleJava_parameter_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blocoMetodo53: BinaryAssociation = BinaryAssociation(
    name="blocoMetodo53",
    ends={
        Property(name="simpleJava_statement_block", type=simpleJava_method_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_method_declaration54", type=simpleJava_statement_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tipoParametro55: BinaryAssociation = BinaryAssociation(
    name="tipoParametro55",
    ends={
        Property(name="simpleJava_type56", type=simpleJava_parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_parameter", type=simpleJava_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parametros57: BinaryAssociation = BinaryAssociation(
    name="parametros57",
    ends={
        Property(name="simpleJava_parameter59", type=simpleJava_parameter_list, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_parameter_list58", type=simpleJava_parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
corpo60: BinaryAssociation = BinaryAssociation(
    name="corpo60",
    ends={
        Property(name="simpleJava_statement", type=simpleJava_statement_block, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_statement_block61", type=simpleJava_statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaracaoVariavel62: BinaryAssociation = BinaryAssociation(
    name="declaracaoVariavel62",
    ends={
        Property(name="simpleJava_variable_declaration64", type=simpleJava_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_statement63", type=simpleJava_variable_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressao65: BinaryAssociation = BinaryAssociation(
    name="expressao65",
    ends={
        Property(name="simpleJava_expression", type=simpleJava_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_statement66", type=simpleJava_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
newbloco67: BinaryAssociation = BinaryAssociation(
    name="newbloco67",
    ends={
        Property(name="simpleJava_statement_block69", type=simpleJava_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_statement68", type=simpleJava_statement_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modificador94: BinaryAssociation = BinaryAssociation(
    name="modificador94",
    ends={
        Property(name="simpleJava_MODIFIER96", type=simpleJava_variable_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_variable_declaration95", type=simpleJava_MODIFIER, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tipoVariavel97: BinaryAssociation = BinaryAssociation(
    name="tipoVariavel97",
    ends={
        Property(name="simpleJava_type99", type=simpleJava_variable_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_variable_declaration98", type=simpleJava_type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
corpoWhile74: BinaryAssociation = BinaryAssociation(
    name="corpoWhile74",
    ends={
        Property(name="simpleJava_while_statement", type=simpleJava_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_statement75", type=simpleJava_while_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
corpoFor76: BinaryAssociation = BinaryAssociation(
    name="corpoFor76",
    ends={
        Property(name="simpleJava_for_statement", type=simpleJava_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_statement77", type=simpleJava_for_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
corpoTryCatch78: BinaryAssociation = BinaryAssociation(
    name="corpoTryCatch78",
    ends={
        Property(name="simpleJava_try_statement", type=simpleJava_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_statement79", type=simpleJava_try_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
corpoSwitchCase80: BinaryAssociation = BinaryAssociation(
    name="corpoSwitchCase80",
    ends={
        Property(name="simpleJava_switch_statement", type=simpleJava_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_statement81", type=simpleJava_switch_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressaoSynchronized82: BinaryAssociation = BinaryAssociation(
    name="expressaoSynchronized82",
    ends={
        Property(name="simpleJava_expression84", type=simpleJava_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_statement83", type=simpleJava_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
corpoSynchronize86: BinaryAssociation = BinaryAssociation(
    name="corpoSynchronize86",
    ends={
        Property(name="simpleJava_statement87", type=simpleJava_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_statement85", type=simpleJava_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
return88: BinaryAssociation = BinaryAssociation(
    name="return88",
    ends={
        Property(name="simpleJava_expression90", type=simpleJava_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_statement89", type=simpleJava_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exececao91: BinaryAssociation = BinaryAssociation(
    name="exececao91",
    ends={
        Property(name="simpleJava_expression93", type=simpleJava_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_statement92", type=simpleJava_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blocoDo122: BinaryAssociation = BinaryAssociation(
    name="blocoDo122",
    ends={
        Property(name="simpleJava_statement124", type=simpleJava_do_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_do_statement123", type=simpleJava_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressaoWhile125: BinaryAssociation = BinaryAssociation(
    name="expressaoWhile125",
    ends={
        Property(name="simpleJava_expression127", type=simpleJava_do_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_do_statement126", type=simpleJava_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaracaoVariaveis100: BinaryAssociation = BinaryAssociation(
    name="declaracaoVariaveis100",
    ends={
        Property(name="simpleJava_variable_declarator", type=simpleJava_variable_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_variable_declaration101", type=simpleJava_variable_declarator, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blocoVariavel102: BinaryAssociation = BinaryAssociation(
    name="blocoVariavel102",
    ends={
        Property(name="simpleJava_statement_block104", type=simpleJava_variable_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_variable_declaration103", type=simpleJava_statement_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valorVariavel105: BinaryAssociation = BinaryAssociation(
    name="valorVariavel105",
    ends={
        Property(name="simpleJava_variable_initializer", type=simpleJava_variable_declarator, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_variable_declarator106", type=simpleJava_variable_initializer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressaoVariavel107: BinaryAssociation = BinaryAssociation(
    name="expressaoVariavel107",
    ends={
        Property(name="simpleJava_expression109", type=simpleJava_variable_initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_variable_initializer108", type=simpleJava_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
valorVariaveis111: BinaryAssociation = BinaryAssociation(
    name="valorVariaveis111",
    ends={
        Property(name="simpleJava_variable_initializer112", type=simpleJava_variable_initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_variable_initializer110", type=simpleJava_variable_initializer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
espressaoIf113: BinaryAssociation = BinaryAssociation(
    name="espressaoIf113",
    ends={
        Property(name="simpleJava_expression115", type=simpleJava_if_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_if_statement114", type=simpleJava_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blcoIf116: BinaryAssociation = BinaryAssociation(
    name="blcoIf116",
    ends={
        Property(name="simpleJava_statement118", type=simpleJava_if_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_if_statement117", type=simpleJava_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blocoElse119: BinaryAssociation = BinaryAssociation(
    name="blocoElse119",
    ends={
        Property(name="simpleJava_statement121", type=simpleJava_if_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_if_statement120", type=simpleJava_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blocoTry149: BinaryAssociation = BinaryAssociation(
    name="blocoTry149",
    ends={
        Property(name="simpleJava_statement_block151", type=simpleJava_try_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_try_statement150", type=simpleJava_statement_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parametroCatch152: BinaryAssociation = BinaryAssociation(
    name="parametroCatch152",
    ends={
        Property(name="simpleJava_parameter154", type=simpleJava_try_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_try_statement153", type=simpleJava_parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blocoCatch155: BinaryAssociation = BinaryAssociation(
    name="blocoCatch155",
    ends={
        Property(name="simpleJava_statement_block157", type=simpleJava_try_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_try_statement156", type=simpleJava_statement_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressaoWhile128: BinaryAssociation = BinaryAssociation(
    name="expressaoWhile128",
    ends={
        Property(name="simpleJava_expression130", type=simpleJava_while_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_while_statement129", type=simpleJava_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blocoWhile131: BinaryAssociation = BinaryAssociation(
    name="blocoWhile131",
    ends={
        Property(name="simpleJava_statement133", type=simpleJava_while_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_while_statement132", type=simpleJava_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaracaoVariavel134: BinaryAssociation = BinaryAssociation(
    name="declaracaoVariavel134",
    ends={
        Property(name="simpleJava_variable_declaration136", type=simpleJava_for_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_for_statement135", type=simpleJava_variable_declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressaoDeclaracao137: BinaryAssociation = BinaryAssociation(
    name="expressaoDeclaracao137",
    ends={
        Property(name="simpleJava_expression139", type=simpleJava_for_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_for_statement138", type=simpleJava_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressaoFor140: BinaryAssociation = BinaryAssociation(
    name="expressaoFor140",
    ends={
        Property(name="simpleJava_expression142", type=simpleJava_for_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_for_statement141", type=simpleJava_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressaoIncremento143: BinaryAssociation = BinaryAssociation(
    name="expressaoIncremento143",
    ends={
        Property(name="simpleJava_expression145", type=simpleJava_for_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_for_statement144", type=simpleJava_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blocoFor146: BinaryAssociation = BinaryAssociation(
    name="blocoFor146",
    ends={
        Property(name="simpleJava_statement148", type=simpleJava_for_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_for_statement147", type=simpleJava_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blocoEstatico179: BinaryAssociation = BinaryAssociation(
    name="blocoEstatico179",
    ends={
        Property(name="simpleJava_statement_block181", type=simpleJava_static_initializer, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_static_initializer180", type=simpleJava_statement_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blocoFinally158: BinaryAssociation = BinaryAssociation(
    name="blocoFinally158",
    ends={
        Property(name="simpleJava_statement_block160", type=simpleJava_try_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_try_statement159", type=simpleJava_statement_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressaoSwitch161: BinaryAssociation = BinaryAssociation(
    name="expressaoSwitch161",
    ends={
        Property(name="simpleJava_expression163", type=simpleJava_switch_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_switch_statement162", type=simpleJava_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressaoCases164: BinaryAssociation = BinaryAssociation(
    name="expressaoCases164",
    ends={
        Property(name="simpleJava_expression166", type=simpleJava_switch_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_switch_statement165", type=simpleJava_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
blocoSwitch167: BinaryAssociation = BinaryAssociation(
    name="blocoSwitch167",
    ends={
        Property(name="simpleJava_statement169", type=simpleJava_switch_statement, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_switch_statement168", type=simpleJava_statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
modificador170: BinaryAssociation = BinaryAssociation(
    name="modificador170",
    ends={
        Property(name="simpleJava_MODIFIER172", type=simpleJava_constructor_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_constructor_declaration171", type=simpleJava_MODIFIER, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parametrosContrutor173: BinaryAssociation = BinaryAssociation(
    name="parametrosContrutor173",
    ends={
        Property(name="simpleJava_parameter_list175", type=simpleJava_constructor_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_constructor_declaration174", type=simpleJava_parameter_list, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
blocoConstrutor176: BinaryAssociation = BinaryAssociation(
    name="blocoConstrutor176",
    ends={
        Property(name="simpleJava_statement_block178", type=simpleJava_constructor_declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_constructor_declaration177", type=simpleJava_statement_block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bit199: BinaryAssociation = BinaryAssociation(
    name="bit199",
    ends={
        Property(name="simpleJava_bit_expression", type=simpleJava_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_expression200", type=simpleJava_bit_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
novoObjeto182: BinaryAssociation = BinaryAssociation(
    name="novoObjeto182",
    ends={
        Property(name="simpleJava_name183", type=simpleJava_creating_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_creating_expression", type=simpleJava_name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parametros184: BinaryAssociation = BinaryAssociation(
    name="parametros184",
    ends={
        Property(name="simpleJava_creating_aux", type=simpleJava_creating_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_creating_expression185", type=simpleJava_creating_aux, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tipoObjeto186: BinaryAssociation = BinaryAssociation(
    name="tipoObjeto186",
    ends={
        Property(name="simpleJava_type_specifier", type=simpleJava_creating_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_creating_expression187", type=simpleJava_type_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressaoNew188: BinaryAssociation = BinaryAssociation(
    name="expressaoNew188",
    ends={
        Property(name="simpleJava_expression190", type=simpleJava_creating_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_creating_expression189", type=simpleJava_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
novo191: BinaryAssociation = BinaryAssociation(
    name="novo191",
    ends={
        Property(name="simpleJava_newBlock", type=simpleJava_creating_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_creating_expression192", type=simpleJava_newBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressao193: BinaryAssociation = BinaryAssociation(
    name="expressao193",
    ends={
        Property(name="simpleJava_expression194", type=simpleJava_exp_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_exp_aux", type=simpleJava_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
logical195: BinaryAssociation = BinaryAssociation(
    name="logical195",
    ends={
        Property(name="simpleJava_logical_expression", type=simpleJava_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_expression196", type=simpleJava_logical_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
numeric197: BinaryAssociation = BinaryAssociation(
    name="numeric197",
    ends={
        Property(name="simpleJava_numeric_expression", type=simpleJava_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_expression198", type=simpleJava_numeric_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
espressao218: BinaryAssociation = BinaryAssociation(
    name="espressao218",
    ends={
        Property(name="simpleJava_expression219", type=simpleJava_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_aux", type=simpleJava_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
novo201: BinaryAssociation = BinaryAssociation(
    name="novo201",
    ends={
        Property(name="simpleJava_creating_expression203", type=simpleJava_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_expression202", type=simpleJava_creating_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literal204: BinaryAssociation = BinaryAssociation(
    name="literal204",
    ends={
        Property(name="simpleJava_literal_expression", type=simpleJava_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_expression205", type=simpleJava_literal_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parametros206: BinaryAssociation = BinaryAssociation(
    name="parametros206",
    ends={
        Property(name="simpleJava_arglist", type=simpleJava_expression_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_expression_aux", type=simpleJava_arglist, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp207: BinaryAssociation = BinaryAssociation(
    name="exp207",
    ends={
        Property(name="simpleJava_expression209", type=simpleJava_expression_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_expression_aux208", type=simpleJava_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
op210: BinaryAssociation = BinaryAssociation(
    name="op210",
    ends={
        Property(name="simpleJava_mais_aux", type=simpleJava_expression_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_expression_aux211", type=simpleJava_mais_aux, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressoes213: BinaryAssociation = BinaryAssociation(
    name="expressoes213",
    ends={
        Property(name="simpleJava_expression_aux214", type=simpleJava_expression_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_expression_aux212", type=simpleJava_expression_aux, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argumentos215: BinaryAssociation = BinaryAssociation(
    name="argumentos215",
    ends={
        Property(name="simpleJava_arglist217", type=simpleJava_creating_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_creating_aux216", type=simpleJava_arglist, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pacote235: BinaryAssociation = BinaryAssociation(
    name="pacote235",
    ends={
        Property(name="simpleJava_package_name_aux", type=simpleJava_name, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_name236", type=simpleJava_package_name_aux, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp220: BinaryAssociation = BinaryAssociation(
    name="exp220",
    ends={
        Property(name="simpleJava_expression222", type=simpleJava_logical_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_logical_expression221", type=simpleJava_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressao223: BinaryAssociation = BinaryAssociation(
    name="expressao223",
    ends={
        Property(name="simpleJava_expression225", type=simpleJava_bit_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_bit_expression224", type=simpleJava_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressao226: BinaryAssociation = BinaryAssociation(
    name="expressao226",
    ends={
        Property(name="simpleJava_expression228", type=simpleJava_numeric_expression, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_numeric_expression227", type=simpleJava_expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressoesArgumentos229: BinaryAssociation = BinaryAssociation(
    name="expressoesArgumentos229",
    ends={
        Property(name="simpleJava_expression231", type=simpleJava_arglist, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_arglist230", type=simpleJava_expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tipoParametro232: BinaryAssociation = BinaryAssociation(
    name="tipoParametro232",
    ends={
        Property(name="simpleJava_type234", type=simpleJava_arglist, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_arglist233", type=simpleJava_type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pacote238: BinaryAssociation = BinaryAssociation(
    name="pacote238",
    ends={
        Property(name="simpleJava_package_name_aux239", type=simpleJava_package_name_aux, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_package_name_aux237", type=simpleJava_package_name_aux, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primitivo240: BinaryAssociation = BinaryAssociation(
    name="primitivo240",
    ends={
        Property(name="simpleJava_type_specifier242", type=simpleJava_type, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_type241", type=simpleJava_type_specifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
objeto243: BinaryAssociation = BinaryAssociation(
    name="objeto243",
    ends={
        Property(name="simpleJava_name245", type=simpleJava_type, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleJava_type244", type=simpleJava_name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_simpleJava_compilation_unit_Model = Generalization(general=Model, specific=simpleJava_compilation_unit)
gen_simpleJava_doc_comment_type_declaration = Generalization(general=type_declaration, specific=simpleJava_doc_comment)
gen_simpleJava_constructor_declaration_newBlock = Generalization(general=newBlock, specific=simpleJava_constructor_declaration)
gen_simpleJava_exp_aux_expression = Generalization(general=expression, specific=simpleJava_exp_aux)
gen_simpleJava_expression_expression_aux = Generalization(general=expression_aux, specific=simpleJava_expression)
gen_simpleJava_aux_expression_aux = Generalization(general=expression_aux, specific=simpleJava_aux)
gen_simpleJava_aux_creating_aux = Generalization(general=creating_aux, specific=simpleJava_aux)
gen_simpleJava_name_expression_aux = Generalization(general=expression_aux, specific=simpleJava_name)
gen_simpleJava_arglist_variable_declarator = Generalization(general=variable_declarator, specific=simpleJava_arglist)
gen_simpleJava_type_exp_aux = Generalization(general=exp_aux, specific=simpleJava_type)

# Domain Model
domain_model = DomainModel(
    name="simpleJava",
    types={simpleJava_type_declaration, simpleJava_name, simpleJava_Model, simpleJava_compilation_unit, Model, simpleJava_package_statement, simpleJava_import_statement, simpleJava_class_declaration, simpleJava_interface_declaration, simpleJava_doc_comment, type_declaration, simpleJava_MODIFIER, simpleJava_field_declaration, simpleJava_type, simpleJava_parameter_list, simpleJava_method_declaration, simpleJava_constructor_declaration, simpleJava_variable_declaration, simpleJava_static_initializer, simpleJava_if_statement, simpleJava_do_statement, simpleJava_while_statement, simpleJava_statement_block, simpleJava_parameter, simpleJava_statement, simpleJava_expression, simpleJava_variable_declarator, simpleJava_for_statement, simpleJava_try_statement, simpleJava_switch_statement, simpleJava_variable_initializer, simpleJava_creating_expression, newBlock, simpleJava_bit_expression, simpleJava_creating_aux, simpleJava_type_specifier, simpleJava_newBlock, simpleJava_exp_aux, expression, expression_aux, simpleJava_logical_expression, simpleJava_numeric_expression, simpleJava_literal_expression, simpleJava_expression_aux, simpleJava_arglist, simpleJava_mais_aux, simpleJava_aux, creating_aux, simpleJava_package_name_aux, variable_declarator, exp_aux},
    associations={declaracao3, noomePacote5, pacote0, importes1, corpoClasse22, declaracaoClasse25, modificadores27, nomeImporte7, declaracaoClasse10, declaracaoInterface12, modificadores14, superclasse16, implementosClasse19, modificadorMetodo46, tipoRetorno49, superinterfaces30, corpoInterface33, comentario36, declaracaoMetodo38, declaracaoConstrutor40, declaracaoVariavel42, estatico44, corpoIf70, corpoDoWhile72, parametrosMetodo51, blocoMetodo53, tipoParametro55, parametros57, corpo60, declaracaoVariavel62, expressao65, newbloco67, modificador94, tipoVariavel97, corpoWhile74, corpoFor76, corpoTryCatch78, corpoSwitchCase80, expressaoSynchronized82, corpoSynchronize86, return88, exececao91, blocoDo122, expressaoWhile125, declaracaoVariaveis100, blocoVariavel102, valorVariavel105, expressaoVariavel107, valorVariaveis111, espressaoIf113, blcoIf116, blocoElse119, blocoTry149, parametroCatch152, blocoCatch155, expressaoWhile128, blocoWhile131, declaracaoVariavel134, expressaoDeclaracao137, expressaoFor140, expressaoIncremento143, blocoFor146, blocoEstatico179, blocoFinally158, expressaoSwitch161, expressaoCases164, blocoSwitch167, modificador170, parametrosContrutor173, blocoConstrutor176, bit199, novoObjeto182, parametros184, tipoObjeto186, expressaoNew188, novo191, expressao193, logical195, numeric197, espressao218, novo201, literal204, parametros206, exp207, op210, expressoes213, argumentos215, pacote235, exp220, expressao223, expressao226, expressoesArgumentos229, tipoParametro232, pacote238, primitivo240, objeto243},
    generalizations={gen_simpleJava_compilation_unit_Model, gen_simpleJava_doc_comment_type_declaration, gen_simpleJava_constructor_declaration_newBlock, gen_simpleJava_exp_aux_expression, gen_simpleJava_expression_expression_aux, gen_simpleJava_aux_expression_aux, gen_simpleJava_aux_creating_aux, gen_simpleJava_name_expression_aux, gen_simpleJava_arglist_variable_declarator, gen_simpleJava_type_exp_aux},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)