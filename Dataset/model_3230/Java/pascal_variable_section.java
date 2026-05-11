





import java.util.List;
import java.util.ArrayList;

public class pascal_variable_section  {






    private pascal_variable_identifier_list pascal_variable_identifier_list;




    private pascal_type pascal_type;




    private pascal_variable_declaration_part pascal_variable_declaration_part;


    public pascal_variable_section(
    ) {
    }



    public pascal_variable_identifier_list getPascal_variable_identifier_list() {
        return pascal_variable_identifier_list;
    }

    public void setPascal_variable_identifier_list(pascal_variable_identifier_list pascal_variable_identifier_list) {
        this.pascal_variable_identifier_list = pascal_variable_identifier_list;
    }
    public pascal_type getPascal_type() {
        return pascal_type;
    }

    public void setPascal_type(pascal_type pascal_type) {
        this.pascal_type = pascal_type;
    }
    public pascal_variable_declaration_part getPascal_variable_declaration_part() {
        return pascal_variable_declaration_part;
    }

    public void setPascal_variable_declaration_part(pascal_variable_declaration_part pascal_variable_declaration_part) {
        this.pascal_variable_declaration_part = pascal_variable_declaration_part;
    }

}