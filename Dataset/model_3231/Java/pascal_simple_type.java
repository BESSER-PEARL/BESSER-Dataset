





import java.util.List;
import java.util.ArrayList;

public class pascal_simple_type  {

    private String name;





    private pascal_array_type pascal_array_type;




    private pascal_type pascal_type;




    private pascal_subrange_type pascal_subrange_type;




    private pascal_enumerated_type pascal_enumerated_type;


    public pascal_simple_type(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pascal_array_type getPascal_array_type() {
        return pascal_array_type;
    }

    public void setPascal_array_type(pascal_array_type pascal_array_type) {
        this.pascal_array_type = pascal_array_type;
    }
    public pascal_type getPascal_type() {
        return pascal_type;
    }

    public void setPascal_type(pascal_type pascal_type) {
        this.pascal_type = pascal_type;
    }
    public pascal_subrange_type getPascal_subrange_type() {
        return pascal_subrange_type;
    }

    public void setPascal_subrange_type(pascal_subrange_type pascal_subrange_type) {
        this.pascal_subrange_type = pascal_subrange_type;
    }
    public pascal_enumerated_type getPascal_enumerated_type() {
        return pascal_enumerated_type;
    }

    public void setPascal_enumerated_type(pascal_enumerated_type pascal_enumerated_type) {
        this.pascal_enumerated_type = pascal_enumerated_type;
    }

}