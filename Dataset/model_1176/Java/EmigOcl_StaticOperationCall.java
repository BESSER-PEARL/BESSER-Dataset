





import java.util.List;
import java.util.ArrayList;

public class EmigOcl_StaticOperationCall extends StaticPropertyCall {

    private String operationName;





    private List<EmigOcl_OclExpression> emigocl_oclexpressions;


    public EmigOcl_StaticOperationCall(
        String operationName    ) {
        super(
        );
        this.operationName = operationName;
        this.emigocl_oclexpressions = new ArrayList<>();
    }

    public EmigOcl_StaticOperationCall(
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

}