





import java.util.List;
import java.util.ArrayList;

public class typesystem_ArrayType extends DataType {

    private int dimensionality;
    private boolean dimensional;
    private boolean multidimensional;





    private typesystem_DataType typesystem_datatype;




    private typesystem_DataType typesystem_datatype;


    public typesystem_ArrayType(
        int dimensionality,        boolean dimensional,        boolean multidimensional    ) {
        super(
        );
        this.dimensionality = dimensionality;
        this.dimensional = dimensional;
        this.multidimensional = multidimensional;
    }


    public int getDimensionality() {
        return dimensionality;
    }

    public void setDimensionality(int dimensionality) {
        this.dimensionality = dimensionality;
    }
    public boolean getDimensional() {
        return dimensional;
    }

    public void setDimensional(boolean dimensional) {
        this.dimensional = dimensional;
    }
    public boolean getMultidimensional() {
        return multidimensional;
    }

    public void setMultidimensional(boolean multidimensional) {
        this.multidimensional = multidimensional;
    }

    public typesystem_DataType getTypesystem_datatype() {
        return typesystem_datatype;
    }

    public void setTypesystem_datatype(typesystem_DataType typesystem_datatype) {
        this.typesystem_datatype = typesystem_datatype;
    }
    public typesystem_DataType getTypesystem_datatype() {
        return typesystem_datatype;
    }

    public void setTypesystem_datatype(typesystem_DataType typesystem_datatype) {
        this.typesystem_datatype = typesystem_datatype;
    }

}