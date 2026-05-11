





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_av_seff_pc_av_ExternalCallAction extends seff_pc_av_CallReturnAction, seff_pc_av_AbstractAction, seff_reliability_pc_av_FailureHandlingEntity {

    private int retryCount;





    private OperationSignature operationsignature;




    private OperationRequiredRole operationrequiredrole;


    public pcm_pc_av_seff_pc_av_ExternalCallAction(
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