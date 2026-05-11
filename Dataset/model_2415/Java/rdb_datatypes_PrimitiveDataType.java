





import java.util.List;
import java.util.ArrayList;

public class rdb_datatypes_PrimitiveDataType extends DataType {

    private String type;



    public rdb_datatypes_PrimitiveDataType(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}