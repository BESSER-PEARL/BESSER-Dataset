





import java.util.List;
import java.util.ArrayList;

public class pascal_variable_declaration_part  {






    private List<pascal_variable_section> pascal_variable_sections;


    public pascal_variable_declaration_part(
    ) {
        this.pascal_variable_sections = new ArrayList<>();
    }

    public pascal_variable_declaration_part(
        ArrayList<pascal_variable_section> pascal_variable_sections    ) {
        this.pascal_variable_sections = pascal_variable_sections;
    }


    public List<pascal_variable_section> getPascal_variable_sections() {
        return pascal_variable_sections;
    }

    public void addPascal_variable_section(Pascal_variable_section pascal_variable_section) {
        this.pascal_variable_sections.add(pascal_variable_section);
    }

}