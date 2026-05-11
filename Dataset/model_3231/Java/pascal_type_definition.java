





import java.util.List;
import java.util.ArrayList;

public class pascal_type_definition  {

    private String name;





    private pascal_type_definition_part pascal_type_definition_part;


    public pascal_type_definition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pascal_type_definition_part getPascal_type_definition_part() {
        return pascal_type_definition_part;
    }

    public void setPascal_type_definition_part(pascal_type_definition_part pascal_type_definition_part) {
        this.pascal_type_definition_part = pascal_type_definition_part;
    }

}