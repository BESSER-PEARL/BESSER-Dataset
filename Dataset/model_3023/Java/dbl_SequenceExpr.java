





import java.util.List;
import java.util.ArrayList;

public class dbl_SequenceExpr extends RhsExpression {






    private List<dbl_RhsExpression> dbl_rhsexpressions;


    public dbl_SequenceExpr(
    ) {
        super(
        );
        this.dbl_rhsexpressions = new ArrayList<>();
    }

    public dbl_SequenceExpr(
        ArrayList<dbl_RhsExpression> dbl_rhsexpressions    ) {
        this.dbl_rhsexpressions = dbl_rhsexpressions;
    }


    public List<dbl_RhsExpression> getDbl_rhsexpressions() {
        return dbl_rhsexpressions;
    }

    public void addDbl_rhsexpression(Dbl_rhsexpression dbl_rhsexpression) {
        this.dbl_rhsexpressions.add(dbl_rhsexpression);
    }

}