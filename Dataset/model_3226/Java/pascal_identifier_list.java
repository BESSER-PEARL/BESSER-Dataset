





import java.util.List;
import java.util.ArrayList;

public class pascal_identifier_list extends program_heading {

    private String ids;





    private pascal_variable_declaration pascal_variable_declaration;


    public pascal_identifier_list(
        String ids    ) {
        super(
        );
        this.ids = ids;
    }


    public String getIds() {
        return ids;
    }

    public void setIds(String ids) {
        this.ids = ids;
    }

    public pascal_variable_declaration getPascal_variable_declaration() {
        return pascal_variable_declaration;
    }

    public void setPascal_variable_declaration(pascal_variable_declaration pascal_variable_declaration) {
        this.pascal_variable_declaration = pascal_variable_declaration;
    }

}