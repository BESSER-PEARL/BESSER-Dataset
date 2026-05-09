





import java.util.List;
import java.util.ArrayList;

public class EmigOcl_OperationCall extends PropertyCall {

    private String operationName;





    private List<EmigOcl_OclExpression> emigocl_oclexpressions;




    private EmigOcl_OclExpression emigocl_oclexpression;


    public EmigOcl_OperationCall(
        String operationName    ) {
        super(
        );
        this.operationName = operationName;
        this.emigocl_oclexpressions = new ArrayList<>();
    }

    public EmigOcl_OperationCall(
        String operationName        ArrayList<EmigOcl_OclExpression> emigocl_oclexpressions    ) {
        this.operationName = operationName;
        this.emigocl_oclexpressions = emigocl_oclexpressions;
    }

    public String getOperationname() {
        return operationName;
    }

    public void setOperationname(String operationName) {
        this.operationName = operationName;
    }

    public List<EmigOcl_OclExpression> getEmigocl_oclexpressions() {
        return emigocl_oclexpressions;
    }

    public void addEmigocl_oclexpression(Emigocl_oclexpression emigocl_oclexpression) {
        this.emigocl_oclexpressions.add(emigocl_oclexpression);
    }
    public EmigOcl_OclExpression getEmigocl_oclexpression() {
        return emigocl_oclexpression;
    }

    public void setEmigocl_oclexpression(EmigOcl_OclExpression emigocl_oclexpression) {
        this.emigocl_oclexpression = emigocl_oclexpression;
    }

}