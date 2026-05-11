





import java.util.List;
import java.util.ArrayList;

public class pcm_av_pc_usagemodel_av_pc_BranchTransition  {

    private float branchProbability;





    private ScenarioBehaviour scenariobehaviour;


    public pcm_av_pc_usagemodel_av_pc_BranchTransition(
        float branchProbability    ) {
        this.branchProbability = branchProbability;
    }


    public float getBranchprobability() {
        return branchProbability;
    }

    public void setBranchprobability(float branchProbability) {
        this.branchProbability = branchProbability;
    }

    public ScenarioBehaviour getScenariobehaviour() {
        return scenariobehaviour;
    }

    public void setScenariobehaviour(ScenarioBehaviour scenariobehaviour) {
        this.scenariobehaviour = scenariobehaviour;
    }

}