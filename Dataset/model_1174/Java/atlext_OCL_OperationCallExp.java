





import java.util.List;
import java.util.ArrayList;

public class atlext_OCL_OperationCallExp extends PropertyCallExp {

    private String operationName;





    private List<OclExpression> oclexpressions;


    public atlext_OCL_OperationCallExp(
        String operationName    ) {
        super(
        );
        this.operationName = operationName;
        this.oclexpressions = new ArrayList<>();
    }

    public atlext_OCL_OperationCallExp(
        String operationName        ArrayList<OclExpression> oclexpressions    ) {
        this.operationName = operationName;
        this.oclexpressions = oclexpressions;
    }

    public String getOperationname() {
        return operationName;
    }

    public void setOperationname(String operationName) {
        this.operationName = operationName;
    }

    public List<OclExpression> getOclexpressions() {
        return oclexpressions;
    }

    public void addOclexpression(Oclexpression oclexpression) {
        this.oclexpressions.add(oclexpression);
    }

}