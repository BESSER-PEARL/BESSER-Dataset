





import java.util.List;
import java.util.ArrayList;

public class gbind_simpleocl_OperatorCallExp extends OclExpression {

    private String operationName;



    public gbind_simpleocl_OperatorCallExp(
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


}