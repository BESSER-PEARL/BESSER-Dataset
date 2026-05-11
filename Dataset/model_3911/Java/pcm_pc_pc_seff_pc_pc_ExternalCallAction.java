





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_pc_seff_pc_pc_ExternalCallAction extends seff_pc_pc_CallReturnAction, seff_reliability_pc_pc_FailureHandlingEntity, seff_pc_pc_AbstractAction {

    private int retryCount;





    private OperationSignature operationsignature;




    private OperationRequiredRole operationrequiredrole;


    public pcm_pc_pc_seff_pc_pc_ExternalCallAction(
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

    public OperationSignature getOperationsignature() {
        return operationsignature;
    }

    public void setOperationsignature(OperationSignature operationsignature) {
        this.operationsignature = operationsignature;
    }
    public OperationRequiredRole getOperationrequiredrole() {
        return operationrequiredrole;
    }

    public void setOperationrequiredrole(OperationRequiredRole operationrequiredrole) {
        this.operationrequiredrole = operationrequiredrole;
    }

}