





import java.util.List;
import java.util.ArrayList;

public class atl_n_ocl_ATL_BindingStat extends Statement {

    private String propertyName;
    private boolean isAssignment;





    private OclExpression oclexpression;




    private OclExpression oclexpression;


    public atl_n_ocl_ATL_BindingStat(
        String propertyName,        boolean isAssignment    ) {
        super(
        );
        this.propertyName = propertyName;
        this.isAssignment = isAssignment;
    }


    public String getPropertyname() {
        return propertyName;
    }

    public void setPropertyname(String propertyName) {
        this.propertyName = propertyName;
    }
    public boolean getIsassignment() {
        return isAssignment;
    }

    public void setIsassignment(boolean isAssignment) {
        this.isAssignment = isAssignment;
    }

    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }
    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}