





import java.util.List;
import java.util.ArrayList;

public class pascal_formal_parameter_list  {






    private List<pascal_formal_parameter_section> pascal_formal_parameter_sections;




    private pascal_abstraction_heading pascal_abstraction_heading;


    public pascal_formal_parameter_list(
    ) {
        this.pascal_formal_parameter_sections = new ArrayList<>();
    }

    public pascal_formal_parameter_list(
        ArrayList<pascal_formal_parameter_section> pascal_formal_parameter_sections    ) {
        this.pascal_formal_parameter_sections = pascal_formal_parameter_sections;
    }


    public List<pascal_formal_parameter_section> getPascal_formal_parameter_sections() {
        return pascal_formal_parameter_sections;
    }

    public void addPascal_formal_parameter_section(Pascal_formal_parameter_section pascal_formal_parameter_section) {
        this.pascal_formal_parameter_sections.add(pascal_formal_parameter_section);
    }
    public pascal_abstraction_heading getPascal_abstraction_heading() {
        return pascal_abstraction_heading;
    }

    public void setPascal_abstraction_heading(pascal_abstraction_heading pascal_abstraction_heading) {
        this.pascal_abstraction_heading = pascal_abstraction_heading;
    }

}