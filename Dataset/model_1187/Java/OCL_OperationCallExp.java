





import java.util.List;
import java.util.ArrayList;

public class OCL_OperationCallExp extends FeaturePropertyCall {






    private List<OclExpression> oclexpressions;


    public OCL_OperationCallExp(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public OCL_OperationCallExp(
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