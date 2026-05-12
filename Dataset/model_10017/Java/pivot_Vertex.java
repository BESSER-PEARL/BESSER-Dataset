





import java.util.List;
import java.util.ArrayList;

public class pivot_Vertex extends NamedElement {






    private pivot_Region pivot_region;




    private pivot_Transition pivot_transition;




    private List<pivot_Transition> pivot_transitions;




    private pivot_Region pivot_region;




    private List<pivot_Transition> pivot_transitions;




    private pivot_Transition pivot_transition;


    public pivot_Vertex(
    ) {
        super(
        );
        this.pivot_transitions = new ArrayList<>();
        this.pivot_transitions = new ArrayList<>();
    }

    public pivot_Vertex(
        ArrayList<pivot_Transition> pivot_transitions,        ArrayList<pivot_Transition> pivot_transitions    ) {
        this.pivot_transitions = pivot_transitions;
        this.pivot_transitions = pivot_transitions;
    }


    public pivot_Region getPivot_region() {
        return pivot_region;
    }

    public void setPivot_region(pivot_Region pivot_region) {
        this.pivot_region = pivot_region;
    }
    public pivot_Transition getPivot_transition() {
        return pivot_transition;
    }

    public void setPivot_transition(pivot_Transition pivot_transition) {
        this.pivot_transition = pivot_transition;
    }
    public List<pivot_Transition> getPivot_transitions() {
        return pivot_transitions;
    }

    public void addPivot_transition(Pivot_transition pivot_transition) {
        this.pivot_transitions.add(pivot_transition);
    }
    public pivot_Region getPivot_region() {
        return pivot_region;
    }

    public void setPivot_region(pivot_Region pivot_region) {
        this.pivot_region = pivot_region;
    }
    public List<pivot_Transition> getPivot_transitions() {
        return pivot_transitions;
    }

    public void addPivot_transition(Pivot_transition pivot_transition) {
        this.pivot_transitions.add(pivot_transition);
    }
    public pivot_Transition getPivot_transition() {
        return pivot_transition;
    }

    public void setPivot_transition(pivot_Transition pivot_transition) {
        this.pivot_transition = pivot_transition;
    }

}