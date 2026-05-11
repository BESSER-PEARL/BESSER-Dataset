





import java.util.List;
import java.util.ArrayList;

public class pascal_parameter_type  {






    private pascal_type_identifier pascal_type_identifier;




    private pascal_variable_parameter_section pascal_variable_parameter_section;




    private pascal_value_parameter_section pascal_value_parameter_section;


    public pascal_parameter_type(
    ) {
    }



    public pascal_type_identifier getPascal_type_identifier() {
        return pascal_type_identifier;
    }

    public void setPascal_type_identifier(pascal_type_identifier pascal_type_identifier) {
        this.pascal_type_identifier = pascal_type_identifier;
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

}