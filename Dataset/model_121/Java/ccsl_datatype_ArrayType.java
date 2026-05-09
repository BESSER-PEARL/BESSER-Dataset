





import java.util.List;
import java.util.ArrayList;

public class ccsl_datatype_ArrayType extends ObjectType {

    private String dimensions;





    private datatype_DataType datatype_datatype;


    public ccsl_datatype_ArrayType(
        String dimensions    ) {
        super(
        );
        this.dimensions = dimensions;
    }


    public String getDimensions() {
        return dimensions;
    }

    public void setDimensions(String dimensions) {
        this.dimensions = dimensions;
    }

    public datatype_DataType getDatatype_datatype() {
        return datatype_datatype;
    }

    public void setDatatype_datatype(datatype_DataType datatype_datatype) {
        this.datatype_datatype = datatype_datatype;
    }

}