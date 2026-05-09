





import java.util.List;
import java.util.ArrayList;

public class ImperativeOCL_AssignExp extends ImperativeExpression {

    private String isReset;





    private List<OclExpression> oclexpressions;




    private OclExpression oclexpression;




    private OclExpression oclexpression;


    public ImperativeOCL_AssignExp(
        String isReset    ) {
        super(
        );
        this.isReset = isReset;
        this.oclexpressions = new ArrayList<>();
    }

    public ImperativeOCL_AssignExp(
        String isReset        ArrayList<OclExpression> oclexpressions    ) {
        this.isReset = isReset;
        this.oclexpressions = oclexpressions;
    }

    public String getIsreset() {
        return isReset;
    }

    public void setIsreset(String isReset) {
        this.isReset = isReset;
    }

    public List<OclExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
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