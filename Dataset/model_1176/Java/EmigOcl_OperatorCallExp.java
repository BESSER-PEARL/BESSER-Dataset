





import java.util.List;
import java.util.ArrayList;

public class EmigOcl_OperatorCallExp extends PropertyCallExp {

    private String operationName;





    private EmigOcl_OclExpression emigocl_oclexpression;


    public EmigOcl_OperatorCallExp(
        String operationName    ) {
        super(
        );
        this.operationName = operationName;
    }


    public String getOperationname() {
        return operationName;
    }

    public void setOperationname(String operationName) {
        this.operationName = operationName;
    }

    public EmigOcl_OclExpression getEmigocl_oclexpression() {
        return emigocl_oclexpression;
    }

    public void setEmigocl_oclexpression(EmigOcl_OclExpression emigocl_oclexpression) {
        this.emigocl_oclexpression = emigocl_oclexpression;
    }

}