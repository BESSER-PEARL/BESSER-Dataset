





import java.util.List;
import java.util.ArrayList;

public class atlext_OCL_OclExpression extends TypedElement {

    private boolean implicitlyCasted;





    private OCL_atlext_Type ocl_atlext_type;


    public atlext_OCL_OclExpression(
        boolean implicitlyCasted    ) {
        super(
        );
        this.implicitlyCasted = implicitlyCasted;
    }


    public boolean getImplicitlycasted() {
        return implicitlyCasted;
    }

    public void setImplicitlycasted(boolean implicitlyCasted) {
        this.implicitlyCasted = implicitlyCasted;
    }

    public OCL_atlext_Type getOcl_atlext_type() {
        return ocl_atlext_type;
    }

    public void setOcl_atlext_type(OCL_atlext_Type ocl_atlext_type) {
        this.ocl_atlext_type = ocl_atlext_type;
    }

}