





import java.util.List;
import java.util.ArrayList;

public class JTLMM_essentialocl_OperationCallExp extends FeaturePropertyCall {






    private List<OclExpression> oclexpressions;




    private Operation operation;


    public JTLMM_essentialocl_OperationCallExp(
    ) {
        super(
        );
        this.oclexpressions = new ArrayList<>();
    }

    public JTLMM_essentialocl_OperationCallExp(
        ArrayList<OclExpression> oclexpressions    ) {
        this.oclexpressions = oclexpressions;
    }


    public List<OclExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }
    public Operation getOperation() {
        return operation;
    }

    public void setOperation(Operation operation) {
        this.operation = operation;
    }

}