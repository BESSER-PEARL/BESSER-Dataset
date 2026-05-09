





import java.util.List;
import java.util.ArrayList;

public class OCL_OperationCallExp extends PropertyCallExp {

    private String operationName;



    public OCL_OperationCallExp(
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