





import java.util.List;
import java.util.ArrayList;

public class simpleocl_OperationCall extends PropertyCall {

    private String operationName;



    public simpleocl_OperationCall(
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