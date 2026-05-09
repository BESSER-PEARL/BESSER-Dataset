





import java.util.List;
import java.util.ArrayList;

public class ir_ocl_TuplePart  {

    private String name;





    private OclExpression oclexpression;


    public ir_ocl_TuplePart(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}