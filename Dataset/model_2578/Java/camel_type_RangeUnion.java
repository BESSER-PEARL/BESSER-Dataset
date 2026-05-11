





import java.util.List;
import java.util.ArrayList;

public class camel_type_RangeUnion extends ValueType {

    private String primitiveType;



    public camel_type_RangeUnion(
        String primitiveType    ) {
        super(
        );
        this.primitiveType = primitiveType;
    }


    public String getPrimitivetype() {
        return primitiveType;
    }

    public void setPrimitivetype(String primitiveType) {
        this.primitiveType = primitiveType;
    }


}