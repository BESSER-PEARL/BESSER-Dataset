





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_seff_pc_ExternalCallAction extends seff_reliability_pc_FailureHandlingEntity, seff_pc_AbstractAction, seff_pc_CallReturnAction {

    private int retryCount;





    private OperationRequiredRole operationrequiredrole;




    private OperationSignature operationsignature;


    public pcm_pc_seff_pc_ExternalCallAction(
        int retryCount    ) {
        super(
        );
        this.retryCount = retryCount;
    }


    public int getRetrycount() {
        return retryCount;
    }

    public void setRetrycount(int retryCount) {
        this.retryCount = retryCount;
    }

    public OperationRequiredRole getOperationrequiredrole() {
        return operationrequiredrole;
    }

    public void setOperationrequiredrole(OperationRequiredRole operationrequiredrole) {
        this.operationrequiredrole = operationrequiredrole;
    }
    public OperationSignature getOperationsignature() {
        return operationsignature;
    }

    public void setOperationsignature(OperationSignature operationsignature) {
        this.operationsignature = operationsignature;
    }

}