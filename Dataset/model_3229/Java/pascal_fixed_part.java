





import java.util.List;
import java.util.ArrayList;

public class pascal_fixed_part  {






    private pascal_field_list pascal_field_list;




    private List<pascal_record_section> pascal_record_sections;


    public pascal_fixed_part(
    ) {
        this.pascal_record_sections = new ArrayList<>();
    }

    public pascal_fixed_part(
        ArrayList<pascal_record_section> pascal_record_sections    ) {
        this.pascal_record_sections = pascal_record_sections;
    }


    public pascal_field_list getPascal_field_list() {
        return pascal_field_list;
    }

    public void setPascal_field_list(pascal_field_list pascal_field_list) {
        this.pascal_field_list = pascal_field_list;
    }
    public List<pascal_record_section> getPascal_record_sections() {
        return pascal_record_sections;
    }

    public void addPascal_record_section(Pascal_record_section pascal_record_section) {
        this.pascal_record_sections.add(pascal_record_section);
    }

}