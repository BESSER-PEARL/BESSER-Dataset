





import java.util.List;
import java.util.ArrayList;

public class cm_seff_ProbabilisticBranchTransition extends composition_Entity, seff_Automaton {

    private float branchProbability;



    public cm_seff_ProbabilisticBranchTransition(
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