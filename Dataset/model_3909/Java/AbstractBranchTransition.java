





import java.util.List;
import java.util.ArrayList;

public class AbstractBranchTransition  {






    private pcm_pc_seff_pc_BranchAction pcm_pc_seff_pc_branchaction;




    private pcm_pc_seff_pc_ResourceDemandingBehaviour pcm_pc_seff_pc_resourcedemandingbehaviour;


    public AbstractBranchTransition(
    ) {
    }



    public pcm_pc_seff_pc_BranchAction getPcm_pc_seff_pc_branchaction() {
        return pcm_pc_seff_pc_branchaction;
    }

    public void setPcm_pc_seff_pc_branchaction(pcm_pc_seff_pc_BranchAction pcm_pc_seff_pc_branchaction) {
        this.pcm_pc_seff_pc_branchaction = pcm_pc_seff_pc_branchaction;
    }
    public pcm_pc_seff_pc_ResourceDemandingBehaviour getPcm_pc_seff_pc_resourcedemandingbehaviour() {
        return pcm_pc_seff_pc_resourcedemandingbehaviour;
    }

    public void setPcm_pc_seff_pc_resourcedemandingbehaviour(pcm_pc_seff_pc_ResourceDemandingBehaviour pcm_pc_seff_pc_resourcedemandingbehaviour) {
        this.pcm_pc_seff_pc_resourcedemandingbehaviour = pcm_pc_seff_pc_resourcedemandingbehaviour;
    }

}