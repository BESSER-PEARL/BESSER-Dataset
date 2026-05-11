





import java.util.List;
import java.util.ArrayList;

public class pascal_field_list  {






    private pascal_fixed_part pascal_fixed_part;




    private pascal_record_type pascal_record_type;




    private pascal_variant_part pascal_variant_part;




    private pascal_variant pascal_variant;


    public pascal_field_list(
    ) {
    }



    public pascal_fixed_part getPascal_fixed_part() {
        return pascal_fixed_part;
    }

    public void setPascal_fixed_part(pascal_fixed_part pascal_fixed_part) {
        this.pascal_fixed_part = pascal_fixed_part;
    }
    public pascal_record_type getPascal_record_type() {
        return pascal_record_type;
    }

    public void setPascal_record_type(pascal_record_type pascal_record_type) {
        this.pascal_record_type = pascal_record_type;
    }
    public pascal_variant_part getPascal_variant_part() {
        return pascal_variant_part;
    }

    public void setPascal_variant_part(pascal_variant_part pascal_variant_part) {
        this.pascal_variant_part = pascal_variant_part;
    }
    public pascal_variant getPascal_variant() {
        return pascal_variant;
    }

    public void setPascal_variant(pascal_variant pascal_variant) {
        this.pascal_variant = pascal_variant;
    }

}