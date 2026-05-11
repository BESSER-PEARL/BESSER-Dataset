





import java.util.List;
import java.util.ArrayList;

public class pcm_pc_av_repository_pc_av_OperationInterface extends Interface {






    private List<OperationSignature> operationsignatures;


    public pcm_pc_av_repository_pc_av_OperationInterface(
    ) {
        super(
        );
        this.operationsignatures = new ArrayList<>();
    }

    public pcm_pc_av_repository_pc_av_OperationInterface(
        ArrayList<OperationSignature> operationsignatures    ) {
        this.operationsignatures = operationsignatures;
    }


    public List<OperationSignature> getOperationsignatures() {
        return operationsignatures;
    }

    public void addOperationsignature(Operationsignature operationsignature) {
        this.operationsignatures.add(operationsignature);
    }

}