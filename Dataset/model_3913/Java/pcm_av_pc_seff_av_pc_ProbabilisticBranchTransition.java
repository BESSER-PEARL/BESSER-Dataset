





import java.util.List;
import java.util.ArrayList;

public class pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition extends AbstractBranchTransition {

    private float branchProbability;



    public pcm_av_pc_seff_av_pc_ProbabilisticBranchTransition(
        float branchProbability    ) {
        super(
        );
        this.branchProbability = branchProbability;
    }


    public float getBranchprobability() {
        return branchProbability;
    }

    public void setBranchprobability(float branchProbability) {
        this.branchProbability = branchProbability;
    }


}