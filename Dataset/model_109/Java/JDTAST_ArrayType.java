





import java.util.List;
import java.util.ArrayList;

public class JDTAST_ArrayType extends Type {

    private String dimensions;





    private JDTAST_Type jdtast_type;




    private JDTAST_ArrayCreation jdtast_arraycreation;




    private JDTAST_Type jdtast_type;


    public JDTAST_ArrayType(
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

    public JDTAST_Type getJdtast_type() {
        return jdtast_type;
    }

    public void setJdtast_type(JDTAST_Type jdtast_type) {
        this.jdtast_type = jdtast_type;
    }
    public JDTAST_ArrayCreation getJdtast_arraycreation() {
        return jdtast_arraycreation;
    }

    public void setJdtast_arraycreation(JDTAST_ArrayCreation jdtast_arraycreation) {
        this.jdtast_arraycreation = jdtast_arraycreation;
    }
    public JDTAST_Type getJdtast_type() {
        return jdtast_type;
    }

    public void setJdtast_type(JDTAST_Type jdtast_type) {
        this.jdtast_type = jdtast_type;
    }

}