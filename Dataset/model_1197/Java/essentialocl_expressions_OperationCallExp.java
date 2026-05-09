





import java.util.List;
import java.util.ArrayList;

public class essentialocl_expressions_OperationCallExp extends FeatureCallExp {






    private List<OclExpression> oclexpressions;


    public essentialocl_expressions_OperationCallExp(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public essentialocl_expressions_OperationCallExp(
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