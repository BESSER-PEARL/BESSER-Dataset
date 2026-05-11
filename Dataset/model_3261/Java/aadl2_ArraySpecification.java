





import java.util.List;
import java.util.ArrayList;

public class aadl2_ArraySpecification extends Element {

    private String dimension;





    private aadl2_ArrayableElement aadl2_arrayableelement;


    public aadl2_ArraySpecification(
        String dimension    ) {
        super(
        );
        this.dimension = dimension;
    }


    public String getDimension() {
        return dimension;
    }

    public void setDimension(String dimension) {
        this.dimension = dimension;
    }

    public aadl2_ArrayableElement getAadl2_arrayableelement() {
        return aadl2_arrayableelement;
    }

    public void setAadl2_arrayableelement(aadl2_ArrayableElement aadl2_arrayableelement) {
        this.aadl2_arrayableelement = aadl2_arrayableelement;
    }

}