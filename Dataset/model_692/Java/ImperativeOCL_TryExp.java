





import java.util.List;
import java.util.ArrayList;

public class ImperativeOCL_TryExp extends ImperativeExpression {






    private List<OclExpression> oclexpressions;


    public ImperativeOCL_TryExp(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public ImperativeOCL_TryExp(
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