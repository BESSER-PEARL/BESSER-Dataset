





import java.util.List;
import java.util.ArrayList;

public class simpleocl_OperationCall extends PropertyCall {

    private String operationName;





    private simpleocl_OclExpression simpleocl_oclexpression;




    private List<simpleocl_OclExpression> simpleocl_oclexpressions;


    public simpleocl_OperationCall(
        String operationName    ) {
        super(
        );
        this.operationName = operationName;
        this.simpleocl_oclexpressions = new ArrayList<>();
    }

    public simpleocl_OperationCall(
        String operationName        ArrayList<simpleocl_OclExpression> simpleocl_oclexpressions    ) {
        this.operationName = operationName;
        this.simpleocl_oclexpressions = simpleocl_oclexpressions;
    }

    public String getOperationname() {
        return operationName;
    }

    public void setOperationname(String operationName) {
        this.operationName = operationName;
    }

    public simpleocl_OclExpression getSimpleocl_oclexpression() {
        return simpleocl_oclexpression;
    }

    public void setSimpleocl_oclexpression(simpleocl_OclExpression simpleocl_oclexpression) {
        this.simpleocl_oclexpression = simpleocl_oclexpression;
    }
    public List<simpleocl_OclExpression> getSimpleocl_oclexpressions() {
        return simpleocl_oclexpressions;
    }

    public void addSimpleocl_oclexpression(Simpleocl_oclexpression simpleocl_oclexpression) {
        this.simpleocl_oclexpressions.add(simpleocl_oclexpression);
    }

}