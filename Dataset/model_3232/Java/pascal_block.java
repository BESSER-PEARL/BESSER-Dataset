





import java.util.List;
import java.util.ArrayList;

public class pascal_block  {






    private pascal_function_procedure_declaration pascal_function_procedure_declaration;




    private pascal_constant_definition_part pascal_constant_definition_part;




    private pascal_type_definition_part pascal_type_definition_part;




    private pascal_statement_part pascal_statement_part;




    private pascal_program pascal_program;




    private pascal_variable_declaration_part pascal_variable_declaration_part;


    public pascal_block(
    ) {
    }



    public pascal_function_procedure_declaration getPascal_function_procedure_declaration() {
        return pascal_function_procedure_declaration;
    }

    public void setPascal_function_procedure_declaration(pascal_function_procedure_declaration pascal_function_procedure_declaration) {
        this.pascal_function_procedure_declaration = pascal_function_procedure_declaration;
    }
    public pascal_constant_definition_part getPascal_constant_definition_part() {
        return pascal_constant_definition_part;
    }

    public void setPascal_constant_definition_part(pascal_constant_definition_part pascal_constant_definition_part) {
        this.pascal_constant_definition_part = pascal_constant_definition_part;
    }
    public pascal_type_definition_part getPascal_type_definition_part() {
        return pascal_type_definition_part;
    }

    public void setPascal_type_definition_part(pascal_type_definition_part pascal_type_definition_part) {
        this.pascal_type_definition_part = pascal_type_definition_part;
    }
    public pascal_statement_part getPascal_statement_part() {
        return pascal_statement_part;
    }

    public void setPascal_statement_part(pascal_statement_part pascal_statement_part) {
        this.pascal_statement_part = pascal_statement_part;
    }
    public pascal_program getPascal_program() {
        return pascal_program;
    }

    public void setPascal_program(pascal_program pascal_program) {
        this.pascal_program = pascal_program;
    }
    public pascal_variable_declaration_part getPascal_variable_declaration_part() {
        return pascal_variable_declaration_part;
    }

    public void setPascal_variable_declaration_part(pascal_variable_declaration_part pascal_variable_declaration_part) {
        this.pascal_variable_declaration_part = pascal_variable_declaration_part;
    }

}