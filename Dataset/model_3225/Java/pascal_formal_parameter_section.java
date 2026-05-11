





import java.util.List;
import java.util.ArrayList;

public class pascal_formal_parameter_section  {






    private pascal_variable_parameter_section pascal_variable_parameter_section;




    private pascal_value_parameter_section pascal_value_parameter_section;




    private pascal_formal_parameter_list pascal_formal_parameter_list;




    private pascal_function_parameter_section pascal_function_parameter_section;




    private pascal_procedure_parameter_section pascal_procedure_parameter_section;


    public pascal_formal_parameter_section(
    ) {
    }



    public pascal_variable_parameter_section getPascal_variable_parameter_section() {
        return pascal_variable_parameter_section;
    }

    public void setPascal_variable_parameter_section(pascal_variable_parameter_section pascal_variable_parameter_section) {
        this.pascal_variable_parameter_section = pascal_variable_parameter_section;
    }
    public pascal_value_parameter_section getPascal_value_parameter_section() {
        return pascal_value_parameter_section;
    }

    public void setPascal_value_parameter_section(pascal_value_parameter_section pascal_value_parameter_section) {
        this.pascal_value_parameter_section = pascal_value_parameter_section;
    }
    public pascal_formal_parameter_list getPascal_formal_parameter_list() {
        return pascal_formal_parameter_list;
    }

    public void setPascal_formal_parameter_list(pascal_formal_parameter_list pascal_formal_parameter_list) {
        this.pascal_formal_parameter_list = pascal_formal_parameter_list;
    }
    public pascal_function_parameter_section getPascal_function_parameter_section() {
        return pascal_function_parameter_section;
    }

    public void setPascal_function_parameter_section(pascal_function_parameter_section pascal_function_parameter_section) {
        this.pascal_function_parameter_section = pascal_function_parameter_section;
    }
    public pascal_procedure_parameter_section getPascal_procedure_parameter_section() {
        return pascal_procedure_parameter_section;
    }

    public void setPascal_procedure_parameter_section(pascal_procedure_parameter_section pascal_procedure_parameter_section) {
        this.pascal_procedure_parameter_section = pascal_procedure_parameter_section;
    }

}