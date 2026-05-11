





import java.util.List;
import java.util.ArrayList;

public class pascal_array_type  {






    private List<pascal_simple_type> pascal_simple_types;




    private pascal_unpacked_structured_type pascal_unpacked_structured_type;


    public pascal_array_type(
    ) {
        this.pascal_simple_types = new ArrayList<>();
    }

    public pascal_array_type(
        ArrayList<pascal_simple_type> pascal_simple_types    ) {
        this.pascal_simple_types = pascal_simple_types;
    }


    public List<pascal_simple_type> getPascal_simple_types() {
        return pascal_simple_types;
    }

    public void addPascal_simple_type(Pascal_simple_type pascal_simple_type) {
        this.pascal_simple_types.add(pascal_simple_type);
    }
    public pascal_unpacked_structured_type getPascal_unpacked_structured_type() {
        return pascal_unpacked_structured_type;
    }

    public void setPascal_unpacked_structured_type(pascal_unpacked_structured_type pascal_unpacked_structured_type) {
        this.pascal_unpacked_structured_type = pascal_unpacked_structured_type;
    }

}