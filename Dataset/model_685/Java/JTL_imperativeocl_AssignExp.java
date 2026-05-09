





import java.util.List;
import java.util.ArrayList;

public class JTL_imperativeocl_AssignExp extends ImperativeExpression {

    private boolean isReset;





    private List<OclExpression> oclexpressions;




    private OclExpression oclexpression;




    private OclExpression oclexpression;


    public JTL_imperativeocl_AssignExp(
        boolean isReset    ) {
        super(
        );
        this.isReset = isReset;
        this.oclexpressions = new ArrayList<>();
    }

    public JTL_imperativeocl_AssignExp(
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