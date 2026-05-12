





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_datatypes_PredefinedDataType extends SQLDataType {

    private String primitiveType;



    public sqlmodel_datatypes_PredefinedDataType(
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