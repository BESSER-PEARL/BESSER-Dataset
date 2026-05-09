





import java.util.List;
import java.util.ArrayList;

public class OCLinEmig_OperationCallExp extends PropertyCallExp {

    private String operationName;





    private List<OCLinEmig_OclExpression> oclinemig_oclexpressions;




    private OCLinEmig_OclExpression oclinemig_oclexpression;


    public OCLinEmig_OperationCallExp(
        String operationName    ) {
        super(
        );
        this.operationName = operationName;
        this.oclinemig_oclexpressions = new ArrayList<>();
    }

    public OCLinEmig_OperationCallExp(
        String operationName        ArrayList<OCLinEmig_OclExpression> oclinemig_oclexpressions    ) {
        this.operationName = operationName;
        this.oclinemig_oclexpressions = oclinemig_oclexpressions;
    }

    public String getOperationname() {
        return operationName;
    }

    public void setOperationname(String operationName) {
        this.operationName = operationName;
    }

    public List<OCLinEmig_OclExpression> getOclinemig_oclexpressions() {
        return oclinemig_oclexpressions;
    }

    public void addOclinemig_oclexpression(Oclinemig_oclexpression oclinemig_oclexpression) {
        this.oclinemig_oclexpressions.add(oclinemig_oclexpression);
    }
    public OCLinEmig_OclExpression getOclinemig_oclexpression() {
        return oclinemig_oclexpression;
    }

    public void setOclinemig_oclexpression(OCLinEmig_OclExpression oclinemig_oclexpression) {
        this.oclinemig_oclexpression = oclinemig_oclexpression;
    }

}