





import java.util.List;
import java.util.ArrayList;

public class pascal_tag_field  {

    private String name;





    private pascal_variant_part pascal_variant_part;


    public pascal_tag_field(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pascal_variant_part getPascal_variant_part() {
        return pascal_variant_part;
    }

    public void setPascal_variant_part(pascal_variant_part pascal_variant_part) {
        this.pascal_variant_part = pascal_variant_part;
    }

}