





import java.util.List;
import java.util.ArrayList;

public class pascal_type  {






    private pascal_type_definition pascal_type_definition;




    private pascal_structured_type pascal_structured_type;




    private pascal_variable_section pascal_variable_section;




    private pascal_record_section pascal_record_section;




    private pascal_simple_type pascal_simple_type;


    public pascal_type(
    ) {
    }



    public pascal_type_definition getPascal_type_definition() {
        return pascal_type_definition;
    }

    public void setPascal_type_definition(pascal_type_definition pascal_type_definition) {
        this.pascal_type_definition = pascal_type_definition;
    }
    public pascal_structured_type getPascal_structured_type() {
        return pascal_structured_type;
    }

    public void setPascal_structured_type(pascal_structured_type pascal_structured_type) {
        this.pascal_structured_type = pascal_structured_type;
    }
    public pascal_variable_section getPascal_variable_section() {
        return pascal_variable_section;
    }

    public void setPascal_variable_section(pascal_variable_section pascal_variable_section) {
        this.pascal_variable_section = pascal_variable_section;
    }
    public pascal_record_section getPascal_record_section() {
        return pascal_record_section;
    }

    public void setPascal_record_section(pascal_record_section pascal_record_section) {
        this.pascal_record_section = pascal_record_section;
    }
    public pascal_simple_type getPascal_simple_type() {
        return pascal_simple_type;
    }

    public void setPascal_simple_type(pascal_simple_type pascal_simple_type) {
        this.pascal_simple_type = pascal_simple_type;
    }

}