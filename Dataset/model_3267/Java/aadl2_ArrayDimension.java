





import java.util.List;
import java.util.ArrayList;

public class aadl2_ArrayDimension extends Element {






    private aadl2_ArraySize aadl2_arraysize;




    private aadl2_ArrayableElement aadl2_arrayableelement;


    public aadl2_ArrayDimension(
    ) {
        super(
        );
    }



    public aadl2_ArraySize getAadl2_arraysize() {
        return aadl2_arraysize;
    }

    public void setAadl2_arraysize(aadl2_ArraySize aadl2_arraysize) {
        this.aadl2_arraysize = aadl2_arraysize;
    }
    public aadl2_ArrayableElement getAadl2_arrayableelement() {
        return aadl2_arrayableelement;
    }

    public void setAadl2_arrayableelement(aadl2_ArrayableElement aadl2_arrayableelement) {
        this.aadl2_arrayableelement = aadl2_arrayableelement;
    }

}