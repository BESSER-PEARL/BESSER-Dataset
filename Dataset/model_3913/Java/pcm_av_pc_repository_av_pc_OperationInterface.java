





import java.util.List;
import java.util.ArrayList;

public class pcm_av_pc_repository_av_pc_OperationInterface extends Interface {






    private List<OperationSignature> operationsignatures;


    public pcm_av_pc_repository_av_pc_OperationInterface(
    ) {
        super(
        );
        this.operationsignatures = new ArrayList<>();
    }

    public pcm_av_pc_repository_av_pc_OperationInterface(
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