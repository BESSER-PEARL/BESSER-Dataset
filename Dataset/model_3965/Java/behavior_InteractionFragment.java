





import java.util.List;
import java.util.ArrayList;

public class behavior_InteractionFragment extends NamedElement {






    private List<behavior_Lifeline> behavior_lifelines;




    private behavior_Lifeline behavior_lifeline;


    public behavior_InteractionFragment(
    ) {
        super(
        );
        this.behavior_lifelines = new ArrayList<>();
    }

    public behavior_InteractionFragment(
        ArrayList<behavior_Lifeline> behavior_lifelines    ) {
        this.behavior_lifelines = behavior_lifelines;
    }


    public List<behavior_Lifeline> getBehavior_lifelines() {
        return behavior_lifelines;
    }

    public void addBehavior_lifeline(Behavior_lifeline behavior_lifeline) {
        this.behavior_lifelines.add(behavior_lifeline);
    }
    public behavior_Lifeline getBehavior_lifeline() {
        return behavior_lifeline;
    }

    public void setBehavior_lifeline(behavior_Lifeline behavior_lifeline) {
        this.behavior_lifeline = behavior_lifeline;
    }

}