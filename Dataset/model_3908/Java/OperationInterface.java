





import java.util.List;
import java.util.ArrayList;

public class OperationInterface  {






    private pcm_av_repository_av_OperationSignature pcm_av_repository_av_operationsignature;




    private pcm_av_repository_av_OperationProvidedRole pcm_av_repository_av_operationprovidedrole;




    private pcm_av_repository_av_OperationRequiredRole pcm_av_repository_av_operationrequiredrole;


    public OperationInterface(
    ) {
    }



    public pcm_av_repository_av_OperationSignature getPcm_av_repository_av_operationsignature() {
        return pcm_av_repository_av_operationsignature;
    }

    public void setPcm_av_repository_av_operationsignature(pcm_av_repository_av_OperationSignature pcm_av_repository_av_operationsignature) {
        this.pcm_av_repository_av_operationsignature = pcm_av_repository_av_operationsignature;
    }
    public pcm_av_repository_av_OperationProvidedRole getPcm_av_repository_av_operationprovidedrole() {
        return pcm_av_repository_av_operationprovidedrole;
    }

    public void setPcm_av_repository_av_operationprovidedrole(pcm_av_repository_av_OperationProvidedRole pcm_av_repository_av_operationprovidedrole) {
        this.pcm_av_repository_av_operationprovidedrole = pcm_av_repository_av_operationprovidedrole;
    }
    public pcm_av_repository_av_OperationRequiredRole getPcm_av_repository_av_operationrequiredrole() {
        return pcm_av_repository_av_operationrequiredrole;
    }

    public void setPcm_av_repository_av_operationrequiredrole(pcm_av_repository_av_OperationRequiredRole pcm_av_repository_av_operationrequiredrole) {
        this.pcm_av_repository_av_operationrequiredrole = pcm_av_repository_av_operationrequiredrole;
    }

}