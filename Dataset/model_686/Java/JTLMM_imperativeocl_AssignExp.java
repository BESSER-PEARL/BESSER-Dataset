





import java.util.List;
import java.util.ArrayList;

public class JTLMM_imperativeocl_AssignExp extends ImperativeExpression {

    private boolean isReset;





    private OclExpression oclexpression;




    private List<OclExpression> oclexpressions;




    private OclExpression oclexpression;


    public JTLMM_imperativeocl_AssignExp(
        boolean isReset    ) {
        super(
        );
        this.isReset = isReset;
        this.oclexpressions = new ArrayList<>();
    }

    public JTLMM_imperativeocl_AssignExp(
        boolean isReset        ArrayList<OclExpression> oclexpressions    ) {
        this.isReset = isReset;
        this.oclexpressions = oclexpressions;
    }

    public boolean getIsreset() {
        return isReset;
    }

    public void setIsreset(boolean isReset) {
        this.isReset = isReset;
    }

    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
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

}