





import java.util.List;
import java.util.ArrayList;

public class pascal_parameter_type  {

    private String name;





    private pascal_value_parameter_section pascal_value_parameter_section;




    private pascal_variable_parameter_section pascal_variable_parameter_section;


    public pascal_parameter_type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pascal_value_parameter_section getPascal_value_parameter_section() {
        return pascal_value_parameter_section;
    }

    public void setPascal_value_parameter_section(pascal_value_parameter_section pascal_value_parameter_section) {
        this.pascal_value_parameter_section = pascal_value_parameter_section;
    }
    public pascal_variable_parameter_section getPascal_variable_parameter_section() {
        return pascal_variable_parameter_section;
    }

    public void setPascal_variable_parameter_section(pascal_variable_parameter_section pascal_variable_parameter_section) {
        this.pascal_variable_parameter_section = pascal_variable_parameter_section;
    }

}