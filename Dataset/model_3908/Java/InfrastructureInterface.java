





import java.util.List;
import java.util.ArrayList;

public class InfrastructureInterface  {






    private pcm_av_repository_av_InfrastructureRequiredRole pcm_av_repository_av_infrastructurerequiredrole;




    private pcm_av_repository_av_InfrastructureProvidedRole pcm_av_repository_av_infrastructureprovidedrole;




    private pcm_av_repository_av_InfrastructureSignature pcm_av_repository_av_infrastructuresignature;


    public InfrastructureInterface(
    ) {
    }



    public pcm_av_repository_av_InfrastructureRequiredRole getPcm_av_repository_av_infrastructurerequiredrole() {
        return pcm_av_repository_av_infrastructurerequiredrole;
    }

    public void setPcm_av_repository_av_infrastructurerequiredrole(pcm_av_repository_av_InfrastructureRequiredRole pcm_av_repository_av_infrastructurerequiredrole) {
        this.pcm_av_repository_av_infrastructurerequiredrole = pcm_av_repository_av_infrastructurerequiredrole;
    }
    public pcm_av_repository_av_InfrastructureProvidedRole getPcm_av_repository_av_infrastructureprovidedrole() {
        return pcm_av_repository_av_infrastructureprovidedrole;
    }

    public void setPcm_av_repository_av_infrastructureprovidedrole(pcm_av_repository_av_InfrastructureProvidedRole pcm_av_repository_av_infrastructureprovidedrole) {
        this.pcm_av_repository_av_infrastructureprovidedrole = pcm_av_repository_av_infrastructureprovidedrole;
    }
    public pcm_av_repository_av_InfrastructureSignature getPcm_av_repository_av_infrastructuresignature() {
        return pcm_av_repository_av_infrastructuresignature;
    }

    public void setPcm_av_repository_av_infrastructuresignature(pcm_av_repository_av_InfrastructureSignature pcm_av_repository_av_infrastructuresignature) {
        this.pcm_av_repository_av_infrastructuresignature = pcm_av_repository_av_infrastructuresignature;
    }

}