





import java.util.List;
import java.util.ArrayList;

public class pascal_constant_definition_part  {






    private pascal_declaration_part pascal_declaration_part;




    private List<pascal_constant_definition> pascal_constant_definitions;


    public pascal_constant_definition_part(
    ) {
        this.pascal_constant_definitions = new ArrayList<>();
    }

    public pascal_constant_definition_part(
        ArrayList<pascal_constant_definition> pascal_constant_definitions    ) {
        this.pascal_constant_definitions = pascal_constant_definitions;
    }


    public pascal_declaration_part getPascal_declaration_part() {
        return pascal_declaration_part;
    }

    public void setPascal_declaration_part(pascal_declaration_part pascal_declaration_part) {
        this.pascal_declaration_part = pascal_declaration_part;
    }
    public List<pascal_constant_definition> getPascal_constant_definitions() {
        return pascal_constant_definitions;
    }

    public void addPascal_constant_definition(Pascal_constant_definition pascal_constant_definition) {
        this.pascal_constant_definitions.add(pascal_constant_definition);
    }

}