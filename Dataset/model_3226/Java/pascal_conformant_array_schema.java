





import java.util.List;
import java.util.ArrayList;

public class pascal_conformant_array_schema  {

    private String id;





    private pascal_parameter_type pascal_parameter_type;


    public pascal_conformant_array_schema(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public pascal_parameter_type getPascal_parameter_type() {
        return pascal_parameter_type;
    }

    public void setPascal_parameter_type(pascal_parameter_type pascal_parameter_type) {
        this.pascal_parameter_type = pascal_parameter_type;
    }

}