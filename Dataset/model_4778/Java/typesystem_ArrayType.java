





import java.util.List;
import java.util.ArrayList;

public class typesystem_ArrayType extends DataType {

    private int dimensionality;
    private boolean multidimensional;
    private boolean dimensional;



    public typesystem_ArrayType(
        int dimensionality,        boolean multidimensional,        boolean dimensional    ) {
        super(
        );
        this.dimensionality = dimensionality;
        this.multidimensional = multidimensional;
        this.dimensional = dimensional;
    }


    public int getDimensionality() {
        return dimensionality;
    }

    public void setDimensionality(int dimensionality) {
        this.dimensionality = dimensionality;
    }
    public boolean getMultidimensional() {
        return multidimensional;
    }

    public void setMultidimensional(boolean multidimensional) {
        this.multidimensional = multidimensional;
    }
    public boolean getDimensional() {
        return dimensional;
    }

    public void setDimensional(boolean dimensional) {
        this.dimensional = dimensional;
    }


}