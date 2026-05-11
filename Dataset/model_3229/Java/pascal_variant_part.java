





import java.util.List;
import java.util.ArrayList;

public class pascal_variant_part  {

    private String name;





    private pascal_tag_field pascal_tag_field;




    private pascal_field_list pascal_field_list;




    private List<pascal_variant> pascal_variants;


    public pascal_variant_part(
        String name    ) {
        this.name = name;
        this.pascal_variants = new ArrayList<>();
    }

    public pascal_variant_part(
        String name        ArrayList<pascal_variant> pascal_variants    ) {
        this.name = name;
        this.pascal_variants = pascal_variants;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pascal_tag_field getPascal_tag_field() {
        return pascal_tag_field;
    }

    public void setPascal_tag_field(pascal_tag_field pascal_tag_field) {
        this.pascal_tag_field = pascal_tag_field;
    }
    public pascal_field_list getPascal_field_list() {
        return pascal_field_list;
    }

    public void setPascal_field_list(pascal_field_list pascal_field_list) {
        this.pascal_field_list = pascal_field_list;
    }
    public List<pascal_variant> getPascal_variants() {
        return pascal_variants;
    }

    public void addPascal_variant(Pascal_variant pascal_variant) {
        this.pascal_variants.add(pascal_variant);
    }

}