





import java.util.List;
import java.util.ArrayList;

public class pivot_OperationCallExp extends FeatureCallExp, ReferringElement {






    private List<pivot_OCLExpression> pivot_oclexpressions;




    private pivot_Operation pivot_operation;


    public pivot_OperationCallExp(
    ) {
        super(
        );
        this.pivot_oclexpressions = new ArrayList<>();
    }

    public pivot_OperationCallExp(
        ArrayList<pivot_OCLExpression> pivot_oclexpressions    ) {
        this.pivot_oclexpressions = pivot_oclexpressions;
    }


    public List<pivot_OCLExpression> getPivot_oclexpressions() {
        return pivot_oclexpressions;
    }

    public void addPivot_oclexpression(Pivot_oclexpression pivot_oclexpression) {
        this.pivot_oclexpressions.add(pivot_oclexpression);
    }
    public pivot_Operation getPivot_operation() {
        return pivot_operation;
    }

    public void setPivot_operation(pivot_Operation pivot_operation) {
        this.pivot_operation = pivot_operation;
    }

}