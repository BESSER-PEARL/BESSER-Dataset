





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_datatypes_ExactNumericDataType extends NumericalDataType {

    private int scale;



    public sqlmodel_datatypes_ExactNumericDataType(
        int scale    ) {
        super(
        );
        this.scale = scale;
    }


    public int getScale() {
        return scale;
    }

    public void setScale(int scale) {
        this.scale = scale;
    }


}