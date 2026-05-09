





import java.util.List;
import java.util.ArrayList;

public class java_ArrayType extends Type {

    private int dimensions;



    public java_ArrayType(
        int dimensions    ) {
        super(
        );
        this.dimensions = dimensions;
    }


    public int getDimensions() {
        return dimensions;
    }

    public void setDimensions(int dimensions) {
        this.dimensions = dimensions;
    }


}