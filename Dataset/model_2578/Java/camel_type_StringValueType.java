





import java.util.List;
import java.util.ArrayList;

public class camel_type_StringValueType extends ValueType {

    private String primitiveType;



    public camel_type_StringValueType(
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