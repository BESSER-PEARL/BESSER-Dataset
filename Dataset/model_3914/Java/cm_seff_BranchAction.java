





import java.util.List;
import java.util.ArrayList;

public class cm_seff_BranchAction extends AbstractAction {






    private List<ProbabilisticBranchTransition> probabilisticbranchtransitions;


    public cm_seff_BranchAction(
    ) {
        super(
        );
        this.probabilisticbranchtransitions = new ArrayList<>();
    }

    public cm_seff_BranchAction(
        ArrayList<ProbabilisticBranchTransition> probabilisticbranchtransitions    ) {
        this.probabilisticbranchtransitions = probabilisticbranchtransitions;
    }


    public List<ProbabilisticBranchTransition> getProbabilisticbranchtransitions() {
        return probabilisticbranchtransitions;
    }

    public void addProbabilisticbranchtransition(Probabilisticbranchtransition probabilisticbranchtransition) {
        this.probabilisticbranchtransitions.add(probabilisticbranchtransition);
    }

}