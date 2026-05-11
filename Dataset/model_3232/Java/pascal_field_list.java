





import java.util.List;
import java.util.ArrayList;

public class pascal_field_list  {






    private List<pascal_record_section> pascal_record_sections;




    private pascal_record_type pascal_record_type;


    public pascal_field_list(
    ) {
        this.pascal_record_sections = new ArrayList<>();
    }

    public pascal_field_list(
        ArrayList<pascal_record_section> pascal_record_sections    ) {
        this.pascal_record_sections = pascal_record_sections;
    }


    public List<pascal_record_section> getPascal_record_sections() {
        return pascal_record_sections;
    }

    public void addPascal_record_section(Pascal_record_section pascal_record_section) {
        this.pascal_record_sections.add(pascal_record_section);
    }
    public pascal_record_type getPascal_record_type() {
        return pascal_record_type;
    }

    public void setPascal_record_type(pascal_record_type pascal_record_type) {
        this.pascal_record_type = pascal_record_type;
    }

}