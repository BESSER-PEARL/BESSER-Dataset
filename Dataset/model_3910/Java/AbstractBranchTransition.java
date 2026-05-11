





import java.util.List;
import java.util.ArrayList;

public class AbstractBranchTransition  {






    private pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour pcm_pc_av_seff_pc_av_resourcedemandingbehaviour;




    private pcm_pc_av_seff_pc_av_BranchAction pcm_pc_av_seff_pc_av_branchaction;


    public AbstractBranchTransition(
    ) {
    }



    public pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour getPcm_pc_av_seff_pc_av_resourcedemandingbehaviour() {
        return pcm_pc_av_seff_pc_av_resourcedemandingbehaviour;
    }

    public void setPcm_pc_av_seff_pc_av_resourcedemandingbehaviour(pcm_pc_av_seff_pc_av_ResourceDemandingBehaviour pcm_pc_av_seff_pc_av_resourcedemandingbehaviour) {
        this.pcm_pc_av_seff_pc_av_resourcedemandingbehaviour = pcm_pc_av_seff_pc_av_resourcedemandingbehaviour;
    }
    public pcm_pc_av_seff_pc_av_BranchAction getPcm_pc_av_seff_pc_av_branchaction() {
        return pcm_pc_av_seff_pc_av_branchaction;
    }

    public void setPcm_pc_av_seff_pc_av_branchaction(pcm_pc_av_seff_pc_av_BranchAction pcm_pc_av_seff_pc_av_branchaction) {
        this.pcm_pc_av_seff_pc_av_branchaction = pcm_pc_av_seff_pc_av_branchaction;
    }

}