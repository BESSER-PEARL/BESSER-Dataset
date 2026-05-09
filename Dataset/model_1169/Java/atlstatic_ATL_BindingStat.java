





import java.util.List;
import java.util.ArrayList;

public class atlstatic_ATL_BindingStat extends Statement {

    private String propertyName;
    private String isAssignment;





    private OclExpression oclexpression;




    private OclExpression oclexpression;


    public atlstatic_ATL_BindingStat(
        String propertyName,        String isAssignment    ) {
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
    public String getIsassignment() {
        return isAssignment;
    }

    public void setIsassignment(String isAssignment) {
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