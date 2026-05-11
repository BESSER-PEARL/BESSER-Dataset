





import java.util.List;
import java.util.ArrayList;

public class OperationInterface  {






    private pcm_pc_av_repository_pc_av_OperationSignature pcm_pc_av_repository_pc_av_operationsignature;




    private pcm_pc_av_repository_pc_av_OperationRequiredRole pcm_pc_av_repository_pc_av_operationrequiredrole;




    private pcm_pc_av_repository_pc_av_OperationProvidedRole pcm_pc_av_repository_pc_av_operationprovidedrole;


    public OperationInterface(
    ) {
    }



    public pcm_pc_av_repository_pc_av_OperationSignature getPcm_pc_av_repository_pc_av_operationsignature() {
        return pcm_pc_av_repository_pc_av_operationsignature;
    }

    public void setPcm_pc_av_repository_pc_av_operationsignature(pcm_pc_av_repository_pc_av_OperationSignature pcm_pc_av_repository_pc_av_operationsignature) {
        this.pcm_pc_av_repository_pc_av_operationsignature = pcm_pc_av_repository_pc_av_operationsignature;
    }
    public pcm_pc_av_repository_pc_av_OperationRequiredRole getPcm_pc_av_repository_pc_av_operationrequiredrole() {
        return pcm_pc_av_repository_pc_av_operationrequiredrole;
    }

    public void setPcm_pc_av_repository_pc_av_operationrequiredrole(pcm_pc_av_repository_pc_av_OperationRequiredRole pcm_pc_av_repository_pc_av_operationrequiredrole) {
        this.pcm_pc_av_repository_pc_av_operationrequiredrole = pcm_pc_av_repository_pc_av_operationrequiredrole;
    }
    public pcm_pc_av_repository_pc_av_OperationProvidedRole getPcm_pc_av_repository_pc_av_operationprovidedrole() {
        return pcm_pc_av_repository_pc_av_operationprovidedrole;
    }

    public void setPcm_pc_av_repository_pc_av_operationprovidedrole(pcm_pc_av_repository_pc_av_OperationProvidedRole pcm_pc_av_repository_pc_av_operationprovidedrole) {
        this.pcm_pc_av_repository_pc_av_operationprovidedrole = pcm_pc_av_repository_pc_av_operationprovidedrole;
    }

}