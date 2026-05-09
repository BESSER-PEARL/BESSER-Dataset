





import java.util.List;
import java.util.ArrayList;

public class gbind_simpleocl_OperationCall extends PropertyCall {

    private String operationName;





    private List<OclExpression> oclexpressions;


    public gbind_simpleocl_OperationCall(
        String operationName    ) {
        super(
        );
        this.operationName = operationName;
        this.oclexpressions = new ArrayList<>();
    }

    public gbind_simpleocl_OperationCall(
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