





import java.util.List;
import java.util.ArrayList;

public class atl_n_ocl_OCL_Attribute extends OclFeature {

    private String name;





    private OclType ocltype;




    private OclExpression oclexpression;


    public atl_n_ocl_OCL_Attribute(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public OclType getOcltype() {
        return ocltype;
    }

    public void setOcltype(OclType ocltype) {
        this.ocltype = ocltype;
    }
    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}