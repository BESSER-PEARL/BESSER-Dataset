





import java.util.List;
import java.util.ArrayList;

public class pascal_constant_definition  {

    private String name;





    private pascal_constant_definition_part pascal_constant_definition_part;




    private pascal_constant pascal_constant;


    public pascal_constant_definition(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pascal_constant_definition_part getPascal_constant_definition_part() {
        return pascal_constant_definition_part;
    }

    public void setPascal_constant_definition_part(pascal_constant_definition_part pascal_constant_definition_part) {
        this.pascal_constant_definition_part = pascal_constant_definition_part;
    }
    public pascal_constant getPascal_constant() {
        return pascal_constant;
    }

    public void setPascal_constant(pascal_constant pascal_constant) {
        this.pascal_constant = pascal_constant;
    }

}