





import java.util.List;
import java.util.ArrayList;

public class InfrastructureInterface  {






    private pcm_pc_av_repository_pc_av_InfrastructureRequiredRole pcm_pc_av_repository_pc_av_infrastructurerequiredrole;




    private pcm_pc_av_repository_pc_av_InfrastructureProvidedRole pcm_pc_av_repository_pc_av_infrastructureprovidedrole;




    private pcm_pc_av_repository_pc_av_InfrastructureSignature pcm_pc_av_repository_pc_av_infrastructuresignature;


    public InfrastructureInterface(
    ) {
    }



    public pcm_pc_av_repository_pc_av_InfrastructureRequiredRole getPcm_pc_av_repository_pc_av_infrastructurerequiredrole() {
        return pcm_pc_av_repository_pc_av_infrastructurerequiredrole;
    }

    public void setPcm_pc_av_repository_pc_av_infrastructurerequiredrole(pcm_pc_av_repository_pc_av_InfrastructureRequiredRole pcm_pc_av_repository_pc_av_infrastructurerequiredrole) {
        this.pcm_pc_av_repository_pc_av_infrastructurerequiredrole = pcm_pc_av_repository_pc_av_infrastructurerequiredrole;
    }
    public pcm_pc_av_repository_pc_av_InfrastructureProvidedRole getPcm_pc_av_repository_pc_av_infrastructureprovidedrole() {
        return pcm_pc_av_repository_pc_av_infrastructureprovidedrole;
    }

    public void setPcm_pc_av_repository_pc_av_infrastructureprovidedrole(pcm_pc_av_repository_pc_av_InfrastructureProvidedRole pcm_pc_av_repository_pc_av_infrastructureprovidedrole) {
        this.pcm_pc_av_repository_pc_av_infrastructureprovidedrole = pcm_pc_av_repository_pc_av_infrastructureprovidedrole;
    }
    public pcm_pc_av_repository_pc_av_InfrastructureSignature getPcm_pc_av_repository_pc_av_infrastructuresignature() {
        return pcm_pc_av_repository_pc_av_infrastructuresignature;
    }

    public void setPcm_pc_av_repository_pc_av_infrastructuresignature(pcm_pc_av_repository_pc_av_InfrastructureSignature pcm_pc_av_repository_pc_av_infrastructuresignature) {
        this.pcm_pc_av_repository_pc_av_infrastructuresignature = pcm_pc_av_repository_pc_av_infrastructuresignature;
    }

}