





import java.util.List;
import java.util.ArrayList;

public class pascal_tag_field  {

    private String id;





    private pascal_variant_part pascal_variant_part;


    public pascal_tag_field(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public pascal_variant_part getPascal_variant_part() {
        return pascal_variant_part;
    }

    public void setPascal_variant_part(pascal_variant_part pascal_variant_part) {
        this.pascal_variant_part = pascal_variant_part;
    }

}