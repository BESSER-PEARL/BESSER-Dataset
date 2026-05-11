





import java.util.List;
import java.util.ArrayList;

public class pascal_identifier_list  {

    private String ids;





    private pascal_enumerated_type pascal_enumerated_type;




    private pascal_record_section pascal_record_section;




    private pascal_program_heading pascal_program_heading;




    private pascal_value_parameter_section pascal_value_parameter_section;




    private pascal_variable_parameter_section pascal_variable_parameter_section;


    public pascal_identifier_list(
        String ids    ) {
        this.ids = ids;
    }


    public String getIds() {
        return ids;
    }

    public void setIds(String ids) {
        this.ids = ids;
    }

    public pascal_enumerated_type getPascal_enumerated_type() {
        return pascal_enumerated_type;
    }

    public void setPascal_enumerated_type(pascal_enumerated_type pascal_enumerated_type) {
        this.pascal_enumerated_type = pascal_enumerated_type;
    }
    public pascal_record_section getPascal_record_section() {
        return pascal_record_section;
    }

    public void setPascal_record_section(pascal_record_section pascal_record_section) {
        this.pascal_record_section = pascal_record_section;
    }
    public pascal_program_heading getPascal_program_heading() {
        return pascal_program_heading;
    }

    public void setPascal_program_heading(pascal_program_heading pascal_program_heading) {
        this.pascal_program_heading = pascal_program_heading;
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