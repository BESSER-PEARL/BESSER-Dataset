





import java.util.List;
import java.util.ArrayList;

public class InfrastructureInterface  {






    private pcm_pc_repository_pc_InfrastructureRequiredRole pcm_pc_repository_pc_infrastructurerequiredrole;




    private pcm_pc_repository_pc_InfrastructureProvidedRole pcm_pc_repository_pc_infrastructureprovidedrole;




    private pcm_pc_repository_pc_InfrastructureSignature pcm_pc_repository_pc_infrastructuresignature;


    public InfrastructureInterface(
    ) {
    }



    public pcm_pc_repository_pc_InfrastructureRequiredRole getPcm_pc_repository_pc_infrastructurerequiredrole() {
        return pcm_pc_repository_pc_infrastructurerequiredrole;
    }

    public void setPcm_pc_repository_pc_infrastructurerequiredrole(pcm_pc_repository_pc_InfrastructureRequiredRole pcm_pc_repository_pc_infrastructurerequiredrole) {
        this.pcm_pc_repository_pc_infrastructurerequiredrole = pcm_pc_repository_pc_infrastructurerequiredrole;
    }
    public pcm_pc_repository_pc_InfrastructureProvidedRole getPcm_pc_repository_pc_infrastructureprovidedrole() {
        return pcm_pc_repository_pc_infrastructureprovidedrole;
    }

    public void setPcm_pc_repository_pc_infrastructureprovidedrole(pcm_pc_repository_pc_InfrastructureProvidedRole pcm_pc_repository_pc_infrastructureprovidedrole) {
        this.pcm_pc_repository_pc_infrastructureprovidedrole = pcm_pc_repository_pc_infrastructureprovidedrole;
    }
    public pcm_pc_repository_pc_InfrastructureSignature getPcm_pc_repository_pc_infrastructuresignature() {
        return pcm_pc_repository_pc_infrastructuresignature;
    }

    public void setPcm_pc_repository_pc_infrastructuresignature(pcm_pc_repository_pc_InfrastructureSignature pcm_pc_repository_pc_infrastructuresignature) {
        this.pcm_pc_repository_pc_infrastructuresignature = pcm_pc_repository_pc_infrastructuresignature;
    }

}