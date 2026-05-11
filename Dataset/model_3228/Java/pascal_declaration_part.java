





import java.util.List;
import java.util.ArrayList;

public class pascal_declaration_part  {






    private pascal_block pascal_block;




    private pascal_constant_definition_part pascal_constant_definition_part;




    private pascal_label_declaration_part pascal_label_declaration_part;




    private pascal_type_definition_part pascal_type_definition_part;




    private pascal_procedure_and_function_declaration_part pascal_procedure_and_function_declaration_part;




    private pascal_variable_declaration_part pascal_variable_declaration_part;


    public pascal_declaration_part(
    ) {
    }



    public pascal_block getPascal_block() {
        return pascal_block;
    }

    public void setPascal_block(pascal_block pascal_block) {
        this.pascal_block = pascal_block;
    }
    public pascal_constant_definition_part getPascal_constant_definition_part() {
        return pascal_constant_definition_part;
    }

    public void setPascal_constant_definition_part(pascal_constant_definition_part pascal_constant_definition_part) {
        this.pascal_constant_definition_part = pascal_constant_definition_part;
    }
    public pascal_label_declaration_part getPascal_label_declaration_part() {
        return pascal_label_declaration_part;
    }

    public void setPascal_label_declaration_part(pascal_label_declaration_part pascal_label_declaration_part) {
        this.pascal_label_declaration_part = pascal_label_declaration_part;
    }
    public pascal_type_definition_part getPascal_type_definition_part() {
        return pascal_type_definition_part;
    }

    public void setPascal_type_definition_part(pascal_type_definition_part pascal_type_definition_part) {
        this.pascal_type_definition_part = pascal_type_definition_part;
    }
    public pascal_procedure_and_function_declaration_part getPascal_procedure_and_function_declaration_part() {
        return pascal_procedure_and_function_declaration_part;
    }

    public void setPascal_procedure_and_function_declaration_part(pascal_procedure_and_function_declaration_part pascal_procedure_and_function_declaration_part) {
        this.pascal_procedure_and_function_declaration_part = pascal_procedure_and_function_declaration_part;
    }
    public pascal_variable_declaration_part getPascal_variable_declaration_part() {
        return pascal_variable_declaration_part;
    }

    public void setPascal_variable_declaration_part(pascal_variable_declaration_part pascal_variable_declaration_part) {
        this.pascal_variable_declaration_part = pascal_variable_declaration_part;
    }

}