





import java.util.List;
import java.util.ArrayList;

public class pascal_case_label_list  {






    private List<pascal_constant> pascal_constants;




    private pascal_variant pascal_variant;


    public pascal_case_label_list(
    ) {
        this.pascal_constants = new ArrayList<>();
    }

    public pascal_case_label_list(
        ArrayList<pascal_constant> pascal_constants    ) {
        this.pascal_constants = pascal_constants;
    }


    public List<pascal_constant> getPascal_constants() {
        return pascal_constants;
    }

    public void addPascal_constant(Pascal_constant pascal_constant) {
        this.pascal_constants.add(pascal_constant);
    }
    public pascal_variant getPascal_variant() {
        return pascal_variant;
    }

    public void setPascal_variant(pascal_variant pascal_variant) {
        this.pascal_variant = pascal_variant;
    }

}