





import java.util.List;
import java.util.ArrayList;

public class InfrastructureInterface  {






    private pcm_av_pc_repository_av_pc_InfrastructureSignature pcm_av_pc_repository_av_pc_infrastructuresignature;




    private pcm_av_pc_repository_av_pc_InfrastructureProvidedRole pcm_av_pc_repository_av_pc_infrastructureprovidedrole;




    private pcm_av_pc_repository_av_pc_InfrastructureRequiredRole pcm_av_pc_repository_av_pc_infrastructurerequiredrole;


    public InfrastructureInterface(
    ) {
    }



    public pcm_av_pc_repository_av_pc_InfrastructureSignature getPcm_av_pc_repository_av_pc_infrastructuresignature() {
        return pcm_av_pc_repository_av_pc_infrastructuresignature;
    }

    public void setPcm_av_pc_repository_av_pc_infrastructuresignature(pcm_av_pc_repository_av_pc_InfrastructureSignature pcm_av_pc_repository_av_pc_infrastructuresignature) {
        this.pcm_av_pc_repository_av_pc_infrastructuresignature = pcm_av_pc_repository_av_pc_infrastructuresignature;
    }
    public pcm_av_pc_repository_av_pc_InfrastructureProvidedRole getPcm_av_pc_repository_av_pc_infrastructureprovidedrole() {
        return pcm_av_pc_repository_av_pc_infrastructureprovidedrole;
    }

    public void setPcm_av_pc_repository_av_pc_infrastructureprovidedrole(pcm_av_pc_repository_av_pc_InfrastructureProvidedRole pcm_av_pc_repository_av_pc_infrastructureprovidedrole) {
        this.pcm_av_pc_repository_av_pc_infrastructureprovidedrole = pcm_av_pc_repository_av_pc_infrastructureprovidedrole;
    }
    public pcm_av_pc_repository_av_pc_InfrastructureRequiredRole getPcm_av_pc_repository_av_pc_infrastructurerequiredrole() {
        return pcm_av_pc_repository_av_pc_infrastructurerequiredrole;
    }

    public void setPcm_av_pc_repository_av_pc_infrastructurerequiredrole(pcm_av_pc_repository_av_pc_InfrastructureRequiredRole pcm_av_pc_repository_av_pc_infrastructurerequiredrole) {
        this.pcm_av_pc_repository_av_pc_infrastructurerequiredrole = pcm_av_pc_repository_av_pc_infrastructurerequiredrole;
    }

}