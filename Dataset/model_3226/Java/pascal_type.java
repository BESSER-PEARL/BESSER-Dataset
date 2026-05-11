





import java.util.List;
import java.util.ArrayList;

public class pascal_type extends type_definition {

    private String name;





    private pascal_variable_declaration pascal_variable_declaration;


    public pascal_type(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pascal_variable_declaration getPascal_variable_declaration() {
        return pascal_variable_declaration;
    }

    public void setPascal_variable_declaration(pascal_variable_declaration pascal_variable_declaration) {
        this.pascal_variable_declaration = pascal_variable_declaration;
    }

}