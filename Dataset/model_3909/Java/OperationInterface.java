





import java.util.List;
import java.util.ArrayList;

public class OperationInterface  {






    private pcm_pc_repository_pc_OperationRequiredRole pcm_pc_repository_pc_operationrequiredrole;




    private pcm_pc_repository_pc_OperationSignature pcm_pc_repository_pc_operationsignature;




    private pcm_pc_repository_pc_OperationProvidedRole pcm_pc_repository_pc_operationprovidedrole;


    public OperationInterface(
    ) {
    }



    public pcm_pc_repository_pc_OperationRequiredRole getPcm_pc_repository_pc_operationrequiredrole() {
        return pcm_pc_repository_pc_operationrequiredrole;
    }

    public void setPcm_pc_repository_pc_operationrequiredrole(pcm_pc_repository_pc_OperationRequiredRole pcm_pc_repository_pc_operationrequiredrole) {
        this.pcm_pc_repository_pc_operationrequiredrole = pcm_pc_repository_pc_operationrequiredrole;
    }
    public pcm_pc_repository_pc_OperationSignature getPcm_pc_repository_pc_operationsignature() {
        return pcm_pc_repository_pc_operationsignature;
    }

    public void setPcm_pc_repository_pc_operationsignature(pcm_pc_repository_pc_OperationSignature pcm_pc_repository_pc_operationsignature) {
        this.pcm_pc_repository_pc_operationsignature = pcm_pc_repository_pc_operationsignature;
    }
    public pcm_pc_repository_pc_OperationProvidedRole getPcm_pc_repository_pc_operationprovidedrole() {
        return pcm_pc_repository_pc_operationprovidedrole;
    }

    public void setPcm_pc_repository_pc_operationprovidedrole(pcm_pc_repository_pc_OperationProvidedRole pcm_pc_repository_pc_operationprovidedrole) {
        this.pcm_pc_repository_pc_operationprovidedrole = pcm_pc_repository_pc_operationprovidedrole;
    }

}