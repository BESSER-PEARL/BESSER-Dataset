





import java.util.List;
import java.util.ArrayList;

public class pascal_record_section  {






    private pascal_identifier_list pascal_identifier_list;




    private pascal_type pascal_type;




    private pascal_fixed_part pascal_fixed_part;


    public pascal_record_section(
    ) {
    }



    public pascal_identifier_list getPascal_identifier_list() {
        return pascal_identifier_list;
    }

    public void setPascal_identifier_list(pascal_identifier_list pascal_identifier_list) {
        this.pascal_identifier_list = pascal_identifier_list;
    }
    public pascal_type getPascal_type() {
        return pascal_type;
    }

    public void setPascal_type(pascal_type pascal_type) {
        this.pascal_type = pascal_type;
    }
    public pascal_fixed_part getPascal_fixed_part() {
        return pascal_fixed_part;
    }

    public void setPascal_fixed_part(pascal_fixed_part pascal_fixed_part) {
        this.pascal_fixed_part = pascal_fixed_part;
    }

}