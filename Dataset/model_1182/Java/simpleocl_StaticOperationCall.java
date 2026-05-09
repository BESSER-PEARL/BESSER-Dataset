





import java.util.List;
import java.util.ArrayList;

public class simpleocl_StaticOperationCall extends StaticPropertyCall {

    private String operationName;





    private List<simpleocl_OclExpression> simpleocl_oclexpressions;


    public simpleocl_StaticOperationCall(
        String operationName    ) {
        super(
        );
        this.operationName = operationName;
        this.simpleocl_oclexpressions = new ArrayList<>();
    }

    public simpleocl_StaticOperationCall(
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

    public List<simpleocl_OclExpression> getSimpleocl_oclexpressions() {
        return simpleocl_oclexpressions;
    }

    public void addSimpleocl_oclexpression(Simpleocl_oclexpression simpleocl_oclexpression) {
        this.simpleocl_oclexpressions.add(simpleocl_oclexpression);
    }

}