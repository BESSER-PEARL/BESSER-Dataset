





import java.util.List;
import java.util.ArrayList;

public class pascal_identifier_list  {

    private String names;





    private pascal_value_parameter_section pascal_value_parameter_section;




    private pascal_record_section pascal_record_section;




    private pascal_variable_parameter_section pascal_variable_parameter_section;


    public pascal_identifier_list(
        String names    ) {
        this.names = names;
    }


    public String getNames() {
        return names;
    }

    public void setNames(String names) {
        this.names = names;
    }

    public pascal_value_parameter_section getPascal_value_parameter_section() {
        return pascal_value_parameter_section;
    }

    public void setPascal_value_parameter_section(pascal_value_parameter_section pascal_value_parameter_section) {
        this.pascal_value_parameter_section = pascal_value_parameter_section;
    }
    public pascal_record_section getPascal_record_section() {
        return pascal_record_section;
    }

    public void setPascal_record_section(pascal_record_section pascal_record_section) {
        this.pascal_record_section = pascal_record_section;
    }
    public pascal_variable_parameter_section getPascal_variable_parameter_section() {
        return pascal_variable_parameter_section;
    }

    public void setPascal_variable_parameter_section(pascal_variable_parameter_section pascal_variable_parameter_section) {
        this.pascal_variable_parameter_section = pascal_variable_parameter_section;
    }

}