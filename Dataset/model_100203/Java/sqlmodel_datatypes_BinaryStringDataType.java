





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_datatypes_BinaryStringDataType extends PredefinedDataType {

    private int length;



    public sqlmodel_datatypes_BinaryStringDataType(
        int length    ) {
        super(
        );
        this.length = length;
    }


    public int getLength() {
        return length;
    }

    public void setLength(int length) {
        this.length = length;
    }


}