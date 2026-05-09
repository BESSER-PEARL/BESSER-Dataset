





import java.util.List;
import java.util.ArrayList;

public class ImperativeOCL_BlockExp extends ImperativeExpression {






    private List<OclExpression> oclexpressions;


    public ImperativeOCL_BlockExp(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public ImperativeOCL_BlockExp(
        ArrayList<OclExpression> oclexpressions    ) {
        this.oclexpressions = oclexpressions;
    }


    public List<OclExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }

}