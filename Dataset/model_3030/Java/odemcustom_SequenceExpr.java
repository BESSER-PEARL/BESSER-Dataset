





import java.util.List;
import java.util.ArrayList;

public class odemcustom_SequenceExpr extends RhsExpression {






    private List<odemcustom_RhsExpression> odemcustom_rhsexpressions;


    public odemcustom_SequenceExpr(
    ) {
        super(
        );
        this.odemcustom_rhsexpressions = new ArrayList<>();
    }

    public odemcustom_SequenceExpr(
        ArrayList<odemcustom_RhsExpression> odemcustom_rhsexpressions    ) {
        this.odemcustom_rhsexpressions = odemcustom_rhsexpressions;
    }


    public List<odemcustom_RhsExpression> getOdemcustom_rhsexpressions() {
        return odemcustom_rhsexpressions;
    }

    public void addOdemcustom_rhsexpression(Odemcustom_rhsexpression odemcustom_rhsexpression) {
        this.odemcustom_rhsexpressions.add(odemcustom_rhsexpression);
    }

}