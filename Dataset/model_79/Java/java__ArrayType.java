





import java.util.List;
import java.util.ArrayList;

public class java__ArrayType extends Type {

    private int dimensions;





    private java__TypeAccess java__typeaccess;


    public java__ArrayType(
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

    public java__TypeAccess getJava__typeaccess() {
        return java__typeaccess;
    }

    public void setJava__typeaccess(java__TypeAccess java__typeaccess) {
        this.java__typeaccess = java__typeaccess;
    }

}