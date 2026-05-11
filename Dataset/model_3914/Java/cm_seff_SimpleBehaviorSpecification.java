





import java.util.List;
import java.util.ArrayList;

public class cm_seff_SimpleBehaviorSpecification extends seff_ServiceEffectSpecification, seff_Automaton {






    private ProbabilisticBranchTransition probabilisticbranchtransition;


    public cm_seff_SimpleBehaviorSpecification(
    ) {
        super(
        );
    }



    public ProbabilisticBranchTransition getProbabilisticbranchtransition() {
        return probabilisticbranchtransition;
    }

    public void setProbabilisticbranchtransition(ProbabilisticBranchTransition probabilisticbranchtransition) {
        this.probabilisticbranchtransition = probabilisticbranchtransition;
    }

}