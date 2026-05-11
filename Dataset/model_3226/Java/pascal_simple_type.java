





import java.util.List;
import java.util.ArrayList;

public class pascal_simple_type  {

    private String primitiveType;





    private pascal_type pascal_type;


    public pascal_simple_type(
        String primitiveType    ) {
        this.primitiveType = primitiveType;
    }


    public String getPrimitivetype() {
        return primitiveType;
    }

    public void setPrimitivetype(String primitiveType) {
        this.primitiveType = primitiveType;
    }

    public pascal_type getPascal_type() {
        return pascal_type;
    }

    public void setPascal_type(pascal_type pascal_type) {
        this.pascal_type = pascal_type;
    }

}