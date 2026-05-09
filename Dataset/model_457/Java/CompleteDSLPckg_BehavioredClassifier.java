





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_BehavioredClassifier extends Classifier {






    private CompleteDSLPckg_Behavior completedslpckg_behavior;




    private List<CompleteDSLPckg_Behavior> completedslpckg_behaviors;




    private CompleteDSLPckg_Behavior completedslpckg_behavior;


    public CompleteDSLPckg_BehavioredClassifier(
    ) {
        super(
        );
        this.completedslpckg_behaviors = new ArrayList<>();
    }

    public CompleteDSLPckg_BehavioredClassifier(
        ArrayList<CompleteDSLPckg_Behavior> completedslpckg_behaviors    ) {
        this.completedslpckg_behaviors = completedslpckg_behaviors;
    }


    public CompleteDSLPckg_Behavior getCompletedslpckg_behavior() {
        return completedslpckg_behavior;
    }

    public void setCompletedslpckg_behavior(CompleteDSLPckg_Behavior completedslpckg_behavior) {
        this.completedslpckg_behavior = completedslpckg_behavior;
    }
    public List<CompleteDSLPckg_Behavior> getCompletedslpckg_behaviors() {
        return completedslpckg_behaviors;
    }

    public void addCompletedslpckg_behavior(Completedslpckg_behavior completedslpckg_behavior) {
        this.completedslpckg_behaviors.add(completedslpckg_behavior);
    }
    public CompleteDSLPckg_Behavior getCompletedslpckg_behavior() {
        return completedslpckg_behavior;
    }

    public void setCompletedslpckg_behavior(CompleteDSLPckg_Behavior completedslpckg_behavior) {
        this.completedslpckg_behavior = completedslpckg_behavior;
    }

}